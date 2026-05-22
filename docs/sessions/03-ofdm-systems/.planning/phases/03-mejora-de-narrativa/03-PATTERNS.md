# Phase 03: Mejora de Narrativa — Pattern Map

**Mapped:** 2026-05-22
**Files analyzed:** 1 (index.md — único archivo modificado)
**Analogs found:** todos los patrones extraídos del propio documento

---

## File Classification

| Archivo modificado | Rol | Data Flow | Analog interno | Match Quality |
|--------------------|-----|-----------|----------------|---------------|
| `index.md` (transiciones §4) | narrative-block | text-insertion | `index.md` líneas 784–785 (transición 4.5→4.6 existente) | exact |
| `index.md` (intro NARR-02) | narrative-intro | text-insertion | `index.md` líneas 22–24 (párrafo existente de Sesiones 01–02) | role-match |
| `index.md` (cross-refs §7) | narrative-synthesis | text-append | `index.md` líneas 1078–1086 (dimensiones existentes sin refs) | exact |
| `index.md` (bloque cierre §4) | narrative-block + code-snippet | text-insertion | `index.md` líneas 574–590 (bloque §4.1 con párrafo + código + verification) | role-match |
| `index.md` (caption Figura 3) | figure-caption | text-replacement | `index.md` líneas 59–62 (Figura 1, caption con 3 paneles) | exact |
| `index.md` (bug WR-01) | markup-fix | text-deletion | `index.md` patrón `---` simple entre subsecciones | exact |

---

## Pattern Assignments

---

### PATRÓN 1: Transición pregunta-respuesta entre bloques §4

**Propósito:** Todas las transiciones ausentes (4.1→4.2, 4.2→4.3, 4.3→4.4, 4.4→4.5, 4.6→4.7, 4.7→4.8, 4.8→§5) deben copiar este patrón.

**Analog canónico:** `index.md` líneas 784–785

**Texto verbatim (reproducir estructura, adaptar contenido):**

```markdown
La pregunta natural es: ¿existe un ecualizador que sea más inteligente en esas
subportadoras? En lugar de invertir el canal ciegamente, ¿podría detectar que una
subportadora está muy atenuada y moderar su respuesta para no amplificar el ruido?
La respuesta es sí, y ese ecualizador es el MMSE.
```

**Reglas de estructura extraídas del template:**
1. Frase 1: "La pregunta natural es: ¿[pregunta sobre el problema que deja pendiente el bloque que cierra]?"
2. Frase 2 (opcional): elaboración de la pregunta o la limitación del bloque actual (reformulación o matiz).
3. Frase final: "La respuesta es [respuesta breve], y [nombre del bloque siguiente que la resuelve]."
4. Longitud: 1–4 oraciones de texto plano corriente (sin admonition, sin negrita, sin bloque de código).
5. Ubicación: inmediatamente antes del `---` separador que cierra el bloque origen.

**Contenido por transición (notas del RESEARCH.md para cada una):**

| Transición | Problema que cierra el bloque origen | Bloque destino |
|------------|--------------------------------------|----------------|
| 4.1→4.2 | `X` contiene N símbolos en frecuencia pero no es aún una señal transmisible en tiempo | §4.2 IFFT+CP convierte frecuencia→tiempo |
| 4.2→4.3 | `x_cp` es banda-base discreta; el canal real la deformará | §4.3 modela esa deformación |
| 4.3→4.4 | `y_noisy` mezcla ecos de símbolos pasados; el CP debe eliminarse y las subportadoras separarse | §4.4 FFT hace eso |
| 4.4→4.5 | `Y[k] = H[k]·X[k] + W[k]`; sin corregir la distorsión el detector recibe una nube dispersa | §4.5 ZF la corrige |
| 4.5→4.6 | **YA EXISTE — NO MODIFICAR** (líneas 784–785) | — |
| 4.6→4.7 | §4.5 y §4.6 calculan `H = np.fft.fft(h_channel, n=N)` asumiendo h_channel conocido (líneas 758 y 809); en la práctica nadie lo da | §4.7 muestra cómo estimarlo con pilotos |
| 4.7→4.8 | `H_est` permite ecualizar y `X_hat` es un número complejo; falta convertirlo en bits | §4.8 demapper hace esa decisión |
| 4.8→§5 | Con el demapper la cadena completa está cerrada; la pregunta es ¿qué tan bien funciona? | §5 BER responde |

