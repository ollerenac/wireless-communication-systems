---
title: "Sesión 06 — MIMO: Múltiples Antenas, Múltiples Posibilidades"
session: 6
description: "De SISO a MIMO masivo: el canal matricial, capacidad vía SVD, el compromiso diversidad-multiplexación, y los precodificadores MRT y ZF que usa 5G NR."
---

# Sesión 06 — MIMO: Múltiples Antenas, Múltiples Posibilidades

## Objetivos de Aprendizaje

Al finalizar esta sesión, el estudiante será capaz de:

1. Explicar cómo el canal MIMO se modela como una matriz **H** y por qué añadir antenas aumenta la capacidad linealmente (no logarítmicamente)
2. Aplicar la descomposición SVD de **H** para obtener canales paralelos independientes y calcular la capacidad MIMO con y sin información de canal en el transmisor
3. Describir el compromiso diversidad-multiplexación (DMT) y elegir el régimen adecuado según las condiciones del enlace
4. Calcular los precodificadores MRT y ZF para un sistema multiusuario y comparar su SINR resultante
5. Explicar los fenómenos de *channel hardening* y *favorable propagation* que hacen que Massive MIMO con MRT sea prácticamente óptimo

---

## Introducción

En las sesiones anteriores el canal fue siempre un escalar: una sola señal entra, una sola señal sale. La Sesión 01 caracterizó estadísticamente ese escalar (Rayleigh, Rician). La Sesión 02 diseñó modulaciones para transmitir bits a través de él. La Sesión 03 demostró que OFDM transforma un canal selectivo en frecuencia en cientos de canales planos — pero cada subportadora seguía siendo un escalar. La Sesión 05 añadió redundancia para corregir los errores que ese escalar introduce.

La pregunta que abre esta sesión es diferente: ¿qué ocurre si añadimos más antenas en el transmisor, en el receptor, o en ambos? La respuesta es contraintuitiva y poderosa. Con $N_t$ antenas transmisoras y $N_r$ receptoras, el canal deja de ser un escalar y pasa a ser una **matriz** $\mathbf{H} \in \mathbb{C}^{N_r \times N_t}$. Esta matriz tiene estructura — concretamente, una descomposición SVD — que permite transformarla en hasta $\min(N_t, N_r)$ canales AWGN paralelos e independientes.

La consecuencia es fundamental: mientras que la capacidad SISO crece como $\log_2(1 + \text{SNR})$ — logarítmicamente, con rendimientos decrecientes — la capacidad MIMO puede crecer **linealmente** con $\min(N_t, N_r)$ a cualquier SNR fijo. Un sistema $4 \times 4$ con 10 dB de SNR puede cuadruplicar la tasa de un sistema $1 \times 1$ con la misma potencia y ancho de banda.

Es por eso que **todos** los sistemas inalámbricos modernos son MIMO: el estándar 5G NR define antenas de hasta 256 elementos en la estación base. La sesión pasa de la intuición al álgebra lineal que subyace a esas antenas, y de ahí a los algoritmos de precodificación que las hacen funcionar.

---

## Teoría

### 1. De SISO a MIMO — la Intuición Espacial

El canal SISO tiene una sola "vía" entre el transmisor y el receptor. Con múltiples antenas, existen **múltiples vías simultáneas** que pueden usarse de dos maneras opuestas:

- **Diversidad espacial**: enviar la misma información por todas las vías. Si una vía experimenta *fading* profundo, las otras siguen activas. La confiabilidad aumenta.
- **Multiplexación espacial**: enviar información *diferente* por cada vía. La tasa total aumenta.

Estas dos estrategias son las extremas del **compromiso diversidad-multiplexación** (§4). Entre ellas existe un continuo de soluciones óptimas según la SNR y los requisitos del enlace.

<figure markdown="span">
  ![Configuraciones SISO, SIMO, MISO y MIMO](figures/mimo-configurations.png)
  <!-- generada por celda 2 de lab.ipynb -->
  <figcaption markdown="1">**Figura 1.** Las cuatro configuraciones de antenas. **SISO** ($N_t=1, N_r=1$): canal escalar, capacidad $\log_2(1+\text{SNR})$. **SIMO** ($N_t=1, N_r>1$): el receptor combina $N_r$ copias de la señal (diversidad de recepción, ganancia de array de hasta $N_r$). **MISO** ($N_t>1, N_r=1$): el transmisor forma el haz (beamforming) hacia el receptor. **MIMO** ($N_t>1, N_r>1$): capacidad para multiplexación espacial y/o diversidad simultánea.
  </figcaption>
