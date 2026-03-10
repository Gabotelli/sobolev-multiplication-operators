import PRUEBAS.TFMScaffold

noncomputable section

namespace TFM

variable {H : Type*} [NormedAddCommGroup H] [InnerProductSpace ℂ H] [CompleteSpace H]

/-- Subaditividad de Q_k frente a perturbaciones acotadas. -/
theorem qk_subadditive_under_bounded_perturbation
    (D E : H →L[ℂ] H) (k : ℕ) :
    Qk (D + E) k ≤ Qk D k + ENNReal.ofReal ‖E‖ := by
  sorry

end TFM
