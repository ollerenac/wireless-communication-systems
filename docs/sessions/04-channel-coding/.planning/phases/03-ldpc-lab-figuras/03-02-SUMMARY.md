---
status: complete
---
# SUMMARY — Plan 03-02: LAB-01 + FIG-05 + FIG-08

**Commit:** d97fa09 — 2026-05-29

## What was done
- **Cell 8 (index 8):** `gallager_ldpc()`, `gf2_rank()`, `bp_awgn()`, `bp_awgn_track()` — Gallager LDPC (n=240, d_v=3) at rates ~1/2 (d_c=6) and ~3/4 (d_c=12). BP converges in <15 iterations at threshold SNR. sigma² = 1/(2·Rc·EbN0_lin) formula verified.
- **Cell 9 (index 9):** `bp-messages.png` — 3-panel LLR histogram at iterations 1, 3, 10 at Eb/N0=2.5 dB. seed=137. 56,750 bytes.
- **Cell 10 (index 10):** `ldpc-ber-waterfall.png` — Monte Carlo BER (n_blocks=200) for rates ~1/2 and ~3/4 + BPSK. Waterfall ratio >5000× at rate-1/2. Shannon threshold verticals included. 107,075 bytes.
- **index.md §3.2:** Two `<figure markdown="span">` blocks inserted before closing hook.
- **Notebook:** 18 cells total (15 + 3 new).

## Verification passed
- `figures/bp-messages.png` — 56,750 bytes ✅
- `figures/ldpc-ber-waterfall.png` — 107,075 bytes ✅
- `len(nb['cells']) == 18` ✅
- sigma formula `1.0 / (2 * Rc * EbN0_lin)` confirmed ✅
- Waterfall cliff visible: ≥3 decades BER drop ✅

## Requirements satisfied
- LAB-01, FIG-05, FIG-08
