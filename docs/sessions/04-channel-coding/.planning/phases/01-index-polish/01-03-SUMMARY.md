---
phase: 01-index-polish
plan: "03"
subsystem: index.md
tags: [figures, factual-correction, mkdocs-material, figure-blocks]
dependency_graph:
  requires: [01-01, 01-02]
  provides: [FIG-01-partial, IDX-03]
  affects: [docs/sessions/04-channel-coding/index.md]
tech_stack:
  added: []
  patterns: [MkDocs-Material figure blocks, HTML figcaption]
key_files:
  created: []
  modified:
    - docs/sessions/04-channel-coding/index.md
decisions:
  - "D-04 aplicada: 2 referencias planas convertidas a bloques <figure markdown=span> con figcaption de 2+ líneas"
  - "D-05 aplicada: placeholder <figure> para tanner-graph.png insertado después del mermaid en §3.1; mermaid intacto"
  - "D-07 aplicada: $10^{-1.5} corregido a $10^{-1} en Introducción y (Rule 1) en ejemplo numérico §5"
metrics:
  duration: "~4 min"
  completed: "2026-05-26T08:34:29Z"
  tasks_completed: 2
  tasks_total: 2
  files_modified: 1
---

# Phase 1 Plan 03: Figure Block Conversion + Factual Corrections Summary

**One-liner:** Tres bloques `<figure markdown="span">` con figcaptions detallados y corrección factual de umbral BER pre-FEC ($10^{-1.5}$ → $10^{-1}$) según sesión 02.

## Tasks Completed

| Task | Name | Commit | Files |
|------|------|--------|-------|
| 1 | Convertir referencias planas a `<figure>` (D-04) | 3306cc2 | index.md |
| 2 | Placeholder tanner-graph + corrección intro (D-05, D-07) | 3acff5c | index.md |

## What Was Built

### Task 1 — Conversión de referencias planas (D-04)

Reemplazadas las dos referencias `![alt](path)` por bloques `<figure markdown="span">` completos:

- **Figura 1 (shannon-capacity.png):** figcaption 2 líneas describiendo la curva Shannon, puntos de operación por modulación, flechas de ganancia de codificación, y límite de Eb/N0 = -1.59 dB. Comentario `<!-- generada por celda 3 de lab.ipynb -->`.
- **Figura 2 (waterfall-curves.png):** figcaption 2 líneas describiendo las curvas waterfall de LDPC, Polar y BPSK sin código. Comentario `<!-- será generada por lab.ipynb — Fase 2 -->`. El párrafo descriptivo que seguía a la referencia plana fue absorbido en el figcaption y eliminado del cuerpo del texto.

### Task 2 — Placeholder tanner-graph + corrección factual (D-05, D-07)

- **Figura 3 (tanner-graph.png):** Placeholder `<figure>` insertado en §3.1 inmediatamente después del texto en cursiva `*Grafo de Tanner para el código (7,4)...*` y antes del párrafo "La dispersidad del grafo...". El bloque mermaid inline permanece intacto. El placeholder incluye figcaption de 2 líneas y comentario `<!-- será generada por lab.ipynb — Fase 3 -->`.
- **Corrección D-07:** `$10^{-1.5}$` → `$10^{-1}$` en el párrafo de Introducción. Verificado contra sesión 02 línea 267: "de $10^{-1}$ o superior".

## Deviations from Plan

### Auto-fixed Issues

**1. [Rule 1 - Bug] Corrección de $10^{-1.5}$ también en §5 ejemplo numérico**
- **Found during:** Task 2
- **Issue:** La acceptance criteria del plan exige `grep '10^{-1.5}' index.md` devuelva 0 (cero coincidencias). Tras corregir el intro, persistía una aparición en el Paso 2 del ejemplo numérico end-to-end (§5, línea 268), donde también figuraba el umbral BER pre-FEC de $10^{-1.5}$ — valor igualmente incorrecto según la sesión 02.
- **Fix:** Corregido a `$10^{-1}$` para consistencia factual con el resto del documento.
- **Files modified:** docs/sessions/04-channel-coding/index.md
- **Commit:** 3acff5c

## Verification Results

```
<figure markdown="span"> blocks: 3  (esperado: 3) ✓
Bare image refs sueltas:        0  (esperado: 0) ✓
mermaid intacto:                1  (esperado: >=1) ✓
10^{-1.5} eliminado:            0  (esperado: 0) ✓
10^{-1} presente:               2  (esperado: >=1) ✓
86% presente:                   1  (esperado: 1) ✓
tanner-graph.png:               1  (esperado: 1) ✓
Fase 3 comment:                 2  (esperado: >=1) ✓
generada por celda 3:           1  (esperado: 1) ✓
**Figura N.** labels:           3  (esperado: 3) ✓
```

## Known Stubs

- **Figura 2 (waterfall-curves.png):** La imagen `figures/waterfall-curves.png` existe en el repositorio pero la figura real que usará el site será regenerada en Fase 2. El placeholder en el `<figure>` block es correcto y honesto con este estado.
- **Figura 3 (tanner-graph.png):** La imagen `figures/tanner-graph.png` NO existe todavía. Se generará en Fase 3. El placeholder es intencional y se documenta en el comentario HTML del bloque.

## Self-Check: PASSED

- [x] index.md modificado existe: `/home/researcher/Teaching/uni/2026/wireless-communication-systems/docs/sessions/04-channel-coding/index.md`
- [x] Commit 3306cc2 existe (Task 1)
- [x] Commit 3acff5c existe (Task 2)
- [x] 3 bloques `<figure>` presentes
- [x] 0 referencias planas sueltas
- [x] mermaid de §3.1 intacto
- [x] $10^{-1.5}$ eliminado de todo el archivo
- [x] 86% permanece en Introducción