</figure>

### 2. El Canal MIMO — Modelo Matricial

Sea $\mathbf{x} \in \mathbb{C}^{N_t}$ el vector transmitido con restricción de potencia $\mathbb{E}[\|\mathbf{x}\|^2] \leq P$, y $\mathbf{y} \in \mathbb{C}^{N_r}$ el vector recibido. El modelo de canal MIMO de banda estrecha (flat fading) es:

$$\boxed{\mathbf{y} = \mathbf{H}\mathbf{x} + \mathbf{n}} \tag{1}$$

donde $\mathbf{H} \in \mathbb{C}^{N_r \times N_t}$ es la **matriz de canal** y $\mathbf{n} \sim \mathcal{CN}(\mathbf{0}, N_0\mathbf{I}_{N_r})$ es ruido gaussiano complejo circular i.i.d. El elemento $h_{ji} = [\mathbf{H}]_{j,i}$ es la ganancia compleja entre la antena transmisora $i$ y la antena receptora $j$, incluyendo pérdida de propagación, desvanecimiento y desfase.

**Modelo i.i.d. Rayleigh.** El caso analíticamente más tractable y pedagógicamente fundamental asume que todos los $h_{ji}$ son i.i.d.:

$$h_{ji} \sim \mathcal{CN}(0, 1) \tag{2}$$

Este modelo corresponde a un entorno con *scattering* denso e isótropo donde no hay línea de visión directa (NLOS) y las antenas están suficientemente separadas ($\geq \lambda/2$) para que los coeficientes sean estadísticamente independientes. En 5G NR los canales espacialmente correlacionados (antenas en ULA compacto) requieren modelos más sofisticados como el CDL-C/D del TR 38.901, pero el modelo i.i.d. captura la física esencial y produce todos los resultados analíticos clave.

<figure markdown="span">
  ![Estructura de la matriz de canal MIMO](figures/mimo-channel-matrix.png)
  <!-- generada por celda 3 de lab.ipynb -->
  <figcaption markdown="1">**Figura 2.** Visualización de la matriz $\mathbf{H}$ para un sistema $4 \times 4$. Cada elemento $h_{ji}$ es una variable compleja con módulo $|h_{ji}|$ (intensidad del enlace) y fase $\angle h_{ji}$ (retardo de propagación). El panel izquierdo muestra la magnitud $|\mathbf{H}|$; el panel derecho muestra la fase. En el modelo i.i.d. Rayleigh, todos los elementos son estadísticamente equivalentes — la estructura explotable proviene de la *geometría* de la matriz, no de correlación entre entradas.
  </figcaption>
</figure>

### 3. Capacidad MIMO vía SVD

La herramienta central de esta sesión es la **Descomposición en Valores Singulares** (SVD) de la matriz de canal:

$$\mathbf{H} = \mathbf{U} \boldsymbol{\Sigma} \mathbf{V}^{\mathsf{H}} \tag{3}$$

donde $\mathbf{U} \in \mathbb{C}^{N_r \times N_r}$ y $\mathbf{V} \in \mathbb{C}^{N_t \times N_t}$ son matrices unitarias ($\mathbf{U}\mathbf{U}^{\mathsf{H}} = \mathbf{I}$, $\mathbf{V}\mathbf{V}^{\mathsf{H}} = \mathbf{I}$), y $\boldsymbol{\Sigma} \in \mathbb{R}^{N_r \times N_t}$ es diagonal con los **valores singulares** $\sigma_1 \geq \sigma_2 \geq \cdots \geq \sigma_r \geq 0$, $r = \mathrm{rank}(\mathbf{H}) \leq \min(N_t, N_r)$.

**Diagonalización del canal.** Si el transmisor conoce $\mathbf{H}$ (CSIT completo), puede **precodificar** con $\mathbf{V}$ y el receptor puede **combinar** con $\mathbf{U}^{\mathsf{H}}$:

