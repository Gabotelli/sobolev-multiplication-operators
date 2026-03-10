import PRUEBAS.TFMScaffold

noncomputable section

namespace TFM

variable {H : Type*} [NormedAddCommGroup H] [InnerProductSpace ℂ H] [CompleteSpace H]

/-- Coincidencia exacta entre el primer valor singular asintótico y Q₁. -/
theorem sigma1_eq_q1
    (D : H →L[ℂ] H) :
    Sigma D 1 0 = Qk D 1 := by
  sorry

end TFM
