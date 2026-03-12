import PRUEBAS.TFMScaffold

noncomputable section

namespace TFM

open Polynomial

/-- Cota superior para el número de ceros fuera del disco de radio R. -/
theorem control_outer_zeros
    (p : Polynomial ℂ) (R : ℝ) (N : ℕ) :
    HasAtMostNOuterZeros p R N := by
  -- Esquema del TFM, Teorema de control exterior de ceros.
  let V0 : Submodule ℂ (Polynomial ℂ) := by
    -- Intersección de los núcleos de los N funcionales φ_k(p) = c_k p^(j_k)(c_k) + j_k p^(j_k-1)(c_k).
    sorry
  have hV0_codim : True := by
    -- Al ser intersección de N hiperplanos, codim(V0) ≤ N.
    sorry
  have hD_bound_on_V0 : True := by
    -- En V0 se anula la parte discreta y queda ‖Dp‖ ≤ R ‖p‖.
    sorry
  have h_sigma_bound : True := by
    -- Aplicar Courant-Fischer a V0 ∩ P_{n-1} para obtener σ_{N+1,n} ≤ R.
    sorry
  have h_rankN_decomposition : True := by
    -- Separar D_n = M_n + E_n con rango(E_n) ≤ N y ‖M_n‖ ≤ R mediante SVD.
    sorry
  have h_outer_eigenspace_dim : True := by
    -- Si |λ| > R, entonces (λ I - M_n) es invertible y los autovectores escapan por la imagen de E_n.
    sorry
  have h_zeros_from_eigenvalues : True := by
    -- Invocar la proposición anterior: los ceros de p_n son autovalores de la sección truncada.
    sorry
  sorry

end TFM