$$\tilde{\mathbf{y}} = \mathbf{U}^{\mathsf{H}}\mathbf{y} = \mathbf{U}^{\mathsf{H}}\mathbf{H}\mathbf{V}\tilde{\mathbf{x}} + \mathbf{U}^{\mathsf{H}}\mathbf{n} = \boldsymbol{\Sigma}\tilde{\mathbf{x}} + \tilde{\mathbf{n}} \tag{4}$$

Como $\mathbf{U}$ es unitaria, $\tilde{\mathbf{n}} = \mathbf{U}^{\mathsf{H}}\mathbf{n}$ conserva la distribución $\mathcal{CN}(\mathbf{0}, N_0\mathbf{I})$. El resultado es $r$ **canales AWGN paralelos e independientes**:

$$\tilde{y}_k = \sigma_k \tilde{x}_k + \tilde{n}_k, \quad k = 1, \ldots, r \tag{5}$$

El canal MIMO se ha convertido en $r$ canales escalares independientes con ganancias $\sigma_k^2$.

<figure markdown="span">
  ![SVD descompone H en canales paralelos](figures/mimo-svd-channels.png)
  <!-- generada por celda 5 de lab.ipynb -->
  <figcaption markdown="1">**Figura 3.** La SVD transforma el canal MIMO $\mathbf{H}$ (izquierda) en $r = \min(N_t, N_r)$ canales AWGN escalares independientes con SNR$_k = \sigma_k^2 P_k / N_0$ (derecha). La precodificación con $\mathbf{V}$ en el transmisor y la combinación con $\mathbf{U}^{\mathsf{H}}$ en el receptor realizan esta transformación sin pérdida de información. El SNR de cada subcanal es proporcional al cuadrado del $k$-ésimo valor singular de $\mathbf{H}$.
  </figcaption>
</figure>

**Capacidad con CSIT (water-filling).** Dado que los $r$ subcanales son independientes, la capacidad total se maximiza distribuyendo la potencia $P$ con *water-filling* (WF):

$$\boxed{C_{\text{WF}} = \sum_{k=1}^{r} \log_2\!\left(1 + \frac{P_k^* \sigma_k^2}{N_0}\right)} \quad \text{[bit/s/Hz]} \tag{6}$$

con $P_k^* = (\mu - N_0/\sigma_k^2)^+$ y $\mu$ el nivel de agua que satisface $\sum_k P_k^* = P$.

**Capacidad sin CSIT (potencia uniforme).** En la práctica, el transmisor a menudo no conoce $\mathbf{H}$. Con potencia uniforme $P_k = P/N_t$, la capacidad es:

$$C_{\text{iCSI}} = \log_2\det\!\left(\mathbf{I}_{N_r} + \frac{P}{N_t N_0}\mathbf{H}\mathbf{H}^{\mathsf{H}}\right) = \sum_{k=1}^{r} \log_2\!\left(1 + \frac{P \sigma_k^2}{N_t N_0}\right) \tag{7}$$

**La clave**: con $N_t = N_r = N$ antenas y en alta SNR, $C \approx N \log_2(\text{SNR}/N) + \text{const}$. La capacidad escala **linealmente** con $N = \min(N_t, N_r)$. Cada factor de 2 en el número de antenas *duplica* la capacidad — sin ancho de banda adicional y sin potencia adicional.

<figure markdown="span">
  ![Capacidad MIMO vs SNR para diferentes configuraciones](figures/mimo-capacity.png)
  <!-- generada por celda 6 de lab.ipynb -->
  <figcaption markdown="1">**Figura 4.** Capacidad ergódica (media sobre realizaciones del canal) en función de $E_b/N_0$ para sistemas $1\times1$, $2\times2$, $4\times4$ y $8\times8$ con modelo i.i.d. Rayleigh. Las curvas confirman el crecimiento lineal en $N$ a SNR alta (las curvas se separan proporcionalmente). La **pendiente** en esta escala log es $N$ veces la de SISO — la principal razón por la que todos los sistemas inalámbricos modernos son MIMO.
  </figcaption>
</figure>

### 4. El Compromiso Diversidad-Multiplexación (DMT)

Con múltiples antenas se puede elegir entre dos tipos de ganancia, pero no maximizar ambas simultáneamente. Esta tensión fue formalizada por Zheng y Tse (2003) en el **Diversity-Multiplexing Tradeoff** (DMT).

