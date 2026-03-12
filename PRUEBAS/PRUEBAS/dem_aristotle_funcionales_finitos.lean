import PRUEBAS.TFMScaffold

noncomputable section

namespace TFM

open Polynomial

variable {H : Type*} [NormedAddCommGroup H] [InnerProductSpace ℂ H] [CompleteSpace H]

/-- Dicotomía generalizada para una familia finita de funcionales lineales. -/
theorem codimension_for_finite_family
    {N : ℕ} (ι : Polynomial ℂ →ₗ[ℂ] H) (_h_dense : DenseRange ι)
    (Φ : Fin N → Polynomial ℂ →ₗ[ℂ] ℂ) (k : ℕ) :
    FamilyClosureCodim ι Φ k := by
  -- Esquema del TFM, Teorema de dicotomía generalizada.
  have h_change_of_basis : ∃ Ψ : Fin N → Polynomial ℂ →ₗ[ℂ] ℂ, True := by
    -- Elegir una base adaptada donde los primeros k funcionales sean continuos
    -- y cualquier combinación que involucre a los restantes sea no acotada.
    sorry
  rcases h_change_of_basis with ⟨Ψ, hΨ⟩
  have h_continuous_part : True := by
    -- Para M_c = ⋂_{j < k} ker(Ψ_j), probar codim(M_c) = k mediante rango-nulidad en P_n.
    sorry
  have h_unbounded_part_dense : True := by
    -- Restringir los funcionales no acotados a M_c y aplicar la versión de un funcional.
    sorry
  have h_intersection_closed_form : True := by
    -- Identificar la clausura de la intersección total con M_c.
    sorry
  sorry

end TFM
