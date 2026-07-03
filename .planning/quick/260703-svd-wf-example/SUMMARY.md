---
task: Implementar ejemplo 3×3 SVD + water-filling del video como caja en §3.2
date: 2026-07-03
status: complete
commit: 194e3b1
---

# Summary

## Hecho
- Caja `??? example "Ejemplo numérico: SVD y water-filling en un canal 3×3"` insertada en §3.2 tras el párrafo water-filling, con crédito a la fuente (NPTEL, Jagannatham).
- Párrafo previo nuevo "¿De dónde sale la fórmula de Pk*?" — derivación Lagrange: λ = precio del vatio, μ = 1/(λ·ln2) = nivel de agua.
- Contenido de la caja: atajo columnas ortogonales (SVD por normalización, V = permutación), chequeo Frobenius 69 = 52+13+4, canales desacoplados, water-filling numérico (μ ≈ 0,782; P* = 0,763/0,705/0,532; −1,18/−1,52/−2,74 dB), capacidad 10,34 vs uniforme 10,30 bit/s/Hz con moraleja (WF gana poco a SNR alta), nota de notación mapeando video (1/λ, σ² ruido) ↔ lección (μ, N₀).
- Números verificados con numpy antes de escribir (todos coinciden con el video; transcript tiene typos: "√32"→√52, "1/30"→1/13, "1/14"→1/4).
- Espejo compacto en Artifact guión (cartilla §3, 2 beats).
- Dudas del usuario respondidas en chat: λ = multiplicador de Lagrange (1/λ = μ); σ²/σᵢ² = ruido/ganancia (colisión de notación del video), no un ratio sigma-autovalor.

## Sin necesidad
- Screenshots del video: transcript suficiente, aritmética verificada independientemente.

## Commits
- `194e3b1` feat(06-mimo): ejemplo water-filling 3×3 en §3.2
