# Informe de Auditoría — Sesión 03 OFDM

**Fase:** 01 — Auditoría y Diagnóstico
**Fecha:** 2026-05-22
**Archivos auditados:** `index.md`, `lab.ipynb`, `figures/`
**Resultado global del notebook:** LIMPIO (exit 0, sin errores de celda)

---

## Resumen ejecutivo

| Categoría | BLOCKERs | MINORs |
|-----------|----------|--------|
| Fórmulas y enunciados incorrectos | 2 | 1 |
| Referencias de figuras (rotas / huérfanas) | 3 | 1 |
| Snippets de código desalineados | 0 | 2 |
| Estado del notebook | 0 | 0 |
| **TOTAL** | **5** | **4** |

**Criterio de severidad:**
- **BLOCKER** — impide dictar la clase: fórmula falsa, figura rota al renderizar, resultado numérico erróneo si el estudiante aplica la fórmula
- **MINOR** — inconsistencia que no confunde al estudiante: variable renombrada, snippet sin firma de función, figura generada no referenciada

Cada hallazgo es independientemente corregible en Fase 2 sin releer `index.md`.

---

## 1. Fórmulas y Enunciados Incorrectos

**BLOCKER-S.01** — Factor de normalización incorrecto en demostración de ortogonalidad
- **Descripción:** La operación de demodulación del receptor usa factor `1/N` en lugar de `1/√N`. Con la IFFT normalizada (`norm='ortho'`, factor `1/√N`), el receptor debe aplicar también `1/√N`. El resultado actual de la fórmula es `X[k]/√N` en vez de `X[k]` — un estudiante que siga la derivación obtiene un resultado incorrecto.
- **Ubicación:** `index.md` línea 240 (§2 — Ortogonalidad)
- **Texto actual:**
  ```
  $$\frac{1}{N}\sum_{n=0}^{N-1} x[n]\, e^{-j2\pi kn/N} = \frac{1}{\sqrt{N}}\sum_{l=0}^{N-1} X[l] \underbrace{\left(\frac{1}{N}\sum_{n=0}^{N-1} e^{j2\pi (l-k)n/N}\right)}_{\text{término de interferencia de }l\text{ sobre }k}$$
  ```

---

**BLOCKER-S.02** — Fórmula de eficiencia espectral con factor CP invertido
- **Descripción:** La fórmula simbólica de `η_neta` etiqueta `N_CP/(N+N_CP)` como "overhead CP" y lo usa como multiplicador directo de eficiencia. El factor correcto de eficiencia temporal es `N/(N+N_CP)`. Aplicando la fórmula escrita con N_CP=144, N=2048 se obtendría `η ≈ 0.066 × ... ≈ 0.22 bit/s/Hz`, en lugar de los `≈ 3.5 bit/s/Hz` que produce el cálculo numérico en la misma sección (línea 1037 usa correctamente `(1−0.066)`). La inconsistencia es interna: la fórmula y el número dicen cosas opuestas.
- **Ubicación:** `index.md` línea 1029 (§6 — Eficiencia Espectral)
- **Texto actual:**
  ```
  $$\eta_{\text{neta}} = \underbrace{\frac{N_{CP}}{N + N_{CP}}}_{\text{overhead CP}} \times \underbrace{\frac{N - N_{\text{guard}} - N_{\text{pilot}}}{N}}_{\text{overhead frecuencial}} \times \log_2 M \times r_c$$
  ```

---

**MINOR-01** — Factor `1/N` repetido en nota desplegable de ortogonalidad
- **Descripción:** La nota desplegable que desarrolla internamente la ortogonalidad aplica el mismo factor `1/N` al receptor, confirmando BLOCKER-S.01 en el desarrollo secundario. La nota es consistente con el cuerpo pero con el error.
- **Ubicación:** `index.md` línea 249 (§2 — nota desplegable)
- **Texto actual:**
  ```
  $$\frac{1}{N}\sum_{n=0}^{N-1} x[n]\, e^{-j2\pi kn/N} = \frac{1}{N}\sum_{n=0}^{N-1} \left(\frac{1}{\sqrt{N}} \sum_{l=0}^{N-1} X[l]\, e^{j2\pi ln/N}\right) e^{-j2\pi kn/N}$$
  ```

---

## 2. Referencias de Figuras (Rotas / Huérfanas)

### Inventario completo (verificado 2026-05-22)

Archivos en `figures/` (11): `channel-estimation-ls.png`, `cp-illustration.png`, `isi-problem.png`, `lte-resource-grid-pilots.png`, `mmse-vs-zf-constellation.png`, `ofdm-ber.png`, `ofdm-ifft-transmitter.png`, `ofdm-subcarriers.png`, `zf-equalizer-effect.png`, `zf-equalizer-qam-comparison.png`, `zf-noise-amplification.png`.

