import PRUEBAS.TFMScaffold

noncomputable section

namespace TFM

variable {H : Type*} [NormedAddCommGroup H] [InnerProductSpace ℂ H] [CompleteSpace H]

/-- Cota de los valores singulares truncados en términos del índice Q_k. -/
theorem sigma_le_qk
    (D : H →L[ℂ] H) (k n : ℕ) :
    Sigma D k n ≤ Qk D k := by
  sorry

end TFM
