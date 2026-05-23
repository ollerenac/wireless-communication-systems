# Phase 1: Auditoría y Diagnóstico — Pattern Map

**Mapped:** 2026-05-22
**Files analyzed:** 1 (output: `01-AUDIT-FINDINGS.md`)
**Analogs found:** 2 / 1 (index.md y lab.ipynb actúan como analogs del archivo de diagnóstico)

---

## Nota de contexto

Este es un proyecto editorial, no de software. El único archivo que produce esta fase es
`01-AUDIT-FINDINGS.md` — un informe de diagnóstico. Los "patrones" son las convenciones
estructurales observadas en los documentos que se van a auditar: `index.md` y `lab.ipynb`.
No hay archivo análogo previo de auditoría en el repo; se construye desde cero siguiendo
las decisiones de D-01–D-07 de CONTEXT.md.

---

## File Classification

| Archivo a crear | Rol | Flujo de datos | Análogo más cercano | Calidad del match |
|----------------|-----|---------------|--------------------|--------------------|
| `01-AUDIT-FINDINGS.md` | informe de diagnóstico | lectura de index.md + lab.ipynb → registro estructurado | ningún archivo existente en el repo | sin análogo — construir desde decisiones CONTEXT.md |

---

## Pattern Assignments

### `01-AUDIT-FINDINGS.md` (informe de diagnóstico)

No existe análogo directo en el repo. El patrón del informe se construye íntegramente
desde las decisiones D-01–D-07 del CONTEXT.md. Los patrones a continuación describen
lo que el auditor debe reconocer en los documentos fuente para producir entradas
correctas.

---

### Patrón 1 — Estructura del documento `index.md`

**Fuente observada:** `index.md` líneas 1–1326

**Front-matter y estructura de secciones** (líneas 1–19):
```yaml
---
title: "Sesión 03 — Sistemas OFDM e Implementación"
session: 3
description: "..."
---
```
El documento tiene 7 secciones numeradas (§1–§7 implícitos en los headings):
- `## Objetivos de Aprendizaje` (sin número explícito)
- `## Introducción`
- `## Teoría` → `### 1.` … `### 7.`
- `## Síntesis`
- `## Ejercicios`
- `## Laboratorio Python`
- `## Lecturas Recomendadas`

**Convención de figura** (dos variantes coexisten en el mismo documento):

Variante A — `<figure>` con `<figcaption>` (se usa en figuras con leyenda larga):
```markdown
<figure markdown="span">
  ![Texto alt](figures/nombre-archivo.png)
  <figcaption markdown="1">**Figura N.** Descripción...</figcaption>
</figure>
```
Líneas de ejemplo: 59–62, 233–236.

Variante B — `![...]` inline sin `<figure>` (figuras sin leyenda formal o dentro de bloques):
```markdown
![Texto alt](figures/nombre-archivo.png)
```
Líneas de ejemplo: 308, 405, 739, 753, 782, 814, 840, 953, 961.

**Convención de bloques desplegables** (admonitions MkDocs-Material):
```markdown
??? note "Título del bloque"
    Contenido...

??? example "Verificación"
    ```python
    ...
    ```
```

**Convención de snippet de código en §4** — cada bloque 4.x sigue esta estructura:
```markdown
#### 4.x Nombre del Bloque

**Entrada:** descripción — **Operación:** descripción — **Salida:** descripción

[Párrafo teórico + fórmula LaTeX]

```python
def nombre_funcion(...):
    """Docstring."""
    ...
```

??? example "Verificación"
    ```python
    # test mínimo
    ```
```
Líneas de referencia: 542–695 (bloques 4.1–4.4).

---

### Patrón 2 — Referencias de figuras en `index.md` (inventario completo)

El auditor debe usar esta tabla como referencia canónica para la Sección 2 del informe.

