"""Batería reproducible de verificaciones para el capítulo 3 del TFM.

Separa explícitamente:
- verificaciones directas sobre identidades algebraicas finitas;
- evidencia experimental fuerte para fenómenos asintóticos.
"""

from __future__ import annotations

import argparse
import json
from dataclasses import dataclass
from pathlib import Path
from typing import Sequence

import numpy as np

from verify_chapters4_5 import experimental_singular_threshold


EPS = 1e-10


@dataclass(frozen=True)
class Scenario:
    radius_R: float
    atoms_out: tuple[complex, ...]
    atoms_in: tuple[complex, ...] = ()

    @property
    def atoms_all(self) -> tuple[complex, ...]:
        return self.atoms_out + self.atoms_in

    @property
    def m(self) -> int:
        return len(self.atoms_out)


def complex_to_json(value: complex) -> dict[str, float]:
    return {"real": float(np.real(value)), "imag": float(np.imag(value))}


def array_to_complex_json(values: Sequence[complex]) -> list[dict[str, float]]:
    return [complex_to_json(complex(value)) for value in values]


def monomial_coeffs(degree: int, scale: complex = 1.0) -> np.ndarray:
    coeffs = np.zeros(degree + 1, dtype=np.complex128)
    coeffs[degree] = scale
    return coeffs


def poly_eval(coeffs: np.ndarray, z: complex) -> complex:
    powers = z ** np.arange(coeffs.size)
    return complex(np.dot(coeffs, powers))


def poly_derivative_eval(coeffs: np.ndarray, z: complex) -> complex:
    if coeffs.size <= 1:
        return 0.0 + 0.0j
    degrees = np.arange(1, coeffs.size)
    return complex(np.dot(degrees * coeffs[1:], z ** (degrees - 1)))


def psi_eval(coeffs: np.ndarray, c: complex) -> complex:
    return poly_eval(coeffs, c) + c * poly_derivative_eval(coeffs, c)


def multiply_by_z(coeffs: np.ndarray) -> np.ndarray:
    out = np.zeros(coeffs.size + 1, dtype=np.complex128)
    out[1:] = coeffs
    return out


def gram_matrix(radius_R: float, atoms: Sequence[complex], degree: int) -> np.ndarray:
    gram = np.zeros((degree + 1, degree + 1), dtype=np.complex128)
    for i in range(degree + 1):
        gram[i, i] += radius_R ** (2 * i)
    for atom in atoms:
        for i in range(1, degree + 1):
            for j in range(1, degree + 1):
                gram[i, j] += i * j * (atom ** (i - 1)) * np.conj(atom) ** (j - 1)
    return gram


def sobolev_norm_sq(coeffs: np.ndarray, radius_R: float, atoms: Sequence[complex]) -> float:
    gram = gram_matrix(radius_R=radius_R, atoms=atoms, degree=coeffs.size - 1)
    value = np.vdot(coeffs, gram @ coeffs)
    return float(np.real_if_close(value))


def nullspace(matrix: np.ndarray, tol: float = EPS) -> np.ndarray:
    _, singular_values, vh = np.linalg.svd(matrix)
    rank = int(np.sum(singular_values > tol))
    return vh[rank:].conj().T


def generalized_max_eigenvalue(a: np.ndarray, b: np.ndarray) -> float:
    if a.size == 0:
        return 0.0
    eigvals_b, eigvecs_b = np.linalg.eigh(b)
    keep = eigvals_b > EPS
    if not np.any(keep):
        return 0.0
    whitening = eigvecs_b[:, keep] @ np.diag(1.0 / np.sqrt(eigvals_b[keep]))
    reduced = whitening.conj().T @ a @ whitening
    return float(np.max(np.linalg.eigvalsh(reduced)).real)


def psi_matrix(atoms_out: Sequence[complex], degree: int) -> np.ndarray:
    powers = np.arange(degree + 1)
    return np.array([[(j + 1) * (atom ** j) for j in powers] for atom in atoms_out], dtype=np.complex128)


def value_row(atom: complex, degree: int) -> np.ndarray:
    return np.array([atom ** j for j in range(degree + 1)], dtype=np.complex128)


