"""Experimentos y verificaciones para matrices truncadas de Sobolev discretas.

Uso rápido:
    python3 "Plantilla TFM/scripts/sobolev_experiments.py" --n 8 --r1 1.0 --c1 0.0 --atoms 1.4 -1.6 --thresholds 1 1.1 1.5

Convención IMPORTANTÍSIMA:
- `--n=N` significa la sección truncada teórica `D_N`, de tamaño `(N+1) x (N+1)`.
- Para construir `D_N` hace falta ortonormalizar hasta grado `N+1`, porque `z phi_N`
  puede tener componente en `phi_{N+1}`.
- Esto corrige el corrimiento de índices de la versión anterior, que en la práctica
  devolvía `D_{N-1}` cuando el usuario pedía `--n=N`.
"""

from __future__ import annotations

import argparse
import json
import math
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Iterable, Sequence

import numpy as np


EPS = 1e-12


def parse_complex(value: str) -> complex:
    """Acepta complejos en sintaxis Python o reales simples."""
    return complex(value.replace("i", "j"))


def complex_to_json(value: complex) -> dict[str, float]:
    return {"real": float(np.real(value)), "imag": float(np.imag(value))}


def array_to_complex_json(values: Sequence[complex]) -> list[dict[str, float]]:
    return [complex_to_json(complex(value)) for value in values]


def homo(matrix: np.ndarray, a: complex, b: complex) -> np.ndarray:
    """Implementa el procedimiento Maple `homo`."""
    matrix = np.asarray(matrix, dtype=np.complex128)
    if matrix.ndim != 2 or matrix.shape[0] != matrix.shape[1]:
        raise ValueError("matrix debe ser cuadrada")

    n = matrix.shape[0]
    c = np.zeros((n, n), dtype=np.complex128)
    for i in range(n):
        for j in range(i, n):
            c[i, j] = math.comb(j, i) * (a ** i) * (b ** (j - i))

    return c.conj().T @ matrix @ c


def operador_d(vector: np.ndarray) -> np.ndarray:
    """Desplaza coeficientes como en el Maple `Operador_D`."""
    vector = np.asarray(vector, dtype=np.complex128)
    shifted = np.zeros_like(vector)
    shifted[1:] = vector[:-1]
    return shifted


def sobolev_gram_matrix(r1: complex, c1: complex, atoms: Sequence[complex], degree: int) -> np.ndarray:
    """Construye la matriz de Gram de Sobolev discreta hasta grado `degree`."""
    if degree < 0:
        raise ValueError("degree debe ser no negativo")

    identity = np.eye(degree + 1, dtype=np.complex128)
    m1 = homo(identity, r1, c1)
    m_atoms = np.zeros_like(m1)
    for atom in atoms:
        m_atoms += homo(identity, 0.0, atom)

    gram = np.zeros_like(m1)
    for i in range(degree + 1):
        for j in range(degree + 1):
            if i == 0 or j == 0:
                gram[i, j] = m1[i, j]
            else:
                gram[i, j] = m1[i, j] + i * j * m_atoms[i - 1, j - 1]
    return gram


def sobolev_inner_product(u: np.ndarray, v: np.ndarray, gram: np.ndarray) -> complex:
    """Producto interno u^* G v."""
    u = np.asarray(u, dtype=np.complex128)
    v = np.asarray(v, dtype=np.complex128)
    return np.vdot(u, gram @ v)


def gram_schmidt_sobolev(gram: np.ndarray) -> list[np.ndarray]:
    """Ortonormaliza la base monomial respecto del producto de Sobolev."""
    dim = gram.shape[0]
    basis = [np.eye(dim, dtype=np.complex128)[:, i] for i in range(dim)]
    orthonormal: list[np.ndarray] = []

    for vector in basis:
        current = vector.astype(np.complex128, copy=True)
        for prev in orthonormal:
            denom = sobolev_inner_product(prev, prev, gram)
            if abs(denom) < EPS:
                raise np.linalg.LinAlgError("Apareció un vector de norma casi nula en Gram-Schmidt")
            numer = sobolev_inner_product(prev, current, gram)
            current = current - (numer / denom) * prev

        norm_sq = sobolev_inner_product(current, current, gram)
        norm = math.sqrt(max(float(np.real_if_close(norm_sq)), 0.0))
        if norm < EPS:
            raise np.linalg.LinAlgError("La matriz de Gram no es definida positiva numéricamente")
        orthonormal.append(current / norm)

    return orthonormal


