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
  sorry

end TFM
