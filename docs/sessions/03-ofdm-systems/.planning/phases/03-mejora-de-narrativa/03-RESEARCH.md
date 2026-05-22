# Phase 3: Mejora de Narrativa — Research

**Researched:** 2026-05-22
**Domain:** Edición narrativa de documento pedagógico Markdown/MkDocs-Material
**Confidence:** HIGH

---

## Summary

Esta fase trabaja exclusivamente sobre `index.md`. No hay instalación de paquetes, no hay cambios al notebook. El dominio técnico es edición de texto: insertar transiciones, un párrafo de puente, referencias cruzadas, un bloque de código de demostración, corregir un caption de figura, eliminar un separador duplicado. Todas las ubicaciones exactas han sido verificadas leyendo el archivo actual.

La investigación auditó `index.md` línea por línea para los nueve puntos de interés, verificó la estructura real de Cell 18 y Cell 24 en `lab.ipynb`, y confirmó el estado de los 4 PNGs modificados en el working tree.

**Recomendación primaria:** Ejecutar todos los cambios en un orden secuencial de menor a mayor riesgo editorial — bug fix (WR-01) primero, luego correcciones de caption y referencias cruzadas, luego transiciones §4, luego bloque de cierre §4, finalmente el párrafo de introducción. Los PNGs se evalúan visualmente y se commitean en el mismo commit de cierre.

---

<user_constraints>
## User Constraints (from CONTEXT.md)

### Locked Decisions

**Transiciones §4 (NARR-01):**
- D-01: Estilo pregunta-respuesta, igual que la transición 4.5→4.6 ya existente.
- D-02: Ubicación al final del bloque que cierra, inmediatamente antes del `---` separador.
- D-03: Transición 4.6→4.7 articula: ZF y MMSE asumen H[k] conocido; en la práctica nadie nos lo da; el siguiente bloque muestra cómo.
- D-04: Cierre §4.8→§5 articula: con el demapper la cadena completa está cerrada; la pregunta natural es ¿qué tan bien funciona el sistema?; la respuesta es la curva BER de §5.
- D-05: Transiciones 4.1→4.2, 4.2→4.3, 4.3→4.4, 4.4→4.5, 4.7→4.8 delegadas a Claude. La transición 4.5→4.6 ya existe y NO se modifica.

**Bloque de cierre §4 (NARR-01 extensión):**
- D-06: Snippet de cadena completa uncoded OFDM al final de §4 (después de §4.8, antes del `---` final): `bits → qpsk_map → ofdm_tx → apply_channel + noise → ofdm_rx_no_channel → zf_equalizer → qpsk_demap → bits_hat`. ~15 líneas con comentarios de sección.
- D-07: Nota previa al snippet: "Este es el transceptor OFDM sin codificación de canal — la BER de §5 mide exactamente este sistema. La codificación LDPC (Sesión 04) se añade encima de esta cadena."
- D-08: Nombres de variable: `X` (§4.1), `x_cp` (§4.2), `y_noisy` (§4.3), `Y` (§4.4), `X_hat` (§4.5/§4.6), `bits_hat` (§4.8). Verificar con Cell 24.

**Bug WR-01:**
- D-09: Eliminar el `---` duplicado entre §4.8 y §5. Ubicación: líneas 940–942 (dos `---` consecutivos).

**Introducción (NARR-02):**
- D-10: Agregar brecha explícita: "La Sesión 02 resolvió el canal AWGN plano — un coeficiente escalar de canal que el receptor puede invertir directamente. Aquí el canal es frequency-selective — no existe un único coeficiente que corrija todo el espectro."
- D-11: No agregar párrafo de preview de secciones. La última frase ya sirve.
- D-12: Intervención mínima — solo el parche del trade-off explícito.

**Referencias cruzadas §7 Síntesis (NARR-03):**
- D-13: Formato parenthetical al final de la línea "Implicación de diseño": `(§X)` o `como se desarrolla en §X.`
- D-14: Mapa de referencias: D1→(§2 y §4), D2→(§3), D3→(§2), D4→(§4.5, §4.6, §4.7), D5→(§7).