def derivative_row(atom: complex, degree: int) -> np.ndarray:
    row = np.zeros(degree + 1, dtype=np.complex128)
    for j in range(1, degree + 1):
        row[j] = j * atom ** (j - 1)
    return row


def restricted_operator_norm_sq(radius_R: float, atoms: Sequence[complex], atoms_out: Sequence[complex], degree: int) -> float:
    basis = nullspace(psi_matrix(atoms_out=atoms_out, degree=degree))
    gram_in = gram_matrix(radius_R=radius_R, atoms=atoms, degree=degree)
    gram_out = gram_matrix(radius_R=radius_R, atoms=atoms, degree=degree + 1)
    shift = np.zeros((degree + 2, degree + 1), dtype=np.complex128)
    shift[1:, :] = np.eye(degree + 1, dtype=np.complex128)
    a = basis.conj().T @ shift.conj().T @ gram_out @ shift @ basis
    b = basis.conj().T @ gram_in @ basis
    return generalized_max_eigenvalue(a, b)


def finite_dimensional_E_report(scenario: Scenario, degree: int) -> dict[str, object]:
    basis = nullspace(psi_matrix(atoms_out=scenario.atoms_out, degree=degree))
    gram_in = gram_matrix(radius_R=scenario.radius_R, atoms=scenario.atoms_all, degree=degree)
    gram_out = gram_matrix(radius_R=scenario.radius_R, atoms=scenario.atoms_all, degree=degree + 1)
    shift = np.zeros((degree + 2, degree + 1), dtype=np.complex128)
    shift[1:, :] = np.eye(degree + 1, dtype=np.complex128)
    gram_v = basis.conj().T @ gram_in @ basis
    op_v = basis.conj().T @ shift.conj().T @ gram_out @ shift @ basis

    representers: list[np.ndarray] = []
    functional_norms: dict[str, float] = {}
    for index, atom in enumerate(scenario.atoms_all, start=1):
        row = derivative_row(atom=atom, degree=degree) @ basis
        rhs = np.conj(row).T
        representer = np.linalg.solve(gram_v, rhs)
        representers.append(representer)
        functional_norms[f"ell_{index}"] = float(np.sqrt(max(np.real_if_close(np.vdot(representer, gram_v @ representer)), 0.0)))

    for atom in scenario.atoms_in:
        row = (value_row(atom=atom, degree=degree) + atom * derivative_row(atom=atom, degree=degree)) @ basis
        rhs = np.conj(row).T
        representer = np.linalg.solve(gram_v, rhs)
        representers.append(representer)
        label = f"eta_{complex_to_json(atom)}"
        functional_norms[label] = float(np.sqrt(max(np.real_if_close(np.vdot(representer, gram_v @ representer)), 0.0)))

    if representers:
        matrix_e = np.column_stack(representers)
        q_e, _ = np.linalg.qr(matrix_e)
        gram_q = q_e.conj().T @ gram_v @ q_e
        op_q = q_e.conj().T @ op_v @ q_e
        lambda_e = generalized_max_eigenvalue(op_q, gram_q)
    else:
        lambda_e = 0.0

    lambda_full = generalized_max_eigenvalue(op_v, gram_v)
    predicted = max(scenario.radius_R**2, lambda_e)
    return {
        "scenario": {
            "radius_R": scenario.radius_R,
            "atoms_out": array_to_complex_json(scenario.atoms_out),
            "atoms_in": array_to_complex_json(scenario.atoms_in),
            "degree": degree,
        },
        "lambda_full": lambda_full,
        "lambda_E": lambda_e,
        "predicted_max": predicted,
        "difference": abs(lambda_full - predicted),
        "functional_norms": functional_norms,
    }


