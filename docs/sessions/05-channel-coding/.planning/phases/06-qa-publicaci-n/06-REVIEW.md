---
phase: "06"
status: findings
files_reviewed: 2
findings:
  critical: 2
  warning: 6
  info: 0
  total: 8
---

# Code Review — Phase 06: QA & Publicación

**Files reviewed:** `docs/sessions/05-channel-coding/lab.ipynb`, `docs/sessions/05-channel-coding/index.md`
**Depth:** standard

---

## Critical Issues

### CRIT-1 — Figure 8 caption claims curves that don't exist in the figure

**File:** `docs/sessions/05-channel-coding/index.md` L283–285

The figcaption states "LDPC con tasas $r_c = 1/2$, $2/3$, $3/4$ (azul) y Polar con tasas equivalentes (naranja)" but cell 18 plots exactly one LDPC curve (Rc≈0.508, r_c≈1/2) and one Polar Bhattacharyya bound (r_c=0.5). No r_c=2/3 or r_c=3/4 curves exist.

**Fix:**
```
**Figura 8.** Curvas de BER (*waterfall*) en función de $E_b/N_0$ para BPSK sin código
(negro), LDPC $r_c\approx1/2$ (azul, Monte Carlo, n=240) y cota de unión Bhattacharyya
para Polar $r_c=1/2$ ($N=64$, naranja), todas sobre canal AWGN.
```

---

### CRIT-2 — Lab Exercise 4 instructs students to implement disabled SC/SCL decoders

**File:** `docs/sessions/05-channel-coding/index.md` L497

"Implementa el decodificador SC recursivo y el SCL con lista L=8" — but cell 16 defines both as `raise NotImplementedError('SC decoder deshabilitado — ver TODO')`. Students following the exercise will immediately hit a documented bug.

**Fix:** Rewrite Ej.4 to match implemented scope:
> **Ej. 4 — Polar N=64: encoder + bits congelados (~20 min)**: Construye el encoder Polar con la matriz $G_{64}$ y selección de bits congelados por parámetro de Bhattacharyya. Visualiza la polarización del canal mediante el histograma de $Z(W_{64}^{(i)})$. *(El decodificador SC/SCL queda diferido — ver extensión futura.)*

---

## Warning Issues

### WARN-1 — Figure 4 cell comment says "celda 9", actual generator is `cell-7c`

**File:** `docs/sessions/05-channel-coding/index.md` L177

`<!-- generada por celda 9 de lab.ipynb -->` — `figures/bp-messages.png` is saved by cell `cell-7c`. Stale numbering from a prior scheme.

**Fix:** `<!-- generada por celda 7c de lab.ipynb -->`

---

### WARN-2 — Figure 5 cell comment says "celda 10", actual generator is `cell-7d`

**File:** `docs/sessions/05-channel-coding/index.md` L185

`<!-- generada por celda 10 de lab.ipynb -->` — `figures/ldpc-ber-waterfall.png` is saved by cell `cell-7d`.

**Fix:** `<!-- generada por celda 7d de lab.ipynb -->`

---

### WARN-3 — Resumen table in `lab.ipynb` says Polar info channels `{2,3,5,7}`, actual is `{3,5,6,7}`

**File:** `docs/sessions/05-channel-coding/lab.ipynb` cell `cell-21`

Cell 12 output is deterministic: `Canales de información (k=4): [3, 5, 6, 7]`. Index 2 has Z[2]=0.8086 (frozen). The resumen table answer is wrong.

**Fix:** Change `{2,3,5,7}` to `{3,5,6,7}` in cell-21.

---

### WARN-4 — Lab Ej.3 says "n≈400 bits", actual code uses n=240

**File:** `docs/sessions/05-channel-coding/index.md` L495

Cell `cell-7b`: `H12 = gallager_ldpc(240, d_v=3, d_c=6, seed=2024)` → n=240.

**Fix:** Change `n≈400` to `n=240`.

---

### WARN-5 — Lab Ej.6 says "5 taps", actual `h_ch` has 3 taps

**File:** `docs/sessions/05-channel-coding/index.md` L501

Cell `cell-20`: `h_ch = np.array([0.8, 0.5, 0.3])` = 3 taps. Figure 9 caption correctly says "3 taps".

**Fix:** Change `de 5 taps` to `de 3 taps`.

---

### WARN-6 — Exercise 4(a) uses 1-based indexing ($i=1,\ldots,8$), notebook uses 0-based

**File:** `docs/sessions/05-channel-coding/index.md` L433

The exercise states $i=1,\ldots,8$ but cell 12 prints `Canal 0` through `Canal 7`. Theory section also uses $i=0,\ldots,N-1$.

**Fix:** Change `$i=1,\ldots,8$` to `$i=0,\ldots,7$`.

---

## Clean checks

- Cell 17 SC/SCL crash fix: correct — no calls to disabled decoders remain
- Cell 18 waterfall cell variable scope: all variables defined in prior cells, no forward-reference issues
- Cell 18 Bhattacharyya bound computation: structurally correct
- Figure numbering 1..9: sequential, no duplicates
- `<figure markdown="span">` blocks: all properly opened/closed
- LaTeX delimiters: no unclosed `$` or `$$` found
- Admonition indentation: all `???` bodies use 4-space indent
