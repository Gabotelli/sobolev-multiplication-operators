import PRUEBAS.TFMScaffold

noncomputable section

namespace TFM

variable {H : Type*} [NormedAddCommGroup H] [InnerProductSpace ℂ H] [CompleteSpace H]

/-- En el caso acotado, Q_k coincide con los números de Gelfand. -/
theorem qk_eq_gelfand_in_bounded_case
    (D : H →L[ℂ] H) (k : ℕ) :
    Qk D k = GelfandNumber D k := by
  refine le_antisymm ?_ ?_
  · -- Paso 1 del TFM: de un subespacio cerrado M ⊂ H se pasa a V = M ∩ P[z].
    have h_qk_le : Qk D k ≤ GelfandNumber D k := by
      -- Usar densidad de los polinomios y continuidad de D para comparar las normas de restricción.
      sorry
    exact h_qk_le
  · -- Paso 2 del TFM: de un subespacio algebraico V se pasa a su clausura M = closure V.
    have h_gelfand_le : GelfandNumber D k ≤ Qk D k := by
      -- La clausura no aumenta la norma de la restricción y no empeora la codimensión relevante.
      sorry
    exact h_gelfand_le

end TFM
