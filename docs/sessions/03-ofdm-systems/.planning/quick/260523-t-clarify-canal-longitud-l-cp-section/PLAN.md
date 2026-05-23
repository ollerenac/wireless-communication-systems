---
task_id: 260523-t
slug: clarify-canal-longitud-l-cp-section
date: "2026-05-23"
status: in_progress
---

# Quick Task: Clarify "canal de longitud L" in §3

## Problem

The opening of §3 (El Prefijo Cíclico) says:

> El canal de longitud $L$ convierte los primeros $L-1$ muestras del símbolo OFDM $n$
> en una mezcla que incluye las últimas muestras del símbolo $n-1$.

A reader landing here doesn't know WHY $L-1$ matters. The causal chain is missing:
- $L$ = number of channel taps ($h[0], \ldots, h[L-1]$)
- The last tap $h[L-1]$ arrives $L-1$ samples late
- Therefore the first $L-1$ received samples of symbol $n$ still carry energy from symbol $n-1$

$L$ was defined in §1 (Ec. 1 and the two admonition tables) but is invoked cold in §3.

## Fix

Replace the paragraph's first sentence to include the causal link. No figure needed —
the explanation is tight enough in prose.

## Scope

- One paragraph in `index.md` (~4 lines)
- No notebook changes
