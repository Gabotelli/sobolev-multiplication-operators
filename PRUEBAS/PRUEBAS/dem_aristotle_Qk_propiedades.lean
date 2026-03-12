import PRUEBAS.TFMScaffold

noncomputable section

namespace TFM

variable {H : Type*} [NormedAddCommGroup H] [InnerProductSpace ℂ H] [CompleteSpace H]

/-- Monotonía y coincidencia del primer índice con la norma global. -/
theorem qk_basic_properties
    (D : H →L[ℂ] H) (k : ℕ) :
    Qk D 1 = GelfandNumber D 1 ∧ Qk D (k + 1) ≤ Qk D k := by
  constructor
  · -- Para k = 1, ambos índices se calculan sobre el espacio total.
    have h_q1 : Qk D 1 = GelfandNumber D 1 := by
      -- La condición codim < 1 fuerza V = H, y c₁(D) = ‖D‖ = Q₁(D).
      sorry
    exact h_q1
  · -- Monotonía: la familia admisible para k está contenida en la de k+1.
    have h_family_inclusion : True := by
      sorry
    have h_monotone : Qk D (k + 1) ≤ Qk D k := by
      -- Minimizar la misma cantidad sobre un conjunto más grande solo puede disminuir el ínfimo.
      sorry
    exact h_monotone

end TFM
