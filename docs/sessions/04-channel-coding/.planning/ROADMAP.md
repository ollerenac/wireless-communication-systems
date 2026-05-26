# Roadmap — Sesión 04: Codificación de Canal

## Summary

**6 phases** | **14 requirements mapped** | All v1 requirements covered ✓

| # | Phase | Goal | Requirements | Success Criteria |
|---|-------|------|--------------|------------------|
| 1 | Index Polish | 1/3 | In Progress|  |
| 2 | Figuras existentes | shannon-capacity y waterfall-curves publicables con `<figure>` | FIG-02, FIG-03, LAB-05 | 3 |
| 3 | LDPC Lab + Figuras | BP completo realista con Monte Carlo BER y figuras de BP | FIG-04, FIG-05, FIG-08, LAB-01 | 4 |
| 4 | Polar Lab + Figuras | Polar N=64 encoder+SC+SCL con figuras de polarización | FIG-06, FIG-07, LAB-02 | 3 |
| 5 | Integrador OFDM+FEC | Ejercicio end-to-end OFDM+LDPC con figura comparativa | FIG-09, LAB-03 | 3 |
| 6 | QA & Publicación | Notebook ejecutable limpio, index.md sin errores, listo para site | LAB-04, IDX-04 | 3 |

---

### Phase 1: Index Polish

**Goal:** El `index.md` tiene la misma calidad narrativa y estructura que la sesión 03 — ganchos entre secciones, lab section alineada con el notebook real, referencias cruzadas verificadas.

**Requirements:** IDX-01, IDX-02, IDX-03, FIG-01

**Plans:** 1/3 plans executed

Plans:
- [x] 01-01-PLAN.md — Hooks narrativos "La pregunta natural es..." en §1, §2, §3.1, §3.2, §3.3, §4.1, §4.2, §4.3, §5
- [ ] 01-02-PLAN.md — Lab section rewrite (6 ejercicios target) + auditoría admonitions de solución
- [ ] 01-03-PLAN.md — Conversión figuras a `<figure>` + placeholder tanner-graph + corrección factual intro

**Success Criteria:**
1. Cada sub-sección de §3 y §4 termina con "La pregunta natural es…" conectando con la siguiente
2. La sección "Laboratorio Python" describe exactamente los 6 ejercicios del notebook con tiempos estimados
3. Todas las referencias a `figures/` usan `<figure markdown="span">` con `<figcaption markdown="1">` de al menos 2 líneas

---

### Phase 2: Figuras Existentes Polished

**Goal:** Las dos figuras actuales (`shannon-capacity.png`, `waterfall-curves.png`) alcanzan la calidad visual de las 13 figuras de la sesión 03 — generadas por código con colores consistentes, anotaciones y leyendas integradas.

**Requirements:** FIG-02, FIG-03, LAB-05

**Success Criteria:**
1. `shannon-capacity.png` muestra la curva de Shannon + puntos de operación por modulación con colormap consistente con sesión 02/03 y leyenda descriptiva
2. `waterfall-curves.png` muestra ≥3 tasas LDPC + ≥2 tasas Polar + BPSK sin código, con anotaciones de umbral visibles
3. Ambas figuras son generadas por celdas del notebook (LAB-05) y se almacenan en `figures/`

---

### Phase 3: LDPC Lab + Figuras

**Goal:** El ejercicio de LDPC en el notebook implementa BP sobre un código real (n≈400 bits), produce curvas BER Monte Carlo con waterfall visible, y genera las figuras de grafo de Tanner y mensajes BP.

**Requirements:** FIG-04, FIG-05, FIG-08, LAB-01

**Success Criteria:**
1. La celda LAB-01 implementa BP completo: inicialización de LLRs, mensajes variable→check y check→variable, decisión iterativa; converge en <15 iteraciones a SNR sobre umbral
2. `ldpc-ber-waterfall.png` muestra curvas Monte Carlo para ≥2 tasas con waterfall cliff claramente visible (salto de ≥3 décadas en BER en ≤2 dB)
3. `tanner-graph.png` y `bp-messages.png` son publicables y el index.md las referencia correctamente

---

### Phase 4: Polar Lab + Figuras

**Goal:** El ejercicio Polar en el notebook implementa el encoder $G_{64}$ y el decodificador SC/SCL-8, visualiza la polarización del canal, y genera las figuras de mariposa y polarización.

**Requirements:** FIG-06, FIG-07, LAB-02

**Success Criteria:**
1. La celda LAB-02 implementa el encoder Polar (N=64) y el decodificador SC recursivo correctamente: BER < BER teórica BPSK sin código a SNR > umbral
2. SCL con L=8 mejora visiblemente al SC básico en la región waterfall (diferencia ≥1 dB a BER=10⁻³)
3. `polar-polarization.png` muestra el histograma de $Z(W_N^{(i)})$ con polarización visible (modos en torno a 0 y 1)

---

### Phase 5: Integrador OFDM+FEC

**Goal:** El ejercicio 6 del notebook demuestra OFDM+LDPC end-to-end sobre un canal frequency-selective, conectando el transceptor de la sesión 03 con el codec de esta sesión.

**Requirements:** FIG-09, LAB-03

**Success Criteria:**
1. La celda LAB-03 reutiliza sin modificación las funciones `ofdm_tx`, `apply_channel`, `ofdm_rx_no_channel`, `zf_equalizer` de la sesión 03
2. `ofdm-ldpc-ber.png` muestra BER OFDM sin FEC, OFDM+LDPC, y límite AWGN en el mismo eje — ganancia de codificación visible (≥3 dB a BER=10⁻³)
3. El index.md §3.3 o §5 hace referencia a este resultado como cierre del arco OFDM→FEC

---

### Phase 6: QA & Publicación

**Goal:** El notebook ejecuta de principio a fin sin errores, el index.md pasa validación MkDocs, y toda la sesión está lista para dictar y publicar.

**Requirements:** LAB-04, IDX-04

**Success Criteria:**
1. `jupyter nbconvert --execute lab.ipynb` completa sin errores ni warnings críticos
2. Todas las referencias de figura en index.md apuntan a archivos que existen en `figures/`
3. El índice renderiza correctamente en MkDocs-Material (sin admonitions rotas, sin LaTeX malformado)
