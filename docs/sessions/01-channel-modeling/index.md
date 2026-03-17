---
title: "Sesión 01 — Modelado del Canal Inalámbrico"
status: draft
session: 1
description: "Fundamentos del canal inalámbrico: pérdidas de propagación, sombreado, desvanecimiento multitrayecto y modelos estadísticos de Rayleigh y Rician."
---

# Sesión 01 — Modelado del Canal Inalámbrico

## Objetivos de Aprendizaje

Al finalizar esta sesión, el estudiante será capaz de:

1. Calcular la potencia recibida usando el modelo de pérdida de propagación en espacio libre y el modelo log-distancia
2. Modelar el sombreado mediante una variable aleatoria log-normal y estimar su impacto en el enlace
3. Describir el fenómeno de propagación multitrayecto y sus consecuencias en el dominio temporal y frecuencial
4. Derivar las distribuciones de Rayleigh y Rician para la envolvente de la señal en canales con desvanecimiento
5. Calcular el ancho de banda de coherencia y el tiempo de coherencia a partir de parámetros del canal

---

## Introducción

El canal inalámbrico es el elemento más impredecible y limitante de cualquier sistema de comunicaciones. A diferencia de los canales guiados (fibra óptica, cable coaxial), el canal inalámbrico somete a la señal a una combinación de efectos que degradan su calidad de forma simultánea:

- **Pérdida de propagación**: la potencia de la señal disminuye con la distancia
- **Sombreado**: obstáculos como edificios y colinas atenúan la señal de forma aleatoria
- **Desvanecimiento multitrayecto**: múltiples reflexiones, difracciones y dispersiones crean versiones retardadas de la señal que interfieren entre sí

Comprender y modelar estos efectos es indispensable para todo lo que viene después en este curso: desde el diseño de modulaciones robustas hasta el dimensionamiento de sistemas MIMO y la optimización mediante aprendizaje por refuerzo. **El canal inalámbrico es la razón por la que existen la mayoría de los problemas que estudiaremos.**

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

---

### 3. Sombreado (Shadowing)

Las variaciones lentas de la potencia recibida debidas a obstáculos se modelan añadiendo un término aleatorio al modelo log-distancia:

$$\text{PL}(d)\ [\text{dB}] = \overline{\text{PL}}(d) + X_\sigma$$

donde $X_\sigma \sim \mathcal{N}(0, \sigma^2)$ es una variable gaussiana con desviación típica $\sigma$ (en dB), típicamente entre 4 y 12 dB.

En escala lineal, la potencia recibida sigue una distribución **log-normal** — de ahí el nombre de sombreado log-normal.

---

### 4. Propagación Multitrayecto

En entornos reales, la señal llega al receptor a través de múltiples caminos con distintos retardos $\tau_i$, atenuaciones $a_i$ y desplazamientos de fase $\phi_i$. La respuesta impulsional del canal en banda base equivalente es:

$$h(\tau, t) = \sum_{i} a_i(t)\, e^{j\phi_i(t)}\, \delta(\tau - \tau_i(t))$$

Los parámetros clave que caracterizan el dispersión temporal del canal son:

**Retardo medio de exceso** (*mean excess delay*):

$$\bar{\tau} = \frac{\sum_i |a_i|^2 \tau_i}{\sum_i |a_i|^2}$$

**Dispersión de retardo RMS** (*RMS delay spread*) $\sigma_\tau$:

$$\sigma_\tau = \sqrt{\overline{\tau^2} - \bar{\tau}^2}$$

**Ancho de banda de coherencia** (*coherence bandwidth*):

$$B_c \approx \frac{1}{5\sigma_\tau}$$

Si el ancho de banda de la señal $B_s \ll B_c$: canal de **desvanecimiento plano** (*flat fading*).
Si $B_s \gg B_c$: canal de **desvanecimiento selectivo en frecuencia** (*frequency-selective fading*).

---

### 5. Efecto Doppler y Tiempo de Coherencia

El movimiento relativo entre transmisor y receptor produce un desplazamiento Doppler:

$$f_D = \frac{v}{\lambda}\cos\theta$$

donde $v$ es la velocidad del móvil y $\theta$ el ángulo de llegada. La **frecuencia Doppler máxima** es $f_{D,\text{max}} = v/\lambda$.

El **tiempo de coherencia** del canal es aproximadamente:

$$T_c \approx \frac{0{,}423}{f_{D,\text{max}}}$$

Si el período de símbolo $T_s \ll T_c$: canal **lentamente variante** (*slow fading*).
Si $T_s \gg T_c$: canal **rápidamente variante** (*fast fading*).

---

### 6. Desvanecimiento de Rayleigh

Cuando no existe línea de visión directa (NLOS) entre transmisor y receptor, y hay un gran número de componentes multitrayecto con amplitudes y fases aleatorias, la **envolvente** de la señal recibida sigue una distribución de **Rayleigh**:

