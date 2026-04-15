/-
  Análisis Espectral y Matricial del Operador de Multiplicación
  en Espacios de Sobolev Discretos
  — Gabriel Suárez

  Section 1: Introduction and Preliminaries
  Covers: Definitions 1.1–1.14, Proposition 1.1, Lemmas 1.1–1.3, Corollary 1.1
-/
import PRUEBAS.Defs

open Polynomial SobolevData
open scoped ENNReal

noncomputable section

variable (S : SobolevData)

/-! ## §1.5 Bounded Point Evaluations (BPE)

The behaviour of the Sobolev Hilbert space depends critically on the location
of the discrete points relative to the support of the continuous measure.
-/

/-- **Proposition 1.1** (Boundedness and Continuous Extension in the Interior).
For interior points (|c_k| < R), the evaluation functional δ_{c_k} is continuous
with respect to the Sobolev norm ‖·‖_S. -/
theorem bpe_interior_continuous (k : Fin S.N) (hk : S.IsInterior k) :
    ∃ C : ℝ, 0 < C ∧ ∀ p : ℂ[X],
      ‖p.eval (S.pts k)‖^2 ≤ C * (S.sobolevNormSq p).re := by
  sorry

/-- **Lemma 1.1** (Continuity of the derivative functional for ABPE points).
If c is a BPE for the L²(μ) norm with |c| < R, then c is an Analytic BPE (ABPE)
and the derivative evaluation functional δ'_c is continuous. -/
theorem abpe_derivative_continuous (c : ℂ) (hc : ‖c‖ < S.R)
    (hbpe : S.IsBPE c) :
    ∃ C : ℝ, 0 < C ∧ ∀ p : ℂ[X],
      ‖p.derivative.eval c‖^2 ≤ C * (S.sobolevNormSq p).re := by
  sorry

/-- **Lemma 1.2** (Unboundedness of derivative evaluation at boundary and exterior).
If μ = m_{0;R} (normalized Lebesgue on circle of radius R) and |c| ≥ R,
then the derivative evaluation functional δ'_c is unbounded w.r.t. the L² norm.
Formally: for every M > 0, there exists p with ‖p‖_{L²} = 1 and |p'(c)| > M. -/
theorem deriv_eval_unbounded_exterior (c : ℂ) (hc : S.R ≤ ‖c‖) :
    ∀ M : ℝ, 0 < M → ∃ p : ℂ[X],
      (S.L2InnerProd p p).re = 1 ∧ M < ‖p.derivative.eval c‖ := by
  sorry

/-- **Corollary 1.1** (Implication for the non-BPE Lebesgue case).
If the point evaluation δ_c is unbounded in L²(μ) (i.e., |c| ≥ R),
then the derivative evaluation δ'_c is also unbounded. -/
theorem non_bpe_implies_deriv_unbounded (c : ℂ) (hc : S.R ≤ ‖c‖) :
    ∀ M : ℝ, 0 < M → ∃ p : ℂ[X],
      (S.L2InnerProd p p).re = 1 ∧ M < ‖p.derivative.eval c‖ := by
  sorry

/-- **Lemma 1.3** (Normalization of an unbounded functional).
Let X be a complex normed space and φ : X → ℂ an unbounded linear functional.
Then there exists a sequence (x_n) with ‖x_n‖ → 0 and φ(x_n) = 1 for all n.

We state a concrete version: for every n ≥ 1, there exists x with
‖x‖ < 1/n and φ(x) = 1. -/
theorem unbounded_functional_normalization
    {X : Type*} [SeminormedAddCommGroup X] [Module ℂ X]
    (φ : X →ₗ[ℂ] ℂ) (hunb : ∀ M : ℝ, ∃ x : X, ‖x‖ ≤ 1 ∧ M ≤ ‖φ x‖) :
    ∀ n : ℕ, 0 < n → ∃ x : X, ‖x‖ < (1 : ℝ) / n ∧ φ x = 1 := by
  sorry

end
