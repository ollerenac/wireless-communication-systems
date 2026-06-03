---
phase: 4
slug: polar-lab-figuras
status: draft
nyquist_compliant: false
wave_0_complete: false
created: 2026-05-29
---

# Phase 04 — Validation Strategy

> Per-phase validation contract for feedback sampling during execution.

---

## Test Infrastructure

| Property | Value |
|----------|-------|
| **Framework** | Jupyter nbconvert + manual cell-execution |
| **Config file** | lab.ipynb (ground truth) |
| **Quick run command** | `jupyter nbconvert --to notebook --execute lab.ipynb --output lab_test.ipynb && echo OK` |
| **Full suite command** | `jupyter nbconvert --to notebook --execute --ExecutePreprocessor.timeout=120 lab.ipynb --output /tmp/lab_test.ipynb && python -c "import json; nb=json.load(open('/tmp/lab_test.ipynb')); errors=[c for c in nb['cells'] if any('ename' in o for o in c.get('outputs',[]))]  ; assert not errors, errors; print('All cells OK')"` |
| **Estimated runtime** | ~30 seconds |

---

## Sampling Rate

- **After every task commit:** Run `jupyter nbconvert --to script lab.ipynb --stdout 2>/dev/null | python 2>&1 | tail -5`
- **After every plan wave:** Run full suite command above
- **Before `/gsd:verify-work`:** Full suite must be green + all figures exist
- **Max feedback latency:** ~30 seconds

---

## Per-Task Verification Map

| Task ID | Plan | Wave | Requirement | Threat Ref | Secure Behavior | Test Type | Automated Command | File Exists | Status |
|---------|------|------|-------------|------------|-----------------|-----------|-------------------|-------------|--------|
| 04-01-01 | 01 | 1 | LAB-02 | — | N/A | exec | `python -c "import json; nb=json.load(open('lab.ipynb')); print(len(nb['cells']), 'cells')"` | ✅ | ⬜ pending |
| 04-01-02 | 01 | 1 | LAB-02 | — | N/A | exec | `ls figures/polar-butterfly.png` | ❌ W0 | ⬜ pending |
| 04-01-03 | 01 | 1 | FIG-06 | — | N/A | exec | `python -c "from PIL import Image; img=Image.open('figures/polar-butterfly.png'); assert img.size[0]>=1000"` | ❌ W0 | ⬜ pending |
| 04-02-01 | 02 | 2 | LAB-02 | — | N/A | exec | `ls figures/polar-polarization.png` | ❌ W0 | ⬜ pending |
| 04-02-02 | 02 | 2 | FIG-07 | — | N/A | exec | `python -c "from PIL import Image; img=Image.open('figures/polar-polarization.png'); assert img.size[0]>=1000"` | ❌ W0 | ⬜ pending |
| 04-02-03 | 02 | 2 | FIG-07 | — | N/A | exec | `grep -c "polar-butterfly\|polar-polarization\|polar-ber" index.md` | ✅ | ⬜ pending |

*Status: ⬜ pending · ✅ green · ❌ red · ⚠️ flaky*

---

## Wave 0 Requirements

- [ ] Verify `lab.ipynb` has 18 cells (baseline before Phase 4 adds 3 more)
- [ ] Verify `figures/` directory exists and has prior phase outputs (tanner-graph.png, bp-messages.png, etc.)
- [ ] Confirm Cell 14 defines `f_func`, `g_func`, `sc_decode_n4` (Phase 4 must REUSE these)
- [ ] Confirm `index.md` §4 has insertion points at lines ~229–231

*Existing infrastructure covers all phase requirements — no new test files needed.*

---

## Manual-Only Verifications

| Behavior | Requirement | Why Manual | Test Instructions |
|----------|-------------|------------|-------------------|
| Polar butterfly diagram shows correct N=8 factor graph with f/g nodes | FIG-06 | Visual correctness | Open figures/polar-butterfly.png; verify 3 stages, 8 leaves, f-nodes (top) and g-nodes (bottom with partial sums) |
| Polarization histogram shows bimodal distribution for N=64 | FIG-07 | Visual shape check | Open figures/polar-polarization.png; verify Z_i concentrates near 0 and 1 |
| BER curves show SC worse than SCL-L=8, both below uncoded | LAB-02 | Curve ordering | Open figures/polar-ber-curves.png; verify SCL-L=8 < SC < uncoded at Eb/N0 ≥ 3 dB |
| index.md §4 reads coherently end-to-end | LAB-02 | Narrative quality | Read §4.1 Polar Codes section; check figures render correctly in MkDocs preview |
| SC decoder produces correct codeword for N=4 test case u=[0,0,1,0] | LAB-02 | Algorithmic correctness | Run Cell 14 manually; verify u_hat = [0,0,1,0] at infinite SNR |

---

## Validation Sign-Off

- [ ] All tasks have `<automated>` verify or Wave 0 dependencies
- [ ] Sampling continuity: no 3 consecutive tasks without automated verify
- [ ] Wave 0 covers all MISSING references
- [ ] No watch-mode flags
- [ ] Feedback latency < 30s
- [ ] `nyquist_compliant: true` set in frontmatter

**Approval:** pending
