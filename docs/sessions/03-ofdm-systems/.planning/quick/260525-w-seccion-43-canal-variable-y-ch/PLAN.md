---
slug: 260525-w
title: Alinear §4.3 con Bloque 3 del notebook — quitar ruido del snippet, cambiar y_noisy → y_ch
date: 2026-05-25
---

## Diagnóstico

§4.3 Canal Multipath (index.md ~línea 671) muestra:

```python
y_noisy = apply_channel(x_cp, h_channel) + noise
```

El Bloque 3 del notebook (Cell 12, id=3ee4d17a) hace:

```python
y_ch_b3 = apply_channel(x_cp_b2, h_channel)[:N + N_CP]   # sin ruido
```

Y el header de Bloque 3 (Cell 11) explica explícitamente:
"el AWGN no se añade aquí — se introduce en el Bloque 5 para poder observar el
efecto del canal y el del ruido por separado."

Dos discrepancias:
1. **Variable**: `y_noisy` vs `y_ch_b3` (base: `y_ch`)
2. **Ruido**: snippet de §4.3 incluye generación de noise + suma; notebook no la tiene

## Cambios en index.md

**Cambio 1 — Código snippet §4.3** (líneas 671–682):

Antes:
```python
def apply_channel(x_signal, h):
    """Convolución lineal con h: simula el canal multipath."""
    return np.convolve(x_signal, h, mode='full')[:len(x_signal)]

# El ruido se añade por separado, calibrado al Eb/N0 del punto de simulación:
SNR_lin = 10 ** (SNR_dB / 10)
sigma2  = 1 / (2 * k * SNR_lin)
noise   = (rng.normal(0, np.sqrt(sigma2), N + N_CP) +
           1j * rng.normal(0, np.sqrt(sigma2), N + N_CP))
y_noisy = apply_channel(x_cp, h_channel) + noise
```

Después:
```python
def apply_channel(x_signal, h):
    """Convolución lineal con h: simula el canal multipath."""
    return np.convolve(x_signal, h, mode='full')[:len(x_signal)]

y_ch = apply_channel(x_cp, h_channel)
# Nota: el AWGN se añade por separado en la cadena de BER (§4.5); aquí
# se aísla el efecto del canal para poder verificarlo sin ruido de por medio.
```

**Cambio 2 — Prosa posterior** (línea 692):
Cambiar `\`y_noisy\`` → `\`y_ch\``

## Archivos sin modificar
- `lab.ipynb`: ground truth, sin tocar
