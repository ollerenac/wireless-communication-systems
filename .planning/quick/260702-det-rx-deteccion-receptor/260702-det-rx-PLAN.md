---
slug: det-rx-deteccion-receptor
created: 2026-07-02
mode: quick-inline
---

# Quick Task — Detección en el receptor (§3.3 nueva)

## Problema
Lección enseña precodificación TX (SVD §3, MRT/ZF §5) casi sin el dual RX.
Multiplexación espacial sin CSIT necesita detector en recepción. V-BLAST
aparece solo en pie de Figura 5 — nombrado, nunca explicado. Asimetría
pedagógica: estudiante forma haces pero no sabe des-mezclar en el receptor.

## Solución (text-first, sin figuras nuevas)
Insertar **§3.3 "El problema dual: detección en el receptor"** tras §3.2,
antes del puente a DMT. No renumera secciones (subsección de §3).

Contenido:
- Setup: sin CSIT, RX conoce H (pilotos), recupera x de y=Hx+n solo.
- Detectores lineales: ZF (H^+, cancela interferencia, amplifica ruido —
  dual del precoder ZF §5), MMSE (balancea ruido/interferencia).
- No lineales: ML (óptimo, costo exponencial), SIC/V-BLAST (por capas — el
  nombre del pie de Fig 5).
- Ejemplo a mano reusando H=[[1,0.5],[0.5,1]] del §3.1: (H^H H)^-1 diagonal
  = 2,22 → factor de amplificación de ruido ZF concreto.
- Tabla comparativa ZF/MMSE/ML/SIC.
- ??? question concept-check.
- Puente a DMT: V-BLAST ya tiene mecanismo.

## Verificación
- mkdocs build --strict pasa
- ecuaciones con \mathbf (no \boldsymbol)

## Commits
1. feat(06-mimo): §3.3 detección en receptor (ZF/MMSE/ML/SIC + ejemplo 2×2)
2. docs(quick-260702-det-rx): plan + summary
