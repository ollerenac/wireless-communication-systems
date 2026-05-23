---
slug: 260523-u
title: Derivar algebraicamente por qué Ec. (4) es convolución circular
date: 2026-05-23
---

## Objetivo

El alumno dice "no me queda nada claro como es que la muestra n-ésima del símbolo recibido es [Ec. 4]". La Ec. (4) aparece en §3 (El Prefijo Cíclico) precedida por intuición pero sin el puente algebraico que la justifica.

## Diagnóstico

En `index.md` líneas 394–400:

1. Párrafo "¿Por qué funciona?" (l. 396) — intuición conceptual correcta.
2. "Formalmente, tras eliminar el CP..." (l. 398) — afirma el resultado sin mostrarlo.
3. Ec. (4) (l. 400) — la convolución circular aparece sin derivar.

Falta la derivación algebraica de un solo paso clave:

> El bloque transmitido $\tilde{x}[m]$ satisface $\tilde{x}[m] = x[(m - N_{CP}) \bmod N]$
> para todo $m$. Al sustituir en la convolución lineal post-CP-removal,
> el argumento `mod N` sale en una línea.

## Cambio

Archivo: `docs/sessions/03-ofdm-systems/index.md`

Insertar un párrafo de derivación **entre** la línea 396 ("¿Por qué funciona?") y la
línea 398 ("Formalmente, tras eliminar el CP"), que muestre:

1. Definición compacta de $\tilde{x}[m] = x[(m - N_{CP}) \bmod N]$ con explicación
   de por qué funciona en la zona del CP.
2. La convolución lineal post-CP-removal expresada en términos de $\tilde{x}$.
3. La sustitución directa que produce el mod N.

No se modifican ecuaciones existentes (Ec. 4 y Ec. 5 quedan sin cambios).
No se toca `lab.ipynb`.

## Scope

- 1 archivo modificado: `index.md`
- ~10 líneas añadidas entre l. 396 y l. 398
- Sin nuevas figuras, sin cambios a ecuaciones numeradas existentes
