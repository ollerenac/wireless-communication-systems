# Catálogo de ejercicios de simulación — Diseño de red 4G/5G

**Curso:** 3 clases × 3 h = 9 h. Prerrequisitos cubiertos: canal inalámbrico, OFDM, codificación de canal, MIMO.

**Entorno verificado:** Sionna 2.0.1 / Dr.Jit 1.3.1 / Mitsuba 3.8.0 sobre Ubuntu, backend LLVM (CPU),
sin GPU. Todos los tiempos de esta guía son medidos, no estimados. Ver `verificacion_entorno.json`.

**Instalación (Ubuntu 22.04):**

```bash
conda create -n ran-design python=3.12 numpy scipy matplotlib pandas -y
conda activate ran-design
pip install sionna sionna-rt      # arrastra torch, drjit, mitsuba
```

**Sionna 2.0.1 exige Python ≥ 3.11** (verificado en los metadatos del paquete), y Ubuntu
22.04 trae 3.10. Por eso no sirve `python3 -m venv`: `venv` reutiliza el intérprete del
sistema, no instala uno nuevo. Tres alternativas, ninguna requiere tocar el Python del
sistema:

```bash
# Opción A — uv (binario único, sin sudo, entorno dentro de la carpeta del curso)
curl -LsSf https://astral.sh/uv/install.sh | sh
uv venv --python 3.12 && source .venv/bin/activate
uv pip install sionna sionna-rt

# Opción B — Miniforge sin modificar el shell (el flag -b evita tocar ~/.bashrc)
bash Miniforge3-Linux-x86_64.sh -b -p ~/miniforge3
source ~/miniforge3/etc/profile.d/conda.sh
conda create -n ran-design python=3.12 -y && conda activate ran-design
pip install sionna sionna-rt

# Opción C — deadsnakes + venv (requiere sudo; instala 3.12 junto al 3.10 del sistema)
sudo add-apt-repository ppa:deadsnakes/ppa && sudo apt install python3.12 python3.12-venv
python3.12 -m venv ~/venvs/ran-design && source ~/venvs/ran-design/bin/activate
pip install sionna sionna-rt
```

Ni conda ni `uv` interfieren con los paquetes de Python que ya tenga el sistema: viven en
su propia carpeta y se desinstalan borrándola. En Ubuntu 24.04 (Python 3.12) basta con
`python3 -m venv`.

**Tamaño del entorno: 6.4 GB**, de los cuales **2.7 GB son librerías CUDA de NVIDIA** y
691 MB Triton — ambos inútiles sin GPU, los arrastra `torch` por defecto. Para reducirlo
sustancialmente, instalar primero la rueda de CPU:

```bash
pip install torch --index-url https://download.pytorch.org/whl/cpu
pip install sionna sionna-rt
```

(No pude medir el tamaño resultante: el dominio de PyTorch no es accesible desde mi
entorno. El ahorro debería rondar los 3 GB según el desglose de paquetes, pero conviene
confirmarlo antes de anunciarlo a los alumnos.)

Comprobación de que el backend CPU está activo:

```python
import drjit as dr
assert dr.has_backend(dr.JitBackend.LLVM)      # True en Ubuntu, ruedas de PyPI
print("CUDA:", dr.has_backend(dr.JitBackend.CUDA))   # False sin GPU, no importa
```

---

## Progresión pedagógica

El curso encadena las tres capas del diseño de red en el orden en que las hace un
ingeniero real:

| Clase | Pregunta de diseño | Capa | Herramienta |
|---|---|---|---|
| 1 | ¿Cuántos sitios necesito y con qué parámetros? | Enlace y celda aislada | NumPy + `sionna.sys.HexGrid` |
| 2 | ¿Dónde los pongo, sobre geometría real? | Celda con interferencia | `sionna.rt` |
| 3 | ¿Aguanta la carga de tráfico? | Red con scheduler y varios UE | `sionna.sys` |

**Regla de oro para el material:** cada ejercicio arranca de un resultado que el alumno
puede predecir con lápiz y papel, y termina en un resultado que solo la simulación revela.
Esa brecha es la lección.

---

