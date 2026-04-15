/-
  Análisis Espectral y Matricial del Operador de Multiplicación
  en Espacios de Sobolev Discretos
  — Gabriel Suárez

  Core definitions for the formalization.
-/
import Mathlib

open Polynomial MeasureTheory
open scoped ENNReal

noncomputable section

/-- A `SobolevData` packages the parameters for a discrete Sobolev inner product. -/
structure SobolevData where
  R : ℝ
  hR : 0 < R
  N : ℕ
  pts : Fin N → ℂ
  pts_distinct : Function.Injective pts

namespace SobolevData

variable (S : SobolevData)

/-- Evaluate a polynomial at a complex point. -/
abbrev evalAt (p : ℂ[X]) (z : ℂ) : ℂ := p.eval z

/-- Evaluate the formal derivative of `p` at a complex point. -/
abbrev derivEvalAt (p : ℂ[X]) (z : ℂ) : ℂ := p.derivative.eval z

/-- The L² inner product on the circle of radius R. -/
def L2InnerProd (p q : ℂ[X]) : ℂ := let _ := S.R; sorry

/-- The discrete part: Σ p'(c_k)·conj(q'(c_k)). -/
def discretePart (p q : ℂ[X]) : ℂ :=
  ∑ k : Fin S.N, (derivEvalAt p (S.pts k)) * starRingEnd ℂ (derivEvalAt q (S.pts k))

/-- The Sobolev inner product (Definition 1.8). -/
def sobolevInnerProd (p q : ℂ[X]) : ℂ :=
  S.L2InnerProd p q + S.discretePart p q

/-- The Sobolev norm squared. -/
def sobolevNormSq (p : ℂ[X]) : ℂ := S.sobolevInnerProd p p

/-- Interior point: ‖c_k‖ < R. -/
def IsInterior (k : Fin S.N) : Prop := ‖S.pts k‖ < S.R

/-- Exterior point: R ≤ ‖c_k‖. -/
def IsExterior (k : Fin S.N) : Prop := S.R ≤ ‖S.pts k‖

/-- The set of exterior indices. -/
def I_out : Finset (Fin S.N) :=
  Finset.univ.filter (fun k => decide (S.R ≤ ‖S.pts k‖) = true)

/-- Number of exterior points. -/
def m : ℕ := S.I_out.card

/-- Multiplication operator 𝒟p(z) = z·p(z). -/
def multOp (p : ℂ[X]) : ℂ[X] := let _ := S.R; X * p

/-- Functional ψ_k(p) = p(c_k) + c_k·p'(c_k). -/
def psi (k : Fin S.N) (p : ℂ[X]) : ℂ :=
  p.eval (S.pts k) + (S.pts k) * p.derivative.eval (S.pts k)

/-- Bounded Point Evaluation (BPE). -/
def IsBPE (a : ℂ) : Prop :=
  ∃ C : ℝ, 0 < C ∧ ∀ p : ℂ[X], ‖p.eval a‖^2 ≤ C * (S.sobolevNormSq p).re

/-- Algebraic codimension of a subspace of ℂ[X]. -/
def algCodim (V : Submodule ℂ ℂ[X]) : ℕ∞ :=
  let _ := S.R
  Cardinal.toENat (Module.rank ℂ (ℂ[X] ⧸ V))

/-- Algebraic index Q_k(𝒟). -/
def Q_index (k : ℕ) : ℝ≥0∞ := let _ := S.R; let _ := k; sorry

/-- Topological index S_k(𝒟). -/
def S_index (k : ℕ) : ℝ≥0∞ := let _ := S.R; let _ := k; sorry

/-- Gelfand numbers c_k(𝒟). -/
def gelfandNumber (k : ℕ) : ℝ≥0∞ := let _ := S.R; let _ := k; sorry

/-- Annihilator ideal I(V). -/
def annihilatorIdeal (V : Submodule ℂ ℂ[X]) : Ideal ℂ[X] :=
  let _ := S.R; let _ := V; sorry

/-- Canonical subspace V_out = ∩_{k ∈ I_out} ker(ψ_k). -/
def V_out : Submodule ℂ ℂ[X] := let _ := S.I_out; sorry

/-- Annihilator polynomial A_out(z) = ∏_{k ∈ I_out} (z - c_k)². -/
def A_out : ℂ[X] :=
  S.I_out.prod (fun k => (X - Polynomial.C (S.pts k))^2)

/-- Hessenberg matrix truncated to order n. -/
def hessenbergSection (n : ℕ) : Matrix (Fin (n + 1)) (Fin (n + 1)) ℂ :=
  let _ := S.R; sorry

/-- Singular value σ_{k,n} of the n-th truncated section. -/
def singularValue (k n : ℕ) : ℝ := let _ := S.R; let _ := k; let _ := n; sorry

/-- Asymptotic singular index σ_k = lim σ_{k,n}. -/
def asympSingularIndex (k : ℕ) : ℝ≥0∞ := let _ := S.R; let _ := k; sorry

/-- The n-th orthonormal Sobolev polynomial. -/
def orthonormalPoly (n : ℕ) : ℂ[X] := let _ := S.R; let _ := n; sorry

/-- Spectral radius of a matrix. -/
def spectralRadius {n : ℕ} (A : Matrix (Fin n) (Fin n) ℂ) : ℝ :=
  let _ := S.R; let _ := A; sorry

/-- Annihilating polynomial A(z) = ∏(z - c_k)². -/
def annihilatingPoly : ℂ[X] :=
  Finset.univ.prod (fun k : Fin S.N => (X - Polynomial.C (S.pts k))^2)

/-- Degree of the annihilating polynomial: L = 2N. -/
def annihilatingDeg : ℕ := 2 * S.N

end SobolevData

end