| Línea en index.md | Ruta referenciada | Existe en disco | Notas |
|-------------------|------------------|----------------|-------|
| 60 | `figures/isi-problem.png` | SÍ | OK |
| 234 | `figures/ofdm-ifft-transmitter.png` | SÍ | OK |
| 308 | `figures/ofdm-subcarriers.png` | SÍ | OK |
| 405 | `figures/cp-illustration.png` | SÍ | OK |
| 739 | `figures/zf-equalizer-effect.png` | SÍ | OK |
| 753 | `figures/zf-equalizer-qam-comparison.png` | SÍ | OK |
| 782 | `figures/zf-noise-amplification.png` | SÍ | OK |
| 814 | `figures/ofdm-ber-equalizers.png` | SÍ (como `ofdm-ber.png`) | **ROTA** — nombre incorrecto |
| 840 | `figures/channel-estimation-ls.png` | SÍ | OK |
| 868 | `figures/lte-resource-grid-pilots.png` | SÍ | OK |
| 953 | `figures/ofdm-ber-equalizers.png` | SÍ (como `ofdm-ber.png`) | **ROTA** — nombre incorrecto (2.ª ref) |
| 961 | `figures/ofdm-per-subcarrier-ber.png` | NO | **ROTA** — archivo no existe |

Figura en disco sin referenciar:
- `figures/mmse-vs-zf-constellation.png` — generada por `lab.ipynb` celda `81830cd0`, **no referenciada** en `index.md`

---

### Patrón 3 — Snippets de código en `index.md` y sus equivalentes en `lab.ipynb`

El auditor compara cada snippet funcional de `index.md` contra la celda ejecutable
correspondiente. Las firmas de función son la referencia de verdad.

| Snippet en index.md (línea) | Celda en lab.ipynb | Función | Estado |
|-----------------------------|--------------------|---------|--------|
| `qpsk_map` (línea 574–580) | `a5c7793d` (Sección 1 Bloque 1) y `cell-08-ex1-code` (Ejercicio 1) | `def qpsk_map(bits)` | Verificar coincidencia |
| `ofdm_tx` (línea 618–623) | `11d893ff` (Bloque 2) y `cell-08-ex1-code` | `def ofdm_tx(X, N_CP)` | Verificar coincidencia |
| `apply_channel` (línea 648–658) | `3ee4d17a` (Bloque 3) y `cell-13-ex3-code` | `def apply_channel(x_signal, h)` | Verificar coincidencia |
| `ofdm_rx_no_channel` (línea 681–685) | `da295e7a` (Bloque 4) y `cell-11-ex2-code` | `def ofdm_rx_no_channel(...)` | Verificar firma — index.md usa `(y_received, N, N_CP)`; notebook usa `(x_with_cp, N, N_CP)` en Bloque 4 vs `(y_received, N, N_CP)` en Sección 1 |
| ZF snippet (línea 806–808) | `11e22143` (Bloque 5) | `def zf_equalizer(Y, h, N)` | Verificar coincidencia |
| MMSE snippet (línea 806–808 dentro de `??? example`) | `81830cd0` (Bloque 6) | `def mmse_equalizer(Y, h, N, SNR_dB)` | Verificar coincidencia |
| LS estimate (línea 891–894) | `23ad1479` (Bloque 7) | `def ls_channel_estimate(Y, pilot_idx, X_pilot, N)` | Verificar coincidencia |

**Nota sobre `ofdm_rx_no_channel`:** index.md línea 682 define `def ofdm_rx_no_channel(y_received, N, N_CP)`. En la celda `da295e7a` la firma es `def ofdm_rx_no_channel(x_with_cp, N, N_CP)` — mismo orden de argumentos, nombre del primer parámetro diferente. Según D-05, diferencias de nombres de variables **no** se reportan a menos que sean funcionales. El auditor debe confirmar que el comportamiento es idéntico.

---

### Patrón 4 — Estructura del notebook `lab.ipynb`

**Fuente observada:** todas las celdas del notebook

