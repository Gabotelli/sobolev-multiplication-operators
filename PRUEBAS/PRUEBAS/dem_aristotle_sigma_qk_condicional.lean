import PRUEBAS.TFMScaffold

noncomputable section

namespace TFM

variable {H : Type*} [NormedAddCommGroup H] [InnerProductSpace ℂ H] [CompleteSpace H]

/-- Coincidencia exacta para k ≥ 1 bajo aproximación en norma. -/
theorem sigma_eq_qk_under_norm_approximation
    (D : H →L[ℂ] H) (k : ℕ) (_happrox : SupportsNormApproximation D) :
    Sigma D k 0 = Qk D k := by
  sorry

end TFM
