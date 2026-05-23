---
phase: 04
status: findings
files_reviewed: 1
findings:
  critical: 0
  warning: 1
  info: 2
  total: 3
reviewed_at: 2026-05-23
reviewer: claude-sonnet-4-6
scope: standard
context: >
  Phase 4 re-executed the notebook end-to-end (exit code 0, verified twice by Plan 04-02).
  No Python source was modified; only cell outputs were updated. Review covers code
  correctness, latent bugs, and pedagogical code quality across all 17 code cells.
---

# 04-REVIEW — lab.ipynb Code Review

**File:** `docs/sessions/03-ofdm-systems/lab.ipynb`
**Cells:** 44 total — 17 code, 27 markdown
**Execution:** exit code 0 (verified twice, Plan 04-02)
**Scope:** Standard — code correctness, latent bugs, pedagogical quality

---

## Summary

The notebook is functionally correct. All 17 code cells run cleanly and produce consistent
outputs. The OFDM chain (IFFT/CP/channel/FFT/equalizer/demap) is implemented correctly; noise
power, BER formulas, and MMSE/ZF equations are mathematically consistent. No runtime errors,
no division-by-zero risks (minimum |H[k]| = 0.435 across all 64 subcarriers), and no
state-ordering bugs between cells.

Three findings below the Critical threshold were identified: one Warning (dead write to disk,
no runtime impact) and two Info items (tautological CP assertion, non-canonical Gray code in
a display-only helper). None affect execution, numerical results, or student outcomes.

---

## Critical — 0 findings

None.

---

## Warning — 1 finding

### W-01 — Duplicate savefig filename overwrites Cell 11 output

**Confidence:** 85
**Cells:** Cell 11 (Bloque 9) and Cell 15 (Ejercicio 4)
**Path written:** `figures/ofdm-ber-equalizers.png`

Two cells save to the same filename with different parameters:

```python
# Cell 11 — Bloque 9 (ofdm_ber_quick, n_frames=200, dpi=150)
plt.savefig('figures/ofdm-ber-equalizers.png', dpi=150, bbox_inches='tight')

# Cell 15 — Ejercicio 4 (simulate_ofdm_ber, N_frames=500, dpi=300)
plt.savefig('figures/ofdm-ber-equalizers.png', dpi=300, bbox_inches='tight', facecolor='white')
```

Cell 15 executes after Cell 11 and overwrites the file. The version on disk after a full
notebook run is from Ejercicio 4 (dpi=300, facecolor='white'). This is the version
referenced in `index.md`.

The Cell 11 save call is a dead write: it produces a file that is immediately replaced.
If the notebook is run selectively (Sección 1 cells only, without Ejercicio 4), the
`figures/` directory will contain a lower-quality version (dpi=150, no forced white
background) under the same name that `index.md` references.

**Impact:** No execution error. Full-run behavior is correct (Cell 15 wins). Risk is only
when cells are run in partial subsets.

**Suggested fix:** Rename the Cell 11 save to a distinct filename, e.g.,
`figures/ofdm-ber-quick.png`, since it represents a different simulation
(`ofdm_ber_quick` with 200 frames vs `simulate_ofdm_ber` with 500 frames).

---

## Info — 2 findings

### I-01 — CP verification assertion is a tautology

**Confidence:** 90
**Cell:** Cell 4 (Bloque 2)

```python
print(f'¿CP == cola del símbolo? {np.allclose(x_cp_b2[:N_CP], x_cp_b2[N_CP+N-N_CP:])}')
```

`N_CP + N - N_CP` reduces to `N`, so the expression is:

```python
np.allclose(x_cp_b2[:N_CP], x_cp_b2[N:])
```

`x_cp_b2 = [cp | x]` has length `N + N_CP`. The slice `x_cp_b2[N:]` = last `N_CP` elements
of the array, which IS the CP block. Both sides of `allclose` reference the same
`N_CP`-element region — the comparison is always True regardless of whether `ofdm_tx`
is correct.

**Impact:** The assertion always prints `True` and students see the expected output. No
numerical result depends on it. No student will make an incorrect inference from the output.

