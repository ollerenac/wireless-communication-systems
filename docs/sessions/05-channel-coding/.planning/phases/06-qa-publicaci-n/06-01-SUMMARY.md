---
phase: 06-qa-publicaci-n
plan: "01"
subsystem: docs/sessions/05-channel-coding
tags: [notebook, nbconvert, qa, figures, ldpc, polar, waterfall]
dependency_graph:
  requires: [05-01]
  provides: [LAB-04, LAB-05, IDX-04-partial]
  affects: [docs/sessions/05-channel-coding/lab.ipynb, docs/sessions/05-channel-coding/figures/]
tech_stack:
  added: []
  patterns:
    - "nbconvert --execute --inplace para ejecución limpia reproducible"
    - "Cota de unión Bhattacharyya como sustituto de curva Polar (decodificador diferido)"
key_files:
  created: []
  modified:
    - docs/sessions/05-channel-coding/lab.ipynb
    - docs/sessions/05-channel-coding/figures/waterfall-curves.png
decisions:
  - "Cota de unión Bhattacharyya para Polar en waterfall (decodificador SC N=64 diferido Fase 4 / LAB-02)"
  - "Bloque MC BER SC vs SCL eliminado de celda 17 — no reimplementar en QA"
metrics:
  duration: "~30 minutos"
  completed_date: "2026-06-04"
  tasks_completed: 3
  files_modified: 2
---

# Phase 06 Plan 01: QA — Notebook ejecutable end-to-end (LAB-04) Summary

**One-liner:** Notebook lab.ipynb ejecuta limpio con nbconvert (14 celdas, exit 0) eliminando crash NotImplementedError Polar SC/SCL y añadiendo celda generadora de waterfall-curves.png.

## Tasks Completed

| Task | Name | Commit | Files |
|------|------|--------|-------|
| 1 | Eliminar crash celda 17 (SC/SCL NotImplementedError) | `3252b92` | `lab.ipynb` |
| 2 | Añadir celda generadora waterfall-curves.png | `e9a5a03` | `lab.ipynb` |
| 3 | Ejecución limpia end-to-end nbconvert (LAB-04) | `2c8eb7e` | `lab.ipynb`, `figures/waterfall-curves.png` |

## Verification

- `jupyter nbconvert --execute lab.ipynb` → exit code 0
- 14 celdas de código, execution_count 1..14 secuencial, sin outputs de error
- `figures/waterfall-curves.png` (101902 bytes) generada por celda nueva en posición 18
- `figures/polar-polarization.png` (63752 bytes) generada por celda 17 (FIG-07 preservada)
- Todas las figuras declaradas del notebook existen en disco con mtime reciente

## Deviations from Plan

None — plan ejecutado exactamente como escrito.

## Known Stubs

- Celda 16: `sc_decode_polar` y `scl_decode_polar` siguen siendo `raise NotImplementedError` (intencional, scope Fase 4 / LAB-02)
- Curva Polar en `waterfall-curves.png` es cota de unión Bhattacharyya teórica (etiquetada explícitamente), no simulación SC (intencional, scope Fase 4 / LAB-02)

## Key Decisions Made

1. **No reimplementar decodificador SC/SCL en QA:** El bug de convención kron documentado en celda 16 requiere cambio arquitectural (transponer `F` en `build_polar_G`). Reimplementarlo estaba fuera del mandato LAB-04. La comparativa SC vs SCL queda diferida a Fase 4 / LAB-02.

2. **Cota Bhattacharyya para curva Polar waterfall:** Dado que el decodificador SC está diferido, la curva Polar en `waterfall-curves.png` se genera como cota de unión Bhattacharyya `P_b ≤ Σ Z(info_idx) / k` normalizada por Eb/N0. La leyenda la identifica explícitamente como cota teórica.

## Self-Check: PASSED

- FOUND: docs/sessions/05-channel-coding/lab.ipynb
- FOUND: docs/sessions/05-channel-coding/figures/waterfall-curves.png
- FOUND: docs/sessions/05-channel-coding/figures/polar-polarization.png
- FOUND: .planning/phases/06-qa-publicaci-n/06-01-SUMMARY.md
- FOUND commit 3252b92 (Task 1)
- FOUND commit e9a5a03 (Task 2)
- FOUND commit 2c8eb7e (Task 3)
- ALL ACCEPTANCE CRITERIA PASSED
