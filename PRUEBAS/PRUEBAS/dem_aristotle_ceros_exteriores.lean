import PRUEBAS.TFMScaffold

noncomputable section

namespace TFM

open Polynomial

/-- Cota superior para el número de ceros fuera del disco de radio R. -/
theorem control_outer_zeros
    (p : Polynomial ℂ) (R : ℝ) (N : ℕ) :
    HasAtMostNOuterZeros p R N := by
  sorry

end TFM