# CLASE 1 — Dimensionado y presupuesto de enlace (3 h)

**Objetivo de aprendizaje.** Al final, el alumno calcula cuántos gNB necesita una zona
dada y justifica cada término del presupuesto de enlace con su origen físico o normativo.

**Por qué esta clase primero.** Es la única que no necesita simulación pesada: se resuelve
con álgebra. Pone el vocabulario (RSRP, SINR, MAPL, ISD, sectorización) que las otras dos
clases van a usar sin explicar.

### Ejercicio 1.1 — Presupuesto de enlace 4G vs 5G (45 min)

*Modalidad: NumPy puro, notebook. Sin Sionna. Tiempo de cómputo: instantáneo.*

El alumno construye una función de presupuesto de enlace de descenso y la evalúa en dos
configuraciones: LTE a 1.8 GHz con 20 MHz, y NR a 3.5 GHz con 100 MHz.

Términos a implementar:

```
EIRP           = P_tx + G_ant − L_alimentador
Sensibilidad   = −174 + 10·log10(BW_eficaz) + NF + SINR_objetivo
MAPL           = EIRP − Sensibilidad − margen_desvanecimiento − pérdida_penetración − ganancia_diversidad
```

**El punto que debe descubrir.** Al pasar de 1.8 a 3.5 GHz con la misma potencia, la
pérdida de propagación en espacio libre crece ~5.8 dB, pero el arreglo masivo de 5G
recupera esa pérdida y más. La pregunta guía: *¿cuánta ganancia de arreglo hace falta para
que 3.5 GHz cubra el mismo radio que 1.8 GHz?* La respuesta (≈6 dB, es decir un arreglo
4×4 frente a un 2×2) conecta directo con lo que ya saben de MIMO.

**Entregable.** Tabla comparativa de MAPL y radio de celda para las dos bandas, con el
término dominante identificado en cada una.

### Ejercicio 1.2 — De MAPL a número de sitios (50 min)

*Modalidad: NumPy + `sionna.sys.HexGrid`. Tiempo de cómputo: < 1 s.*

Invertir un modelo de pérdida 3GPP TR 38.901 (UMa/UMi) para pasar del MAPL al radio de
celda, y de ahí a conteo de sitios sobre una retícula hexagonal.

```python
from sionna.sys import HexGrid, gen_hexgrid_topology

hg = HexGrid(num_rings=2, isd=500.0, cell_height=30.0)
# num_rings=2  ->  19 celdas ;  cell_radius = 288.7 m para ISD = 500 m
print(hg.num_cells, float(hg.cell_radius))
```

Verificado: `num_rings=2` genera **19 celdas** y `cell_radius = 288.7 m` con ISD de 500 m.

Luego genera un escenario completo con usuarios:

```python
top = gen_hexgrid_topology(batch_size=1, num_rings=1, num_ut_per_sector=4,
                           scenario="umi", isd=400.0, bs_height=25.0)
ut_loc, bs_loc = top[0], top[1]   # (1, 84, 3) y (1, 21, 3): 21 sectores = 7 sitios × 3,
                                  # y 21 × 4 = 84 usuarios
```

**El punto que debe descubrir.** El conteo por cobertura y el conteo por capacidad dan
números distintos, y el diseño real toma el mayor de los dos. En zona rural manda
cobertura; en zona urbana densa manda capacidad. El alumno calcula ambos y descubre en qué
densidad de tráfico se cruzan las curvas.

**Entregable.** Gráfica de nº de sitios vs densidad de tráfico, con las dos curvas
(cobertura y capacidad) y el punto de cruce anotado.

### Ejercicio 1.3 — Sectorización y reutilización (40 min)

*Modalidad: NumPy analítico. Tiempo de cómputo: instantáneo.*

Calcular la SINR de borde de celda para configuraciones omnidireccional, 3 sectores y 6
sectores, usando un modelo de interferencia de primer anillo (6 interferentes dominantes).

**El punto que debe descubrir.** Sectorizar multiplica la capacidad por sector pero *no*
por el número de sectores: la interferencia intersectorial se come parte de la ganancia. El
alumno cuantifica esa pérdida y explica por qué 3 sectores es el estándar de la industria y
6 rara vez se justifica.

