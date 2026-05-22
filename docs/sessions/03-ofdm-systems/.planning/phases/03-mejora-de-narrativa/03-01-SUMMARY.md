---
phase: 03-mejora-de-narrativa
plan: 01
subsystem: index.md
tags:
  - narrative
  - markdown
  - mkdocs
  - ofdm

dependency_graph:
  requires: []
  provides:
    - "7 transiciones §4 en estilo pregunta-respuesta (NARR-01)"
    - "Bloque de cierre §4: nota D-07 + snippet cadena completa D-06/D-08"
    - "Corrección bug WR-01 (doble ---)"
  affects:
    - "index.md §4.1–§4.8 (transiciones de sección)"
    - "index.md §4.8→§5 (bloque de cierre)"

tech_stack:
  added: []
  patterns:
    - "Patrón pregunta-respuesta: La pregunta natural es: […] La respuesta es […]"
    - "Snippet pedagógico con comentarios # §4.X por línea"
    - "Párrafo plano (no admonition) como nota previa al snippet"

key_files:
  created: []
  modified:
    - path: "docs/sessions/03-ofdm-systems/index.md"
      description: "7 transiciones §4 nuevas + bloque de cierre + corrección WR-01"

decisions:
  - "Transiciones en texto plano corriente (sin admonition, sin negrita) — consistente con template 4.5→4.6"
  - "Nota D-07 como párrafo plano (no ??? note colapsable) para que el estudiante no la omita"
  - "Snippet usa zf_equalizer (no MMSE) por simplicidad pedagógica — el lector ya conoce ambos"
  - "Nombres de variable D-08 estrictamente: X, x_cp, y_noisy, Y, X_hat, bits_hat"

metrics:
  duration: "3 minutes"
  completed_date: "2026-05-22"
  tasks_completed: 2
  tasks_total: 2
  files_modified: 1
---

# Phase 03 Plan 01: Transiciones §4 y Bloque de Cierre — Summary

**One-liner:** 7 transiciones pregunta-respuesta en §4 más snippet de cadena completa bits→bits_hat y corrección del doble `---` (WR-01)

## What Was Built

### Task 1: 6 transiciones intermedias §4

Seis párrafos de transición insertados en `index.md` siguiendo el patrón canónico de la transición 4.5→4.6 existente (línea 792). Cada transición nombra el problema que deja pendiente el bloque origen y la respuesta del bloque destino.

**Líneas finales de cada transición:**

| Transición | Línea en index.md | Pregunta que articula |
|------------|-------------------|-----------------------|
| 4.1→4.2 | 591 | N símbolos en frecuencia no son señal transmisible → IFFT + CP convierte a tiempo |
| 4.2→4.3 | 637 | x_cp banda-base discreta → canal real deforma con ecos multipath |
| 4.3→4.4 | 673 | y_noisy mezcla ecos → CP + FFT separa subportadoras en N escalares independientes |
| 4.4→4.5 | 702 | Y[k]=H[k]X[k]+W[k] distorsionado → ecualizador divide subportadora a subportadora |
| 4.5→4.6 | 792 | **YA EXISTÍA — NO MODIFICADA** (template canónico) |
| 4.6→4.7 | 835 | ZF/MMSE asumen h_channel conocido (D-03) → pilotos para estimar H[k] en práctica |
| 4.7→4.8 | 915 | X_hat complejo → demapper asigna punto de constelación y extrae bits |

### Task 2: Bloque de cierre §4 + corrección WR-01

Insertado entre `</figure>` de Figura 3 y `### 5. Rendimiento End-to-End`:

1. **Transición D-04 (línea 952):** cierre de cadena con demapper → pregunta ¿qué tan bien funciona? → respuesta es curva BER de §5
2. **Nota D-07 (línea 955):** párrafo plano "transceptor OFDM sin codificación de canal — BER de §5 mide exactamente este sistema — LDPC Sesión 04 como capa superior"
3. **Snippet D-06/D-08 (líneas 957–965):**

```python
# Transceptor OFDM uncoded — exactamente lo que §5 mide con la curva BER
bits     = rng.integers(0, 2, N * 2)               # bits aleatorios (2 bits/símbolo QPSK)
X        = qpsk_map(bits)                           # §4.1  mapper
x_cp     = ofdm_tx(X, N_CP)                        # §4.2  IFFT + CP
y_noisy  = apply_channel(x_cp, h_channel) + noise  # §4.3  canal + AWGN
Y        = ofdm_rx_no_channel(y_noisy, N, N_CP)    # §4.4  eliminar CP + FFT
X_hat    = zf_equalizer(Y, h_channel, N)           # §4.5  ecualizador ZF
bits_hat = qpsk_demap(X_hat)                       # §4.8  demapper
ber      = np.mean(bits != bits_hat)
```

4. **Bug WR-01 corregido:** el doble `---` (líneas 952/954 del estado pre-tarea) fue reemplazado por un único `---`. El total de separadores pasó de 27 a 26.

## Verification Grep Counts

| Check | Comando | Resultado | Esperado |
|-------|---------|-----------|----------|
| Transiciones totales | `grep -c "La pregunta natural es"` | **8** | ≥8 |
| Respuestas totales | `grep -c "La respuesta es"` | **8** | ≥8 |
| Subsecciones §4.x | `grep -c "^#### 4\."` | **8** | 8 |
| Separadores `---` | `awk '/^---$/{c++} END{print c}'` | **26** | 26 |
| qpsk_demap(X_hat) | `grep -c "qpsk_demap(X_hat)"` | **1** | ≥1 |
| Snippet header | `grep -c "Transceptor OFDM uncoded"` | **1** | 1 |
| LDPC / Sesión 04 | `grep -c "LDPC"` / `grep -c "Sesión 04"` | **5** / **4** | ≥1 |
| Pares `---` consecutivos | awk consecutivo check | **0** | 0 |
| Transición §4.5 intacta | `sed -n '780,795p' \| grep "más inteligente"` | **1** | 1 |
| §5 heading | `grep -c "^### 5\. Rendimiento End-to-End$"` | **1** | 1 |

## Observations

### Nota D-07 — formato párrafo plano
La nota D-07 se insertó como párrafo de texto corriente (no como admonition `??? note`), en cumplimiento de PATTERN 5 y Pitfall 2. El estudiante no puede colapsarla: el aviso sobre uncoded OFDM y la relación con §5/Sesión 04 es siempre visible.

### Transición existente §4.5→4.6 preservada
La transición canónica en línea 792 no fue tocada. Todas las verificaciones la encuentran intacta.

### Snippet con nombres D-08
Los nombres de variable (`X`, `x_cp`, `y_noisy`, `Y`, `X_hat`, `bits_hat`) coinciden exactamente con los definidos en D-08 y verificados contra Cell 24 del notebook. La función `qpsk_demap(X_hat)` usa la firma de Cell 22.

## Deviations from Plan

None — el plan se ejecutó exactamente como estaba especificado.

## Known Stubs

None — todas las inserciones son texto pedagógico completo y funcional. El snippet muestra la cadena con las funciones ya definidas en §4.1–§4.8.

## Threat Flags

None — no se introdujeron nuevos endpoints de red, paths de autenticación ni cambios de esquema.

## Self-Check: PASSED

- `docs/sessions/03-ofdm-systems/index.md` modificado y commitado
- Commit Task 1: `8f49404` — 6 transiciones §4
- Commit Task 2: `379a9c4` — bloque de cierre + WR-01
- Todos los grep counts verificados contra criterios de aceptación
- SUMMARY.md creado en `.planning/phases/03-mejora-de-narrativa/`
