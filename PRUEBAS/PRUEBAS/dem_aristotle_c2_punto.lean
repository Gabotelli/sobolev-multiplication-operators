import PRUEBAS.TFMScaffold

noncomputable section

namespace TFM

variable {H : Type*} [NormedAddCommGroup H] [InnerProductSpace ℂ H] [CompleteSpace H]
variable [IsSobolevOnePointSpace H]

/-- Valor exacto de c₂ en el caso de un único punto discreto. -/
theorem exact_c2_for_one_point (D : H →L[ℂ] H) :
    GelfandNumber D 2 = 1 := by
  refine le_antisymm ?_ ?_
  · -- Cota superior del TFM: elegir el hiperplano óptimo V_opt = ker Ψ,
    -- donde Ψ(p) = p(c₁) + c₁ p'(c₁), y comprobar que D es contractivo en él.
    have hPsi_extends : ∃ Ψ : H →L[ℂ] ℂ, True := by
      sorry
    rcases hPsi_extends with ⟨Ψ, hΨ⟩
    have hVopt_codim_one : True := by
      -- La continuidad de Ψ da que ker Ψ es cerrado y de codimensión 1.
      sorry
    have hD_contracts_on_Vopt : True := by
      -- Para p ∈ ker Ψ, la parte discreta de ‖Dp‖² se anula y queda solo la norma continua.
      sorry
    have h_upper : GelfandNumber D 2 ≤ 1 := by
      -- Insertar aquí la traducción Lean de la definición de número de Gelfand
      -- usando el candidato V_opt y la estimación anterior.
      sorry
    exact h_upper
  · -- Cota inferior del TFM: si c₂ < 1, un hiperplano demasiado contractivo
    -- produciría un vector no nulo q con q'(c₁) = 0 y ‖q‖² ≤ 0, contradicción.
    by_contra hlt
    have hstrict : GelfandNumber D 2 < 1 := by
      simpa using hlt
    have h_exists_hyperplane : ∃ (V : Submodule ℂ H) (ε : ℝ), 0 < ε ∧ True := by
      -- Extraer de hstrict un subespacio de codimensión 1 donde D tenga norma < 1.
      sorry
    rcases h_exists_hyperplane with ⟨V, ε, hε, hV⟩
    have h_derivative_not_injective : ∃ q : H, q ∈ V ∧ q ≠ 0 ∧ True := by
      -- Restringir la evaluación de la derivada a V y usar que V sigue siendo infinito-dimensional.
      sorry
    rcases h_derivative_not_injective with ⟨q, hqV, hq_ne, hq_deriv⟩
    have h_contradiction : False := by
      -- Sustituir q en la desigualdad estricta obtenida para V.
      sorry
    exact h_contradiction

end TFM
