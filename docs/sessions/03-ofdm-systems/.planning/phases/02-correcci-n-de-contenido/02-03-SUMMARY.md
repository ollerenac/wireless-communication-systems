---
phase: 02-correcci-n-de-contenido
plan: "03"
subsystem: index.md
tags:
  - snippets
  - figures
  - python
  - mkdocs
dependency_graph:
  requires:
    - "02-01-SUMMARY: mmse-vs-zf-constellation.png versionada en git (D-03)"
    - "02-02-SUMMARY: fórmulas LaTeX corregidas; index.md en 1326 líneas"
    - "01-AUDIT-FINDINGS.md: MINOR-02/03/04 con texto exacto a reemplazar"
  provides:
    - "index.md con snippet MMSE alineado con lab.ipynb celda 81830cd0 (MINOR-03)"
    - "index.md con snippet LS alineado con lab.ipynb celda 23ad1479 (MINOR-04)"
    - "index.md §4.8 con <figure> referenciando mmse-vs-zf-constellation.png (MINOR-02/D-03)"
    - "0 referencias rotas a figuras en index.md"
    - "0 figuras huérfanas no exceptuadas"
  affects:
    - "Fase 3 verificación: index.md listo para publicar"
tech_stack:
  added: []
  patterns:
    - "Ediciones Edit tool con old_string/new_string exactos — sin sed, sin reemplazos masivos"
    - "Ancla textual (no número de línea) para localizar punto de inserción en §4.8"
key_files:
  created: []
  modified:
    - docs/sessions/03-ofdm-systems/index.md
decisions:
  - "D-09 aplicado: snippets MMSE y LS expandidos a funciones completas con firma y docstring del notebook"
  - "D-03 cerrado: mmse-vs-zf-constellation.png referenciada en §4.8 como Figura 3"
  - "D-04 respetado: channel-estimation-pilots, qpsk-decision-regions, ofdm-time-domain, cp-effect-constellation NO referenciadas en index.md"
  - "Numeración Figura 3 verificada: no existía Figura 3 previa en el documento"
metrics:
  duration: "~10 minutos"
  completed_date: "2026-05-22"
  tasks_completed: 4
  files_modified: 1
---

# Phase 02 Plan 03: Alineación de Snippets MMSE/LS y Figura §4.8 — MINOR-02/03/04 resueltos

**One-liner:** Tres ediciones puntuales en `index.md` reemplazan los snippets inline de MMSE y estimación LS con las funciones invocables completas del notebook (`mmse_equalizer` y `ls_channel_estimate`) e insertan un bloque `<figure>` en §4.8 que liga la figura antes huérfana `mmse-vs-zf-constellation.png` al texto, cerrando los requisitos CORR-01/02/03 de Fase 2.

## What Was Built

Tres ediciones en `docs/sessions/03-ofdm-systems/index.md`:

1. **MINOR-03 (§4.6 línea ~806):** El snippet inline de dos líneas (`SNR_lin = ...`, `X_hat = ...`) fue reemplazado por la función completa `mmse_equalizer(Y, h, N, SNR_dB)` con docstring y cuerpo de 3 líneas — coincide exactamente con la celda `81830cd0` de `lab.ipynb`. El archivo creció en +3 líneas netas.

2. **MINOR-04 (§4.7 línea ~886):** El snippet inline de nueve líneas (con `pilot_spacing`, comentarios y `np.interp` sobre array complejo) fue reemplazado por la función completa `ls_channel_estimate(Y, pilot_idx, X_pilot, N)` con interpolación separada real/imag — coincide con la celda `23ad1479` de `lab.ipynb`. El archivo decreció en -3 líneas netas.

3. **MINOR-02/D-03 (§4.8 después del párrafo LLR):** Se insertó un bloque `<figure markdown="span">` referenciando `figures/mmse-vs-zf-constellation.png` (Figura 3) entre el párrafo de cierre de §4.8 y el divider `---`. La figura antes huérfana en disco queda ahora ligada al texto de la sección MMSE/ZF. El archivo creció en +5 líneas netas.

**Resultado final:** `wc -l index.md` = 1331 líneas (1326 de Plan 02-02 +3 −3 +5).

## Tasks Completed

| Task | Name | Commit | Files |
|------|------|--------|-------|
| 1 | Alinear snippet MMSE (MINOR-03) | d6309e3 | index.md |
| 2 | Alinear snippet LS (MINOR-04) | d6309e3 | index.md |
| 3 | Insertar bloque figure §4.8 (D-03/MINOR-02) | d6309e3 | index.md |
| 4 | Verificación final + commit unificado | d6309e3 | index.md |

*Las tres ediciones van en un único commit según las instrucciones del plan.*

## Verification Results

