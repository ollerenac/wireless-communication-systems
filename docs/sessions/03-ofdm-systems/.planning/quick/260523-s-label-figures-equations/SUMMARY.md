---
task_id: 260523-s
slug: label-figures-equations
date: "2026-05-23"
status: complete
---

# Summary: Ordinal Figure Labels and Equation Numbers

## What was done

Added sequential ordinal labels to all 13 figures in `index.md` and numbered 9 key
equations in both `index.md` and `lab.ipynb` with `\tag{N}`.

### Figures (index.md)

All figures now have `<figure markdown="span">` + `<figcaption>**Figura N.**...</figcaption>`:

| # | File | Change |
|---|------|--------|
| 1 | isi-problem.png | No change (already labeled) |
| 2 | ofdm-ifft-transmitter.png | No change (already labeled) |
| 3 | ofdm-subcarriers.png | Added `<figure>` + caption |
| 4 | cp-illustration.png | Added `<figure>` + caption |
| 5 | zf-equalizer-effect.png | Added `<figure>` + caption |
| 6 | zf-equalizer-qam-comparison.png | Added `<figure>` + caption |
| 7 | zf-noise-amplification.png | Added `<figure>` + caption |
| 8 | ofdm-ber-equalizers.png (§4.6 admonition) | Added indented `<figure>` + caption |
| 9 | channel-estimation-ls.png | Added `<figure>` + caption |
| 10 | lte-resource-grid-pilots.png (§4.7 admonition) | Added indented `<figure>` + caption |
| 11 | mmse-vs-zf-constellation.png | Renumbered "Figura 3" → "Figura 11" |
| 12 | ofdm-ber-equalizers.png (§5.1) | Added `<figure>` + caption |
| 13 | ofdm-per-subcarrier-ber.png (§5.1 list) | Added indented `<figure>` + caption |

### Equations

| Ec. | Equation | index.md | lab.ipynb |
|-----|----------|----------|-----------|
| (1) | Channel model | line 27 | — |
| (2) | OFDM IDFT | line 229 | Cell 3 |
| (3) | DFT orthogonality | line 263 | — |
| (4) | Circular convolution | line 400 | — |
| (5) | Freq. domain Y[k]=H[k]X[k]+W[k] | line 404 | Cell 3 |
| (6) | ZF equalizer | line 732 | Cell 3 |
| (7) | ZF SNR | line 744 | — |
| (8) | MMSE equalizer | line 819 | Cell 3 |
| (9) | LS channel estimation | line 869 | Cell 37 |

## Validation

- `mkdocs build --strict` passes (exit 0, built in 0.76 s)
- All 13 figure labels sequential (Figura 1–13)
- All 9 equation tags confirmed present in both files
