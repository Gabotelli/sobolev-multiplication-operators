import PRUEBAS.TFMScaffold

noncomputable section

namespace TFM

variable {H : Type*} [NormedAddCommGroup H] [InnerProductSpace ℂ H] [CompleteSpace H]

/-- Monotonía y coincidencia del primer índice con la norma global. -/
theorem qk_basic_properties
    (D : H →L[ℂ] H) (k : ℕ) :
    Qk D 1 = GelfandNumber D 1 ∧ Qk D (k + 1) ≤ Qk D k := by
  sorry

end TFM
