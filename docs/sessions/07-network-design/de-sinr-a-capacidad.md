# De la distribución de SINR a la capacidad de celda — nota de referencia

> El error que esta nota mata: dimensionar con el throughput *pico* ("5G da
> 1 Gbps") o con el SINR de *un* punto. Una celda sirve a usuarios repartidos
> por toda su área: su capacidad es una **propiedad estadística de la
> distribución espacial de SINR** — y de cómo el scheduler reparte el tiempo.

*Nota de profundización de la [Sesión 07](index.md) §Fase 3. Las advertencias
sobre Shannon (lineal vs dB, factor α, techo de MCS) están en la
[nota de RSRP/RSRQ/SINR](rsrp-rsrq-sinr.md) §3 y aquí se dan por sabidas.*

---

## 1. El pico no dimensiona nada

El folleto dice "hasta 1.2 Gbps". Ese número corresponde a UN usuario pegado
a la antena, con SINR > 22 dB, todos los PRBs para él y 4 capas MIMO. En la
celda real:

- la mayoría de los usuarios está lejos del pico de SINR;
- todos **comparten** los mismos PRBs;
- el scheduler decide quién transmite en cada TTI.

La capacidad vendible de la celda es el throughput **agregado sostenido** con
usuarios repartidos — típicamente 5 a 10 veces menos que el pico del
folleto. Dimensionar con el pico = construir una red que se cae en hora
cargada.

## 2. La celda como promedio espacial

Cada punto $x$ del área de la celda tiene su SINR (el mapa de la Fase 6 lo
da medido; un modelo estadístico lo da aproximado). Cada SINR se traduce a
eficiencia espectral:

$$\text{SE}(x) = \min\!\big(\alpha \log_2(1 + \text{SINR}(x)),\ \text{SE}_{\max}\big)$$

con $\alpha \approx 0.7$ (overhead de implementación) y
$\text{SE}_{\max} \approx 7.4$ bit/s/Hz (techo de 256-QAM). La pregunta es:
¿qué **promedio** de $\text{SE}(x)$ representa a la celda? Depende de una
decisión que no es matemática sino de **política de reparto**.

## 3. El concepto difícil: qué media usa tu scheduler

Supón dos usuarios: A cerca (SE = 6 bit/s/Hz) y B en el borde
(SE = 0.6 bit/s/Hz). Un solo canal de $B$ Hz. Dos políticas:

### Política "mismo tiempo para todos" (round robin temporal)

Cada usuario recibe la mitad de los TTIs. Throughput de celda:

$$R_{\text{celda}} = B \cdot \frac{\text{SE}_A + \text{SE}_B}{2} = B \cdot 3.3 \text{ bit/s/Hz}$$

La celda rinde la **media aritmética** de las eficiencias. El usuario de
borde recibe pocos bits, pero no arrastra a la celda.

### Política "mismos gigas para todos" (reparto igualitario de datos)

Para entregar los mismos bits a ambos, B necesita 10 veces más tiempo que A.
El throughput de celda colapsa hacia la **media armónica**:

$$R_{\text{celda}} = B \cdot \frac{2}{\frac{1}{\text{SE}_A} + \frac{1}{\text{SE}_B}} = B \cdot 1.09 \text{ bit/s/Hz}$$

**Tres veces menos celda, mismos usuarios, mismo canal.** El usuario de borde
consume el recurso escaso (tiempo) a tasa de borde, y la celda entera paga.

### La regla

> La media aritmética espacial es el **techo** del scheduler equitativo en
> tiempo; la media armónica es el **piso** del reparto igualitario de datos.
> Los schedulers reales (*proportional fair*) viven entre ambas, más cerca de
> la aritmética, y ganan un extra explotando el fading (sirven a cada usuario
> en sus picos — *multiuser diversity*).

Para dimensionar se usa la media aritmética espacial con $\alpha$
conservador — y se declara la hipótesis.

## 4. Del bit/s/Hz a los Mbps de celda

$$R_{\text{celda}} = \text{SE}_{\text{celda}} \times B_{\text{efectivo}} \times (1 - OH)$$

- $B_{\text{efectivo}}$: en TDD, la fracción DL del canal (Fase 1: 71 de
  100 MHz con DDDSU).
- $OH \approx 20\text{–}25\%$: PRBs que no llevan datos de usuario — SSB,
  PDCCH, DMRS, TRS, mensajes del sistema. Se paga *antes* de vender un bit.

Ejemplo con números del encargo: $\text{SE}_{\text{celda}} = 2.0$ bit/s/Hz
(conservador SISO, ver §6) → $2.0 \times 71 \text{ MHz} \times 0.78 \approx
111$ Mbps por celda, $\times 3$ sectores $\approx 330$ Mbps por sitio.

## 5. El acople carga↔interferencia (por qué se dimensiona a plena carga)

El SINR de mi celda depende de cuánto transmiten las vecinas — y cuánto
transmiten depende de su carga. Círculo:

- Red vacía → vecinas callan → SINR alto → celdas rinden más.
- Hora cargada → todas transmiten → SINR cae → justo cuando más se necesita.

Por eso el mapa de SINR de diseño se calcula **full-buffer** (todas las
celdas transmitiendo siempre): es el peor caso, y es el caso de la hora
cargada, que es la única hora que importa para dimensionar. Un mapa medido
en hora valle es propaganda.

## 6. De dónde sale la SE de celda en la práctica

| Fuente | Cuándo se usa | Nuestro caso |
|---|---|---|
| Valores de industria (2–2.5 SISO, 4–7 con MU-MIMO) | diseño sin escena | hipótesis inicial: **2.0** |
| Integral del mapa SINR (modelo estadístico) | planificación nominal | — |
| Integral del mapa SINR **medido/ray-traced** | validación | Fase 6: reemplaza la hipótesis con el mapa de San Isidro |

La hipótesis se declara, se apunta, y se reemplaza cuando hay mapa. Diseñar
es iterar sobre hipótesis explícitas, no adivinar bien a la primera.
