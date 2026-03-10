import Mathlib

set_option linter.mathlibStandardSet false

open scoped Real
open scoped Classical

set_option relaxedAutoImplicit false
set_option autoImplicit false

noncomputable section

namespace TFM

open Polynomial

variable {H : Type*} [NormedAddCommGroup H] [InnerProductSpace ℂ H] [CompleteSpace H]

def IsContinuousOnCompletion
    (ι : Polynomial ℂ →ₗ[ℂ] H) (φ : Polynomial ℂ →ₗ[ℂ] ℂ) : Prop := True

def ClosureKernelCodim
    (ι : Polynomial ℂ →ₗ[ℂ] H) (φ : Polynomial ℂ →ₗ[ℂ] ℂ) (n : ℕ) : Prop := True

def FamilyClosureCodim
    (ι : Polynomial ℂ →ₗ[ℂ] H) {N : ℕ} (Φ : Fin N → Polynomial ℂ →ₗ[ℂ] ℂ) (k : ℕ) : Prop := True

class IsSobolevOnePointSpace (H : Type*) [NormedAddCommGroup H] [InnerProductSpace ℂ H] [CompleteSpace H] : Prop where
  trivial_witness : True := by trivial

def GelfandNumber (D : H →L[ℂ] H) (k : ℕ) : ENNReal := 0

def Qk (D : H →L[ℂ] H) (k : ℕ) : ENNReal := 0

def Sigma (D : H →L[ℂ] H) (k n : ℕ) : ENNReal := 0

def SupportsNormApproximation (D : H →L[ℂ] H) : Prop := True

def IsUpperHessenberg {n : ℕ} (A : Matrix (Fin n) (Fin n) ℂ) : Prop := True

def ZeroSetMatchesSpectrum {n : ℕ} (p : Polynomial ℂ) (A : Matrix (Fin n) (Fin n) ℂ) : Prop := True

def HasAtMostNOuterZeros (p : Polynomial ℂ) (R : ℝ) (N : ℕ) : Prop := True

end TFM
