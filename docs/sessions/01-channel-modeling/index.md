---
title: "Sesión 01 — Modelado del Canal Inalámbrico"
session: 1
description: "Fundamentos del canal inalámbrico: path loss, shadowing, multipath fading y modelos estadísticos de Rayleigh y Rician."
---

# Sesión 01 — Modelado del Canal Inalámbrico

## Objetivos de Aprendizaje

Al finalizar esta sesión, el estudiante será capaz de:

1. Calcular la potencia recibida usando el modelo de pérdida de propagación en espacio libre y el modelo log-distancia
2. Modelar el shadowing mediante una variable aleatoria log-normal y estimar su impacto en el link budget
3. Describir el fenómeno de multipath propagation y sus consecuencias en el dominio temporal y frecuencial
4. Derivar las distribuciones de Rayleigh y Rician para la envolvente de la señal en canales con fading
5. Calcular el coherence bandwidth y el coherence time a partir de parámetros del canal

---

## Introducción

El canal inalámbrico es el elemento más impredecible y limitante de cualquier sistema de comunicaciones. A diferencia de los canales guiados (fibra óptica, cable coaxial), el canal inalámbrico somete a la señal a una combinación de efectos que degradan su calidad de forma simultánea:

- **Path loss**: la potencia de la señal disminuye con la distancia
- **Shadowing**: obstáculos como edificios y colinas atenúan la señal de forma aleatoria
- **Multipath fading**: múltiples reflexiones, difracciones y dispersiones crean versiones retardadas de la señal que interfieren entre sí

Comprender y modelar estos efectos es indispensable para todo lo que viene después en este curso: desde el diseño de modulaciones robustas hasta el dimensionamiento de sistemas MIMO y la gestión del espectro en redes 5G. **El canal inalámbrico es la razón por la que existen la mayoría de los problemas que estudiaremos.**

---

## Teoría

### 1. Pérdida de Propagación en Espacio Libre

La **ecuación de Friis** describe la potencia recibida en ausencia de obstáculos:

$$P_r = P_t G_t G_r \left(\frac{\lambda}{4\pi d}\right)^2$$

donde:

- $P_t$: potencia transmitida
- $G_t, G_r$: ganancias de antena transmisora y receptora
- $\lambda = c/f$: longitud de onda
- $d$: distancia entre transmisor y receptor

En decibelios, la **pérdida de propagación en espacio libre** es:

$$\text{PL}_{\text{FS}}(d)\ [\text{dB}] = 20\log_{10}(4\pi d / \lambda) = 20\log_{10}(d) + 20\log_{10}(f) - 147{,}55$$

!!! example "Ejemplo"
    Para $f = 2{,}4\ \text{GHz}$ y $d = 100\ \text{m}$:
    $\text{PL}_{\text{FS}} = 20\log_{10}(100) + 20\log_{10}(2{,}4\times10^9) - 147{,}55 \approx 80\ \text{dB}$

El modelo de Friis es exacto en condiciones de espacio libre, pero las medidas en entornos urbanos muestran sistemáticamente pérdidas que superan esta predicción en 10, 20 o incluso 30 dB — y la discrepancia no es aleatoria: crece de forma ordenada con la distancia y depende del tipo de entorno.

---

### 2. Modelo Log-Distancia

En entornos reales, la pérdida de propagación sigue un modelo empírico más general:

$$\text{PL}(d)\ [\text{dB}] = \text{PL}(d_0) + 10n\log_{10}\!\left(\frac{d}{d_0}\right)$$

donde:

- $d_0$: distancia de referencia (típicamente 1 m en interiores, 100 m en exteriores)
- $n$: **exponente de pérdida de propagación** (path loss exponent)

| Entorno | $n$ típico |
|---------|-----------|
| Espacio libre | 2 |
| Urbano (macrocelda) | 2,7 – 3,5 |
| Suburbano | 3 – 5 |
| Interior (sin obstáculos) | 1,6 – 1,8 |
| Interior (con obstáculos) | 4 – 6 |

Con el exponente $n$ correcto, el modelo predice bien la potencia media recibida a cada distancia. El problema es que dos terminales situados exactamente a la misma distancia de la misma estación base pueden diferir en más de 15 dB — y esa variación cambia lentamente mientras el usuario se desplaza, no con la frecuencia portadora.

---

### 3. Shadowing

Las variaciones lentas de la potencia recibida debidas a obstáculos se modelan añadiendo un término aleatorio al modelo log-distancia:

