---
task_id: 260523-s
slug: label-figures-equations
date: "2026-05-23"
status: in_progress
---

# Quick Task: Add Ordinal Figure Labels and Equation Numbers

## Goal

Give every figure in `index.md` a proper `**Figura N.**` caption and tag the 9 key
equations in both `index.md` and `lab.ipynb` with `\tag{N}` so students can reference
them by number across both materials.

## Scope

### Figures (index.md)

| # | File | Action |
|---|------|--------|
| 1 | isi-problem.png | Already labeled — no change |
| 2 | ofdm-ifft-transmitter.png | Already labeled — no change |
| 3 | ofdm-subcarriers.png (line 308) | Wrap in `<figure>` + add caption |
| 4 | cp-illustration.png (line 407) | Wrap in `<figure>` + add caption |
| 5 | zf-equalizer-effect.png (line 749) | Wrap in `<figure>` + add caption |
| 6 | zf-equalizer-qam-comparison.png (line 763) | Wrap in `<figure>` + add caption |
| 7 | zf-noise-amplification.png (line 792) | Wrap in `<figure>` + add caption |
| 8 | ofdm-ber-equalizers.png (line 827, inside admonition) | Add `<figure>` wrapper (4-space indent) |
| 9 | channel-estimation-ls.png (line 855) | Wrap in `<figure>` + add caption |
| 10 | lte-resource-grid-pilots.png (line 883, inside admonition) | Add `<figure>` wrapper (4-space indent) |
| 11 | mmse-vs-zf-constellation.png (line 950) | Already has `<figure>` — change "Figura 3" → "Figura 11" |
| 12 | ofdm-ber-equalizers.png (line 986) | Wrap in `<figure>` + add caption |
| 13 | ofdm-per-subcarrier-ber.png (line 994, inside list) | Add `<figure>` wrapper (4-space indent) |

### Equations (index.md + lab.ipynb)

| Ec. | Equation | index.md line | Notebook cell |
|-----|----------|---------------|---------------|
| 1 | Channel model `y[n] = Σh[l]x[n-l] + w[n]` | 27 | — |
| 2 | OFDM IDFT `x[n] = (1/√N)ΣX[k]e^{j2πkn/N}` | 229 | Cell 3 |
| 3 | Orthogonality `(1/N)Σe^{j2π(l-k)n/N} = δ[l−k]` | 263 | — |
| 4 | Circular conv. `y[n] = Σh[l]x[(n−l)modN] + w[n]` | 397 | — |
| 5 | Freq. domain `Y[k] = H[k]X[k] + W[k]` | 401 | Cell 3 |
| 6 | ZF estimator `X̂^ZF[k] = Y[k]/H[k]` | 726 | Cell 3 |
| 7 | ZF SNR `SNR^ZF[k] = |H[k]|²·SNR₀` | 738 | — |
| 8 | MMSE estimator `X̂^MMSE[k] = H*[k]/(|H[k]|²+1/SNR)·Y[k]` | 804 | Cell 3 |
| 9 | LS estimation `Ĥ^LS[k_p] = Y[k_p]/X_p` | 851 | Cell 37 |

## Steps

1. Edit `index.md`: wrap bare figures in `<figure>` + `<figcaption>`, renumber Figura 3→11
2. Edit `index.md`: add `\tag{N}` to 9 key equations
3. Edit `lab.ipynb`: add `\tag{N}` to equations in Cells 3 and 37
4. Update STATE.md
5. Write SUMMARY.md
6. Commit
