---
slug: 260525-w
status: complete
date: 2026-05-25
---

## Resultado

§4.3 Canal Multipath ahora coincide con el Bloque 3 del notebook:

1. **Snippet**: eliminadas las líneas de generación de ruido (`SNR_lin`, `sigma2`, `noise`);
   reemplazado `y_noisy = apply_channel(...) + noise` por `y_ch = apply_channel(...)`.
2. **Prosa**: `y_noisy` → `y_ch` en el párrafo de cierre de §4.3.

## Archivos modificados
- `index.md`: ~8 líneas reemplazadas + 1 referencia de texto

## Sin modificar
- `lab.ipynb`: ground truth, no cambia.
