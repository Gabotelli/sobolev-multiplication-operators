"""Experimentos reproducibles para el caso mixto con frontera.

Objetivo:
- verificar el conteo macroscópico de ceros en |z| > R + eps;
- medir la atracción hacia átomos estrictamente exteriores;
- medir la escala fina n(z/c-1) para átomos de frontera |c|=R.

IMPORTANTE:
- Esto es SOLO evidencia numérica.
- No sustituye una prueba matemática.
"""

from __future__ import annotations

import json
import math
from dataclasses import dataclass
from pathlib import Path

import numpy as np

from sobolev_experiments import array_to_complex_json
from sobolev_experiments import run_experiment


def boundary_profile(x: float) -> float:
    if abs(x) < 1e-12:
        return 1.0 - 1.5
    return math.exp(x) - 3.0 * (math.exp(x) * (x - 1.0) + 1.0) / (x * x)


def positive_boundary_root() -> float:
    left, right = 1.0, 2.0
    f_left, f_right = boundary_profile(left), boundary_profile(right)
    if f_left == 0.0:
        return left
    if f_right == 0.0:
        return right
    if f_left * f_right > 0:
        raise RuntimeError("No se pudo encerrar la raíz positiva de H en [1,2].")
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
    epsilons: tuple[float, ...]

    @property
    def atoms(self) -> list[complex]:
        return list(self.atoms_out + self.atoms_boundary + self.atoms_in)


def nearest_zero(values: np.ndarray, target: complex) -> complex:
    return complex(values[int(np.argmin(np.abs(values - target)))])


def scenario_report(scenario: Scenario, x_star: float) -> dict[str, object]:
    rows: list[dict[str, object]] = []

    for n in scenario.n_values:
        results = run_experiment(
            r1=scenario.radius_R,
            c1=0.0,
            atoms=scenario.atoms,
            n=n,
            thresholds=[scenario.radius_R + eps for eps in scenario.epsilons],
        )
        eigenvalues = np.asarray(results["snapshot"].eigenvalues, dtype=np.complex128)
        moduli = np.abs(eigenvalues)

        row: dict[str, object] = {
            "n": n,
            "matrix_size": [n + 1, n + 1],
            "max_zero_modulus": float(np.max(moduli)),
            "zeros": array_to_complex_json(eigenvalues),
        }

        for eps in scenario.epsilons:
            outside = eigenvalues[moduli > scenario.radius_R + eps]
            row[f"count_outside_R_plus_{eps:g}"] = int(outside.size)
            row[f"outside_zeros_R_plus_{eps:g}"] = array_to_complex_json(outside)

        if scenario.atoms_out:
            row["outer_atom_tracking"] = {
                str(atom): {
                    "nearest_zero": array_to_complex_json([nearest_zero(eigenvalues, atom)])[0],
                    "distance": float(np.min(np.abs(eigenvalues - atom))),
                }
                for atom in scenario.atoms_out
            }

        if scenario.atoms_boundary:
            row["boundary_atom_tracking"] = {
                str(atom): {
                    "nearest_zero": array_to_complex_json([nearest_zero(eigenvalues, atom)])[0],
                    "scaled_x": array_to_complex_json([n * (nearest_zero(eigenvalues, atom) / atom - 1.0)])[0],
                    "error_against_x_star": float(abs(n * (nearest_zero(eigenvalues, atom) / atom - 1.0) - x_star)),
                }
                for atom in scenario.atoms_boundary
            }

        rows.append(row)

    summary: dict[str, object] = {
        "x_star": x_star,
        "max_zero_modulus_overall": max(float(row["max_zero_modulus"]) for row in rows),
    }
    for eps in scenario.epsilons:
        key = f"count_outside_R_plus_{eps:g}"
        summary[f"max_{key}"] = max(int(row[key]) for row in rows)
        summary[f"last_{key}"] = int(rows[-1][key])

    if scenario.atoms_boundary:
        tail = rows[-min(3, len(rows)) :]
        summary["tail_boundary_scaled_x"] = {
            str(atom): [tail_row["boundary_atom_tracking"][str(atom)]["scaled_x"] for tail_row in tail]
            for atom in scenario.atoms_boundary
        }

    return {
        "scenario": {
            "name": scenario.name,
            "radius_R": scenario.radius_R,
            "atoms_out": array_to_complex_json(scenario.atoms_out),
            "atoms_boundary": array_to_complex_json(scenario.atoms_boundary),
            "atoms_in": array_to_complex_json(scenario.atoms_in),
            "n_values": list(scenario.n_values),
            "epsilons": list(scenario.epsilons),
            "m_out": len(scenario.atoms_out),
            "m_boundary": len(scenario.atoms_boundary),
        },
        "rows": rows,
        "summary": summary,
    }


def build_report(output_dir: Path) -> dict[str, object]:
    x_star = positive_boundary_root()
    scenarios = [
        Scenario(
            name="mixed_boundary_single_each",
            radius_R=1.0,
            atoms_out=(1.4,),
            atoms_boundary=(1.0,),
            atoms_in=(0.25,),
            n_values=(10, 12, 16, 20, 24, 28, 32, 40),
            epsilons=(0.02, 0.05, 0.1, 0.25),
        ),
        Scenario(
            name="mixed_boundary_two_plus_two",
            radius_R=1.0,
            atoms_out=(1.4, -1.3),
            atoms_boundary=(1.0, -1.0),
            atoms_in=(0.4,),
            n_values=(10, 12, 16, 20, 24),
            epsilons=(0.02, 0.05, 0.1, 0.25),
        ),
        Scenario(
            name="mixed_boundary_extra_interior",
            radius_R=1.0,
            atoms_out=(1.25,),
            atoms_boundary=(1.0,),
            atoms_in=(0.6, -0.5),
            n_values=(10, 12, 16, 20, 24),
            epsilons=(0.02, 0.05, 0.1, 0.2),
        ),
    ]

    return {
        "methodology_note": "Estos resultados son SOLO evidencia numérica. No sustituyen una prueba matemática del caso mixto con frontera.",
        "reproducibility": {
            "output_dir": str(output_dir),
            "command": f'python3 "Plantilla TFM/scripts/verify_mixed_with_boundary.py" --output-dir "{output_dir}"',
        },
        "experiments": {scenario.name: scenario_report(scenario, x_star) for scenario in scenarios},
    }


def main() -> None:
    import argparse

    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--output-dir",
        type=Path,
        default=Path("Plantilla TFM/scripts/results/mixed_with_boundary_verification"),
    )
    args = parser.parse_args()

    args.output_dir.mkdir(parents=True, exist_ok=True)
    report = build_report(args.output_dir)
    report_path = args.output_dir / "verification_report.json"
    report_path.write_text(json.dumps(report, indent=2, ensure_ascii=False), encoding="utf-8")

    print("Batería mixed-with-boundary completada.")
    print(f"Reporte JSON: {report_path}")


if __name__ == "__main__":
    main()