def verify_derivative_nonboundedness() -> dict[str, object]:
    rows_strict = []
    rows_boundary = []
    radius_R = 1.0
    c_strict = 1.4
    c_boundary = 1.0
    for n in [2, 4, 8, 12, 16, 20]:
        coeffs_strict = monomial_coeffs(n, scale=radius_R ** (-n))
        coeffs_boundary = monomial_coeffs(n, scale=radius_R ** (-n))
        rows_strict.append(
            {
                "n": n,
                "norm_L2": sobolev_norm_sq(coeffs_strict, radius_R=radius_R, atoms=[]),
                "abs_delta_prime_c": abs(poly_derivative_eval(coeffs_strict, c_strict)),
                "formula": (n / radius_R) * (abs(c_strict) / radius_R) ** (n - 1),
            }
        )
        rows_boundary.append(
            {
                "n": n,
                "norm_L2": sobolev_norm_sq(coeffs_boundary, radius_R=radius_R, atoms=[]),
                "abs_delta_prime_c": abs(poly_derivative_eval(coeffs_boundary, c_boundary)),
                "formula": n / radius_R,
            }
        )

    return {
        "strict_exterior": {
            "c": c_strict,
            "rows": rows_strict,
            "trend": "|p_n'(c)| crece exponencialmente con ||p_n||_{L2}=1.",
        },
        "boundary": {
            "c": c_boundary,
            "rows": rows_boundary,
            "trend": "|p_n'(c)| = n/R crece linealmente con ||p_n||_{L2}=1.",
        },
        "interpretation": "EVIDENCIA EXPERIMENTAL fuerte para lem:no_acotacion_derivada_exterior_lebesgue; la no acotación infinita no puede certificarse solo con cálculo finito.",
    }


def verify_exterior_model_nonboundedness() -> dict[str, object]:
    radius_R = 1.0
    atoms = [1.4]
    rows_strict = []
    for n in [2, 4, 8, 12, 16]:
        coeffs = np.zeros(n + 2, dtype=np.complex128)
        coeffs[n] = (n + 1) * atoms[0]
        coeffs[n + 1] = -n
        norm_sq = sobolev_norm_sq(coeffs, radius_R=radius_R, atoms=atoms)
        rows_strict.append(
            {
                "n": n,
                "Qn_prime_c": complex_to_json(poly_derivative_eval(coeffs, atoms[0])),
                "psi_c_Qn": complex_to_json(psi_eval(coeffs, atoms[0])),
                "norm_sq": norm_sq,
                "ratio_sq": abs(psi_eval(coeffs, atoms[0])) ** 2 / norm_sq,
            }
        )

    c = 1.0
    rows_boundary = []
    for n in [2, 4, 8, 12, 16, 24]:
        alpha_n = 3.0 / (2 * n + 1)
        coeffs = np.array([(1 - alpha_n * k) / (c**k) for k in range(n + 1)], dtype=np.complex128)
        norm_sq = sobolev_norm_sq(coeffs, radius_R=radius_R, atoms=[c])
        rows_boundary.append(
            {
                "n": n,
                "Pn_prime_c": complex_to_json(poly_derivative_eval(coeffs, c)),
                "psi_c_Pn": complex_to_json(psi_eval(coeffs, c)),
                "norm_sq": norm_sq,
                "ratio_sq": abs(psi_eval(coeffs, c)) ** 2 / norm_sq,
            }
        )

    return {
        "strict_exterior_case": rows_strict,
        "boundary_case": rows_boundary,
        "interpretation": "EVIDENCIA EXPERIMENTAL fuerte para prop:no_acotacion_modelo_exterior: las sucesiones explícitas del manuscrito reproducen Q_n'(c)=0 o P_n'(c)=0 y muestran crecimiento del cociente |psi_c(p_n)|^2 / ||p_n||_S^2.",
    }


def verify_independence_and_codimension(scenario: Scenario, degree: int) -> dict[str, object]:
    matrix = psi_matrix(atoms_out=scenario.atoms_out, degree=degree)
    singular_values = np.linalg.svd(matrix, compute_uv=False)
    rank = int(np.sum(singular_values > EPS))
    nullity = (degree + 1) - rank
    return {
        "scenario": {
            "radius_R": scenario.radius_R,
            "atoms_out": array_to_complex_json(scenario.atoms_out),
            "degree": degree,
        },
        "psi_matrix_shape": list(matrix.shape),
        "rank": rank,
        "expected_rank": scenario.m,
        "nullity": nullity,
        "expected_nullity": degree + 1 - scenario.m,
        "smallest_singular_value": float(singular_values[-1]),
    }


