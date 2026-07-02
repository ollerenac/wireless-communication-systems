---
slug: fig-detectores
created: 2026-07-02
mode: quick-inline
---

# Quick Task — Figura BER detectores ZF/MMSE/ML para §3.3

## Problema
§3.3 (detección RX) quedó text-first sin evidencia visual. Falta curva BER
que muestre: ZF amplifica ruido, MMSE lo balancea, ML óptimo con mejor
pendiente (diversidad).

## Solución
1. lab.ipynb: insertar tras celda DMT (11) par markdown+code
   "Figura 5b — Detección en el receptor": sim Monte Carlo 2×2 QPSK,
   detectores ZF (pinv), MMSE (regularizado Nt/snr), ML (fuerza bruta 16
   hipótesis). Genera figures/mimo-detectors.png.
2. Ejecutar celda (script extraído: celda 1 imports + nueva celda) → PNG.
3. index.md §3.3: figura tras la tabla comparativa, figcaption estilo
   existente.

## Verificación
- PNG generado, curvas ordenadas ML ≤ MMSE ≤ ZF
- lab.ipynb JSON válido
- mkdocs build --strict pasa

## Commits
1. feat(06-mimo): figura BER detectores ZF/MMSE/ML (lab + §3.3)
2. docs(quick-260702-fig-det): plan + summary