$$\text{PL}(d)\ [\text{dB}] = \overline{\text{PL}}(d) + X_\sigma$$

donde $X_\sigma \sim \mathcal{N}(0, \sigma^2)$ es una variable gaussiana con desviación típica $\sigma$ (en dB), típicamente entre 4 y 12 dB.

En escala lineal, la potencia recibida sigue una distribución **log-normal** — de ahí el nombre de log-normal shadowing.

El shadowing explica la variabilidad lenta. Pero incluso un terminal completamente estacionario, en un entorno sin objetos en movimiento, muestra fluctuaciones de señal de varios decibelios al desplazarse unos pocos centímetros. A esa escala, los edificios no se mueven — algo más está ocurriendo.

---

### 4. Propagación Multitrayecto

En entornos reales, la señal llega al receptor a través de múltiples caminos con distintos retardos $\tau_i$, atenuaciones $a_i$ y desplazamientos de fase $\phi_i$. La respuesta impulsional del canal en banda base equivalente es:

$$h(\tau, t) = \sum_{i} a_i(t)\, e^{j\phi_i(t)}\, \delta(\tau - \tau_i(t))$$

Los parámetros clave que caracterizan la dispersión temporal del canal son:

**Retardo medio de exceso** (*mean excess delay*):

$$\bar{\tau} = \frac{\sum_i |a_i|^2 \tau_i}{\sum_i |a_i|^2}$$

**Dispersión de retardo RMS** (*RMS delay spread*) $\sigma_\tau$:

$$\sigma_\tau = \sqrt{\overline{\tau^2} - \bar{\tau}^2}$$

**Ancho de banda de coherencia** (*coherence bandwidth*):

$$B_c \approx \frac{1}{5\sigma_\tau}$$

Si el ancho de banda de la señal $B_s \ll B_c$: canal de **flat fading**.
Si $B_s \gg B_c$: canal de **frequency-selective fading**.

La respuesta impulsional $h(\tau, t)$ describe cómo varía el canal en frecuencia. Lo que no dice es con qué rapidez varía en el tiempo — información crítica cuando el terminal está en movimiento.

---

### 5. Efecto Doppler y Tiempo de Coherencia

El movimiento relativo entre transmisor y receptor produce un desplazamiento Doppler:

$$f_D = \frac{v}{\lambda}\cos\theta$$

donde $v$ es la velocidad del móvil y $\theta$ el ángulo de llegada. La **frecuencia Doppler máxima** es $f_{D,\text{max}} = v/\lambda$.

El **tiempo de coherencia** del canal es aproximadamente:

$$T_c \approx \frac{0{,}423}{f_{D,\text{max}}}$$

Si el período de símbolo $T_s \ll T_c$: canal de **slow fading**.
Si $T_s \gg T_c$: canal de **fast fading**.

El coherence time caracteriza la velocidad de variación del canal, pero no dice nada sobre los valores que toma la envolvente. Para calcular BER, probabilidad de outage o ganancia de diversidad, se necesita un modelo estadístico de la amplitud recibida.

---

### 6. Rayleigh Fading

Cuando no existe línea de visión directa (NLOS) entre transmisor y receptor, y hay un gran número de componentes multitrayecto con amplitudes y fases aleatorias, la **envolvente** de la señal recibida sigue una distribución de **Rayleigh**:

$$f_R(r) = \frac{r}{\sigma^2}\exp\!\left(-\frac{r^2}{2\sigma^2}\right), \quad r \geq 0$$

donde $\sigma^2$ es la potencia media de cada componente I/Q. La potencia instantánea $\gamma = r^2 / \bar{\gamma}$ sigue una distribución **exponencial**:

$$f_\gamma(\gamma) = \frac{1}{\bar{\gamma}}\exp\!\left(-\frac{\gamma}{\bar{\gamma}}\right)$$

La **tasa de error de bit (BER)** para BPSK en canal Rayleigh con SNR medio $\bar{\gamma}$ es:

$$\text{BER}_{\text{Rayleigh}} = \frac{1}{2}\left(1 - \sqrt{\frac{\bar{\gamma}}{1 + \bar{\gamma}}}\right) \approx \frac{1}{4\bar{\gamma}} \quad (\bar{\gamma} \gg 1)$$

Nótese que la BER decae como $1/\bar{\gamma}$ (lineal), frente a la caída exponencial en canal AWGN. Este es el coste del fading.

El modelo Rayleigh asume que no existe ninguna componente directa entre transmisor y receptor. En muchos escenarios reales — interiores con visión directa, enlaces punto a punto, picoceldas — esa suposición es demasiado pesimista.

