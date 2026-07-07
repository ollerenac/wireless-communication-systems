# Analisis: reenfoque implementativo de Session 06 MIMO

## Diagnostico

El contenido actual es tecnicamente solido, pero esta optimizado para responder otra pregunta. Hoy la pregunta central es:

> Como se modela y se calcula la capacidad de un canal MIMO?

Para el publico descrito por el usuario, la pregunta central deberia ser:

> Tengo un problema de cobertura, capacidad, interferencia o densidad de usuarios. Que estrategia MIMO uso y que costo practico pago?

La diferencia no es cosmetica. Cambia el orden, los objetivos, los ejemplos y el laboratorio.

## Evidencia en el archivo actual

- Los objetivos actuales empiezan por matriz `H`, SVD, capacidad y DMT. Solo despues aparecen MRT/ZF y Massive MIMO.
- La seccion 3, "Capacidad MIMO via SVD", ocupa unas 200 lineas, mas que cualquier otra parte. Es el centro real de gravedad.
- Las decisiones practicas aparecen tarde y comprimidas: una tabla DMT en la seccion 4, una tabla MRT/ZF en la seccion 5, y un parrafo 5G NR en la seccion 6.
- El laboratorio implementa conceptos teoricos: SVD, capacidad ergodica, BER de precoders, hardening y favorable propagation. Falta un laboratorio de decision: elegir configuracion, rank, precoder y supuestos de CSI para un escenario.
- El resumen final todavia dice que la implicacion practica del modelo MIMO es "algebra lineal como herramienta principal". Para este curso, la implicacion practica deberia ser "las antenas son grados de libertad para cobertura, throughput, interferencia y densidad de usuarios".

## Que conservar

Hay material valioso que no conviene tirar:

- La intuicion de carriles/firmas espaciales y la aclaracion de que los streams comparten tiempo, frecuencia y banda.
- La matriz `H` como tabla de acoplamientos entre antenas. Es imprescindible para cualquier implementacion.
- La idea de rango, condicionamiento y valores singulares, pero como diagnostico de canal, no como primer destino de la clase.
- La comparacion ZF/MMSE/ML/SIC en receptor.
- La comparacion MRT/ZF/RZF-MMSE en transmisor.
- La parte TDD, pilotos y contamination, porque eso si es diseno de red real.
- Las figuras de BER, sum-rate y Massive MIMO, porque conectan algoritmo con efecto observable.

## Que comprimir o mover a apoyo

- La derivacion completa de SVD y la capacidad via water-filling no deberian ocupar el centro de la sesion. Deben pasar a una caja "matematica detras de la decision" o a una seccion opcional.
- El DMT formal con limites puede reducirse. Para el estudiante implementativo importa mas reconocer el eje diversidad vs multiplexacion que memorizar la definicion asintotica.
- El ejemplo 3x3 de water-filling se puede mantener como lectura avanzada. En una red real, el punto practico es mas simple: no todos los modos espaciales merecen potencia, y el rank efectivo cambia con SNR, correlacion y CSI.
- Los ejercicios de asimilacion deberian dejar de ser principalmente calculos de SVD/capacidad y pasar a mini-casos de decision.

## Nuevo enfoque recomendado

### Nuevo titulo sugerido

`Sesion 06 - MIMO en redes reales: cobertura, capacidad, beams y usuarios`

### Nueva tesis de apertura

MIMO no es "mas capacidad por algebra lineal". MIMO es una caja de herramientas para cuatro problemas de red:

1. **Cobertura**: hacer que el enlace sobreviva en borde de celda o SNR baja.
2. **Throughput**: enviar mas capas cuando el canal tiene rango suficiente.
3. **Interferencia**: separar usuarios o flujos que se pisan.
4. **Densidad**: servir muchos usuarios con una estacion base grande sin multiplicar potencia ni espectro.

La matematica entra como herramienta para decidir entre esas opciones.

## Nueva estructura propuesta

### 1. La decision de red: para que quiero mas antenas?

Abrir con cuatro escenarios concretos:

