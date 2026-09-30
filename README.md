# MSc thesis: multiplication operators in discrete Sobolev spaces

My MSc thesis in Advanced Mathematics at Universidad Politécnica de Madrid: *Spectral and Matrix Analysis of the Multiplication Operator in Discrete Sobolev Spaces* (9.5/10).

## Research overview / Main contribution

**Problem.** When discrete derivative evaluations are added to an inner product on polynomials, the multiplication operator $Dp(z)=zp(z)$ can become unbounded. The thesis studies how many independent obstructions cause this failure and how they appear in finite matrix computations.

**Contribution.** The thesis introduces a Gelfand-type index $Q_k(D)$, defined through restrictions to polynomial subspaces of finite codimension and allowing infinite values. For a normalized circle measure of radius $R$ with $N$ distinct derivative atoms, let $m$ count atoms on or outside the circle. The manuscript proves that the first finite index is $Q_m(D)$, while $Q_k(D)=R$ for $k\ge N$.

**Operator-to-matrix connection.** Bounded point evaluations inside the circle control evaluation and derivative terms; boundary and exterior atoms produce the singular obstructions. In an orthonormal polynomial basis, multiplication has a Hessenberg matrix representation. Eigenvalues of its principal sections give polynomial zeros, and the limits of the ordered singular values recover $Q_k(D)$. Finite numerical experiments illustrate this relationship; they do not replace the proofs.

## Available experiments

The current repository contains **Python/NumPy auxiliary verification scripts** under [Plantilla TFM/scripts](Plantilla%20TFM/scripts/):

| Script | Purpose |
| --- | --- |
| `sobolev_experiments.py` | Gram matrices, orthonormalization, Hessenberg sections, zeros, singular values and threshold counts. |
| `threshold_counterexample.py` | Threshold counterexample calculation. |
| `verify_chapter3.py` | Numerical checks for the chapter 3 configurations. |
| `verify_chapters4_5.py` | Matrix identities and spectral checks. |
| `verify_mixed_no_boundary.py` | Interior and mixed configurations without boundary atoms. |
| `verify_mixed_with_boundary.py` | Exterior attraction and boundary-scale numerical evidence. |
| `verify_mixed_boundary_two_scale.py` | Reduced atom system and two-scale boundary verification. |

From the repository root, with Python and NumPy installed:

```bash
python3 "Plantilla TFM/scripts/sobolev_experiments.py" --n 8 --r1 1.0 --c1 0.0 --atoms 1.4 -1.6 --thresholds 1 1.1 1.5 --json-output results/example.json
```

Here `--n 8` means the theoretical section $D_8$, of size $9\times9$. This small example has been run successfully. Larger configurations can be sensitive to numerical conditioning.

## Authorship and scope

The thesis is my academic research project. My documented computational contribution includes Maple routines for finite Hessenberg representations and singular-value analysis. **No standalone Maple worksheets are present in this current tree.** The Python files are supplementary verification code; their individual authorship is not established by this repository and is not claimed here as solely original code written by me. The document class, university branding and cited results retain their respective attribution.

## Manuscript and defense

- [Main manuscript](Plantilla%20TFM/main.tex), with chapters and conclusions in `chapters/`.
- `MUMAv-UPM.cls`, `logos/` and `referencias.bib`: document class, branding and bibliography.
- `figures/`: manuscript figures.
- [Defense slides](Plantilla%20TFM/presentacion/defensa.tex), with `estructura.md` and `notas_orador.md`.

Compiled PDFs, intermediate TeX output, working drafts and unused imagery were removed in the earlier cleanup. A suitable TeX installation is required; a clean manuscript/slide build has not been verified.