**Secuencia de celdas por ID:**
```
cell-01-title        → Markdown: título + badge Colab
cell-02-objectives   → Markdown: objetivos del lab
cell-03-setup        → Código: imports + configuración global
cell-04-theory       → Markdown: repaso teórico con LaTeX
cell-05-params       → Markdown: separador "Parámetros Globales"
cell-06-params-code  → Código: N=64, N_CP=16, M=4, h_channel definido
4b8a5004            → Markdown: tabla de bloques Sección 1
[Bloques 1–9]       → pares Markdown+Código para cada bloque funcional
2078ebce            → Markdown: separador Sección 2
[Ejercicios 1–6]    → pares Markdown+Código para cada ejercicio
cell-21-conclusions  → Markdown: conclusiones + próximos pasos
```

**Convención de celda de código ejecutable** — cada bloque funcional sigue:
1. Celda Markdown con `### Bloque N — Nombre` + descripción E/S
2. Celda de código con: definición de función → test mínimo → figura → `plt.savefig(...)`

**Figuras que el notebook escribe en disco** (relevante para auditoría de §4 del informe):
| `plt.savefig(...)` en notebook | Celda | Genera archivo en `figures/` |
|-------------------------------|-------|------------------------------|
| `figures/zf-equalizer-effect.png` | `11e22143` | SÍ — existe |
| `figures/zf-equalizer-qam-comparison.png` | `11e22143` | SÍ — existe |
| `figures/mmse-vs-zf-constellation.png` | `81830cd0` | SÍ — existe (huérfana en index.md) |
| `figures/ofdm-ber-equalizers.png` | `a602f4ca` y `cell-16-ex4-code` | SÍ — existe como `ofdm-ber.png` o se sobreescribe |
| `figures/channel-estimation-pilots.png` | `eecd25a6` | NO referenciada en index.md |
| `figures/ofdm-per-subcarrier-ber.png` | `cell-19-ex5-code` | SÍ — esta celda la genera |
| `figures/ofdm-subcarriers.png` | `cell-19-ex5-code` | SÍ — existe |
| `figures/cp-illustration.png` | `cell-19-ex5-code` | SÍ — existe |
| `figures/ofdm-time-domain.png` | `cell-08-ex1-code` | NO referenciada en index.md |
| `figures/cp-effect-constellation.png` | `cell-13-ex3-code` | NO referenciada en index.md |
| `figures/qpsk-decision-regions.png` | `2fd4f44b` | NO referenciada en index.md |

**Observación crítica para Sección 4 del informe:** `ofdm-ber-equalizers.png` es generada
por la celda `a602f4ca` (Sección 1 Bloque 9) con `plt.savefig('figures/ofdm-ber-equalizers.png', ...)`.
Si el notebook se ejecuta limpio, este archivo sí se crea. Su ausencia en disco sugiere que
el notebook no se ha ejecutado desde la última reorganización de figuras.
El archivo `figures/ofdm-ber.png` que sí existe en disco probablemente es una versión anterior
con nombre distinto.

---

### Patrón 5 — Convenciones de fórmulas LaTeX en `index.md`

El auditor identifica fórmulas auditables por estas convenciones:

Fórmulas en bloque (delimitadas por `$$...$$`):
- Línea 27: convolución canal `$$y[n] = \sum_{l=0}^{L-1} h[l]\, x[n-l] + w[n]$$`
- Línea 240: operación receptor (atención: mezcla de factores `1/N` y `1/sqrt(N)` — auditar)
- Línea 263: condición de ortogonalidad
- Línea 599: definición IFFT
- Línea 677: relación convolución circular / multiplicación DFT
- Línea 808: ecualizador MMSE (en bloque de código)
- Línea 836: estimador LS `$$\hat{H}^{LS}[k_p] = \frac{Y[k_p]}{X_p}$$`
- Línea 949: relación Eb/N0 vs SNR (§5.1 — auditar atentamente)
- Líneas 1029–1037: fórmula eficiencia espectral §6 (error de notación conocido — auditar)
- Línea 1063: definición PAPR