Se definen en el límite de SNR alta:
- **Ganancia de multiplexación**: $r = \lim_{\text{SNR}\to\infty} R/\log_2\text{SNR}$ (cuántas "dimensiones" de tasa)
- **Ganancia de diversidad**: $d = -\lim_{\text{SNR}\to\infty} \log P_e / \log\text{SNR}$ (qué tan rápido cae la BER)

La **curva DMT óptima** para un sistema $N_t \times N_r$ con i.i.d. Rayleigh es:

$$d^*(r) = (N_t - r)(N_r - r), \quad r \in \{0, 1, \ldots, \min(N_t, N_r)\} \tag{8}$$

Los puntos extremos son:
- $r = 0$: diversidad máxima $d = N_t N_r$ (enviar 0 streams independientes, repetición completa)
- $r = \min(N_t, N_r)$: multiplexación máxima $d = 0$ (máximos streams, sin protección)

**Regla práctica de diseño:**

| Condición del enlace | Estrategia recomendada | Razón |
|---|---|---|
| SNR baja, cobertura crítica | Diversidad ($r$ pequeño) | La BER cae más rápido con SNR |
| SNR alta, throughput máximo | Multiplexación ($r = \min(N_t,N_r)$) | La tasa crece linealmente |
| SNR media | Punto intermedio DMT | Equilibrio tasa/confiabilidad |

En 5G NR, el selector de rango (rank adaptation) elige $r$ dinámicamente basándose en el CQI reportado por el UE — exactamente esta lógica.

<figure markdown="span">
  ![Curva DMT para sistemas 2×2, 4×4](figures/mimo-dmt.png)
  <!-- generada por celda 8 de lab.ipynb -->
  <figcaption markdown="1">**Figura 5.** Curva DMT $d^*(r)$ para sistemas $2\times2$ (triángulo) y $4\times4$ (polígono). Los puntos marcados son esquemas concretos: **OSTBC** (Space-Time Block Code) maximiza diversidad operando en $r=1$; **V-BLAST** maximiza multiplexación en $r=\min(N_t,N_r)$; el punto intermedio es la solución de Zheng-Tse para $r=1$ en el sistema $4\times4$. Un sistema que opera al vértice inferior-derecho explota toda la multiplexación — cada dB adicional de SNR se traduce en tasa, no en reducción de errores.
  </figcaption>
</figure>

### 5. Precodificación Lineal: MRT y ZF

En el escenario multiusuario (MU-MIMO), la estación base tiene $M$ antenas y sirve simultáneamente a $K$ usuarios, cada uno con una sola antena. El canal de bajada es:

$$\mathbf{y} = \mathbf{H}\mathbf{W}\mathbf{s} + \mathbf{n} \tag{9}$$

donde $\mathbf{H} \in \mathbb{C}^{K \times M}$ es el canal agregado, $\mathbf{W} \in \mathbb{C}^{M \times K}$ es la **matriz de precodificación** y $\mathbf{s} \in \mathbb{C}^K$ son los símbolos de los $K$ usuarios. La señal recibida por el usuario $k$ es:

$$y_k = \mathbf{h}_k^{\mathsf{H}} \mathbf{w}_k s_k + \underbrace{\sum_{j \neq k} \mathbf{h}_k^{\mathsf{H}} \mathbf{w}_j s_j}_{\text{interferencia entre usuarios}} + n_k \tag{10}$$

El diseño del precoder $\mathbf{W}$ es el problema central del MU-MIMO.

**Maximum Ratio Transmission (MRT).** El precoder más simple: apuntar el haz hacia cada usuario con el vector conjugado de su canal:

$$\mathbf{W}_{\text{MRT}} = \mathbf{H}^{\mathsf{H}} \tag{11}$$

MRT maximiza la potencia recibida por el usuario objetivo, pero **no cancela la interferencia** entre usuarios. El SINR del usuario $k$ es:

$$\text{SINR}_k^{\text{MRT}} = \frac{|\mathbf{h}_k^{\mathsf{H}} \mathbf{h}_k|^2}{\sum_{j \neq k} |\mathbf{h}_k^{\mathsf{H}} \mathbf{h}_j|^2 + N_0} \tag{12}$$

