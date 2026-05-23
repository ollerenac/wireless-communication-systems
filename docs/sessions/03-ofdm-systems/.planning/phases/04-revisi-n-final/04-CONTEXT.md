# Phase 4: Revisión Final - Context

**Gathered:** 2026-05-22
**Status:** Ready for planning

<domain>
## Phase Boundary

Verificación final de coherencia y publicabilidad — confirmar que `index.md` y `lab.ipynb` están listos para publicar y dictar en clase, sin correcciones de última hora. Las tres palancas: (1) verificación estructural automática de `index.md` con foco especial en §4, produciendo un reporte para barrido humano del profesor; (2) verificación completa de LAB-01 (ejecución limpia del notebook + revisión de orden y enunciados de ejercicios vs `index.md` + ajuste de texto en celdas markdown donde haya desalineación); (3) cierre de tracking: actualizar REQUIREMENTS.md y PROJECT.md para reflejar las 3 fases completadas. No hay cambios narrativos nuevos — solo verificación, ajustes menores de enunciados del notebook, y documentación de cierre.

</domain>

<decisions>
## Implementation Decisions

### LAB-01 — Verificación del notebook

- **D-01:** Scope completo de LAB-01: (a) correr el notebook end-to-end sin errores, (b) revisar el orden de los ejercicios (celdas markdown de ejercicio) contra el orden de las secciones de `index.md`, y (c) comparar los enunciados de cada ejercicio contra la terminología y el contenido del bloque correspondiente en `index.md`, ajustando donde haya desalineación.
- **D-02:** Límite de edición del notebook: **solo texto en celdas markdown existentes**. No se agregan ni eliminan celdas, no se reordenan celdas de código (dependencias de ejecución), no se toca el código Python. El notebook sigue siendo ground truth de código — solo los enunciados pedagógicos son editables.

### Coherencia estructural de index.md

- **D-03:** Checks estructurales automáticos que el agente debe verificar: (1) todas las referencias de figura en `index.md` existen como archivos en `figures/`; (2) no hay separadores dobles `---` consecutivos (WR-01 fue corregido en Fase 3, verificar que se mantuvo); (3) las 6 transiciones §4 están presentes y cada una sigue el patrón pregunta-respuesta (nombrar el problema resuelto + pregunta hacia el siguiente bloque); (4) los 5 parenthéticals de §7 Síntesis apuntan a secciones que existen en el documento.
- **D-04:** Foco especial en **§4 completo** — el agente lee cada una de las 6 transiciones y confirma que el patrón pregunta-respuesta es coherente y uniforme. El template canónico es la transición §4.5 (líneas ~780–784 de `index.md`, ya existente desde antes de Fase 3). El tono de las 6 transiciones nuevas debe ser consistente con ese template.
- **D-05:** Salida de la verificación: un **reporte de publicabilidad** que incluye (a) resultado de cada check (✅/⚠️/❌), (b) el texto verbatim de las 6 transiciones §4 para que el profesor las revise de corrido, (c) el texto verbatim de la transición §4.6→§4.7 destacado para revisión humana (ver D-06). El profesor hace el barrido humano final a partir de ese reporte.

### Item human_needed de Fase 3 (transición §4.6→§4.7)

- **D-06:** La transición §4.6→§4.7 fue marcada `human_needed` en la verificación de Fase 3 (D-03 de Fase 3) — la phrasing exacta requiere ojo humano para confirmar que fluye naturalmente. El agente extrae el texto actual de esa transición y lo incluye destacado en el reporte de publicabilidad. Si el profesor hace una corrección, se commitea en Fase 4. Si el texto actual es satisfactorio, no hay acción adicional.

### Exit criterion — "publicar"

- **D-07:** La Fase 4 está completa cuando: (a) todos los cambios están commiteados en git con mensajes descriptivos, y (b) `mkdocs build` corre localmente sin warnings ni errores. Push al remoto es responsabilidad del profesor — fuera del scope de los planes de Fase 4.

### Actualización de tracking

- **D-08:** REQUIREMENTS.md: mover NARR-01, NARR-02, NARR-03 de "Active" a "Validated" con referencia explícita a Fase 3. LAB-01: mover a "Validated" al completarse en Fase 4.
- **D-09:** PROJECT.md: evolucionar al cierre de Fase 4 — igual que las transiciones de fases anteriores (actualizar Requirements, Key Decisions, Last updated). Esto es el último paso de la fase.

### Claude's Discretion

- Número de planes y su granularidad (¿1 plan end-to-end o 2 planes separados: verificación + cierre?).
- Orden de ejecución de los checks de verificación estructural.
- Formato exacto del reporte de publicabilidad (markdown tabla, secciones, etc.) — lo que resulte más legible para el profesor.
- Redacción de los commits de cierre.

</decisions>

<canonical_refs>
## Canonical References

**Downstream agents MUST read these before planning or implementing.**

