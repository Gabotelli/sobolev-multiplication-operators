import PRUEBAS.TFMScaffold

noncomputable section

namespace TFM

/-- La matriz de multiplicación en una base ortonormal es Hessenberg superior. -/
theorem multiplication_matrix_is_hessenberg
    {n : ℕ} (A : Matrix (Fin n) (Fin n) ℂ) :
    IsUpperHessenberg A := by
  -- Esquema del TFM, Proposición de Hessenberg:
  -- si la j-ésima columna representa z φ_j, entonces deg(z φ_j) = j + 1,
  -- así que las componentes en φ_i con i > j + 1 se anulan.
  have h_column_support : True := by
    -- Formalizar que cada columna j solo puede tener coeficientes no nulos hasta la fila j+1.
    sorry
  have h_entries_zero : True := by
    -- Reescribir la condición anterior entrada a entrada: A i j = 0 si i > j + 1.
    sorry
  sorry

end TFM
