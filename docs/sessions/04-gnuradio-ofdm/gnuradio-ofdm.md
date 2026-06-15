---
title: "Lab — OFDM con GNU Radio"
description: "Construcción visual de la cadena OFDM completa: TX, canal AWGN y multipath, RX con ecualización, y medición de BER en tiempo real."
---

# Lab — Estudiando OFDM con GNU Radio

- [Vídeo](https://youtu.be/SWQYXDt1svw?si=1wB68uDhIBoqPfg2)

GNU Radio Companion (GRC) permite construir sistemas de procesamiento de señal como **flowgraphs** visuales: cada etapa de la cadena es un bloque, las conexiones son los flujos de datos, y la ejecución corre en tiempo real. En este laboratorio construiremos la cadena OFDM completa y observaremos en vivo el efecto del canal, el prefijo cíclico y el ruido sobre la constelación recibida.

---

## 1. Instalación

### Windows

GNU Radio en Windows se instala a través de **radioconda**, un entorno conda que incluye GNU Radio y todos sus componentes Qt GUI.

1. Ve a [https://github.com/radioconda/radioconda-installer](https://github.com/radioconda/radioconda-installer) y descarga el instalador bajo **OS: Windows — x86_64 (amd64)**.
2. Ejecuta el `.exe` y acepta los valores por defecto.
3. Abre **Radioconda Prompt** desde el menú Inicio.
4. Verifica la instalación:

```bash
gnuradio-companion --version
```

5. Lanza GRC:

```bash
gnuradio-companion
```

??? note "Alternativa: WSL2"
    Si prefieres Linux nativo en Windows, instala WSL2 con Ubuntu y ejecuta:
    ```bash
    sudo apt update && sudo apt install gnuradio
    ```
    Para usar la GUI desde WSL2 necesitas un servidor X (VcXsrv o WSLg en Windows 11).

### Linux (Ubuntu / Debian)

```bash
sudo apt update && sudo apt install gnuradio
gnuradio-companion
```

---

## 2. El Flowgraph OFDM

El sistema que construiremos implementa la cadena completa de un símbolo OFDM: desde bits aleatorios hasta la constelación decodificada, con visualización en cada etapa.

```
[Fuente bits] → [Pack] → [QPSK] → [S→V] → [IFFT] → [+CP]
                                                         ↓
                                                     [Canal]
                                                         ↓
                          [Const RX] ← [×1] ← [FFT] ← [−CP]
```

### Parámetros globales

Antes de colocar bloques, define estas variables (bloque **Variable**):

| ID | Valor | Significado |
|----|-------|-------------|
| `samp_rate` | `100000` | Tasa de bits de la fuente — controla la velocidad de simulación |
| `fft_size` | `8` | N = número de subportadoras OFDM |
| `cp_len` | `2` | Longitud del prefijo cíclico (N/4) |

Y un control deslizante (bloque **QT GUI Range**):

| ID | Start | Stop | Step | Default |
|----|-------|------|------|---------|
| `noise_amp` | `0.0` | `2.0` | `0.01` | `0.1` |

Finalmente, añade el bloque **`Constellation Object`** para elegir la modulación:

| Parámetro | Valor |
|-----------|-------|
| **ID** | `mod_const` |
| **Constellation Type** | Elige entre: `QPSK`, `16QAM`, `64QAM`, `8PSK` |

Este bloque centraliza la modulación — cambiando solo este parámetro el TX y RX se adaptan automáticamente.

!!! warning "Ajusta K según la modulación elegida"
    El parámetro **K** de `Pack K Bits` y `Unpack K Bits` debe coincidir:

    | Constellation Type | K (bits/símbolo) |
    |--------------------|-----------------|
    | QPSK | `2` |
    | 8PSK | `3` |
    | 16QAM | `4` |
    | 64QAM | `6` |

---

## 3. Transmisor (TX)

### Bloque 1 — Random Uniform Source

**Búscalo como:** `Random Uniform Source`

| Parámetro | Valor | Por qué |
|-----------|-------|---------|
| Type | `Byte` | Genera bytes, usaremos valores 0 ó 1 como bits |
| Minimum | `0` | Bit mínimo |
| Maximum | `2` | Genera {0, 1} — rango [min, max) |

Produce un flujo continuo de bits aleatorios uniformes.

### Bloque 2 — Throttle

**Búscalo como:** `Throttle`

| Parámetro | Valor | Por qué |
|-----------|-------|---------|
| Type | `Byte` | Mismo tipo que la fuente |
| Sample Rate | `samp_rate` | Limita la CPU para que la GUI sea fluida |

Sin este bloque el flowgraph consume el 100% de CPU generando muestras tan rápido como puede.

### Bloque 3 — Pack K Bits

**Búscalo como:** `Pack K Bits`

| Parámetro | Valor | Por qué |
|-----------|-------|---------|
| K | `2` (QPSK) | Agrupa K bits → 1 índice de símbolo (ver tabla de modulaciones arriba) |

Convierte el flujo de bits individuales en índices de símbolo. K debe coincidir con la modulación elegida en `mod_const`.

### Bloque 4 — Chunks to Symbols

**Búscalo como:** `Chunks to Symbols`

| Parámetro | Valor | Por qué |
|-----------|-------|---------|
| Input Type | `Byte` | Recibe índices 0–3 |
| Output Type | `Complex` | Produce puntos complejos I+jQ |
| Symbol Table | `mod_const.points()` | Puntos de la constelación elegida en `mod_const` |
| Dimensionality | `1` | Un símbolo complejo por índice de entrada |

Mapea cada índice de símbolo a su punto en el plano complejo. Aquí cada byte vale un punto QPSK — esto es la modulación.

!!! tip "GUI ① — Constelación TX"
    Conecta un **QT GUI Constellation Sink** a la salida de este bloque. Verás los puntos de la constelación elegida perfectos antes de entrar al canal.

### Bloque 5 — Stream to Vector

**Búscalo como:** `Stream to Vector`

| Parámetro | Valor | Por qué |
|-----------|-------|---------|
| Item Size | `Complex` | Recibe símbolos complejos |
| Num Items | `fft_size` | Agrupa N=8 símbolos en un vector |

La IFFT necesita recibir todos los N símbolos del dominio de la frecuencia juntos para producir un símbolo OFDM en tiempo. Este bloque forma ese paquete de N símbolos: $\mathbf{X} = [X_0, X_1, \ldots, X_{N-1}]$.

### Bloque 6 — FFT (IFFT)

**Búscalo como:** `FFT`

| Parámetro | Valor | Por qué |
|-----------|-------|---------|
| FFT Size | `fft_size` | Tamaño N de la IFFT |
| Forward/Reverse | `Reverse` | Reverse = IFFT: convierte X[k] → x[n] |
| Window | `Rectangular` | Sin ventana — la OFDM no ventanea el IFFT |
| Shift | `No` | Sin fftshift — subportadora 0 en índice 0 |

Implementa $x[n] = \frac{1}{N}\sum_{k=0}^{N-1} X[k]\, e^{+j2\pi kn/N}$. Cada muestra de salida es la suma de N subportadoras ortogonales.

??? note "¿Por qué Rectangular y no Blackman-Harris?"
    La ventana se usa para reducir *spectral leakage* al **analizar** señales. Aquí estamos **generando** la señal OFDM — aplicar una ventana al IFFT distorsionaría la ortogonalidad entre subportadoras, que es la propiedad fundamental que hace funcionar OFDM.

### Bloque 7 — OFDM Cyclic Prefixer

**Búscalo como:** `OFDM Cyclic Prefixer`

| Parámetro | Valor | Por qué |
|-----------|-------|---------|
| Input Size | `fft_size` | Recibe vectores de N muestras |
| Output Size | `fft_size+cp_len` | Produce vectores de N+CP muestras |
| Rolloff | `0` | Sin roll-off, transición rectangular |
| Tag Length Key | `""` | Modo stream continuo (sin paquetes etiquetados) |

Copia las últimas `cp_len` muestras del símbolo OFDM al inicio: $[x_{N-CP}, \ldots, x_{N-1}, x_0, x_1, \ldots, x_{N-1}]$. El prefijo cíclico es lo que convierte la convolución lineal del canal en circular, permitiendo la ecualización de un tap por subportadora.

!!! tip "GUI ② — Símbolo OFDM en tiempo"
    Conecta un **QT GUI Time Sink** (Size: `fft_size+cp_len`, Type: `Complex`) a la salida de este bloque. Con N=8 y CP=2 verás un símbolo de 10 muestras — las primeras 2 (CP) son copia exacta de las últimas 2.

---

## 4. Canal

### Bloque 8 — Channel Model

**Búscalo como:** `Channel Model`

| Parámetro | Valor | Por qué |
|-----------|-------|---------|
| Noise Voltage | `noise_amp` | Amplitud del AWGN — controlado por el slider |
| Frequency Offset | `0` | Sin desplazamiento de frecuencia portadora |
| Epsilon | `1.0` | Sin error de timing (reloj TX = RX) |
| Taps | `[1.0+0j]` | Canal AWGN plano — sin multipath |

Modela el canal de propagación. Con `taps=[1.0+0j]` el canal es transparente excepto por el ruido AWGN. Para añadir multipath: `taps=[1.0, 0, 0.5j]` agrega una reflexión con retardo 2 muestras y desfase 90°.

!!! tip "GUI ③ y ④ — Señal recibida y espectro"
    Conecta desde la salida de este bloque:
    - **QT GUI Time Sink** → verás la señal OFDM ruidosa
    - **QT GUI Frequency Sink** → verás el espectro plano y rectangular que ocupa el ancho de banda OFDM

---

## 5. Receptor (RX)

### Bloque 9 — Keep M in N

**Búscalo como:** `Keep M in N`

| Parámetro | Valor | Por qué |
|-----------|-------|---------|
| Type | `Complex` | Muestras complejas |
| M | `fft_size` | Número de muestras a conservar (N útiles) |
| N | `fft_size+cp_len` | Período total de un símbolo con CP |
| Offset | `cp_len` | Empieza a conservar después del CP |

De cada bloque de N+CP muestras, descarta las primeras `cp_len` (el prefijo cíclico, que ya cumplió su función) y conserva las N muestras útiles del símbolo OFDM.

### Bloque 10 — Stream to Vector

Igual que en TX: agrupa N muestras en un vector para alimentar la FFT.

| Parámetro | Valor |
|-----------|-------|
| Item Size | `Complex` |
| Num Items | `fft_size` |

### Bloque 11 — FFT (Forward)

**Búscalo como:** `FFT`

| Parámetro | Valor | Por qué |
|-----------|-------|---------|
| FFT Size | `fft_size` | Mismo N que el IFFT del TX |
| Forward/Reverse | `Forward` | Forward = FFT: x[n] → Y[k] = X[k] (canal plano) |
| Window | `Rectangular` | Sin ventana |
| Shift | `No` | Consistente con el TX |

Implementa $Y[k] = \sum_{n=0}^{N-1} y[n]\, e^{-j2\pi kn/N}$. Para canal plano sin ruido: $Y[k] = X[k]$ — recupera exactamente los símbolos transmitidos.

### Bloque 12 — Vector to Stream

Convierte el vector de N complejos de vuelta a un stream continuo.

| Parámetro | Valor |
|-----------|-------|
| Item Size | `Complex` |
| Num Items | `fft_size` |

### Bloque 13 — Multiply Const

**Búscalo como:** `Multiply Const`

| Parámetro | Valor | Por qué |
|-----------|-------|---------|
| Type | `Complex` | Opera sobre símbolos complejos |
| Constant | `1.0` | Canal plano H[k]=1: no se necesita corrección |

Este es el **ecualizador de un tap**. Para un canal plano sin multipath, $H[k]=1$ para toda subportadora, por lo que la corrección es multiplicar por $1/H[k] = 1$. Con multipath se necesita primero estimar $H[k]$ mediante pilotos y luego dividir por él.

!!! tip "GUI ⑤ — Constelación RX post-ecualización"
    Conecta un **QT GUI Constellation Sink** aquí. Este es el sink más importante del laboratorio: muestra qué tan bien se recuperan los símbolos después del canal.

### Bloque 14 — Constellation Decoder

**Búscalo como:** `Constellation Decoder`

| Parámetro | Valor | Por qué |
|-----------|-------|---------|
| Constellation | `mod_const` | Mismo objeto que en TX |

Toma cada símbolo complejo recibido y decide cuál de los 4 puntos QPSK es el más cercano (decisión dura). Convierte cada punto complejo en un índice {0,1,2,3}.

### Bloque 15 — Unpack K Bits

**Búscalo como:** `Unpack K Bits`

| Parámetro | Valor | Por qué |
|-----------|-------|---------|
| K | `2` | Desempaqueta 2 bits por símbolo decodificado |

Convierte el índice de símbolo {0,1,2,3} de vuelta a bits individuales {0,1} — el inverso del bloque `Pack K Bits` del TX.

### Bloque 16 — Null Sink

**Búscalo como:** `Null Sink`

| Parámetro | Valor |
|-----------|-------|
| Type | `Byte` |

Descarta los bits decodificados. En el ejercicio final lo reemplazaremos por un comparador BER.

---

## 6. Visualización de Subportadoras

Para ver las 8 subportadoras individualmente **después de la FFT**, añade:

**Bloque A — Complex to Mag**

| Parámetro | Valor |
|-----------|-------|
| Vec Length | `fft_size` |

Conectado a la salida vectorial del **FFT (Forward)**, antes del `Vector to Stream`.

**Bloque B — QT GUI Vector Sink**

| Parámetro | Valor |
|-----------|-------|
| Vec Size | `fft_size` |
| X Step | `samp_rate/fft_size` |
| X Axis Label | `Frecuencia (Hz)` |
| Y Axis Label | `Magnitud` |

Muestra la magnitud de cada subportadora individualmente. Con canal plano y sin ruido, las 8 barras tienen la misma altura.

---

## 7. Demostraciones: Efectos del Prefijo Cíclico

Con el flowgraph completo, realiza estas demostraciones en secuencia:

| Paso | `noise_amp` | `taps` | `cp_len` | Lo que verás |
|------|-------------|--------|----------|--------------|
| 1 | `0` | `[1.0+0j]` | `2` | 4 puntos perfectos — canal ideal |
| 2 | `0.1` | `[1.0+0j]` | `2` | Pequeñas nubes — AWGN bajo |
| 3 | `0.5` | `[1.0+0j]` | `2` | Nubes solapadas — BER notable |
| 4 | `0` | `[1.0, 0, 0.5j]` | `2` | 4 puntos limpios — CP absorbe multipath |
| 5 | `0` | `[1.0, 0, 0.5j]` | `0` | Constelación colapsada — sin CP, ISI destruye la señal |
| 6 | `0` | `[1.0, 0, 0.5j]` | `2` | Recuperación — CP restaura la señal |

??? note "¿Por qué el CP absorbe el multipath?"
    El canal `[1.0, 0, 0.5j]` tiene un eco con retardo 2 muestras. El CP de longitud 2 copia las últimas 2 muestras al inicio del símbolo. Cuando el eco del símbolo anterior llega con 2 muestras de retraso, "aterriza" dentro del CP del símbolo actual — no contamina las N muestras útiles. Al quitar el CP en el receptor, el símbolo útil ve solo la convolución **circular** del canal, que la FFT puede ecualizar subportadora a subportadora con un solo coeficiente.

---

## 8. Ejercicio — Medir BER en Tiempo Real

¿Hay forma de medir BER directamente en GNU Radio? Sí — usando el bloque `digital.ber_bf` que compara dos streams de bits alineados.

### El problema de la alineación

El TX genera bits y el RX los decodifica con un **retardo de procesamiento** que proviene de los bloques del pipeline (stream_to_vector, FFT, etc.). Para comparar TX vs RX necesitas retrasar los bits TX exactamente esa cantidad.

### Construcción

**Paso 1 — Bifurcar el stream TX**

Después de `Pack K Bits`, conecta la salida a dos destinos:
- Al `Chunks to Symbols` (cadena existente)
- A un nuevo bloque **`Delay`**

**Paso 2 — Bloque Delay**

| Parámetro | Valor |
|-----------|-------|
| Type | `Byte` |
| Delay | `delay_val` |

Añade una nueva variable: `delay_val = 0`.

**Paso 3 — Bloque BER BF**

**Búscalo como:** `BER BF`

| Puerto | Conexión |
|--------|----------|
| Input 0 | Salida de `Unpack K Bits` (bits RX decodificados) |
| Input 1 | Salida del `Delay` (bits TX retrasados) |

**Paso 4 — Mostrar BER**

Conecta la salida de `BER BF` a un **QT GUI Number Sink**.

### Calibración del delay

1. Pon `noise_amp = 0`, `taps = [1.0+0j]` (canal ideal)
2. Añade una variable `variable_qtgui_range` para `delay_val`: Start=0, Stop=200, Step=1
3. Mueve el slider de `delay_val` hasta que el Number Sink muestre BER ≈ 0
4. Ese valor es el retardo de procesamiento del sistema

### Medición BER vs SNR

Con el delay calibrado, llena esta tabla variando `noise_amp`:

| `noise_amp` σ | BER medido | BER teórico QPSK |
|---------------|------------|-----------------|
| 0.0 | — | 0 |
| 0.1 | | |
| 0.2 | | |
| 0.5 | | |
| 1.0 | | |

La BER teórica de QPSK es: $\text{BER} = Q\!\left(\sqrt{2\,E_b/N_0}\right)$

donde $E_b/N_0 \approx 1/(2\sigma^2)$ para señal de potencia unitaria.

??? note "¿Por qué el BER aumenta con σ?"
    El bloque `Channel Model` añade ruido gaussiano complejo con potencia $\sigma^2$ por componente. Cuando la nube de ruido es suficientemente grande como para cruzar el límite de decisión entre dos puntos QPSK (separados √2 en el plano complejo), el decoder toma la decisión incorrecta y produce un error de bit.

### Extensión — BER con multipath

Con el delay calibrado, cambia los taps a `[1.0, 0, 0.5j]` (multipath, delay spread = 2):

- Con `cp_len = 2` (CP ≥ delay spread): el BER debería ser el mismo que sin multipath
- Con `cp_len = 0` (sin CP): el BER debe dispararse aunque `noise_amp = 0`

Esto demuestra cuantitativamente que el CP no solo es una "guardia de seguridad" — es el mecanismo que garantiza que el multipath no añade BER cuando su retardo está dentro del CP.

---

## Notas — Laboratorio 2

| Alumno | **Nota /20** |
|--------|:------------:|
| Bermúdez Silva, Moisés | **18** |
| Castilla Alcalá, Luis  | **18** |
| Livia Mariano, Mariano | **18** |
| Loayza Sáenz, Néstor   | **18** |
| Taipe Quiroz, Meri     | **18** |
