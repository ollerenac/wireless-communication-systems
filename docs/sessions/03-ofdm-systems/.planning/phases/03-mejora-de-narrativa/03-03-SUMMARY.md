---
phase: 03-mejora-de-narrativa
plan: 03
subsystem: index.md
tags:
  - narrative
  - synthesis
  - figure-caption
  - markdown

dependency_graph:
  requires:
    - "03-01 (transiciones §4 — wave 1)"
    - "03-02 (introducción NARR-02 — wave 2)"
  provides:
    - "5 referencias cruzadas parenthetical en §7 Síntesis (NARR-03, D-13, D-14)"
    - "Caption + alt-text de Figura 3 corregidos para describir 3 paneles reales (D-15)"
  affects:
    - "index.md §7 Síntesis (líneas 1104–1112)"
    - "index.md Figura 3 caption (línea 948–949)"

tech_stack:
  added: []
  patterns:
    - "Parenthetical `(§X)` al final de la oración de Implicación de diseño, antes del punto final"
    - "Caption multi-panel con etiquetas **Izquierda:** / **Centro:** / **Derecha:** en orden"
    - "figcaption markdown=\"1\" preservado para renderizado de LaTeX inline"

key_files:
  created: []
  modified:
    - path: "docs/sessions/03-ofdm-systems/index.md"
      description: "5 parentheticals en §7 Síntesis + caption Figura 3 corregido (3 paneles)"

decisions:
  - "Formulación verbatim de D-14 para los 5 parentheticals (sin variaciones editoriales)"
  - "Caption Figura 3 sigue exactamente el orden izquierda→centro→derecha, con LaTeX para α[k]"
  - "Caption verbatim tomado de RESEARCH.md Code Examples con ajuste mínimo (azules/cian para ZF)"

metrics:
  duration: "10 minutes"
  completed_date: "2026-05-22"
  tasks_completed: 2
  tasks_total: 2
  files_modified: 1
---

# Phase 03 Plan 03: Referencias Cruzadas §7 + Caption Figura 3 — Summary

**One-liner:** 5 parentheticals D-14 insertados al final de cada Implicación de diseño en §7 Síntesis, y caption de Figura 3 reescrito para describir los 3 paneles reales (α[k], ZF, MMSE) en lugar de los 2 paneles incorrectos del estado anterior

## What Was Built

### Task 1: Referencias cruzadas parenthetical en las 5 dimensiones de §7 Síntesis

Insertados al final de la oración "Implicación de diseño" de cada dimensión, inmediatamente antes del punto final. Mapa D-14 implementado con exactitud:

| Dimensión | Línea | Texto final (resultado) |
|-----------|-------|------------------------|
| D1 — FSF → N canales flat | 1104 | `...pero no tan grande que el Doppler cause ICI (§2 y §4).` |
| D2 — CP como precio de circularidad | 1106 | `...5G NR balancea esto con numerologías (§3).` |
| D3 — FFT como implementación eficiente | 1108 | `...N se elige potencia de 2 para maximizar la eficiencia de la FFT radix-2 (§2).` |
| D4 — Ecualización + estimación de canal | 1110 | `...Sesión 08 desarrolla los estimadores LS y MMSE (§4.5, §4.6, §4.7).` |
| D5 — PAPR como coste energético | 1112 | `...a costa de perder la ecualización de un tap pura (§7).` |

Nota D5: La referencia `(§7)` apunta a la sección §7 de esta misma sesión (PAPR: La Penalización de la Amplificación), no a la Sesión 07 (MIMO masivo). El contexto del documento lo deja claro.

### Task 2: Caption y alt-text de Figura 3 — corrección a 3 paneles

**Alt-text anterior (2 paneles, incorrecto):**
```
Constelaciones QAM tras ecualización ZF (izquierda) vs MMSE (derecha)
```

**Alt-text nuevo (3 paneles, D-15):**
```
Factor de contracción α[k] (izquierda), constelación ZF (centro) y MMSE (derecha) en un canal selectivo en frecuencia
```

**Caption anterior (2 paneles, incorrecto):**
```
**Figura 3.** Dispersión de la constelación QAM tras ecualización en un canal selectivo en frecuencia: ZF (izquierda) amplifica ruido en las subportadoras débiles — la nube se ensancha desproporcionadamente; MMSE (derecha) la contiene mediante regularización con $1/\text{SNR}$ — los puntos quedan más cerca de los símbolos ideales. La diferencia se ve más pronunciada a SNR baja, donde el regularizador domina.
```

**Caption nuevo (3 paneles, D-15):**
```
**Figura 3.** Tres paneles del ecualizador MMSE en un canal selectivo en frecuencia. **Izquierda:** factor de contracción $\alpha[k] \in (0,1)$ por subportadora — valores $\approx 1$ (rojo) indican canal fuerte donde MMSE $\approx$ ZF; valores $\ll 1$ (azul/cian) indican *fades* donde el MMSE modera la amplificación. **Centro:** constelación tras ecualizador ZF — los puntos azules/cian muestran ruido amplificado en las subportadoras débiles. **Derecha:** constelación tras ecualizador MMSE — la contracción $\alpha[k]$ compacta la nube en las subportadoras débiles a costa de un pequeño sesgo.
```

