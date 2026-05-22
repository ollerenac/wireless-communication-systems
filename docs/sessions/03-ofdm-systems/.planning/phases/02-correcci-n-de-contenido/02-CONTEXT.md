# Phase 2: Corrección de Contenido - Context

**Gathered:** 2026-05-22
**Status:** Ready for planning

<domain>
## Phase Boundary

Aplicar todas las correcciones catalogadas en `01-AUDIT-FINDINGS.md` directamente sobre `index.md` y `figures/`. El resultado es un `index.md` sin fórmulas falsas, sin referencias rotas, con snippets alineados al notebook, y con las figuras generadas commiteadas al repositorio. **No se toca `lab.ipynb`** (es ground truth; solo cambia si hay bug real de código, y la auditoría confirmó que corre limpio).

</domain>

<decisions>
## Implementation Decisions

### Estrategia para figuras generadas
- **D-01:** Commitear las figuras generadas durante la auditoría directamente al repositorio: `figures/ofdm-ber-equalizers.png` y `figures/ofdm-per-subcarrier-ber.png` (BLOCKERs resueltos) más las 4 figuras de ejercicios (`channel-estimation-pilots.png`, `qpsk-decision-regions.png`, `ofdm-time-domain.png`, `cp-effect-constellation.png`). El repo queda auto-contenido sin depender de CI/CD para regenerar figuras.
- **D-02:** El nombre canónico es `ofdm-ber-equalizers.png` (es el que genera el notebook en su `savefig`). `index.md` ya usa ese nombre — se mantiene. El archivo `figures/ofdm-ber.png` pre-existente queda como está (no se elimina, no se renombra).

### Figuras huérfanas
- **D-03:** Agregar referencia pedagógica a `figures/mmse-vs-zf-constellation.png` en §4.8 (sección MMSE equalizer) — la figura muestra exactamente la comparación de constelaciones que §4.8 explica.
- **D-04:** Las 4 figuras de ejercicios (`channel-estimation-pilots.png`, `qpsk-decision-regions.png`, `ofdm-time-domain.png`, `cp-effect-constellation.png`) se commitean al repo pero **sin** agregar referencias en `index.md`. Su lugar natural es la sección de ejercicios, que está fuera del scope de rediseño.

### Corrección de fórmulas matemáticas
- **D-05:** El agente de corrección edita y commitea directamente sin checkpoint de verificación intermedia. Los errores están documentados con texto citado textualmente; la revisión final es el `git diff` antes de avanzar a Fase 3.
- **D-06:** Para BLOCKER-S.01 (§2 línea 240): corregir el factor del receptor de `1/N` → `1/√N` en la demostración de ortogonalidad. El resultado correcto de la derivación debe ser `X[k]` (no `X[k]/√N`). Convención: IFFT con `norm='ortho'` (factor `1/√N`) — consistente con NumPy y con el notebook.
- **D-07:** Para BLOCKER-S.02 (§6 línea 1029): (a) corregir el factor de `N_CP/(N+N_CP)` → `N/(N+N_CP)` y (b) actualizar la etiqueta de la llave de `"overhead CP"` → `"eficiencia temporal"` (o equivalente). El overhead CP es `N_CP/(N+N_CP)` — su complemento es la eficiencia temporal.
- **D-08:** Corregir también MINOR-01 (§2 línea 249, nota desplegable): el factor `1/N` en la nota es consistente con BLOCKER-S.01 y debe corregirse a `1/√N` para mantener consistencia interna del documento.

### Corrección de snippets de código
- **D-09:** Alinear snippets MMSE (líneas 806–808) y LS (líneas 886–895) mostrando la **firma de función completa** del notebook en `index.md`. El alumno debe ver `def mmse_equalizer(Y, h, N, SNR_dB):` y `def ls_channel_estimate(Y, pilot_idx, X_pilot, N):` tal como están en el lab.

### Claude's Discretion
- Ubicación exacta de la referencia a `mmse-vs-zf-constellation.png` dentro de §4.8 (antes/después del texto existente, en admonition o inline).
- Redacción del caption/alt-text de la figura nueva en §4.8.
- Orden de los commits dentro de la fase (por BLOCKER primero vs por sección).

</decisions>

<canonical_refs>
## Canonical References

**Downstream agents MUST read these before planning or implementing.**

### Informe de auditoría (lista de trabajo)
- `.planning/phases/01-auditor-a-y-diagn-stico/01-AUDIT-FINDINGS.md` — checklist completo con 5 BLOCKERs + 4 MINORs, texto actual citado textualmente para cada corrección

### Documentos fuente a modificar
- `index.md` — documento pedagógico principal; **único archivo narrativo que se modifica en esta fase**
- `figures/` — directorio de figuras; se agregan 6 archivos PNG nuevos

### Ground truth (solo lectura)
- `lab.ipynb` — notebook ejecutable; reference para alinear snippets y verificar nombres de funciones

### Requisitos y restricciones
- `.planning/REQUIREMENTS.md` — IDs CORR-01, CORR-02, CORR-03, LAB-01
- `.planning/PROJECT.md` — constraints: idioma español, MkDocs-Material, notebook como ground truth

</canonical_refs>

<code_context>
## Existing Code Insights

### Stack técnico de index.md
- Usa sintaxis MkDocs-Material: admonitions (`??? note`, `!!! warning`), LaTeX math con `$$`, bloques de figura `<figure markdown="span">`
- Las referencias a figuras usan la forma: `![alt text](figures/nombre.png){ width=... }`

### Patrones establecidos para figuras
- Cada referencia de figura en index.md usa `<figure markdown="span">` con `<figcaption>` para el caption
- Ejemplo de figura existente: `<figure markdown="span">![...](figures/...)...</figure>`

### Snippets Python en index.md
- Los snippets van en bloques de código con triple backtick y `python`
- Las funciones del notebook incluyen docstring de una línea entre comillas triples

### Convención numérica en §6
- El ejemplo numérico usa N=2048, N_CP=144 → overhead CP = 144/(2048+144) ≈ 0.066; eficiencia temporal = 1 − 0.066 = 0.934

</code_context>

<specifics>
## Specific Ideas

- El factor correcto para la demostración de ortogonalidad (§2) es `1/√N` tanto en el transmisor (IFFT norm='ortho') como en el receptor (FFT norm='ortho'). El producto de ambos factores cancela y resulta en `X[k]` exacto.
- Para §6, el factor en la fórmula simbólica debe ser `N/(N+N_CP)` y la llave debe etiquetarse `\text{eficiencia temporal}` — el overhead CP es el complemento `N_{CP}/(N+N_{CP})` y aparece en la fracción de pérdida, no en la de eficiencia.
- La figura `mmse-vs-zf-constellation.png` es una comparación visual de la dispersión de constelación QAM después de ecualización ZF vs MMSE — va bien como cierre visual de §4.8 antes de la siguiente sección.

</specifics>

<deferred>
## Deferred Ideas

Ninguna — la discusión se mantuvo dentro del scope de la fase.

</deferred>

---

*Phase: 2-Corrección de Contenido*
*Context gathered: 2026-05-22*
