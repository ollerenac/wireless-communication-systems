---
slug: precoder-zf
status: complete
created: 2026-07-02
completed: 2026-07-02
commit: 0a652f0
---

# Summary — precoder_zf implementado

## Hecho
1. **lab.ipynb celda 15**: precoder_zf implementado (np.linalg.pinv +
   normalize_precoder), líneas ZF de simulación y plot descomentadas,
   N_mc 300→2000 (piso estadístico 6e-5, curva ZF llega a ~2e-4 antes de
   caer bajo el eje).
2. **figures/mimo-mrt-zf.png** regenerado con ambas curvas.
3. **index.md caption Figura 6** corregido con datos reales: cruce ~2 dB
   (no "10–12 dB" especulado), MRT satura en piso de interferencia ~6e-2,
   ZF sin piso; nota de que el piso de MRT solo desaparece cuando M>>K (§6).

## Hallazgo
Caption original especulaba cruce 10–12 dB. Simulación real con M/K=2:
MRT toca su piso de interferencia tan pronto que ZF lo cruza ya a ~2 dB.
El "MRT gana a SNR baja" del texto §5 sigue siendo cierto pero el margen es
estrecho con M/K=2 — coherente con la teoría (MRT óptimo solo cuando M>>K).

## Decisión pedagógica
Ejercicio 3 deja de ser TODO y pasa a solución de referencia en el notebook
(pendiente del instructor desde hace sesiones). Si se quiere restaurar como
hueco para alumnos: revertir celda a `pass` + re-comentar 2 líneas.

## Verificación
- lab.ipynb JSON OK; mkdocs build --strict pasa
- Física: ZF diversidad de orden M-K+1=5 (caída abrupta), MRT floor plano ✓

## Commits
- 0a652f0 — feat(06-mimo): precoder_zf + Figura 6 completa
- (artifacts) — docs(quick-260702-zf): plan + summary
