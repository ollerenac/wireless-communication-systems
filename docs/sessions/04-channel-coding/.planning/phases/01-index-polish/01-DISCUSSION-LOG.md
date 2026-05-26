# Phase 1: Index Polish - Discussion Log

> **Audit trail only.** Do not use as input to planning, research, or execution agents.
> Decisions are captured in CONTEXT.md — this log preserves the alternatives considered.

**Date:** 2026-05-26
**Phase:** 1-Index Polish
**Areas discussed:** Alcance de hooks §3.2/§4.2, Lab section, Grafo Tanner mermaid, Verificación IDX-03, Admonitions ??? example, Tabla traza figura↔celda, §1 Shannon con hook

---

## Alcance de hooks §3.2/§4.2

| Opción | Descripción | Seleccionado |
|--------|-------------|--------------|
| Solo §3.2 y §4.2 | Los 2 hooks mínimos prescritos en IDX-01 | |
| También transiciones de sección mayor | 4 hooks: §3.2, §4.2, cierre §3, cierre §4 | |
| En cada sub-sección como sesión 03 | Hooks en todos los cierres: §1, §2, §3.1, §3.2, §3.3, §4.1, §4.2, §4.3, §5 | ✓ |

**User's choice:** En cada sub-sección como sesión 03
**Notes:** Paridad total con sesión 03 desde el principio.

---

## Estilo de hooks en secciones teóricas puras

| Opción | Descripción | Seleccionado |
|--------|-------------|--------------|
| Concepto matemático en backticks | Anclar al objeto matemático como sesión 03 ancla a variable Python | |
| Pregunta abierta narrativa | Sin anclar a objeto específico | |
| Tú decides (consistencia con sesión 03) | Claude elige la formulación que mejor replique el estilo | ✓ |

**User's choice:** Tú decides (consistencia con sesión 03)
**Notes:** Claude tiene libertad para formular cada hook, priorizando coherencia con el patrón de sesión 03.

---

## Lab section: ¿ahora o después?

| Opción | Descripción | Seleccionado |
|--------|-------------|--------------|
| Estado TARGET (6 ejercicios completos) | Escribir descripción final ya, notebook la alcanza en Fases 3-5 | ✓ |
| Estado actual + placeholder Ej 3/4/6 | Precisión presente sobre aspiración futura | |
| Fase 1 solo alinea títulos | Detalles en Fase 6 | |

**User's choice:** Estado TARGET
**Notes:** index.md describe el destino; el notebook lo alcanza. Los 6 ejercicios con tiempos estimados.

---

## Grafo Tanner mermaid

| Opción | Descripción | Seleccionado |
|--------|-------------|--------------|
| Mantenerlo + añadir \<figure\> debajo | Mermaid coexiste con placeholder hasta Fase 3 | ✓ |
| Reemplazarlo por \<figure\> placeholder | index.md queda sin visualización hasta Fase 3 | |
| Mantenerlo sin tocar hasta Fase 3 | FIG-01 no aplica al mermaid | |

**User's choice:** Mantenerlo + añadir `<figure>` debajo
**Notes:** Fase 3 elimina el mermaid cuando genere `tanner-graph.png`.

---

## Profundidad verificación IDX-03

| Opción | Descripción | Seleccionado |
|--------|-------------|--------------|
| Sintactic: que archivos/secciones existan | Solo check de links rotos | |
| Factual: también verificar números y afirmaciones | Verificar "86%", "$10^{-1.5}$" en sesiones referenciadas | ✓ |
| Solo afirmaciones numeradas del intro | Verificación factual parcial | |

**User's choice:** Factual completa
**Notes:** Si hay discrepancia entre lo que dice el intro y lo que está en las sesiones 02/03, corregir el intro.

---

## Admonitions ??? example

| Opción | Descripción | Seleccionado |
|--------|-------------|--------------|
| Sí, convertir en Fase 1 | Paridad estructural con sesión 03 desde el principio | ✓ |
| No, queda para Fase 6 | Conversión como parte del pulido final | |
| Solo los que ya tienen solución escrita | Conversión parcial | |

**User's choice:** Sí, convertir en Fase 1
**Notes:** Ejercicios con solución completa → `??? example "Solución"`. Ej 3, 4, 6 no tienen solución todavía — solo descripción del ejercicio target.

---

## Tabla traza figura↔celda (IDX-04)

| Opción | Descripción | Seleccionado |
|--------|-------------|--------------|
| Tabla en index.md con TBD para figuras futuras | Artefacto de trazabilidad global visible | |
| Solo verificar en Fase 6, sin tabla explícita | Trazabilidad implícita, verificada al final | |
| Comentarios HTML inline junto a cada \<figure\> | Trazabilidad distribuida por figura | ✓ |

**User's choice:** Comentarios HTML inline
**Notes:** `<!-- generada por celda N de lab.ipynb -->` en cada bloque `<figure>`. Sin tabla global.

---

## §1 Shannon también con hook

| Opción | Descripción | Seleccionado |
|--------|-------------|--------------|
| Sí, todas las secciones incluidas §1 y §2 | Cobertura total del documento | ✓ |
| Solo desde §3 (donde comienzan los algoritmos) | Hooks solo donde hay transición algoritmo→implementación | |

**User's choice:** Sí, todas las secciones
**Notes:** Cobertura total — hook al cierre de §1 conecta con §2, hook al cierre de §2 conecta con §3 (LDPC).

---

## Claude's Discretion

- Formulación exacta de cada hook "La pregunta natural es..." — Claude elige el objeto matemático ancla y la formulación narrativa, calibrando contra los 11 hooks de sesión 03.
- Caption detallado de cada `<figure>` — Claude redacta al nivel descriptivo de las figuras 1-13 de sesión 03.

## Deferred Ideas

None — discussion stayed within phase scope.