---

### 7. Rician Fading

Cuando existe una componente de línea de visión (LOS) dominante además de las componentes dispersas, la envolvente sigue una distribución de **Rician**:

$$f_R(r) = \frac{r}{\sigma^2}\exp\!\left(-\frac{r^2 + A^2}{2\sigma^2}\right) I_0\!\left(\frac{rA}{\sigma^2}\right), \quad r \geq 0$$

donde $A$ es la amplitud de la componente LOS e $I_0(\cdot)$ es la función de Bessel modificada de orden cero.

El **factor K de Rician** es la relación entre la potencia de la componente LOS y la potencia de las componentes dispersas:

$$K = \frac{A^2}{2\sigma^2}$$

- $K = 0$: Rayleigh fading (sin LOS)
- $K \to \infty$: canal AWGN (LOS dominante, sin dispersión)
- $K = 1$–$10$: valores típicos en entornos con LOS parcial (interior, picoceldas)

!!! example "Ejemplo numérico"
    Un enlace en interiores (corredor de oficinas, $f = 5{,}8\ \text{GHz}$) con potencia total recibida $\Omega = -60\ \text{dBm}$ y $K = 4$ (6 dB). La componente LOS concentra una fracción $K/(K+1) = 4/5 = 80\,\%$ de la potencia total; las componentes difusas aportan el 20 % restante. Esto implica que el deep fading (envolvente $\ll$ valor medio) es mucho menos probable que en Rayleigh fading puro.

Los modelos de Rayleigh y Rician son tractables analíticamente, pero sus parámetros — $\sigma$, $K$, $\sigma_\tau$, $f_D$, el exponente $n$ — deben venir de algún sitio. En diseño de sistemas reales, esos valores no se eligen arbitrariamente.

---

### 8. Modelos de Canal Estandarizados (3GPP TR 38.901)

Los modelos de canal de los organismos de estandarización, como el **3GPP TR 38.901**, parametrizan con precisión los entornos de despliegue para validar sistemas 5G/6G. Los escenarios principales son:

| Escenario | Descripción | $n$ típico (NLOS) | $\sigma_\tau$ típico |
|-----------|-------------|:-----------------:|:--------------------:|
| **UMa** (Urban Macro) | Macrocelda urbana, antena sobre azotea | 3,5 – 4,0 | 300 – 1 000 ns |
| **UMi** (Urban Micro) | Picocelda en calle, antena bajo azotea | 2,8 – 3,5 | 100 – 300 ns |
| **InH** (Indoor Hotspot) | Oficina / corredor interior | 1,7 – 2,2 | 20 – 70 ns |
| **RMa** (Rural Macro) | Macrocelda rural | 2,3 – 4,0 | 10 – 40 ns |

El estándar también distingue entre condiciones **LOS** y **NLOS**, asignando exponentes de path loss y parámetros de fading diferentes para cada caso.

!!! note "Relevancia para el diseño"
    Cuando se evalúa una nueva técnica (OFDM, MIMO, RIS) sobre un canal realista, se utilizan los parámetros de TR 38.901 para que los resultados de simulación sean representativos de los despliegues reales. En las sesiones 06, 07 y 09 utilizaremos este estándar para calibrar nuestras simulaciones.

---

## Síntesis

El canal inalámbrico introduce **tres capas de degradación** que operan a escalas espaciales y temporales distintas:

1. **Path loss** (escala: kilómetros) — determina el radio de cobertura y el link budget. Se controla con potencia de transmisión, ganancia de antena y frecuencia de portadora.
2. **Shadowing** (escala: decenas de metros) — introduce variabilidad estadística lenta. Se gestiona con shadowing margins o diversidad de sitio.
3. **Multipath fading** (escala: longitud de onda, ~cm) — produce fluctuaciones rápidas de la envolvente. Requiere técnicas específicas: OFDM (sesión 03), codificación de canal (sesión 04), MIMO (sesión 06) o diversidad de recepción.

Comprender qué capa domina en cada escenario es el primer paso del diseño de cualquier sistema inalámbrico. El resto del curso puede verse como un catálogo de soluciones a los problemas que esta sesión ha identificado.

---

## Ejercicios

### Ejercicio 1

Un sistema celular opera a $f = 900\ \text{MHz}$. La estación base transmite con $P_t = 2\ \text{W}$ y antenas isotrópicas ($G_t = G_r = 0\ \text{dBi}$). El exponente de pérdida de propagación es $n = 3{,}5$ y la distancia de referencia es $d_0 = 100\ \text{m}$.

