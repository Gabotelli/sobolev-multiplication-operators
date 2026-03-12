import PRUEBAS.TFMScaffold

noncomputable section

namespace TFM

variable {H : Type*} [NormedAddCommGroup H] [InnerProductSpace ℂ H] [CompleteSpace H]

/-- Cota de los valores singulares truncados en términos del índice Q_k. -/
theorem sigma_le_qk
    (D : H →L[ℂ] H) (k n : ℕ) :
    Sigma D k n ≤ Qk D k := by
  -- Esquema del TFM, Proposición σ_{k,n} ≤ Q_k.
  have h_minmax : True := by
    -- Reescribir Sigma D k n mediante la caracterización minimax de la sección truncada.
    sorry
  have h_from_algebraic_subspace : True := by
    -- Fijado V con codim < k, definir V_n = V ∩ P_{n-1} y el subespacio W_n de coordenadas.
    sorry
  have h_contractivity_of_projection : True := by
    -- Comparar ‖D_n|_{W_n}‖ con ‖D|_{V_n}‖ y luego con ‖D|_V‖.
    sorry
  have h_infimum : Sigma D k n ≤ Qk D k := by
    -- Tomar ínfimo sobre todos los V admisibles.
    sorry
  exact h_infimum

end TFM
