---
title: "Sesión 07 — Diseño de red de acceso 4G/5G sobre una ciudad real"
session: 7
description: "El flujo profesional de diseño de RAN — requisitos, espectro, cobertura, capacidad, plan nominal, parámetros y validación — ejecutado sobre una escena ray-traced de San Isidro, Lima."
---

# Sesión 07 — Diseño de red de acceso 4G/5G sobre una ciudad real

> **Página en construcción** — se escribe fase por fase junto con el
> notebook `design.ipynb`. Documento de trabajo: `brainstorming-diseno-red.md`.

## Objetivos de Aprendizaje

Al finalizar esta sesión, el estudiante será capaz de:

1. Traducir metas de negocio en requisitos técnicos medibles de una red de acceso (cobertura, calidad, capacidad, servicios).
2. Ejecutar el flujo profesional de diseño de RAN: espectro → dimensionamiento por cobertura → dimensionamiento por capacidad → plan nominal → planificación detallada → validación.
3. Justificar la elección de bandas 4G/5G según penetración, radio de celda y capacidad, sobre geometría urbana real.
4. Configurar y defender los parámetros que consumen los procedimientos de red: PCI, RACH, tracking areas, vecindades y umbrales de handover.
5. Validar un diseño con ray tracing (Sionna RT) sobre un escenario real y cerrar el lazo de optimización.

---

## El encargo

Un operador móvil te contrata para diseñar su red de acceso 5G en un
polígono de **San Isidro, Lima** — 1.32 × 0.83 km del distrito financiero.
Tienes licencia de 100 MHz en la banda n78 (3.5 GHz), azoteas disponibles
y un presupuesto limitado de sitios. La empresa quiere promesas que pueda
publicitar y cumplir.

Todo lo que sigue en esta sesión es resolver ese encargo con método.

---

## Fase 0 — Requisitos: el diseño empieza en números, no en antenas

Un requisito de red vale solo si es **medible**. "Buena cobertura" no es un
requisito; "RSRP ≥ −110 dBm en el 95% del área" sí, porque se puede verificar
con un mapa o un drive test y se puede firmar en un contrato.

### 0.1 Las tres métricas que gobiernan los requisitos de radio

- **RSRP** (*Reference Signal Received Power*): potencia recibida de la señal
  de referencia de la celda (en 5G, del SSB). Mide **cobertura de control**:
  ¿el UE encuentra la red y puede engancharse a ella? No dice nada de
  interferencia.
- **SINR**: señal sobre interferencia más ruido. Mide **calidad de datos**:
  ¿la señal sirve para transportar bits? Se puede tener RSRP excelente con
  SINR pésimo — típico en frontera de dos celdas sin coordinación.
- **RSRQ** (*Reference Signal Received Quality*): híbrido que relaciona RSRP
  con la potencia total recibida; útil para decidir handovers cuando RSRP
  solo no discrimina.

La pareja RSRP/SINR separa dos preguntas de diseño distintas: **cobertura**
(Fase 2) y **calidad/capacidad** (Fase 3). Confundirlas es el error clásico.

!!! info "Nota de profundización"

    La mecánica completa de las tres métricas — dónde viven en la grilla
    tiempo-frecuencia, el patrón de señales de referencia, EPRE, el techo
    estructural del RSRQ y las trampas de medición — está en
    [RSRP, RSRQ y SINR — nota de referencia](rsrp-rsrq-sinr.md). Aquí basta
    el nivel conceptual; la Fase 2 recurre a esa nota para calcular.

### 0.2 Por qué las metas son probabilísticas

La Sesión 01 mostró que la señal urbana es una variable aleatoria: el
shadowing log-normal hace que dos esquinas a la misma distancia de la BS
difieran 10–20 dB. Garantizar cobertura en el 100% del área exigiría
potencia/sitios infinitos — cada punto porcentual final cuesta más que todos
los anteriores. Por eso la industria diseña a probabilidad: **95% del área**
(o del borde de celda) con la métrica sobre el umbral, y un **margen de
shadowing** en el link budget que compra esa probabilidad.

### 0.3 De GB por mes a Mbps de hora cargada

La capacidad no se dimensiona para el promedio del día sino para la **hora
cargada** (*busy hour*). La conversión estándar:

$$R_{\text{usuario}} = \frac{V_{\text{mes}} \cdot f_{BH}}{30 \cdot 3600}$$

donde $V_{\text{mes}}$ es el volumen mensual por abonado (bits) y $f_{BH}$
la fracción del tráfico diario que cae en la hora cargada (típico 8–12%).

