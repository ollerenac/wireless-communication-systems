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

Imagina que mides la potencia recibida en 60 puntos distintos del mismo barrio, todos a exactamente 1 km de la misma antena. El modelo log-distancia predice un único valor de PL para esa distancia. Las medidas reales, sin embargo, se dispersan alrededor de esa predicción en un rango de ±15–20 dB. La causa no es ruido de medida: es la disposición particular de edificios, muros y obstáculos entre la antena y cada punto — diferente en cada ubicación, impredecible de antemano.

Modelar cada obstáculo individualmente es inviable. En cambio, se trata el efecto acumulado como una variable aleatoria: la pérdida a una distancia $d$ ya no es un número fijo sino la suma de la predicción media más una desviación aleatoria que depende del entorno específico de cada ubicación.

$$\text{PL}(d)\ [\text{dB}] = \overline{\text{PL}}(d) + X_\sigma$$

- $\overline{\text{PL}}(d)$ — la barra indica **valor medio**: es exactamente la predicción del modelo log-distancia, es decir, la pérdida esperada promediada sobre todas las posibles ubicaciones a distancia $d$.
- $X_\sigma \sim \mathcal{N}(0, \sigma^2)$ — la desviación aleatoria en dB en una ubicación concreta, con media cero (no introduce sesgo) y desviación típica $\sigma$ entre 4 y 12 dB según el entorno.

La elección de una distribución gaussiana en dB tiene dos justificaciones. La primera es empírica: las medidas de campo en entornos urbanos muestran consistentemente que los residuos $\text{PL}_{\text{medido}} - \overline{\text{PL}}(d)$ siguen una campana gaussiana. La segunda es teórica: cada obstáculo multiplica la potencia por un factor aleatorio en escala lineal; el producto de muchos factores aleatorios independientes tiene logaritmo gaussiano por el teorema central del límite. En escala lineal, la potencia sigue una distribución **log-normal** — de ahí el nombre de log-normal shadowing.

![Shadowing: medidas reales vs. predicción del modelo](figures/shadowing-scatter.png)

El panel izquierdo muestra medidas simuladas dispersas alrededor de la curva $\overline{\text{PL}}(d)$: cada punto es una ubicación real con su disposición única de obstáculos. La flecha roja marca $X_\sigma$ — la desviación de esa ubicación concreta respecto a la predicción media. Las bandas $\pm\sigma$ y $\pm 2\sigma$ encierran aproximadamente el 68% y el 95% de las ubicaciones posibles. El panel derecho muestra el histograma de los residuos a distancia fija: la campana gaussiana confirma por qué $\mathcal{N}(0, \sigma^2)$ es el modelo correcto.

La figura siguiente resume las tres contribuciones estudiadas hasta aquí, representadas sobre los mismos ejes de distancia y path loss:

![Path loss: de Friis al shadowing](figures/path-loss-models.png)

La curva de **Friis** ($n=2$) establece el límite inferior de pérdida en espacio libre: es determinista, sin dispersión. Las curvas de **log-distancia** ($n=2.5$, $3.5$, $4.5$) muestran cómo el entorno físico modifica el slope — la divergencia respecto a Friis crece logarítmicamente con la distancia. Las **bandas de shadowing** ($\pm\sigma$ y $\pm 2\sigma$ alrededor de $n=3.5$) representan la dispersión estadística que introduce el log-normal shadowing: para cualquier distancia dada, la potencia recibida no es un valor único sino una distribución gaussiana en dB, centrada en la curva del modelo log-distancia.

Las tres capas comparten el mismo espacio: distancia vs. path loss. Esto cambia a partir de la siguiente sección. El multipath fading no opera a escala de metros sino de centímetros — a la escala de la longitud de onda — y su descripción requiere un framework matemático completamente distinto.

El shadowing explica la variabilidad lenta. Pero incluso un terminal completamente estacionario, en un entorno sin objetos en movimiento, muestra fluctuaciones de señal de varios decibelios al desplazarse unos pocos centímetros. A esa escala, los edificios no se mueven — algo más está ocurriendo.

---

### 4. Multipath Propagation

En un entorno urbano, la señal transmitida no viaja únicamente en línea recta hacia el receptor. Se refleja en fachadas de edificios, se difracta en esquinas, se dispersa en vehículos y objetos. El receptor recibe simultáneamente varias copias de la misma señal, cada una llegando por un camino distinto.

