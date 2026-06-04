---
phase: 06-qa-publicaci-n
plan: "02"
subsystem: docs/sessions/05-channel-coding
tags: [index, figures, polar, caption-numbering, mkdocs, qa]
dependency_graph:
  requires: [06-01]
  provides: [IDX-04]
  affects: [docs/sessions/05-channel-coding/index.md]
tech_stack:
  added: []
  patterns:
    - "figure markdown=span con figcaption markdown=1 para todas las figuras de la sesión"
    - "comentarios HTML de trazabilidad figura-celda verificados contra índices reales del notebook"
key_files:
  created: []
  modified:
    - docs/sessions/05-channel-coding/index.md
decisions:
  - "Insertar polar-butterfly.png justo después de la descripción butterfly G_2/G_N (antes de Bhattacharyya), no después de las fórmulas"
  - "Insertar polar-polarization.png justo antes de la pregunta natural de 4.1 (cierre lógico de polarización del canal)"
  - "Corregir celda 19→20 para ofdm-ldpc-ber.png (Rule 1 — bug descubierto al auditar todos los comentarios de origen)"
metrics:
  duration: "~15 minutos"
  completed_date: "2026-06-04"
  tasks_completed: 3
  files_modified: 1
---

# Phase 06 Plan 02: QA — Auditoría de figuras y trazabilidad (IDX-04) Summary

**One-liner:** index.md pasa mkdocs build --strict con 9 figuras trazadas a celdas reales del notebook, figuras Polar visibles en sección 4.1 y numeración secuencial 1..9 sin duplicados.

## Tasks Completed

| Task | Name | Commit | Files |
|------|------|--------|-------|
| 1 | Añadir figuras Polar en 4.1 y corregir comentarios de origen | `f43c24c` | `index.md` |
| 2 | Renumerar captions 1..9 en orden de documento | `c94e57c` | `index.md` |
| 3 | Validar build MkDocs y trazabilidad final figura-archivo | (verificación pura) | — |

## Verification

- `grep -c 'polar-butterfly.png' index.md` → 1 (dentro de `<figure markdown="span">` en sección 4.1)
- `grep -c 'polar-polarization.png' index.md` → 1 (dentro de `<figure markdown="span">` en sección 4.1)
- `grep -q 'generada por celda 13' index.md` → exit code 1 (sin coincidencias)
- `python3 verify_fignums.py` → `[1, 2, 3, 4, 5, 6, 7, 8, 9]` OK
- `python3 verify_figs_exist.py` → 9 figuras — todas presentes
- `mkdocs build --strict --site-dir /tmp/mkdocs-qa-06` → exit code 0, sin errores
- `/tmp/mkdocs-qa-06/sessions/05-channel-coding/index.html` existe
- Todas las referencias `figures/*.png` envueltas en bloques `<figure markdown="span">`

## Mapa figura-celda final verificado

| Figura | PNG | Celda notebook | Comentario en index.md |
|--------|-----|----------------|------------------------|
| 1 | shannon-sphere-packing.png | gsd-quick (excepción) | `generada por gsd-quick` |
| 2 | shannon-capacity.png | celda 3 | `generada por celda 3` |
| 3 | tanner-graph.png | celda 7 | `generada por celda 7` |
| 4 | bp-messages.png | celda 9 | `generada por celda 9` |
| 5 | ldpc-ber-waterfall.png | celda 10 | `generada por celda 10` |
| 6 | polar-butterfly.png | celda 15 | `generada por celda 15` |
| 7 | polar-polarization.png | celda 17 | `generada por celda 17` |
| 8 | waterfall-curves.png | celda 18 | `generada por celda 18` |
| 9 | ofdm-ldpc-ber.png | celda 20 | `generada por celda 20` |

## Deviations from Plan

### Auto-fixed Issues

**1. [Rule 1 - Bug] Comentario origen ofdm-ldpc-ber.png: celda 19 → celda 20**
- **Found during:** Task 1 (al auditar todos los comentarios de origen)
- **Issue:** El bloque `ofdm-ldpc-ber.png` decía "generada por celda 19 de lab.ipynb"; la celda 19 es un nodo MARKDOWN (encabezado del Ej. 6). La celda que ejecuta `plt.savefig('figures/ofdm-ldpc-ber.png')` es la celda 20.
- **Fix:** Actualizado el comentario a "generada por celda 20 de lab.ipynb"
- **Files modified:** `docs/sessions/05-channel-coding/index.md`
- **Commit:** `f43c24c`

## Known Stubs

None — todas las figuras están cableadas a celdas de código reales. La única excepción documentada es `shannon-sphere-packing.png`, generada por `gsd-quick` (sin celda de notebook), acordado en el plan como excepción OK.

## Threat Surface Scan

Ningún nuevo endpoint de red, ruta de auth, ni acceso a archivos fuera del directorio de la sesión. El site-dir del build MkDocs se aisló en `/tmp/mkdocs-qa-06`.

## Self-Check: PASSED

- FOUND: `docs/sessions/05-channel-coding/index.md`
- FOUND commit `f43c24c` (Task 1)
- FOUND commit `c94e57c` (Task 2)
- FOUND: `/tmp/mkdocs-qa-06/sessions/05-channel-coding/index.html`
- `grep -c 'polar-butterfly.png' index.md` = 1
- `grep -c 'polar-polarization.png' index.md` = 1
- Caption sequence = [1,2,3,4,5,6,7,8,9]
- 9/9 figuras presentes en disco
- mkdocs build --strict exit code 0
