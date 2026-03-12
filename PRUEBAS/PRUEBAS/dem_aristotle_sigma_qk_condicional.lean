import PRUEBAS.TFMScaffold

noncomputable section

namespace TFM

variable {H : Type*} [NormedAddCommGroup H] [InnerProductSpace ℂ H] [CompleteSpace H]

/-- Coincidencia exacta para k ≥ 1 bajo aproximación en norma. -/
theorem sigma_eq_qk_under_norm_approximation
    (D : H →L[ℂ] H) (k : ℕ) (_happrox : SupportsNormApproximation D) :
    Sigma D k 0 = Qk D k := by
  -- Esquema del TFM, proposición condicional de convergencia exacta.
  let Dtrunc : H →L[ℂ] H := by
    -- Dtrunc debe representar la compresión P_n D P_n.
    sorry
  have h_finite_rank_identity : True := by
    -- Para operadores de rango finito, los números de Gelfand coinciden con los valores singulares.
    sorry
  have h_lipschitz : True := by
    -- Usar que k ↦ GelfandNumber es 1-Lipschitz respecto de la norma operatorial.
    sorry
  have h_sigma_eq_gelfand : Sigma D k 0 = GelfandNumber D k := by
    -- Aplicar la hipótesis de aproximación en norma a Dtrunc.
    sorry
  calc
    Sigma D k 0 = GelfandNumber D k := h_sigma_eq_gelfand
    _ = Qk D k := by
      symm
      exact qk_eq_gelfand_in_bounded_case D k

end TFM