Ejemplo con números de Perú urbano: 10 GB/mes ≈ $2.7$ Gbit/día; con
$f_{BH} = 10\%$ → **~75 kbps sostenidos por abonado**. Parece poco — esa es
la magia de la multiplexión estadística: miles de usuarios que navegan a
ráfagas comparten la celda, y el diseñador dimensiona la suma, no los picos
individuales.

### 0.4 Requisitos del encargo

| # | Requisito | Meta | Se verifica con |
|---|---|---|---|
| R1 | Área de servicio | polígono de 1.1 km² (San Isidro) | — |
| R2 | Cobertura de control | RSRP ≥ −110 dBm en 95% del área | mapa RSS / drive test |
| R3 | Calidad de datos | SINR ≥ 0 dB en 90% del área | mapa SINR |
| R4 | Throughput de borde | p5 ≥ 50 Mbps DL, ≥ 5 Mbps UL | mapa de throughput |
| R5 | Capacidad agregada | ≥ 600 Mbps/km² en hora cargada | Fase 3 |
| R6 | Servicios | eMBB + VoNR, latencia de usuario < 20 ms | arquitectura/QoS |
| R7 | Espectro | 100 MHz TDD en n78 (3.5 GHz) | licencia (MTC) |
| R8 | Despliegue | solo azoteas existentes, máximo 6 sitios | plan nominal |

La cuenta detrás de R5: 25 000 personas/km² presentes en hora cargada
(distrito financiero) × 30% de participación de mercado × 75 kbps por
abonado ≈ 560 Mbps/km², redondeado a 600. Cada factor es una hipótesis de
negocio — cámbialos y cambia la red que hay que construir.

!!! question "Comprueba tu comprensión"

    **P1.** ¿Puede un punto del mapa cumplir R2 e incumplir R3 a la vez?
    ¿Qué lo causaría?

    **P2.** Si el market share sube al 45%, ¿qué requisitos cambian y qué
    fases del diseño hay que rehacer?

    ---

    **R1.** Sí: RSRP alto con SINR bajo — señal fuerte pero interferida,
    típico en fronteras de celda. Se cura con coordinación/tilts, no con
    más potencia.

    **R2.** Cambia R5 (∝ abonados). La cobertura (Fase 2) no se toca; el
    dimensionamiento por capacidad (Fase 3) y quizá el plan nominal (más
    sectores/sitios) sí.

---

## Fase 1 — Estrategia de espectro: la decisión que fija todas las demás

Antes de colocar un solo sitio hay que decidir **en qué frecuencia vive la
red**. Es la decisión más estructural del diseño: fija el radio de celda (y
por tanto cuántos sitios costará la cobertura), la penetración en interiores
y cuánta capacidad hay para vender. En nuestro encargo la licencia ya está
dada (R7: 100 MHz en n78) — pero hay que entender qué compramos y qué no.

### 1.1 La física: frecuencia contra alcance

La pérdida de espacio libre crece con $20\log_{10}(f)$: subir de banda cuesta
dB, y esos dB se pagan en radio de celda. Además, a mayor frecuencia peor
difracción (las esquinas "doblan" menos la señal) y peor penetración de
muros. Regla mental: **bajar una octava de frecuencia ≈ doblar el radio de
celda**.

Con el exponente de propagación urbano ($n \approx 3.8$), el delta de
pérdida se convierte en factor de área — y el factor de área, en sitios:

| Banda | $\Delta$ pérdida vs n78 | Radio relativo | Sitios para la misma área |
|---|---|---|---|
| 700 MHz (n28) | −14 dB | ×2.3 | ÷5.4 |
| 2.1 GHz (B4/n1) | −4.4 dB | ×1.3 | ÷1.7 |
| **3.5 GHz (n78)** | 0 (referencia) | ×1.0 | ×1.0 |
| 26 GHz (n258) | +17.4 dB | ×0.35 | ×8 |

Ya lo medimos sobre Lima real: mismos 3 sitios a 2.1 GHz cubren 74.6% del
área; a 3.5 GHz, 71.2% (`test_scene.ipynb`, Parte 5) — y eso que 2.1→3.5 es
el salto *chico* de la tabla.

### 1.2 Por qué entonces no todo es 700 MHz: capas de espectro

Porque el alcance se paga en capacidad: en low-band hay poco espectro (10–20
MHz por operador, y repartido); en mid-band hay bloques de 80–100 MHz. De ahí
la arquitectura de **capas** que usa todo operador real:

- **Capa de cobertura** (700/850/900 MHz): llega lejos y adentro; poco
  ancho de banda → sostiene voz, IoT y el "siempre conectado".
- **Capa de capacidad** (2.6/3.5 GHz): bloques anchos → sostiene el tráfico
  eMBB; celdas chicas → más sitios.
