# Fragmento — Snippets de Código Desalineados

## 3. Snippets de Código Desalineados

### 3.1 Inventario verificado snippet ↔ celda

| Línea en index.md | Celda en notebook | Función | Estado |
|---|---|---|---|
| 574–580 | `a5c7793d` | `qpsk_map(bits)` | OK |
| 618–623 | `11d893ff` | `ofdm_tx(X, N_CP)` | OK |
| 648–651 | `3ee4d17a` | `apply_channel(x_signal, h)` | OK |
| 681–685 | `da295e7a` | `ofdm_rx_no_channel(y_received, N, N_CP)` | OK |
| 756–759 | `11e22143` | `zf_equalizer(Y, h, N)` | OK |
| 806–808 | `81830cd0` | MMSE equalizer (inline vs `mmse_equalizer(Y, h, N, SNR_dB)`) | FUNCIONAL-MISMATCH |
| 886–895 | `23ad1479` | LS estimate (inline vs `ls_channel_estimate(Y, pilot_idx, X_pilot, N)`) | FUNCIONAL-MISMATCH |

**Notas sobre decisiones:**

- **Línea 681–685 / celda `da295e7a`:** `index.md` usa `def ofdm_rx_no_channel(y_received, N, N_CP)`, la celda usa `def ofdm_rx_no_channel(x_with_cp, N, N_CP)`. Solo el nombre del primer parámetro difiere (`y_received` vs `x_with_cp`); el orden, cantidad y tipo son idénticos. Según D-05 (diferencias de nombres de variables no son funcionales) → **NO se reporta**.
- **Líneas 806–808 / celda `81830cd0`:** `index.md` presenta código inline sin función; la celda define `mmse_equalizer(Y, h, N, SNR_dB)`. La fórmula matemática es equivalente pero la API difiere (sin callable vs función invocable). → **FUNCIONAL-MISMATCH** (MINOR).
- **Líneas 886–895 / celda `23ad1479`:** `index.md` presenta código inline sin función; la celda define `ls_channel_estimate(Y, pilot_idx, X_pilot, N)`. La interpolación de `np.interp` directa sobre valores complejos (index.md) produce resultados idénticos a la interpolación separada real/imag (notebook, NumPy ≥1.17) — diferencia NO funcional en el cómputo. La API sí difiere (sin callable vs función). → **FUNCIONAL-MISMATCH** (MINOR).

---

### 3.2 Hallazgos

**MINOR-01**: El bloque MMSE en `index.md` muestra código inline sin definición de función, mientras que `lab.ipynb` define una función invocable `mmse_equalizer(Y, h, N, SNR_dB)`.
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

**MINOR-02**: El bloque LS de estimación de canal en `index.md` muestra código inline sin definición de función, mientras que `lab.ipynb` define `ls_channel_estimate(Y, pilot_idx, X_pilot, N)` con interpolación compleja explícita.
- **Ubicación:** `index.md` líneas 886–895 ↔ `lab.ipynb` celda `23ad1479`
- **Texto actual (index.md):**
  ```python
  pilot_spacing = 8
  pilot_idx     = np.arange(0, N, pilot_spacing)
  X_pilot       = np.ones(len(pilot_idx))            # pilotos BPSK: valor conocido = +1

  # Estimación LS en posiciones piloto
  H_ls = Y[pilot_idx] / X_pilot

  # Interpolación lineal al resto de subportadoras
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

Total de hallazgos: 0 blockers, 2 minors
