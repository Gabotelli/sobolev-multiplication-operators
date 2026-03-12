import PRUEBAS.TFMScaffold

noncomputable section

namespace TFM

variable {H : Type*} [NormedAddCommGroup H] [InnerProductSpace ℂ H] [CompleteSpace H]

/-- Explosión y estabilización inicial del índice Q_k en el caso no-BPE. -/
theorem qk_explosion_and_stabilization
    (D : H →L[ℂ] H) (R : ℝ) :
    Qk D 1 = ⊤ ∧ Qk D 2 ≤ ENNReal.ofReal R := by
  constructor
  · -- Para k = 1, la única codimensión < 1 es el espacio total.
    have h_only_candidate : True := by
      sorry
    have h_unbounded_global : Qk D 1 = ⊤ := by
      -- Traducir que el funcional p ↦ p(c) + c p'(c) es no acotado en la norma de Sobolev.
      sorry
    exact h_unbounded_global
  · -- Para k = 2, tomar el subespacio algebraico V0 = ker φ de codimensión 1.
    let V0 : Submodule ℂ H := by
      sorry
    have hV0_codim_one : True := by
      sorry
    have h_bound_on_V0 : True := by
      -- En V0 desaparece la parte discreta y solo queda la integral continua, controlada por R.
      sorry
    have h_q2_bound : Qk D 2 ≤ ENNReal.ofReal R := by
      sorry
    exact h_q2_bound

end TFM