- **Capa de hotspot** (mmWave): enorme ancho de banda, alcance de cuadra;
  solo donde la densidad lo justifica.

Nuestro encargo es deliberadamente **mono-capa** (solo n78): más simple para
aprender, y realista para un despliegue 5G inicial. La comparación con una
capa de 700 MHz queda como extensión (requiere escena de 3×3 km — una celda
low-band tapa nuestra escena entera).

### 1.3 TDD: los 100 MHz no son todos tuyos todo el tiempo

n78 es TDD (Sesión 06: subida y bajada alternan sobre la misma frecuencia).
El tiempo se reparte con un patrón de slots; el típico en n78 es **DDDSU**:
de cada 5 slots, 3 son de bajada, 1 "especial" (mayormente bajada + guarda) y
1 de subida. Consecuencia aritmética que golpea el diseño:

- DL dispone de ≈ 71% del tiempo → **≈ 71 MHz "efectivos"** de los 100.
- UL dispone de ≈ 20% → **≈ 20 MHz efectivos** — y el UE ya era el extremo
  débil (23 dBm). El uplink pierde dos veces: en potencia y en tiempo.

El patrón TDD además debe estar **sincronizado entre operadores vecinos** de
la banda (lo coordina el regulador): si mi celda transmite DL mientras la
tuya escucha UL, mi potencia entierra a tus usuarios.

En FDD (las bandas bajas clásicas) esto no existe: DL y UL tienen cada uno su
frecuencia dedicada, tiempo completo.

### 1.4 Numerología: el detalle que conecta con OFDM

En n78 se usa subportadora de 30 kHz (Sesión 03: numerología µ=1): slots de
0.5 ms, CP de 2.3 µs — y ya verificamos sobre Lima que el delay spread urbano
(mediana 60 ns) cabe holgado en ese CP (`test_scene.ipynb`, Parte 8). La
numerología queda decidida por la banda y el estándar; no es una perilla de
esta clase.

### Decisión de la Fase 1 (lo que hereda el resto del diseño)

> Banda **n78 (3.5 GHz)**, **100 MHz** TDD con patrón **DDDSU** (≈71/20% 
> DL/UL), SCS 30 kHz. La Fase 2 dimensionará cobertura con la física de 3.5
> GHz; la Fase 3 repartirá 71/20 MHz efectivos contra la demanda de R5.

!!! question "Comprueba tu comprensión"

    **P1.** Un colega propone pedir al regulador cambiar la licencia a 20 MHz
    en 700 MHz "porque cubre 5 veces más área con los mismos sitios". ¿Qué
    requisito del encargo mata la propuesta?

    **P2.** ¿Por qué el patrón TDD de tu red no es 100% decisión tuya?

    ---

    **R1.** R5/R4: con 20 MHz no hay capacidad ni throughput de borde — la
    cobertura barata de low-band se paga en Mbps. (Cuenta rápida: 20 MHz ×
    ~74% DL deja ~15 MHz efectivos; ni la mediana de 50 Mbps se sostiene con
    carga.)

    **R2.** Debe sincronizarse con los demás operadores de la banda en la
    zona: patrones cruzados = interferencia DL→UL entre redes. Lo fija el
    regulador o el acuerdo inter-operador.

## Fase 2 — Dimensionamiento por cobertura: del presupuesto de dB al número de sitios

La pregunta de esta fase: **¿cuántos sitios necesita R2** (RSRP ≥ −110 dBm en
95% del área)**?** La herramienta es el *link budget*: una contabilidad en dB
donde cada ganancia suma, cada pérdida resta, y lo que queda es cuánto camino
puede recorrer la señal.

### 2.1 El punto de partida no es la potencia del amplificador

Error clásico: arrancar el presupuesto con "la BS transmite 44 dBm". Esos
44 dBm se reparten entre **todas** las subportadoras del canal. Con 100 MHz a
SCS 30 kHz hay 273 PRB × 12 = 3 276 subportadoras:

$$\text{EPRE} = 44 - 10\log_{10}(3276) \approx 44 - 35.2 = 8.8 \text{ dBm por RE}$$

Como el RSRP se mide **por resource element** (ver la
[nota de referencia](rsrp-rsrq-sinr.md)), el link budget de cobertura de
control empieza en 8.8 dBm, no en 44. La red incluso difunde este número
(`referenceSignalPower` en el SIB) para que el UE pueda despejar el path
loss.

### 2.2 El presupuesto término a término

$$\text{RSRP}_{\text{borde}} = \underbrace{\text{EPRE}}_{8.8} + \underbrace{G_{tx}}_{+16} - \underbrace{\text{PL}}_{?} - \underbrace{M_{\text{shadow}}}_{9} \geq -110 \text{ dBm}$$