**Figura 3 — corrección caption:**
- D-15: El caption actual menciona 2 paneles (ZF izquierda, MMSE derecha) pero la figura tiene 3 paneles. Paneles: izquierda = factor α[k]; centro = constelación ZF; derecha = constelación MMSE.

**4 PNGs modificados:**
- D-16: Inspeccionar visualmente antes de commitear. Si son mejoras, commitear con `fig(03): commit re-generated figures with turbo colormap`. Revertir individualmente los que no mejoren.

### Claude's Discretion
- Redacción exacta de las transiciones (siguiendo patrón pregunta-respuesta).
- Longitud de cada transición (1–4 oraciones).
- Ubicación exacta del bloque de cierre §4 dentro de §4.8 (antes o después de la figura, siempre antes del `---`).

### Deferred Ideas (OUT OF SCOPE)
- Demostrar el efecto de la densidad de pilotos en LS vs MMSE (Sesión 08).
- Agregar ejercicio interactivo para el bloque de cierre §4.
- Soft decisions (LLR) en el demapper.
</user_constraints>

---

<phase_requirements>
## Phase Requirements

| ID | Description | Research Support |
|----|-------------|------------------|
| NARR-01 | Fortalecer hilo conductor §4 (bloques 4.1–4.8): cada bloque motiva al siguiente con frase de transición | Transiciones 4.1→…→4.8: ubicaciones exactas verificadas; transición template (4.5→4.6) transcrita; cadena Cell 24 verificada para snippet de cierre |
| NARR-02 | Mejorar Introducción: progresión Sesiones 01–02 → OFDM sin saltos lógicos | Párrafo de inserción identificado (línea 23); frase de destino verificada (línea 68) |
| NARR-03 | Integrar §7 Síntesis con referencias cruzadas hacia secciones de desarrollo | Cinco dimensiones verificadas en líneas 1078–1086; mapa D-14 verificado contra estructura real del documento |
</phase_requirements>

---

## Architectural Responsibility Map

| Capability | Primary Tier | Secondary Tier | Rationale |
|------------|-------------|----------------|-----------|
| Edición de texto / narrativa | Documento (index.md) | — | Fase de solo edición de texto; no hay capa de app ni backend |
| Ground truth de código | Notebook (lab.ipynb) | — | Lee pero no modifica |
| Assets visuales (PNGs) | Working tree / git | — | Decisión de commit basada en inspección visual |

---

## Estado Actual Verificado: Sección por Sección

### WR-01: Bug del doble `---` [VERIFIED: lectura directa de index.md]

- **Línea 940:** `---` (primer separador — cierra §4.8)
- **Línea 941:** línea vacía
- **Línea 942:** `---` (segundo separador — duplicado)
- **Línea 944:** `### 5. Rendimiento End-to-End`

**Corrección D-09:** Eliminar las líneas 942 y 941 (o bien solo la línea 942 y dejar la 941 como separación visual). El resultado correcto es un único `---` entre §4 y §5.

---

### NARR-02: Introducción — Gap a rellenar [VERIFIED: lectura directa de index.md]

**Párrafo donde vive la frase incompleta (línea 23):**

```
Las Sesiones 01 y 02 construyeron los dos pilares del problema de transmisión digital:
el canal inalámbrico y la modulación. La Sesión 01 mostró que los canales de banda
ancha son frequency-selective — distintas frecuencias experimentan ganancias distintas,
y los ecos producen ISI cuando el período de símbolo es menor que el delay spread.
La Sesión 02 mostró que para transmitir k bits por símbolo con M-QAM se necesita un
SNR proporcional a (M-1). Pero hay un problema que no resolvimos: ¿qué ocurre cuando
aplicamos una única portadora M-QAM de alta tasa sobre un canal frequency-selective?
```

**Gap identificado:** La frase "Pero hay un problema que no resolvimos" salta directamente a la pregunta sin explicar QUÉ asumió la Sesión 02 que ya no vale aquí. No dice que la Sesión 02 asumió canal AWGN plano (un solo coeficiente escalar), ni que ese supuesto no se cumple cuando el canal es frequency-selective.