### Documentos a verificar y (posiblemente) modificar
- `index.md` — documento pedagógico principal; 1357 líneas; única fuente de narrativa
- `lab.ipynb` — notebook ejecutable; 17 celdas de código; ground truth de código y figuras

### Figuras en disco (todas presentes — verificar contra index.md)
- `figures/` — 17 archivos PNG; todas las referencias de `index.md` ya coinciden con disco (verificado pre-discusión)

### Tracking que se actualiza en esta fase
- `.planning/REQUIREMENTS.md` — NARR-01, NARR-02, NARR-03 pendientes de marcar como Validated; LAB-01 pendiente de completar
- `.planning/PROJECT.md` — evolucionar al cierre de Fase 4

### Fase 3 — resultados y pendientes
- `.planning/phases/03-mejora-de-narrativa/03-CONTEXT.md` — decisiones D-01 a D-16 (Fase 3); incluye template canónico de transición §4.5 y ubicación de cada transición nueva
- `.planning/phases/03-mejora-de-narrativa/03-VERIFICATION.md` — reporte de verificación 11/12; incluye el texto exacto y la nota `human_needed` de la transición §4.6→§4.7 (D-03)

### Requisitos y restricciones del proyecto
- `.planning/PROJECT.md` — constraints: idioma español, MkDocs-Material, notebook como ground truth, 8h
- `.planning/ROADMAP.md` — success criteria de Fase 4 (3 criterios)

### Fase 2 — patrones establecidos
- `.planning/phases/02-correcci-n-de-contenido/02-CONTEXT.md` — patrones MkDocs-Material, convenciones de figuras, snippets Python

</canonical_refs>

<code_context>
## Existing Code Insights

### Estado actual del repositorio
- `index.md`: 1357 líneas — §1 a §7 completos; 6 transiciones §4 nuevas; 5 parenthéticals §7; frase puente intro; bloque cadena completa §4; caption Figura 3 corregido
- `lab.ipynb`: 17 celdas de código, 0 errores en outputs (confirmado en Fase 3 wave 4 con nbconvert)
- `figures/`: 17 PNG; todas las 13 referencias de `index.md` apuntan a archivos existentes

### Transición template canónico (§4.5 — NO modificar)
```
La pregunta natural es: ¿existe un ecualizador que sea más inteligente en esas subportadoras? En lugar de invertir el canal ciegamente, ¿podría detectar que una subportadora está muy atenuada y moderar su respuesta para no amplificar el ruido? La respuesta es sí, y ese ecualizador es el MMSE.
```
*Fuente: §4.5, líneas ~780–784 de index.md*

### Checks de verificación disponibles (sin herramientas especiales)
- Referencias de figuras: `grep -n "figures/" index.md` + `ls figures/*.png`
- Separadores: `grep -c "^---$" index.md`
- Transiciones §4: buscar frases "La pregunta natural es" o "La respuesta es" en §4
- §7 parenthéticals: buscar `(§` en las líneas del bloque §7 Síntesis
- MkDocs build: `mkdocs build --strict` en el directorio del sitio

### Patrones MkDocs-Material establecidos
- Figuras: `<figure markdown="span">` con `<figcaption markdown="1">**Figura N.** ...`
- Admonitions: `??? note "Título"` (plegable) o `!!! warning "Título"` (expandido)
- Separadores de subsección: `---` (uno solo)
- Math: bloques `$$` para LaTeX display, `$...$` inline

</code_context>

<specifics>
## Specific Ideas

- La transición §4.6→§4.7 (D-06) debe articular que ZF y MMSE asumen H[k] conocido pero nunca explican cómo se obtiene. El texto actual (generado en Fase 3) puede estar semánticamente correcto pero con phrasing que no fluye naturalmente — el profesor es el árbitro.
- El reporte de publicabilidad (D-05) debe presentar las 6 transiciones de §4 en secuencia (4.1→4.2, 4.2→4.3, ..., 4.7→4.8) para que el profesor pueda leerlas como un flujo continuo y detectar saltos de tono sin necesidad de abrir el archivo completo.
- Para LAB-01, la guía de alineación es: cada ejercicio del notebook debe usar la misma terminología que el bloque correspondiente en `index.md` (ej. nombres de variables `X`, `x_cp`, `y_noisy`, `Y`, `X_hat`, `bits_hat` conforme a D-08 de Fase 3).
- `mkdocs build` se ejecuta desde el directorio que contiene `mkdocs.yml` — verificar el path correcto relativo al worktree del proyecto.

</specifics>

<deferred>
## Deferred Ideas

- Agregar ejercicios interactivos o widgets Jupyter para la cadena completa OFDM — fuera del scope de 8 horas; pertenece a una revisión editorial mayor (v2).
- Push al remoto y verificación de CI/CD — responsabilidad del profesor post-Fase 4.
- Revisión de los ejercicios numerados (§Ejercicios finales) de `index.md` — correctos como están; fuera del scope de rediseño (PROJECT.md Out of Scope).

</deferred>

---

*Phase: 4-Revisión Final*
*Context gathered: 2026-05-22*
