---
title: "Examen — Diseño de red de acceso 5G"
description: "Proyecto integrador de diseño y validación de una red 5G sobre un mapa 3D real de Lima."
---

# Examen — Diseño de red de acceso 5G

**Sesión 07 · Proyecto integrador**

| | |
|---|---|
| **Fecha** | *por definir* |
| **Duración** | 3 horas |
| **Modalidad** | *por definir (presencial / remota)* |
| **Entrega** | *por definir* — el notebook ejecutado de punta a punta (`.ipynb`) |
| **Material permitido** | la [lección de la Sesión 07](../sessions/07-network-design/index.md) (con sus notas) y el notebook del examen |

## Qué vas a hacer

Un operador móvil entrante te contrata para diseñar su red de acceso 5G
sobre un mapa 3D real de Lima. El examen recorre las mismas siete fases de
la lección, sobre **tu propio mapa**:

| Fase | Entregable |
|---|---|
| 0 | Requisitos R1–R8 a partir de la publicidad y los TdR |
| 1 | Estrategia de espectro: *physical resource blocks* (PRB, bloques de recursos físicos), reparto *time-division duplexing* (TDD, duplexación por división de tiempo), anchos efectivos |
| 2 | *Link budget* (presupuesto de enlace) en *downlink* (DL, bajada) y *uplink* (UL, subida) → radio de celda → sitios por cobertura |
| 3 | Capacidad por sitio → sitios por demanda → veredicto del dimensionamiento |
| 4 | Plan nominal sobre el trazador: posiciones en azoteas reales, iterado con los proxies R2/R3 |
| 5 | Planificación detallada: *physical cell identity* (PCI, identidad física de celda), zona de contención del *physical random access channel* (PRACH, canal físico de acceso aleatorio), *tracking areas* (áreas de seguimiento) |
| 6 | Validación contra el mapa consolidado: veredicto R1–R8 |

## Abre el notebook

[![Abrir en Google Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/ollerenac/wireless-communication-systems/blob/main/docs/sessions/07-network-design/examen-alumno.ipynb)

1. Abre el notebook con el botón anterior y guarda una copia en Drive.
2. Activa la GPU: *Entorno de ejecución → Cambiar tipo de entorno de
   ejecución → T4 GPU*.
3. En la primera celda elige uno de los nombres válidos en `ESCENA` y
   ejecútala. Esa celda instala Sionna RT y descarga el ZIP del mapa.
4. Comprueba que aparezca `listo: mapa '<nombre>' disponible` antes de
   empezar la Fase 0.

También puedes [descargar el notebook](../sessions/07-network-design/examen-alumno.ipynb)
para conservar una copia local.

## La dinámica

Cada fase trae los mismos bloques:

1. **Enunciado** — la parte del proyecto que esa fase resuelve.
2. **Pistas** — qué tabla o sección de la lección consultar.
3. **Celda `TU TRABAJO`** — complétala: cada `None` marcado con
   `<- COMPLETA` es tuyo; lo demás viene armado.
4. **Celda `VERIFICADOR`** — ejecútala **sin modificarla**: chequea que tu
   respuesta esté bien *formada* (no que esté bien *pensada*).
5. **Celda `JUSTIFICACIÓN`** — responde en 2–3 líneas por pregunta.

**Cómo se califica:** cada número que escribas debe tener **origen** — una
oferta de la publicidad, una cláusula de los TdR, o una tabla de la
lección (citada). Un valor distinto al de la pauta pero bien defendido
vale; un valor "correcto" sin defender, no.

## Elige tu mapa

El notebook descarga desde el sitio del curso el mapa que declares en la
variable `ESCENA` de la primera celda. Solo los dos nombres siguientes son
válidos. Cada mapa tiene su propia publicidad y sus propios TdR — **los
números de tu Fase 0 salen de aquí**:

### `jesus-maria-01` — Jesús María

[Descarga de respaldo del mapa](../sessions/07-network-design/escenas/jesus-maria-01.zip)

Polígono de **1.27 × 1.07 km** de distrito residencial denso, con el eje
hospitalario de la Av. Arenales (Torre Trecca, Edificio Lima) dentro del
área. La publicidad ya impresa:

> *"5G real en todo Jesús María. Video HD sin cortes y videollamadas que
> no se caen, en tu casa y en la calle. La red que sí llega."*

Términos de referencia:

- Licencia: **80 MHz en n78** (3.5 GHz), TDD.
- Azoteas disponibles; el municipio autoriza **máximo 7 sitios**.
- Potencia máxima por sector: **43 dBm**.
- Mercado: ~**30 000 hab/km²**, participación objetivo **25%**,
  consumo típico **12 GB/mes** por abonado.
- *Throughput* (tasa útil) mínimo en el borde según la guía de planificación del operador:
  **50 Mbps DL / 5 Mbps UL** en el percentil 5 (ref. NGMN
  *"50 Mbps everywhere"*).

### `san-isidro-01` — San Isidro

[Descarga de respaldo del mapa](../sessions/07-network-design/escenas/san-isidro-01.zip)

Polígono de **1.2 × 1.1 km** del distrito financiero. La publicidad que
el operador quiere poder cumplir:

> *"Videollamadas nítidas y tu oficina en la nube, en todo San Isidro."*

Términos de referencia:

- Licencia: **100 MHz en n78** (3.5 GHz), TDD.
- Azoteas disponibles; el municipio autoriza **máximo 6 sitios**.
- Potencia máxima por sector: **43 dBm**.
- Mercado: ~**25 000 personas presentes/km²** en hora cargada (distrito
  financiero: población flotante), participación objetivo **30%**,
  consumo típico **10 GB/mes** por abonado.
- *Throughput* mínimo en el borde según la guía de planificación del operador:
  **50 Mbps DL / 5 Mbps UL** en el percentil 5 (ref. NGMN
  *"50 Mbps everywhere"*).

### `cercado-lima-01` — Cercado de Lima

*En preparación — no disponible para este examen.*

!!! note "El mapa de la lección no es tu examen"

    La lección resuelve San Isidro paso a paso en
    [`design.ipynb`](../sessions/07-network-design/design.ipynb) sobre una
    escena *distinta* (otro export, otro polígono): te sirve como ejemplo
    del método, no como fuente de respuestas — las posiciones, mapas y
    números medidos no coinciden.

## Tiempos de GPU — planifícalos

- **Fase 4**: cada corrida del mapa exploratorio tarda ~1–3 min, y vas a
  iterar tu colocación varias veces.
- **Fase 6**: el mapa consolidado (10⁶ rayos) tarda **10–30 min y se corre
  UNA sola vez**. No lo dejes para los últimos 20 minutos.
- Las verificaciones de la Fase 6 y toda la Fase 5 son analíticas:
  re-ejecutables sin costo.

## Reglas

- Los **verificadores no se modifican**. Un verificador en verde no es
  nota: chequea forma y consistencia, no criterio.
- El notebook se entrega **ejecutado de punta a punta** (todas las celdas
  con salida) y con las **justificaciones respondidas**.
- Trabajo **individual**.