![Multipath propagation: caminos físicos y respuesta impulsional](figures/multipath-channel.png)

El panel izquierdo muestra tres caminos de ejemplo. El **camino directo** (verde) recorre la distancia mínima y llega primero, con el menor retardo $\tau_1$ y la mayor amplitud $a_1$. Los caminos reflejados (azul, rojo) recorren distancias mayores: llegan más tarde ($\tau_2 > \tau_1$, $\tau_3 > \tau_2$) y con menor amplitud ($a_2 < a_1$, $a_3 < a_2$) porque cada reflexión introduce pérdidas adicionales.

**El experimento mental del impulso**: supón que el transmisor emite un pulso perfectamente corto — un impulso de Dirac $\delta(t)$. El receptor no recibe un único pulso sino una secuencia de ecos, uno por cada camino, llegando en tiempos distintos. El panel derecho de la figura muestra exactamente eso: la **respuesta impulsional del canal** $h(\tau)$, con tres impulsos en $\tau_1$, $\tau_2$ y $\tau_3$ de amplitudes $a_1$, $a_2$ y $a_3$. El canal queda completamente caracterizado por esa "huella".

Formalizando: si el camino $i$ llega con retardo $\tau_i$, atenuación $a_i$ y desfase $\phi_i$, su contribución a la señal recibida es una copia de la señal transmitida desplazada $\tau_i$ segundos, escalada por $a_i$ y rotada en fase $e^{j\phi_i}$. La suma de todas las contribuciones es la respuesta impulsional del canal en banda base equivalente:

$$h(\tau, t) = \sum_{i} a_i(t)\, e^{j\phi_i(t)}\, \delta(\tau - \tau_i(t))$$

Cada término de la suma es un eco: la **delta de Dirac** $\delta(\tau - \tau_i)$ actúa como selector — extrae del eje de retardos exactamente el instante $\tau_i$ en que llega el camino $i$. La amplitud $a_i$ y la fase $e^{j\phi_i}$ describen cuánto atenúa y cuánto desfasa ese camino específico.

La dependencia en $t$ — la segunda variable — aparece porque el canal no es estático: cuando el terminal o los objetos del entorno se mueven, las longitudes de los caminos cambian. Un camino que antes llegaba en $\tau_i$ ahora llega en $\tau_i(t)$, con una amplitud $a_i(t)$ y una fase $\phi_i(t)$ distintas. El canal es, por tanto, una función de **dos variables independientes**: $\tau$ describe la estructura del canal en el dominio de los retardos; $t$ describe cómo evoluciona esa estructura en el tiempo.

Con la respuesta impulsional definida, el siguiente paso es cuantificar cuánto se dispersan los ecos en tiempo. Tres parámetros lo describen:

**Mean excess delay** $\bar{\tau}$ — el "centro de masa" de la energía multitrayecto en el eje de retardos, ponderado por la potencia de cada camino:

$$\bar{\tau} = \frac{\sum_i |a_i|^2 \tau_i}{\sum_i |a_i|^2}$$

No tiene consecuencias directas de diseño por sí solo, pero es el punto de referencia para calcular el parámetro que sí importa.

**RMS delay spread** $\sigma_\tau$ — la desviación estándar de los retardos respecto a $\bar{\tau}$, ponderada por potencia:

$$\sigma_\tau = \sqrt{\overline{\tau^2} - \bar{\tau}^2}$$

$\sigma_\tau$ mide cuánto tiempo tardan en llegar todos los ecos significativos después del primero — es decir, la "duración de la memoria" del canal. Un canal con $\sigma_\tau$ grande tiene ecos que llegan muy dispersos en el tiempo; uno con $\sigma_\tau$ pequeño tiene ecos casi simultáneos. Valores típicos: interiores de oficina ~30 ns, urbano ~300 ns, suburbano ~1 µs.

**Coherence bandwidth** $B_c$ — el rango de frecuencias sobre el que el canal se comporta de forma aproximadamente uniforme:

$$B_c \approx \frac{1}{5\,\sigma_\tau}$$

