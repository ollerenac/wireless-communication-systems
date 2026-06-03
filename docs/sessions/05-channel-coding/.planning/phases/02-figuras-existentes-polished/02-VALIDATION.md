---
phase: 2
slug: figuras-existentes-polished
status: draft
nyquist_compliant: false
wave_0_complete: true
created: 2026-05-28
---

# Phase 2 — Validation Strategy

> Per-phase validation contract for feedback sampling during execution.

---

## Test Infrastructure

| Property | Value |
|----------|-------|
| **Framework** | Manual notebook execution (no pytest — outputs visuales) |
| **Config file** | none — ejecución directa del kernel Jupyter |
| **Quick run command** | `jupyter nbconvert --to notebook --execute lab.ipynb --ExecutePreprocessor.timeout=120 --output /tmp/test-04-ph2.ipynb` |
| **Full suite command** | Quick run + `python3 -c "import os; [print(f) or __import__('sys').exit(1) for f in ['figures/shannon-capacity.png','figures/waterfall-curves.png'] if os.path.getsize(f) < 5000]"` |
| **Estimated runtime** | ~5 seconds (curvas analíticas, sin Monte Carlo) |

---

## Sampling Rate

- **After every task commit:** Ejecutar la celda modificada en Jupyter, inspección visual de la figura generada, confirmar que `figures/nombre.png` existe y pesa >5 KB
- **After every plan wave:** Quick run command — notebook ejecuta Cells 1-13 sin errores
- **Before `/gsd:verify-work`:** Full suite must be green + inspección visual confirma calidad de figura (curvas separadas, leyenda legible, sin solapamiento de etiquetas)
- **Max feedback latency:** ~10 seconds (ejecución del notebook)

---

## Per-Task Verification Map

| Task ID | Plan | Wave | Requirement | Threat Ref | Secure Behavior | Test Type | Automated Command | File Exists | Status |
|---------|------|------|-------------|------------|-----------------|-----------|-------------------|-------------|--------|
| 02-01-T1 | 02-01 | 1 | LAB-05 | — | N/A | smoke | `jupyter nbconvert --to notebook --execute lab.ipynb --ExecutePreprocessor.cells_timeout=30 --output /tmp/t.ipynb 2>&1 | grep -c Error | grep ^0` | ✅ | ⬜ pending |
| 02-01-T2 | 02-01 | 1 | FIG-02 | — | N/A | smoke | `python3 -c "import os; assert os.path.getsize('figures/shannon-capacity.png') > 5000, 'FIG-02 too small'"` | ✅ sobreescribir | ⬜ pending |
| 02-02-T1 | 02-02 | 2 | FIG-03 | — | N/A | smoke | `python3 -c "import os; assert os.path.getsize('figures/waterfall-curves.png') > 5000, 'FIG-03 too small'"` | ✅ sobreescribir | ⬜ pending |
| 02-02-T2 | 02-02 | 2 | — | — | N/A | unit | `grep -c "generada por celda 13" index.md | grep -q ^1 && echo PASS` | ✅ | ⬜ pending |
| 02-02-T3 | 02-02 | 2 | LAB-05 | — | N/A | unit | `grep -q "Ejercicio 6 (waterfall)" .planning/REQUIREMENTS.md && echo PASS` | ✅ | ⬜ pending |

*Status: ⬜ pending · ✅ green · ❌ red · ⚠️ flaky*

---

## Wave 0 Requirements

Existing infrastructure covers all phase requirements. No test framework installation needed — el notebook se valida con `nbconvert` (ya disponible) y los archivos de figura se verifican con `python3 -c` inline.

*No Wave 0 stubs needed. All required tooling already present.*

---

## Manual-Only Verifications

| Behavior | Requirement | Why Manual | Test Instructions |
|----------|-------------|------------|-------------------|
| `shannon-capacity.png` muestra 5 puntos MCS con flechas de gap legibles y sin solapamiento de etiquetas QPSK | FIG-02 | Output visual — legibilidad no automatizable | Ejecutar Cell 3, abrir `figures/shannon-capacity.png`, confirmar: 5 scatter points de colores distintos, 5 flechas horizontales grises con valores en dB, etiquetas QPSK sin solapamiento |
| `waterfall-curves.png` muestra 6 curvas con waterfall cliff visible y 3 threshold markers legibles | FIG-03 | Output visual — separación y pendiente no automatizables | Ejecutar Cell 13, abrir `figures/waterfall-curves.png`, confirmar: BPSK negra + 3 azules LDPC + 2 naranjas Polar, cliff claro en cada curva codificada, 3 líneas grises en ~[-0.82, -0.55, -0.41] dB con etiquetas C(r=...) no solapadas |
| Coding gain visual ≥4 dB a BER=1e-5 vs BPSK sin código | FIG-03 | Apreciación visual de ganancia | En la figura waterfall: la curva LDPC r=1/2 a BER=1e-5 debe estar ≥4 dB a la izquierda del BPSK sin código |

---

## Validation Sign-Off

- [ ] All tasks have `<automated>` verify or Wave 0 dependencies
- [ ] Sampling continuity: no 3 consecutive tasks without automated verify
- [ ] Wave 0 covers all MISSING references
- [ ] No watch-mode flags
- [ ] Feedback latency < 10s
- [ ] `nyquist_compliant: true` set in frontmatter

**Approval:** pending
