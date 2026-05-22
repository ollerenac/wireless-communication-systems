# Phase 2: Corrección de Contenido - Discussion Log

> **Audit trail only.** Do not use as input to planning, research, or execution agents.
> Decisions are captured in CONTEXT.md — this log preserves the alternatives considered.

**Date:** 2026-05-22
**Phase:** 02-correcci-n-de-contenido
**Areas discussed:** Estrategia para figuras generadas, Figuras huérfanas, Verificación de fórmulas matemáticas, Alcance de corrección de snippets

---

## Estrategia para figuras generadas

| Opción | Descripción | Seleccionada |
|--------|-------------|--------------|
| Commitear las figuras al repo | Solución simple: repo auto-contenido | ✓ |
| No commitear — ejecutar notebook en CI | Más robusto a largo plazo pero fuera del alcance de 8h | |
| Commitear todas las figuras nuevas | Incluye las 4 huérfanas también | |

**Nombre canónico de figura BER:** `ofdm-ber-equalizers.png` (es el que genera el notebook) — mantener en index.md tal como está.

---

## Figuras huérfanas

| Opción | Descripción | Seleccionada |
|--------|-------------|--------------|
| Agregar mmse-vs-zf-constellation.png en §4.8 | Enriquece la sección con figura relevante | ✓ |
| Dejar sin referenciar | Commitear pero no tocar index.md | |

| Opción | Descripción | Seleccionada |
|--------|-------------|--------------|
| Commitear 4 figuras de ejercicios sin referenciar | Repo auto-contenido, sin alterar index.md fuera de scope | ✓ |
| Ignorar (no commitear) | No causan referencias rotas | |

---

## Verificación de fórmulas matemáticas

| Opción | Descripción | Seleccionada |
|--------|-------------|--------------|
| Corregir directamente sin checkpoint | Errores bien documentados; revisión vía git diff | ✓ |
| Corregir con checkpoint human-verify | Aprobación explícita por fórmula | |

**§2 BLOCKER-S.01:** Corregir receptor de `1/N` → `1/√N`; resultado debe ser `X[k]` (recomendado) ✓

**§6 BLOCKER-S.02:** Corregir fórmula Y actualizar etiqueta `"overhead CP"` → `"eficiencia temporal"` ✓

---

## Alcance de corrección de snippets

| Opción | Descripción | Seleccionada |
|--------|-------------|--------------|
| Mostrar firma de función completa en index.md | Consistencia total con notebook | ✓ |
| Dejar inline, agregar nota | Mínima intervención | |

**MINOR-01:** Corregir también nota desplegable §2 línea 249 (factor 1/N → 1/√N) ✓

---

## Claude's Discretion

- Ubicación exacta de referencia a mmse-vs-zf-constellation.png dentro de §4.8
- Redacción del caption/alt-text de la figura nueva
- Orden de commits (por BLOCKER primero vs por sección)