**Estructura HTML exterior preservada (T-03-07, T-03-08):**
```html
<figure markdown="span">
  ![Factor de contracción α[k] (izquierda), ...](figures/mmse-vs-zf-constellation.png)
  <figcaption markdown="1">**Figura 3.** Tres paneles...</figcaption>
</figure>
```

El atributo `markdown="1"` está presente — el LaTeX inline `$\alpha[k]$` se renderizará correctamente.

## Verification Grep Counts

| Check | Comando | Resultado | Esperado |
|-------|---------|-----------|----------|
| D1 parenthetical | `grep -cF "(§2 y §4)." index.md` | **1** | 1 |
| D2 parenthetical | `grep -cE "numerologías \(§3\)\." index.md` | **1** | 1 |
| D3 parenthetical | `grep -cE "FFT radix-2 \(§2\)\." index.md` | **1** | 1 |
| D4 parenthetical | `grep -cF "(§4.5, §4.6, §4.7)." index.md` | **1** | 1 |
| D5 parenthetical | `grep -cE "tap pura \(§7\)\." index.md` | **1** | 1 |
| Dimensiones presentes | `grep -c "^\*\*Dimensión [1-5]:" index.md` | **5** | 5 |
| Image referenciada 1 vez | `grep -c "mmse-vs-zf-constellation.png" index.md` | **1** | 1 |
| Caption viejo eliminado | `grep -c "ZF (izquierda) amplifica ruido" index.md` | **0** | 0 |
| Labels Izquierda/Centro/Derecha | `grep -oE "\*\*Izquierda:\*\*|\*\*Centro:\*\*|\*\*Derecha:\*\*" \| wc -l` | **3** | ≥ 3 |
| figcaption markdown="1" Figura 3 | `grep -c "figcaption markdown=\"1\".*Figura 3"` | **1** | 1 |
| `<figure markdown="span">` count | `grep -c '<figure markdown="span">'` | **3** | 3 (igual que antes) |
| α[k] presente | `grep -cE "α\[k\]" index.md` | **3** | ≥ 1 |
| fades/amplificación | `grep -cE "fade\|amplificación" index.md` | **22** | ≥ 1 |

**Nota sobre el check de labels (Izquierda/Centro/Derecha):** El plan especifica `grep -cE ... ≥ 3` (líneas), pero como el caption es una sola línea larga, `grep -c` retorna 1 línea. La verificación con `grep -o | wc -l` confirma 3 ocurrencias individuales — todos los labels están presentes.

## Observations

### Worktree merge antes de las ediciones
El worktree `agent-a0b493ca5fa5f039c` fue creado antes de que los commits de Plans 01 y 02 llegaran a `main`. Se ejecutó `git merge main --no-edit` (fast-forward) para incorporar todas las ediciones previas de la fase antes de aplicar las del Plan 03.

### Formato parenthetical D-13 (texto plano, sin enlace)
Los 5 parentheticals son texto plano `(§X)` — no son hipervínculos Markdown. T-03-09 (información disclosure) fue clasificado como `accept` en el threat model por ser riesgo bajo: las referencias son texto plano sin enlaces externos.

### Figura 3: estructura HTML intacta
Los tags `<figure markdown="span">` y `</figure>` se preservaron. El número total de figuras con ese tag sigue siendo 3 (Figura 1, Figura 2, Figura 3), confirmando que no se afectaron otras figuras.

## Deviations from Plan

None — el plan se ejecutó exactamente como estaba especificado. Las 5 referencias cruzadas usan el mapa D-14 verbatim y el caption nuevo sigue la formulación de RESEARCH.md Code Examples con el ajuste menor de "azules/cian" en lugar de "azul/cian" para el plural gramatical correcto (plural de puntos de la constelación ZF en subportadoras débiles).

## Known Stubs

None — todas las ediciones son texto pedagógico completo. Los parentheticals son referencias a secciones existentes del documento. El caption de Figura 3 describe la figura real generada por Cell 18 del notebook.

## Threat Flags

None — edición de texto plano dentro de una sección de síntesis existente y reemplazo de caption de figura. No se introdujeron nuevos endpoints de red, paths de autenticación ni cambios de esquema.

## Self-Check: PASSED

- `docs/sessions/03-ofdm-systems/index.md` modificado y commitado
- Commit Task 1: `9870c27` — 5 parentheticals en §7 Síntesis (NARR-03)
- Commit Task 2: `0131983` — caption + alt-text Figura 3 (3 paneles, D-15)
- Todos los grep counts verificados contra criterios de aceptación
- Estructura `<figure markdown="span">...</figure>` intacta (T-03-07)
- Atributo `markdown="1"` preservado en figcaption (T-03-08)
- SUMMARY.md creado en `.planning/phases/03-mejora-de-narrativa/`
