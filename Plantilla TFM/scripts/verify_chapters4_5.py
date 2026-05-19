"""Batería reproducible de verificaciones para capítulos 4 y 5 del TFM.

Separa explícitamente:
- verificaciones directas sobre identidades matriciales finitas;
- evidencia experimental para resultados asintóticos.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path

import numpy as np

from sobolev_experiments import array_to_complex_json
from sobolev_experiments import run_experiment
from sobolev_experiments import section_matrix
from sobolev_experiments import sobolev_gram_matrix
from sobolev_experiments import gram_schmidt_sobolev
from sobolev_experiments import spectral_snapshot
from sobolev_experiments import threshold_counts


def direct_verifications() -> dict[str, object]:
    scenario = {"r1": 1.0, "c1": 0.0, "atoms": [1.4, -1.6], "n": 8, "thresholds": [1.0, 1.05, 1.1, 1.25, 1.5]}
    results = run_experiment(**scenario)
    verifications = results["verifications"]

    return {
        "scenario": scenario,
        "status": {name: value.passed for name, value in verifications.items()},
        "details": {name: value.__dict__ for name, value in verifications.items()},
    }


def experimental_singular_threshold(n_min: int, n_max: int, thresholds: list[float]) -> dict[str, object]:
    scenario = {"r1": 1.0, "c1": 0.0, "atoms": [1.4, -1.6]}
    m = len(scenario["atoms"])
    rows: list[dict[str, object]] = []

    for n in range(n_min, n_max + 1):
        results = run_experiment(n=n, thresholds=thresholds, **scenario)
        snapshot = results["snapshot"]
        singular_values = snapshot.singular_values
        row = {
            "n": n,
            "sigma_0_n": float(singular_values[0]),
            "sigma_1_n": float(singular_values[1]) if singular_values.size >= 2 else None,
            "sigma_m_n": float(singular_values[m]) if singular_values.size >= m + 1 else None,
        }
        for threshold in thresholds:
            row[f"count_s_gt_{threshold:g}"] = threshold_counts(singular_values, [threshold], use_modulus=False, strict=True)[threshold]
        rows.append(row)

    sigma_m_values = [row["sigma_m_n"] for row in rows if row["sigma_m_n"] is not None]
    return {
        "scenario": {**scenario, "m": m, "radius_R": 1.0, "n_range": [n_min, n_max]},
        "interpretation": "Evidencia experimental de thm:umbral_singular_indice_m_enunciado: se observa crecimiento en j<m y estabilización de sigma_{m,n} cerca de R=1.",
        "rows": rows,
        "summary": {
            "max_sigma_m_n": float(max(sigma_m_values)),
            "min_sigma_m_n": float(min(sigma_m_values)),
            "last_sigma_m_n": float(sigma_m_values[-1]),
            "max_abs_deviation_from_R": float(max(abs(value - 1.0) for value in sigma_m_values)),
        },
    }


def experimental_zero_count(n_min: int, n_max: int, epsilons: list[float]) -> dict[str, object]:
    scenario = {"r1": 1.0, "c1": 0.0, "atoms": [1.4, -1.6]}
    m = len(scenario["atoms"])
    rows: list[dict[str, object]] = []

    for n in range(n_min, n_max + 1):
        results = run_experiment(n=n, thresholds=[1.0 + eps for eps in epsilons], **scenario)
        eigenvalues = results["snapshot"].eigenvalues
        row = {"n": n, "zeros": array_to_complex_json(eigenvalues)}
        for eps in epsilons:
            row[f"count_outside_R_plus_{eps:g}"] = int(np.count_nonzero(np.abs(eigenvalues) > 1.0 + eps))
        rows.append(row)

    eventual_bounds = {}
    for eps in epsilons:
        key = f"count_outside_R_plus_{eps:g}"
        eventual_bounds[key] = max(int(row[key]) for row in rows)

    return {
        "scenario": {**scenario, "m": m, "radius_R": 1.0, "n_range": [n_min, n_max], "epsilons": epsilons},
        "interpretation": "Evidencia experimental de thm:conteo_ceros: para |z|>R+ε el conteo observado no supera m en el rango computado.",
        "rows": rows,
        "summary": eventual_bounds,
    }


def threshold_counterexample_report() -> dict[str, object]:
    matrix = np.array([[7.0, 18.0], [0.0, 1.0]], dtype=np.complex128)
    eigenvalues = np.linalg.eigvals(matrix)
    singular_values = np.sort(np.linalg.svd(matrix, compute_uv=False))[::-1]
    thresholds = [1.0, 5.0, 10.0, 15.0]

    return {
        "matrix": [[7.0, 18.0], [0.0, 1.0]],
        "eigenvalues": array_to_complex_json(eigenvalues),
        "singular_values": [float(x) for x in singular_values],
        "strict_counts": {
            "eigenvalues": threshold_counts(eigenvalues, thresholds, use_modulus=True, strict=True),
            "singular_values": threshold_counts(singular_values, thresholds, use_modulus=False, strict=True),
        },
        "nonstrict_counts": {
            "eigenvalues": threshold_counts(eigenvalues, thresholds, use_modulus=True, strict=False),
            "singular_values": threshold_counts(singular_values, thresholds, use_modulus=False, strict=False),
        },
        "interpretation": "Con > tau, Weyl--Horn no falla. El falso contraejemplo aparece si se usa >= tau y se cuenta un autovalor exactamente en el umbral.",
    }


def build_report(output_dir: Path, n_min: int, n_max: int) -> dict[str, object]:
    thresholds = [1.0, 1.02, 1.05, 1.1, 1.25, 1.5]
    epsilons = [0.02, 0.05, 0.1, 0.25]
    report = {
        "indexing_note": "Se corrigió el corrimiento: ahora --n=N corresponde a D_N, no a D_{N-1}.",
        "direct_verifications": direct_verifications(),
        "experimental_verifications": {
            "thm:umbral_singular_indice_m_enunciado": experimental_singular_threshold(n_min=n_min, n_max=n_max, thresholds=thresholds),
            "thm:conteo_ceros": experimental_zero_count(n_min=n_min, n_max=n_max, epsilons=epsilons),
        },
        "supporting_note": threshold_counterexample_report(),
        "reproducibility": {
            "output_dir": str(output_dir),
            "command": f'python3 "Plantilla TFM/scripts/verify_chapters4_5.py" --output-dir "{output_dir}" --n-min {n_min} --n-max {n_max}',
        },
    }
    return report


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output-dir", type=Path, default=Path("Plantilla TFM/scripts/results/ch4_ch5_verification"))
    parser.add_argument("--n-min", type=int, default=4)
    parser.add_argument("--n-max", type=int, default=24)
    args = parser.parse_args()

    args.output_dir.mkdir(parents=True, exist_ok=True)
    report = build_report(output_dir=args.output_dir, n_min=args.n_min, n_max=args.n_max)

    report_path = args.output_dir / "verification_report.json"
    report_path.write_text(json.dumps(report, indent=2, ensure_ascii=False), encoding="utf-8")

    print("Batería completada.")
    print(f"Reporte JSON: {report_path}")
    print("Verificaciones directas:")
    for name, status in report["direct_verifications"]["status"].items():
        print(f"- {name}: {'OK' if status else 'FALLÓ'}")
    print("\nAdvertencia metodológica: los teoremas asintóticos quedan como EVIDENCIA EXPERIMENTAL, no como prueba.")


if __name__ == "__main__":
    main()
