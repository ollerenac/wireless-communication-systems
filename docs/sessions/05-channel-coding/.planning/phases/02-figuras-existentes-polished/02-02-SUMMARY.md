# SUMMARY — Plan 02-02: FIG-03 Waterfall curves analíticas

**Status:** ✅ Complete  
**Commit:** e30e158 — 2026-05-29  
**Duration:** ~2 min (subagent execution)

## What was done

- **Cell 13 (Ejercicio 6):** Complete replacement — all Monte Carlo code (`awgn_llr`, `simulate_ldpc_bler`, `bp_ldpc_llr`, `np.random`) removed. New analytical waterfall code: 5 code curves (LDPC r=1/2,2/3,3/4 + Polar r=1/2,3/4) + BPSK baseline + 3 Shannon threshold verticals with staggered Y labels.
- **index.md line 245:** Comment updated from `<!-- será generada por lab.ipynb — Fase 2 -->` to `<!-- generada por celda 13 de lab.ipynb -->`.
- **REQUIREMENTS.md line 30:** "Ejercicio 5 (waterfall)" corrected to "Ejercicio 6 (waterfall)" (D-12).

## Verification passed
- `figures/waterfall-curves.png` exists — 126 KB ✅
- 6 curves: BPSK (black) + LDPC×3 (blue family) + Polar×2 (orange family) ✅
- 3 Shannon threshold lines with `C(r=1/2)`, `C(r=2/3)`, `C(r=3/4)` labels at staggered Y positions ✅
- BER floor at 1e-7 (prevents log(0)) ✅
- `figsize=(10, 5)` in `plt.subplots` ✅
- `grep -c simulate_ldpc_bler lab.ipynb` → 0 ✅

## Requirements satisfied
- FIG-03, LAB-05 (Ej6), D-04, D-05, D-06, D-07, D-08, D-10, D-11, D-12
