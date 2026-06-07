---
slug: tanner-graph-layout
date: 2026-06-04
status: in-progress
---

# Fix: Tanner graph layout in lab.ipynb

## Goal
Corregir el layout del grafo de Tanner en la celda 7 de lab.ipynb para que los nodos de verificación estén centrados respecto a los de variable y haya suficiente separación vertical.

## Changes
1. `c_x`: cambiar `linspace(1.5, n_c + 0.5, n_c)` → `linspace(0.5, n_v - 0.5, n_c)` — centra los check nodes sobre el span completo
2. `v_y, c_y`: cambiar `1.0, 0.0` → `1.5, 0.0` — aumenta separación vertical
3. `ax.set_ylim`: cambiar `(-0.7, 1.7)` → `(-0.7, 2.2)` — preserva margen superior
4. Regenerar figures/tanner-graph.png ejecutando la celda

## File
- `docs/sessions/05-channel-coding/lab.ipynb` (celda 7)
- `docs/sessions/05-channel-coding/figures/tanner-graph.png`
