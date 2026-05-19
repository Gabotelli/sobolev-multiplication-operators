"""Verificación numérica del cierre mixto con frontera.

Idea:
- resolver el sistema exacto de derivadas en los átomos (sin Gram-Schmidt global),
- reconstruir el polinomio mónico,
- medir la escala fina n(z/c-1) en los átomos frontera,
- comparar el perfil local con el límite teórico F_out(c) H(x).

Esto NO sustituye la prueba del manuscrito; solo documenta evidencia reproducible.
"""

from __future__ import annotations

import json
import math
from dataclasses import dataclass
from pathlib import Path

import numpy as np

from sobolev_experiments import array_to_complex_json


def s_n(xi: complex, n: int) -> complex:
    j = np.arange(1, n + 1, dtype=np.complex128)
    return np.sum(j * (xi ** (j - 1)))


def t_n(xi: complex, n: int) -> complex:
    j = np.arange(1, n + 1, dtype=np.complex128)
    return np.sum((j**2) * (xi ** (j - 1)))


def boundary_profile(x: float) -> float:
    if abs(x) < 1e-12:
        return -0.5
    return math.exp(x) - 3.0 * (math.exp(x) * (x - 1.0) + 1.0) / (x * x)


def positive_boundary_root() -> float:
    left, right = 1.0, 2.0
    f_left, f_right = boundary_profile(left), boundary_profile(right)
    for _ in range(80):
        mid = 0.5 * (left + right)
        f_mid = boundary_profile(mid)
        if f_left * f_mid <= 0:
            right = mid
            f_right = f_mid
        else:
            left = mid
            f_left = f_mid
    return 0.5 * (left + right)


@dataclass(frozen=True)
class Scenario:
    name: str
    radius_R: float
    atoms_out: tuple[complex, ...]
    atoms_boundary: tuple[complex, ...]
    atoms_in: tuple[complex, ...]
    n_values: tuple[int, ...]
    sample_x: tuple[float, ...] = (0.5, 1.0, 2.0)

    @property
    def atoms(self) -> tuple[complex, ...]:
        return self.atoms_out + self.atoms_boundary + self.atoms_in


def solve_atom_system(radius_R: float, atoms: tuple[complex, ...], n: int) -> tuple[np.ndarray, np.ndarray]:
    size = len(atoms)
    matrix = np.zeros((size, size), dtype=np.complex128)
    rhs = np.zeros(size, dtype=np.complex128)
    for i, atom_i in enumerate(atoms):
        rhs[i] = (n + 1) * (atom_i**n)
        for j, atom_j in enumerate(atoms):
            matrix[i, j] = (1.0 if i == j else 0.0) + t_n(atom_i * np.conj(atom_j) / (radius_R**2), n) / (radius_R**2)
    derivatives = np.linalg.solve(matrix, rhs)

    coeffs = np.zeros(n + 2, dtype=np.complex128)  # ascendentes
    coeffs[n + 1] = 1.0
    for k in range(1, n + 1):
        coeffs[k] = -(k / (radius_R ** (2 * k))) * sum(
            derivatives[j] * (np.conj(atoms[j]) ** (k - 1)) for j in range(size)
        )
    return coeffs, derivatives


def poly_eval_ascending(coeffs: np.ndarray, z: complex) -> complex:
    return sum(coeff * (z**k) for k, coeff in enumerate(coeffs))


def nearest_zero(values: np.ndarray, target: complex) -> complex:
    return complex(values[int(np.argmin(np.abs(values - target)))])


def f_out(radius_R: float, atoms_out: tuple[complex, ...], z: complex) -> complex:
    value = 1.0 + 0.0j
    for atom in atoms_out:
        value *= (z - atom) / (z - (radius_R**2) / np.conj(atom))
    return value