**Sección §6 — error de notación conocido** (líneas 1029–1037):
```markdown
$$\eta_{\text{neta}} = \underbrace{\frac{N_{CP}}{N + N_{CP}}}_{\text{overhead CP}} \times ...$$

$$\text{Overhead CP} = \frac{144}{2048 + 144} = \frac{144}{2192} \approx 6{,}6\%$$
```
El término `N_CP / (N + N_CP)` representa la *fracción de overhead*, no la *eficiencia*.
La eficiencia temporal sería `N / (N + N_CP)`. El auditor debe determinar si el factor
en la fórmula principal de eta_neta es correcto o invierte el significado.

**Fórmula de ortogonalidad en §2** (línea 240) — posible inconsistencia de normalización:
index.md línea 240 usa `\frac{1}{N}` frente al símbolo de la suma:
```
\frac{1}{N}\sum_{n=0}^{N-1} x[n] e^{-j2\pi kn/N} = \frac{1}{\sqrt{N}}\sum_{l=0}^{N-1} X[l] (...)
```
El lado izquierdo aplica `1/N` pero el lado derecho produce `1/sqrt(N)`. Si `x[n]` usa la
normalización `1/sqrt(N)` (IFFT ortonormal), la operación del receptor debería aplicar
`1/sqrt(N)` (FFT ortonormal), no `1/N`. El auditor debe verificar si esta mezcla de
factores de normalización es una inconsistencia o un desarrollo pedagógico intencional.

---

## Shared Patterns

### Severidad — cómo clasificar cada hallazgo (D-02)

**Blocker** — impide dictar la clase:
- Fórmula que produce resultado incorrecto si un estudiante la aplica
- Figura con `<figure>` o `![]()` apuntando a archivo que no existe en `figures/`
- Snippet Python con API incorrecta (función inexistente, argumentos en orden distinto)
- Lógica de código que produce resultado diferente al notebook ejecutado

**Minor** — inconsistencia que no confunde:
- Variable renombrada entre index.md y notebook (mismo comportamiento)
- Texto levemente desactualizado pero sin error factual
- Figura huérfana en disco (no referenciada) sin impacto en el texto

### Formato de entrada en el informe (D-03)

Cada entrada sigue exactamente esta estructura:
```
**[BLOCKER|MINOR]-NN**: [descripción en una oración]
- **Ubicación:** `index.md` línea XXX / celda `ID-celda`
- **Texto actual:** "[cita textual del fragmento problemático]"
```

No se incluye propuesta de corrección — eso es trabajo de Fase 2.

### Secciones del informe (D-04)

El informe `01-AUDIT-FINDINGS.md` tiene exactamente 4 secciones:
```
## 1. Fórmulas y Enunciados Incorrectos
## 2. Referencias de Figuras (Rotas / Huérfanas)
## 3. Snippets de Código Desalineados
## 4. Estado del Notebook (lab.ipynb)
```

### Criterio de inclusión de snippets (D-05, D-06)

Un snippet de index.md entra en la Sección 3 **solo si**:
1. La diferencia es funcional (API distinta, lógica que produce resultado diferente)
2. Existe una celda ejecutable equivalente en lab.ipynb para comparar

Diferencias de estilo, nombres de variables y formato **no** se reportan.

---

## No Analog Found

| Archivo | Rol | Flujo | Razón |
|---------|-----|-------|-------|
| `01-AUDIT-FINDINGS.md` | informe de diagnóstico | lectura → registro | No existe ningún archivo de auditoría previo en el repo. El planner debe construir la estructura desde las decisiones D-01–D-07 del CONTEXT.md y los patrones de formato descritos arriba. |

---

## Metadata

**Scope de búsqueda de análogos:** directorio raíz y `.planning/`
**Archivos escaneados:** index.md (1326 líneas), lab.ipynb (completo, ~1800 líneas), REQUIREMENTS.md, ROADMAP.md, CONTEXT.md
**Fecha de mapeo:** 2026-05-22
