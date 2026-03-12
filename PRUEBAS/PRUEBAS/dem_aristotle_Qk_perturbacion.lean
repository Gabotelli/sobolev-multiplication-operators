import PRUEBAS.TFMScaffold

noncomputable section

namespace TFM

variable {H : Type*} [NormedAddCommGroup H] [InnerProductSpace ℂ H] [CompleteSpace H]

/-- Subaditividad de Q_k frente a perturbaciones acotadas. -/
theorem qk_subadditive_under_bounded_perturbation
    (D E : H →L[ℂ] H) (k : ℕ) :
    Qk (D + E) k ≤ Qk D k + ENNReal.ofReal ‖E‖ := by
  -- Esquema del TFM, Proposición de perturbación acotada.
  have h_on_each_candidate : True := by
    -- Para todo subespacio admisible V:
    -- ‖(D + E)|_V‖ ≤ ‖D|_V‖ + ‖E|_V‖ ≤ ‖D|_V‖ + ‖E‖.
    sorry
  have h_take_infimum : Qk (D + E) k ≤ Qk D k + ENNReal.ofReal ‖E‖ := by
    -- Tomar ínfimo sobre todos los V con codim < k en la desigualdad anterior.
    sorry
  exact h_take_infimum

end TFM