def annihilator_truncated_report(scenario: Scenario, degree_bound: int) -> dict[str, object]:
    a_out = np.array([1.0 + 0.0j])
    for atom in scenario.atoms_out:
        a_out = np.polynomial.polynomial.polymul(a_out, np.array([atom**2, -2 * atom, 1.0], dtype=np.complex128))

    inclusion_rows = []
    for q_degree in range(0, max(degree_bound - len(a_out) + 2, 1)):
        candidate = np.polynomial.polynomial.polymul(a_out, monomial_coeffs(q_degree))
        inclusion_rows.append(
            {
                "q_degree": q_degree,
                "psi_values": [complex_to_json(psi_eval(candidate, atom)) for atom in scenario.atoms_out],
            }
        )

    rows = []
    for atom in scenario.atoms_out:
        rows.append(psi_matrix([atom], degree_bound)[0])
        shifted = np.polynomial.polynomial.polymul(np.array([-atom, 1.0], dtype=np.complex128), np.eye(degree_bound + 1, dtype=np.complex128)[0])
        del shifted
        rows.append(atom * value_row(atom, degree_bound))
    constraint_matrix = np.vstack(rows)
    solution_basis = nullspace(constraint_matrix)

    multiples = []
    max_q_degree = degree_bound - (len(a_out) - 1)
    if max_q_degree >= 0:
        for q_degree in range(max_q_degree + 1):
            product = np.polynomial.polynomial.polymul(a_out, monomial_coeffs(q_degree))
            padded = np.pad(product, (0, degree_bound + 1 - product.size))
            multiples.append(padded)
    multiples_matrix = np.column_stack(multiples) if multiples else np.zeros((degree_bound + 1, 0), dtype=np.complex128)
    combined_rank = int(np.linalg.matrix_rank(np.hstack([solution_basis, multiples_matrix]), tol=EPS))

    return {
        "scenario": {
            "atoms_out": array_to_complex_json(scenario.atoms_out),
            "degree_bound": degree_bound,
        },
        "A_out_coefficients_ascending": array_to_complex_json(a_out),
        "direct_inclusion_checks": inclusion_rows,
        "truncated_solution_dimension": int(solution_basis.shape[1]),
        "expected_solution_dimension": max_q_degree + 1 if max_q_degree >= 0 else 0,
        "multiples_dimension": int(multiples_matrix.shape[1]),
        "combined_rank": combined_rank,
        "expected_combined_rank": int(multiples_matrix.shape[1]),
    }


def pre_threshold_q1_report(radius_R: float, c: complex, max_degree: int) -> dict[str, object]:
    rows = []
    for degree in range(2, max_degree + 1):
        norm_sq = restricted_operator_norm_sq(radius_R=radius_R, atoms=[c], atoms_out=[c], degree=degree)
        rows.append({"degree": degree, "restricted_norm": float(np.sqrt(max(norm_sq, 0.0)))})
    return {
        "scenario": {"radius_R": radius_R, "c": complex_to_json(c)},
        "rows": rows,
        "max_restricted_norm": max(row["restricted_norm"] for row in rows),
        "interpretation": "EVIDENCIA finita para prop:lebesgue_pre_umbral_Qk: sobre truncaciones de ker(psi_c), la norma restringida se mantiene en R dentro del error numérico.",
    }


def vout_boundedness_report(scenario: Scenario, min_degree: int, max_degree: int) -> dict[str, object]:
    rows = []
    for degree in range(min_degree, max_degree + 1):
        norm_sq = restricted_operator_norm_sq(
            radius_R=scenario.radius_R,
            atoms=scenario.atoms_all,
            atoms_out=scenario.atoms_out,
            degree=degree,
        )
        rows.append({"degree": degree, "restricted_norm": float(np.sqrt(max(norm_sq, 0.0)))})
    return {
        "scenario": {
            "radius_R": scenario.radius_R,
            "atoms_out": array_to_complex_json(scenario.atoms_out),
            "atoms_in": array_to_complex_json(scenario.atoms_in),
        },
        "rows": rows,
        "max_restricted_norm": max(row["restricted_norm"] for row in rows),
        "interpretation": "EVIDENCIA EXPERIMENTAL para lem:vout_acotacion: las normas restringidas en V_out ∩ P_n permanecen acotadas en el rango computado.",
    }