Para entender de dónde viene esta relación: la respuesta en frecuencia del canal $H(f)$ es la transformada de Fourier de $h(\tau)$. Si los ecos se extienden durante $\sigma_\tau$ segundos en el dominio temporal, $H(f)$ varía significativamente en un rango de frecuencias del orden de $1/\sigma_\tau$. El factor 5 es una convención práctica (criterio del 50% de correlación). $B_c$ define, por tanto, el "ancho de banda de correlación" del canal: dos componentes espectrales separadas por menos de $B_c$ ven esencialmente el mismo canal; separadas por más de $B_c$, ven canales independientes.

La relación entre $B_c$ y el ancho de banda de la señal $B_s$ determina el régimen de operación:

- **Flat fading** ($B_s \ll B_c$): $B_c$ es la zona del espectro sobre la que el canal aplica una degradación uniforme. Si $B_s$ es mucho menor que $B_c$, toda la señal cabe dentro de esa zona uniforme — el canal aplica **una única ganancia** a toda la señal, como multiplicar por un solo número complejo. Todas las frecuencias de la señal sufren la misma atenuación y el mismo desfase. No hay distorsión espectral: la señal sale del canal con la misma forma que entró, solo escalada y rotada en fase.

- **Frequency-selective fading** ($B_s \gg B_c$): cuando $B_s$ supera ampliamente $B_c$, la señal ocupa varias zonas del espectro, cada una con su propia ganancia. El canal ya no aplica una degradación única — aplica **ganancias diferentes a diferentes partes de la señal**. Algunas frecuencias son muy atenuadas (los valles de $|H(f)|$), otras lo son menos (los picos). En el dominio temporal esto significa que los ecos de un símbolo se extienden en el tiempo y se solapan con el símbolo siguiente, produciendo **ISI** (inter-symbol interference).

![Flat fading vs frequency-selective fading](figures/flat-vs-selective-fading.png)

La curva negra en ambos paneles es la misma: la respuesta en frecuencia $|H(f)|$ del canal, con sus picos y valles. Lo que cambia es el tamaño de $B_s$ respecto a $B_c$.

En el panel izquierdo (flat fading), $B_s$ es estrecho y cae en un tramo aproximadamente plano de $|H(f)|$: todas las frecuencias de la señal ven la misma ganancia, el canal se comporta como un multiplicador. En el panel derecho (frequency-selective fading), $B_s$ es ancho y abarca múltiples picos y valles de $|H(f)|$: cada segmento de la señal recibe una atenuación distinta, la forma espectral queda distorsionada y aparece ISI en el dominio temporal.

Este es uno de los problemas centrales que motiva el diseño de OFDM (sesión 03): dividir el ancho de banda total en cientos de subportadoras estrechas, cada una con $B_s \ll B_c$, de modo que cada subportadora opera en flat fading aunque el canal global sea frequency-selective.

Todo lo visto en esta sección — $h(\tau)$, $\sigma_\tau$, $B_c$, flat fading, FSF — describe el canal **en un instante congelado**. Es una fotografía. Lo que no dice es con qué rapidez cambia esa fotografía cuando el terminal o los objetos del entorno se mueven.

---

### 5. Doppler Effect y Coherence Time

Imagina un coche circulando a 120 km/h con una conexión 4G activa. A 2 GHz, la longitud de onda es $\lambda = 15$ cm. En 1 ms, el coche recorre 3,3 cm — aproximadamente $\lambda/4$. En ese intervalo, la diferencia de camino hacia cada reflexor ha cambiado en una fracción de $\lambda$, lo que equivale a una rotación de fase de varios grados en cada eco multitrayecto. La respuesta en frecuencia $|H(f)|$ — los picos y valles que vimos en la figura anterior — es ahora diferente. El canal que el receptor midió hace 1 ms ya no es válido. ¿Cuánto tiempo sigue siendo válida una estimación del canal? Esa es la pregunta que responde esta sección.

**Mecanismo físico**: cuando el terminal se mueve con velocidad $v$, cada camino multitrayecto tiene una componente de velocidad distinta a lo largo de su dirección de llegada. Esa componente acorta o alarga el camino en cada ciclo de la portadora, produciendo un **desplazamiento en frecuencia** — el efecto Doppler:

$$f_D = \frac{v}{\lambda}\cos\theta$$

