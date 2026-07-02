---
slug: csi-tdd-mmwave
status: complete
created: 2026-07-02
completed: 2026-07-02
commit: c04ffc3
---

# Summary — CSI/reciprocidad TDD/pilot contamination + one-liners

## Hecho
Tres ediciones en `docs/sessions/06-mimo-systems/index.md`:
1. **§6.3** (tras el "free lunch", antes de Fig 7): ¿de dónde sale H?
   Pilotos downlink no escalan con M → reciprocidad TDD (costo ∝ K, no M) →
   pilot contamination como techo real multicelda que NO desaparece al crecer
   M. Cierra Massive MIMO honestamente.
2. **§2** (tras scattering): frase MIMO-OFDM — H de banda estrecha, en banda
   ancha una matriz por subportadora, link Sesión 03, arquitectura 5G/WiFi.
3. **§6 "5G NR"**: frase beamforming híbrido FR2/mmWave (cadena RF por antena
   inviable → analógico+digital), reenvío Sesión 07.

## Verificación
- mkdocs build --strict: pasa (solo INFO CLAUDE.md fuera de nav)

## Commits
- c04ffc3 — feat(06-mimo): §6.3 + notas MIMO-OFDM e híbrido
- (artifacts) — docs(quick-260702-csi-tdd): plan + summary