**Suggested fix (optional):** Store `x` before calling `ofdm_tx`, then assert:
```python
assert np.allclose(x_cp_b2[:N_CP], x[-N_CP:])
```

---

### I-02 — Non-canonical Gray code in display-only 16-QAM mapper

**Confidence:** 82
**Cell:** Cell 7 (Bloque 5)
**Function:** `qam16_map` — used only in the QPSK vs 16-QAM constellation figure

```python
def gray_idx(g1, g0): return 2*g1 + (g1 ^ g0)
```

This maps bit patterns to lut indices as follows:

| (g1, g0) | Index | Amplitude |
|----------|-------|-----------|
| (0, 0)   | 0     | -3/√10    |
| (0, 1)   | 1     | -1/√10    |
| (1, 0)   | 3     | +3/√10    |
| (1, 1)   | 2     | +1/√10    |

Standard Gray-coded 16-QAM has the pair (01, 10) differing in exactly one bit. This
function produces (01→1, 10→3) swapping +3/√10 and +1/√10 relative to canonical — the
pair (01, 10) differs in both bits, violating the Gray property.

**Impact:** `qam16_map` is used only for the visual illustration in Bloque 5. All BER
simulations use `qpsk_map` and `qpsk_demap`, which are correctly implemented. A student
inspecting `gray_idx` may notice inconsistency with the docstring.

**Suggested fix (optional):**
```python
def gray_idx(g1, g0): return (2*g1 + g0) ^ g1  # canonical Gray: 00→0, 01→1, 11→2, 10→3
```

---

## Cells Reviewed — Status Summary

| Cell | Content | Status |
|------|---------|--------|
| 1  | Setup: imports, rng, rcParams, figures dir | Clean |
| 2  | Parameters: N=64, N_CP=16, M=4, h_channel | Clean |
| 3  | `qpsk_map` + constellation figure | Clean |
| 4  | `ofdm_tx` + CP structure test | Clean — I-01 (tautological assertion) |
| 5  | `apply_channel` + impulse response test | Clean |
| 6  | `ofdm_rx_no_channel` + round-trip test | Clean |
| 7  | `zf_equalizer` + `qam16_map` + QPSK/16-QAM figures | Clean — I-02 (qam16_map Gray code) |
| 8  | `mmse_equalizer` + α[k] figure | Clean |
| 9  | `ls_channel_estimate` + pilot figure | Clean |
| 10 | `qpsk_demap` + decision boundary figure | Clean |
| 11 | `ofdm_ber_quick` (Bloque 9) + BER curve | Clean — W-01 (dead savefig) |
| 12 | Ejercicio 1 — time domain + spectrum | Clean |
| 13 | Ejercicio 2 — IFFT/FFT round-trip | Clean |
| 14 | Ejercicio 3 — ISI sin CP vs con CP | Clean |
| 15 | Ejercicio 4 — `simulate_ofdm_ber` ZF vs MMSE | Clean — W-01 (overwrites Cell 11) |
| 16 | Ejercicio 5 — LS estimation with pilots | Clean |
| 17 | Ejercicio 6 — per-subcarrier BER + figure export | Clean |

---

## Key Correctness Checks — All Passed

- **Noise power model:** `sigma = sqrt(1/(k*SNR_lin*2))` is correct for QPSK
- **MMSE formula:** `conj(H)*Y / (|H|^2 + 1/SNR)` matches the Wiener filter derivation
- **ZF formula:** `Y/H` correctly inverts the channel; minimum |H[k]| = 0.435 (no division risk)
- **CP condition:** N_CP=16 >= L-1=6 holds throughout; circular convolution property valid
- **`qpsk_map`/`qpsk_demap` round-trip:** Gray coding is self-consistent; demap is exact inverse
- **Ejercicio 3 ISI model:** No-CP loop correctly prepends `prev_tail` (L-1=6 samples)
- **`ls_channel_estimate` interpolation:** `np.interp` on real and imaginary parts separately is correct
- **Per-subcarrier BER (Cell 17):** `Q(sqrt(2 * |H[k]|^2 * SNR))` is correct for ZF-equalized QPSK
