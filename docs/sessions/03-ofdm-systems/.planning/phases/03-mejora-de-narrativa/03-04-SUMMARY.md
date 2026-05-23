---
plan: 03-04
phase: 03-mejora-de-narrativa
status: complete
wave: 4
---

## Summary

Implementación del checkpoint D-16: inspección visual de los 4 PNGs modificados y decisión commit/revert, con corrección de bug visual (colorbar overlapping) en `zf-equalizer-qam-comparison.png`.

## What Was Built

**Task 1 — Inspección visual (human-gated):**
El usuario inspeccionó los 4 PNGs del working tree vs las versiones committed. Encontró que `zf-equalizer-qam-comparison.png` tenía el colorbar superpuesto sobre los paneles de la tercera columna — un bug visual causado por `plt.colorbar(sm2, ax=axes2[:, 2], shrink=0.8)` que roba espacio de esos subplots.

Decisión por archivo:
- `cp-illustration.png`: **commit** (turbo colormap mejora contraste)
- `ofdm-subcarriers.png`: **commit** (turbo colormap mejora contraste)
- `zf-equalizer-effect.png`: **commit** (turbo colormap mejora contraste)
- `zf-equalizer-qam-comparison.png`: **regenerar con fix** → commit

**Task 2 — Ejecución del commit/fix:**
- Se corrigió el bug de colorbar en `lab.ipynb` (cell `11e22143`): reemplazado `plt.colorbar(sm2, ax=axes2[:, 2], shrink=0.8)` por `tight_layout(rect=[0,0,0.92,1])` + `fig2.add_axes([0.93, 0.15, 0.015, 0.7])` + `fig2.colorbar(sm2, cax=cbar_ax2, ...)`.
- Se re-ejecutó `lab.ipynb` completo con `jupyter nbconvert --execute` para regenerar todas las figuras.
- Se commitearon lab.ipynb y los 4 PNGs en dos commits separados.

## Commits

| Commit | Message |
|--------|---------|
| `1fa8fac` | fix(lab): move fig2 colorbar outside subplot grid (tight_layout rect + add_axes) |
| `19f4051` | fig(03): commit re-generated figures with turbo colormap |

## Verification

- `git status --porcelain figures/*.png` → vacío (0 líneas) ✓
- Los 4 archivos PNG existen en `figures/` ✓
- El commit de figuras contiene `fig(03)` y `turbo colormap` ✓
- `index.md` no fue modificado en esta tarea ✓
- Las 4 rutas referenciadas en `index.md` siguen siendo válidas ✓

## Self-Check: PASSED

Todos los criterios de aceptación verificados:
- Decisión humana explícita registrada por archivo (commit/fix+commit)
- Working tree limpio respecto a los 4 PNGs
- Mensaje de commit sigue D-16: `fig(03): commit re-generated figures with turbo colormap`
- Bug visual corregido en lab.ipynb (ground truth) antes de regenerar
- Las referencias de imagen en `index.md` siguen siendo válidas