donde $\theta$ es el ángulo entre la dirección de movimiento y la dirección de llegada del camino. Un camino que llega de frente ($\theta=0°$) sufre el máximo desplazamiento positivo $f_{D,\text{max}} = v/\lambda$; uno que llega por detrás ($\theta=180°$) sufre el máximo negativo $-f_{D,\text{max}}$; los que llegan en perpendicular ($\theta=90°$) no tienen desplazamiento.

![Doppler effect: geometría y espectro](figures/doppler-spectrum-v2.png)

El panel izquierdo muestra cuatro caminos multitrayecto llegando al receptor móvil desde ángulos distintos. Cada uno produce un desplazamiento Doppler diferente según $f_D = (v/\lambda)\cos\theta$: el camino frontal (verde, $\theta=0°$) se desplaza al máximo positivo; el camino trasero (rojo, $\theta=180°$) al máximo negativo; los intermedios quedan entre ambos extremos.

El panel derecho muestra lo que ocurre en el dominio de la frecuencia. El transmisor emite una **única frecuencia** $f_0$ — el tono negro vertical. El receptor, sin embargo, recibe **múltiples copias** de esa frecuencia, cada una desplazada por el Doppler de su camino: los cuatro círculos de colores corresponden exactamente a los cuatro caminos del panel izquierdo. El conjunto de todos estos desplazamientos forma el **Doppler spread**, que se extiende entre $-f_{D,\text{max}}$ y $+f_{D,\text{max}}$. La curva gris es el perfil espectral resultante para dispersión isotrópica (caminos igualmente distribuidos en todos los ángulos) — la forma en "U" característica del modelo de Jakes.

Con muchos caminos en ángulos distintos, cada uno contribuye en una frecuencia ligeramente diferente — el conjunto forma un **Doppler spread** que se extiende entre $-f_{D,\text{max}}$ y $+f_{D,\text{max}}$.

**Coherence time** $T_c$ — el dual temporal del coherence bandwidth: así como $B_c$ definía el rango de frecuencias sobre el que el canal es uniforme, $T_c$ define el intervalo de tiempo durante el que el canal puede considerarse estático. Dos medidas del canal separadas por menos de $T_c$ son similares; separadas por más de $T_c$, son prácticamente independientes:

$$T_c \approx \frac{0{,}423}{f_{D,\text{max}}}$$

Nótese la dualidad con $B_c \approx 1/(5\sigma_\tau)$: el delay spread $\sigma_\tau$ comprime $B_c$ en frecuencia; el Doppler spread $f_{D,\text{max}}$ comprime $T_c$ en tiempo. Velocidades altas → $f_{D,\text{max}}$ grande → $T_c$ pequeño → el canal cambia rápidamente.

La relación entre $T_s$ (duración de un símbolo) y $T_c$ determina el régimen temporal:

- **Slow fading** ($T_s \ll T_c$): el canal apenas cambia durante la transmisión de un símbolo. Una estimación del canal obtenida con un piloto sigue siendo válida varios símbolos después. Es el régimen habitual en la mayoría de los sistemas prácticos.

- **Fast fading** ($T_s \gg T_c$): el canal cambia múltiples veces dentro de un solo símbolo. El receptor no puede seguir el canal con suficiente rapidez. Es el caso de terminales muy rápidos o portadoras muy altas (mmWave con vehículos).

![Slow fading vs fast fading](figures/slow-vs-fast-fading.png)

Ambos paneles muestran la amplitud recibida en dB en una sola frecuencia, variando en el tiempo. En slow fading (arriba), $T_c$ es grande — el canal cambia lentamente y un símbolo de duración $T_s \ll T_c$ ve un canal prácticamente constante. En fast fading (abajo), $T_c$ es pequeño — el canal completa varias fluctuaciones dentro de un símbolo de duración $T_s \gg T_c$, lo que hace imposible asumir que el canal es estático durante la recepción.

**Los cuatro parámetros que caracterizan $h(\tau, t)$**: la función de dos variables queda completamente descrita por dos pares duales:

| Dimensión | Parámetro de dispersión | Parámetro de coherencia | Régimen |
|-----------|------------------------|------------------------|---------|
| Frecuencia ($\tau$) | Delay spread $\sigma_\tau$ | Coherence bandwidth $B_c \approx 1/5\sigma_\tau$ | Flat / Frequency-selective |
| Tiempo ($t$) | Doppler spread $f_{D,\text{max}}$ | Coherence time $T_c \approx 0.423/f_{D,\text{max}}$ | Slow / Fast fading |