**Última frase de la Introducción (línea 68):**
```
Esta sesión construye esa cadena completa: símbolos QAM → IFFT → CP → canal → FFT
→ ecualización de un tap.
```
Esta frase ya funciona como preview (D-11: no agregar otro párrafo de preview).

**Inserción D-10:** El puente debe insertarse al final del párrafo de línea 23, inmediatamente antes de "Pero hay un problema que no resolvimos" o justo después de la frase sobre Sesión 02 y M-QAM. Opción más limpia: insertar una frase entre "SNR proporcional a $(M-1)$." y "Pero hay un problema…" que diga explícitamente que la Sesión 02 asumió canal AWGN plano.

**Ubicación exacta de inserción:** Después del punto al final de la frase que termina en `$(M-1)$.` y antes de `Pero hay un problema que no resolvimos`.

---

### NARR-01: Transiciones §4 — Estado actual [VERIFIED: lectura directa de index.md]

#### Transición 4.5→4.6 (EXISTENTE — NO modificar)

**Ubicación:** Líneas 779–784, al final de §4.5, antes del `---` en línea 786.

**Texto exacto (verbatim):**
```
La pregunta natural es: ¿existe un ecualizador que sea más inteligente en esas
subportadoras? En lugar de invertir el canal ciegamente, ¿podría detectar que una
subportadora está muy atenuada y moderar su respuesta para no amplificar el ruido?
La respuesta es sí, y ese ecualizador es el MMSE.
```

Este es el template canónico para todas las transiciones nuevas.

#### Transiciones AUSENTES — Ubicaciones de inserción

| Transición | Insertar ANTES de | Línea de referencia | Último párrafo del bloque origen |
|------------|-------------------|---------------------|----------------------------------|
| 4.1→4.2 | `---` que cierra §4.1 | línea 591 | Verification block de `qpsk_map` termina línea 590 |
| 4.2→4.3 | `---` que cierra §4.2 | línea 635 | Verification block de `ofdm_tx` termina línea 634 |
| 4.3→4.4 | `---` que cierra §4.3 | línea 669 | Verification block de `apply_channel` termina línea 668 |
| 4.4→4.5 | `---` que cierra §4.4 | línea 696 | Verification block de `ofdm_rx_no_channel` termina línea 695 |
| 4.6→4.7 | `---` que cierra §4.6 | línea 827 | Último párrafo sobre FEC termina línea 826 |
| 4.7→4.8 | `---` que cierra §4.7 | línea 905 | Verification block de `ls_channel_estimate` termina línea 904 |
| 4.8→§5 | `---` del bug WR-01 (línea 940) | línea 940 | `</figure>` de Figura 3 termina línea 938 |

**Nota sobre 4.6→4.7 (D-03):** El gap explícito es que §4.5 y §4.6 ambos calculan `H = np.fft.fft(h_channel, n=N)` internamente — asumiendo que `h_channel` es conocido por el ecualizador. Línea 758 (`zf_equalizer`) y línea 809 (`mmse_equalizer`) tienen esa línea. La transición debe hacer visible ese supuesto implícito.

**Nota sobre 4.1→4.2 (D-05):** El problema que §4.1 deja pendiente es que el mapper produce `N` símbolos en frecuencia, pero esos números complejos no son aún una señal transmisible — necesitan convertirse en muestras de tiempo. El bloque siguiente (§4.2 IFFT) resuelve eso.

**Nota sobre 4.2→4.3 (D-05):** El problema que §4.2 deja pendiente es que `x_cp` ya es una señal en tiempo, pero sigue siendo discreta y banda-base — el canal real deformará esa señal. El bloque siguiente (§4.3) modela exactamente esa deformación.

**Nota sobre 4.3→4.4 (D-05):** El problema que §4.3 deja pendiente es que `y_noisy` lleva mezclados ecos de símbolos pasados y el CP ya no sirve a nada — hay que limpiarlo y separar las subportadoras para que el ecualizador pueda actuar. El bloque siguiente (§4.4 FFT) hace eso.

**Nota sobre 4.4→4.5 (D-05):** El problema que §4.4 deja pendiente es que `Y[k] = H[k]·X[k] + W[k]` — el canal distorsionó cada subportadora de forma independiente, y sin corregirla el detector recibirá una nube dispersa en lugar de la constelación original. El bloque siguiente (§4.5 ZF) corrige esa distorsión.

