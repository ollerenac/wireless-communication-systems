---
title: "Sesión 06 — MIMO en redes reales: cobertura, capacidad y usuarios"
session: 6
description: "Cómo elegir entre diversidad, beamforming, SU-MIMO, MU-MIMO y Massive MIMO según SNR, rank, CSI, interferencia, pilotos y arquitectura de red."
---

# Sesión 06 — MIMO en redes reales: cobertura, capacidad y usuarios

- [Vídeo - Parte 1](https://youtu.be/GaMZSzmyoIs)


## Objetivos de Aprendizaje

Al finalizar esta sesión, el estudiante será capaz de:

1. Diagnosticar qué problema de red intenta resolver un sistema multiantena: cobertura, throughput, interferencia, densidad de usuarios o pérdida de propagación en bandas altas.
2. Elegir entre SIMO, MISO, SU-MIMO, MU-MIMO, Massive MIMO y beamforming híbrido según el escenario de despliegue.
3. Interpretar la matriz de canal $\mathbf{H}$ como herramienta de diseño: rank, valores singulares, condicionamiento, correlación espacial, normas de canal y CSI.
4. Decidir cuándo conviene diversidad, beamforming o multiplexación espacial, y cuándo subir o bajar el rank de transmisión.
5. Comparar detectores y precodificadores implementables (ZF, MMSE, SIC, ML, MRT, ZF y RZF/MMSE) en términos de interferencia, ruido, cómputo y disponibilidad de CSI.
6. Explicar por qué Massive MIMO depende de TDD, pilotos, reciprocidad, scheduler y control de contaminación de pilotos.

---

## Introducción

En las sesiones anteriores el problema parecía tener una sola dimensión: una señal entra, una señal sale, y el diseñador ajusta modulación, codificación, OFDM o potencia para que los bits sobrevivan. MIMO cambia la pregunta. La pregunta ya no es solo "cuánta capacidad tiene una matriz", sino:

> Tengo un problema de cobertura, capacidad, interferencia o densidad de usuarios. ¿Qué hago con las antenas?

Esa es la lectura implementativa de MIMO. Las antenas no son decoración ni una fórmula de capacidad: son grados de libertad espaciales que se pueden gastar de formas distintas. A veces se usan para que un usuario en borde de celda reciba suficiente energía. A veces para enviar dos o cuatro capas al mismo terminal. A veces para servir varios usuarios al mismo tiempo. A veces para formar un haz estrecho en mmWave, donde sin ganancia de array el enlace ni siquiera cierra.

La decisión correcta depende del canal, no de una regla fija. Si el canal tiene buen rank y SNR alta, subir capas aumenta throughput. Si el canal está mal condicionado, forzar muchas capas hace que el receptor o el precoder amplifique ruido. Si los usuarios tienen canales casi ortogonales, MU-MIMO funciona bien. Si los canales son paralelos, el scheduler debe separarlos en tiempo/frecuencia o el precoder pagará mucha potencia para cancelar interferencia.

El objetivo de esta sesión es construir esa brújula. La matemática sigue estando: $\mathbf{H}$, la SVD, el compromiso diversidad-multiplexación (DMT), y los precodificadores y detectores clásicos (MRT, ZF, MMSE). Pero aquí aparecen como herramientas para tomar decisiones de red; cada sigla se define en la sección donde se usa por primera vez.

---

## Teoría

!!! note "Vocabulario de la sesión (léelo primero: evita el 80% de la confusión)"

    - **Capa = stream = flujo**: son la misma cosa y este documento los usa como sinónimos. Es un chorro de datos independiente que se transmite al mismo tiempo que los demás. Los estándares dicen *layers*; los papers dicen *streams*.
    - **Modo espacial** (o "tubo"): cada canal paralelo e independiente escondido dentro de $\mathbf{H}$; la SVD los revela. No es sinónimo de capa: la **capa** es *lo que mandas*, el **modo** es *por dónde pasa*. Idealmente cada capa viaja por su propio modo.
    - **Grados de libertad espaciales**: cuántas "cosas distintas a la vez" permite hacer el arreglo de antenas. Se gastan en robustez, en throughput o en servir más usuarios — no en todo a la vez.
    - **Cerrar el enlace**: lograr que la potencia que llega al receptor alcance el SNR mínimo que exige la tasa de error objetivo. Si el enlace "no cierra", ninguna otra optimización importa.
    - **CSI / CSIT / CSIR**: *channel state information* — el conocimiento de $\mathbf{H}$. La T o R final indica quién lo tiene: el Transmisor o el Receptor.
    - **BS / UE**: estación base / terminal del usuario.
    - **TDD / FDD**: duplexación por tiempo (subida y bajada alternan sobre la **misma** frecuencia → el canal de ida y el de vuelta son el mismo: *reciprocidad*) / por frecuencia (subida y bajada en bandas **distintas** → canales distintos, la reciprocidad no aplica).
    - **FR1 / FR2**: los dos rangos de frecuencia de 5G. FR1: sub-6 GHz. FR2: ondas milimétricas (24 GHz en adelante), donde la pérdida de propagación es tan alta que sin ganancia de haz el enlace no cierra.
    - Los términos propios de Massive MIMO (*channel hardening*, *favorable propagation*, contaminación de pilotos) se definen en §7, donde se usan de verdad.

### 1. Primero el problema de red

Antes de hablar de SVD conviene mirar el síntoma del sistema. El mismo array de antenas puede resolver problemas diferentes según cómo se use.

| Escenario | Síntoma de red | Estrategia MIMO natural | Costo o riesgo principal |
|---|---|---|---|
| Borde de celda rural | SNR baja, enlace frágil | Beamforming o diversidad | Subir rank demasiado rompe la robustez |
| Hotspot urbano | Muchos usuarios, interferencia alta | MU-MIMO con ZF/RZF y scheduler | CSI fresco y canales separables |
| Indoor / small cell | Canal rico, distancias cortas | SU-MIMO rank 2/4 | Antenas muy juntas reducen rank efectivo |
| Massive MIMO sub-6 GHz | Muchos UEs por celda | $M \gg K$, TDD, RZF/MRT | Pilotos, reciprocidad y contaminación |
| FR2 / mmWave | Path loss alto, haces estrechos | Arrays grandes y beamforming híbrido | Bloqueo, alineamiento de beams y RF chains |

<figure markdown="span">
  ![Mapa de decisión de estrategias MIMO según problema de red](figures/mimo-design-map.png)
  <!-- generada por generate_design_figures.py -->
  <figcaption markdown="1">**Figura 1.** Mapa de decisión para traducir un síntoma de red en una estrategia MIMO y en el costo operativo que debe vigilarse. Sirve como brújula antes de elegir rank, detector o precoder.
  </figcaption>
</figure>

Una regla práctica aparece desde el primer minuto:

!!! note "Regla de diseño"

    Primero se **cierra el enlace**; después se sube el rank. Si el UE apenas recibe señal, la prioridad es beamforming/diversidad. Si el enlace ya es robusto y el canal tiene modos espaciales independientes, entonces se explota multiplexación.

MIMO ofrece tres usos básicos:

- **Diversidad**: repetir o codificar la misma información sobre caminos independientes para reducir probabilidad de error.
- **Beamforming**: sumar señales con fases controladas para concentrar energía hacia un usuario o dirección.
- **Multiplexación espacial**: enviar capas distintas al mismo tiempo y en la misma banda para aumentar throughput.

La dificultad real es que esas tres metas compiten por los mismos grados de libertad espaciales. Un array no puede gastar todos sus recursos en robustez, máxima tasa y cancelación perfecta de interferencia a la vez.

??? question "Comprueba tu comprensión"

    **P1.** Un UE en borde de celda reporta bajo SNR y alto BLER. ¿Subirías rank o reforzarías beamforming/diversidad?

    **P2.** Dos usuarios tienen canales casi paralelos. ¿Es buen momento para servirlos simultáneamente con MU-MIMO?

    ---

    **R1.** Reforzaría beamforming/diversidad. Subir rank aumenta la carga espacial antes de cerrar el enlace.

    **R2.** No es ideal. Si los canales son casi paralelos, los dos usuarios "se ven iguales" desde la estación base: cualquier señal dirigida a uno llega casi idéntica al otro, y no hay geometría espacial que explotar. Separarlos espacialmente es posible pero caro (en §5 se verá cuánto cuesta); lo razonable es que el scheduler los sirva en tiempos o frecuencias distintas.

### 2. Qué arreglo de antenas usar

La Figura 2 muestra las configuraciones básicas. La lectura práctica no es "más antenas siempre es mejor", sino "qué extremo tiene antenas, quién conoce el canal y qué se quiere optimizar".

<figure markdown="span">
  ![Configuraciones SISO, SIMO, MISO y MIMO](figures/mimo-configurations.png)
  <!-- generada por celda 2 de lab.ipynb -->
  <figcaption markdown="1">**Figura 2.** Configuraciones de antenas. **SISO**: referencia escalar. **SIMO**: varias ramas de recepción para diversidad/combining. **MISO**: varias antenas transmisoras para formar haz hacia un receptor simple. **MIMO**: antenas en ambos extremos para diversidad, beamforming y/o multiplexación espacial.
  </figcaption>
</figure>

| Configuración | Dónde aparece | Cuándo usarla | Qué gana | Qué no resuelve |
|---|---|---|---|---|
| SIMO | Receptor con varias ramas | Mejorar recepción sin cambiar TX | Diversidad RX y combining | No crea múltiples capas si TX=1 |
| MISO | BS con varias antenas, UE simple | Cobertura downlink | Array gain y beamforming | No multiplexa varios streams a un UE de una antena |
| SU-MIMO | BS y UE multiantena | Throughput por usuario | Rank espacial y capas simultáneas | Exige canal bien condicionado |
| MU-MIMO | BS multiantena, varios UEs | Capacidad de celda | Reutilización espacial | Exige CSI y scheduler |
| Massive MIMO | $M$ mucho mayor que $K$ | Densidad y eficiencia energética | Hardening y canales casi ortogonales | Pilotos, TDD, correlación y contaminación |
| Híbrido mmWave | Arrays grandes con pocas cadenas RF | FR2/sub-THz | Ganancia de haz viable en hardware | Bloqueo y entrenamiento de beams |

Un punto de implementación que se olvida fácilmente: **antenas físicas no equivalen automáticamente a grados de libertad independientes**. Para que MIMO entregue multiplexación, las firmas espaciales deben ser distinguibles. Importan:

- separación de antenas, típicamente alrededor de $\lambda/2$;
- geometría del array: ULA, UPA, paneles activos;
- polarización;
- entorno de scattering;
- línea de vista y correlación espacial;
- orientación del UE.

En un teléfono pequeño, dos antenas pueden estar tan correlacionadas que el segundo modo espacial sea débil. En una estación base con muchos elementos, el problema opuesto aparece: hay muchas antenas, pero el sistema necesita CSI y calibración para usarlas bien.

!!! note "¿Y el espectro? Las capas no se reparten la banda"

    Los streams espaciales transmiten **al mismo tiempo y en la misma banda**. No se separan por subportadoras, slots ni códigos distintos. Se separan porque cada stream deja una firma espacial diferente en el receptor, codificada en las columnas de $\mathbf{H}$. Por eso MIMO puede aumentar throughput sin comprar más espectro, siempre que el canal tenga rank suficiente.

### 3. El canal como diagnóstico operativo

La matriz de canal no es solo notación. En un sistema real, $\mathbf{H}$ es el objeto que se estima con pilotos y del que salen decisiones de scheduler, rank, beamforming, precoding y detección.

Para un canal de banda estrecha:

$$\boxed{\mathbf{y} = \mathbf{H}\mathbf{x} + \mathbf{n}} \tag{1}$$

donde $\mathbf{x} \in \mathbb{C}^{N_t}$ es el vector transmitido, $\mathbf{y} \in \mathbb{C}^{N_r}$ el vector recibido, $\mathbf{H} \in \mathbb{C}^{N_r \times N_t}$ la matriz de canal y $\mathbf{n} \sim \mathcal{CN}(\mathbf{0}, N_0\mathbf{I})$ el ruido. La notación $\mathcal{CN}$ se lee "gaussiana compleja": cada antena receptora sufre un ruido con parte real e imaginaria gaussianas, de potencia total $N_0$, independiente del ruido de las demás antenas (eso dice la $\mathbf{I}$). Cada entrada $h_{ji}$ responde: cuánto de la antena TX $i$ llega a la antena RX $j$, con qué amplitud y fase.

<figure markdown="span">
  ![Estructura de la matriz de canal MIMO](figures/mimo-channel-matrix.png)
  <!-- generada por celda 3 de lab.ipynb -->
  <figcaption markdown="1">**Figura 3.** Matriz $\mathbf{H}$ para un sistema $4 \times 4$. Cada casilla contiene magnitud y fase del acoplamiento entre una antena transmisora y una receptora. Para implementación, esta matriz no es abstracta: es el insumo que estima el receptor o la estación base para decidir rank, precoder y detector.
  </figcaption>
</figure>

El modelo pedagógico más limpio es Rayleigh i.i.d.:

$$h_{ji} \sim \mathcal{CN}(0,1) \tag{2}$$

Significa dos cosas. **Independientes**: saber un coeficiente no predice los demás. **Idénticamente distribuidos**: todos los pares TX-RX siguen la misma estadística. Es un buen laboratorio mental para entender MIMO, aunque una red real usa modelos correlacionados como CDL (*Cluster Delay Line*) del TR 38.901 — el modelo de canal estándar de 3GPP, que en vez de coeficientes independientes describe grupos de trayectos físicos con sus retardos, ángulos de salida y llegada, y la geometría real del array.

En sistemas OFDM, esta ecuación vive por subportadora. MIMO-OFDM no tiene una sola matriz $\mathbf{H}$, sino una matriz $\mathbf{H}[k]$ por subportadora $k$. La Sesión 03 ya explicó cómo OFDM convierte un canal selectivo en frecuencia en muchos canales planos; aquí se decide qué hacer espacialmente en cada uno.

#### 3.1 Qué mirar dentro de H

| Indicador | Cómo se lee | Decisión de diseño |
|---|---|---|
| $\mathrm{rank}(\mathbf{H})$ | Número de modos espaciales útiles | Límite superior de capas simultáneas |
| Valores singulares $\sigma_k$ | Ganancia de cada modo espacial | Qué capas merecen potencia |
| Condicionamiento $\kappa = \sigma_1/\sigma_r$ | Desbalance entre modo fuerte y débil | Si ZF va a amplificar mucho ruido |
| Producto interno $\mathbf{h}_i^{\mathsf{H}}\mathbf{h}_j$ | Separabilidad entre usuarios | Si MU-MIMO simultáneo es razonable |
| Norma $\|\mathbf{h}_k\|^2$ | Fuerza del canal de un usuario | Scheduling, beamforming y power control |
| Tiempo de coherencia | Cuánto dura el CSI | Coste de pilotos y velocidad de adaptación |

Regla rápida para leer el condicionamiento: $\kappa \approx 1$ significa modos parejos, canal dócil para multiplexar; $\kappa \gtrsim 10$ significa que el modo débil es frágil y separarlo costará ruido o potencia; $\kappa \to \infty$ significa rank deficiente — hay menos modos útiles que antenas (el caso extremo es el canal *keyhole*, donde todos los trayectos pasan por un mismo "agujero" y $\kappa$ diverge).

La SVD aparece como herramienta de diagnóstico:

$$\mathbf{H} = \mathbf{U}\mathbf{\Sigma}\mathbf{V}^{\mathsf{H}} \tag{3}$$

La lectura implementativa es directa. Las columnas de $\mathbf{V}$ son direcciones de transmisión; las columnas de $\mathbf{U}$ son combinaciones de recepción; los valores singulares $\sigma_k$ dicen cuán bueno es cada modo. Si el segundo valor singular es pequeño, el segundo stream existe en álgebra, pero será caro en BER.

<figure markdown="span">
  ![SVD descompone H en canales paralelos](figures/mimo-svd-channels.png)
  <!-- generada por celda 5 de lab.ipynb -->
  <figcaption markdown="1">**Figura 4.** La SVD interpreta el canal MIMO como modos espaciales paralelos. En una lección implementativa, esto se usa como diagnóstico de rank y calidad de capas: no basta contar antenas; hay que mirar cuántos modos espaciales son fuertes.
  </figcaption>
</figure>

??? example "Ejemplo mínimo: canal 2×2 bien y mal condicionado"

    Canal con acoplamiento cruzado moderado:

    $$\mathbf{H} = \begin{pmatrix} 1 & 0{,}5 \\ 0{,}5 & 1 \end{pmatrix}$$

    Sus direcciones naturales son la señal en fase y en contrafase:

    $$\mathbf{v}_1 = \frac{1}{\sqrt{2}}\begin{pmatrix} 1 \\ 1 \end{pmatrix}, \qquad \mathbf{v}_2 = \frac{1}{\sqrt{2}}\begin{pmatrix} 1 \\ -1 \end{pmatrix}$$

    con valores singulares $\sigma_1 = 1{,}5$ y $\sigma_2 = 0{,}5$. La primera capa tiene ganancia $\sigma_1^2 = 2{,}25$; la segunda solo $\sigma_2^2 = 0{,}25$. El rank es 2, pero el canal ya avisa: la segunda capa será frágil y ZF pagará ruido para separarla.

    El chequeo de energía cuadra:

    $$\|\mathbf{H}\|_F^2 = 1^2 + 0{,}5^2 + 0{,}5^2 + 1^2 = 2{,}5 = 2{,}25 + 0{,}25$$

### 4. Diversidad, beamforming y multiplexación

Ahora podemos formular la decisión central. Con grados de libertad espaciales, ¿qué se optimiza?

| Modo de uso | Qué transmite | Cuándo conviene | Riesgo |
|---|---|---|---|
| Diversidad | Misma información por caminos independientes | Cobertura, baja SNR, enlace crítico | No aumenta throughput por capas |
| Beamforming | Señal alineada en fase hacia un usuario/dirección | Cobertura DL, FR2, UEs simples | Requiere CSI o búsqueda de haz |
| Multiplexación espacial | Capas distintas simultáneas | Alto SNR y buen rank | BER alta si el canal está mal condicionado |

Las tres filas de la tabla compiten por las mismas antenas: cada grado de libertad gastado en enviar una capa extra es un grado de libertad que ya no protege a las capas restantes. Esa es la tensión. La teoría clásica del *Diversity-Multiplexing Tradeoff* (DMT, compromiso diversidad-multiplexación) la vuelve medible con dos números:

- $r$ = **ganancia de multiplexación**: cuántas capas simultáneas efectivas transporta el sistema — cómo escala el throughput cuando sube el SNR;
- $d$ = **ganancia de diversidad**: cuántos caminos independientes protegen cada capa — qué tan rápido cae la probabilidad de error al subir el SNR (BER $\propto \text{SNR}^{-d}$: a mayor $d$, la curva de error cae más en picada).

Para un canal $N_t \times N_r$ i.i.d. Rayleigh, el mejor par $(r, d)$ alcanzable es:

$$d^*(r) = (N_t-r)(N_r-r), \quad r \in \{0,1,\ldots,\min(N_t,N_r)\} \tag{4}$$

La lectura práctica no es memorizar el límite, sino la pendiente del compromiso: cada capa adicional (sube $r$) resta caminos de protección (baja $d$). No se puede tener el máximo de ambos a la vez.

| Si el sistema ve... | Acción razonable | Por qué |
|---|---|---|
| SNR baja o borde de celda | Rank bajo + beamforming/diversidad | Primero cerrar enlace |
| SNR alta y valores singulares equilibrados | Subir rank | El canal soporta capas |
| Segundo valor singular muy débil | Bajar rank o usar más codificación | La capa extra cuesta demasiada BER |
| Usuarios casi ortogonales | MU-MIMO simultáneo | La interferencia espacial es baja |
| Usuarios casi paralelos | Scheduler o ZF/RZF con cuidado | Separarlos cuesta potencia y ruido |

??? example "Alamouti: diversidad plena sin CSIT"

    El ejemplo clásico de diversidad es el código de Alamouti 2×1. Dos antenas TX, una RX, dos ranuras temporales:

    | | Antena 1 | Antena 2 |
    |---|---|---|
    | Ranura 1 | $s_1$ | $s_2$ |
    | Ranura 2 | $-s_2^*$ | $s_1^*$ |

    Con canales $h_1, h_2$ constantes durante las dos ranuras:

    $$r_1 = h_1s_1 + h_2s_2 + n_1, \qquad r_2 = -h_1s_2^* + h_2s_1^* + n_2$$

    El receptor combina:

    $$\hat{s}_1 = h_1^*r_1 + h_2r_2^*, \qquad \hat{s}_2 = h_2^*r_1 - h_1r_2^*$$

    y los términos cruzados se cancelan:

    $$\hat{s}_k = (|h_1|^2 + |h_2|^2)s_k + \tilde{n}_k$$

    Cada símbolo aprovecha ambos trayectos. Para un enlace crítico, esta robustez puede valer más que una capa adicional.

<figure markdown="span">
  ![Curva DMT para sistemas 2×2, 4×4](figures/mimo-dmt.png)
  <!-- generada por celda 8 de lab.ipynb -->
  <figcaption markdown="1">**Figura 5.** Curva DMT para sistemas $2\times2$ y $4\times4$. En operación real se traduce como rank adaptation: el sistema sube capas cuando el canal y el SNR lo permiten, y baja capas cuando necesita robustez.
  </figcaption>
</figure>

### 5. Detección y precodificación que se implementan

Una vez elegido el uso del espacio, aparece el bloque de procesamiento: ¿quién separa la mezcla? ¿El receptor, el transmisor o ambos?

#### 5.1 Detección en el receptor

Si el transmisor no conoce $\mathbf{H}$, envía flujos y el receptor separa:

$$\mathbf{y} = \mathbf{H}\mathbf{x} + \mathbf{n}$$

| Detector | Idea | Ventaja | Costo |
|---|---|---|---|
| ZF | Invertir el canal con $\mathbf{H}^+$ | Cancela interferencia entre capas | Amplifica ruido si $\mathbf{H}$ está mal condicionada |
| MMSE | Invertir con regularización | Balancea ruido e interferencia | Requiere estimar SNR/ruido |
| SIC / V-BLAST | Detectar una capa, restarla y repetir | Mejor que lineal puro | Propagación de errores y ordenamiento |
| ML | Probar combinaciones de símbolos | Óptimo | Costo exponencial con $N_t$ |

??? example "Por qué ZF amplifica ruido"

    En el canal 2×2 del §3.1:

    $$\mathbf{H}^{\mathsf{H}}\mathbf{H} = \begin{pmatrix} 1{,}25 & 1 \\ 1 & 1{,}25 \end{pmatrix}$$

    y:

    $$(\mathbf{H}^{\mathsf{H}}\mathbf{H})^{-1} = \frac{1}{0{,}5625}\begin{pmatrix} 1{,}25 & -1 \\ -1 & 1{,}25 \end{pmatrix}$$

    La diagonal vale $1{,}25/0{,}5625 \approx 2{,}22$. ZF elimina interferencia, pero multiplica el ruido de cada flujo por 2,22. Esa es la razón operativa para preferir MMSE cuando el SNR no es alto o el canal está mal condicionado.

<figure markdown="span">
  ![BER de detectores ZF, MMSE y ML en canal 2×2](figures/mimo-detectors.png)
  <!-- generada por celda "Figura 4b" de lab.ipynb -->
  <figcaption markdown="1">**Figura 6.** BER de detectores ZF, MMSE y ML en un canal $2\times2$ con QPSK. La curva ilustra una decisión implementativa: ZF es barato pero paga ruido; MMSE suele ser el detector lineal práctico; ML sirve como referencia óptima pero no escala bien.
  </figcaption>
</figure>

#### 5.2 Precodificación en la estación base

En MU-MIMO downlink, la BS tiene $M$ antenas y sirve a $K$ usuarios:

$$\mathbf{y} = \mathbf{H}\mathbf{W}\mathbf{s} + \mathbf{n} \tag{5}$$

El usuario $k$ recibe:

$$y_k = \mathbf{h}_k^{\mathsf{H}}\mathbf{w}_ks_k + \sum_{j\neq k}\mathbf{h}_k^{\mathsf{H}}\mathbf{w}_js_j + n_k \tag{6}$$

La matriz $\mathbf{W}$ decide cuánta energía va al usuario deseado y cuánta interferencia cae sobre los demás.

| Precoder | Fórmula base | Cuándo usarlo | Costo |
|---|---|---|---|
| MRT | $\mathbf{W}\propto \mathbf{H}^{\mathsf{H}}$ | SNR baja, $M/K$ grande, canales casi ortogonales | No cancela interferencia |
| ZF | $\mathbf{W}=\mathbf{H}^{\mathsf{H}}(\mathbf{H}\mathbf{H}^{\mathsf{H}})^{-1}$ | Interferencia dominante, SNR alta, $M\geq K$ | Amplifica ruido y pierde potencia si canales son paralelos |
| RZF/MMSE | ZF regularizado | Caso práctico general | Necesita regularización y estimación de ruido |

<figure markdown="span">
  ![BER de MRT vs ZF para K=4 usuarios](figures/mimo-mrt-zf.png)
  <!-- generada por celda 10 de lab.ipynb -->
  <figcaption markdown="1">**Figura 7.** BER de MRT y ZF para $M=8$, $K=4$. A baja SNR, torcer haces con ZF no siempre compensa. A mayor SNR, MRT satura por interferencia y ZF cae sin piso. Esta es una decisión de diseño, no una preferencia estética.
  </figcaption>
</figure>

La dualidad es importante: ZF/MMSE aparecen tanto en receptor como en transmisor. Es la misma álgebra vista desde lados distintos. La decisión depende de dónde está el CSI, quién tiene capacidad de cómputo y qué extremo puede coordinarse.

### 6. Rank adaptation y capacidad útil

La capacidad MIMO sigue siendo el marco teórico que explica por qué subir capas puede aumentar throughput:

$$C = \sum_{k=1}^{r}\log_2\left(1 + \frac{P_k\sigma_k^2}{N_0}\right) \tag{7}$$

donde $P_k$ es la potencia asignada al modo espacial $k$ (sujeta a $\sum_k P_k = P_{\text{total}}$) y $r$ es el rank usado. La estructura lo dice todo: la capacidad total es la **suma de capacidades de canales SISO independientes**, uno por modo — cada término es la fórmula de Shannon de un tubo con ganancia $\sigma_k^2$.

Pero en implementación el sistema no calcula esta expresión para lucirse. La usa como intuición para rank adaptation:

1. medir o estimar calidad del canal;
2. mirar SNR, valores singulares, correlación e interferencia;
3. elegir cuántas capas enviar;
4. reportar o usar indicadores como CQI, RI y PMI;
5. verificar BLER objetivo después de la adaptación.

<figure markdown="span">
  ![Flujo de decisión para elegir rank, capas y precoder](figures/mimo-rank-precoder-flow.png)
  <!-- generada por generate_design_figures.py -->
  <figcaption markdown="1">**Figura 8.** Flujo de decisión para rank adaptation y selección de precoder. La ruta baja el rank si el enlace no cierra o si el segundo modo espacial es débil, y solo usa ZF/RZF cuando la interferencia domina y los canales son separables.
  </figcaption>
</figure>

<figure markdown="span">
  ![Capacidad MIMO vs SNR para diferentes configuraciones](figures/mimo-capacity.png)
  <!-- generada por celda 6 de lab.ipynb -->
  <figcaption markdown="1">**Figura 9.** Capacidad ergódica para $1\times1$, $2\times2$, $4\times4$ y $8\times8$. La lectura práctica: más antenas solo se convierten en throughput si el canal ofrece modos espaciales utilizables y el sistema puede estimarlos y explotarlos.
  </figcaption>
</figure>

??? example "Water-filling como criterio de apagado de capas"

    Si el transmisor conoce los valores singulares, puede repartir potencia con water-filling:

    $$P_k^* = \left(\mu - \frac{N_0}{\sigma_k^2}\right)^+$$

    donde $\mu$ es el "nivel del agua" — una constante que se ajusta hasta que las potencias asignadas suman la potencia total disponible — y $(x)^+ = \max(x, 0)$: un modo que queda "bajo el agua" recibe potencia cero, no potencia negativa.

    La idea implementativa es simple: un modo espacial muy débil no merece potencia. En un canal 3×3 con ganancias $\sigma_1^2=52$, $\sigma_2^2=13$, $\sigma_3^2=4$, todos los modos son fuertes y water-filling gana poco frente a potencia uniforme. En cambio, si un modo cae cerca de cero, el sistema debe bajar rank o asignarle cero potencia.

### 7. Massive MIMO como problema de red

Massive MIMO no es solo "muchas antenas". Es un régimen operativo: una estación base con $M$ antenas sirve a $K$ usuarios con $M \gg K$. Ese exceso de dimensiones espaciales cambia la ingeniería del sistema.

**Channel hardening.** La norma del canal de cada usuario se estabiliza:

$$\frac{\|\mathbf{h}_k\|^2}{M} \xrightarrow[M\to\infty]{\text{a.s.}} \beta_k \tag{8}$$

El fading rápido se promedia en muchas antenas. Para scheduling y control de enlace, el canal efectivo fluctúa menos.

**Favorable propagation.** Los canales de usuarios distintos tienden a ser ortogonales:

$$\frac{\mathbf{h}_k^{\mathsf{H}}\mathbf{h}_j}{M} \xrightarrow[M\to\infty]{\text{a.s.}} 0, \quad k\neq j \tag{9}$$

La interferencia de MRT disminuye sin invertir matrices. Por eso MRT se vuelve competitivo cuando $M/K$ es grande, aunque en sistemas reales RZF/MMSE suele ser más robusto.

<figure markdown="span">
  ![Channel hardening y favorable propagation vs M](figures/mimo-massive.png)
  <!-- generada por celdas 12–13 de lab.ipynb -->
  <figcaption markdown="1">**Figura 10.** Channel hardening y favorable propagation al aumentar $M$. Para el ingeniero, estas curvas dicen cuándo el exceso de antenas empieza a simplificar el precoding y estabilizar el enlace.
  </figcaption>
</figure>

#### 7.1 CSI: el cuello de botella

Todo lo anterior supone que la BS conoce el canal. Con $M$ grande, ese supuesto decide la arquitectura:

- En **FDD**, el UE tendría que estimar muchos canales de bajada y reportarlos. El overhead crece con el número de antenas y se vuelve caro.
- En **TDD**, los usuarios envían pilotos en subida; por reciprocidad, la BS estima el canal y lo reutiliza para precodificar en bajada. El coste escala con $K$, no con $M$.
- En una red multicelda, los pilotos se reutilizan. Si un usuario vecino usa el mismo piloto, contamina la estimación. Esa interferencia no desaparece simplemente añadiendo más antenas.

<figure markdown="span">
  ![Sobrecarga de CSI en FDD y TDD para Massive MIMO](figures/mimo-csi-overhead.png)
  <!-- generada por generate_design_figures.py -->
  <figcaption markdown="1">**Figura 11.** Sobrecarga de CSI para $K=8$ usuarios al crecer $M$. En FDD el coste de estimación y realimentación de canal de bajada crece con las antenas de la BS; en TDD el coste de pilotos queda ligado al número de usuarios.
  </figcaption>
</figure>

Por eso Massive MIMO práctico está profundamente ligado a TDD, calibración de reciprocidad, diseño de pilotos y scheduler.

<figure markdown="span">
  ![Sum-rate MRT vs ZF vs óptimo para Massive MIMO](figures/mimo-sumrate.png)
  <!-- generada por celda 14 de lab.ipynb -->
  <figcaption markdown="1">**Figura 12.** Sum-rate frente a número de antenas BS para $K=4$. La curva muestra una decisión de arquitectura: con pocas antenas ZF/RZF controla interferencia; con muchas antenas, MRT se aproxima al óptimo porque los canales se separan solos.
  </figcaption>
</figure>

#### 7.2 FR1, FR2 y beamforming híbrido

En FR1 sub-6 GHz, las configuraciones 32T32R, 64T64R o 128T128R permiten precoding digital amplio en estaciones base activas. En FR2/mmWave, una cadena RF por elemento es cara y consume demasiado. Por eso se usa **beamforming híbrido**: una etapa analógica forma haces gruesos con desfasadores, y una etapa digital de menor dimensión ajusta capas y usuarios.

La consecuencia para diseño es concreta: en FR2 no basta "usar Massive MIMO"; también hay que entrenar beams, seguir bloqueo, gestionar movilidad angular y decidir cuántas cadenas RF justifican el throughput esperado.

---

## Laboratorio

El laboratorio de esta sesión se puede leer como una serie de decisiones implementativas. El notebook sigue en:
[`lab.ipynb`](lab.ipynb)

1. **Diagnóstico de canal y rank**: generar matrices $\mathbf{H}$ Rayleigh, calcular SVD y observar distribución de valores singulares. Pregunta de diseño: ¿cuántas capas son razonables?
2. **Capacidad y rank adaptation**: comparar $1\times1$, $2\times2$, $4\times4$ y $8\times8$. Pregunta de diseño: ¿cuándo las antenas se convierten realmente en throughput?
3. **Detección ZF/MMSE/ML**: simular BER en un canal $2\times2$. Pregunta de diseño: ¿cuándo vale la pena pagar cómputo o regularización?
4. **Precodificadores MRT y ZF**: comparar BER para $M=8$, $K=4$. Pregunta de diseño: ¿cuándo domina ruido y cuándo domina interferencia?
5. **Massive MIMO**: barrer $M$ para observar hardening, favorable propagation y sum-rate. Pregunta de diseño: ¿a partir de qué $M/K$ el precoder simple empieza a funcionar?

Extensión natural para una versión futura del laboratorio: añadir un mini selector de rank que use SNR, valores singulares y BLER objetivo para decidir si transmitir 1, 2 o más capas.

---

## Ejercicios de Asimilación

Estos ejercicios están planteados como mini-casos de diseño. La meta es justificar decisiones, no solo sustituir números.

**Ejercicio A1 (borde de celda).** Un UE reporta bajo SNR y alto BLER. La BS puede usar 2 capas SU-MIMO o un haz de mayor ganancia con rank 1. ¿Qué eliges primero y por qué?

??? example "Solución"

    Elegiría rank 1 con beamforming/diversidad. Si el enlace no cierra, dos capas solo reparten potencia y hacen más frágil la detección. Primero se estabiliza el enlace; luego se intenta subir rank si el SNR y el canal lo permiten.

**Ejercicio A2 (rank y valores singulares).** Un canal 2×2 tiene $\sigma_1^2=2{,}25$ y $\sigma_2^2=0{,}25$. ¿El rank algebraico permite 2 capas? ¿El diseño debería usar siempre 2 capas?

??? example "Solución"

    El rank algebraico puede ser 2, pero la segunda capa es mucho más débil. A SNR alta quizá se use; a SNR baja o BLER alto conviene rank 1. La decisión no es contar antenas, sino mirar calidad de modos espaciales.

**Ejercicio A3 (usuarios paralelos).** Dos usuarios tienen canales con producto interno normalizado cercano a 1. ¿Los servirías juntos con MU-MIMO? ¿Qué alternativa tiene el scheduler?

??? example "Solución"

    No son buenos candidatos simultáneos: sus canales se pisan espacialmente. ZF puede separarlos, pero pagará potencia y ruido. El scheduler puede separarlos en tiempo/frecuencia y emparejar cada uno con otro usuario más ortogonal.

**Ejercicio A4 (MRT o ZF).** En un sistema $M=8$, $K=4$, a SNR muy baja, ZF no mejora la BER frente a MRT. ¿Por qué?

??? example "Solución"

    A SNR baja domina el ruido térmico. ZF elimina interferencia, pero al invertir un canal finito pierde ganancia útil y amplifica ruido. Si la interferencia aún no domina, ese pago no compensa. MMSE/RZF es el compromiso práctico.

**Ejercicio A5 (TDD frente a FDD).** Una BS tiene 128 antenas y sirve 8 usuarios. ¿Por qué TDD es más natural para Massive MIMO que FDD?

??? example "Solución"

    En FDD, estimar y reportar CSI de bajada escala con el número de antenas de la BS. En TDD, los 8 usuarios envían pilotos en subida y la BS usa reciprocidad para precodificar en bajada. El overhead escala con usuarios, no con antenas.

**Ejercicio A6 (FR2).** En mmWave, ¿por qué no basta decir "usemos 256 antenas digitales"?

??? example "Solución"

    Porque una cadena RF por antena es costosa y consume mucha potencia. FR2 usa arrays grandes para ganar link budget, pero suele implementar beamforming híbrido: fase analógica para formar haces y pocas cadenas digitales para multiplexación/precoding fino.

---

## Resumen

| Decisión | Indicador que miras | Acción típica |
|---|---|---|
| Cerrar cobertura | SNR, BLER, norma de canal | Beamforming, diversidad, rank bajo |
| Subir throughput por UE | Valores singulares, rank, SNR | SU-MIMO con más capas |
| Servir varios usuarios | Ortogonalidad entre canales, $M/K$ | MU-MIMO, scheduler, RZF/ZF |
| Elegir detector | Condicionamiento y SNR | MMSE si ZF amplifica ruido; ML solo como referencia o baja dimensión |
| Elegir precoder | Interferencia vs ruido | MRT para $M/K$ grande o SNR baja; ZF/RZF si interferencia domina |
| Escalar a Massive MIMO | Pilotos, TDD, reciprocidad | Estimar CSI por UL, controlar contaminación de pilotos |
| Usar FR2/mmWave | Path loss, bloqueo, RF chains | Beamforming híbrido y entrenamiento de haces |

La frase clave de la sesión: **MIMO no se diseña contando antenas; se diseña leyendo el canal y el problema de red**. Las fórmulas de SVD, capacidad y DMT explican por qué funcionan las decisiones, pero la tarea del ingeniero es escoger la estrategia correcta para el escenario correcto.