Estos cuatro parámetros son los datos de entrada del diseñador de sistemas: determinan la longitud del cyclic prefix en OFDM, la densidad de pilotos en la cuadrícula tiempo-frecuencia, la frecuencia de actualización del estimador de canal y el máximo orden de modulación que puede sostenerse de forma fiable.

Los cuatro parámetros de la tabla caracterizan la **estructura** del canal — cómo se dispersa en frecuencia y cómo varía en el tiempo. Pero hay una pregunta que aún no hemos respondido: ¿qué **valor** toma la amplitud de la señal recibida en un instante concreto?

Para conectar con lo que viene, es útil recordar qué determina si un bit se recibe correctamente.

En el receptor, la señal llega mezclada con **ruido térmico** — una perturbación aleatoria e inevitable generada en los circuitos electrónicos. El detector compara la señal recibida con un umbral: si la señal está suficientemente por encima del ruido, el bit se decodifica correctamente; si el ruido la empuja al otro lado del umbral, se produce un error. La relación entre la potencia de la señal y la potencia del ruido es la **SNR** (*Signal-to-Noise Ratio*) $\gamma$. Cuanto mayor es $\gamma$, más separada está la señal del umbral de decisión y menor es la probabilidad de error — la **BER** (*Bit Error Rate*).

![SNR y BER: umbral de decisión en BPSK](figures/snr-ber-decision.png)

La figura muestra el proceso de detección para BPSK — el caso más simple, con dos símbolos: $+A$ (bit 1) y $-A$ (bit 0). La señal recibida no es un valor exacto sino una distribución gaussiana centrada en el símbolo transmitido, cuya anchura $\sigma_n$ depende del ruido térmico. El detector coloca el umbral de decisión en 0: todo lo que llega por encima de 0 se decide como bit 1; todo lo que llega por debajo, como bit 0. La **zona de error** (rojo) es la fracción de la distribución que cruza el umbral — la probabilidad de que el ruido haya desplazado la señal al lado equivocado.

En el panel izquierdo (SNR alta), las dos distribuciones están bien separadas: la zona de error es pequeña y la BER es baja. En el panel derecho (SNR baja), el ruido es grande relativo a la señal — las distribuciones se solapan y la zona de error crece sustancialmente. La SNR $\gamma = A^2/\sigma_n^2$ captura exactamente esa relación: a mayor $\gamma$, mayor separación entre señal y umbral, menor zona de error, menor BER.

El link budget de las secciones 1–3 calculó la **potencia media recibida** en función de la distancia, el entorno y el shadowing. Dividida por la potencia de ruido del receptor, esa potencia media da la **SNR media** $\bar{\gamma}$. Si el canal fuera puramente AWGN, $\gamma$ sería constante e igual a $\bar{\gamma}$, y la BER quedaría fijada.

El problema es el multipath fading. Las múltiples réplicas de la señal llegan con fases aleatorias y se suman de forma constructiva o destructiva dependiendo de la posición exacta del receptor. Cuando se suman destructivamente, la amplitud recibida cae — a veces de forma drástica. En esos instantes, la SNR instantánea $\gamma$ desciende muy por debajo de $\bar{\gamma}$: aunque el promedio sea confortable (digamos $\bar{\gamma} = 20$ dB), hay momentos en que $\gamma$ cae a 0 dB o menos. Esos instantes de baja SNR — los **deep fades** — son los que producen ráfagas de errores de bit, aunque el nivel medio de señal sea perfectamente adecuado. Para calcular la BER real es necesario conocer la distribución estadística de esas fluctuaciones de $\gamma$.

---

### 6. Rayleigh Fading

Para obtener esa distribución estadística de $\gamma$ hay que responder primero a una pregunta más física: ¿cómo se suma en el receptor el conjunto de todos los caminos multitrayecto? La respuesta a esa pregunta revela de dónde vienen las componentes $I$ y $Q$, y por qué la envolvente resultante sigue una distribución de Rayleigh.

**De dónde vienen las componentes I y Q**: hay que rastrearlas desde sus orígenes físicos.

