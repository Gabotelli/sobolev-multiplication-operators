import PRUEBAS.TFMScaffold

noncomputable section

namespace TFM

variable {H : Type*} [NormedAddCommGroup H] [InnerProductSpace ℂ H] [CompleteSpace H]

/-- Acotación del segundo valor singular en el caso de un átomo exterior. -/
theorem second_singular_value_bound
    (D : H →L[ℂ] H) (R : ℝ) :
    Sigma D 2 0 ≤ ENNReal.ofReal R := by
  sorry

end TFM
