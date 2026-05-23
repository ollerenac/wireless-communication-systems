---
task_id: 260523-t
slug: clarify-canal-longitud-l-cp-section
date: "2026-05-23"
status: complete
---

# Summary: Clarify "canal de longitud L" in §3

## What was done

Replaced the opening sentence of the "La ISI en OFDM sin CP" paragraph in §3.

**Before:**
> El canal de longitud $L$ convierte los primeros $L-1$ muestras del símbolo OFDM $n$
> en una mezcla que incluye las últimas muestras del símbolo $n-1$.

**After:**
> El canal tiene $L$ taps — $h[0], h[1], \ldots, h[L-1]$ (Ec. 1) — y el eco más tardío
> llega con $L-1$ muestras de retraso. Si dos símbolos OFDM consecutivos se transmiten
> sin CP, ese eco tardío hace que las primeras $L-1$ muestras del símbolo recibido $n$
> contengan también energía del símbolo anterior $n-1$: **ISI inter-símbolo**.

The fix makes the causal chain explicit: $L$ taps → last tap $h[L-1]$ has delay
$L-1$ → first $L-1$ received samples are contaminated. Also cross-references Ec. 1
for readers who need the full definition.
