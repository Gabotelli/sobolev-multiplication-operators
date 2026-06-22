# Verify report — display→inline cleanup (post writer pass)

## Status

**PASS** with one concern flagged for the user.

The thesis compiles cleanly (73 pages, no fatal errors) after the writer
subagents' display→inline cleanup. Several minor overfull hboxes introduced by
over-aggressive inline conversion were detected and fixed in place. One
substantive concern (notational scope creep in chapters 3 and 4) is left for
the user to decide on.

## Compile command

```bash
cd "Plantilla TFM" && latexmk -C main.tex
cd "Plantilla TFM" && latexmk -pdf -interaction=nonstopmode -halt-on-error -file-line-error main.tex
```

A full clean rebuild is required because the previous `main.aux` is timestamped
later than the source files but stale with respect to the new content.

Build result: **Output written on main.pdf (73 pages, 1446211 bytes).** No
errors, no warnings other than the typographic over/underfull hboxes listed
below.

## Files inspected

| File                                          | Lines changed by subagent | Nature of changes                       |
| --------------------------------------------- | ------------------------- | --------------------------------------- |
| `chapters/capitulo1-introduccion.tex`         | 123                       | Mostly display→inline, one revert applied |
| `chapters/capitulo2-codimension-qk.tex`       | 225                       | Mostly display→inline, three reverts applied |
| `chapters/capitulo3-estabilizacion.tex`       | 610                       | Display→inline **plus** notational rewrite, one revert applied |
| `chapters/capitulo4-matricial.tex`            | 344                       | Display→inline **plus** notational touch-ups |
| `chapters/capitulo5-ceros.tex`                | 269                       | Display→inline, one sentence rewritten (no math change) |
| `chapters/conclusiones.tex`                   | 67                        | Display→inline **plus** notational touch-ups |

Chapter 5 was modified by the writer but is **commented out in `main.tex`
(line 78: `% \input{chapters/capitulo5-ceros}`) and was therefore not
included in the verified build**. The changes there were reviewed
manually but not compiled.

## Fixes applied by this verification pass

Four localized reverts where the writer's inline conversion produced real
overfull hboxes (>10 pt overflow). Each revert restored a multi-line display
to its pre-cleanup form. The mathematical content is unchanged.

1. `capitulo1-introduccion.tex`, definition
   `def:operador_multiplicacion_intro` — restored the 2-line display for
   the operator definition. (3.1 pt overfull)
2. `capitulo2-codimension-qk.tex`, line 13 — restored the 4-line display
   for the `codim_H` / `codim_Poly` formulas in the opening paragraph
   of the chapter. (10.9 pt overfull)
3. `capitulo2-codimension-qk.tex`, two more blocks in the codimension
   proofs (`F⊕G` and `M = ∩ ker φ_j`) — same pattern, two further
   11–14 pt overfulls.
4. `capitulo3-estabilizacion.tex`, corollary
   `Sean z_1,…,z_N ∈ C distintos y sea V := …` — restored the
   4-line display for `V := ∩ ker(δ_{z_i})` and
   `codim_P(V) = N`. (14.2 pt overfull)

After these reverts the only remaining overfulls are pre-existing
displays with legitimate long expressions (the Sobolev sums of
exterior atoms at 53/78/111 pt) and a long URL in the preamble.

## Remaining warnings (all pre-existing or negligible)

| Overfull (pt) | Location            | Status                                |
| ------------- | ------------------- | ------------------------------------- |
| 15.0, 17.1    | `main.tex:72`       | Preamble URL — pre-existing          |
| 0.24          | `capitulo3:44–46`   | Negligible (≤ 1 pt)                  |
| 53.99         | `capitulo3:359`     | Sobolev display — pre-existing       |
| 1.03          | `capitulo3:773–776` | Negligible (≤ 1 pt)                  |
| 7.76          | `capitulo4:451`     | Sobolev display — pre-existing       |
| 78.77         | `capitulo4:515`     | Sobolev display — pre-existing       |
| 111.75        | `capitulo4:579`     | Sobolev display — pre-existing       |

`Underfull \vbox (badness 2426)` once on the last page; pre-existing.

## Concern flagged for the user (not fixed)

**Notational scope creep in chapters 3, 4, and `conclusiones.tex`.**

The writer subagent went beyond display→inline. In particular:

- In `capitulo3-estabilizacion.tex` the writer rewrote the set-based
  notation `(F, I_out, I_in, V_out, C_out, …)` as indexed
  `(c_1, …, c_N, V_m, C_m, …)` across roughly 25 statements
  (definitions, lemmas, propositions, theorems, proofs). The
  statements are mathematically equivalent — same codimensions, same
  inequalities, same logical structure — but the notation is genuinely
  different.
- In `capitulo4-matricial.tex` similar touch-ups appear
  (`F ⊂ C` → `c_1,…,c_N`, plus a stray `I_out` reference collapsed
  to `m := N`).
- In `conclusiones.tex` the `c_j` indexed form is used in the prose
  section that summarizes the setup, replacing the original
  `F ⊂ C` / `I_out` prose.

The user said: *"No mathematical, notational, or argument changes were
intended."* The chapter 3/4 changes violate that — even though the
math still works, the notation is a different style. The changes are
internally consistent and compile cleanly, so they were left in place;
the user may want to revert the set-based notation if the original
style was deliberate. To revert, `git restore Plantilla TFM/chapters/capitulo3-estabilizacion.tex` and
`capitulo4-matricial.tex` is the cleanest reset, then redo the
display→inline pass with stricter guard rails (e.g., "do not change
`F`, `I_out`, `I_in`, `V_out`; only inline short connective formulas
that are not definition statements").

## Was Chapter 5 included in the verified build?

**No.** `main.tex` line 78 has `% \input{chapters/capitulo5-ceros}` —
chapter 5 has been commented out in the project for at least three
commits (per `git log -- main.tex`). The writer's modifications to
`capitulo5-ceros.tex` were reviewed by reading the file but not
compiled. If the chapter is to be included for the final build,
uncomment that line and rerun the compile command above.