**Cierre de clase (25 min).** Discusión: los tres números que un operador te pide antes de
aprobar un diseño (nº de sitios, cobertura garantizada, throughput de borde de celda).

---

# CLASE 2 — Planificación sobre escenario real con trazado de rayos (3 h)

**Objetivo de aprendizaje.** El alumno ubica sitios sobre geometría urbana real, evalúa el
resultado con mapas de radio, y diagnostica los dos modos de falla de un despliegue:
agujeros de cobertura y zonas limitadas por interferencia.

**Por qué el trazado de rayos y no un modelo estadístico.** En Clase 1 el alumno usó un
modelo de pérdida promediado sobre muchos escenarios. Aquí ve el escenario concreto: la
sombra que proyecta un edificio específico no la predice ningún modelo estadístico.

### Ejercicio 2.1 — Primer mapa de radio (40 min)

*Modalidad: `sionna.rt`. Tiempo de cómputo verificado: 4.0 s con 4 vCPU.*

```python
from sionna.rt import load_scene, PlanarArray, Transmitter, RadioMapSolver, scene as scenes

sc = load_scene(scenes.munich, merge_shapes=True)
sc.frequency = 3.5e9
sc.tx_array = PlanarArray(num_rows=4, num_cols=4, vertical_spacing=0.5,
                          horizontal_spacing=0.5, pattern="tr38901", polarization="V")
sc.add(Transmitter(name="gnb0", position=[-100., 50., 40.], power_dbm=44.))

rms = RadioMapSolver()
rm = rms(sc, cell_size=(2., 2.), samples_per_tx=int(1e7), max_depth=5,
         diffuse_reflection=True)
```

**Advertencia crítica para el material:** el llenado del mapa depende fuertemente de
`samples_per_tx`. Con 1e7 rayos quedan huecos que el alumno puede confundir con agujeros de
cobertura reales. Para un mapa con 93 % de celdas cubiertas hacen falta **2e8 rayos con
`max_depth=8`**, y eso toma 76 s con 16 vCPU. Sugerencia didáctica: hacer que el alumno
corra primero con 1e6 y luego con 1e8, y que explique por qué cambia el mapa — es una
lección sobre convergencia de Monte Carlo, no un defecto de la herramienta.

**El punto que debe descubrir.** Los huecos por muestreo insuficiente y los huecos por
obstrucción real se distinguen aumentando los rayos: los primeros desaparecen, los segundos
no.

### Ejercicio 2.2 — Efecto de altura, tilt y frecuencia (55 min)

*Modalidad: `sionna.rt`, barrido paramétrico. Tiempo: ~4 s por corrida, 12 corridas ≈ 1 min.*

Barrido sistemático: altura de antena {15, 25, 40} m × frecuencia {700 MHz, 3.5 GHz} ×
inclinación eléctrica {0°, 6°, 12°}. Para cada combinación, extraer el percentil 5 de la
potencia recibida (cobertura de borde) y la fracción de área sobre −110 dBm.

**El punto que debe descubrir.** Subir la antena mejora la cobertura pero empeora la SINR
**en red densa**, porque la señal alcanza celdas vecinas como interferencia. La calificación
"en red densa" es esencial: en el escenario de 3 sitios del Ejercicio 2.3 este efecto no
aparece (verificado — ver la tabla de allí). Que el compromiso dependa de la densidad es
precisamente lo que prepara el terreno para el ejercicio siguiente.

**Entregable.** Superficie de decisión: para cada altura, la inclinación que maximiza el
percentil 5 de SINR — y una frase sobre en qué densidad de despliegue esa superficie
cambiaría de forma.

### Ejercicio 2.3 — Diagnóstico y rediseño de un despliegue de 3 sitios (60 min)

*Modalidad: `sionna.rt`, ejercicio de diseño abierto. Tiempo: ~4 s por iteración.*

Se entrega al alumno un despliegue deliberadamente subdimensionado — 3 gNB a 3.5 GHz,
44 dBm, arreglo 4×4, azoteas a 40 m sobre Múnich — con estas estadísticas verificadas:

