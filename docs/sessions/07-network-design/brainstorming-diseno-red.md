# Diseño de red de acceso 4G/5G — directrices y brainstorming

> **Documento de trabajo** (no es la clase). Aquí se acumulan las directrices
> generales del diseño de red, el mapeo contra lo que ya construimos en
> `test_scene.ipynb`, y las preguntas abiertas que vamos resolviendo en el
> bucle de estudio. De aquí sale el `index.md` de la sesión.

---

## 1. El flujo real de diseño de una red de acceso

Un diseño profesional de RAN sigue siempre el mismo esqueleto de fases. Cada
fase consume las salidas de la anterior; saltarse una se paga en la siguiente.

### Fase 0 — Requisitos (lo que el cliente/negocio fija)

| Insumo | Ejemplo típico | Pregunta que responde |
|---|---|---|
| Área de servicio | polígono urbano de 2 km² | ¿dónde? |
| Meta de cobertura | 95% del área con RSRP > −110 dBm | ¿con qué probabilidad hay señal? |
| Meta de calidad | SINR > 0 dB en 90%, BLER < 10% | ¿la señal sirve? |
| Meta de capacidad | X usuarios, Y GB/mes, hora cargada | ¿aguanta a todos a la vez? |
| Servicios | eMBB, voz, IoT, URLLC | ¿qué tipo de tráfico? |
| Regulatorio | bandas licenciadas, límite EIRP (MTC en Perú) | ¿qué está permitido? |
| Presupuesto/sitios | azoteas disponibles, torres, fibra | ¿dónde se puede construir? |

**Lección clave**: el diseño no empieza en la antena — empieza en metas
numéricas. Sin meta, "cobertura buena" no significa nada.

### Fase 1 — Estrategia de espectro

Elegir banda(s) es la decisión más estructural: fija el radio de celda, la
penetración indoor y la capacidad disponible. Ver §2.

### Fase 2 — Dimensionamiento por cobertura

1. **Link budget** por servicio: potencias, ganancias, ruido, márgenes
   (shadowing, penetración de edificio, cuerpo) → MAPL (máxima pérdida de
   trayecto admisible).
2. MAPL + modelo de propagación → **radio de celda** → **número de sitios
   por cobertura**. El enlace limitante suele ser el **uplink** (ya lo vimos:
   Parte 6 del notebook).

### Fase 3 — Dimensionamiento por capacidad

1. Modelo de tráfico: usuarios/km², demanda por usuario en hora cargada.
2. Eficiencia espectral media de celda (bit/s/Hz, depende de la distribución
   de SINR) × ancho de banda → **capacidad por celda**.
3. Demanda ÷ capacidad → **número de sitios por capacidad**.

**El número final de sitios es max(cobertura, capacidad)** — ciudades densas
terminan limitadas por capacidad; zonas rurales, por cobertura.

### Fase 4 — Plan nominal (radio planning)

Colocar sitios en el mapa real: posiciones candidatas (azoteas viables),
sectorización (típico 3 sectores × 120°), azimuts, alturas, tilts, potencias.
Es la fase que iteramos a mano en el notebook con el dict `sites`.

### Fase 5 — Planificación detallada (los "números de la red")

Los parámetros que hacen que los procedimientos funcionen:

| Parámetro | Procedimiento que lo consume | Regla de diseño |
|---|---|---|
| PCI (identidad física de celda) | búsqueda de celda | sin colisión (vecinas ≠ PCI) ni confusión (dos vecinas de una misma celda con igual PCI); cuidar mod 3 / mod 30 |
| Raíces de preámbulo RACH | acceso aleatorio | zona de contención ≥ radio de celda; sin reuso entre vecinas |
| TAC / tracking areas | paging y TAU | TA grande = menos actualizaciones pero más carga de paging; equilibrio |
| Listas de vecinas / ANR | handover | completas pero sin basura (vecinas falsas = HOs fallidos) |
| A3 offset, histéresis, TTT | handover | ya medido en Parte 4: sin histéresis = ping-pong |
| Potencia SSB/pilotos, tilt | todo lo anterior | cobertura del canal de control ≠ cobertura de datos |

### Fase 6 — Validación y optimización (el lazo cerrado)

Predicción (ray tracing / herramienta de planificación) → despliegue →
**drive test** real → comparar con predicción → ajustar (tilt, potencia,
vecindades, parámetros HO) → repetir. En operación continua esto es SON
(self-organizing networks). Nuestra Parte 4 es un drive test *virtual*: la
predicción del lazo.

---

## 2. Bandas en Perú y por qué importa el mapa

La penetración a través de obstáculos cae con la frecuencia — misma ciudad,
radios de celda completamente distintos:

| Banda | Tecnología típica | Radio urbano aprox. | Rol |
|---|---|---|---|
| 700 MHz (B28/n28) | 4G, capa de cobertura 5G | 1–2 km | cobertura, indoor profundo, IoT |
| 1900 MHz (B2) | 4G | 500 m – 1 km | capa media histórica |
| AWS 1.7/2.1 GHz (B4) | 4G | 400–800 m | capacidad 4G |
| 2.6 GHz (B7) | 4G | 300–600 m | capacidad 4G urbana |
| 3.5 GHz (n78) | 5G | 200–500 m | capacidad 5G (nuestro caso actual) |
| 26 GHz (n258) | 5G mmWave | 50–200 m, LoS casi obligatorio | hotspots (futuro en Perú) |