def stabilization_reports(n_min: int, n_max: int) -> tuple[dict[str, object], dict[str, object]]:
    base = experimental_singular_threshold(n_min=n_min, n_max=n_max, thresholds=[1.0, 1.02, 1.05, 1.1, 1.25])
    stabilization = {
        **base,
        "interpretation": "EVIDENCIA EXPERIMENTAL reutilizada del capítulo 4: para m=2, sigma_0,n y sigma_1,n crecen mientras sigma_2,n se mantiene cerca de R=1 en el rango computado.",
    }
    exactitud = {
        **base,
        "interpretation": "EVIDENCIA EXPERIMENTAL reutilizada de capítulos 4--5 para thm:exactitud_Qm_R: el valor singular de índice m=2 permanece numéricamente cerca de R=1, pero esto NO reemplaza la prueba exacta de Q_m(D)=R.",
    }
    return stabilization, exactitud


def build_report(output_dir: Path, n_min: int, n_max: int) -> dict[str, object]:
    pure_exterior = Scenario(radius_R=1.0, atoms_out=(1.4, -1.6))
    mixed = Scenario(radius_R=1.0, atoms_out=(1.4, -1.6), atoms_in=(0.25,))
    stabilization_report, exactitud_report = stabilization_reports(n_min=n_min, n_max=n_max)
    direct = {
        "lem:independencia_funcionales_psi": verify_independence_and_codimension(pure_exterior, degree=5),
        "lem:vout_codimension": verify_independence_and_codimension(pure_exterior, degree=8),
        "thm:Vout_anulador": annihilator_truncated_report(pure_exterior, degree_bound=10),
    }
    experimental = {
        "lem:no_acotacion_derivada_exterior_lebesgue": verify_derivative_nonboundedness(),
        "prop:no_acotacion_modelo_exterior": verify_exterior_model_nonboundedness(),
        "prop:lebesgue_pre_umbral_Qk": pre_threshold_q1_report(radius_R=1.0, c=1.4, max_degree=16),
        "lem:vout_acotacion": vout_boundedness_report(mixed, min_degree=4, max_degree=18),
        "thm:estabilizacion_Qm": stabilization_report,
        "thm:exactitud_Qm_R": exactitud_report,
        "thm:caracterizacion_finita_vout_mixto": finite_dimensional_E_report(mixed, degree=12),
    }
    return {
        "methodology_note": "Las secciones 'direct_verifications' contienen chequeos algebraicos finitos. Las secciones 'experimental_verifications' son SOLO evidencia numérica y no sustituyen una prueba matemática.",
        "direct_verifications": direct,
        "experimental_verifications": experimental,
        "reproducibility": {
            "output_dir": str(output_dir),
            "command": f'python3 "Plantilla TFM/scripts/verify_chapter3.py" --output-dir "{output_dir}" --n-min {n_min} --n-max {n_max}',
        },
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output-dir", type=Path, default=Path("Plantilla TFM/scripts/results/ch3_verification"))
    parser.add_argument("--n-min", type=int, default=4)
    parser.add_argument("--n-max", type=int, default=24)
    args = parser.parse_args()

    args.output_dir.mkdir(parents=True, exist_ok=True)
    report = build_report(output_dir=args.output_dir, n_min=args.n_min, n_max=args.n_max)
    report_path = args.output_dir / "verification_report.json"
    report_path.write_text(json.dumps(report, indent=2, ensure_ascii=False), encoding="utf-8")

    print("Batería capítulo 3 completada.")
    print(f"Reporte JSON: {report_path}")
    print("Chequeos directos incluidos:")
    for name in report["direct_verifications"]:
        print(f"- {name}")
    print("\nAdvertencia metodológica: los resultados asintóticos o de no acotación quedan como EVIDENCIA EXPERIMENTAL.")


if __name__ == "__main__":
    main()
