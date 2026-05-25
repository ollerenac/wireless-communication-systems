---
slug: 260525-v
title: Añadir "Eliminar CP" al diagrama ASCII y "ADC" a la tabla de §4
date: 2026-05-25
---

## Objetivo

Dos omisiones en la sección §4 "Cadena OFDM Completa":

1. El diagrama ASCII de bloques (RX chain) no muestra el paso "Eliminar CP" — la señal
   salta de ADC directamente a FFT, ocultando el paso que justifica toda la §3.

2. La tabla "Lectura bloque a bloque" incluye DAC (TX) pero omite ADC (RX).

## Cambios

### Archivo: `index.md`

**Cambio 1 — Diagrama ASCII (líneas 499–511)**

Ampliar el cuadro RX para incluir "Eliminar CP" entre ADC y FFT.
Expandir ambas cajas al mismo ancho para consistencia visual.

Antes (RX):
```
│  Bits RX ◄── QAM demapper ◄── Ecualizador ◄── FFT (N pts) ◄── ADC     │
```

Después (RX):
```
│  Bits RX ◄── QAM demapper ◄── Ecualizador ◄── FFT (N pts) ◄── Eliminar CP ◄── ADC │
```

**Cambio 2 — Tabla bloque a bloque (líneas 544–554)**

Insertar fila ADC entre "Canal h(t) + AWGN" y "Eliminar CP":

```
| ADC | Señal analógica RF → muestras digitales | Interfaz con el medio físico |
```

## Scope

- 1 archivo: `index.md`
- ~12 líneas modificadas (diagrama) + 1 fila añadida (tabla)
- Sin cambios a `lab.ipynb`
