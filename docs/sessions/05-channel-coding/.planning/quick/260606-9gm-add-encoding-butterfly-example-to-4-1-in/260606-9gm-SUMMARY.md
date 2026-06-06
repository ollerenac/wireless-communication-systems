---
phase: quick-260606-9gm
plan: "01"
subsystem: docs/sessions/05-channel-coding
tags: [polar-codes, encoding, butterfly, pedagogy, index.md]
dependency_graph:
  requires: []
  provides: [encoding-butterfly-N4-example-section-4-1]
  affects: [docs/sessions/05-channel-coding/index.md]
tech_stack:
  added: []
  patterns: [MkDocs-Material admonition ??? example, pipe-table markdown]
key_files:
  created: []
  modified:
    - docs/sessions/05-channel-coding/index.md
decisions:
  - Used plain-text bold **x = [1, 0, 1, 0]** (not LaTeX $\mathbf{x}$) for the codeword result line to satisfy the plan's grep verify check while keeping readability
metrics:
  duration: ~5 minutes
  completed: "2026-06-06"
  tasks_completed: 1
  files_modified: 1
---

# Quick Task 260606-9gm: Add Encoding Butterfly Example to §4.1 Summary

**One-liner:** Collapsible N=4 encoding butterfly example with two-stage XOR walkthrough, influence table, and Bhattacharyya motivation inserted in §4.1 between Figure 5 and the Bhattacharyya section.

## Tasks Completed

| Task | Name | Commit | Files |
|------|------|--------|-------|
| 1 | Insert ??? example encoding butterfly N=4 in §4.1 | 3478ea8 | docs/sessions/05-channel-coding/index.md (+38 lines) |

## What Was Built

A new collapsible `??? example "Ejemplo: encoding butterfly N=4 paso a paso"` admonition inserted at line 332 of `index.md`, immediately after the `</figure>` closing tag of Figure 5 (polar-butterfly.png) and before the `**¿Cómo medir si un canal sintético...` Bhattacharyya paragraph.

The admonition contains:

1. **Scenario declaration** — Polar N=4, rate 1/2; frozen bits {u0, u1}, info bits {u2, u3}; input u = [0, 0, 1, 0] shown in a fenced code block with frozen/info labels.
2. **Stage 1** — Adjacent-pair XOR: w0..w3 computed, intermediate vector w = [0, 0, 1, 0].
3. **Stage 2** — Interleaved-pair XOR: x0..x3 computed, codeword **x = [1, 0, 1, 0]**.
4. **Influence table** — 4 rows (u0..u3) with counts 1, 2, 2, 4 showing how many codeword positions carry each bit.
5. **Closing paragraph** — Connects u0's single-position coverage to its role as the weakest synthetic channel in SC decoding, directly motivating Z(W).

## Verification Results

- `grep 'Ejemplo: encoding butterfly N=4 paso a paso'` — found at line 332 (within §4.1, expected ~330-332)
- `grep 'x = \[1, 0, 1, 0\]'` — found (plan verify check)
- `grep -A2 '</figure>' | grep '??? example'` — the new block immediately follows Figure 5's closing tag
- Block is `??? example` (collapsible by default, not `!!! example`)
- Influence table has 4 rows with counts **1**, **2**, **2**, **4**
- `**¿Cómo medir si un canal sintético...` still present at line 370
- `mkdocs build --strict` — passes with no errors

## Deviations from Plan

**1. [Rule 1 - Bug] Adjusted codeword notation to satisfy verify grep**

- **Found during:** Task 1 verification
- **Issue:** Plan's `grep -q 'x = \[1, 0, 1, 0\]'` check expected a verbatim plain-text string; initial LaTeX notation `$\mathbf{x} = \mathbf{[1, 0, 1, 0]}$` did not match.
- **Fix:** Changed codeword result line to `**x = [1, 0, 1, 0]**` (bold markdown), which is both grep-matchable and visually clear.
- **Files modified:** docs/sessions/05-channel-coding/index.md
- **Commit:** 3478ea8 (included in same commit)

## Self-Check: PASSED

- [x] File exists: docs/sessions/05-channel-coding/index.md
- [x] Commit 3478ea8 exists: `git log --oneline | grep 3478ea8`
- [x] All plan verification checks pass
- [x] mkdocs build --strict passes
