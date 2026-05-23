---
phase: 03-mejora-de-narrativa
verified: 2026-05-22T21:50:00-05:00
status: human_needed
score: 11/12 must-haves verified
overrides_applied: 0
human_verification:
  - test: "Leer la transición 4.6→4.7 en §4 y evaluar si el gap D-03 ('ZF y MMSE asumen H[k] conocido') queda explícito para el estudiante"
    expected: "El lector entiende que en la práctica el canal no se conoce y que los pilotos lo resuelven, sin necesidad de buscar frases como 'ZF y MMSE asumen que H[k] es conocido' literalmente"
    why_human: "La verificación automatizada de D-03 no encontró las frases exactas del plan, pero el texto real ('asumiendo que el canal es perfectamente conocido por el receptor. En la práctica nadie entrega ese vector') transmite el mismo contenido. Solo un lector puede confirmar si la articulación es pedagógicamente suficiente."
---

# Phase 03: Mejora de Narrativa — Verification Report

**Phase Goal:** Fortalecer la narrativa pedagógica del index.md mejorando el hilo conductor de §4, la transición de la Introducción hacia OFDM, y los anclajes de §7 Síntesis — sin alterar el contenido técnico de fondo.
**Verified:** 2026-05-22T21:50:00-05:00
**Status:** human_needed
**Re-verification:** No — initial verification

---

## Goal Achievement

### Observable Truths

| #  | Truth | Status | Evidence |
|----|-------|--------|----------|
| 1  | Cada bloque §4.1–§4.8 termina con un párrafo de transición pregunta-respuesta antes del `---` que lo cierra | ✓ VERIFIED | `grep -c "La pregunta natural es"` = 8 (6 nuevas + 1 existente §4.5→4.6 + 1 cierre §4.8→§5). 8 `"La respuesta es"`. Las 8 transiciones aparecen en líneas 591, 637, 673, 702, 792, 835, 915, 952. |
| 2  | El cierre de §4 contiene un bloque de código que demuestra la cadena completa bits→bits_hat con comentarios por sección | ✓ VERIFIED | Snippet en líneas 957–965 con variables `X`, `x_cp`, `y_noisy`, `Y`, `X_hat`, `bits_hat` y comentarios `# §4.1` … `# §4.8`. Todas las funciones presentes: `qpsk_map(bits)`, `ofdm_tx(X, N_CP)`, `apply_channel(x_cp, h_channel) + noise`, `ofdm_rx_no_channel(y_noisy, N, N_CP)`, `zf_equalizer(Y, h_channel, N)`, `qpsk_demap(X_hat)`. |
| 3  | El bug WR-01 (doble `---` entre §4.8 y §5) está corregido — queda un único `---` | ✓ VERIFIED | `awk '/^---$/{c++} END{print c}'` = 26 (bajó de 27). El check de pares `---` consecutivos retornó 0. |
| 4  | La transición existente 4.5→4.6 permanece intacta | ✓ VERIFIED | `sed -n '780,800p' \| grep "más inteligente en esas"` = 1. Texto en línea 792 sin modificar. |
| 5  | La transición 4.6→4.7 articula el gap D-03 (ZF/MMSE asumen canal conocido → pilotos lo resuelven) | ? UNCERTAIN | El texto en línea 835 dice: "tanto el ZF como el MMSE calculan H[k] a partir de `h_channel` — asumiendo que el canal es perfectamente conocido por el receptor. En la práctica nadie entrega ese vector al receptor. ¿Cómo se obtiene H[k] cuando el canal es desconocido? La respuesta es transmitir símbolos piloto." El contenido conceptual es correcto pero no usa las frases literales que el PLAN especificó como patrón de aceptación (`grep -n "ZF y MMSE asumen\|H[k] es conocido\|hay que estimarlo"` → 0 matches). Requiere decisión humana sobre si la formulación alternativa es pedagógicamente equivalente. |
| 6  | El párrafo de la Introducción menciona explícitamente que Sesión 02 asumió canal AWGN plano (un coeficiente escalar) y que aquí el canal es frequency-selective | ✓ VERIFIED | Línea 23: "La Sesión 02 resolvió el canal AWGN plano — un coeficiente escalar de canal que el receptor puede invertir directamente. Aquí el canal es frequency-selective — no existe un único coeficiente que corrija todo el espectro." `grep -c "AWGN plano"` = 1, `grep -c "coeficiente escalar de canal"` = 1, `grep -c "no existe un único coeficiente"` = 1. |
| 7  | La progresión Sesión 01 → Sesión 02 → OFDM se lee sin saltos lógicos | ✓ VERIFIED | La frase D-10 queda antes de "Pero hay un problema que no resolvimos" (posición de carácter 1348 < 1538). La frase de preview "símbolos QAM → IFFT → CP → canal → FFT" sigue intacta. `grep -c "Pero hay un problema que no resolvimos"` = 1. |
| 8  | Cada una de las 5 dimensiones de §7 Síntesis termina con referencia parenthetical a la(s) sección(es) donde se desarrolló | ✓ VERIFIED | Los 5 greps retornan 1 cada uno: `(§2 y §4).` (D1), `numerologías (§3).` (D2), `FFT radix-2 (§2).` (D3), `(§4.5, §4.6, §4.7).` (D4), `tap pura (§7).` (D5). Las 5 dimensiones con formato `**Dimensión N:**` siguen presentes: `grep -c "^\*\*Dimensión [1-5]:"` = 5. |
| 9  | El caption de Figura 3 describe los tres paneles (factor α[k] izquierda, ZF centro, MMSE derecha) en lugar de dos | ✓ VERIFIED | Línea 949: "**Figura 3.** Tres paneles del ecualizador MMSE... **Izquierda:** factor de contracción $\alpha[k]$... **Centro:** constelación tras ecualizador ZF... **Derecha:** constelación tras ecualizador MMSE". `grep -oE "(\*\*Izquierda:\*\*|\*\*Centro:\*\*|\*\*Derecha:\*\*)" \| wc -l` = 3. Caption viejo eliminado: `grep -c "ZF (izquierda) amplifica ruido"` = 0. |
| 10 | El alt-text de Figura 3 enumera los tres paneles | ✓ VERIFIED | Línea 948: `![Factor de contracción α[k] (izquierda), constelación ZF (centro) y MMSE (derecha) en un canal selectivo en frecuencia](figures/mmse-vs-zf-constellation.png)`. |
| 11 | Los 4 PNGs han sido inspeccionados y el working tree queda limpio | ✓ VERIFIED | `git status --porcelain figures/*.png` = vacío (0 líneas). Commits `1fa8fac` (fix colorbar) y `19f4051` (figuras con turbo colormap) presentes en git log. |
| 12 | El `index.md` sigue siendo válido MkDocs-Material (estructura de fenced code y figcaptions intactas) | ✓ VERIFIED | `grep -c "figcaption markdown=\"1\""` = 3 (todas las figuras tienen el atributo; Figura 3 lo conserva). `grep -c "<figure markdown=\"span\">"` = 3. El bloque de código Python del snippet usa triple backtick con lenguaje. |

