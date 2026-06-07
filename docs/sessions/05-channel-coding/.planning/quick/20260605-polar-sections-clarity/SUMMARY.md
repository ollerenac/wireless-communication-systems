---
task: polar-sections-clarity
date: "2026-06-05"
status: complete
commit: 410bf89
---

# Summary — Clarify §4.1 and §4.2 (Polar Codes)

## Changes Made

### §4.1 — Polarización del Canal
- Added bridge paragraph connecting Figure 5 butterfly diagram to the N=2 recursion (each XOR column = one butterfly stage)
- Rewrote Bhattacharyya Z(W) introduction: probabilistic intuition (cota de error ML) before equations
- Added collapsible mini-example: Z₀=0.5, two butterfly stages, table showing polarization in N=4 (Z from 0.94 to 0.06)

### §4.2 — Decodificación por Cancelación Sucesiva
- Exposed f and g LLR operations explicitly with formulas and intuition (f = BP check-node message, g = successive cancellation via XOR undo)
- Added worked numerical example: Polar N=4, rate 1/2, AWGN, shows frozen-bit decisions → cancellation → info bit decoding with LLR amplification
- Expanded SCL description: beam-search analogy over binary decision tree, L=8 → up to 256 candidate paths

## Build

MkDocs strict build: PASS (0.75s)