| Línea | Ruta referenciada | En disco | Estado |
|-------|-------------------|----------|--------|
| 60 | figures/isi-problem.png | SÍ | OK |
| 234 | figures/ofdm-ifft-transmitter.png | SÍ | OK |
| 308 | figures/ofdm-subcarriers.png | SÍ | OK |
| 405 | figures/cp-illustration.png | SÍ | OK |
| 739 | figures/zf-equalizer-effect.png | SÍ | OK |
| 753 | figures/zf-equalizer-qam-comparison.png | SÍ | OK |
| 782 | figures/zf-noise-amplification.png | SÍ | OK |
| 814 | figures/ofdm-ber-equalizers.png | NO | **ROTA** (1.ª ref) |
| 840 | figures/channel-estimation-ls.png | SÍ | OK |
| 868 | figures/lte-resource-grid-pilots.png | SÍ | OK |
| 953 | figures/ofdm-ber-equalizers.png | NO | **ROTA** (2.ª ref) |
| 961 | figures/ofdm-per-subcarrier-ber.png | NO | **ROTA** |

Huérfanas en disco (sin referenciar): `figures/mmse-vs-zf-constellation.png`

> **Nota para Fase 2:** Las figuras `ofdm-ber-equalizers.png` y `ofdm-per-subcarrier-ber.png` son generadas por `lab.ipynb` al ejecutar `Run All` (celdas `a602f4ca`/`cell-16-ex4-code` y `cell-19-ex5-code`). La solución en Fase 2 es ejecutar el notebook una vez para generar las figuras en `figures/`, no renombrar archivos existentes.

---

**BLOCKER-S.03** — Referencia rota a `figures/ofdm-ber-equalizers.png` (primera aparición)
- **Descripción:** El archivo no existe en disco; la figura no carga al renderizar MkDocs. Impide ver la comparación BER ZF vs MMSE en §4.7.
- **Ubicación:** `index.md` línea 814 (§4.7 — Ecualización ZF)
- **Texto actual:** `![BER ZF vs MMSE](figures/ofdm-ber-equalizers.png)`

---

**BLOCKER-S.04** — Referencia rota a `figures/ofdm-ber-equalizers.png` (segunda aparición)
- **Descripción:** Mismo archivo faltante; segunda instancia en §4.8. El estudiante ve dos figuras vacías en dos secciones distintas.
- **Ubicación:** `index.md` línea 953 (§4.8 — MMSE)
- **Texto actual:** `![BER OFDM end-to-end: ZF vs MMSE vs AWGN](figures/ofdm-ber-equalizers.png)`

---

**BLOCKER-S.05** — Referencia rota a `figures/ofdm-per-subcarrier-ber.png`
- **Descripción:** El archivo no existe en disco; la figura de BER por subportadora no carga. Impide visualizar el ejercicio final §Ej.5.
- **Ubicación:** `index.md` línea 961 (§Ejercicios finales)
- **Texto actual:** `![BER por subportadora](figures/ofdm-per-subcarrier-ber.png)`

---

**MINOR-02** — Figura huérfana `figures/mmse-vs-zf-constellation.png`
- **Descripción:** Existe en disco (generada por celda `81830cd0`), no está referenciada en `index.md`. No confunde al estudiante pero ocupa espacio sin uso pedagógico. Fase 2 puede agregar la referencia o ignorar.
- **Ubicación:** `figures/mmse-vs-zf-constellation.png` (sin referencia en `index.md`)

---

## 3. Snippets de Código Desalineados

### Inventario completo (7 snippets canónicos verificados)

| Líneas en index.md | Celda notebook | Función | Estado |
|--------------------|----------------|---------|--------|
| 574–580 | `a5c7793d` | `qpsk_map(bits)` | OK |
| 618–623 | `11d893ff` | `ofdm_tx(X, N_CP)` | OK |
| 648–651 | `3ee4d17a` | `apply_channel(x_signal, h)` | OK |
| 681–685 | `da295e7a` | `ofdm_rx_no_channel(y_received, N, N_CP)` | OK — diferencia de nombre de parámetro no funcional (D-05) |
| 756–759 | `11e22143` | `zf_equalizer(Y, h, N)` | OK |
| 806–808 | `81830cd0` | MMSE equalizer | MINOR — ver MINOR-03 |
| 886–895 | `23ad1479` | LS channel estimate | MINOR — ver MINOR-04 |

---

**MINOR-03** — MMSE: código inline en index.md vs función invocable en notebook
- **Descripción:** `index.md` presenta el cálculo MMSE como código inline (sin firma de función); `lab.ipynb` define `mmse_equalizer(Y, h, N, SNR_dB)` invocable. La lógica matemática es equivalente pero la API difiere. Un estudiante que copie el snippet de `index.md` no obtendrá el mismo resultado que llamar la función del notebook.
- **Ubicación:** `index.md` líneas 806–808 ↔ `lab.ipynb` celda `81830cd0`
- **Texto actual (index.md):**
  ```python
  SNR_lin   = 10 ** (SNR_dB / 10)
  X_hat     = (np.conj(H) / (np.abs(H)**2 + 1/SNR_lin)) * Y
  ```