Regla mental: **bajar un octavo de frecuencia ≈ doblar el radio**. Y ya lo
medimos: 2.1 vs 3.5 GHz con los mismos sitios = 3.4 puntos de cobertura
(Parte 5) — y eso que 2.1→3.5 es un salto chico.

### Dimensión de escena recomendada por banda

Criterio: la escena debe contener **varias celdas completas** de la banda
estudiada (si no, no hay interferencia ni fronteras reales), pero el costo de
ray tracing y el peso de la malla crecen con el área.

| Banda a estudiar | Radio de celda | Escena recomendada | ¿La actual (1.3 × 0.8 km) sirve? |
|---|---|---|---|
| 3.5 GHz | 200–500 m | 1.5 × 1.5 km | **Sí** — es nuestro caso |
| 26 GHz | < 200 m | 1 × 1 km basta | Sí, sobra |
| 2.1/2.6 GHz | 400–800 m | 2 × 2 km | Ajustada (celdas se salen) |
| 700 MHz | 1–2 km | **3 × 3 a 4 × 4 km** | **No** — una sola celda taparía toda la escena |

**Recomendación concreta**: mantener la escena actual de San Isidro para n78
y mmWave, y descargar UNA escena adicional de ~3 × 3 km para la comparación
low-band vs mid-band. Límites prácticos: en Blosm el área grande tarda y
Overpass puede cortar la descarga (bajar por tiles si falla); la malla crecerá
a decenas de MB y cada radio map a 10⁶ rayos pasará de minutos a decenas de
minutos en CPU. Para la escena grande: `cell_size` de 10–20 m en vez de 5 m
compensa el costo.

---

## 3. Dónde estamos: mapeo del flujo contra el notebook

| Fase del diseño | Estado | Dónde |
|---|---|---|
| 0. Requisitos | implícitos (meta 95% SINR>0) — **formalizar** | — |
| 1. Espectro | comparación 2.1 vs 3.5 hecha; falta 700 MHz | Parte 5 |
| 2. Cobertura | mapas RSS/SINR, uplink limitante | Partes 2, 6 |
| 3. Capacidad | **falta** — no hay modelo de tráfico | pendiente |
| 4. Plan nominal | manual con `sites`; falta sectorización 3×120°, tilts | Partes 2, 7 |
| 5. Detallada | solo A3/histéresis; faltan PCI, RACH, TAC, vecinas | Parte 4 |
| 6. Validación | drive test virtual, densificación | Partes 4, 7 |

Lo que el notebook ya enseña sin decirlo: el lazo explorar→medir→corregir de
la Fase 6, y que el diseño es iterativo, no una fórmula cerrada.

---

## 4. Preguntas abiertas (el brainstorming vivo)

Decisiones pendientes de conversación — se van resolviendo y anotando aquí:

- [ ] **Escenario ancla de la clase**: ¿operador urbano (San Isidro, lo
  actual) o red privada/campus? ¿O el urbano como hilo y campus como tarea?
- [ ] **Metas numéricas oficiales del ejercicio**: ¿95% SINR > 0 dB se queda?
  ¿Agregamos meta de RSRP (cobertura de control) y de throughput de borde
  (p5 > 50 Mbps)?
- [ ] **Modelo de tráfico para la Fase 3**: ¿algo simple tipo N usuarios/km² ×
  demanda en hora cargada, con eficiencia espectral sacada del mapa SINR real
  (integrar Shannon sobre el mapa)? Eso conectaría capacidad con lo ya medido.
- [ ] **Escena low-band**: ¿qué zona de 3×3 km? (San Isidro ampliado, u otro
  distrito con mejor cobertura OSM de alturas).
- [ ] **Sectorización**: pasar de iso a 3×tr38901 con azimut/tilt por sitio —
  ¿en la clase o como ejercicio para alumnos?
- [ ] **Procedimientos**: profundidad de los diagramas de secuencia —
  ¿conceptual (4-5 mensajes) o con nombres 3GPP reales (RRCSetupRequest,
  Msg1-Msg4)? [pregunta ya planteada, sin respuesta aún]
- [ ] **Emulación de señalización**: ¿Open5GS + UERANSIM como lab
  complementario para VER los procedimientos (registro, PDU session), o se
  deja fuera del alcance de esta sesión?
- [ ] **Una sesión o dos**: el material ya da para 07 (arquitectura +
  procedimientos) y 08 (diseño con Sionna). ¿Partimos?

---

## 5. Ruta tentativa de la clase (borrador)

1. Motivación: "te encargan la red de este distrito" + metas numéricas
2. El flujo de 7 fases (§1) como mapa de la sesión
3. Arquitectura 4G→5G: qué nodo hace qué en cada fase del flujo
4. Espectro y bandas (§2) — con la comparación medida sobre Lima
5. Link budget → sitios (Fase 2) — conecta con S01
6. Capacidad y tráfico (Fase 3) — nuevo
7. Plan nominal y detallado (Fases 4-5): sectores, PCI, RACH, TA, vecinas
8. Procedimientos: del encendido al handover, cada uno con su parámetro
9. Lab: el notebook como ciclo completo de diseño + validación
10. Cierre: el lazo de optimización nunca termina (SON)
