import PRUEBAS.TFMScaffold

noncomputable section

namespace TFM

open Polynomial

/-- Los ceros del polinomio ortogonal coinciden con los autovalores de la sección truncada. -/
theorem zeros_as_eigenvalues
    {n : ℕ} (p : Polynomial ℂ) (A : Matrix (Fin n) (Fin n) ℂ) :
    ZeroSetMatchesSpectrum p A := by
  -- Esquema del TFM, Sección 4.1:
  -- 1. probar que el polinomio característico de Aᵀ es proporcional a p;
  -- 2. deducir la coincidencia de conjuntos de ceros y espectro.
  have h_charpoly_proportional : ∃ c : ℂ, c ≠ 0 ∧ True := by
    -- Aquí debe aparecer la relación det(A - z I) = c * p(z).
    sorry
  rcases h_charpoly_proportional with ⟨c, hc_ne, hprop⟩
  have h_zero_imp_eigen : True := by
    -- Si p(λ) = 0, entonces el determinante característico se anula en λ.
    sorry
  have h_eigen_imp_zero : True := by
    -- Si λ es autovalor, entonces det(A - λ I) = 0 y, por proporcionalidad, p(λ) = 0.
    sorry
  -- Falta cerrar la equivalencia empaquetada en ZeroSetMatchesSpectrum.
  sorry

end TFM