**Nota sobre 4.7→4.8 (D-05):** El problema que §4.7 deja pendiente es que `H_est` ya permite ecualizar, pero `X_hat` sigue siendo un número complejo en el plano — hay que convertirlo en bits. El bloque siguiente (§4.8 demapper) hace esa decisión.

---

### NARR-01 Extensión: Bloque de cierre §4 [VERIFIED: Cell 24 de lab.ipynb]

#### Cadena completa de Cell 24 (`ofdm_ber_quick`)

```python
# Cadena de referencia del notebook (Cell 24 / a602f4ca):
bits   = rng.integers(0, 2, N * k_bits)
X      = qpsk_map(bits)                          # §4.1
x_cp_  = ofdm_tx(X, N_CP)                        # §4.2
y_     = apply_channel(x_cp_, h)[:N + N_CP]      # §4.3
y_    += sigma * (rng.normal(size=N+N_CP) + 1j*rng.normal(size=N+N_CP))  # ruido
Y_     = ofdm_rx_no_channel(y_, N, N_CP)         # §4.4
X_hat  = zf_equalizer(Y_, h, N)                  # §4.5 (o mmse_equalizer para §4.6)
# qpsk_demap(X_hat) → bits_hat                   # §4.8
```

**Nombres de variables para D-08:** Según Cell 24, los nombres estándar son:
- `bits` (entrada)
- `X` = salida de `qpsk_map` (§4.1)
- `x_cp` = salida de `ofdm_tx` (§4.2) — Cell 24 usa `x_cp_` por ser función local; el snippet de index.md puede usar `x_cp` directamente
- `y_noisy` = salida de `apply_channel` + ruido (§4.3) — Cell 24 fusiona los dos pasos con `y_` y adición inline; el snippet de index.md puede separarlo en dos líneas para claridad pedagógica
- `Y` = salida de `ofdm_rx_no_channel` (§4.4)
- `X_hat` = salida de `zf_equalizer` (§4.5/§4.6)
- `bits_hat` = salida de `qpsk_demap` (§4.8) — Cell 24 no almacena esto en una variable separada; el snippet de index.md sí debe hacerlo

**Firma de `qpsk_demap` (Cell 22 / `2fd4f44b`):**
```python
def qpsk_demap(X_hat):
    """Hard decision QPSK con Gray coding: Re<0 → b0=1, Im<0 → b1=1."""
    bits = np.zeros(len(X_hat) * 2, dtype=int)
    bits[0::2] = (X_hat.real < 0).astype(int)
    bits[1::2] = (X_hat.imag < 0).astype(int)
    return bits
```
La función existe como callable en el notebook (Cell 22). El index.md aún no la documenta como función completa — el snippet de cierre la usará directamente.

**Ubicación del bloque de cierre:** Después de `</figure>` de Figura 3 (línea 938) y antes del primer `---` del bug WR-01 (línea 940). El bug WR-01 se corrige a la vez dejando un único `---`.

---

### NARR-03: §7 Síntesis — Estado actual [VERIFIED: lectura directa de index.md]

**Líneas exactas de cada dimensión:**

| Dimensión | Línea | Texto de "Implicación de diseño" actual | Referencia D-14 a agregar |
|-----------|-------|----------------------------------------|---------------------------|
| D1 | 1078 | "…N debe ser suficientemente grande para que $\Delta f \ll B_c$, pero no tan grande que el Doppler cause ICI." | `(§2 y §4)` |
| D2 | 1080 | "…CP más largo protege frente a mayor delay spread pero reduce la eficiencia espectral. 5G NR balancea esto con numerologías." | `(§3)` |
| D3 | 1082 | "…N se elige potencia de 2 para maximizar la eficiencia de la FFT radix-2." | `(§2)` |
| D4 | 1084 | "…la densidad de pilotos es el trade-off entre exactitud de estimación y eficiencia espectral. Sesión 08 desarrolla los estimadores LS y MMSE." | `(§4.5, §4.6, §4.7)` |
| D5 | 1086 | "…PAPR es especialmente crítico en el uplink (terminal móvil con batería limitada). 5G NR usa DFT-spread OFDM (SC-FDMA) en el uplink para reducir el PAPR, a costa de perder la ecualización de un tap pura." | `(§7)` |

