---
phase: quick-260701-mhk
plan: 01
subsystem: docs/sessions
tags: [mimo, pedagogy, spanish, mkdocs]
requires: []
provides:
  - "Sesión 06 MIMO con arco intuición → ejemplo → formalismo por sección"
  - "Ejemplo numérico 2×2 resuelto a mano (SVD + capacidad)"
  - "Sección Ejercicios de Asimilación con 4 drills + soluciones"
affects: []
tech-stack:
  added: []
  patterns: ["??? question / ??? example admonitions colapsables (estilo sesión 05)"]
key-files:
  created: []
  modified:
    - docs/sessions/06-mimo-systems/index.md
decisions:
  - "Todo el andamiaje nuevo va en prosa/admonitions sin ecuaciones numeradas nuevas → las 16 ecuaciones \\tag{1}–\\tag{16} conservan su numeración original sin renumerar"
  - "Se añadió subtítulo #### 3.2 'El caso general' para que el #### 3.1 (ejemplo 2×2) no quede como subsección huérfana"
  - "Decimales con coma española ({,}) en math mode, siguiendo el precedente de la sesión 05"
  - "Drills nombrados A1–A4 para no colisionar con los Ejercicios 1–4 del laboratorio"
metrics:
  duration: "10m"
  completed: "2026-07-01"
status: complete
---

# Quick Task 260701-mhk: Mejorar Sesión 06 MIMO — Summary

**One-liner:** Sesión 06 MIMO reestructurada para enseñabilidad: analogías concretas antes del álgebra en §1–§6, ejemplo 2×2 ancla (H=[[1,0.5],[0.5,1]], C≈4,78 bit/s/Hz) resuelto paso a paso, 6 concept-checks colapsables y 4 drills de lápiz y papel con solución.

## What Was Done

### Task 1 — Andamiaje de intuición, analogías y ejemplo 2×2 (commit 3f7d13c)

- §1: analogía del carril de autopista antes de la lista diversidad/multiplexación.
- §2: intuición "cada antena RX oye una mezcla ponderada; H es la tabla de ponderaciones" antes de la ec.(1), con lectura física de $h_{ji}$.
- §3: analogía mesa de mezclas / ejes naturales antes de la SVD; nueva subsección `#### 3.1 Un ejemplo concreto 2×2` con el ejemplo colapsable (σ={1,5, 0,5}, ganancias {2,25, 0,25}, v₁/v₂ en ±45°, verificación Frobenius 2,5, C≈4,78 vs SISO 3,46, referencia a Figura 3); frase de aterrizaje tras la ec.(5) conectando con Sesión 02; analogía del agua en recipiente irregular tras la ec.(6), enlazada al subcanal débil del §3.1.
- §4: analogía seguro vs velocidad + glosa intuitiva de r y d sin el límite, antes de las definiciones formales.
- §5: párrafo de apertura sobre por qué la precodificación recae en el TX; filosofías MRT (egoísta/simple) vs ZF (cooperativo, amplifica ruido) antes de la ec.(11).
- §6: analogía de la ley de los grandes números (dados → hardening; casi-ortogonalidad en dimensión alta → favorable propagation) antes de la ec.(14).
- Frases-puente al final de §1→§2, §2→§3, §3→§4, §4→§5, §5→§6 con el patrón "La pregunta natural es…" de la sesión 05.

### Task 2 — Ejercicios de asimilación (commit 04f041f)

- 6 admonitions `??? question "Comprueba tu comprensión"` (una al cierre de cada sección §1–§6) con preguntas conceptuales y respuestas en el mismo bloque.
- Nueva sección `## Ejercicios de Asimilación` entre Laboratorio y Resumen: drills A1 (SVD de matriz diagonal), A2 (capacidad, ≈6,97 bit/s/Hz), A3 (vector MRT con h=[1, j]), A4 (ortogonalidad / favorable propagation), cada uno con `??? example "Solución"` paso a paso; frase de cierre remitiendo a `lab.ipynb` para los ejercicios computacionales.

### Task 3 — Verificación de build (sin cambios, no requirió commit)

- `mkdocs build --strict` pasa limpio (verificado tras cada task y al final).
- HTML generado: 6 `<details class="question">`, 5 `<details class="example">`, 8 referencias a figures/mimo-*.
- Sin `\tag{N}` duplicados; las 16 ecuaciones conservan su numeración original.
- `figures/` intacto (git status limpio); notebook no tocado ni ejecutado.

## Deviations from Plan

None - plan executed exactly as written. (Adiciones menores dentro del espíritu del plan: subtítulo `#### 3.2` para estructura, frases-puente también en §1→§2 y §2→§3, decimales con coma española.)

## Verification

- [x] `mkdocs build --strict` limpio
- [x] Cada §1–§6 abre con intuición/analogía y cierra con concept-check
- [x] Ejemplo 2×2 en §3.1 (H=[[1, 0,5],[0,5, 1]], C≈4,78) en `??? example`
- [x] `## Ejercicios de Asimilación` con 4 drills + soluciones colapsables
- [x] 8 PNG originales intactos, sin regenerar
- [x] Ecuaciones (1)–(16) conservadas sin renumerar

## Commits

| Task | Commit | Description |
|------|--------|-------------|
| 1 | 3f7d13c | Intuition scaffolding, analogies, 2×2 worked example, bridges |
| 2 | 04f041f | Concept-checks + Ejercicios de Asimilación section |
| 3 | — | Verification only, no changes needed |

## Self-Check: PASSED

- Commits 3f7d13c and 04f041f present in git log
- docs/sessions/06-mimo-systems/index.md modified and committed (working tree clean under docs/)
- SUMMARY.md exists at expected path
