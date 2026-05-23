---
slug: 260523-u
status: complete
date: 2026-05-23
---

## Resultado

Añadida la sección **"Derivación algebraica"** en §3 de `index.md`, entre el párrafo
"¿Por qué funciona?" y la afirmación "Formalmente, tras eliminar el CP...".

## Cambios

**`index.md`** (~14 líneas insertadas entre la línea 396 y la línea 398 original):

### Antes

```
**¿Por qué funciona?** ... convolución circular.

Formalmente, tras eliminar el CP, la muestra n-ésima del símbolo recibido es:

y[n] = Σ h[l] x[(n-l) mod N] + w[n]   (Ec. 4)
```

### Después

```
**¿Por qué funciona?** ... convolución circular.

**Derivación algebraica.** La clave es que el bloque transmitido x̃[m] satisface:

   x̃[m] = x[(m - N_CP) mod N]   para todo m = 0..N+N_CP-1

Para m ≥ N_CP: da x[m-N_CP] (símbolo).
Para m < N_CP (zona CP): da x[m-N_CP+N] (cola del símbolo).

El canal aplica convolución lineal. Descartando N_CP muestras y re-indexando n = m - N_CP:

   y[n] = Σ h[l] x̃[n + N_CP - l] + w[n]

Sustituyendo: x̃[n+N_CP-l] = x[(n-l) mod N]. Por tanto:

Formalmente, tras eliminar el CP, la muestra n-ésima es:

   y[n] = Σ h[l] x[(n-l) mod N] + w[n]   (Ec. 4)  ← ahora derivada, no afirmada
```

## Archivos modificados

- `index.md`: 14 líneas insertadas, 0 eliminadas

## Archivos sin modificar

- `lab.ipynb`: sin cambios (no requerido)