**Zero-Forcing (ZF).** El precoder que **elimina completamente** la interferencia entre usuarios mediante la pseudoinversa:

$$\mathbf{W}_{\text{ZF}} = \mathbf{H}^{\mathsf{H}}(\mathbf{H}\mathbf{H}^{\mathsf{H}})^{-1} \tag{13}$$

Con ZF, $\mathbf{h}_k^{\mathsf{H}} \mathbf{w}_j^{\text{ZF}} = 0$ para $k \neq j$ (interferencia nula), pero la inversión de $\mathbf{H}\mathbf{H}^{\mathsf{H}}$ amplifica el ruido cuando los canales son casi paralelos (mal condicionamiento).

| Precoder | Interferencia | Ruido | Óptimo cuando |
|---|---|---|---|
| MRT | Alta (no cancelada) | Bajo | $M \gg K$ (canales casi ortogonales) |
| ZF | Cero | Amplificado | SNR alta, $M \geq K$ |
| Óptimo (MMSE/RZF) | Cancelada parcialmente | Balance óptimo | Siempre (mayor coste computacional) |

<figure markdown="span">
  ![BER de MRT vs ZF para K=4 usuarios](figures/mimo-mrt-zf.png)
  <!-- generada por celda 10 de lab.ipynb -->
  <figcaption markdown="1">**Figura 6.** Curvas BER (QPSK) para MRT y ZF con $M=8$ antenas en la BS y $K=4$ usuarios. A SNR baja, MRT domina porque ZF amplifica el ruido. A SNR alta, ZF supera a MRT porque la interferencia (no cancelada por MRT) se convierte en el término limitante. La figura muestra el "cruce" típico alrededor de 10–12 dB para esta configuración.
  </figcaption>
</figure>

### 6. Massive MIMO — Escalar a $M \gg K$ Antenas

Massive MIMO lleva el MU-MIMO al extremo: $M \gg K$ (típicamente $M/K \geq 10$). Dos fenómenos emergentes hacen que el sistema sea analíticamente tratable y, sobre todo, **extremadamente eficiente**:

**6.1 Channel Hardening.** Con $M$ antenas y canal i.i.d., la norma del canal del usuario $k$ concentra:

$$\frac{\|\mathbf{h}_k\|^2}{M} \xrightarrow[M \to \infty]{\text{a.s.}} \beta_k \tag{14}$$

donde $\beta_k$ es la ganancia de gran escala (path loss + shadowing). La potencia recibida con MRT deja de ser aleatoria — se **endurece** (hardening). El canal efectivo actúa como un canal AWGN determinístico. Las fluctuaciones por *fading* rápido desaparecen en la agregación de $M$ antenas.

**6.2 Favorable Propagation.** Con $M \gg K$, los canales de distintos usuarios se vuelven asintóticamente ortogonales:

$$\frac{\mathbf{h}_k^{\mathsf{H}} \mathbf{h}_j}{M} \xrightarrow[M \to \infty]{\text{a.s.}} 0, \quad k \neq j \tag{15}$$

Esto significa que la interferencia entre usuarios con MRT (el numerador cruzado en la ec. (12)) tiende a cero conforme $M$ crece — MRT se vuelve **asintóticamente óptimo** y la interferencia entre usuarios desaparece sin necesidad de inversión matricial.

**Consecuencia práctica**: con $M \gg K$, MRT es suficiente. El SINR del usuario $k$ converge a:

$$\text{SINR}_k^{\text{MRT}} \xrightarrow{M \to \infty} \frac{M \beta_k P / K}{N_0} \tag{16}$$

La potencia útil crece **linealmente con $M$** (array gain) mientras la interferencia desaparece. Esto es la esencia del "free lunch" del Massive MIMO: más antenas en la BS aumentan la SNR de todos los usuarios sin coste de potencia en el terminal.