**Score:** 11/12 truths verified (1 UNCERTAIN → ver item #5)

---

### Deferred Items

Ninguno — todos los items de la fase están dentro del alcance de Phase 03.

---

### Required Artifacts

| Artifact | Expected | Status | Details |
|----------|----------|--------|---------|
| `index.md` | 7 transiciones §4 + bloque de cierre + D-10 + parentheticals §7 + Figura 3 corregida | ✓ VERIFIED | Todos los cambios presentes. 8 "La pregunta natural es", 26 `---`, snippet lines 957–965, frase D-10 en línea 23, 5 parentheticals, caption Figura 3 con 3 paneles. |
| `figures/cp-illustration.png` | Committed or reverted | ✓ VERIFIED | Working tree limpio. Commiteado en `19f4051`. |
| `figures/ofdm-subcarriers.png` | Committed or reverted | ✓ VERIFIED | Working tree limpio. Commiteado en `19f4051`. |
| `figures/zf-equalizer-effect.png` | Committed or reverted | ✓ VERIFIED | Working tree limpio. Commiteado en `19f4051`. |
| `figures/zf-equalizer-qam-comparison.png` | Committed or reverted (con fix de colorbar) | ✓ VERIFIED | Bug de colorbar corregido en `lab.ipynb` (`1fa8fac`), PNG regenerado y commiteado en `19f4051`. Working tree limpio. |

---

### Key Link Verification

| From | To | Via | Status | Details |
|------|----|-----|--------|---------|
| `§4.8 (línea ~964)` | `§5` | transición D-04 + snippet + único `---` | ✓ WIRED | Línea 952: transición D-04 presente. Snippet en 957–965. Un único `---` tras snippet. `### 5. Rendimiento End-to-End` sigue presente (`grep -c` = 1). |
| Snippet de cierre §4 | funciones §4.1–§4.8 | nombres D-08 | ✓ WIRED | `qpsk_map(bits)`, `ofdm_tx(X, N_CP)`, `apply_channel(x_cp, h_channel)`, `ofdm_rx_no_channel(y_noisy, N, N_CP)`, `zf_equalizer(Y, h_channel, N)`, `qpsk_demap(X_hat)` — todos presentes en el snippet y definidos en §4.1–§4.8. |
| Frase D-10 Introducción | "Pero hay un problema" | inserción inline mismo párrafo | ✓ WIRED | D-10 en posición 1348, "Pero hay un problema" en 1538 — mismo párrafo, orden correcto. |
| §7 Dimensión 1 | §2 y §4 | parenthetical `(§2 y §4)` | ✓ WIRED | `grep -cF "(§2 y §4)."` = 1. |
| Figura 3 caption | código real Cell 18 (`plt.subplots(1, 3)`) | descripción de 3 paneles | ✓ WIRED | Caption describe exactamente izquierda (α[k]), centro (ZF), derecha (MMSE) — alineado con `plt.subplots(1, 3)`. |

---

### Behavioral Spot-Checks

| Comportamiento | Comando | Resultado | Estado |
|----------------|---------|-----------|--------|
| 8 transiciones pregunta-respuesta en §4 | `grep -c "La pregunta natural es" index.md` | 8 | ✓ PASS |
| 8 frases de cierre de transición | `grep -c "La respuesta es" index.md` | 8 | ✓ PASS |
| 8 subsecciones §4.x presentes | `grep -c "^#### 4\." index.md` | 8 | ✓ PASS |
| Bug WR-01 corregido (26 separadores) | `awk '/^---$/{c++} END{print c}' index.md` | 26 | ✓ PASS |
| Snippet: qpsk_demap(X_hat) presente | `grep -c "qpsk_demap(X_hat)" index.md` | 1 | ✓ PASS |
| Nota D-07 presente | `grep -c "Transceptor OFDM uncoded" index.md` | 1 | ✓ PASS |
| Frase D-10 AWGN plano | `grep -c "AWGN plano" index.md` | 1 | ✓ PASS |
| 5 parentheticals §7 | 5 greps individuales | 1 cada uno | ✓ PASS |
| Caption Figura 3: 3 labels | `grep -oE "Izquierda\|Centro\|Derecha" \| wc -l` | 3 | ✓ PASS |
| Caption viejo eliminado | `grep -c "ZF (izquierda) amplifica ruido"` | 0 | ✓ PASS |
| PNGs limpios en working tree | `git status --porcelain figures/*.png \| wc -l` | 0 | ✓ PASS |
| Pares `---` consecutivos | awk consecutivo check | 0 | ✓ PASS |
| Transición §4.5→4.6 original intacta | `grep "más inteligente en esas" index.md` | 1 (línea 792) | ✓ PASS |
| Commits declarados existen en git log | `git log --oneline` | `8f49404`, `379a9c4`, `df05be0`, `9870c27`, `0131983`, `1fa8fac`, `19f4051` — todos presentes | ✓ PASS |
| Transición D-03 (frases literales del plan) | `grep -n "ZF y MMSE asumen\|hay que estimarlo"` | 0 matches | ? SKIP — ver Human Verification |

---

### Requirements Coverage

| Requirement | Plan | Descripción | Estado | Evidencia |
|-------------|------|-------------|--------|-----------|
| NARR-01 | 03-01 | Hilo conductor §4: transiciones pregunta-respuesta + bloque de cierre | ✓ SATISFIED | 8 transiciones + snippet en index.md verificados por grep. |
| NARR-02 | 03-02 | Introducción: brecha Sesión 02 → OFDM explícita | ✓ SATISFIED | Frase D-10 en línea 23, `grep -c "AWGN plano"` = 1. |
| NARR-03 | 03-03 | §7 Síntesis: referencias cruzadas parenthetical | ✓ SATISFIED | 5 parentheticals verificados. |

---

### Anti-Patterns Found

| Archivo | Línea | Patrón | Severidad | Impacto |
|---------|-------|--------|-----------|---------|
| Ninguno encontrado | — | — | — | — |

Se escanearon los cambios de la fase en `index.md`. No hay marcadores `TBD`, `FIXME`, `XXX`, `TODO`, `PLACEHOLDER` ni `return null`/`return []` en el texto insertado. El snippet de Python es pedagógicamente completo (no hay stub). La nota D-07 es párrafo plano visible (no admonition colapsable).

---

### Human Verification Required

#### 1. Formulación de la transición 4.6→4.7 (gap D-03)

**Test:** Leer el párrafo en línea 835 de `index.md` (transición de §4.6 MMSE hacia §4.7 Estimación de Canal). El texto actual dice: *"tanto el ZF como el MMSE calculan H[k] a partir de `h_channel` — asumiendo que el canal es perfectamente conocido por el receptor. En la práctica nadie entrega ese vector al receptor. ¿Cómo se obtiene H[k] cuando el canal es desconocido? La respuesta es transmitir símbolos piloto conocidos en posiciones conocidas, y estimar el canal a partir de ellos."*

**Expected:** El estudiante que llega de §4.6 (MMSE) entiende inmediatamente que el supuesto de canal conocido es la brecha que §4.7 resuelve, sin necesitar la formulación literal del plan ("ZF y MMSE asumen que H[k] es conocido").

**Why human:** El check automatizado buscó frases literales del plan (`"ZF y MMSE asumen"`, `"H[k] es conocido"`, `"hay que estimarlo"`) y no encontró ninguna (0 matches). El texto real usa formulación distinta pero conceptualmente equivalente. Solo un instructor puede juzgar si la formulación es pedagógicamente suficiente para el nivel de posgrado del curso.

---

### Gaps Summary

No hay gaps bloqueantes. El único item incierto (#5) es una diferencia de formulación en la transición 4.6→4.7: el plan exigía ciertas frases literales de D-03 y el texto resultante expresa el mismo concepto con palabras distintas. El contenido técnico es correcto; la decisión es editorial/pedagógica y requiere confirmación humana.

---

_Verified: 2026-05-22T21:50:00-05:00_
_Verifier: Claude (gsd-verifier)_
