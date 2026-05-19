"""Experimentos reproducibles para el caso interior puro y el caso mixto sin frontera.

Objetivo:
- medir conteos de ceros fuera de |z|=R+eps;
- comparar con el número de átomos exteriores m;
- registrar distancias de los ceros exteriores a los átomos exteriores.

IMPORTANTE:
- Esto es SOLO evidencia numérica.
- Se apoya en la infraestructura existente de `sobolev_experiments.py`.
"""

from __future__ import annotations

import json
from dataclasses import dataclass
from pathlib import Path

import numpy as np

from sobolev_experiments import array_to_complex_json
from sobolev_experiments import run_experiment


@dataclass(frozen=True)
class Scenario:
    name: str
    radius_R: float
    atoms_out: tuple[complex, ...]
    atoms_in: tuple[complex, ...]
    n_values: tuple[int, ...]
    epsilons: tuple[float, ...]

    @property
    def atoms(self) -> list[complex]:
        return list(self.atoms_out + self.atoms_in)


def zero_report(scenario: Scenario) -> dict[str, object]:
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
                row[f"distances_to_outer_atoms_R_plus_{eps:g}"] = {
                    str(atom): float(np.min(np.abs(outside - atom))) if outside.size else None
                    for atom in scenario.atoms_out
                }
        rows.append(row)

    summary: dict[str, object] = {
        "max_zero_modulus_overall": max(row["max_zero_modulus"] for row in rows),
    }
    for eps in scenario.epsilons:
        key = f"count_outside_R_plus_{eps:g}"
        summary[f"max_{key}"] = max(int(row[key]) for row in rows)
        summary[f"last_{key}"] = int(rows[-1][key])

    if scenario.atoms_out:
        tail = rows[-min(3, len(rows)) :]
        summary["tail_distance_to_outer_atoms"] = {
            str(atom): [
                tail_row[f"distances_to_outer_atoms_R_plus_{scenario.epsilons[1]:g}"][str(atom)]
                for tail_row in tail
            ]
            for atom in scenario.atoms_out
        }

    return {
        "scenario": {
            "name": scenario.name,
            "radius_R": scenario.radius_R,
            "atoms_out": array_to_complex_json(scenario.atoms_out),
            "atoms_in": array_to_complex_json(scenario.atoms_in),
            "n_values": list(scenario.n_values),
            "epsilons": list(scenario.epsilons),
            "m": len(scenario.atoms_out),
        },
        "rows": rows,
        "summary": summary,
    }


def build_report(output_dir: Path) -> dict[str, object]:
    scenarios = [
        Scenario(
            name="pure_interior_mild",
            radius_R=1.0,
            atoms_out=(),
            atoms_in=(0.25, -0.45),
            n_values=(10, 12, 16, 20, 24),
            epsilons=(0.02, 0.05, 0.1, 0.25),
        ),
        Scenario(
            name="pure_interior_near_boundary",
            radius_R=1.0,
            atoms_out=(),
            atoms_in=(0.9, -0.8),
            n_values=(10, 12, 14, 18, 24),
            epsilons=(0.02, 0.05, 0.1),
        ),
        Scenario(
            name="mixed_mild",
            radius_R=1.0,
            atoms_out=(1.4, -1.6),
            atoms_in=(0.25,),
            n_values=(10, 12, 16, 20, 24),
            epsilons=(0.02, 0.05, 0.1, 0.25),
        ),
        Scenario(
            name="mixed_near_boundary_interior",
            radius_R=1.0,
            atoms_out=(1.4, -1.6),
            atoms_in=(0.9, -0.8),
            n_values=(18, 24, 28, 32),
            epsilons=(0.02, 0.05, 0.1, 0.25),
        ),
    ]

    return {
        "methodology_note": "Estos resultados son SOLO evidencia numérica. No sustituyen una prueba matemática del caso mixto ni del interior puro.",
        "reproducibility": {
            "output_dir": str(output_dir),
            "command": f'python3 "Plantilla TFM/scripts/verify_mixed_no_boundary.py" --output-dir "{output_dir}"',
        },
        "experiments": {scenario.name: zero_report(scenario) for scenario in scenarios},
    }


def main() -> None:
    import argparse

    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--output-dir",
        type=Path,
        default=Path("Plantilla TFM/scripts/results/mixed_no_boundary_verification"),
    )
    args = parser.parse_args()

    args.output_dir.mkdir(parents=True, exist_ok=True)
    report = build_report(args.output_dir)
    report_path = args.output_dir / "verification_report.json"
    report_path.write_text(json.dumps(report, indent=2, ensure_ascii=False), encoding="utf-8")

    print("Batería mixed-no-boundary completada.")
    print(f"Reporte JSON: {report_path}")


if __name__ == "__main__":
    main()
