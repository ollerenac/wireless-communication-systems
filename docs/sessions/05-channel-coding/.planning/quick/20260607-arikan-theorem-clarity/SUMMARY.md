---
slug: arikan-theorem-clarity
date: 2026-06-07
status: complete
commit: 98e71ad
---

# Summary: Arıkan theorem clarity improvement

## What was done

Improved readability of the polarization theorem paragraph in §4.1 of index.md (lines 403-407):

1. Added setup sentence before the formula: "los N = 2^n canales sintéticos se polarizan hacia los extremos"
2. Added `\overbrace{...}^{\text{nº de canales con Z≈0}}` annotation over the numerator
3. Split the conclusion into two sentences for clarity
4. Final sentence makes explicit: "Los códigos Polar no se *aproximan* al límite de Shannon — lo **alcanzan**"

## Files changed

- `index.md`: 3 lines → 7 lines (4 lines added, net +4)

## Acceptance

- mkdocs build --strict: PASS (0.79s)
- Commit: 98e71ad