- `grep -c "def mmse_equalizer(Y, h, N, SNR_dB):"` → 1 (exactamente una vez)
- `grep -c '"""MMSE: regulariza la inversión del canal'` → 1
- `grep -c "return (np.conj(H) / (np.abs(H)**2 + 1/SNR)) * Y"` → 1 (sin `_lin` — API del notebook)
- `grep -c "def ls_channel_estimate(Y, pilot_idx, X_pilot, N):"` → 1
- `grep -c '"""Estimación LS en pilotos + interpolación lineal'` → 1
- `grep -c "1j * np.interp(np.arange(N), pilot_idx, H_ls.imag))"` → 1
- `grep -c "return H_est"` → 1
- `grep -c "pilot_spacing = 8"` → 0 (snippet inline eliminado)
- `grep -c "figures/mmse-vs-zf-constellation.png"` → 1 (anteriormente 0)
- `grep -c "**Figura 3.**"` → 1
- `grep -c "Constelaciones QAM tras ecualización ZF"` → 1
- Posición verificada con `awk '/se tratará en detalle en la Sesión 04/,/^---$/'` → figura encontrada
- `grep -A3 mmse-vs-zf-constellation.png | grep 'markdown="1"'` → 1 (figcaption con atributo correcto)
- 0 referencias rotas a figuras (12 refs × 12 archivos en disco = 0 rotas)
- 0 huérfanas no exceptuadas (6 exceptuadas: D-04 × 4 + ofdm-ber + ofdm-per-subcarrier-ber)
- `git show --name-only HEAD` lista exclusivamente `docs/sessions/03-ofdm-systems/index.md`
- Commit contiene tokens: MINOR-02, MINOR-03, MINOR-04, CORR-01, CORR-02, CORR-03

**Estado del checklist de `01-AUDIT-FINDINGS.md`:** todos los ítems resueltos — BLOCKER-S.01/S.02 (Plan 02-02), BLOCKER-S.03/S.04/S.05 (Plan 02-01), MINOR-01 (Plan 02-02), MINOR-02/03/04 (este plan). `index.md` no contiene errores de contenido ni referencias rotas.

## Deviations from Plan

**1. [Rule 1 - Discrepancy] Diferencia en conteo de líneas netas para Task 3 (+5 vs +8 esperado)**
- **Encontrado durante:** Task 3 verificación post-edit
- **Problema:** El plan especificaba "+8 líneas netas" para la inserción de la figura en §4.8. El resultado real fue +5 líneas.
- **Análisis:** El plan calculó old_string con 2 líneas y new_string con 10 líneas (diferencia de 8). Sin embargo, old_string incluye explícitamente 3 líneas: LLR paragraph + blank line + `---`. El new_string tiene 8 líneas: LLR paragraph + blank + `<figure>` + `  ![...]` + `  <figcaption>` + `</figure>` + blank + `---`. La diferencia correcta es 8 − 3 = +5 líneas. El plan tenía un error de conteo de 3 en su criterio de aceptación.
- **Resultado:** La inserción es estructuralmente correcta y consistente con el patrón Figura 2 (líneas 233–236). Todas las verificaciones de contenido y posición pasaron. No se requiere corrección.
- **Impacto:** Ninguno — el acceptance criterion numérico del plan (+8) era incorrecto; el criterio funcional (figura en §4.8, antes del `---`, con `markdown="1"`) se cumple.

## Known Stubs

Ninguno — las ediciones reemplazan código inline con funciones del notebook y agregan una referencia a figura existente. No hay placeholders ni TODOs.

## Threat Surface Scan

No nuevas superficies de seguridad introducidas. Las ediciones modifican bloques Python en markdown pedagógico y agregan un bloque HTML `<figure>` — sin endpoints, rutas de auth, ni cambios de esquema.

## Self-Check: PASSED

- [x] `docs/sessions/03-ofdm-systems/index.md` modificado y commiteado
- [x] Commit `d6309e3` existe en el log
- [x] `def mmse_equalizer(Y, h, N, SNR_dB):` presente exactamente 1 vez
- [x] `def ls_channel_estimate(Y, pilot_idx, X_pilot, N):` presente exactamente 1 vez
- [x] `figures/mmse-vs-zf-constellation.png` referenciada exactamente 1 vez
- [x] `**Figura 3.**` presente exactamente 1 vez (sin Figura 3 previa en el documento)
- [x] 0 referencias rotas a figuras
- [x] 0 figuras huérfanas no exceptuadas
- [x] Commit message contiene CORR-01, CORR-02, CORR-03, MINOR-02, MINOR-03, MINOR-04
- [x] `git show --name-only HEAD` lista solo `docs/sessions/03-ofdm-systems/index.md`
- [x] `wc -l index.md` = 1331
