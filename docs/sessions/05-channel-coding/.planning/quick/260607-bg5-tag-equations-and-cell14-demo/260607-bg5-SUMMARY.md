---
quick_id: 260607-bg5
slug: tag-equations-and-cell14-demo
status: complete
date: "2026-06-07"
commit: 61dfb39
---

# Summary — 260607-bg5

## Task A: Ecuaciones numeradas
Added `\tag{1}`–`\tag{10}` to 10 key display equations in `index.md`:
- \tag{1} Shannon capacity
- \tag{2} Coding gain G_c
- \tag{3} LLR definition λ_v
- \tag{4} BP variable→check message
- \tag{5} BP check→variable message (arctanh)
- \tag{6} Bhattacharyya Z(W_2^-)
- \tag{7} Bhattacharyya Z(W_2^+)
- \tag{8} Arıkan polarization theorem
- \tag{9} SC f function
- \tag{10} SC g function

MkDocs --strict build passes.

## Task B: Cell 14 alignment
- Fixed G matrix in `sc_decode_n4` and demo: lower-triangular kron(F,F)
  → upper-triangular kron(F^T,F^T) matching §4.2 butterfly convention
- Encoding now produces x=[1,0,1,0] from u=[0,0,1,0] as in §4.2
- Added deterministic §4.2 trace: all 4 stages printed with exact values
  (g02=-4.4, g13=+3.6, LLR(u3)=+8.0 match §4.2 exactly)
- f_func values differ slightly (exact arctanh vs §4.2 min-sum approximation)
  but sign is correct — decisions are identical
- Added 100-block MC test at 5 dB

## Note
The kron convention mismatch between cell 14 (upper triangular, §4.2-compatible)
and cell 15 (lower triangular, kron(G,F) convention) remains — fixing cell 15/17
is the separate Phase 4 SC/SCL decoder bug task.
