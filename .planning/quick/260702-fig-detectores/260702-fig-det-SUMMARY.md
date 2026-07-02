---
slug: fig-detectores
status: complete
created: 2026-07-02
completed: 2026-07-02
commit: f7ba3e8
---

# Summary — Figura BER detectores ZF/MMSE/ML

## Hecho
1. **lab.ipynb**: nuevas celdas 12 (markdown) + 13 (code) "Figura 4b —
   Detección en el receptor", tras la celda DMT, antes de MU-MIMO. Monte
   Carlo 2×2 QPSK i.i.d. Rayleigh: detect_zf (pinv), detect_mmse
   (regularizador Nt/snr), detect_ml (fuerza bruta 16 candidatos).
   N_mc=4000, SNR 0–20 dB. Notebook ahora 20 celdas, JSON válido.
2. **figures/mimo-detectors.png** generado (ejecución real, seed 42).
   Sanity: ML < MMSE < ZF en todo el rango; @20 dB ZF 1.1e-2, MMSE 6.9e-3,
   ML 6e-4 — pendiente ML más empinada (diversidad 2 vs 1). Física correcta.
3. **index.md §3.3**: Figura 4b insertada tras la tabla comparativa, antes
   del párrafo de dualidad TX↔RX. Numeración 4b evita renumerar Fig 5–8.

## Decisiones
- Ejecución de la celda vía script extraído (celda 1 + celda nueva) en vez
  de nbconvert --execute: evita correr los Monte Carlos pesados del resto
  del notebook y el TODO precoder_zf.
- SIC no simulado (mencionado en caption): es el ejercicio natural del
  estudiante, no regalo del profe.

## Verificación
- mkdocs build --strict: pasa
- lab.ipynb: json.load OK

## Commits
- 7b89052 — fix(06-mimo): heading §6 sin LaTeX (edición manual del usuario)
- f7ba3e8 — feat(06-mimo): figura BER detectores
- (artifacts) — docs(quick-260702-fig-det): plan + summary
