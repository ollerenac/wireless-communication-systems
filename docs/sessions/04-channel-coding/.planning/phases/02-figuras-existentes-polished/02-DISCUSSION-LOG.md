# Phase 2: Figuras Existentes Polished - Discussion Log

> **Audit trail only.** Do not use as input to planning, research, or execution agents.
> Decisions are captured in CONTEXT.md — this log preserves the alternatives considered.

**Date:** 2026-05-28
**Phase:** 02-figuras-existentes-polished
**Areas discussed:** Shannon operating points, Waterfall simulation approach, Figure size and style, Exercise numbering (LAB-05)

---

## Shannon operating points

| Option | Description | Selected |
|--------|-------------|----------|
| 5G NR standard set | BPSK r=1/2, QPSK r=1/2, QPSK r=3/4, 16QAM r=1/2, 64QAM r=3/4. Ties to Sesión 02 MCS table. | ✓ |
| Clean academic set | BPSK/QPSK/16QAM/64QAM each at r=1/2 only — simpler, uniform | |
| Just expand on existing | Keep 64-QAM 3/4 and add BPSK r=1/2 as extremes only | |

**User's choice:** 5G NR standard set

---

| Option | Description | Selected |
|--------|-------------|----------|
| One color per modulation + arrows | BPSK=blue, QPSK=green, 16QAM=orange, 64QAM=red. Consistent with BER curves in later phases. | ✓ |
| Single color, differentiated markers | Same color, different shapes — simpler but no cross-figure connection | |
| You decide | Let Claude choose | |

**User's choice:** One color per modulation + annotation arrows

---

| Option | Description | Selected |
|--------|-------------|----------|
| Yes — horizontal gap arrows | Horizontal distance annotation from each operating point to Shannon limit at same η | ✓ |
| No — points only | Cleaner, gap implied | |
| Gap for 64-QAM only | Representative case only | |

**User's choice:** Yes — horizontal gap arrows for all points

---

## Waterfall simulation approach

| Option | Description | Selected |
|--------|-------------|----------|
| Analytical approximations | Union bound / sphere-packing for LDPC, capacity-achieving for Polar. Instant, clean. | ✓ |
| Monte Carlo simulation | BP decoding for each LDPC rate + SC/SCL for Polar. Rigorous but 10–30 min in Colab. | |
| Hybrid (analytical + 1 MC validation) | Analytical + one Monte Carlo run for LDPC r=1/2 as validation | |

**User's choice:** Analytical approximations

---

| Option | Description | Selected |
|--------|-------------|----------|
| LDPC r=1/2, 2/3, 3/4 + Polar r=1/2, 3/4 | Exact match to FIG-03 requirement and 5G NR operating rates | ✓ |
| LDPC r=1/3, 1/2, 2/3 + Polar r=1/2 | Broader LDPC range, less Polar comparison | |
| You decide | Let Claude pick | |

**User's choice:** LDPC r=1/2, 2/3, 3/4 + Polar r=1/2, 3/4

---

| Option | Description | Selected |
|--------|-------------|----------|
| Yes — dashed vertical lines at threshold + text label | Each curve gets vertical dashed line at Shannon threshold Eb/N0 with gap label | ✓ |
| No — curves only | Cleaner figure | |
| You decide | Let Claude decide | |

**User's choice:** Yes — dashed vertical threshold markers + text labels

---

## Figure size and style

| Option | Description | Selected |
|--------|-------------|----------|
| Match Session 03 — (10, 5) for publication | Slightly narrower than session 03's (12,5), better for MkDocs | ✓ |
| Keep (8, 5) | No change | |
| Different per figure | Shannon=(10,5), Waterfall=(12,5) | |

**User's choice:** (10, 5) for both figures

---

| Option | Description | Selected |
|--------|-------------|----------|
| PNG at 150 dpi | Standard quality, reasonable file size (~150–300 KB) | ✓ |
| PNG at 200 dpi | Sharper but larger | |
| SVG (vector) | Resolution-independent but MkDocs plugin required | |

**User's choice:** PNG at 150 dpi

---

| Option | Description | Selected |
|--------|-------------|----------|
| Minimal alignment only | Add figure.figsize=(10,5) to existing rcParams dict. No other changes. | ✓ |
| Full Session 03 parity | Copy complete rcParams block from session 03 | |
| No change to rcParams | Set figsize only in individual cells | |

**User's choice:** Minimal alignment — add figsize to setup cell only

---

## Exercise numbering (LAB-05)

| Option | Description | Selected |
|--------|-------------|----------|
| Upgrade existing Ej6 waterfall in place | Keep current numbering; upgrade Ej6 to generate FIG-03. Update REQUIREMENTS.md. | ✓ |
| Restructure to match target layout | Move waterfall to Ej5 position | |
| Add new Ej5 for waterfall | Insert new cell, push current Ej5/Ej6 down | |

**User's choice:** Upgrade Ej6 in place; update REQUIREMENTS.md to say "Ejercicio 6"

---

| Option | Description | Selected |
|--------|-------------|----------|
| Replace entirely with analytical multi-rate | Remove LDPC (8,4) Monte Carlo, write analytical waterfall from scratch | ✓ |
| Keep (8,4) and add multi-rate above | Preserve existing code as reference, add multi-rate as second subplot | |
| You decide | Let Claude choose the structure | |

**User's choice:** Replace entirely with analytical multi-rate curves

---

## Claude's Discretion

- Exact Eb/N0 values for MCS operating points (calculated from rate and Shannon capacity)
- Specific analytical bound for LDPC (union bound vs Gallager bound)
- Specific analytical bound for Polar (Bhattacharyya vs capacity-bound)
- Placement of threshold marker text labels to avoid overlap
- Color scheme for waterfall curves (per-modulation-order vs per-rate linear colormap)

## Deferred Ideas

- Monte Carlo BER for real LDPC (n≈400 bits) — Phase 3 (LAB-01)
- BER curves by modulation order — Phases 3/5
- SVG output — Phase 6 (QA), verify MkDocs plugin compatibility
- SCL-L=8 waterfall curves — Phase 4 (LAB-02)