def section_matrix(orthonormal_basis: Sequence[np.ndarray], gram: np.ndarray, n: int) -> np.ndarray:
    """Construye la sección teórica `D_n`, de tamaño `(n+1) x (n+1)`."""
    if n < 0:
        raise ValueError("n debe ser no negativo")
    if len(orthonormal_basis) < n + 2:
        raise ValueError("Hace falta base ortonormal hasta grado n+1 para construir D_n")

    matrix = np.zeros((n + 1, n + 1), dtype=np.complex128)
    for i in range(n + 1):
        for j in range(n + 1):
            matrix[i, j] = sobolev_inner_product(operador_d(orthonormal_basis[j]), orthonormal_basis[i], gram)
    return matrix


def polynomial_coefficients_desc(vector: np.ndarray) -> np.ndarray:
    """Convierte coeficientes ascendentes en descendentes."""
    return np.asarray(vector[::-1], dtype=np.complex128)


def normalize_polynomial(coeffs: np.ndarray) -> np.ndarray:
    coeffs = np.asarray(coeffs, dtype=np.complex128)
    nz = np.flatnonzero(np.abs(coeffs) > EPS)
    if nz.size == 0:
        raise ValueError("polinomio nulo")
    coeffs = coeffs[nz[0] :]
    return coeffs / coeffs[0]


def sort_complex(values: Sequence[complex]) -> np.ndarray:
    arr = np.asarray(values, dtype=np.complex128)
    if arr.size == 0:
        return arr
    order = np.lexsort((np.round(arr.imag, 12), np.round(arr.real, 12)))
    return arr[order]


@dataclass
class SpectralSnapshot:
    n: int
    max_eig_modulus: float
    max_singular_value: float
    second_singular_value: float | None
    third_singular_value: float | None
    eigenvalues: np.ndarray
    singular_values: np.ndarray


@dataclass
class HessenbergVerification:
    passed: bool
    max_forbidden_entry: float


@dataclass
class CharpolyVerification:
    passed: bool
    scale_factor: dict[str, float]
    max_coefficient_error: float


@dataclass
class EigenvalueZeroVerification:
    passed: bool
    max_root_distance: float


@dataclass
class WeylHornVerification:
    passed: bool
    max_product_excess: float
    count_violations: list[float]


def spectral_snapshot(matrix: np.ndarray, n: int) -> SpectralSnapshot:
    """Extrae autovalores y valores singulares de `D_n`."""
    eigenvalues = np.linalg.eigvals(matrix)
    singular_values = np.linalg.svd(matrix, compute_uv=False)
    singular_values = np.sort(np.real_if_close(singular_values).astype(float))[::-1]

    max_eig_modulus = float(np.max(np.abs(eigenvalues))) if eigenvalues.size else 0.0
    max_sv = float(singular_values[0]) if singular_values.size else 0.0
    sec_sv = float(singular_values[1]) if singular_values.size >= 2 else None
    thrd_sv = float(singular_values[2]) if singular_values.size >= 3 else None

    return SpectralSnapshot(
        n=n,
        max_eig_modulus=max_eig_modulus,
        max_singular_value=max_sv,
        second_singular_value=sec_sv,
        third_singular_value=thrd_sv,
        eigenvalues=eigenvalues,
        singular_values=singular_values,
    )


def threshold_counts(values: Iterable[complex | float], thresholds: Sequence[float], use_modulus: bool = True, strict: bool = True) -> dict[float, int]:
    """Cuenta cuántos valores superan cada umbral.

    Para Weyl--Horn la desigualdad correcta usa `>` y NO `>=`.
    """
    arr = np.asarray(list(values))
    magnitudes = np.abs(arr) if use_modulus else np.real(arr)
    if strict:
        return {threshold: int(np.count_nonzero(magnitudes > threshold)) for threshold in thresholds}
    return {threshold: int(np.count_nonzero(magnitudes >= threshold)) for threshold in thresholds}


def gram_diagnostics(gram: np.ndarray) -> list[tuple[int, float, float]]:
    """Replica las columnas c_nn y nth_c_nn impresas en el Maple."""
    diag = np.real_if_close(np.diag(gram)).astype(float)
    out: list[tuple[int, float, float]] = []
    for i in range(1, len(diag)):
        ratio = float(diag[i] / diag[i - 1])
        root = float(diag[i - 1] ** (1.0 / i))
        out.append((i, ratio, root))
    return out


def verify_hessenberg(matrix: np.ndarray, tol: float = 1e-9) -> HessenbergVerification:
    forbidden = np.tril(matrix, k=-2)
    max_forbidden = float(np.max(np.abs(forbidden))) if forbidden.size else 0.0
    return HessenbergVerification(passed=max_forbidden <= tol, max_forbidden_entry=max_forbidden)