**(a)** Calcula la pérdida de propagación en espacio libre $\text{PL}(d_0)$ a la distancia de referencia.

**(b)** Calcula la potencia recibida en dBm a $d = 1\ \text{km}$.

**(c)** Si el shadowing tiene $\sigma = 8\ \text{dB}$, ¿qué shadowing margin adicional se necesita para garantizar cobertura al 90% de las ubicaciones? (Usa $Q^{-1}(0{,}1) \approx 1{,}28$.)

??? example "Solución"

    **(a)** Pérdida en espacio libre a $d_0 = 100\ \text{m}$, $f = 900\ \text{MHz}$:

    $$\lambda = c/f = 3\times10^8 / 9\times10^8 = 0{,}333\ \text{m}$$

    $$\text{PL}(d_0) = 20\log_{10}\!\left(\frac{4\pi \cdot 100}{0{,}333}\right) = 20\log_{10}(3770) \approx 71{,}5\ \text{dB}$$

    **(b)** Con el modelo log-distancia ($d = 1000\ \text{m}$, $d_0 = 100\ \text{m}$, $n = 3{,}5$):

    $$\text{PL}(1000) = 71{,}5 + 10 \times 3{,}5 \times \log_{10}(10) = 71{,}5 + 35 = 106{,}5\ \text{dB}$$

    $$P_r\ [\text{dBm}] = P_t\ [\text{dBm}] - \text{PL} = 33\ \text{dBm} - 106{,}5\ \text{dB} = -73{,}5\ \text{dBm}$$

    **(c)** Para cobertura al 90% de las ubicaciones con shadowing $X_\sigma \sim \mathcal{N}(0, 8^2)$:

    El shadowing margin necesario es:

    $$M_\sigma = Q^{-1}(0{,}1) \times \sigma = 1{,}28 \times 8 \approx 10{,}2\ \text{dB}$$

---

### Ejercicio 2

Un canal de comunicaciones móviles presenta una dispersión de retardo RMS $\sigma_\tau = 5\ \mu\text{s}$.

**(a)** Calcula el ancho de banda de coherencia $B_c$.

**(b)** Un sistema OFDM usa $N = 256$ subportadoras con un ancho de banda total de $B = 10\ \text{MHz}$. ¿El canal es plano o selectivo en frecuencia para cada subportadora?

**(c)** El móvil se desplaza a $v = 120\ \text{km/h}$ y la portadora es $f_c = 2\ \text{GHz}$. Calcula el tiempo de coherencia $T_c$ y determina si el canal es lento o rápido para una duración de símbolo OFDM de $T_s = 100\ \mu\text{s}$.

??? example "Solución"

    **(a)** Ancho de banda de coherencia:

    $$B_c \approx \frac{1}{5\sigma_\tau} = \frac{1}{5 \times 5\times10^{-6}} = 40\ \text{kHz}$$

    **(b)** Espaciado entre subportadoras: $\Delta f = B/N = 10\ \text{MHz}/256 \approx 39\ \text{kHz}$.

    Como $\Delta f \approx B_c$, el canal es **ligeramente frequency-selective** por subportadora. En la práctica se añade un cyclic prefix mayor que $\sigma_\tau$.

    **(c)** Velocidad: $v = 120/3{,}6 \approx 33{,}3\ \text{m/s}$. Longitud de onda: $\lambda = c/f_c = 0{,}15\ \text{m}$.

    $$f_{D,\text{max}} = v/\lambda = 33{,}3/0{,}15 \approx 222\ \text{Hz}$$

    $$T_c \approx \frac{0{,}423}{222} \approx 1{,}9\ \text{ms}$$

    Como $T_s = 100\ \mu\text{s} \ll T_c = 1{,}9\ \text{ms}$, el canal es **slow fading** — el canal no cambia significativamente durante un símbolo OFDM.

---

### Ejercicio 3

En un canal Rayleigh con SNR medio $\bar{\gamma} = 20\ \text{dB}$:

**(a)** Calcula la BER para modulación BPSK. Compara con la BER en canal AWGN con la misma SNR.

**(b)** ¿Cuántos dB adicionales de SNR se necesitan en el canal Rayleigh para alcanzar la misma BER que en AWGN a $\bar{\gamma} = 10\ \text{dB}$?

**(c)** Un canal Rician con $K = 5\ \text{dB}$ y la misma potencia total. ¿Esperarías una BER mayor o menor que en Rayleigh? Justifica cualitativamente.

