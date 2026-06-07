---
task: polar-sections-clarity
date: "2026-06-05"
status: in-progress
---

# Quick Task — Clarify §4.1 and §4.2 (Polar Codes)

## Goal

Make §4.1 (Channel Polarization) and §4.2 (Successive Cancellation Decoding) in index.md more digestible without changing the mathematical content.

## Changes

### §4.1 — Polarización del Canal

1. **Explain Z(W) intuitively BEFORE equations** — frame Z as "probability that ML detection fails on this channel" so the recursion has meaning
2. **Add numerical mini-example N=2, Z₀=0.5** — show Z⁻=0.75, Z⁺=0.25 concretely before the general theorem
3. **Connect Figure 5 butterfly explicitly to the recursion** — add a sentence explaining that each stage of the butterfly applies the N=2 transformation recursively, and refer to the figure *before* the limit theorem

### §4.2 — Decodificación por Cancelación Sucesiva

1. **Expand with worked SC decoding example** — analogous to BP example in §3.2, show how 2-3 bits from a Polar N=8 block are decoded step by step (frozen bit → known, info bit → compute LLR from butterfly)
2. **Add SCL intuition analogy** — frame it as "beam search" over a binary decision tree: keep L paths, prune the least probable at each step

## Files

- `index.md` — sections §4.1 and §4.2 only

## Constraints

- Español, terminología técnica en inglés
- MkDocs-Material compatible (admonitions, display math)
- Do not change figures or figure captions
- Math content must remain correct
