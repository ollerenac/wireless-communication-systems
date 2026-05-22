# Fragmento — Estado del Notebook (lab.ipynb)

## 4. Estado del Notebook (lab.ipynb)

**Fecha de auditoría:** 2026-05-22
**Método de ejecución:** jupyter nbconvert --execute (kernel Python 3, timeout 180s por celda)
**Resultado global:** LIMPIO <!-- Resultado global: LIMPIO -->

### 4.1 Hallazgos de ejecución

- Sin errores. Todas las celdas se ejecutaron exitosamente de punta a punta.

El comando ejecutado fue:
```bash
cd /home/researcher/Teaching/uni/2026/wireless-communication-systems/docs/sessions/03-ofdm-systems
jupyter nbconvert --to notebook --execute lab.ipynb --output lab.executed.ipynb --ExecutePreprocessor.timeout=180
```

Salida del log: `[NbConvertApp] Writing 1523309 bytes to lab.executed.ipynb` (exit code 0).

El archivo temporal `lab.executed.ipynb` fue eliminado tras la verificación. `git diff -- lab.ipynb` está vacío.

### 4.2 Inventario de figuras generadas por el notebook vs disco

| `plt.savefig(...)` en celda | Archivo generado | Existe en `figures/` tras ejecución | Referenciada en `index.md` |
|---|---|---|---|
| `11e22143` | `figures/zf-equalizer-effect.png` | Sí | Sí (línea 739) |
| `11e22143` | `figures/zf-equalizer-qam-comparison.png` | Sí | Sí (línea 753) |
| `81830cd0` | `figures/mmse-vs-zf-constellation.png` | Sí | No (huérfana — no referenciada en index.md) |
| `2fd4f44b` | `figures/qpsk-decision-regions.png` | Sí | No (huérfana — no referenciada en index.md) |
| `a602f4ca` | `figures/ofdm-ber-equalizers.png` | Sí | Sí (líneas 814 y 953) |
| `cell-08-ex1-code` | `figures/ofdm-time-domain.png` | Sí | No (huérfana — no referenciada en index.md) |
| `cell-13-ex3-code` | `figures/cp-effect-constellation.png` | Sí | No (huérfana — no referenciada en index.md) |
| `cell-16-ex4-code` | `figures/ofdm-ber-equalizers.png` | Sí | Sí (líneas 814 y 953) — sobreescribe la versión de `a602f4ca` con mayor resolución |
| `eecd25a6` | `figures/channel-estimation-pilots.png` | Sí | No (huérfana — no referenciada en index.md; `channel-estimation-ls.png` sí está referenciada en línea 840) |
| `cell-19-ex5-code` | `figures/ofdm-per-subcarrier-ber.png` | Sí | Sí (línea 961) |
| `cell-19-ex5-code` | `figures/ofdm-subcarriers.png` | Sí | Sí (línea 308) |
| `cell-19-ex5-code` | `figures/cp-illustration.png` | Sí | Sí (línea 405) |

**Figuras generadas por el notebook que no existían en disco antes de la ejecución:**
- `figures/ofdm-ber-equalizers.png` (referenciada en index.md líneas 814, 953) — CONFIRMADO GENERADA
- `figures/ofdm-per-subcarrier-ber.png` (referenciada en index.md línea 961) — CONFIRMADO GENERADA
- `figures/channel-estimation-pilots.png` (no referenciada en index.md) — CONFIRMADO GENERADA
- `figures/cp-effect-constellation.png` (no referenciada en index.md) — CONFIRMADO GENERADA
- `figures/qpsk-decision-regions.png` (no referenciada en index.md) — CONFIRMADO GENERADA
- `figures/ofdm-time-domain.png` (no referenciada en index.md) — CONFIRMADO GENERADA

**Figuras en disco que el notebook actualiza (ya existían):**
- `figures/zf-equalizer-effect.png`, `figures/zf-equalizer-qam-comparison.png`, `figures/mmse-vs-zf-constellation.png`, `figures/ofdm-subcarriers.png`, `figures/cp-illustration.png`

### 4.3 Observación crítica

Tras ejecución limpia el archivo `figures/ofdm-ber-equalizers.png` aparece en disco (generado por celda `a602f4ca` y sobreescrito con mayor resolución por `cell-16-ex4-code`). Esto confirma la observación del CONTEXT.md:

**La ausencia previa de `ofdm-ber-equalizers.png` se debe a que el notebook no se había ejecutado desde la última reorganización. Tras Run All, el archivo se regenera. Esto NO invalida los BLOCKERs de Sección 2 (las referencias rotas existen mientras el notebook no se re-ejecute en CI). La referencia en index.md (líneas 814 y 953) queda funcional solo si el notebook se ha ejecutado previamente en el mismo directorio.**

Lo mismo aplica a `figures/ofdm-per-subcarrier-ber.png` (referenciada en index.md línea 961, generada por `cell-19-ex5-code`).

**Figura huérfana confirmada:** `figures/channel-estimation-pilots.png` (generada por celda `eecd25a6`) existe tras la ejecución pero no está referenciada en `index.md`. La figura referenciada en index.md línea 840 es `figures/channel-estimation-ls.png`, que ya existía en disco y NO es generada por el notebook — es una figura estática pre-existente.

---

Total de hallazgos: 0 blockers, 0 minors
