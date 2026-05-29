---
slug: tanner-graph-fix
created: "2026-05-29"
status: in_progress
---

# Quick Task: Generar tanner-graph.png

## Problem
`figures/tanner-graph.png` referenciada en `index.md` línea 132 no existe → imagen rota en el sitio publicado.

## Fix
Generar `figures/tanner-graph.png` programáticamente desde la matriz H_ldpc (8,4) ya definida en el notebook, usando matplotlib con layout bipartito manual. Actualizar el comentario en index.md.

## H_ldpc matrix (from lab.ipynb Cell 7)
```
H = [[1, 1, 1, 1, 0, 0, 0, 0],
     [0, 1, 1, 0, 1, 1, 0, 0],
     [0, 0, 1, 1, 0, 1, 1, 0],
     [1, 0, 0, 1, 0, 0, 1, 1]]
```
4 check nodes (c0–c3), 8 variable nodes (v0–v7)

## Task 1: Generate tanner-graph.png
Run Python script inline to produce the figure. Requirements:
- figsize=(10, 5), dpi=150
- Variable nodes (circles, top row): v0–v7, color steelblue
- Check nodes (squares, bottom row): c0–c3, color darkorange
- Edges from H: draw line between cᵢ and vⱼ when H[i,j]==1
- Labels: vⱼ for variable nodes, cᵢ for check nodes
- No axes, clean white background
- savefig('figures/tanner-graph.png', dpi=150, bbox_inches='tight')

## Task 2: Update index.md comment
Line 133: change `<!-- será generada por lab.ipynb — Fase 3 -->` → `<!-- generada por gsd-quick (tanner-graph-fix) -->`

## Commit
`fix(quick): generar tanner-graph.png desde H_ldpc(8,4) — corrige figura rota §3.1`
Files: figures/tanner-graph.png, index.md
