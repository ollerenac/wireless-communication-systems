# Sesión 04 — Codificación de Canal: LDPC y Códigos Polar

## What This Is

Clase 04 de un curso de posgrado en sistemas de comunicaciones inalámbricas. Cubre la codificación de canal moderna: del límite de Shannon a los dos códigos que lo alcanzan (LDPC y Polar), tal como se usan en 5G NR. El material existe como `index.md` (narrativa pedagógica publicada en el site) y `lab.ipynb` (notebook ejecutable, fuente de verdad de código y figuras).

**Estado actual (borrador funcional):** El `index.md` tiene estructura completa y contenido teórico correcto (503 líneas). El `lab.ipynb` tiene 15 celdas con ejercicios pedagógicos básicos. Ambos existen pero no alcanzan la calidad de la sesión 03 de referencia.

**Estado objetivo (publicable):** Paridad de calidad con la sesión 03 — figuras publicables generadas por código con `<figure>` y leyendas detalladas, simulación LDPC BP realista con curvas BER Monte Carlo, decodificador Polar completo (N≥64), ejercicio integrador OFDM+LDPC end-to-end, y alineación perfecta entre `index.md` y `lab.ipynb`.

## Core Value

El `index.md` debe explicar rigurosa y narrativamente lo que el `lab.ipynb` demuestra — cada sección teórica tiene una figura publicable que la ilustra, el notebook implementa esa misma teoría a escala real, y el ejercicio integrador final conecta la cadena OFDM de la sesión 03 con el codec FEC de esta sesión.

## Context

**Sesión de referencia:** `../03-ofdm-systems/` — estándar de calidad a alcanzar. Tiene 13 figuras ricas con `<figure>` y leyendas detalladas, código Python que implementa la cadena completa block-a-block, y ejercicios con soluciones embebidas (`??? example`).

**Continuidad curricular:**
- Sesión 03 termina mencionando que "LDPC se agrega como una capa superior a la cadena OFDM" y que "la transición de decisión hard a soft se tratará en la Sesión 04"
- Sesión 04 cierra esas referencias — el ejercicio integrador final da concreción a esa promesa
- Sesiones 05-09 asumen que el estudiante entiende ganancia de codificación, umbrales waterfall, y la diferencia LDPC/Polar

**Audiencia:** Posgrado en ingeniería de telecomunicaciones. Python competente, matemáticas universitarias. Español como idioma de la sesión, terminología técnica en inglés.

## Requirements

### Active

- [ ] **FIG-01**: Convertir todas las referencias de figura planas (`![alt](path)`) a `<figure>` con leyendas detalladas alineadas con el texto teórico
- [ ] **FIG-02**: Figura de capacidad de Shannon con puntos de operación por modulación (actualmente sin leyenda detallada) — polished version
- [ ] **FIG-03**: Figura de curvas waterfall BER para LDPC y Polar vs BPSK sin código — polished version
- [ ] **FIG-04**: Figura del grafo de Tanner (visualización del bipartite graph con nodos de variable y verificación)
- [ ] **FIG-05**: Figura de propagación de mensajes BP — iteraciones mostrando convergencia de LLRs
- [ ] **FIG-06**: Figura de la mariposa Arıkan (butterfly transform, $G_2$ y composición)
- [ ] **FIG-07**: Figura de polarización del canal — evolución de $Z(W)$ para N canales sintéticos mostrando la separación
- [ ] **FIG-08**: Figura de BER Monte Carlo LDPC (BP sobre código real n~200-500 bits) — curvas a distintas tasas
- [ ] **FIG-09**: Figura OFDM+LDPC end-to-end — BER antes y después del codec FEC sobre canal frequency-selective
- [ ] **IDX-01**: Añadir ganchos narrativos "La pregunta natural es..." al final de §3 y §4 (alinear con estilo sesión 03)
- [ ] **IDX-02**: Alinear la sección "Laboratorio Python" del index.md con los ejercicios reales del notebook
- [ ] **IDX-03**: Verificar todas las referencias cruzadas con sesiones 01, 02, 03 (ninguna apunta a sección inexistente)
- [ ] **LAB-01**: Ejercicio 3 reescrito: LDPC BP sobre código real (n=200-500 bits, k/n=1/2), 3-5 iteraciones visibles, curva BER Monte Carlo
- [ ] **LAB-02**: Ejercicio 4 reescrito: Polar N=64 completo — encoder + decodificador SC con árbol factor, comparación SC vs SCL-L=8
- [ ] **LAB-03**: Ejercicio 6 nuevo: integrador OFDM (reutilizar funciones de sesión 03) + LDPC codec — BER coded vs uncoded sobre canal frequency-selective
- [ ] **LAB-04**: Notebook ejecutable sin errores (células en orden, imports correctos, salidas reproducibles)
- [ ] **LAB-05**: Código del notebook es ground truth para las figuras del index.md — cada figura tiene una celda origen

### Out of Scope

- Implementación de HARQ (se cubre en sesión 05)
- Decodificador turbo (históricamente relevante pero reemplazado por LDPC en 5G NR)
- SCL con lista grande (L>8) — complejidad no justificada pedagógicamente
- Análisis density evolution / EXIT charts (nivel de investigación, no posgrado)
- Refactorizar estructura de secciones del index.md — la arquitectura §1-§5 es correcta

## Key Decisions

| Decisión | Rationale | Outcome |
|----------|-----------|---------|
| BP realista sobre n~200-500 bits | Balancear ejecutabilidad (~30 seg) con realismo de la curva waterfall | — Pendiente |
| Polar N=64 vs N=128 | N=64 es suficiente para mostrar polarización y es ejecutable rápido | — Pendiente |
| Integrador usa funciones de sesión 03 | Consistencia con el código del curso, no duplicar implementaciones | — Pendiente |
| SCL con L=8 | Es el estándar de 5G NR y converge visiblemente mejor que SC básico | — Pendiente |

## Evolution

Este documento evoluciona en las transiciones de fase y en los hitos del milestone.

**Después de cada transición de fase** (via `/gsd-transition`):
1. ¿Requisitos invalidados? → Mover a Out of Scope con razón
2. ¿Requisitos validados? → Mover a Validated con referencia de fase
3. ¿Requisitos nuevos emergieron? → Añadir a Active
4. ¿Decisiones a registrar? → Añadir a Key Decisions

---
*Last updated: 2026-05-26 after initialization*
