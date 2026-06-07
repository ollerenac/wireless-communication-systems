---
slug: remove-mermaid-tanner
date: 2026-06-04
status: complete
---

# Summary: Remove inconsistent Mermaid Tanner graph

## Problem
Mermaid showed LDPC(7,4) with 1-indexed v₁–v₇/c₁–c₃ whose implicit H
matched neither the Hamming(7,4) H in Ejercicio 3 nor the LDPC(8,4) H_ldpc
in the lab. The PNG (Figura 2) already showed the correct LDPC(8,4).

## Change
- Removed Mermaid block (lines 121–132) and its italic caption (line 134)
- Replaced with one sentence referencing Figura 2 and naming the (8,4) code
- MkDocs strict build passes in 0.81s

## Commit
d37498e