| Métrica | p05 | p50 | p95 |
|---|---|---|---|
| Potencia recibida (dBm) | −102 | −73 | −39 |
| SINR de descenso (dB) | −16.0 | 5.9 | 28.6 |

Área sobre −110 dBm: **91 %**. Área con SINR positiva: **67 %**. Reparto: 9 % sin
cobertura, 24 % con potencia suficiente pero SINR negativa.

La tarea: mejorar la fracción con SINR positiva **sin agregar más de un sitio**.
Herramientas: reubicar, cambiar altura, ajustar inclinación, sectorizar, modificar potencia.

**Resultados verificados** (2×10⁸ rayos, `max_depth=8`, refracción y dispersión difusa):

| Palanca | SINR > 0 | vs. base |
|---|---|---|
| Entregado (3 sitios, 44 dBm) | 67.0 % | — |
| **+6 dB de potencia** | **74.9 %** | **+7.9 pp** |
| Inclinación 6° | 66.8 % | −0.2 pp |
| Inclinación 12° | 65.5 % | −1.5 pp |
| Cuarto sitio (44 dBm) | 71.8 % | +4.8 pp |
| 3 sitios a 50 dBm + inclinación 6° | 74.8 % | +7.8 pp |
| **4 sitios a 50 dBm** | **78.5 %** | **+11.5 pp** |

**El punto que debe descubrir — y es lo contrario de lo que dice el manual.** La regla de
memoria ("subir la potencia no mejora la SINR porque señal e interferencia crecen juntas")
vale **solo en redes limitadas por interferencia**. Con tres sitios repartidos sobre un
kilómetro cuadrado, buena parte del área tiene un servidor dominante y poca interferencia:
ahí el denominador de la SINR lo gobierna el **ruido**, y subir la potencia sí funciona
(+7.9 pp, medido).

La inclinación, en cambio, no mueve la aguja (−0.2 pp) **aunque su mecanismo físico
funcione perfectamente**: el perfil radial verificado con un solo transmisor muestra que a
20° la potencia cercana sube +4.5 dB y la lejana cae 13 dB. El haz se recoge como predice
la teoría — pero con celdas tan separadas, la energía que dejas de radiar lejos no estaba
interfiriendo a la vecina, estaba cubriendo tu propio borde de celda.

| Anillo | 0–100 m | 100–200 m | 200–400 m | 400–800 m |
|---|---|---|---|---|
| Inclinación 0° | −76.9 | −56.4 | −54.2 | −59.3 dBm |
| Inclinación 10° | −75.1 | −64.6 | −59.6 | −63.0 dBm |
| Inclinación 20° | −72.4 | −67.9 | −70.3 | −72.3 dBm |

**La lección es metodológica, no un resultado que memorizar:** identifica qué régimen
limita la red *antes* de elegir la palanca. Un alumno que aplica la regla de manual sin
verificar su condición previa llega a la conclusión equivocada — y en este escenario los
datos lo desmienten en 20 segundos de cómputo. Esto es más valioso que confirmarle una
regla que ya se sabe.

**Nota para el docente.** Si prefieres un escenario donde el *tilt* sí sea la palanca
dominante, hay que densificar bastante: siete sitios sobre la misma área no bastan
(probado). Haría falta reducir el área de estudio o subir a una decena de sitios con ISD
de 100–150 m. Mientras tanto, el escenario tal como está enseña algo mejor: que las reglas
tienen condiciones de validez.

**Entregable.** Informe de rediseño con el diagnóstico de régimen, la tabla de las tres
palancas medidas, los mapas antes/después y la justificación de cada cambio. Criterio de
evaluación: aplicar la regla de manual sin comprobar su condición previa suspende, aunque
el diseño final funcione.

### Cierre (25 min)
Planificación de PCI sobre el resultado: asignar identificadores de celda física evitando
colisión y confusión entre vecinos, sobre el despliegue que el propio alumno diseñó.

---

# CLASE 3 — Validación a nivel sistema (3 h)

**Objetivo de aprendizaje.** El alumno comprueba si el despliegue de Clase 2 aguanta
tráfico real, y entiende cómo scheduler, adaptación de enlace y control de potencia
convierten SINR en throughput.

