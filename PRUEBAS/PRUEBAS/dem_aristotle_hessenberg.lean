import PRUEBAS.TFMScaffold

noncomputable section

namespace TFM

/-- La matriz de multiplicación en una base ortonormal es Hessenberg superior. -/
theorem multiplication_matrix_is_hessenberg
    {n : ℕ} (A : Matrix (Fin n) (Fin n) ℂ) :
    IsUpperHessenberg A := by
  sorry

end TFM