| Término | Valor | De dónde sale |
|---|---|---|
| EPRE | 8.8 dBm | 44 dBm ÷ 3 276 subportadoras |
| $G_{tx}$ | +16 dBi | antena sectorial macro típica |
| $M_{\text{shadow}}$ | −9 dB | compra el 95% de área con shadowing log-normal $\sigma = 8$ dB |
| $G_{rx}$, pérdidas de cuerpo/cable | 0 dB neto | UE: antena ~0 dBi; simplificación explícita |

Despejando: la señal puede perder hasta

$$\text{MAPL} = 8.8 + 16 + 110 - 9 \approx 126 \text{ dB}$$

**MAPL** (*Maximum Allowable Path Loss*) es el número que resume toda la
fase: el presupuesto de pérdida que el trayecto no debe superar.

El margen de shadowing es donde la meta probabilística de la Fase 0 se
vuelve un número: con $\sigma = 8$ dB, reservar ~9 dB garantiza que el ~95%
del área (no solo el punto medio) quede sobre el umbral. Más probabilidad =
más margen = menos radio: la certeza se paga en dB.

### 2.3 De MAPL a radio: el modelo de propagación

El MAPL se convierte en distancia invirtiendo un modelo. El estándar de la
industria sin escena 3D es el **UMa NLOS de 3GPP TR 38.901**:

$$\text{PL} = 13.54 + 39.08\log_{10}(d) + 20\log_{10}(f_c) \quad [\text{d en m, } f_c \text{ en GHz}]$$

Con 126 dB y $f_c = 3.5$: $d \approx 390$ m — coherente con la tabla de la
Fase 1 (n78: 200–500 m urbano).

Cada sitio trisectorial cubre un hexágono de área $\approx 2.6\,r^2$:

$$N_{\text{sitios}} = \frac{1.1 \text{ km}^2}{2.6 \times 0.39^2 \text{ km}^2} \approx 3 \text{ sitios por cobertura}$$

**Tres sitios** — coherente con el esbozo (`test_scene.ipynb`) que con 3 BS
logró ~71% de SINR > 0: la cobertura de control alcanza, la calidad todavía
no. La fórmula da el *orden de magnitud*; el ray tracing sobre la escena
real (Fase 6) da la verdad calle por calle. Ambos se necesitan: la fórmula
para dimensionar sin escena, el trazador para validar con ella.

### 2.4 El enlace de vuelta: uplink

El mismo ejercicio con el UE como transmisor: 23 dBm sobre sus PRBs
asignados (no per-RE de 100 MHz — el UE concentra su potencia en pocos PRB,
su gran defensa), antena de 0 dBi, y la BS escuchando con NF de 5 dB. El
enlace que soporte **menos** pérdida define el radio real de la celda: de
nada sirve que el UE oiga a la BS si la BS no lo oye de vuelta. La cuenta
completa está en `design.ipynb`; el resultado con nuestros números: DL de
control y UL de datos quedan sorprendentemente parejos (~126 vs ~130 dB) —
precisamente porque el UE concentra y la BS reparte.

### 2.5 RSS → RSRP: cerrar el círculo con Sionna

Los radio maps de Sionna entregan potencia de banda ancha (RSS). Para
verificar R2 hay que convertir: restar $10\log_{10}(N_{\text{RE}})$ del
despliegue. Es la misma cuenta del EPRE vista del lado del receptor — y el
motivo por el que la meta R2 no puede compararse directo contra el mapa
crudo. La verificación numérica vive en `design.ipynb`.

!!! question "Comprueba tu comprensión"

    **P1.** El operador propone duplicar el ancho de banda a 200 MHz "para
    duplicar capacidad" manteniendo los 44 dBm. ¿Qué pasa con la cobertura?

    **P2.** ¿Por qué el margen de shadowing no se puede eliminar "midiendo
    mejor el canal"?

    ---

    **R1.** El EPRE cae 3 dB (misma potencia entre el doble de
    subportadoras) → el RSRP cae 3 dB en todo punto → el MAPL pierde 3 dB →
    el radio se encoge ~16% y hacen falta ~40% más sitios. La capacidad
    también se paga en cobertura.

    **R2.** Porque no es error de medición: es la variabilidad *física* del
    entorno (qué edificios estorban en cada punto). Se puede mapear con ray
    tracing punto a punto, pero al diseñar con un modelo estadístico, la
    incertidumbre espacial es irreducible y hay que presupuestarla.

## Fase 3 — Dimensionamiento por capacidad *(en construcción)*

## Fase 4 — Plan nominal *(en construcción)*

## Fase 5 — Planificación detallada y procedimientos *(en construcción)*

## Fase 6 — Validación y optimización *(en construcción)*
