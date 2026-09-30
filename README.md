# MSc thesis: multiplication operators in discrete Sobolev spaces

My MSc thesis in Advanced Mathematics at Universidad Politécnica de Madrid: *Spectral and Matrix Analysis of the Multiplication Operator in Discrete Sobolev Spaces* (9.5/10).

## Research overview / Main contribution

**Problem.** When discrete derivative evaluations are added to an inner product on polynomials, the multiplication operator $Dp(z)=zp(z)$ can become unbounded. The thesis studies how many independent obstructions cause this failure and how they appear in finite matrix computations.

**Contribution.** The thesis introduces a Gelfand-type index $Q_k(D)$, defined through restrictions to polynomial subspaces of finite codimension and allowing infinite values. For a normalized circle measure of radius $R$ with $N$ distinct derivative atoms, let $m$ count atoms on or outside the circle. The manuscript proves that the first finite index is $Q_m(D)$, while $Q_k(D)=R$ for $k\ge N$.

**Operator-to-matrix connection.** Bounded point evaluations inside the circle control evaluation and derivative terms; boundary and exterior atoms produce the singular obstructions. In an orthonormal polynomial basis, multiplication has a Hessenberg matrix representation. Eigenvalues of its principal sections give polynomial zeros, and the limits of the ordered singular values recover $Q_k(D)$. Finite numerical experiments illustrate this relationship; they do not replace the proofs.

## Computational work and repository scope

I developed Maple routines to investigate finite Hessenberg representations and singular values of the multiplication operator. The manuscript describes the mathematical framework and computational experiments. **Standalone Maple worksheets are not currently included**, so this repository does not yet provide an executable reproduction of those experiments.

## Authorship

The thesis and the Maple algorithm are my academic work. The document class, university branding and cited results retain their respective attribution.

## Manuscript and defense

- [Main manuscript](Plantilla%20TFM/main.tex), with chapters and conclusions in `chapters/`.
- `MUMAv-UPM.cls`, `logos/` and `referencias.bib`: document class, branding and bibliography.
- `figures/`: manuscript figures.
- [Defense slides](Plantilla%20TFM/presentacion/defensa.tex), with `estructura.md` and `notas_orador.md`.

Compiled PDFs, intermediate TeX output, working drafts and unused imagery were removed in the earlier cleanup. A suitable TeX installation is required; a clean manuscript/slide build has not been verified.