---

### PATRÓN 2: Separador de subsección `---`

**Propósito:** Un único `---` entre bloques. Nunca doble.

**Analog:** `index.md` patrón repetido en líneas 591, 635, 669, 696, 786, 827, 905.

**Estructura correcta** (verificada en línea 786 — cierre §4.5, que tiene la transición + `---`):

```markdown
La respuesta es sí, y ese ecualizador es el MMSE.

---

#### 4.6 Ecualizador MMSE
```

**Bug WR-01 (líneas 940–942):** Actualmente hay dos `---` consecutivos:

```
línea 940: ---
línea 941: (línea vacía)
línea 942: ---
```

La corrección elimina la línea 942 (y opcionalmente la 941). El resultado correcto:

```markdown
</figure>

---

### 5. Rendimiento End-to-End
```

---

### PATRÓN 3: Estructura interna de cada bloque §4 (subsección)

**Propósito:** Los bloques de cierre §4 (snippet + nota D-07) deben insertarse respetando el patrón de cada bloque.

**Analog:** `index.md` líneas 593–634 (§4.2 — ejemplo representativo con nota + código + verification)

**Estructura de un bloque §4:**
```markdown
#### 4.X Nombre del bloque

**Entrada:** ... — **Operación:** ... — **Salida:** ...

[Párrafos de explicación conceptual — texto plano o con LaTeX inline]

??? note "Aclaración opcional"
    [contenido colapsable]

```python
def nombre_funcion(args):
    """Docstring de una línea."""
    ...
```

??? example "Verificación"
    ```python
    # código de verificación
    ```

[Párrafo de transición al siguiente bloque — patrón pregunta-respuesta]

---
```

**Observación clave:** La nota D-07 (aviso sobre uncoded OFDM) va como **párrafo plano** antes del snippet, NO como `??? note` colapsable. El patrón más cercano son los párrafos introductorios de líneas 524–538 y los párrafos explicativos de §4.3 (líneas 641–658) — texto corriente sin admonition wrapper.

---

### PATRÓN 4: Figura con caption MkDocs-Material

**Propósito:** El caption de Figura 3 debe reemplazarse manteniendo exactamente esta estructura.

**Analog:** `index.md` líneas 59–62 (Figura 1 — caption multi-panel con descripción de cada panel)

**Patrón de figura simple** (línea 739 — sin caption, solo imagen inline):
```markdown
![Texto descriptivo alt-text](figures/nombre.png)
```

**Patrón de figura con `<figure>` y `<figcaption>`** (líneas 59–62):
```html
<figure markdown="span">
  ![alt text descriptivo](figures/nombre.png)
  <figcaption markdown="1">**Figura N.** Texto del caption con $LaTeX$ inline y *énfasis*.</figcaption>
</figure>
```

**Figura 3 — estructura actual que se reemplaza** (líneas 935–938):
```html
<figure markdown="span">
  ![Constelaciones QAM tras ecualización ZF (izquierda) vs MMSE (derecha)](figures/mmse-vs-zf-constellation.png)
  <figcaption markdown="1">**Figura 3.** Dispersión de la constelación QAM tras ecualización en un canal selectivo
en frecuencia: ZF (izquierda) amplifica ruido en las subportadoras débiles — la nube
se ensancha desproporcionadamente; MMSE (derecha) la contiene mediante regularización
con $1/\text{SNR}$ — los puntos quedan más cerca de los símbolos ideales. La diferencia
se ve más pronunciada a SNR baja, donde el regularizador domina.</figcaption>
</figure>
```

**Alt-text correcto (D-15):** `Factor de contracción α[k] (izquierda), constelación ZF (centro) y MMSE (derecha) en un canal selectivo en frecuencia`