$$f_R(r) = \frac{r}{\sigma^2}\exp\!\left(-\frac{r^2}{2\sigma^2}\right), \quad r \geq 0$$

donde $\sigma^2$ es la potencia media de cada componente I/Q. La potencia instantánea $\gamma = r^2 / \bar{\gamma}$ sigue una distribución **exponencial**:

$$f_\gamma(\gamma) = \frac{1}{\bar{\gamma}}\exp\!\left(-\frac{\gamma}{\bar{\gamma}}\right)$$

La **tasa de error de bit (BER)** para BPSK en canal Rayleigh con SNR medio $\bar{\gamma}$ es:

$$\text{BER}_{\text{Rayleigh}} = \frac{1}{2}\left(1 - \sqrt{\frac{\bar{\gamma}}{1 + \bar{\gamma}}}\right) \approx \frac{1}{4\bar{\gamma}} \quad (\bar{\gamma} \gg 1)$$

Nótese que la BER decae como $1/\bar{\gamma}$ (lineal), frente a la caída exponencial en canal AWGN. Este es el coste del desvanecimiento.

---

### 7. Desvanecimiento de Rician

Cuando existe una componente de línea de visión (LOS) dominante además de las componentes dispersas, la envolvente sigue una distribución de **Rician**:

$$f_R(r) = \frac{r}{\sigma^2}\exp\!\left(-\frac{r^2 + A^2}{2\sigma^2}\right) I_0\!\left(\frac{rA}{\sigma^2}\right), \quad r \geq 0$$

donde $A$ es la amplitud de la componente LOS e $I_0(\cdot)$ es la función de Bessel modificada de orden cero.

El **factor K de Rician** es la relación entre la potencia de la componente LOS y la potencia de las componentes dispersas:

$$K = \frac{A^2}{2\sigma^2}$$

- $K = 0$: distribución de Rayleigh (sin LOS)
- $K \to \infty$: canal AWGN (LOS dominante, sin dispersión)
- $K = 1$–$10$: valores típicos en entornos con LOS parcial (interior, picoceldas)

---

## Ejercicios

### Ejercicio 1

Un sistema celular opera a $f = 900\ \text{MHz}$. La estación base transmite con $P_t = 2\ \text{W}$ y antenas isotrópicas ($G_t = G_r = 0\ \text{dBi}$). El exponente de pérdida de propagación es $n = 3{,}5$ y la distancia de referencia es $d_0 = 100\ \text{m}$.

**(a)** Calcula la pérdida de propagación en espacio libre $\text{PL}(d_0)$ a la distancia de referencia.

**(b)** Calcula la potencia recibida en dBm a $d = 1\ \text{km}$.

**(c)** Si el sombreado tiene $\sigma = 8\ \text{dB}$, ¿qué margen de enlace adicional se necesita para garantizar cobertura al 90% de las ubicaciones? (Usa $Q^{-1}(0{,}1) \approx 1{,}28$.)

<details>
<summary>Solución</summary>

**(a)** Pérdida en espacio libre a $d_0 = 100\ \text{m}$, $f = 900\ \text{MHz}$:

$$\lambda = c/f = 3\times10^8 / 9\times10^8 = 0{,}333\ \text{m}$$

$$\text{PL}(d_0) = 20\log_{10}\!\left(\frac{4\pi \cdot 100}{0{,}333}\right) = 20\log_{10}(3770) \approx 71{,}5\ \text{dB}$$

**(b)** Con el modelo log-distancia ($d = 1000\ \text{m}$, $d_0 = 100\ \text{m}$, $n = 3{,}5$):

$$\text{PL}(1000) = 71{,}5 + 10 \times 3{,}5 \times \log_{10}(10) = 71{,}5 + 35 = 106{,}5\ \text{dB}$$

$$P_r\ [\text{dBm}] = P_t\ [\text{dBm}] - \text{PL} = 33\ \text{dBm} - 106{,}5\ \text{dB} = -73{,}5\ \text{dBm}$$

**(c)** Para cobertura al 90% de las ubicaciones con sombreado $X_\sigma \sim \mathcal{N}(0, 8^2)$:

El margen de sombreado necesario es:

$$M_\sigma = Q^{-1}(0{,}1) \times \sigma = 1{,}28 \times 8 \approx 10{,}2\ \text{dB}$$

</details>

---

### Ejercicio 2

Un canal de comunicaciones móviles presenta una dispersión de retardo RMS $\sigma_\tau = 5\ \mu\text{s}$.

**(a)** Calcula el ancho de banda de coherencia $B_c$.

**(b)** Un sistema OFDM usa $N = 256$ subportadoras con un ancho de banda total de $B = 10\ \text{MHz}$. ¿El canal es plano o selectivo en frecuencia para cada subportadora?

**(c)** El móvil se desplaza a $v = 120\ \text{km/h}$ y la portadora es $f_c = 2\ \text{GHz}$. Calcula el tiempo de coherencia $T_c$ y determina si el canal es lento o rápido para una duración de símbolo OFDM de $T_s = 100\ \mu\text{s}$.

