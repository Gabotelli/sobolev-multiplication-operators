import PRUEBAS.TFMScaffold

noncomputable section

namespace TFM

variable {H : Type*} [NormedAddCommGroup H] [InnerProductSpace ℂ H] [CompleteSpace H]

/-- Explosión y estabilización inicial del índice Q_k en el caso no-BPE. -/
theorem qk_explosion_and_stabilization
    (D : H →L[ℂ] H) (R : ℝ) :
    Qk D 1 = ⊤ ∧ Qk D 2 ≤ ENNReal.ofReal R := by
  sorry

end TFM