**Caption correcto (D-15):** debe describir los 3 paneles en orden izquierda → centro → derecha:
- Panel izquierdo (`axes[0]`): factor de contracción α[k] — valores ≈ 1 (rojo) canal fuerte, valores ≪ 1 (azul/cian) fades donde MMSE modera amplificación
- Panel central (`axes[1]`): constelación ZF
- Panel derecho (`axes[2]`): constelación MMSE

---

### PATRÓN 5: Bloque de código Python en §4

**Propósito:** El snippet de cadena completa (D-06) debe seguir el estilo de todos los bloques de código de §4.

**Analog:** `index.md` líneas 648–658 (§4.3 — función + código inline posterior, sin wrapper de función separada)

**Estilo de snippet de uso** (no definición de función):
```python
def apply_channel(x_signal, h):
    """Convolución lineal con h: simula el canal multipath."""
    return np.convolve(x_signal, h, mode='full')[:len(x_signal)]

# El ruido se añade por separado, calibrado al Eb/N0 del punto de simulación:
SNR_lin = 10 ** (SNR_dB / 10)
sigma2  = 1 / (2 * k * SNR_lin)          # varianza por componente I o Q
noise   = (rng.normal(0, np.sqrt(sigma2), N + N_CP) +
           1j * rng.normal(0, np.sqrt(sigma2), N + N_CP))
y_noisy = apply_channel(x_cp, h_channel) + noise
```

**Cadena completa — nombres de variable (D-08, verificados vs Cell 24):**

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

**Nota D-07 — ubicación y formato (párrafo plano, NO admonition):**

El texto de aviso sobre uncoded OFDM va como párrafo corriente antes del bloque de código, igual que los párrafos de contexto en §4.3 (líneas 641–642):

```markdown
[párrafo de transición + setup del snippet]

Con todos los bloques en su lugar, la cadena completa puede ejecutarse de principio
a fin. Este snippet es el transceptor OFDM sin codificación de canal — exactamente el
sistema que §5 mide con la curva BER. La codificación LDPC (Sesión 04) se agrega
como una capa superior a esta cadena.

```python
# ...snippet...
```
```

---

### PATRÓN 6: Párrafo de introducción — inserción de frase de brecha

**Propósito:** La frase D-10 se inserta dentro del párrafo de línea 23 sin reescribir el párrafo completo.

**Analog:** `index.md` líneas 22–24 — párrafo existente

**Texto actual del párrafo (línea 23 — verbatim):**

```markdown
Las Sesiones 01 y 02 construyeron los dos pilares del problema de transmisión digital:
el canal inalámbrico y la modulación. La Sesión 01 mostró que los canales de banda
ancha son frequency-selective — distintas frecuencias experimentan ganancias distintas,
y los ecos producen ISI cuando el período de símbolo es menor que el delay spread.
La Sesión 02 mostró que para transmitir $k$ bits por símbolo con M-QAM se necesita un
SNR proporcional a $(M-1)$. Pero hay un problema que no resolvimos: ¿qué ocurre cuando
aplicamos una única portadora M-QAM de alta tasa sobre un canal frequency-selective?
```

**Punto exacto de inserción (D-10):** después del punto que cierra `$(M-1)$.` y antes de `Pero hay un problema que no resolvimos`.

**Frase a insertar (D-10 — formulación de CONTEXT.md):**

```markdown
La Sesión 02 resolvió el canal AWGN plano — un coeficiente escalar de canal que el
receptor puede invertir directamente. Aquí el canal es frequency-selective — no existe
un único coeficiente que corrija todo el espectro.
```

**Resultado esperado del párrafo modificado:**

```markdown
[...] La Sesión 02 mostró que para transmitir $k$ bits por símbolo con M-QAM se
necesita un SNR proporcional a $(M-1)$. La Sesión 02 resolvió el canal AWGN plano —
un coeficiente escalar de canal que el receptor puede invertir directamente. Aquí el
canal es frequency-selective — no existe un único coeficiente que corrija todo el
espectro. Pero hay un problema que no resolvimos: ¿qué ocurre cuando aplicamos una
única portadora M-QAM de alta tasa sobre un canal frequency-selective?
```

---

### PATRÓN 7: Referencias cruzadas §7 Síntesis

