---
plan: 05-01
phase: 05-integrador-ofdm-fec
status: complete
commit: 7f66aaf
---

# Summary — Plan 05-01: OFDM+LDPC Integrador

## What Was Built

- **lab.ipynb Cell 18**: Markdown actualizado describiendo el ejercicio OFDM+LDPC end-to-end
- **lab.ipynb Cell 19**: Integrador completo — 4 funciones OFDM de sesión 03 (sin modificación) + QPSK helpers + simulación Monte Carlo OFDM sin FEC vs OFDM+LDPC + figura FIG-09
- **lab.ipynb Cell 20**: Entrada de resumen actualizada para Ejercicio 6
- **figures/ofdm-ldpc-ber.png**: 100,486 bytes — 3 curvas BER (AWGN teórico, OFDM sin FEC, OFDM+LDPC)
- **index.md §5**: Bloque `<figure markdown="span">` FIG-09 insertado después del hook narrativo

## Key Metrics

| Métrica | Valor |
|---------|-------|
| ofdm-ldpc-ber.png | 100,486 bytes |
| BER uncoded @ 5 dB | 5.11e-02 |
| BER OFDM+LDPC @ 5 dB | 2.21e-02 |
| Frames Monte Carlo | 300 por punto de SNR |
| Puntos de SNR | 21 (0–10 dB, paso 0.5 dB) |

## Deviations

Ninguna. El plan se ejecutó exactamente como diseñado.

## Self-Check: PASSED

- [x] figures/ofdm-ldpc-ber.png existe (100 KB > 40 KB mínimo)
- [x] Cell 19 contiene las 4 funciones OFDM de sesión 03 sin modificación
- [x] Cell 19 usa bp_awgn de Cell 8
- [x] index.md §5 tiene bloque <figure> con "celda 19 de lab.ipynb"
- [x] lab.ipynb mantiene 21 celdas totales
- [x] Commit 7f66aaf incluye lab.ipynb, index.md, ofdm-ldpc-ber.png, 05-01-PLAN.md
