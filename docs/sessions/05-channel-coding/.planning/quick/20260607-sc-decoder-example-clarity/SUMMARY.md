---
slug: sc-decoder-example-clarity
date: 2026-06-07
status: complete
commit: 519f070
---

# Summary: SC decoder example restructured into 4 stages

## What was done

Replaced the opaque "Etapa butterfly — combinar pares" + flat decision list
with a 4-stage structure in index.md (§4.2 example):

1. Etapa 1 — explains WHY pairs (0,2)/(1,3) and names ℓ_{02}, ℓ_{13} verbally
2. Etapa 2 — f/g rule made explicit: f for first bit (no context), g for second (uses prior decision)
3. Etapa 3 — cancellation uses û₀⊕û₁ (correct); explains why we return to channel LLRs
4. Etapa 4 — makes symmetric structure visible ("same logic as Etapa 2")

Net: +30 lines inserted, -11 removed. mkdocs build --strict PASS.

## Files changed

- `index.md`: +19 net lines