- **Texto actual (lab.ipynb):**
  ```python
  def mmse_equalizer(Y, h, N, SNR_dB):
      """MMSE: regulariza la inversión del canal → limita amplificación de ruido en fades."""
      H   = np.fft.fft(h, n=N)
      SNR = 10 ** (SNR_dB / 10)
      return (np.conj(H) / (np.abs(H)**2 + 1/SNR)) * Y
  ```

---

**MINOR-04** — LS channel estimate: código inline en index.md vs función invocable en notebook
- **Descripción:** `index.md` presenta la estimación LS como código inline; `lab.ipynb` define `ls_channel_estimate(Y, pilot_idx, X_pilot, N)` con interpolación explícita real/imag. La diferencia de API (sin callable vs función) es funcional por D-05; el cómputo produce resultados idénticos en NumPy ≥1.17.
- **Ubicación:** `index.md` líneas 886–895 ↔ `lab.ipynb` celda `23ad1479`
- **Texto actual (index.md):**
  ```python
  pilot_spacing = 8
  pilot_idx     = np.arange(0, N, pilot_spacing)
  X_pilot       = np.ones(len(pilot_idx))

  H_ls  = Y[pilot_idx] / X_pilot
  H_est = np.interp(np.arange(N), pilot_idx, H_ls)
  ```
- **Texto actual (lab.ipynb):**
  ```python
  def ls_channel_estimate(Y, pilot_idx, X_pilot, N):
      """Estimación LS en pilotos + interpolación lineal a todas las subportadoras."""
      H_ls = Y[pilot_idx] / X_pilot
      H_est = (np.interp(np.arange(N), pilot_idx, H_ls.real) +
               1j * np.interp(np.arange(N), pilot_idx, H_ls.imag))
      return H_est
  ```

---

## 4. Estado del Notebook (lab.ipynb)

**Método:** `jupyter nbconvert --execute lab.ipynb --output lab.executed.ipynb --ExecutePreprocessor.timeout=180`
**Resultado global:** **LIMPIO** — exit code 0, sin errores de celda
**Figuras generadas:** 12 llamadas `plt.savefig` ejecutadas exitosamente
**Ground truth preservado:** `git diff -- lab.ipynb` vacío; `lab.executed.ipynb` eliminado tras verificación

> No se registran BLOCKERs ni MINORs en esta categoría.

---

## Validación contra Criterios de Éxito (Roadmap §Phase 1)

| # | Criterio | Estado |
|---|----------|--------|
| 1 | Lista de enunciados falsos y fórmulas incorrectas con sección y línea | ✓ CUMPLIDO — Sección 1: 2 BLOCKERs con líneas exactas |
| 2 | Lista de referencias a figuras cruzada contra `figures/` | ✓ CUMPLIDO — Sección 2: tabla de 12 refs, 3 rotas marcadas |
| 3 | Diff conceptual de snippets Python index.md vs lab.ipynb | ✓ CUMPLIDO — Sección 3: 7 snippets verificados, 2 MINORs |
| 4 | Registro de ejecución de lab.ipynb con número de celda de cualquier fallo | ✓ CUMPLIDO — Sección 4: LIMPIO, 0 errores de celda |

**Todos los criterios de éxito de Fase 1 están cubiertos.**

---

## Checklist para Fase 2

Los siguientes ítems son la lista de trabajo de Fase 2 (CORR-01, CORR-02, CORR-03, LAB-01):

- [ ] **BLOCKER-S.01** — Corregir factor `1/N` → `1/√N` en línea 240 de index.md (§2)
- [ ] **BLOCKER-S.02** — Corregir fórmula η_neta: `N_CP/(N+N_CP)` → `N/(N+N_CP)` en línea 1029 de index.md (§6)
- [ ] **BLOCKER-S.03** — Resolver figura faltante `ofdm-ber-equalizers.png` para línea 814 (ejecutar notebook)
- [ ] **BLOCKER-S.04** — Resolver figura faltante `ofdm-ber-equalizers.png` para línea 953 (mismo archivo que S.03)
- [ ] **BLOCKER-S.05** — Resolver figura faltante `ofdm-per-subcarrier-ber.png` para línea 961 (ejecutar notebook)
- [ ] **MINOR-01** — Corregir factor `1/N` en nota desplegable línea 249 (consistente con S.01)
- [ ] **MINOR-02** — Decidir sobre `mmse-vs-zf-constellation.png`: referenciar en index.md o ignorar
- [ ] **MINOR-03** — Alinear snippet MMSE de líneas 806–808 con firma de función del notebook
- [ ] **MINOR-04** — Alinear snippet LS de líneas 886–895 con firma de función del notebook
