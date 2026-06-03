# Phase 1: Index Polish - Context

**Gathered:** 2026-05-26
**Status:** Ready for planning

<domain>
## Phase Boundary

Pulido narrativo y estructural puro de `index.md` — sin modificar el notebook, sin generar figuras nuevas. El objetivo es llevar el texto, los hooks de transición, la sección de laboratorio y las referencias de figura al nivel de calidad de la sesión 03 de referencia.

Entregable: un `index.md` con hooks "La pregunta natural es..." en cada cierre de sub-sección, referencias `<figure>` correctas, lab section que describe los 6 ejercicios finales, soluciones en admonitions `??? example`, y verificación factual de todas las afirmaciones cruzadas con sesiones 01-03.

</domain>

<decisions>
## Implementation Decisions

### Hooks narrativos (IDX-01)

- **D-01:** Añadir hooks "La pregunta natural es..." al CIERRE de TODAS las sub-secciones del documento — §1, §2, §3.1, §3.2, §3.3, §4.1, §4.2, §4.3, §5. Cobertura total, no solo §3.2 y §4.2 como dice el requisito mínimo.
- **D-02:** Para secciones teóricas sin código Python, el hook ancla al ÚLTIMO OBJETO MATEMÁTICO introducido en esa sección (ej. la LLR $\lambda_v$, el parámetro de Bhattacharyya $Z(W)$, la matriz $G_N$) — mismo patrón que sesión 03 ancla al nombre de la variable Python. Claude decide la formulación exacta de cada hook para máxima coherencia narrativa.

### Lab section (IDX-02)

- **D-03:** Escribir la sección "Laboratorio Python" para el ESTADO TARGET — 6 ejercicios completos descritos como si el notebook estuviera terminado. El notebook "alcanza" esta descripción en las Fases 3-5. Los 6 ejercicios son:
  - Ej 1: Capacidad de Shannon y puntos de operación (~15 min)
  - Ej 2: Código LDPC — verificación de paridad con matriz H (~15 min)
  - Ej 3: LDPC BP realista sobre código n≈400 bits, curva BER Monte Carlo (~30 min)
  - Ej 4: Polar N=64 — encoder + decodificador SC + SCL-L=8 (~35 min)
  - Ej 5: Curvas waterfall comparativas LDPC vs Polar vs BPSK sin código (~15 min)
  - Ej 6: Integrador OFDM+LDPC — BER coded vs uncoded, canal frequency-selective (~30 min)

### Conversión de figuras (FIG-01)

- **D-04:** Convertir las 2 referencias planas `![alt](path)` a bloques `<figure markdown="span">` con `<figcaption markdown="1">` de al menos 2 líneas. Cada `<figure>` incluye un comentario HTML inline indicando la celda origen del notebook: `<!-- generada por celda N de lab.ipynb -->`.
- **D-05:** El diagrama mermaid inline de §3.1 (grafo de Tanner) se MANTIENE tal como está. Se añade además una referencia `<figure>` placeholder para `figures/tanner-graph.png` debajo del mermaid, con caption descriptivo. Cuando la Fase 3 genere el PNG, el mermaid se elimina.

### Admonitions `??? example`

- **D-06:** Convertir a `??? example "Solución"` todos los ejercicios que ya tienen solución completa escrita (Ej 1, 2, 5 en la sección actual). Los ejercicios cuya solución aún no existe en el notebook (Ej 3, 4, 6 del estado target) no tienen admonition de solución — solo descripción del ejercicio.

### Verificación referencias cruzadas (IDX-03)

- **D-07:** Verificación FACTUAL completa: además de comprobar que las secciones referenciadas existen, verificar que las afirmaciones numéricas específicas del intro ("86% de la capacidad de Shannon", "BER pre-FEC de $10^{-1.5}$") aparecen realmente en las sesiones 02 y 03 respectivamente. Si hay discrepancia, corregir la afirmación en el intro.

### Claude's Discretion

- La formulación exacta de cada hook "La pregunta natural es..." — Claude elige el objeto matemático ancla y el puente narrativo hacia la siguiente sección, optimizando para consistencia con el estilo de sesión 03.
- El caption detallado de cada `<figure>` (mínimo 2 líneas) — Claude lo redacta con el mismo nivel descriptivo que las figuras 1-13 de sesión 03.

</decisions>

<canonical_refs>
## Canonical References

**Downstream agents MUST read these before planning or implementing.**

### Fuente de verdad del material

- `index.md` — archivo a modificar en esta fase (503 líneas, borrador funcional)
- `lab.ipynb` — notebook de referencia para los 6 ejercicios (15 celdas actuales)

### Estándar de calidad

- `../03-ofdm-systems/index.md` — referencia OBLIGATORIA de estilo. 11 hooks "La pregunta natural es...", 13 figuras con `<figure markdown="span">`, admonitions `??? example` con soluciones, narrativa de código block-a-block.

### Planificación del proyecto

- `.planning/ROADMAP.md` — Phase 1 goal, success criteria (3 criterios cuantitativos), requirements mapping
- `.planning/REQUIREMENTS.md` — especificación detallada de IDX-01..04, FIG-01, LAB-01..05

### Sintaxis MkDocs-Material

- No hay spec externa — constraints capturados en CLAUDE.md: `<figure markdown="span">`, `<figcaption markdown="1">`, admonitions `??? note/example`

</canonical_refs>

<code_context>
## Existing Code Insights

### Reusable Assets

- `../03-ofdm-systems/index.md` §Ejercicios: patrón de admonitions `??? example` con soluciones detalladas — copiar estructura exacta
- `../03-ofdm-systems/index.md` hooks §3-§5: 11 instancias del patrón "La pregunta natural es: `variable` ya es X, pero..." — usar como plantilla directa

### Established Patterns

- Figuras en sesión 03: `<figure markdown="span">` + imagen + `<figcaption markdown="1">**Figura N.** ...` + descripción de 2-4 líneas + cierre `</figcaption></figure>`
- Hooks de sesión 03: siempre comienzan por "La pregunta natural es: `objeto_exacto` ya es [descripción breve], [pero / sin embargo / ahora]. [Pregunta retórica]. La respuesta es [concepto de la siguiente sección]."

### Integration Points

- Las referencias a sesiones 02 y 03 en el párrafo de Introducción deben verificarse factualmente contra `../02-*/index.md` y `../03-ofdm-systems/index.md`
- El `<figure>` placeholder para `tanner-graph.png` debe apuntar a `figures/tanner-graph.png` — el mismo path que Fase 3 usará al generar el archivo

</code_context>

<specifics>
## Specific Ideas

- La sesión 03 tiene el patrón exacto para hooks; el agente debe leer al menos 3 instancias de `../03-ofdm-systems/index.md` antes de escribir cualquier hook para calibrar el tono y la densidad.
- Los ejercicios del estado target (Ej 3, 4, 6) deben describirse con suficiente precisión para que un estudiante sepa qué implementar: mencionar el tamaño del código (n≈400), el N del Polar (64), y que el integrador reutiliza las funciones OFDM de la sesión 03.
- El `<figure>` placeholder para `tanner-graph.png` debe incluir el mismo caption de 2+ líneas descriptivo que tendrá la figura real en Fase 3.

</specifics>

<deferred>
## Deferred Ideas

None — discussion stayed within phase scope.

</deferred>

---

*Phase: 1-Index Polish*
*Context gathered: 2026-05-26*