**Formato D-13:** Agregar la referencia parenthetical al final de la oración de "Implicación de diseño", antes del punto final. Por ejemplo, la D1 quedaría:
```
*Implicación de diseño*: N debe ser suficientemente grande para que $\Delta f \ll B_c$,
pero no tan grande que el Doppler cause ICI (§2 y §4).
```

**Observación sobre D5:** La referencia `(§7)` se refiere a la sección §7 de esta misma sesión (PAPR: La Penalización de la Amplificación, línea 1064). Es una auto-referencia válida — la dimensión 5 de la Síntesis apunta al desarrollo de §7 que está algunas líneas más arriba en el mismo documento.

---

### Figura 3 — Caption actual vs correcto [VERIFIED: lectura directa + Cell 18]

**Caption actual (líneas 936–937):**
```
Constelaciones QAM tras ecualización ZF (izquierda) vs MMSE (derecha)
```
(texto del alt-text, línea 936)

```
**Figura 3.** Dispersión de la constelación QAM tras ecualización en un canal selectivo
en frecuencia: ZF (izquierda) amplifica ruido en las subportadoras débiles — la nube
se ensancha desproporcionadamente; MMSE (derecha) la contiene mediante regularización
con $1/\text{SNR}$ — los puntos quedan más cerca de los símbolos ideales. La diferencia
se ve más pronunciada a SNR baja, donde el regularizador domina.
```
(figcaption, línea 937)

**Problema (D-15):** El caption menciona 2 paneles (ZF izquierda, MMSE derecha). La figura real tiene 3 paneles (`plt.subplots(1, 3)` en Cell 18):
- Panel izquierdo (`axes[0]`): Factor de contracción MMSE α[k] por subportadora (barras verticales)
- Panel central (`axes[1]`): Constelación ZF (`scatter_zf`)
- Panel derecho (`axes[2]`): Constelación MMSE (`scatter_zf`)

**Context adicional para el caption correcto (de la nota en Cell 18):**
- El título del panel izquierdo es "Factor de contracción MMSE α[k]\n(azul/cian = MMSE frena fuerte, rojo ≈ ZF)"
- El código de color turbo: azul/cian = subportadora débil, rojo = fuerte
- α[k] cerca de 1 indica canal fuerte (MMSE ≈ ZF); α[k] cerca de 0 indica fade donde el MMSE modera la amplificación

**Alt-text correcto:** "Factor de contracción α[k] (izquierda), constelación ZF (centro) y MMSE (derecha) en un canal selectivo en frecuencia"

---

### 4 PNGs modificados en working tree [VERIFIED: git diff --stat]

| Archivo | Tamaño antes | Tamaño después | Variación |
|---------|-------------|----------------|-----------|
| `cp-illustration.png` | 124 690 B | 123 047 B | −1 643 B (−1.3%) |
| `ofdm-subcarriers.png` | 386 283 B | 321 860 B | −64 423 B (−16.7%) |
| `zf-equalizer-effect.png` | 143 336 B | 145 468 B | +2 132 B (+1.5%) |
| `zf-equalizer-qam-comparison.png` | 426 252 B | 427 476 B | +1 224 B (+0.3%) |

Los cambios de tamaño son consistentes con una re-generación: `ofdm-subcarriers.png` se redujo significativamente (colormap turbo puede ser más eficiente para datos continuos), mientras que `zf-equalizer-effect.png` y `zf-equalizer-qam-comparison.png` crecieron ligeramente (posiblemente más detalle en el scatter plot). El tamaño del archivo no es indicador definitivo de calidad visual — la evaluación final es visual.

**Protocolo de inspección (D-16):** El agente de ejecución abre cada PNG y juzga:
1. ¿El contraste entre subportadoras fuertes/débiles es más claro con turbo que con el colormap anterior?
2. ¿Los ejes, labels y títulos son legibles?
3. ¿El fondo blanco está presente (`facecolor='white'` en el savefig)?

