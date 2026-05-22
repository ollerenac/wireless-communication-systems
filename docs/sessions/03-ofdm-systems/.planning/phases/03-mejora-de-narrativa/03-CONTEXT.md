# Phase 3: Mejora de Narrativa - Context

**Gathered:** 2026-05-22
**Status:** Ready for planning

<domain>
## Phase Boundary

Fortalecer el hilo conductor pedagógico de `index.md` — sin tocar `lab.ipynb` ni reorganizar la estructura de secciones. Las tres palancas: (1) frases de transición entre bloques de §4 que nombran el problema que resuelve cada bloque y el que deja pendiente; (2) un párrafo de puente en la Introducción que cierra el gap Sesión 02 → OFDM; (3) referencias cruzadas explícitas en §7 Síntesis hacia las secciones donde cada dimensión se desarrolló. Incluye también: bloque de cierre §4 que demuestra la cadena completa (bits→bits_hat), corrección del caption de Figura 3 (3 paneles), commit de los 4 PNGs re-generados si son mejoras visuales, y corrección del bug WR-01 (doble `---`).

</domain>

<decisions>
## Implementation Decisions

### Transiciones §4 (NARR-01)

- **D-01:** Estilo de transición: **patrón pregunta-respuesta**, igual que la transición 4.5→4.6 ya existente. Cada bloque termina nombrando la limitación que resuelve y la pregunta que deja pendiente, con la respuesta apuntando al bloque siguiente. Ejemplo canónico (verbatim de §4.5): *"La pregunta natural es: ¿existe un ecualizador que sea más inteligente en esas subportadoras?… La respuesta es sí, y ese ecualizador es el MMSE."*
- **D-02:** Ubicación: **al final del bloque que cierra**, inmediatamente antes del `---` separador. Consistente con el patrón ya establecido en §4.5.
- **D-03:** Transición 4.6→4.7: puente desde la suposición implícita de H conocido. La frase debe articular: *"ZF y MMSE asumen que H[k] es conocido. En la práctica nadie nos lo da — hay que estimarlo. El siguiente bloque muestra cómo."* (Claude tiene discreción sobre la redacción exacta.)
- **D-04:** Cierre §4.8→§5: cierre de cadena + pregunta de rendimiento. Articular: *"Con el demapper, la cadena completa está cerrada. La pregunta natural es: ¿qué tan bien funciona el sistema? La respuesta es la curva BER de §5."* (Claude tiene discreción sobre la redacción exacta.)
- **D-05:** Las transiciones 4.1→4.2, 4.2→4.3, 4.3→4.4, 4.4→4.5, y 4.7→4.8 son delegadas a Claude siguiendo el mismo patrón pregunta-respuesta (D-01). La transición 4.5→4.6 ya existe y **no se modifica**.

### Bloque de cierre §4 — cadena completa (NARR-01 extensión)

- **D-06:** Agregar al final de §4 (después de §4.8, antes del `---` final) un snippet de código que demuestre la **cadena completa uncoded OFDM**: `bits → qpsk_map → ofdm_tx → apply_channel + noise → ofdm_rx_no_channel → zf_equalizer → qpsk_demap → bits_hat`. Un solo snippet (~15 líneas), con comentarios que identifican cada paso por sección (ej. `# §4.1 Mapper`, `# §4.2 IFFT+CP`, etc.).
- **D-07:** Incluir antes del snippet una nota breve explícita: *"Este es el transceptor OFDM sin codificación de canal — la BER de §5 mide exactamente este sistema. La codificación LDPC (Sesión 04) se añade encima de esta cadena."* Justifica la omisión de FEC con el argumento correcto: uncoded OFDM es el baseline pedagógico de esta sesión.
- **D-08:** El snippet usa las funciones definidas en §4.1–§4.8 con nombres de variables consistentes: `X` (salida §4.1), `x_cp` (salida §4.2), `y_noisy` (salida §4.3), `Y` (salida §4.4), `X_hat` (salida §4.5/§4.6), `bits_hat` (salida §4.8). El notebook Cell 24 (`ofdm_ber_quick`) tiene la cadena de referencia — usarla para verificar nombres y orden.

### Corrección bug WR-01

- **D-09:** Eliminar el `---` duplicado entre §4.8 y §5 (líneas 940–942 tienen dos `---` consecutivos). Corregir en el mismo plan que las transiciones §4.