??? example "Solución"

    **(a)** $\bar{\gamma} = 20\ \text{dB} = 100$.

    Canal Rayleigh:
    $$\text{BER}_{\text{Rayleigh}} \approx \frac{1}{4\bar{\gamma}} = \frac{1}{400} = 2{,}5\times10^{-3}$$

    Canal AWGN ($Q(x) \approx \frac{1}{2}e^{-x^2/2}$ para $x$ grande):
    $$\text{BER}_{\text{AWGN}} = Q(\sqrt{2\bar{\gamma}}) = Q(\sqrt{200}) = Q(14{,}1) \approx 10^{-44}$$

    La diferencia es de **más de 40 órdenes de magnitud** — el Rayleigh fading degrada dramáticamente la BER.

    **(b)** En AWGN con $\bar{\gamma} = 10\ \text{dB} = 10$:
    $$\text{BER}_{\text{AWGN}} = Q(\sqrt{20}) = Q(4{,}47) \approx 3{,}9\times10^{-6}$$

    En Rayleigh, para obtener $\text{BER} \approx 3{,}9\times10^{-6}$:
    $$\frac{1}{4\bar{\gamma}} = 3{,}9\times10^{-6} \Rightarrow \bar{\gamma} \approx 64{,}000 \approx 48\ \text{dB}$$

    Se necesitan aproximadamente **38 dB adicionales** — esta es la "penalización por desvanecimiento" sin técnicas de diversidad.

    **(c)** Con $K > 0$, existe una componente LOS que estabiliza la amplitud de la señal. El Rician fading tiene **menor variabilidad** que el Rayleigh fading, por lo que la BER será **menor** para el mismo $\bar{\gamma}$. A medida que $K \to \infty$, la BER converge a la del canal AWGN.

---

### Ejercicio 4

Sea la envolvente $R$ de un canal Rayleigh con parámetro $\sigma = 1/\sqrt{2}$ (potencia media unitaria).

**(a)** Escribe la función de distribución acumulada (CDF) de $R$ y simplifica para $\sigma^2 = 1/2$.

**(b)** Calcula la **probabilidad de interrupción** (*outage probability*) $P_{\text{out}}$ para un umbral de potencia recibida $\gamma_{\text{th}} = -10\ \text{dB}$ respecto a la potencia media (es decir, $r_{\text{th}}^2 / \mathbb{E}[R^2] = 0{,}1$).

**(c)** ¿Cuál es el umbral $r_{\text{th}}$ (en dB respecto a la potencia media) para que la probabilidad de interrupción sea del 1%?

??? example "Solución"

    **(a)** La CDF de la distribución Rayleigh es:

    $$F_R(r) = 1 - \exp\!\left(-\frac{r^2}{2\sigma^2}\right)$$

    Con $\sigma^2 = 1/2$ y potencia media $\mathbb{E}[R^2] = 2\sigma^2 = 1$:

    $$F_R(r) = 1 - e^{-r^2}$$

    **(b)** El umbral de potencia $\gamma_{\text{th}} = 0{,}1$ corresponde a $r_{\text{th}} = \sqrt{0{,}1} \approx 0{,}316$.

    $$P_{\text{out}} = F_R(r_{\text{th}}) = 1 - e^{-0{,}1} \approx 0{,}095 \approx 9{,}5\,\%$$

    Un 9,5% de las posiciones aleatorias del móvil están en interrupción con este umbral.

    **(c)** Para $P_{\text{out}} = 0{,}01$:

    $$1 - e^{-r_{\text{th}}^2} = 0{,}01 \Rightarrow r_{\text{th}}^2 = -\ln(0{,}99) \approx 0{,}01005$$

    En dB respecto a la potencia media ($\mathbb{E}[R^2]=1$):

    $$10\log_{10}(r_{\text{th}}^2) = 10\log_{10}(0{,}01005) \approx -20\ \text{dB}$$

    Para garantizar sólo el 1% de outage, la señal recibida puede caer hasta **−20 dB** respecto a su valor medio — lo que ilustra por qué el fading margin en el link budget es tan elevado.

---

### Ejercicio 5 — Presupuesto de Enlace Completo

Un sistema LTE opera a $f_c = 1{,}8\ \text{GHz}$ con los siguientes parámetros:

