---
task: Implementar ejemplo 3×3 SVD + water-filling del video (transcript en figures/svd-based-mimo/) como caja en §3.2
date: 2026-07-03
mode: quick-inline
---

# Plan

## Fuente
`docs/sessions/06-mimo-systems/figures/svd-based-mimo/transcript-svd-based-mimo.txt` (video ~29 min, inglés) + 13 screenshots `MM-SS.png`. Transcript suficiente — números verificados a mano, screenshots no necesarios.

## Contenido del video
- H = [[2,−6,0],[3,4,0],[0,0,2]], 3×3, columnas ortogonales.
- SVD por normalización de columnas: normas √13, √52, 2 = valores singulares; reordenar decreciente → σ₁=√52, σ₂=√13, σ₃=2; V = matriz de permutación.
- Post-proceso RX ỹ=Uᴴy, precoding TX x=Vx̃ → 3 canales desacoplados.
- Water-filling: Pᵢ = (1/λ − σ²/σᵢ²)₊ con λ = multiplicador de Lagrange, σ² = ruido (colisión de notación).
- Números: N₀=1 (0 dB), P=2 (3 dB) → 1/λ = (2 + 1/52 + 1/13 + 1/4)/3 = 0,7821 → P₁=0,7629 (−1,18 dB), P₂=0,7052 (−1,52 dB), P₃=0,5321 (−2,74 dB).

## Tareas
1. Caja `??? example` "Ejemplo numérico: water-filling en un canal 3×3" en §3.2, tras párrafo water-filling, antes de "Capacidad sin CSIT". Notación de la lección (μ, N₀); nota mapeando notación del video (1/λ = μ; σ² del video = N₀). Incluye: atajo columnas-ortogonales, chequeo Frobenius (69=52+13+4), derivación Lagrange breve, números, capacidad final ≈ 10,34 bit/s/Hz + comparación uniforme (10,30 — por qué WF gana poco a SNR alta).
2. Verificación aritmética inline (python).
3. `mkdocs build --strict`.
4. Espejo compacto en Artifact guión (§3 card).
5. Commits: contenido + artefactos GSD.

## Trampas del transcript (corregidas)
- "square root of 32" → √52; "1 over 30" → 1/13; "1 over 14" → 1/4; "sigma 3 square = 4" correcto (2²).
