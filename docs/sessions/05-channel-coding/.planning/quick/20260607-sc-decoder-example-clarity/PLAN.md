---
slug: sc-decoder-example-clarity
date: 2026-06-07
status: in-progress
---

# Quick Task: Mejorar estructura del ejemplo numérico SC Polar N=4

## Problemas identificados

1. "Etapa butterfly — combinar pares (0,2) y (1,3)" no explica POR QUÉ esos pares
2. ℓ_{02} y ℓ_{13} aparecen sin nombre verbal ni definición explícita
3. No se ve el patrón simétrico: las mismas operaciones (f para el primero, g para el segundo) se repiten en ambas mitades
4. La "Cancelación" no explica que se vuelve a los LLRs de canal (no a los ℓ intermedios)

## Solución

Restructurar en 4 etapas explícitas:
- Etapa 1: LLRs intermedios (deshacer Stage 2 hacia atrás) — explica POR QUÉ pares (0,2) y (1,3)
- Etapa 2: Decodificar u₀ y u₁ (deshacer Stage 1 hacia atrás)
- Etapa 3: Cancelar (û₀, û₁) y calcular nuevos LLRs intermedios
- Etapa 4: Decodificar u₂ y u₃ (misma lógica que Etapa 2)

## File

- `index.md` líneas 450-477

## Acceptance

- mkdocs build --strict pasa
- La estructura de 4 etapas está commitada
