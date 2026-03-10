import PRUEBAS.TFMScaffold

noncomputable section

namespace TFM

variable {H : Type*} [NormedAddCommGroup H] [InnerProductSpace ℂ H] [CompleteSpace H]

/-- En el caso acotado, Q_k coincide con los números de Gelfand. -/
theorem qk_eq_gelfand_in_bounded_case
    (D : H →L[ℂ] H) (k : ℕ) :
    Qk D k = GelfandNumber D k := by
  sorry

end TFM
