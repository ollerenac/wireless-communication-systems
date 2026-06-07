---
slug: tanner-graph-layout
date: 2026-06-04
status: complete
---

# Summary: Tanner graph layout fix

## Changes applied
1. `c_x`: `linspace(1.5, n_c+0.5, n_c)` → `linspace(0.5, n_v-0.5, n_c)` — check nodes now span full width
2. `v_y`: `1.0` → `1.5` — increased vertical separation
3. `ylim`: `(-0.7, 1.7)` → `(-0.7, 2.2)` — preserved top margin
4. Regenerated `figures/tanner-graph.png`

## Commit
6bb2204