### Introducción (NARR-02)

- **D-10:** Agregar al puente Sesión 02→OFDM la **brecha explícita**: *"La Sesión 02 resolvió el canal AWGN plano — un coeficiente escalar de canal que el receptor puede invertir directamente. Aquí el canal es frequency-selective — no existe un único coeficiente que corrija todo el espectro."* Esto cierra el gap entre lo aprendido y el nuevo problema.
- **D-11:** No agregar párrafo de preview de secciones. La última frase de la intro actual (*"Esta sesión construye esa cadena completa: símbolos QAM → IFFT → CP → canal → FFT → ecualización de un tap"*) ya hace de preview adecuado.
- **D-12:** Intervención mínima en la Introducción — solo el parche del trade-off explícito (D-10). No reescribir párrafos que ya funcionan.

### Referencias cruzadas §7 Síntesis (NARR-03)

- **D-13:** Formato: **parenthetical al final** de la línea de "Implicación de diseño" de cada dimensión: `(§X)` o `como se desarrolla en §X.` — conciso, no interrumpe el flujo.
- **D-14:** Mapa de referencias por dimensión:
  - Dimensión 1 (FSF → N canales flat): `(§2 y §4)`
  - Dimensión 2 (CP como precio de circularidad): `(§3)`
  - Dimensión 3 (FFT como implementación eficiente): `(§2)`
  - Dimensión 4 (ecualización + estimación): `(§4.5, §4.6, §4.7)`
  - Dimensión 5 (PAPR): `(§7)`

### Figura 3 — corrección de caption

- **D-15:** El caption de Figura 3 (`mmse-vs-zf-constellation.png`) es incorrecto: menciona 2 paneles (ZF izquierda, MMSE derecha) pero la figura tiene **3 paneles** (confirmado: `plt.subplots(1, 3)` en Cell 18 del notebook). Los paneles son: **izquierda**: factor de contracción α[k] por subportadora; **centro**: constelación ZF; **derecha**: constelación MMSE. El nuevo caption debe describir los 3 paneles.

### 4 PNGs modificados sin commitear

- **D-16:** Los 4 PNGs (`cp-illustration.png`, `ofdm-subcarriers.png`, `zf-equalizer-effect.png`, `zf-equalizer-qam-comparison.png`) aparecen modificados en el working tree (re-generados con colormap turbo). El agente de ejecución los inspecciona visualmente antes de commitear. Si son mejoras (mayor contraste, mejor legibilidad), se commitean en Fase 3 con mensaje `fig(03): commit re-generated figures with turbo colormap`. Si alguno no mejora, se revierte individualmente.

### Claude's Discretion

- Redacción exacta de cada frase de transición (D-01, D-03, D-04, D-05) — siguiendo el patrón pregunta-respuesta como template, pero adaptada al contenido específico de cada bloque.
- Longitud de cada transición — de 1 a 4 oraciones, lo que sea necesario para nombrar el problema resuelto y el problema pendiente.
- Ubicación exacta del bloque de cierre §4 dentro de §4.8 (antes o después de la figura, siempre antes del `---`).

</decisions>

<canonical_refs>
## Canonical References

**Downstream agents MUST read these before planning or implementing.**

### Documento a modificar
- `index.md` — único archivo de narrativa que se modifica en esta fase

### Ground truth (solo lectura)
- `lab.ipynb` — notebook ejecutable; **Cell 18** (`plt.subplots(1, 3)`) confirma 3 paneles en Figura 3; **Cell 24** (`ofdm_ber_quick`) contiene la cadena completa de referencia para el snippet de cierre §4; **Cells 8–20** contienen las firmas de todas las funciones de §4.1–§4.8

### Requisitos y restricciones
- `.planning/REQUIREMENTS.md` — IDs NARR-01, NARR-02, NARR-03 (active); LAB-01 (pendiente); decisión sobre 4 PNGs
- `.planning/PROJECT.md` — constraints: idioma español, MkDocs-Material, 8h, notebook como ground truth

### Hallazgos previos
- `.planning/phases/01-auditor-a-y-diagn-stico/01-AUDIT-FINDINGS.md` — bug WR-01 (doble `---` entre §4.8 y §5, líneas 940–942); hallazgos de narrativa

### Decisiones de fases anteriores
- `.planning/phases/02-correcci-n-de-contenido/02-CONTEXT.md` — D-01 a D-09 (no re-discutir); patrón de figura establecido

