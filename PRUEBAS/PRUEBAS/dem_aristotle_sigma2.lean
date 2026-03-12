import PRUEBAS.TFMScaffold

noncomputable section

namespace TFM

variable {H : Type*} [NormedAddCommGroup H] [InnerProductSpace ℂ H] [CompleteSpace H]

/-- Acotación del segundo valor singular en el caso de un átomo exterior. -/
theorem second_singular_value_bound
    (D : H →L[ℂ] H) (R : ℝ) :
    Sigma D 2 0 ≤ ENNReal.ofReal R := by
  -- Esquema del TFM, Teorema de estabilización algebraica para σ₂.
  let V0 : Submodule ℂ H := by
    -- V0 = ker(p ↦ p(c) + c p'(c)), o equivalentemente {(zp)'(c) = 0}.
    sorry
  have hV0_codim : True := by
    -- V0 tiene codimensión 1.
    sorry
  have h_bound_on_V0 : True := by
    -- En V0 desaparece la parte discreta y queda ‖Dp‖ ≤ R ‖p‖.
    sorry
  have h_minmax : Sigma D 2 0 ≤ ENNReal.ofReal R := by
    -- Intersectar V0 con la sección finita correspondiente y aplicar Courant-Fischer.
    sorry
  exact h_minmax

end TFM
