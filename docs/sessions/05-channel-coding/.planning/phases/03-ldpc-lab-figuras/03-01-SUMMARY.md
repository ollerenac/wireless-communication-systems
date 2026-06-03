---
status: complete
---
# SUMMARY — Plan 03-01: FIG-04 tanner-graph.png desde notebook

**Commit:** e2b2491 — 2026-05-29

## What was done
- **Cell 7 codeword fix:** `c_ldpc = [1,1,0,0,1,0,1,1]` → `[0,1,0,1,0,1,0,1]`. Síndrome `[0,0,0,0]` — celda imprime "válida".
- **Tanner graph block added to Cell 7:** `plt.Circle` (variable nodes, steelblue) + `plt.Rectangle` (check nodes, darkorange) + edges from H_ldpc + `plt.savefig('figures/tanner-graph.png', dpi=150)`.
- **index.md comment updated:** line 140 `gsd-quick (tanner-graph-fix)` → `celda 7 de lab.ipynb`.
- **Figcaption cleaned:** forward-reference "Esta figura se generará en la Fase 3 del laboratorio." removed.

## Verification passed
- `figures/tanner-graph.png` — 39,934 bytes ✅
- Cell 7 produces the figure when executed ✅ (IDX-04 pre-compliance)
- bp_bsc demonstration prints "válida" with corrected codeword ✅

## Requirements satisfied
- FIG-04