Considera un transmisor que emite una portadora $\cos(2\pi f_c t)$. Cada uno de los $N$ caminos multitrayecto llega al receptor con una amplitud $a_i$ y un desfase de fase acumulado $\phi_i$ (debido a la diferencia de longitud de camino). La contribución del camino $i$ es:

$$s_i(t) = a_i \cos(2\pi f_c t + \phi_i)$$

Aplicando la identidad trigonométrica $\cos(\alpha + \beta) = \cos\alpha\cos\beta - \sin\alpha\sin\beta$:

$$s_i(t) = \underbrace{a_i \cos\phi_i}_{I_i} \cdot \cos(2\pi f_c t) \;-\; \underbrace{a_i \sin\phi_i}_{Q_i} \cdot \sin(2\pi f_c t)$$

Cada camino aporta dos proyecciones: una sobre la portadora coseno ($I_i$) y otra sobre la portadora seno desplazada 90° ($Q_i$). Sumando los $N$ caminos, la señal total es:

$$s(t) = \underbrace{\left(\sum_{i=1}^N a_i \cos\phi_i\right)}_{I} \cos(2\pi f_c t) \;-\; \underbrace{\left(\sum_{i=1}^N a_i \sin\phi_i\right)}_{Q} \sin(2\pi f_c t)$$

$I$ y $Q$ son, por tanto, **sumas de muchas variables aleatorias independientes** — cada $a_i$ y $\phi_i$ es aleatoria e independiente de los demás caminos. Cuando $N$ es grande (entorno urbano: decenas o centenares de caminos), el **teorema central del límite** (TCL) garantiza que $I$ y $Q$ convergen a distribuciones gaussianas de media cero e igual varianza $\sigma^2$. El hecho de que ambas tengan media cero refleja que, sin LOS, las fases $\phi_i$ se distribuyen uniformemente en $[0, 2\pi)$ — los cosenos y senos se cancelan en promedio.

![Derivación de Rayleigh: diagrama fasorial e histogramas I/Q](figures/rayleigh-derivation.png)

El panel izquierdo muestra la imagen fasorial: cada flecha de color representa un camino multitrayecto ($I_i + jQ_i$), con amplitud $a_i$ y fase $\phi_i$ aleatorias. La flecha negra gruesa es la **suma vectorial** $I + jQ$ — el fasor resultante que ve el receptor. En cada nuevo instante de tiempo, las amplitudes y fases cambian, y el punto extremo de la flecha negra recorre la región sombreada de manera aleatoria. El panel derecho muestra los histogramas de $I$ y $Q$ obtenidos de miles de realizaciones independientes: ambas componentes siguen distribuciones gaussianas centradas en cero, tal como predice el TCL.

La **envolvente** de la señal — la amplitud del fasor resultante — es:

$$r = \sqrt{I^2 + Q^2}$$

Geométricamente, $r$ es la distancia desde el origen hasta el extremo del fasor negro. Como $I$ y $Q$ son gaussianas independientes de igual varianza, $r$ sigue una distribución de **Rayleigh**:

$$f_R(r) = \frac{r}{\sigma^2}\exp\!\left(-\frac{r^2}{2\sigma^2}\right), \quad r \geq 0$$

La envolvente tiene un valor medio $\bar{r}$ — pero a diferencia de una señal AWGN pura, tiene una cola izquierda no nula: existe una probabilidad de que $r$ caiga muy cerca de cero (deep fade), independientemente de cuál sea la potencia media.

La **SNR instantánea** $\gamma = r^2/\bar{\gamma}$ — la potencia instantánea normalizada — sigue una distribución **exponencial**:

$$f_\gamma(\gamma) = \frac{1}{\bar{\gamma}}\exp\!\left(-\frac{\gamma}{\bar{\gamma}}\right)$$

La distribución exponencial tiene una **cola izquierda pesada**: aunque la SNR media sea $\bar{\gamma}$, hay una fracción significativa del tiempo en que $\gamma$ es mucho menor que $\bar{\gamma}$. Esos instantes de baja SNR son los que generan errores.

