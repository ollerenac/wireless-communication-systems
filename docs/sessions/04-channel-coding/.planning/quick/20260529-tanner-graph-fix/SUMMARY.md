---
status: complete
---
# SUMMARY — tanner-graph-fix

Commit: 58ec99f — 2026-05-29

## What was done
- Generated `figures/tanner-graph.png` (121 KB) from H_ldpc (8,4) bipartite layout:
  8 variable nodes (steelblue circles, v0–v7, top row) + 4 check nodes (darkorange squares, c0–c3, bottom row) + edges from H matrix
- Updated `index.md` line 133 comment from "será generada por lab.ipynb — Fase 3" to "generada por gsd-quick (tanner-graph-fix)"

## Verification
- `figures/tanner-graph.png` exists, 121 KB ✅
- Broken image reference at index.md:132 resolved ✅
