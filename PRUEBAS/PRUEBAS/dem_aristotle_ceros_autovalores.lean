import PRUEBAS.TFMScaffold

noncomputable section

namespace TFM

open Polynomial

/-- Los ceros del polinomio ortogonal coinciden con los autovalores de la sección truncada. -/
theorem zeros_as_eigenvalues
    {n : ℕ} (p : Polynomial ℂ) (A : Matrix (Fin n) (Fin n) ℂ) :
    ZeroSetMatchesSpectrum p A := by
  sorry

end TFM
