---
phase: 01-index-polish
plan: "01"
subsystem: index.md
tags: [narrative, hooks, polish, index]
dependency_graph:
  requires: []
  provides: [IDX-01]
  affects: [index.md]
tech_stack:
  added: []
  patterns: ["La pregunta natural es... La respuesta es... hook pattern (sesión 03 style)"]
key_files:
  created: []
  modified:
    - docs/sessions/04-channel-coding/index.md
decisions:
  - "9 hooks cobertura total (D-01): todas las sub-secciones §1, §2, §3.1, §3.2, §3.3, §4.1, §4.2, §4.3, §5 — no solo §3.2 y §4.2 como el requisito mínimo IDX-01"
  - "Objeto ancla matemático por sección (D-02): cada hook ancla al último objeto matemático introducido — límite Shannon, G_c, ciclos largos, waterfall/ĉ_v, factor Z, Z(W_N^(i)), CA-Polar SCL, 1706 bits, throughput 160 Mbit/s"
  - "Corrección gramatical: 'La respuesta son' → 'La respuesta es' en hooks §3.3 y §4.2 para cumplir criterio done exacto del plan"
metrics:
  duration_minutes: 18
  completed_date: "2026-05-26"
  tasks_completed: 2
  files_modified: 1
---

# Phase 1 Plan 01: Narrative Hooks — Summary

**One-liner:** 9 hooks "La pregunta natural es...La respuesta es" insertados en los cierres de §1, §2, §3.1, §3.2, §3.3, §4.1, §4.2, §4.3 y §5 de index.md, cada uno anclado al último objeto matemático de la sección y con puente narrativo explícito hacia la sección siguiente, siguiendo el patrón calibrado de sesión 03.

## Tasks Completed

| Task | Name | Commit | Files |
|------|------|--------|-------|
| 1 | Leer referencias y mapear posiciones de hooks | — (lectura pura) | index.md (lectura), sesión 03 (referencia) |
| 2 | Insertar los 9 hooks en index.md | 6bdae05 | index.md (+18 líneas) |

## Verification Results

```
grep -c "La pregunta natural es" index.md  → 9  ✓
grep -c "La respuesta es" index.md         → 9  ✓
grep -A2 "La pregunta natural es" | grep '```'  → 0  ✓
```

Distribución de hooks (líneas en el archivo final):
- Línea 67: §1 — límite Shannon $E_b/N_0 \geq \ln 2 = -1{,}59$ dB
- Línea 95: §2 — ganancia de codificación $G_c \approx 8$ dB
- Línea 129: §3.1 — grafo de Tanner disperso / ciclos largos
- Línea 156: §3.2 — decisión $\hat{c}_v$ y curva waterfall
- Línea 167: §3.3 — factor de lifting $Z$ y matrices expandidas
- Línea 196: §4.1 — parámetro de Bhattacharyya $Z(W_N^{(i)})$
- Línea 209: §4.2 — CA-Polar con SCL $L=8$
- Línea 223: §4.3 — bloque máximo 1706 bits Polar vs 8448 LDPC
- Línea 260: §5 — throughput $R \approx 160$ Mbit/s ejemplo end-to-end

## Deviations from Plan

### Auto-fixed Issues

**1. [Rule 1 - Bug] Ajuste del conteo de referencia en Task 1**
- **Found during:** Task 1 verificación
- **Issue:** El plan indicaba "grep retorna ≥11" para sesión 03, pero la sesión 03 tiene 8 instancias del patrón. La discrepancia es entre el PLAN.md y la realidad del archivo de referencia.
- **Fix:** Se ejecutó Task 1 con el resultado real (8 instancias). El patrón de referencia está completamente disponible — las 8 instancias son suficientes para calibrar tono y densidad. No afecta la calidad de los 9 hooks escritos.
- **Files modified:** ninguno
- **Commit:** N/A (no requirió cambio)

**2. [Rule 1 - Bug] Corrección gramatical "La respuesta son" → "La respuesta es"**
- **Found during:** Task 2 verificación final
- **Issue:** Los hooks de §3.3 y §4.2 usaban "La respuesta son" (gramaticalmente correcto con sustantivos plurales), pero el criterio done del plan exige exactamente "La respuesta es" en todos los hooks.
- **Fix:** Reformulado: "La respuesta son los códigos Polar" → "La respuesta es la familia de códigos Polar"; "La respuesta son los canales" → "La respuesta es el conjunto de canales de control".
- **Files modified:** index.md
- **Commit:** incluido en 6bdae05

## Known Stubs

Ninguno — este plan solo inserta párrafos de texto narrativo sin datos ni figuras dinámicas.

## Threat Flags

Ninguno — solo modificaciones de texto plano en markdown, sin nuevos endpoints, rutas de autenticación ni cambios de esquema.

## Self-Check: PASSED

- [x] index.md modificado existe: `/home/researcher/Teaching/uni/2026/wireless-communication-systems/docs/sessions/04-channel-coding/index.md`
- [x] Commit 6bdae05 existe en git log
- [x] 9 hooks "La pregunta natural es" en index.md
- [x] 9 instancias "La respuesta es" en index.md
- [x] 0 backticks dentro de hooks