**De la BER en AWGN a la BER en fading**: en un canal AWGN con SNR fija $\gamma$, la BER para BPSK es determinista: $\text{BER}_{\text{AWGN}}(\gamma) = Q(\sqrt{2\gamma})$. En un canal Rayleigh, $\gamma$ es aleatoria — la BER efectiva es el **promedio** de $\text{BER}_{\text{AWGN}}(\gamma)$ sobre todas las posibles realizaciones de $\gamma$:

$$\text{BER}_{\text{Rayleigh}} = \int_0^\infty Q\!\left(\sqrt{2\gamma}\right) f_\gamma(\gamma)\, d\gamma = \frac{1}{2}\left(1 - \sqrt{\frac{\bar{\gamma}}{1 + \bar{\gamma}}}\right) \approx \frac{1}{4\bar{\gamma}} \quad (\bar{\gamma} \gg 1)$$

El resultado es una BER que decae como $1/\bar{\gamma}$ — **linealmente** con la SNR media — en lugar de la caída exponencial del canal AWGN. La diferencia es enorme en la práctica.

![Rayleigh fading: PDF, distribución de SNR y BER](figures/rayleigh-ber.png)

El panel izquierdo muestra la PDF de la envolvente Rayleigh: aunque la envolvente tiene un valor medio $\bar{r}$, hay una probabilidad no despreciable de que caiga por debajo del umbral de detección (zona roja) — esos instantes producen errores. El panel central muestra la distribución exponencial de la SNR instantánea $\gamma$: la cola izquierda pesada confirma que existe una fracción significativa del tiempo con $\gamma$ muy baja. El panel derecho compara directamente la BER en AWGN y en Rayleigh fading: para alcanzar una BER de $10^{-3}$, el canal Rayleigh requiere aproximadamente **17 dB más de SNR** que el canal AWGN — esa es la penalización por fading sin ninguna técnica de mitigación.

El modelo Rayleigh asume que no existe ninguna componente directa entre transmisor y receptor. En muchos escenarios reales — interiores con visión directa, enlaces punto a punto, picoceldas — esa suposición es demasiado pesimista.

---

### 7. Rician Fading

La derivación I/Q de la sección anterior asumió que todas las fases $\phi_i$ son uniformemente distribuidas en $[0, 2\pi)$, de modo que las medias de $I$ y $Q$ son exactamente cero. Esa suposición corresponde a un entorno NLOS sin camino directo entre transmisor y receptor. Ahora consideramos qué ocurre cuando **sí existe un camino LOS**: una componente con amplitud fija $A$ que llega con fase $\phi_\text{LOS}$ prácticamente constante (el camino directo no cambia de longitud de manera aleatoria).

**Impacto del LOS en el diagrama fasorial**: por la misma identidad trigonométrica de la sección 6, el camino LOS aporta:

$$s_\text{LOS}(t) = A\cos(2\pi f_c t + \phi_\text{LOS}) = \underbrace{A\cos\phi_\text{LOS}}_{\mu_I} \cos(2\pi f_c t) - \underbrace{A\sin\phi_\text{LOS}}_{\mu_Q} \sin(2\pi f_c t)$$

Este término es **determinista** — no aleatorio. Los $N-1$ caminos dispersos restantes siguen siendo aleatorios con media cero, igual que en Rayleigh. La suma total da:

$$I = \underbrace{A\cos\phi_\text{LOS}}_{\mu_I \neq 0} + \tilde{I}_\text{scatter}, \qquad Q = \underbrace{A\sin\phi_\text{LOS}}_{\mu_Q \neq 0} + \tilde{Q}_\text{scatter}$$

donde $\tilde{I}_\text{scatter}$ y $\tilde{Q}_\text{scatter}$ son gaussianas de media cero y varianza $\sigma^2$ (igual que en Rayleigh). Con el término LOS, $I$ y $Q$ siguen siendo gaussianas de varianza $\sigma^2$, pero ahora con **media no nula**: $I \sim \mathcal{N}(\mu_I, \sigma^2)$, $Q \sim \mathcal{N}(\mu_Q, \sigma^2)$. En el diagrama fasorial, el cúmulo de puntos ya no está centrado en el origen — está desplazado al punto $(\mu_I, \mu_Q)$, que es el fasor LOS.

