---
phase: quick-260606-ocz
plan: "01"
subsystem: docs/sessions/05-channel-coding
tags: [polar-codes, figures, lab-notebook, index-md]
dependency_graph:
  requires: [quick-260606-9gm]
  provides: [polar-butterfly-n4.png, §4.1-figure-block, lab-cell-16]
  affects: [index.md §4.1, lab.ipynb]
tech_stack:
  added: []
  patterns: [matplotlib-butterfly-annotated, figure-admonition-inline]
key_files:
  created:
    - docs/sessions/05-channel-coding/figures/polar-butterfly-n4.png
  modified:
    - docs/sessions/05-channel-coding/index.md
    - docs/sessions/05-channel-coding/lab.ipynb
decisions:
  - Used existing draw_butterfly() from cell 15 as base; overlaid colored output nodes and annotated u/w/x values in cell 16
  - Single commit for both tasks (figure block + generator cell + PNG are one atomic deliverable)
metrics:
  duration: ~7 minutes
  completed: "2026-06-06"
  tasks_completed: 2
  tasks_total: 2
  files_changed: 3
---

# Quick Task 260606-ocz: Add polar-butterfly-n4.png to §4.1 Example Summary

**One-liner:** Added polar-butterfly-n4.png showing annotated N=4 butterfly network (u/w/x values) inside the §4.1 encoding example admonition, with matching lab.ipynb generator cell.

## Tasks Completed

| Task | Description | Commit |
|------|-------------|--------|
| 1 | Insert `<figure markdown="span">` block with polar-butterfly-n4.png in §4.1 admonition | 05b86c2 |
| 2 | Insert cell 16 in lab.ipynb generating polar-butterfly-n4.png; mkdocs build --strict passes | 05b86c2 |

## What Was Built

**Task 1 — index.md §4.1 figure block:**
- Inserted a `<figure markdown="span">` block inside the `??? example "Ejemplo: encoding butterfly N=4 paso a paso"` admonition at line 334 (after the blank, before `**Escenario.**`)
- Block is indented 4 spaces as required for MkDocs admonition content
- Figcaption describes u=[0,0,1,0]: salmon=frozen bits, blue=info bits; output x=[1,0,1,0] tied to step-by-step calculation below
- Comment `<!-- generada por celda 16 de lab.ipynb -->` maintains notebook-as-ground-truth traceability

**Task 2 — lab.ipynb cell 16:**
- New code cell inserted at index 16 (after cell 15 which generates polar-butterfly.png N=8)
- Reuses `draw_butterfly(N4, frozen4, ax)` from cell 15 — no code duplication
- Overlays colored output nodes (green=x=0, red=x=1) and annotates u_i, w_i (intermediate), x_i values
- Saves to `figures/polar-butterfly-n4.png` at dpi=150
- Figure generated and committed (69 KB)
- Total notebook: 23 cells (was 22)

## Verification

- `grep "polar-butterfly-n4.png" index.md` — line 335 inside §4.1 admonition
- `python3 -c "import json; ..."` — NB OK (cell present, JSON valid)
- `mkdocs build --strict` — exit code 0, no warnings, no errors

## Deviations from Plan

None — plan executed exactly as written.

## Self-Check: PASSED

- [x] `figures/polar-butterfly-n4.png` exists (69 KB)
- [x] index.md contains figure block with polar-butterfly-n4.png indented inside §4.1 admonition
- [x] lab.ipynb cell 16 contains `polar-butterfly-n4.png` savefig
- [x] Commit 05b86c2 exists on branch worktree-agent-a5967fdc072c69925
- [x] mkdocs build --strict passes
