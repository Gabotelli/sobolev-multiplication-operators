import PRUEBAS.TFMScaffold

noncomputable section

namespace TFM

open Polynomial

variable {H : Type*} [NormedAddCommGroup H] [InnerProductSpace ℂ H] [CompleteSpace H]

/-- Dicotomía generalizada para una familia finita de funcionales lineales. -/
theorem codimension_for_finite_family
    {N : ℕ} (ι : Polynomial ℂ →ₗ[ℂ] H) (_h_dense : DenseRange ι)
    (Φ : Fin N → Polynomial ℂ →ₗ[ℂ] ℂ) (k : ℕ) :
    FamilyClosureCodim ι Φ k := by
  sorry

end TFM
