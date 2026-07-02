---
slug: det-rx-deteccion-receptor
status: complete
created: 2026-07-02
completed: 2026-07-02
commit: ac35bf1
---

# Summary — Detección en el receptor (§3.3)

## Hecho
Nueva **§3.3 "El problema dual: detección en el receptor"** en
`docs/sessions/06-mimo-systems/index.md`, tras §3.2, antes del puente a DMT.
Cierra la asimetría TX/RX: la lección enseñaba precodificación (TX) sin el
dual receptor.

Contenido:
- Motivación: sin CSIT el receptor separa la mezcla solo (analogía mesa de
  mezclas desde el lado altavoces).
- ZF (dual del precoder ZF §5, amplifica ruido) y MMSE (regularizado).
- ML (óptimo, exponencial) y SIC/V-BLAST (da mecanismo al nombre del pie de
  Fig 5).
- Ejemplo a mano reusando H=[[1,0.5],[0.5,1]] del §3.1: (H^H H)^-1 diagonal
  = 2,22 → factor de amplificación de ruido ZF concreto.
- Tabla comparativa ZF/MMSE/ML/SIC + nota de dualidad TX↔RX.
- Concept-check ??? question.
- Puente reescrito hacia DMT.

## Decisiones
- Subsección §3.3 en vez de sección nueva → no renumera §4/§5/§6 ni sus
  cross-refs (menos churn, menos riesgo).
- Text-first, cero figuras nuevas: reusa el ancla 2×2 del §3.1 → coherencia
  con la pedagogía existente. Figura BER-vs-SNR de detectores queda como
  posible extensión futura (lab.ipynb).
- \mathbf en todas las ecuaciones (convención del repo).

## Verificación
- mkdocs build --strict: pasa (solo INFO de CLAUDE.md fuera de nav,
  intencionales).

## Commits
- ac35bf1 — feat(06-mimo): §3.3 detección en receptor
- (artifacts) — docs(quick-260702-det-rx): plan + summary
