# Fragmento — Referencias de Figuras (Rotas / Huérfanas)

## 2. Referencias de Figuras (Rotas / Huérfanas)

### 2.1 Inventario completo de referencias

Verificado contra `ls figures/` en disco el 2026-05-22.
Archivos en disco (11): `channel-estimation-ls.png`, `cp-illustration.png`, `isi-problem.png`, `lte-resource-grid-pilots.png`, `mmse-vs-zf-constellation.png`, `ofdm-ber.png`, `ofdm-ifft-transmitter.png`, `ofdm-subcarriers.png`, `zf-equalizer-effect.png`, `zf-equalizer-qam-comparison.png`, `zf-noise-amplification.png`.

| Línea | Ruta referenciada                            | En disco | Estado             |
|-------|----------------------------------------------|----------|--------------------|
| 60    | figures/isi-problem.png                      | SÍ       | OK                 |
| 234   | figures/ofdm-ifft-transmitter.png            | SÍ       | OK                 |
| 308   | figures/ofdm-subcarriers.png                 | SÍ       | OK                 |
| 405   | figures/cp-illustration.png                  | SÍ       | OK                 |
| 739   | figures/zf-equalizer-effect.png              | SÍ       | OK                 |
| 753   | figures/zf-equalizer-qam-comparison.png      | SÍ       | OK                 |
| 782   | figures/zf-noise-amplification.png           | SÍ       | OK                 |
| 814   | figures/ofdm-ber-equalizers.png              | NO       | **ROTA** (1.ª ref) |
| 840   | figures/channel-estimation-ls.png            | SÍ       | OK                 |
| 868   | figures/lte-resource-grid-pilots.png         | SÍ       | OK                 |
| 953   | figures/ofdm-ber-equalizers.png              | NO       | **ROTA** (2.ª ref) |
| 961   | figures/ofdm-per-subcarrier-ber.png          | NO       | **ROTA**           |

Archivos en `figures/` sin referenciar (huérfanos):
- `figures/mmse-vs-zf-constellation.png` — existe en disco; no está referenciada en `index.md`

### 2.2 Hallazgos

**BLOCKER-01**: Referencia rota a `figures/ofdm-ber-equalizers.png` (primera aparición, línea 814) — el archivo no existe en disco; la figura no carga al renderizar MkDocs.
- **Ubicación:** `index.md` línea 814
- **Texto actual:** `![BER ZF vs MMSE](figures/ofdm-ber-equalizers.png)`

---

**BLOCKER-02**: Referencia rota a `figures/ofdm-ber-equalizers.png` (segunda aparición, línea 953) — mismo archivo faltante; segunda instancia invisible al estudiante.
- **Ubicación:** `index.md` línea 953
- **Texto actual:** `![BER OFDM end-to-end: ZF vs MMSE vs AWGN](figures/ofdm-ber-equalizers.png)`

---

**BLOCKER-03**: Referencia rota a `figures/ofdm-per-subcarrier-ber.png` (línea 961) — el archivo no existe en disco; la figura no carga al renderizar MkDocs.
- **Ubicación:** `index.md` línea 961
- **Texto actual:** `![BER por subportadora](figures/ofdm-per-subcarrier-ber.png)`

---

**MINOR-01**: Figura huérfana `figures/mmse-vs-zf-constellation.png` — existe en disco pero no está referenciada en `index.md`; no confunde al estudiante pero es capacidad generada sin uso.
- **Ubicación:** `figures/mmse-vs-zf-constellation.png`
- **Texto actual:** (sin referencia en index.md; generada por lab.ipynb celda `81830cd0`)

---

Total de hallazgos: 3 blockers, 1 minors