<details>
<summary>Solución</summary>

**(a)** Ancho de banda de coherencia:

$$B_c \approx \frac{1}{5\sigma_\tau} = \frac{1}{5 \times 5\times10^{-6}} = 40\ \text{kHz}$$

**(b)** Espaciado entre subportadoras: $\Delta f = B/N = 10\ \text{MHz}/256 \approx 39\ \text{kHz}$.

Como $\Delta f \approx B_c$, el canal es **ligeramente selectivo en frecuencia** por subportadora. En la práctica se añade un prefijo cíclico mayor que $\sigma_\tau$.

**(c)** Velocidad: $v = 120/3{,}6 \approx 33{,}3\ \text{m/s}$. Longitud de onda: $\lambda = c/f_c = 0{,}15\ \text{m}$.

$$f_{D,\text{max}} = v/\lambda = 33{,}3/0{,}15 \approx 222\ \text{Hz}$$

$$T_c \approx \frac{0{,}423}{222} \approx 1{,}9\ \text{ms}$$

Como $T_s = 100\ \mu\text{s} \ll T_c = 1{,}9\ \text{ms}$, el canal es **lentamente variante** (slow fading) — el canal no cambia significativamente durante un símbolo OFDM.

</details>

---

### Ejercicio 3

En un canal Rayleigh con SNR medio $\bar{\gamma} = 20\ \text{dB}$:

**(a)** Calcula la BER para modulación BPSK. Compara con la BER en canal AWGN con la misma SNR.

**(b)** ¿Cuántos dB adicionales de SNR se necesitan en el canal Rayleigh para alcanzar la misma BER que en AWGN a $\bar{\gamma} = 10\ \text{dB}$?

**(c)** Un canal Rician con $K = 5\ \text{dB}$ y la misma potencia total. ¿Esperarías una BER mayor o menor que en Rayleigh? Justifica cualitativamente.

<details>
<summary>Solución</summary>

**(a)** $\bar{\gamma} = 20\ \text{dB} = 100$.

Canal Rayleigh:
$$\text{BER}_{\text{Rayleigh}} \approx \frac{1}{4\bar{\gamma}} = \frac{1}{400} = 2{,}5\times10^{-3}$$

Canal AWGN ($Q(x) \approx \frac{1}{2}e^{-x^2/2}$ para $x$ grande):
$$\text{BER}_{\text{AWGN}} = Q(\sqrt{2\bar{\gamma}}) = Q(\sqrt{200}) = Q(14{,}1) \approx 10^{-44}$$

La diferencia es de **más de 40 órdenes de magnitud** — el desvanecimiento Rayleigh degrada dramáticamente la BER.

**(b)** En AWGN con $\bar{\gamma} = 10\ \text{dB} = 10$:
$$\text{BER}_{\text{AWGN}} = Q(\sqrt{20}) = Q(4{,}47) \approx 3{,}9\times10^{-6}$$

En Rayleigh, para obtener $\text{BER} \approx 3{,}9\times10^{-6}$:
$$\frac{1}{4\bar{\gamma}} = 3{,}9\times10^{-6} \Rightarrow \bar{\gamma} \approx 64{,}000 \approx 48\ \text{dB}$$

Se necesitan aproximadamente **38 dB adicionales** — esta es la "penalización por desvanecimiento" sin técnicas de diversidad.

**(c)** Con $K > 0$, existe una componente LOS que estabiliza la amplitud de la señal. El canal Rician tiene **menor variabilidad** que el Rayleigh, por lo que la BER será **menor** para el mismo $\bar{\gamma}$. A medida que $K \to \infty$, la BER converge a la del canal AWGN.

</details>

---

## Laboratorio Python

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/ollerenac/wireless-communication-systems/blob/main/docs/sessions/01-channel-modeling/lab.ipynb)

En este laboratorio implementarás los modelos de canal estudiados en la sesión:

1. **Simulación de canal Rayleigh y Rician**: generarás trayectorias de desvanecimiento y compararás las distribuciones empíricas con las teóricas
2. **BER vs SNR**: calcularás curvas de BER para BPSK en canal AWGN y en canal Rayleigh, y verificarás la penalización por desvanecimiento
3. **Respuesta impulsional del canal**: generarás y visualizarás la respuesta impulsional de un canal multitrayecto con varios retardos

---

## Lecturas Recomendadas

1. **Goldsmith, A.** — *Wireless Communications*, Cambridge University Press, 2005. Capítulos 2 y 3.
2. **Tse, D. & Viswanath, P.** — *Fundamentals of Wireless Communication*, Cambridge University Press, 2005. Capítulo 2. (Disponible en abierto en el sitio web de los autores.)
3. **Rappaport, T. S.** — *Wireless Communications: Principles and Practice*, 2ª ed., Prentice Hall, 2002. Capítulos 3 y 4.
4. **3GPP TR 38.901** — *Study on channel model for frequencies from 0.5 to 100 GHz*, Release 17.