**De dónde sale la PDF de Rician**: la envolvente $r = \sqrt{I^2 + Q^2}$ es la distancia desde el origen hasta ese cúmulo desplazado. Para obtener su distribución, hay que integrar la PDF gaussiana 2D sobre todos los puntos situados a distancia $r$ del origen — es decir, sobre el círculo de radio $r$:

$$f_R(r) = \int_0^{2\pi} \frac{r}{2\pi\sigma^2} \exp\!\left(-\frac{(I-\mu_I)^2 + (Q-\mu_Q)^2}{2\sigma^2}\right) d\theta$$

Expandiendo el cuadrado y usando la identidad $\mu_I^2 + \mu_Q^2 = A^2$ (porque $A^2\cos^2\phi_\text{LOS} + A^2\sin^2\phi_\text{LOS} = A^2$), la integral sobre el ángulo $\theta$ produce exactamente $\int_0^{2\pi} e^{(rA/\sigma^2)\cos\theta}\,d\theta = 2\pi\, I_0(rA/\sigma^2)$, donde $I_0(\cdot)$ es la **función de Bessel modificada de orden cero** — simplemente el nombre que recibe esa integral estándar. El resultado es la **distribución de Rician**:

$$f_R(r) = \frac{r}{\sigma^2}\exp\!\left(-\frac{r^2 + A^2}{2\sigma^2}\right) I_0\!\left(\frac{rA}{\sigma^2}\right), \quad r \geq 0$$

Nótese que cuando $A = 0$ (sin LOS), $I_0(0) = 1$ y la expresión se reduce exactamente a la PDF de Rayleigh de la sección 6 — Rayleigh es el caso límite de Rician sin componente directa.

**El factor K de Rician**: es conveniente expresar la distribución en función de la relación entre la potencia LOS y la potencia de las componentes dispersas. La potencia de la componente LOS es $A^2/2$ (valor cuadrático medio de $A\cos(2\pi f_c t + \phi_\text{LOS})$). La potencia total de las componentes dispersas es $\sigma_I^2 + \sigma_Q^2 = 2\sigma^2$. El cociente define el **factor K**:

$$K = \frac{A^2/2}{\sigma^2 + \sigma^2} = \frac{A^2}{2\sigma^2}$$

Con este parámetro, los dos extremos quedan perfectamente caracterizados:

- $K = 0$ ($A = 0$): sin LOS → Rayleigh fading
- $K \to \infty$ ($\sigma \to 0$): sin dispersión → canal puramente determinista, equivalente a AWGN
- $K = 1$–$10$ (0–10 dB): LOS parcial, típico en interiores, picoceldas y enlaces punto a punto

**Efecto sobre la BER**: con LOS, el cúmulo de puntos en el diagrama fasorial está desplazado hacia $A$ — lejos del origen. El deep fading requiere que el ruido aleatorio sea suficientemente grande como para arrastrar el fasor resultante hasta cerca de cero, lo que ocurre con mucha menor frecuencia que en Rayleigh. A medida que $K$ crece, la PDF de la envolvente se estrecha y su pico se aleja del origen, reduciendo la probabilidad de deep fades y mejorando la BER.

![Distribución de Rician para distintos valores de K](figures/rayleigh-rician-pdf.png)

La figura muestra la PDF de la envolvente para K = 0 (Rayleigh), 1, $\sqrt{10}$ y 10. Con K = 0, la PDF tiene su máximo cerca del origen y una cola izquierda ancha — los deep fades son frecuentes. Al aumentar K, el pico se desplaza hacia la derecha y la distribución se estrecha: la envolvente es más predecible y concentrada alrededor de su valor medio. Para K = 10 (10 dB), la PDF se asemeja a una gaussiana estrecha — el canal se comporta casi como AWGN.

!!! example "Ejemplo numérico"
    Un enlace en interiores (corredor de oficinas, $f = 5{,}8\ \text{GHz}$) con potencia total recibida $\Omega = -60\ \text{dBm}$ y $K = 4$ (6 dB). El factor K relaciona las potencias LOS y difusa: $K/(K+1) = 4/5 = 80\,\%$ de la potencia total está concentrada en la componente LOS; las componentes dispersas aportan sólo el 20 % restante. El fasor resultante rara vez se aleja del valor LOS dominante, por lo que la probabilidad de deep fading es mucho menor que en Rayleigh fading puro con la misma potencia media.

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