def verify_charpoly_truncada(matrix: np.ndarray, phi_coeffs_asc: np.ndarray, tol: float = 1e-8) -> CharpolyVerification:
    charpoly = normalize_polynomial(np.poly(matrix.T))
    polynomial = normalize_polynomial(polynomial_coefficients_desc(phi_coeffs_asc))
    if charpoly.shape != polynomial.shape:
        raise ValueError("charpoly y phi_{n+1} tienen grados incompatibles")
    max_error = float(np.max(np.abs(charpoly - polynomial)))
    scale = np.poly(matrix.T)[0] / polynomial_coefficients_desc(phi_coeffs_asc)[0]
    return CharpolyVerification(
        passed=max_error <= tol,
        scale_factor=complex_to_json(complex(scale)),
        max_coefficient_error=max_error,
    )


def verify_eigenvalues_match_zeros(matrix: np.ndarray, phi_coeffs_asc: np.ndarray, tol: float = 1e-8) -> EigenvalueZeroVerification:
    eigenvalues = sort_complex(np.linalg.eigvals(matrix.T))
    zeros = sort_complex(np.roots(polynomial_coefficients_desc(phi_coeffs_asc)))
    max_distance = float(np.max(np.abs(eigenvalues - zeros))) if eigenvalues.size else 0.0
    return EigenvalueZeroVerification(passed=max_distance <= tol, max_root_distance=max_distance)


def verify_weyl_horn(matrix: np.ndarray, thresholds: Sequence[float], tol: float = 1e-9) -> WeylHornVerification:
    eigenvalues = np.asarray(np.linalg.eigvals(matrix), dtype=np.complex128)
    singular_values = np.asarray(np.linalg.svd(matrix, compute_uv=False), dtype=float)
    eig_moduli = np.sort(np.abs(eigenvalues))[::-1]
    singular_values = np.sort(singular_values)[::-1]

    max_excess = 0.0
    for k in range(1, len(eig_moduli) + 1):
        lhs = float(np.prod(eig_moduli[:k]))
        rhs = float(np.prod(singular_values[:k]))
        max_excess = max(max_excess, lhs - rhs)

    count_violations: list[float] = []
    eig_counts = threshold_counts(eigenvalues, thresholds, use_modulus=True, strict=True)
    sig_counts = threshold_counts(singular_values, thresholds, use_modulus=False, strict=True)
    for threshold in thresholds:
        if eig_counts[threshold] > sig_counts[threshold]:
            count_violations.append(float(threshold))

    return WeylHornVerification(
        passed=max_excess <= tol and not count_violations,
        max_product_excess=float(max_excess),
        count_violations=count_violations,
    )


def run_experiment(r1: complex, c1: complex, atoms: Sequence[complex], n: int, thresholds: Sequence[float]) -> dict[str, object]:
    """Ejecuta el experimento principal para la sección teórica `D_n`."""
    gram = sobolev_gram_matrix(r1=r1, c1=c1, atoms=atoms, degree=n + 1)
    orthonormal_basis = gram_schmidt_sobolev(gram)
    truncation = section_matrix(orthonormal_basis, gram, n=n)
    phi_next = orthonormal_basis[n + 1]
    snapshot = spectral_snapshot(truncation, n=n)

    threshold_report = {
        "strict_eigenvalue_counts": threshold_counts(snapshot.eigenvalues, thresholds, use_modulus=True, strict=True),
        "strict_singular_value_counts": threshold_counts(snapshot.singular_values, thresholds, use_modulus=False, strict=True),
        "nonstrict_eigenvalue_counts": threshold_counts(snapshot.eigenvalues, thresholds, use_modulus=True, strict=False),
        "nonstrict_singular_value_counts": threshold_counts(snapshot.singular_values, thresholds, use_modulus=False, strict=False),
    }

    return {
        "n": n,
        "construction_degree": n + 1,
        "gram": gram,
        "orthonormal_basis": orthonormal_basis,
        "phi_next_coefficients": phi_next,
        "truncation_matrix": truncation,
        "snapshot": snapshot,
        "gram_diagnostics": gram_diagnostics(gram),
        "threshold_report": threshold_report,
        "verifications": {
            "prop:hessenberg": verify_hessenberg(truncation),
            "prop:charpoly_truncada": verify_charpoly_truncada(truncation, phi_next),
            "prop:autovalores_ceros": verify_eigenvalues_match_zeros(truncation, phi_next),
            "lem:weyl_horn": verify_weyl_horn(truncation, thresholds),
        },
    }


