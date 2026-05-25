---
quick_id: 260525-y
slug: llr-formula-remove
date: 2026-05-25
status: complete
---

# Summary: Reemplazar fórmula LLR por prosa en §4.8

## What was done

Eliminada la display equation `Λ_i[k] = log P(b_i=0|X̂) / P(b_i=1|X̂)` del párrafo
"Decisión soft (LLR)" en §4.8. Reemplazada por prosa que explica la intuición:
signo → decisión, magnitud → confianza. El título cambió de "Decisión soft (LLR)"
a "Decisión soft" (sin el acrónimo formal).

## Rationale

El laboratorio no implementa LLR — qpsk_demap usa hard decision pura. El párrafo
es motivacional/forward-looking hacia Sesión 04. La fórmula formal es prematura aquí
y se introduce mejor cuando el decodificador LDPC esté en contexto.

## Files changed

- `index.md` línea 975–979: bloque "Decisión soft (LLR)" sin la display equation