**Propósito:** Agregar `(§X)` parenthetical al final de la oración "Implicación de diseño" de cada dimensión.

**Analog:** `index.md` líneas 1078–1086 — texto actual de cada dimensión

**Estructura de cada dimensión (verbatim — Dimensión 1, línea 1078):**

```markdown
**Dimensión 1: Conversión de canal FSF en N canales flat.** OFDM descompone el
problema de ecualización de canal frequency-selective (complejidad $\mathcal{O}(L^2)$)
en N problemas triviales de ganancia escalar (complejidad $\mathcal{O}(N \log N)$
incluyendo la FFT). La condición es $\Delta f \ll B_c$. *Implicación de diseño*: N
debe ser suficientemente grande para que $\Delta f \ll B_c$, pero no tan grande que
el Doppler cause ICI.
```

**Patrón de inserción (D-13 — parenthetical al final, antes del punto):**

```markdown
*Implicación de diseño*: N debe ser suficientemente grande para que $\Delta f \ll B_c$,
pero no tan grande que el Doppler cause ICI (§2 y §4).
```

**Mapa completo de referencias a insertar (D-14):**

| Línea | Dimensión | Fin de oración actual | Referencia a agregar |
|-------|-----------|----------------------|----------------------|
| 1078 | D1 | `...que el Doppler cause ICI.` | `(§2 y §4)` — antes del `.` |
| 1080 | D2 | `...5G NR balancea esto con numerologías.` | `(§3)` — antes del `.` |
| 1082 | D3 | `...maximizar la eficiencia de la FFT radix-2.` | `(§2)` — antes del `.` |
| 1084 | D4 | `...Sesión 08 desarrolla los estimadores LS y MMSE.` | `(§4.5, §4.6, §4.7)` — antes del `.` |
| 1086 | D5 | `...a costa de perder la ecualización de un tap pura.` | `(§7)` — antes del `.` |

**Nota D5:** La referencia `(§7)` apunta a la sección §7 de esta misma sesión (línea 1064: "PAPR: La Penalización de la Amplificación"), no a la Sesión 07 (MIMO masivo). El contexto del documento lo hace claro.

---

## Shared Patterns (patrones transversales)

### Texto plano corriente como vehículo de transiciones

**Fuente:** `index.md` líneas 784–785 (y múltiples párrafos de §4.3, §4.4, §4.5)

**Aplica a:** todas las transiciones §4, la nota D-07, la frase de inserción D-10

Sin admonition wrapper, sin negrita estructural, sin bloque de código. El estudiante no puede colapsar una transición.

### Delimitación `---` como único separador entre subsecciones §4

**Fuente:** `index.md` — patrón repetido en líneas 591, 635, 669, 696, 786, 827, 905

**Aplica a:** bug WR-01 y a la inserción del bloque de cierre §4 (que va antes del único `---` que queda entre §4.8 y §5).

### Comentarios `# §X.Y Nombre` como etiquetas pedagógicas en código

**Fuente:** RESEARCH.md líneas 385–396 (snippet de referencia de Cell 24)

**Aplica a:** snippet de cadena completa D-06 — cada línea del snippet lleva un comentario que identifica la sección

### `markdown="1"` en figcaption para LaTeX inline

**Fuente:** `index.md` líneas 59–62

**Aplica a:** corrección del caption de Figura 3 — sin este atributo el LaTeX no se renderiza dentro del tag HTML

---

## No Analog Found

No aplica en esta fase — todos los patrones necesarios existen ya en el propio `index.md`. No hay ficheros nuevos sin referente.

---

## Metadata

**Scope de búsqueda:** `index.md` completo (1331 líneas), secciones leídas: líneas 1–80, 560–704, 704–943, 943–963, 1060–1096

**Patrones identificados:** 7 patrones primarios + 4 patrones transversales

**Fecha de extracción:** 2026-05-22

**Confianza en números de línea:** MEDIUM para separadores internos §4 (591, 635, 669, 696, 827, 905) — pueden haberse desplazado con ediciones de Fase 2. El agente de ejecución debe verificar contenido contextual alrededor de cada línea antes de editar.