| Parámetro | Valor |
|-----------|-------|
| Potencia de TX | $P_t = 46\ \text{dBm}$ (estación base) |
| Ganancia de antena TX | $G_t = 17\ \text{dBi}$ |
| Ganancia de antena RX | $G_r = 0\ \text{dBi}$ (terminal móvil) |
| Pérdidas de cable/cuerpo | $L_{\text{misc}} = 3\ \text{dB}$ |
| Figura de ruido del receptor | $F = 9\ \text{dB}$ |
| Ancho de banda de señal | $B = 10\ \text{MHz}$ |
| SNR mínima requerida | $\text{SNR}_{\text{min}} = 0\ \text{dB}$ |
| Exponente de pérdida (UMa NLOS) | $n = 3{,}8$, $d_0 = 100\ \text{m}$ |
| Pérdida de referencia en $d_0$ | $\text{PL}(d_0) = 78\ \text{dB}$ |
| Desviación de shadowing | $\sigma = 10\ \text{dB}$, cobertura 90% |

**(a)** Calcula la sensibilidad del receptor $S_{\min}$ en dBm.

**(b)** Calcula la **máxima pérdida de trayecto admisible** (MAPL, *Maximum Allowable Path Loss*).

**(c)** Calcula el radio máximo de celda $d_{\max}$ en metros, incluyendo el margen de sombreado para 90% de cobertura ($Q^{-1}(0{,}1) \approx 1{,}28$).

??? example "Solución"

    **(a)** Sensibilidad del receptor:

    La potencia de ruido térmico en $B = 10\ \text{MHz}$:

    $$N_0 = kTB = -174\ \text{dBm/Hz} + 10\log_{10}(10^7) = -174 + 70 = -104\ \text{dBm}$$

    Con figura de ruido $F = 9\ \text{dB}$:

    $$S_{\min} = N_0 + F + \text{SNR}_{\min} = -104 + 9 + 0 = -95\ \text{dBm}$$

    **(b)** MAPL (Maximum Allowable Path Loss):

    $$\text{MAPL} = P_t + G_t + G_r - L_{\text{misc}} - S_{\min} - M_\sigma$$

    donde el shadowing margin es $M_\sigma = 1{,}28 \times 10 = 12{,}8\ \text{dB}$:

    $$\text{MAPL} = 46 + 17 + 0 - 3 - (-95) - 12{,}8 = 142{,}2\ \text{dB}$$

    **(c)** Radio de celda:

    $$\text{MAPL} = \text{PL}(d_0) + 10n\log_{10}\!\left(\frac{d_{\max}}{d_0}\right)$$

    $$142{,}2 = 78 + 38\log_{10}\!\left(\frac{d_{\max}}{100}\right)$$

    $$\log_{10}\!\left(\frac{d_{\max}}{100}\right) = \frac{64{,}2}{38} = 1{,}689 \Rightarrow d_{\max} = 100 \times 10^{1{,}689} \approx 4{,}9\ \text{km}$$

    Este es el radio de celda máximo para garantizar una SNR de 0 dB en el 90% de las ubicaciones en un entorno UMa NLOS.

---

## Laboratorio Python

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/ollerenac/wireless-communication-systems/blob/main/docs/sessions/01-channel-modeling/lab.ipynb)

En este laboratorio (~90 minutos) implementarás los modelos de canal estudiados en la sesión:

1. **Simulación Rayleigh**: genera la envolvente y verifica la distribución teórica (Ej. 1 — ~15 min)
2. **Rician y factor K**: compara distribuciones para K = 0, 1, 5, 10 dB (Ej. 2 — ~15 min)
3. **BER vs SNR**: curvas de BPSK sobre AWGN y Rayleigh, penalización por desvanecimiento (Ej. 3 — ~20 min)
4. **CDF empírica y probabilidad de interrupción**: calcula outage para distintos umbrales (Ej. 4 — ~15 min)
5. **Link budget calculator**: función completa con Friis + log-distancia + shadowing (Ej. 5 — ~25 min)

---

## Lecturas Recomendadas

1. **Goldsmith, A.** — *Wireless Communications*, Cambridge University Press, 2005. Capítulos 2 y 3.
2. **Tse, D. & Viswanath, P.** — *Fundamentals of Wireless Communication*, Cambridge University Press, 2005. Capítulo 2. (Disponible en abierto en el sitio web de los autores.)
3. **Rappaport, T. S.** — *Wireless Communications: Principles and Practice*, 2ª ed., Prentice Hall, 2002. Capítulos 3 y 4.
4. **3GPP TR 38.901** — *Study on channel model for frequencies from 0.5 to 100 GHz*, Release 17.
