# Phase 4: Revisión Final - Discussion Log

> **Audit trail only.** Do not use as input to planning, research, or execution agents.
> Decisions are captured in CONTEXT.md — this log preserves the alternatives considered.

**Date:** 2026-05-22
**Phase:** 04-revisión-final
**Areas discussed:** LAB-01 scope, Lectura de corrido §1–§7, Item human_needed de Fase 3, Qué significa 'publicar', Límite de edición del notebook, Actualización de REQUIREMENTS.md

---

## LAB-01 — ¿Qué tanto?

| Option | Description | Selected |
|--------|-------------|----------|
| Solo correr end-to-end | Verificar que el notebook ejecuta sin errores y que los outputs están generados. Ejercicios declarados 'correctos como están'. | |
| Verificación completa | Correr + revisar orden de ejercicios vs index.md + ajustar enunciados donde haya desalineación. | ✓ |
| Deferir LAB-01 a v2 | Registrar en REQUIREMENTS.md fuera del scope de 8 horas. Fase 4 solo verifica ejecución. | |

**User's choice:** Verificación completa
**Notes:** El usuario quiere cerrar LAB-01 formalmente en esta fase.

---

## Acción ante desalineación en ejercicios

| Option | Description | Selected |
|--------|-------------|----------|
| Ajustar el notebook | Editar texto de enunciados para alinear terminología con index.md. Cambios de texto, no de lógica. | ✓ |
| Registrar y dejar al profesor | El agente lista desalineaciones pero no edita el notebook. | |

**User's choice:** Ajustar el notebook (Recomendado)
**Notes:** —

---

## Lectura de corrido §1–§7

| Option | Description | Selected |
|--------|-------------|----------|
| Checks estructurales + reporte al profesor | Verificación automática: figura refs, separadores, transiciones §4, refs §7. Reporte para barrido humano. | ✓ |
| Solo checks automáticos | El agente verifica y declara publicable si todo pasa. Sin barrido humano. | |
| Solo reporte para el profesor | Checklist para barrido humano completo. Sin checks automáticos. | |

**User's choice:** Checks estructurales + reporte al profesor (Recomendado)
**Notes:** —

---

## Zona de mayor inquietud en index.md

| Option | Description | Selected |
|--------|-------------|----------|
| Sí — la Sección 4 completa | Las transiciones nuevas son muchas; riesgo de tono no uniforme. | ✓ |
| Sí — el cierre §4→§5→§6 | Zona donde confluyen varias correcciones de fases anteriores. | |
| No — los checks estándar son suficientes | El agente verifica lo automatizable; el profesor hace el resto. | |

**User's choice:** Sí — la Sección 4 completa
**Notes:** El usuario identifica §4 como la zona de mayor riesgo post-edición.

---

## Nivel de verificación de §4

| Option | Description | Selected |
|--------|-------------|----------|
| Verificar que las 6 transiciones están presentes y siguen el patrón pregunta-respuesta | El agente lee cada transición y confirma patrón. | ✓ |
| Solo verificar que las 6 transiciones existen (grep) | El agente confirma existencia. El profesor evalúa tono. | |
| Leer y reportar el texto de cada transición | El agente extrae y muestra el texto para que el profesor compare. | |

**User's choice:** Verificar que las 6 transiciones están presentes y siguen el patrón pregunta-respuesta
**Notes:** —

---

## Item human_needed de Fase 3 (D-03, transición §4.6→§4.7)

| Option | Description | Selected |
|--------|-------------|----------|
| Incluir en Fase 4: revisar y afinar si es necesario | El agente extrae el texto actual e incluye en el reporte para revisión del profesor. Si hay corrección → commitear. | ✓ |
| Dejar al profesor sin acción adicional | Marcar 'a revisar en clase'. No incluir en scope de planes. | |

**User's choice:** Incluir en Fase 4: revisar y afinar si es necesario (Recomendado)
**Notes:** —

---

## Qué significa 'publicar'

| Option | Description | Selected |
|--------|-------------|----------|
| Git commits limpios + MkDocs build local sin errores | `mkdocs build` sin warnings. Push al remoto es del profesor. | ✓ |
| Solo git commits limpios | Build y deploy son externos al workflow. | |
| Push al remoto verificado | Requiere acceso al remoto y pipeline CI/CD. | |

**User's choice:** Git commits limpios + MkDocs build local sin errores (Recomendado)
**Notes:** —

---

## Límite de edición del notebook (LAB-01)

| Option | Description | Selected |
|--------|-------------|----------|
| Solo editar texto en celdas markdown existentes | Sin agregar/eliminar/reordenar celdas. Sin tocar código Python. | ✓ |
| Editar texto + reordenar celdas si el orden no coincide | Riesgoso por dependencias de ejecución entre celdas. | |
| Reportar desalineación sin editar | El agente lista; el profesor decide. | |

**User's choice:** Solo editar texto en celdas markdown existentes (Recomendado)
**Notes:** —

---

## Actualización de REQUIREMENTS.md y PROJECT.md

| Option | Description | Selected |
|--------|-------------|----------|
| Sí — actualizar ambos documentos | NARR-01/02/03 → Validated con ref a Fase 3. PROJECT.md evoluciona al cierre. | ✓ |
| Solo actualizar REQUIREMENTS.md | PROJECT.md se actualiza en transición de milestone. | |
| No — dejar el tracking como está | Se actualiza en /gsd:complete-milestone. | |

**User's choice:** Sí — actualizar ambos documentos (Recomendado)
**Notes:** —

---

## Claude's Discretion

- Número de planes y granularidad para Fase 4 (¿1 end-to-end o 2 separados: verificación + cierre?)
- Orden de ejecución de los checks estructurales
- Formato exacto del reporte de publicabilidad
- Redacción de commits de cierre

## Deferred Ideas

- Ejercicios interactivos/widgets Jupyter para la cadena OFDM completa — v2
- Push al remoto y verificación de CI/CD — responsabilidad del profesor post-Fase 4
- Revisión de §Ejercicios finales de index.md — Out of Scope (PROJECT.md)
