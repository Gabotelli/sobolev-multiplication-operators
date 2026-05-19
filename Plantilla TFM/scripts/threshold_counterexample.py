"""Ejemplo 2x2 para conteos por umbral bien y mal interpretados.

Uso rápido:
    python3 "Plantilla TFM/scripts/threshold_counterexample.py"
    python3 "Plantilla TFM/scripts/threshold_counterexample.py" --thresholds 1 5 10 15

La matriz por defecto es [[7, 18], [0, 1]]. El script muestra dos cosas:
- con `> tau`, la desigualdad de Weyl--Horn sí se respeta;
- con `>= tau`, puede aparecer un falso "contraejemplo" en el borde.
"""

from __future__ import annotations

import argparse

import numpy as np


def threshold_counts(values: np.ndarray, thresholds: list[float], use_modulus: bool, strict: bool) -> dict[float, int]:
    arr = np.abs(values) if use_modulus else np.asarray(values, dtype=float)
    if strict:
        return {threshold: int(np.count_nonzero(arr > threshold)) for threshold in thresholds}
    return {threshold: int(np.count_nonzero(arr >= threshold)) for threshold in thresholds}


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--thresholds", nargs="*", type=float, default=[1.0, 5.0, 10.0, 15.0])
    args = parser.parse_args()

    matrix = np.array([[7.0, 18.0], [0.0, 1.0]], dtype=np.complex128)
    eigenvalues = np.linalg.eigvals(matrix)
    singular_values = np.sort(np.linalg.svd(matrix, compute_uv=False))

    strict_eig_counts = threshold_counts(eigenvalues, args.thresholds, use_modulus=True, strict=True)
    strict_sing_counts = threshold_counts(singular_values, args.thresholds, use_modulus=False, strict=True)
    nonstrict_eig_counts = threshold_counts(eigenvalues, args.thresholds, use_modulus=True, strict=False)
    nonstrict_sing_counts = threshold_counts(singular_values, args.thresholds, use_modulus=False, strict=False)

    print("Matriz:")
    print(matrix)
    print("\nAutovalores:", eigenvalues)
    print("Valores singulares:", singular_values)
    print("\nConteos por umbral (versión correcta de Weyl--Horn: > tau):")
    for threshold in args.thresholds:
        print(
            f"  tau={threshold:g}: "
            f"#{'{'}|lambda|>tau{'}'}={strict_eig_counts[threshold]}, "
            f"#{'{'}s>tau{'}'}={strict_sing_counts[threshold]}"
        )

    print("\nConteos NO estrictos (>= tau), útiles para mostrar la mala lectura):")
    for threshold in args.thresholds:
        print(
            f"  tau={threshold:g}: "
            f"#{'{'}|lambda|>=tau{'}'}={nonstrict_eig_counts[threshold]}, "
            f"#{'{'}s>=tau{'}'}={nonstrict_sing_counts[threshold]}"
        )

    print(
        "\nLectura correcta: Weyl--Horn compara conteos con desigualdad estricta (> tau). "
        "Si usás >= tau, podés fabricar un falso contraejemplo justo en el borde."
    )


if __name__ == "__main__":
    main()