Si todos responden sí → commitear. Si alguno falla → `git checkout figures/<nombre>.png` para ese archivo específico.

---

## Patrones MkDocs-Material Relevantes [VERIFIED: lectura directa de index.md]

### Figuras con caption
```html
<figure markdown="span">
  ![alt text descriptivo](figures/nombre.png)
  <figcaption markdown="1">**Figura N.** Texto del caption con $LaTeX$ inline.</figcaption>
</figure>
```

### Separadores de sección
```
---
```
Un solo `---`, nunca doble. Los separadores van entre subsecciones de §4.

### Admonitions usadas en el documento
- `??? note "Título"` — plegable, para derivaciones y aclaraciones
- `??? example "Solución (x)"` — plegable, para soluciones de ejercicios
- `!!! warning "Título"` — no aparece en §4; no se usa en las inserciones de esta fase

### Párrafo de texto corriente
Las transiciones son párrafos de texto plano (sin admonition, sin bloque de código). El template existente lo confirma (líneas 779–784 de §4.5): texto plano corriente.

### Bloques de código Python
```python
```python
def funcion(args):
    """Docstring de una línea."""
    ...
```

### Notas previas al snippet (D-07)
Las notas breves sin colapsar se escriben como párrafo plano en negrita o como texto corriente. El estilo más cercano en el documento es el patrón de párrafo introductorio que precede a cada bloque de código (ej. líneas 524–538). Para D-07 se recomienda párrafo plano (no admonition) para que el estudiante no pueda colapsarlo.

---

## Resumen de Ediciones por Tarea

| Tarea | Tipo | Ubicación (línea) | Riesgo |
|-------|------|-------------------|--------|
| Bug WR-01 | Eliminar `---` duplicado | 941–942 | Bajo — operación de borrado |
| Figura 3 caption | Reemplazar caption (2→3 paneles) | 936–937 | Bajo — texto delimitado |
| §7 D1 cross-ref | Insertar `(§2 y §4)` | fin de línea 1078 | Bajo |
| §7 D2 cross-ref | Insertar `(§3)` | fin de línea 1080 | Bajo |
| §7 D3 cross-ref | Insertar `(§2)` | fin de línea 1082 | Bajo |
| §7 D4 cross-ref | Insertar `(§4.5, §4.6, §4.7)` | fin de línea 1084 | Bajo |
| §7 D5 cross-ref | Insertar `(§7)` | fin de línea 1086 | Bajo |
| Transición 4.1→4.2 | Insertar párrafo | antes de `---` ~línea 591 | Medio |
| Transición 4.2→4.3 | Insertar párrafo | antes de `---` ~línea 635 | Medio |
| Transición 4.3→4.4 | Insertar párrafo | antes de `---` ~línea 669 | Medio |
| Transición 4.4→4.5 | Insertar párrafo | antes de `---` ~línea 696 | Medio |
| Transición 4.6→4.7 | Insertar párrafo | antes de `---` ~línea 827 | Medio |
| Transición 4.7→4.8 | Insertar párrafo | antes de `---` ~línea 905 | Medio |
| Transición 4.8→§5 | Insertar párrafo + snippet | antes del único `---` restante | Medio-Alto |
| Introducción NARR-02 | Insertar frase de brecha | dentro del párrafo línea 23 | Bajo |
| PNGs commit/revert | Decisión visual + git | working tree | Bajo |

---

## Common Pitfalls

### Pitfall 1: Modificar la transición 4.5→4.6 existente
**Qué sale mal:** Si se edita el bloque entre líneas 779–784 creyendo que es una transición a "agregar", se borra la única transición existente.
**Cómo evitar:** Verificar que el texto canónico esté intacto antes de hacer cualquier edición en §4.5.

### Pitfall 2: Insertar la nota D-07 dentro de una admonition colapsable
**Qué sale mal:** Si se usa `??? note "..."`, el estudiante puede colapsar la nota y no ver la advertencia sobre FEC.
**Cómo evitar:** La nota D-07 va como párrafo plano antes del snippet, igual que los párrafos introductorios del resto de §4.

### Pitfall 3: Dejar el doble `---` al insertar el bloque de cierre §4
**Qué sale mal:** Si se inserta texto entre líneas 938 y 940 sin eliminar el `---` duplicado, quedan tres `---` (el de §4.8, el nuevo del bloque de cierre, y el inicial de §5).
**Cómo evitar:** El bloque de cierre §4 reemplaza el espacio entre la Figura 3 y el separador; el bug WR-01 se corrige en el mismo paso.

### Pitfall 4: Usar nombres de variables inconsistentes en el snippet de cierre
**Qué sale mal:** Si el snippet usa `x_cp_` en lugar de `x_cp`, o `y_` en lugar de `y_noisy`, el estudiante no puede cruzar el snippet con los bloques individuales de §4.1–§4.8.
**Cómo evitar:** Usar estrictamente los nombres de D-08: `X`, `x_cp`, `y_noisy`, `Y`, `X_hat`, `bits_hat`.

### Pitfall 5: Caption de Figura 3 que describe solo ZF vs MMSE sin mencionar α[k]
**Qué sale mal:** El panel izquierdo (α[k]) queda sin explicación, y el estudiante no sabe qué mira.
**Cómo evitar:** El caption debe describir los tres paneles en orden izquierda → centro → derecha.

### Pitfall 6: Referencia cruzada §7 D5 que apunta a una sesión externa
**Qué sale mal:** La referencia `(§7)` podría confundirse con la Sesión 07 (MIMO masivo).
**Cómo evitar:** Usar `(ver §7 arriba)` o simplemente `(§7)` — en el contexto del documento es claro que §7 se refiere a la sección PAPR de esta misma sesión.

---

## Code Examples

### Template de transición (patrón canónico — §4.5, líneas 779–784)

```markdown
La pregunta natural es: ¿existe un ecualizador que sea más inteligente en esas
subportadoras? En lugar de invertir el canal ciegamente, ¿podría detectar que una
subportadora está muy atenuada y moderar su respuesta para no amplificar el ruido?
La respuesta es sí, y ese ecualizador es el MMSE.
```

### Snippet de cadena completa §4 (para D-06 + D-07 + D-08)

```python
# Transceptor OFDM uncoded — exactamente lo que §5 mide con la curva BER
bits    = rng.integers(0, 2, N * 2)              # bits aleatorios
X       = qpsk_map(bits)                          # §4.1  mapper
x_cp    = ofdm_tx(X, N_CP)                        # §4.2  IFFT + CP
y_noisy = apply_channel(x_cp, h_channel) + noise  # §4.3  canal + AWGN
Y       = ofdm_rx_no_channel(y_noisy, N, N_CP)    # §4.4  eliminar CP + FFT
X_hat   = zf_equalizer(Y, h_channel, N)           # §4.5  ecualizador ZF
bits_hat = qpsk_demap(X_hat)                      # §4.8  demapper
ber = np.mean(bits != bits_hat)
```

### Inserción NARR-02 (brecha explícita)

El párrafo de línea 23 contiene la frase:
```
La Sesión 02 mostró que para transmitir $k$ bits por símbolo con M-QAM se necesita
un SNR proporcional a $(M-1)$.
```
La frase de inserción D-10 va inmediatamente después de ese punto:
```
La Sesión 02 asumió implícitamente un canal AWGN plano: un único coeficiente escalar
que el receptor puede invertir con una sola división.
```
O en la formulación más precisa de D-10:
```
La Sesión 02 resolvió el canal AWGN plano — un coeficiente escalar de canal que el
receptor puede invertir directamente.
```
Continuando con la frase ya existente: "Aquí el canal es frequency-selective — no existe un único coeficiente que corrija todo el espectro." — que se inserta antes de "Pero hay un problema que no resolvimos".

### Caption correcto de Figura 3 (D-15)

```markdown
<figure markdown="span">
  ![Factor de contracción α[k] (izquierda), constelación ZF (centro) y MMSE (derecha) en un canal selectivo en frecuencia](figures/mmse-vs-zf-constellation.png)
  <figcaption markdown="1">**Figura 3.** Tres paneles del ecualizador MMSE en un canal selectivo en frecuencia. **Izquierda:** factor de contracción $\alpha[k] \in (0,1)$ por subportadora — valores $\approx 1$ (rojo) indican canal fuerte donde MMSE $\approx$ ZF; valores $\ll 1$ (azul/cian) indican *fades* donde el MMSE modera la amplificación. **Centro:** constelación tras ecualizador ZF — los puntos azules/cian muestran ruido amplificado en las subportadoras débiles. **Derecha:** constelación tras ecualizador MMSE — la contracción $\alpha[k]$ compacta la nube en las subportadoras débiles a costa de un pequeño sesgo.</figcaption>