<figure markdown="span">
  ![Channel hardening y favorable propagation vs M](figures/mimo-massive.png)
  <!-- generada por celdas 12–13 de lab.ipynb -->
  <figcaption markdown="1">**Figura 7.** Izquierda: *Channel hardening* — la distribución de $\|\mathbf{h}_k\|^2/M$ se estrecha entorno a $\beta_k=1$ conforme aumenta $M$ (de $M=4$ a $M=256$). Derecha: *Favorable propagation* — el módulo del producto interno normalizado $|\mathbf{h}_k^{\mathsf{H}}\mathbf{h}_j|/M$ (interferencia entre dos usuarios) tiende a 0 con $M$ creciente. Ambas curvas ilustran la ley de los grandes números aplicada al espacio: las fluctuaciones de fading se promedian en las $M$ antenas.
  </figcaption>
</figure>

**MIMO Masivo en 5G NR.** La estación base 5G NR utiliza arrays de antenas activas (AAS) con configuraciones típicas de 32T32R, 64T64R o 128T128R en FR1 (sub-6 GHz). El estándar soporta hasta $r = 8$ capas (streams) simultáneos por UE en DL (Tabla 7.3.1.3-1 del TS 38.214). El bloque de precodificación en el gNB implementa en la práctica una variante del ZF regularizado (RZF / MMSE precoder) que equilibra los costes computacionales de la inversión matricial con las ganancias de cancelación de interferencia.

<figure markdown="span">
  ![Sum-rate MRT vs ZF vs óptimo para Massive MIMO](figures/mimo-sumrate.png)
  <!-- generada por celda 14 de lab.ipynb -->
  <figcaption markdown="1">**Figura 8.** Suma de tasas (sum-rate) en función del número de antenas en la BS $M$ para $K=4$ usuarios, SNR $= 10$ dB. MRT se acerca al óptimo conforme $M$ crece (favorable propagation) y supera a ZF para $M$ grandes porque evita la amplificación de ruido del inverso. La brecha entre MRT y ZF se cierra cuando $M/K \geq 10$ — la región de Massive MIMO en la que trabajan las BS 5G.
  </figcaption>
</figure>

---

## Laboratorio

El laboratorio de esta sesión implementa los cuatro pilares analíticos de la teoría:

1. **Ejercicio 1 — Canal MIMO y SVD**: construir realizaciones de $\mathbf{H}$ i.i.d. Rayleigh, calcular la SVD y visualizar la distribución de valores singulares (comparar con la distribución Marchenko-Pastur).
2. **Ejercicio 2 — Capacidad MIMO**: trazar la capacidad ergódica (media sobre realizaciones) para $1\times1$, $2\times2$, $4\times4$ y $8\times8$ en función del SNR; verificar el escalado lineal en $N$.
3. **Ejercicio 3 — Precodificadores MRT y ZF**: simular curvas BER (QPSK) para un sistema $8\times4$ (8 antenas BS, 4 usuarios), comparar MRT y ZF a distintas SNR, identificar el cruce.
4. **Ejercicio 4 — Massive MIMO**: demostrar *channel hardening* y *favorable propagation* variando $M$ de 4 a 512; graficar la suma de tasas MRT vs ZF vs óptimo.

Accede al laboratorio en:
[`lab.ipynb`](lab.ipynb)

---

## Resumen

| Concepto | Expresión clave | Implicación práctica |
|---|---|---|
| Modelo MIMO | $\mathbf{y} = \mathbf{H}\mathbf{x} + \mathbf{n}$ | Canal matricial — álgebra lineal como herramienta principal |
| SVD | $\mathbf{H} = \mathbf{U}\boldsymbol{\Sigma}\mathbf{V}^{\mathsf{H}}$ | Descompone H en $r$ canales AWGN independientes |
| Capacidad | $C = \sum_k \log_2(1 + P_k^* \sigma_k^2 / N_0)$ | Escala linealmente con $\min(N_t, N_r)$ |
| DMT | $d^*(r) = (N_t - r)(N_r - r)$ | Elige $r$ según SNR y requisitos de enlace |
| MRT | $\mathbf{W} = \mathbf{H}^{\mathsf{H}}$ | Simple, óptimo cuando $M \gg K$ |
| ZF | $\mathbf{W} = \mathbf{H}^{\mathsf{H}}(\mathbf{H}\mathbf{H}^{\mathsf{H}})^{-1}$ | Cancela interferencia, amplifica ruido |
| Massive MIMO | $M \gg K \Rightarrow$ MRT $\approx$ óptimo | *Channel hardening* + *favorable propagation* |