**Por qué hace falta esta capa.** Clase 2 dio mapas de SINR. Pero SINR no es throughput: en
el medio hay abstracción de capa física, selección de MCS, HARQ y reparto de recursos entre
usuarios. Aquí el alumno cierra ese lazo.

### Ejercicio 3.1 — Abstracción de capa física (40 min)

*Modalidad: `sionna.sys.PHYAbstraction`. Tiempo: instantáneo.*

```python
from sionna.sys import PHYAbstraction
import torch

pa = PHYAbstraction()
mcs = torch.full((10,), 14, dtype=torch.int32)
nb, harq, sinr_eff, tbler, bler = pa(
    mcs_index=mcs, sinr=sinr,                      # sinr: [sym, sc, ut, streams]
    mcs_table_index=torch.ones(10, dtype=torch.int32),
    mcs_category=torch.zeros(10, dtype=torch.int32))
```

**Gotcha verificado:** `PHYAbstraction` devuelve una **tupla de 5 elementos** en este orden:
`(num_decoded_bits, harq, sinr_eff, tbler, bler)`. No está documentado de forma prominente y
es el primer tropiezo del alumno.

**El punto que debe descubrir.** El SINR efectivo por EESM no es el promedio del SINR por
subportadora. Un canal selectivo en frecuencia con el mismo SINR medio que un canal plano da
peor BLER. Los alumnos ya saben esto de la teoría de codificación de canal; aquí lo miden.

### Ejercicio 3.2 — Adaptación de enlace de lazo externo (55 min)

*Modalidad: `sionna.sys.OuterLoopLinkAdaptation`. Tiempo verificado: 0.6 s para 300 slots
× 10 UE — 2.1 ms por slot.*

```python
from sionna.sys import OuterLoopLinkAdaptation

olla = OuterLoopLinkAdaptation(phy_abstraction=pa, num_ut=10,
                               bler_target=0.1, delta_up=0.1)
sinr_eff_prev, harq_prev = None, None
for s in range(300):
    mcs_s = olla(num_allocated_re=n_re, harq_feedback=harq_prev,
                 sinr_eff=sinr_eff_prev, **kw)
    nb, harq_prev, sinr_eff_prev, tbler, bler = pa(mcs_index=mcs_s, sinr=sinr_s, **kw)
```

**Gotcha verificado y crítico:** `OuterLoopLinkAdaptation` **no tiene método `.update()`**.
La realimentación se cierra pasando `harq_feedback=` de vuelta al propio `__call__` en el
slot siguiente. Cualquier tutorial que sugiera `olla.update(...)` falla con `AttributeError`.
Documentar esto en el notebook ahorra 20 minutos de clase.

Resultado verificado con 10 UE en SINR de −2 a 22 dB: el lazo lleva el TBLER a ±5 puntos
porcentuales del objetivo de 10 % en **9 de 10 usuarios**. El décimo no converge porque
satura el MCS máximo (27) — su canal es tan bueno que ni el MCS más alto produce errores.

**El punto que debe descubrir.** Ese UE que no converge no es un fallo: es la señal de que
el usuario está limitado por la tabla de MCS y no por el canal. En una red real eso indica
que sobra SINR y se puede reasignar potencia a otro usuario — que es exactamente el
Ejercicio 3.4.

### Ejercicio 3.3 — Scheduler proporcional justo (45 min)

*Modalidad: `sionna.sys.PFSchedulerSUMIMO`. Tiempo: ~2 ms por slot.*

```python
from sionna.sys import PFSchedulerSUMIMO
sched = PFSchedulerSUMIMO(num_ut=10, num_freq_res=12, num_ofdm_sym=14, beta=0.98)
```

Comparar tres políticas sobre el mismo escenario: round-robin, máximo throughput, y
proporcional justo con distintos valores de `beta`.

**El punto que debe descubrir.** Máximo throughput maximiza la suma y deja al usuario de
borde sin servicio; round-robin es equitativo y desperdicia capacidad. El parámetro `beta`
del PF interpola entre ambos extremos. El alumno grafica la frontera de compromiso
throughput-equidad y elige un punto de operación justificándolo como operador.