</canonical_refs>

<code_context>
## Existing Code Insights

### Funciones disponibles en §4 (para el snippet de cierre)

Estas funciones están definidas en los bloques de §4 y son la base del snippet de cadena completa:

| Función | Definida en | Firma |
|---------|------------|-------|
| `qpsk_map(bits)` | §4.1 | `bits: ndarray → X: ndarray[complex]` |
| `ofdm_tx(X, N_CP)` | §4.2 | `→ x_cp: ndarray` de longitud N+N_CP |
| `apply_channel(x, h)` | §4.3 | `→ y: ndarray` (convolución lineal) |
| `ofdm_rx_no_channel(y, N, N_CP)` | §4.4 | `→ Y: ndarray[complex]` (elimina CP + FFT) |
| `zf_equalizer(Y, h, N)` | §4.5 | `→ X_hat: ndarray[complex]` |
| `mmse_equalizer(Y, h, N, SNR_dB)` | §4.6 | `→ X_hat: ndarray[complex]` |
| `ls_channel_estimate(Y, pilot_idx, X_pilot, N)` | §4.7 | `→ H_est: ndarray[complex]` |

El demapper (§4.8) es una operación inline (`np.argmin` o lookup de la constelación) — no tiene función named en el notebook; el snippet debe incluirlo inline.

### Transición template (la única existente — NO modificar)

```
La pregunta natural es: ¿existe un ecualizador que sea más inteligente en esas subportadoras? En lugar de invertir el canal ciegamente, ¿podría detectar que una subportadora está muy atenuada y moderar su respuesta para no amplificar el ruido? La respuesta es sí, y ese ecualizador es el MMSE.
```
*Fuente: §4.5, líneas ~780–784 de index.md*

### Patrones MkDocs-Material establecidos
- Figuras: `<figure markdown="span">` con `<figcaption markdown="1">**Figura N.** ...`
- Admonitions: `??? note "Título"` (plegable) o `!!! warning "Título"` (expandido)
- Separadores de subsección: `---` (uno solo, no doble)

### Figura 3 — estructura real (Cell 18 del notebook)
```python
fig, axes = plt.subplots(1, 3, figsize=(17, 4.5))
# axes[0]: α[k] — factor de contracción MMSE por subportadora
# axes[1]: constelación ZF (scatter)
# axes[2]: constelación MMSE (scatter)
```

</code_context>

<specifics>
## Specific Ideas

- La transición 4.6→4.7 cierra la suposición implícita: §4.5 y §4.6 dicen `H = np.fft.fft(h_channel, n=N)` asumiendo h_channel conocido, pero nunca explican cómo se obtiene en la práctica. La transición debe hacer ese gap explícito antes de que §4.7 lo resuelva.
- El bloque de cierre §4 puede usar el ZF como ecualizador (más simple visualmente) o dejar al lector elegir con un `equalize='zf'` / `equalize='mmse'` — Claude decide según lo que resulte más pedagógico.
- Para el caption de Figura 3: la descripción de α[k] debe mencionar que valores ≈ 1 indican subportadoras fuertes (MMSE ≈ ZF) y valores ≪ 1 indican fades donde el MMSE modera la amplificación.
- El argumento de omitir FEC: *"Este snippet es el transceptor uncoded OFDM — exactamente el sistema que §5 mide con la curva BER. La codificación LDPC (Sesión 04) se agrega como una capa superior a esta cadena."*
- Introducción: el gap es específico. La frase actual dice *"pero hay un problema que no resolvimos: ¿qué ocurre cuando aplicamos una única portadora M-QAM de alta tasa sobre un canal frequency-selective?"* — falta decir explícitamente que la Sesión 02 asumió AWGN plano y que ese supuesto no se cumple aquí.

</specifics>

<deferred>
## Deferred Ideas

- Demostrar el efecto de la densidad de pilotos en la calidad de estimación LS vs MMSE — eso es Sesión 08, fuera del scope de 8 horas.
- Agregar ejercicio interactivo para el bloque de cierre §4 — pertenece a la sección de Ejercicios y a una revisión editorial más amplia.
- Soft decisions (LLR) en el demapper — §4.8 los menciona correctamente; implementarlos pertenece a Sesión 04.

</deferred>

---

*Phase: 3-Mejora de Narrativa*
*Context gathered: 2026-05-22*