def serialize_results(results: dict[str, object]) -> dict[str, object]:
    snapshot: SpectralSnapshot = results["snapshot"]  # type: ignore[assignment]
    verifications = results["verifications"]  # type: ignore[assignment]
    truncation: np.ndarray = results["truncation_matrix"]  # type: ignore[assignment]
    phi_next: np.ndarray = results["phi_next_coefficients"]  # type: ignore[assignment]

    return {
        "n": results["n"],
        "construction_degree": results["construction_degree"],
        "indexing_note": "--n=N construye la sección teórica D_N; internamente se ortonormaliza hasta grado N+1.",
        "truncation_shape": list(truncation.shape),
        "phi_next_coefficients_ascending": array_to_complex_json(phi_next),
        "eigenvalues": array_to_complex_json(snapshot.eigenvalues),
        "singular_values": [float(x) for x in snapshot.singular_values],
        "snapshot": {
            "n": snapshot.n,
            "max_eig_modulus": snapshot.max_eig_modulus,
            "max_singular_value": snapshot.max_singular_value,
            "second_singular_value": snapshot.second_singular_value,
            "third_singular_value": snapshot.third_singular_value,
        },
        "gram_diagnostics": [
            {"index": i, "c_nn_ratio": ratio, "nth_c_nn": root}
            for i, ratio, root in results["gram_diagnostics"]  # type: ignore[index]
        ],
        "threshold_report": results["threshold_report"],
        "verifications": {name: asdict(value) for name, value in verifications.items()},
    }


def _format_optional(value: float | None) -> str:
    return "-" if value is None else f"{value:.5e}"


def _print_main_table(results: dict[str, object]) -> None:
    snapshot: SpectralSnapshot = results["snapshot"]  # type: ignore[assignment]
    diagnostics: list[tuple[int, float, float]] = results["gram_diagnostics"]  # type: ignore[assignment]
    _, ratio, root = diagnostics[-1]

    print("\n--- Resultados de Sobolev ---")
    print("Convención: --n=N produce la sección teórica D_N (tamaño (N+1)x(N+1)).")
    print(f"{'n':>3} {'max_eigs':>15} {'max_sings':>15} {'sec_sings':>15} {'thrd_sings':>15} {'c_nn':>15} {'nth_c_nn':>15}")
    print(
        f"{snapshot.n:>3d} "
        f"{snapshot.max_eig_modulus:>15.5e} "
        f"{snapshot.max_singular_value:>15.5e} "
        f"{_format_optional(snapshot.second_singular_value):>15} "
        f"{_format_optional(snapshot.third_singular_value):>15} "
        f"{ratio:>15.5e} "
        f"{root:>15.5e}"
    )


def _print_threshold_report(results: dict[str, object], thresholds: Sequence[float]) -> None:
    report: dict[str, dict[float, int]] = results["threshold_report"]  # type: ignore[assignment]
    print("\n--- Conteos por umbral ---")
    print("Versión correcta para Weyl--Horn: conteos con > tau.")
    for threshold in thresholds:
        print(
            f"  tau={threshold:g}: "
            f"#{'{'}|lambda|>tau{'}'}={report['strict_eigenvalue_counts'][threshold]}, "
            f"#{'{'}s>tau{'}'}={report['strict_singular_value_counts'][threshold]}"
        )


def _print_verification_report(results: dict[str, object]) -> None:
    verifications = results["verifications"]  # type: ignore[assignment]
    print("\n--- Verificaciones internas ---")
    for name, verification in verifications.items():
        status = "OK" if verification.passed else "FALLÓ"
        print(f"- {name}: {status}")
        for key, value in asdict(verification).items():
            if key == "passed":
                continue
            print(f"    {key}: {value}")


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--n", type=int, default=8, help="índice teórico de la sección D_n; la matriz resultante es de tamaño (n+1)x(n+1)")
    parser.add_argument("--r1", type=parse_complex, default=1.0, help="parámetro r1 del Maple")
    parser.add_argument("--c1", type=parse_complex, default=0.0, help="parámetro c1 del Maple")
    parser.add_argument(
        "--atoms",
        type=parse_complex,
        nargs="*",
        default=[],
        help="lista de átomos discretos (complejos en sintaxis Python)",
    )
    parser.add_argument(
        "--thresholds",
        type=float,
        nargs="*",
        default=[1.0, 1.1, 1.5],
        help="umbrales para comparar conteos de autovalores y valores singulares",
    )
    parser.add_argument(
        "--show-matrix",
        action="store_true",
        help="imprime también la matriz truncada completa",
    )
    parser.add_argument(
        "--json-output",
        type=Path,
        help="si se pasa, guarda una salida JSON reproducible",
    )
    return parser


def main() -> None:
    args = build_parser().parse_args()
    results = run_experiment(r1=args.r1, c1=args.c1, atoms=args.atoms, n=args.n, thresholds=args.thresholds)

    _print_main_table(results)
    _print_threshold_report(results, args.thresholds)
    _print_verification_report(results)

    if args.show_matrix:
        print("\n--- Matriz truncada del operador de multiplicación ---")
        print(results["truncation_matrix"])

    if args.json_output is not None:
        args.json_output.parent.mkdir(parents=True, exist_ok=True)
        args.json_output.write_text(json.dumps(serialize_results(results), indent=2, ensure_ascii=False), encoding="utf-8")
        print(f"\nJSON guardado en: {args.json_output}")


if __name__ == "__main__":
    main()