| Escenario | Sintoma | Estrategia MIMO natural | Riesgo |
|---|---|---|---|
| Borde de celda rural | SNR baja, enlace fragil | Diversidad / beamforming | No subir rank demasiado |
| Hotspot urbano | muchos usuarios, SINR limitado | MU-MIMO + ZF/RZF | CSI y correlacion espacial |
| Indoor/WiFi o small cell | canal rico, distancias cortas | SU-MIMO rank 2/4 | correlacion si antenas juntas |
| mmWave/FR2 | path loss alto, beams estrechos | arrays grandes + beamforming hibrido | bloqueo, alineamiento, RF chains |

Esta tabla deberia aparecer antes que la matriz `H`. El estudiante debe saber que problema esta intentando resolver antes de ver la herramienta.

### 2. Que arreglo de antenas usar?

Convertir SISO/SIMO/MISO/MIMO/Massive MIMO en una tabla de seleccion:

| Configuracion | Donde aparece | Cuando usarla | Que gana | Que no resuelve |
|---|---|---|---|---|
| SIMO | UE o receptor con varias ramas | mejorar recepcion sin tocar TX | diversidad RX | no aumenta streams si TX=1 |
| MISO | BS con varias antenas, UE simple | cobertura y beamforming DL | array gain | no multiplexa un UE solo |
| SU-MIMO | UE y BS multiantena | throughput por usuario | rank espacial | exige canal bien condicionado |
| MU-MIMO | BS multiantena, varios UEs | capacidad de celda | reutilizacion espacial | exige CSI y scheduler |
| Massive MIMO | M mucho mayor que K | densidad y eficiencia energetica | hardening, favorable propagation | pilotos, TDD, correlacion |
| Hibrido mmWave | arrays grandes con pocas RF chains | FR2/sub-THz | ganancia de haz | bloqueo y entrenamiento de beams |

Aqui tambien conviene introducir geometria de array: separacion `lambda/2`, ULA vs UPA, correlacion, orientacion, polarizacion, y por que antenas muy juntas no dan grados de libertad independientes.

### 3. El canal `H` como diagnostico, no como abstraccion

La matriz `H` debe explicarse como lo que el sistema estima para tomar decisiones:

- `rank(H)`: cuantas capas puedo intentar.
- `condition number`: si ZF va a amplificar ruido.
- correlacion entre columnas/filas: si las antenas o usuarios son realmente separables.
- normas de canal: quien tiene mejor enlace.
- tiempo de coherencia: cuanto cuesta mantener CSI fresco.

La SVD puede aparecer aqui, pero con rol de scanner del canal:

> La SVD no es el tema; es la herramienta que nos dice cuantos modos espaciales existen y que tan buenos son.

### 4. Tres modos de uso: diversidad, beamforming, multiplexacion

Unificar lo que hoy esta separado entre DMT, Alamouti, SVD y precoding.

- **Diversidad**: misma informacion por caminos independientes. Usar cuando la prioridad es confiabilidad.
- **Beamforming**: concentrar energia en una direccion/usuario. Usar cuando la prioridad es SNR o cobertura.
- **Multiplexacion espacial**: enviar capas distintas. Usar cuando hay rango, SNR y CSI suficientes.

La tabla DMT actual puede sobrevivir como "mapa mental", pero debe hablar en terminos de diseno:

| Si veo... | Hago... | Porque |
|---|---|---|
| SNR baja / borde de celda | rank bajo + diversidad/beamforming | primero cerrar enlace |
| canal con alto rank y buena SNR | subir rank | el canal soporta capas |
| usuarios con canales casi ortogonales | MU-MIMO con MRT/RZF | baja interferencia espacial |
| usuarios con canales paralelos | scheduling distinto o ZF caro | separarlos cuesta potencia |

### 5. Precodificacion y deteccion que si se implementan

Esta deberia ser una seccion central, no posterior a SVD/capacidad.

Organizarla como decisiones:

- Receptor sin ayuda del TX: ZF, MMSE, SIC, ML.
- BS con varios usuarios: MRT, ZF, RZF/MMSE.
- Criterios:
  - SNR baja: MMSE/RZF o MRT suelen ser mas robustos.
  - SNR alta e interferencia dominante: ZF/RZF.
  - `M/K` grande: MRT se vuelve competitivo.
  - canales mal condicionados: ZF paga ruido.
  - costo computacional alto: evitar ML y limitar inversiones grandes.

