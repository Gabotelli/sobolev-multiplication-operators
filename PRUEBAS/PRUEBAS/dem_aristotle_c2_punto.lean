import PRUEBAS.TFMScaffold

noncomputable section

namespace TFM

variable {H : Type*} [NormedAddCommGroup H] [InnerProductSpace ℂ H] [CompleteSpace H]
variable [IsSobolevOnePointSpace H]

/-- Valor exacto de c₂ en el caso de un único punto discreto. -/
theorem exact_c2_for_one_point (D : H →L[ℂ] H) :
    GelfandNumber D 2 = 1 := by
  sorry

end TFM