def scenario_report(scenario: Scenario, x_star: float) -> dict[str, object]:
    rows: list[dict[str, object]] = []
    for n in scenario.n_values:
        coeffs, _ = solve_atom_system(scenario.radius_R, scenario.atoms, n)
        roots = np.roots(coeffs[::-1])
        row: dict[str, object] = {
            "n": n,
            "max_zero_modulus": float(np.max(np.abs(roots))),
        }

        if scenario.atoms_out:
            row["outer_atom_tracking"] = {
                str(atom): {
                    "nearest_zero": array_to_complex_json([nearest_zero(roots, atom)])[0],
                    "distance": float(np.min(np.abs(roots - atom))),
                }
                for atom in scenario.atoms_out
            }

        if scenario.atoms_boundary:
            boundary_data: dict[str, object] = {}
            for atom in scenario.atoms_boundary:
                z_near = nearest_zero(roots, atom)
                scaled = n * (z_near / atom - 1.0)
                local_samples = []
                factor = f_out(scenario.radius_R, scenario.atoms_out, atom)
                for x in scenario.sample_x:
                    z = atom * (1.0 + x / n)
                    g_n = poly_eval_ascending(coeffs, z) / (atom ** (n + 1))
                    limit = factor * boundary_profile(x)
                    local_samples.append(
                        {
                            "x": x,
                            "G_n": array_to_complex_json([g_n])[0],
                            "limit_Fout_times_H": array_to_complex_json([limit])[0],
                            "difference": float(abs(g_n - limit)),
                        }
                    )

                boundary_data[str(atom)] = {
                    "F_out_at_atom": array_to_complex_json([factor])[0],
                    "nearest_zero": array_to_complex_json([z_near])[0],
                    "scaled_x": array_to_complex_json([scaled])[0],
                    "error_against_x_star": float(abs(scaled - x_star)),
                    "profile_samples": local_samples,
                }
            row["boundary_atom_tracking"] = boundary_data

        rows.append(row)

    return {
        "scenario": {
            "name": scenario.name,
            "radius_R": scenario.radius_R,
            "atoms_out": array_to_complex_json(scenario.atoms_out),
            "atoms_boundary": array_to_complex_json(scenario.atoms_boundary),
            "atoms_in": array_to_complex_json(scenario.atoms_in),
            "n_values": list(scenario.n_values),
            "sample_x": list(scenario.sample_x),
        },
        "rows": rows,
    }


def build_report(output_dir: Path) -> dict[str, object]:
    x_star = positive_boundary_root()
    scenarios = [
        Scenario(
            name="mixed_boundary_single_each_exact",
            radius_R=1.0,
            atoms_out=(1.4,),
            atoms_boundary=(1.0,),
            atoms_in=(0.25,),
            n_values=(20, 30, 40, 60, 80, 100, 120),
        ),
        Scenario(
            name="mixed_boundary_two_plus_two_exact",
            radius_R=1.0,
            atoms_out=(1.4, -1.3),
            atoms_boundary=(1.0, -1.0),
            atoms_in=(0.4,),
            n_values=(24, 40, 60, 80, 100),
        ),
    ]
    return {
        "methodology_note": "Sistema exacto reducido a los átomos + reconstrucción del polinomio mónico. Solo evidencia numérica.",
        "x_star": x_star,
        "reproducibility": {
            "output_dir": str(output_dir),
            "command": f'python3 "Plantilla TFM/scripts/verify_mixed_boundary_two_scale.py" --output-dir "{output_dir}"',
        },
        "experiments": {scenario.name: scenario_report(scenario, x_star) for scenario in scenarios},
    }


def main() -> None:
    import argparse

    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--output-dir",
        type=Path,
        default=Path("Plantilla TFM/scripts/results/mixed_boundary_two_scale_verification"),
    )
    args = parser.parse_args()

    args.output_dir.mkdir(parents=True, exist_ok=True)
    report = build_report(args.output_dir)
    report_path = args.output_dir / "verification_report.json"
    report_path.write_text(json.dumps(report, indent=2, ensure_ascii=False), encoding="utf-8")

    print("Batería mixed-boundary-two-scale completada.")
    print(f"Reporte JSON: {report_path}")


if __name__ == "__main__":
    main()