### 6. Massive MIMO como problema de red

Mantener hardening y favorable propagation, pero anclarlos en operaciones:

- Por que la BS puede usar pilotos UL en TDD.
- Por que FDD escala peor con muchos elementos.
- Por que el scheduler importa: no todos los usuarios son separables.
- Por que `M/K` no es solo una formula, sino margen para formar beams y controlar interferencia.
- Por que en FR2 se cambia a beamforming hibrido.

La seccion actual ya contiene estos elementos; hay que moverlos antes y expandirlos con casos.

### 7. La matematica detras de la decision

Cerrar o poner en cajas desplegables:

- modelo `y = Hx + n`;
- SVD y capacidad;
- water-filling;
- DMT formal.

Esto preserva rigor sin dejar que la derivacion controle la narrativa.

## Nuevos objetivos de aprendizaje sugeridos

Al finalizar la sesion, el estudiante deberia poder:

1. Elegir entre diversidad, beamforming, SU-MIMO, MU-MIMO y Massive MIMO segun SNR, interferencia, densidad de usuarios y disponibilidad de CSI.
2. Interpretar `H`, rank, condicionamiento, correlacion y `M/K` como indicadores de diseno.
3. Decidir cuando usar MRT, ZF o RZF/MMSE y explicar el costo de cada uno en ruido, interferencia y computo.
4. Explicar por que TDD, pilotos y reciprocidad son centrales en Massive MIMO.
5. Implementar una simulacion que compare decisiones de diseno, no solo curvas teoricas aisladas.

## Nuevo laboratorio recomendado

El laboratorio deberia empezar con escenarios, no con SVD:

1. **Escenario A - borde de celda**: SNR baja, un UE. Comparar diversidad/beamforming vs multiplexacion. Resultado esperado: rank bajo gana robustez.
2. **Escenario B - hotspot multiusuario**: `M=8`, `K=4`, canales con distinta correlacion. Comparar MRT, ZF y RZF. Resultado esperado: ZF ayuda si los usuarios son separables; si no, amplifica ruido.
3. **Escenario C - Massive MIMO**: barrer `M/K` y mostrar cuando MRT se acerca a ZF/RZF. Resultado esperado: la decision cambia con el exceso de antenas.
4. **Escenario D - overhead de CSI**: comparar costo de pilotos DL proporcional a `M` frente a pilotos UL proporcional a `K`. Resultado esperado: TDD es la razon operacional de Massive MIMO.
5. **Mini rank selector**: implementar una regla simple: subir rank si SNR supera umbral, valores singulares no estan demasiado desbalanceados y BER objetivo se mantiene.

Esto conectaria el notebook con decisiones que un ingeniero reconoce.

## Cambios concretos para `index.md`

1. Reescribir los objetivos y la introduccion.
2. Insertar al inicio una tabla "problema de red -> estrategia MIMO".
3. Mover parte de la SVD/capacidad a cajas desplegables o seccion final.
4. Elevar precodificacion, CSI y rank adaptation a temas centrales.
5. Rehacer los ejercicios de asimilacion como casos:
   - "UE en borde de celda: subir rank o beamforming?"
   - "Dos usuarios con canales casi paralelos: ZF o scheduler?"
   - "M=64, K=8: por que MRT empieza a funcionar?"
   - "FDD con 128 antenas: cual es el cuello de botella?"
6. Mantener ejemplos matematicos selectivos como respaldo, no como recorrido principal.

## Decision recomendada

Hacer una reescritura estructural, no una poda local. El contenido teorico actual debe convertirse en "motor explicativo" detras de decisiones de diseno. Si solo se anaden dos tablas practicas al texto actual, el curso seguira sintiendose teorico porque el orden narrativo seguira siendo: formula -> derivacion -> consecuencia. El nuevo orden debe ser: problema de red -> opcion de antenas -> costo practico -> modelo matematico que justifica la decision.