### Ejercicio 3.4 — Control de potencia (35 min)

*Modalidad: `open_loop_uplink_power_control`, `downlink_fair_power_control`.*

```python
from sionna.sys import open_loop_uplink_power_control, downlink_fair_power_control

p_ul = open_loop_uplink_power_control(pathloss=pl, num_allocated_subcarriers=n_sc,
                                     alpha=0.8, p0_dbm=-90., ut_max_power_dbm=26.)
```

Barrer el factor de compensación parcial `alpha` de 0 a 1 en el ascenso.

**El punto que debe descubrir.** `alpha=1` compensa totalmente la pérdida de trayecto: todos
los usuarios llegan con la misma potencia, pero los lejanos generan mucha interferencia a
celdas vecinas. `alpha≈0.8` es el valor que usa la industria, y el alumno descubre por qué
con su propio barrido.

### Cierre del curso (25 min)
Arquitectura: 5G autónomo vs no autónomo, división de la RAN en unidades central,
distribuida y de radio, y segmentación de red. Se plantea como consecuencia de todo lo
anterior: *¿dónde conviene poner la frontera entre unidades si el enlace de retorno tiene
latencia limitada?*

---

## Notas de implementación para el agente que fabrique el material

**Tiempos de cómputo verificados** (Ubuntu, backend LLVM, sin GPU):

| Operación | 2 vCPU | 4 vCPU | 8 vCPU | 16 vCPU |
|---|---|---|---|---|
| Mapa de radio, 10M rayos, celda 2 m, dispersión difusa | 6.4 s | 4.0 s | 2.8 s | 2.7 s |
| Mapa de radio, 50M rayos, celda 5 m | 30.2 s | 20.4 s | 13.9 s | 11.7 s |
| Mapa de alta calidad, 200M rayos, `max_depth=8` | — | — | — | 75.7 s |
| Trazado de caminos, 3 TX × 6 RX, `max_depth=5` | — | 2.6 s | — | — |
| Bucle de sistema, 300 slots × 10 UE | — | — | — | 0.6 s |

Ningún ejercicio de este catálogo excede 80 s de cómputo. La clase no espera a la máquina.

**Gotchas de API que deben quedar documentados en los notebooks:**

1. `PHYAbstraction` devuelve `(num_decoded_bits, harq, sinr_eff, tbler, bler)` — tupla de 5.
2. `OuterLoopLinkAdaptation` no tiene `.update()`; realimentar vía `harq_feedback=`.
3. `EESM.call()` exige `mcs_index` además de `sinr`.
4. `paths.cir()` devuelve tuplas de listas, no tensores: indexar antes de `.numpy()`.
5. `dr.set_thread_count(n)` fija el paralelismo — útil para que todos los alumnos midan lo mismo.
6. El llenado del mapa de radio depende de `samples_per_tx`; huecos por muestreo ≠ huecos por obstrucción.
7. `Transmitter(orientation=...)` **rechaza `np.float64`**: `np.deg2rad(x)` devuelve ese tipo
   y falla con `TypeError: mitsuba.Point3f.__init__(): Item assignment failed`. Envolver
   siempre en `float(...)`. Lo mismo aplica a `position` y `power_dbm` si vienen de NumPy.
8. Las conclusiones cualitativas dependen del muestreo. Con 5×10⁷ rayos el escenario de 3
   sitios reporta 23.9 % sin cobertura; con 2×10⁸ baja a 9.2 %. Los rankings entre palancas
   se mantienen, pero las cifras absolutas de un informe deben usar el ajuste fino.

**Escenarios incluidos en Sionna RT:** `scenes.munich`, `scenes.etoile`, `scenes.florence`,
entre otros. No hace falta descargar geometría externa para las tres clases.

**Sobre GPU:** el código es idéntico con y sin GPU. Un alumno con NVIDIA puede instalar el
mismo paquete y obtener aceleración sin cambiar una línea del notebook. Si se distribuye una
máquina virtual, la GPU no se expone — lo cual tiene la ventaja didáctica de que todos los
alumnos miden los mismos tiempos.
