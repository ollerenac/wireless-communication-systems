---
quick_id: 260525-x
slug: fig7-colorbar-fix
date: 2026-05-25
status: complete
---

# Summary: Fix colorbar overlap in Figura 7

## What was done

Regenerated `figures/zf-noise-amplification.png` with the colorbar placed outside the subplot grid.

**Root cause:** La figura original usaba `plt.colorbar(sm, ax=axes[1])` que roba espacio del panel derecho. Resultado: la colorbar se solapaba con las barras del gráfico.

**Fix:** `plt.tight_layout(rect=[0, 0, 0.92, 1])` + `fig.add_axes([0.93, 0.12, 0.015, 0.72])` reserva un carril de 8% a la derecha del grid para la colorbar. El PNG se redujo de 118 KB → 87 KB (menos padding innecesario).

## Files changed

- `figures/zf-noise-amplification.png` — regenerada, colorbar a la derecha sin solapamiento
