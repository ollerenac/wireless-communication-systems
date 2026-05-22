# Phase 1: Auditoría y Diagnóstico - Context

**Gathered:** 2026-05-22
**Status:** Ready for planning

<domain>
## Phase Boundary

Construir un inventario completo de todos los problemas en `index.md` y `lab.ipynb` — **sin cambiar una sola línea de ningún documento**. El output es un archivo de diagnóstico (`01-AUDIT-FINDINGS.md`) que la Fase 2 usará como lista de trabajo. Esta fase termina cuando existe un registro exhaustivo de errores; la corrección empieza en Fase 2.

</domain>

<decisions>
## Implementation Decisions

### Estructura del informe de diagnóstico
- **D-01:** Los hallazgos se escriben en un archivo separado `01-AUDIT-FINDINGS.md` en el directorio de la fase (`.planning/phases/01-auditor-a-y-diagn-stico/01-AUDIT-FINDINGS.md`). No se anotan en index.md ni se mezclan con CONTEXT.md.
- **D-02:** Severidad de dos niveles: **Blocker** (impide dictar la clase: frase falsa, figura rota visible, fórmula que lleva a resultado erróneo) y **Minor** (inconsistencia que no confunde al estudiante: variable renombrada, texto levemente desactualizado).
- **D-03:** Cada entrada del informe incluye: descripción del error + sección y número de línea de `index.md` (o número de celda si es del notebook) + texto actual citado textualmente. No se incluye propuesta de corrección — eso es trabajo de Fase 2.
- **D-04:** El informe se organiza en **4 secciones por categoría de error**, espejando los 4 criterios de éxito de la fase:
  1. Fórmulas y enunciados incorrectos
  2. Referencias de figuras (rotas / huérfanas)
  3. Snippets de código desalineados
  4. Estado del notebook (lab.ipynb)

### Granularidad de desalineación de código
- **D-05:** Una discrepancia de código cuenta solo si es **funcional**: API distinta (nombre de función incorrecto, argumentos en orden distinto, módulo equivocado), lógica que produce resultado diferente al notebook, o comportamiento que un estudiante no podría reproducir copiando el snippet. Diferencias de estilo, nombres de variables y formato **no** se reportan.
- **D-06:** Snippets ilustrativos o de pseudocódigo en `index.md` se reportan **solo si existe una sección ejecutable equivalente en `lab.ipynb`** para comparar. Si el snippet es puramente didáctico sin equivalente ejecutable, se omite.
- **D-07:** Cada discrepancia de código se registra con: número de línea en `index.md` + número de celda en `lab.ipynb` + descripción de la diferencia funcional.

### Profundidad de auditoría por sección
- **D-08:** **§4 (cadena OFDM completa, bloques 4.1–4.8) y §6 (eficiencia espectral y CP overhead)** son las secciones prioritarias. §6 tiene un error de notación conocido. Ambas reciben auditoría más profunda.
- **D-09:** **§Ejercicios finales se incluye en la auditoría normal** — a pesar de estar fuera del scope de rediseño, debe verificarse que no tiene figuras rotas ni snippets funcionales desalineados.
- **D-10:** **§1–§2 (Introducción) y §7 (Síntesis / 5 dimensiones)** se auditan para errores de contenido (fórmulas incorrectas, figuras rotas), pero **no** se evalúa la calidad narrativa ni el hilo conductor — eso es trabajo de Fase 3.

### Claude's Discretion
- Entorno y método de ejecución del notebook (celda a celda vs. Run All, kernel a usar) — el agente de planificación decide según el entorno disponible.
- Orden interno de las tareas de auditoría dentro del plan.

</decisions>

<canonical_refs>
## Canonical References

**Downstream agents MUST read these before planning or implementing.**

### Documentos principales a auditar
- `index.md` — narrativa pedagógica completa; el documento que se audita
- `lab.ipynb` — notebook de laboratorio ejecutable; ground truth de código y figuras

### Figuras
- `figures/` — directorio de figuras del proyecto; contiene 11 archivos PNG

**Estado conocido pre-auditoría (del scout de la codebase):**
- `figures/ofdm-ber-equalizers.png` — **NO existe** en disco; referenciada en `index.md` líneas 814 y 953
- `figures/ofdm-per-subcarrier-ber.png` — **NO existe** en disco; referenciada en `index.md` línea 961
- `figures/mmse-vs-zf-constellation.png` — existe en disco pero **no está referenciada** en `index.md`
- `figures/ofdm-ber.png` — existe en disco; puede ser la versión renombrada de `ofdm-ber-equalizers.png`

### Requisitos y criterios de éxito
- `.planning/REQUIREMENTS.md` — IDs de requisitos (CORR-01, CORR-02, CORR-03, LAB-01)
- `.planning/ROADMAP.md` — criterios de éxito detallados de la Fase 1

### Constraints del proyecto
- `.planning/PROJECT.md` — constraints (idioma, MkDocs-Material, notebook como ground truth, sin reorganización estructural)

</canonical_refs>

<code_context>
## Existing Assets

### Stack técnico del proyecto
- `index.md` usa sintaxis MkDocs-Material: admonitions (`??? note`), LaTeX math con `$$`, bloques de figura con `<figure markdown="span">`
- `lab.ipynb` usa Python 3 con NumPy, Matplotlib; las celdas de código son la referencia ejecutable

### Figuras confirmadas en disco (11 archivos)
- channel-estimation-ls.png, cp-illustration.png, isi-problem.png, lte-resource-grid-pilots.png
- mmse-vs-zf-constellation.png *(huérfana — no referenciada)*
- ofdm-ber.png, ofdm-ifft-transmitter.png, ofdm-subcarriers.png
- zf-equalizer-effect.png, zf-equalizer-qam-comparison.png, zf-noise-amplification.png

### Referencias de figuras en index.md (11 referencias totales)
Verificadas contra disco: 9 coinciden. 2 no existen: `ofdm-ber-equalizers.png` (×2 refs) y `ofdm-per-subcarrier-ber.png` (×1 ref).

</code_context>

<specifics>
## Specific Ideas

- El archivo `01-AUDIT-FINDINGS.md` debe ser usable directamente como checklist para Fase 2: cada item debe ser independientemente correctable sin necesidad de releer `index.md`.
- El error conocido en §6 (eficiencia espectral, posible error en notación CP overhead) debe localizarse y describirse con precisión.

</specifics>

<deferred>
## Deferred Ideas

Ninguna — la discusión se mantuvo dentro del scope de la fase.

</deferred>

---

*Phase: 01-auditor-a-y-diagn-stico*
*Context gathered: 2026-05-22*
