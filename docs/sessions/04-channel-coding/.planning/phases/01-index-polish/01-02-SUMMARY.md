---
phase: 01-index-polish
plan: 02
subsystem: index.md
tags: [lab-section, admonitions, target-state, D-03, D-06]
dependency_graph:
  requires: [01-01]
  provides: [lab-section-target-state, admonition-audit-D06]
  affects: [index.md]
tech_stack:
  added: []
  patterns: [mkdocs-material-admonitions]
key_files:
  modified:
    - docs/sessions/04-channel-coding/index.md
decisions:
  - "D-03 aplicada: sección Laboratorio Python describe 6 ejercicios del estado target con tiempos ~15+15+30+35+15+30=140 min"
  - "D-06 aplicada: solo Ej1, Ej2, Ej5 conservan admonition de solución; Ej3, Ej4, Ej6 sin admonition"
metrics:
  duration: "2 min"
  completed: "2026-05-26"
  tasks_completed: 2
  files_modified: 1
---

# Phase 1 Plan 02: Lab Section Target-State + Admonition Audit Summary

**One-liner:** Sección "Laboratorio Python" reescrita con 6 ejercicios del estado target (~140 min) y auditoría D-06 que reduce admonitions de 6 a 3 (solo Ej1, Ej2, Ej5).

## Tasks Completed

| Task | Name | Commit | Files |
|------|------|--------|-------|
| 1 | Reescribir sección "Laboratorio Python" con 6 ejercicios target | 081e67f | index.md |
| 2 | Auditar y ajustar admonitions `??? example "Solución"` | 4145805 | index.md |

## What Was Built

### Task 1: Sección "Laboratorio Python" reescrita

La sección "Laboratorio Python" del `index.md` pasó de un borrador con 5 ejercicios (~90 min, contenido incorrecto) al estado target con 6 ejercicios (~140 min), descritos con la precisión suficiente para que un estudiante sepa exactamente qué implementar:

- **Ej.1** (~15 min): Curva Shannon C/B vs SNR con puntos de operación de modulaciones de Sesión 02 y límite de Eb/N0 = -1.59 dB
- **Ej.2** (~15 min): Matriz H en GF(2), verificación de codeword y detección de error por síndrome
- **Ej.3** (~30 min): LDPC BP completo (sum-product) sobre código n≈400 bits — curva BER Monte Carlo con al menos 3 décadas de caída
- **Ej.4** (~35 min): Polar N=64 con encoder G_64, decodificadores SC recursivo y SCL-L=8, comparación de curvas BER
- **Ej.5** (~15 min): Curvas waterfall comparativas LDPC (r_c=1/2, 2/3, 3/4) vs Polar vs BPSK sin código
- **Ej.6** (~30 min): Integrador OFDM+LDPC reutilizando funciones de Sesión 03 sin modificación, canal frequency-selective 5 taps

### Task 2: Auditoría de admonitions (D-06)

Aplicada la regla D-06: solo los ejercicios con solución matemática completa y compatible con el estado target conservan `??? example "Solución"`.

| Ejercicio | Decisión | Razón |
|-----------|----------|-------|
| Ej1 (Shannon) | MANTENER | Solución matemática completa, contenido compatible con target |
| Ej2 (LDPC paridad) | MANTENER | Solución matemática completa, contenido compatible con target |
| Ej3 (síndrome Hamming) | ELIMINAR | Target es BP n≈400 bits, sin implementación en notebook actual |
| Ej4 (Bhattacharyya N=8) | ELIMINAR | Target es Polar N=64 + SCL-L=8, sin implementación en notebook actual |
| Ej5 (waterfall BER) | MANTENER | Solución existente compatible con target (mismo concepto) |
| Ej6 (diseño 5G NR) | ELIMINAR | Target es OFDM+LDPC integrador, sin implementación Python todavía |

Resultado: 6 → 3 admonitions. Los enunciados de los Ejercicios 3, 4 y 6 permanecen intactos.

## Verification Results

```
grep -c "Ej\. [1-6]" index.md          → 6  ✓
grep -o "~[0-9]* min" index.md         → ~140, ~15, ~15, ~30, ~35, ~15, ~30 ✓
grep "140" index.md                     → encontrado en frase introductoria ✓
grep "n≈400" index.md                  → encontrado en Ej.3 ✓
grep "N=64" index.md                   → encontrado en Ej.4 ✓
grep "ofdm_tx\|zf_equalizer" index.md  → encontrado en Ej.6 ✓
grep -c '??? example "Solución"'       → 3 ✓ (Ej1, Ej2, Ej5 — posiciones 297, 327, 390)
```

## Deviations from Plan

None — plan ejecutado exactamente como estaba especificado.

## Known Stubs

La sección "Laboratorio Python" describe el estado target intencionalmente — el notebook `lab.ipynb` actual NO implementa los Ej3, Ej4, Ej6 descritos. Este es un stub documentado y deliberado: las Fases 3, 4 y 5 del roadmap implementarán el notebook hasta alcanzar la descripción del index. No bloquea el objetivo del plan (IDX-02) ya que el plan explícitamente ordena escribir para el estado target.

## Threat Flags

Ninguno — edición de texto narrativo en Markdown sin código ejecutable ni nuevas superficies de ataque.

## Self-Check: PASSED

- [x] `docs/sessions/04-channel-coding/index.md` modificado
- [x] Commit 081e67f existe: `feat(01-02): rewrite Laboratorio Python section with 6 target-state exercises`
- [x] Commit 4145805 existe: `feat(01-02): audit admonitions — remove solution blocks from Ej3, Ej4, Ej6 (D-06)`
- [x] 6 ejercicios target en sección Laboratorio Python
- [x] Tiempos: 15+15+30+35+15+30 = 140 min
- [x] Exactamente 3 admonitions `??? example "Solución"` (Ej1, Ej2, Ej5)
- [x] Enunciados Ej3, Ej4, Ej6 intactos
