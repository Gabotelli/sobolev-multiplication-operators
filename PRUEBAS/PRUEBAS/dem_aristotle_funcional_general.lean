import PRUEBAS.TFMScaffold

noncomputable section

namespace TFM

open Polynomial

variable {H : Type*} [NormedAddCommGroup H] [InnerProductSpace ℂ H] [CompleteSpace H]

/-- Dicotomía de la codimensión para un funcional lineal abstracto sobre polinomios. -/
theorem codimension_dichotomy_for_functional
    (ι : Polynomial ℂ →ₗ[ℂ] H) (_h_dense : DenseRange ι)
    (φ : Polynomial ℂ →ₗ[ℂ] ℂ) :
    (IsContinuousOnCompletion ι φ → ClosureKernelCodim ι φ 1) ∧
    (¬ IsContinuousOnCompletion ι φ → ClosureKernelCodim ι φ 0) := by
  constructor
  · intro hcont
    -- Caso continuo del TFM:
    -- 1. ker φ es cerrado tras extender φ a la completación;
    -- 2. existe q con φ(q) ≠ 0 y P[z] = ker φ ⊕ span{q};
    -- 3. la codimensión topológica vale 1.
    have h_closed_kernel : True := by
      sorry
    have h_direct_sum_on_polynomials : True := by
      -- Usar la descomposición p = (p - φ(p)/φ(q) • q) + φ(p)/φ(q) • q.
      sorry
    have h_codim_one : ClosureKernelCodim ι φ 1 := by
      sorry
    exact h_codim_one
  · intro hnotcont
    -- Caso no continuo del TFM:
    -- el núcleo algebraico es denso, luego su clausura es todo H y la codimensión es 0.
    have h_kernel_dense : True := by
      -- Construir una sucesión q_n con φ(q_n) = 1 y ‖q_n‖ → 0, y luego aproximar 1 por elementos de ker φ.
      sorry
    have h_codim_zero : ClosureKernelCodim ι φ 0 := by
      sorry
    exact h_codim_zero

end TFM