</figure>
```

---

## Package Legitimacy Audit

No aplica — esta fase no instala paquetes externos.

---

## Environment Availability

Esta fase es edición de texto pura sobre `index.md`. No hay dependencias externas de herramientas. El único "entorno" relevante es git para el commit de los PNGs.

| Dependency | Required By | Available | Version | Fallback |
|------------|------------|-----------|---------|----------|
| git | Commit PNGs (D-16) | ✓ | verificado (repo activo) | — |
| Python + matplotlib | Inspección visual de PNGs (opcional) | ✓ | sistema | Abrir PNG con visor nativo |

---

## Validation Architecture

No se generan tests automatizados para edición narrativa. La validación es:

1. **Structural:** `grep -n "^---$" index.md` — no debe mostrar dos `---` consecutivos en el rango de §4.8 a §5.
2. **Reference integrity:** Todas las referencias a figuras en el documento siguen existiendo en `figures/`.
3. **MkDocs build:** `mkdocs build --strict` (si disponible) — no debe emitir warnings sobre syntax de admonitions o figuras rotas.
4. **Visual spot-check:** Leer las transiciones insertadas en contexto para verificar que el patrón pregunta-respuesta fluye naturalmente.

---

## Assumptions Log

| # | Claim | Section | Risk if Wrong |
|---|-------|---------|---------------|
| A1 | Los números de línea citados (591, 635, 669, 696, 827, 905) corresponden a los `---` separadores de cada subsección de §4 | Transiciones §4 | Si el archivo fue editado en Fase 2 y las líneas se desplazaron, las inserciones irán al lugar equivocado. Mitigation: el agente de ejecución debe verificar el contenido del entorno alrededor de cada número de línea antes de editar. |

**Nota:** Los números de línea de las ediciones de Fase 2 pueden haber desplazado ligeramente las líneas de §4. Las líneas críticas verificadas directamente (bug WR-01 en 940–942; Figura 3 en 935–938; §7 en 1078–1086) se verificaron en la sesión actual y tienen alta confianza. Los separadores `---` dentro de §4 (591, 635, 669, 696, 827, 905) son aproximados — el agente de ejecución debe buscarlos por contexto de contenido, no solo por número de línea.

---

## Sources

### Primary (HIGH confidence)
- `index.md` leído directamente — estructura actual, líneas exactas, texto verbatim de todas las secciones relevantes
- `lab.ipynb` leído directamente — Cell 18 (`plt.subplots(1, 3)`) confirma 3 paneles; Cell 24 (`ofdm_ber_quick`) confirma cadena completa y nombres de variables; Cell 22 (`qpsk_demap`) confirma firma de función
- `03-CONTEXT.md` — 16 decisiones bloqueadas (D-01 a D-16)

### Secondary (MEDIUM confidence)
- `01-AUDIT-FINDINGS.md` — corrobora ubicación del bug WR-01 (líneas 940–942)
- `02-CONTEXT.md` — confirma patrones MkDocs establecidos en Fase 2

---

## Metadata

**Confidence breakdown:**
- Ubicaciones exactas de edición: HIGH — verificado leyendo index.md línea por línea
- Estructura de Cell 18 (3 paneles): HIGH — verificado en lab.ipynb
- Cadena Cell 24 (nombres de variable): HIGH — código fuente leído directamente
- Números de línea de separadores §4 internos: MEDIUM — aproximados, necesitan re-verificación antes de editar

**Research date:** 2026-05-22
**Valid until:** Esta sesión — el documento index.md puede cambiar
