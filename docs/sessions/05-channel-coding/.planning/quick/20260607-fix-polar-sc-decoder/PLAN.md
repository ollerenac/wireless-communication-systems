---
slug: fix-polar-sc-decoder
created: "2026-06-07"
status: in-progress
---

# Fix Polar Encoder Convention + SC/SCL Decoder

## Goal
Corregir la inconsistencia de convención kron en `build_polar_G` (cell 15) e implementar
`sc_decode_polar` y `scl_decode_polar` generales en cell 17 de `lab.ipynb`.

## Root Cause
`build_polar_G` usa F=[[1,0],[1,1]] (triangular inferior) pero f_func/g_func, draw_butterfly
y el ejemplo N=4 son consistentes con F_T=[[1,1],[0,1]] (triangular superior).

## Tasks

### T1 — Fix encoder (cell 15)
- Cambiar `F = np.array([[1, 0], [1, 1]])` → `F = np.array([[1, 1], [0, 1]])`
- Actualizar `G4_ref` → `[[1,1,1,1],[0,1,0,1],[0,0,1,1],[0,0,0,1]]`
- Actualizar comentario de `build_polar_G` para reflejar nueva convención

### T2 — Implement SC decoder (cell 17)
- Implementar helper `_sc_llr(llr_ch, u_hat, bit_idx, N)` — computa LLR recursivo
- Implementar `sc_decode_polar(llr_ch, frozen_set, N)` — decoder SC general
- Añadir verificación contra `sc_decode_n4` (cell 14)

### T3 — Implement SCL decoder (cell 17)
- Implementar `scl_decode_polar(llr_ch, frozen_set, N, L=8)` — beam search
- Prueba MC breve: SC vs SCL a SNR 0..5 dB con N=64, k=32

## Verification
- `build_polar_G(4)` debe coincidir con nueva G4_ref
- `sc_decode_polar(L_ex, {0,1}, 4)` debe dar `[0,0,1,0]`
- `scl_decode_polar(L_ex, {0,1}, 4, L=8)` debe dar `[0,0,1,0]`
- Celda 17 ejecuta sin errores
