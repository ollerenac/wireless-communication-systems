---
slug: csi-tdd-mmwave
created: 2026-07-02
mode: quick-inline
---

# Quick Task — CSI/reciprocidad TDD/pilot contamination + one-liners

## Problema
Toda la sesión asume H conocida sin decir cómo se obtiene. Massive MIMO (§6)
depende críticamente de reciprocidad TDD, y su límite REAL es pilot
contamination — ni mencionado. Además faltan dos frases de conexión:
MIMO-OFDM (cómo se aplica MIMO en banda ancha, link Sesión 03) y beamforming
híbrido (mmWave/FR2, link Sesión 07).

## Solución (3 ediciones, text-only)
1. **§6.3 nuevo** tras el "free lunch", antes de Fig 7: ¿de dónde sale H?
   - pilotos downlink no escalan con M
   - reciprocidad TDD → costo de pilotos ∝ K (usuarios), no M
   - pilot contamination → límite que NO desaparece al crecer M (multicelda)
2. **§2** tras párrafo scattering: una frase MIMO-OFDM (per-subcarrier, link
   Sesión 03).
3. **§6 "MIMO Masivo en 5G NR"**: una frase beamforming híbrido FR2/mmWave,
   reenvío Sesión 07.

## Verificación
- mkdocs build --strict pasa
- \mathbf, no \boldsymbol

## Commits
1. feat(06-mimo): §6.3 CSI/reciprocidad TDD/pilot contamination + notas MIMO-OFDM e híbrido
2. docs(quick-260702-csi-tdd): plan + summary
