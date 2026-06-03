# Requirements — Sesión 04: Codificación de Canal

## v1 Requirements

### Figuras (index.md)

- [ ] **FIG-01**: Convertir todas las referencias `![alt](path)` a `<figure markdown="span">` con `<figcaption markdown="1">` detallada, igual que la sesión 03
- [ ] **FIG-02**: `shannon-capacity.png` — versión publicable con puntos de operación por modulación, colormap consistente, leyenda detallada
- [ ] **FIG-03**: `waterfall-curves.png` — curvas BER waterfall LDPC (r=1/2, 2/3, 3/4) y Polar vs BPSK sin código, anotadas
- [ ] **FIG-04**: `tanner-graph.png` — grafo bipartito LDPC con nodos de variable (círculos) y verificación (cuadrados), anotado con $H_{ij}=1$ en aristas
- [ ] **FIG-05**: `bp-messages.png` — iteraciones de belief propagation: LLRs iniciales → mensajes tras 1/3/10 iteraciones mostrando convergencia
- [ ] **FIG-06**: `polar-butterfly.png` — transformación $G_2$ y composición recursiva hasta $G_4$ o $G_8$, con los canales sintéticos etiquetados
- [ ] **FIG-07**: `polar-polarization.png` — evolución del parámetro $Z(W_N^{(i)})$ para N=64 o N=128: histograma de canales sintéticos mostrando la polarización (bimodal hacia 0 y 1)
- [ ] **FIG-08**: `ldpc-ber-waterfall.png` — curvas BER Monte Carlo del código LDPC real (n≈400 bits) a distintas tasas: visibilidad del waterfall cliff y del error floor
- [ ] **FIG-09**: `ofdm-ldpc-ber.png` — BER end-to-end en canal frequency-selective: OFDM sin FEC vs OFDM+LDPC vs límite AWGN

### Índice (index.md)

- [x] **IDX-01**: Añadir ganchos narrativos "La pregunta natural es…" al cierre de §3.2 (BP) y §4.2 (SC) conectando con la sección siguiente, igual que cada sub-sección de la sesión 03
- [ ] **IDX-02**: Reescribir sección "Laboratorio Python" para describir los 6 ejercicios reales del notebook con tiempo estimado
- [ ] **IDX-03**: Verificar referencias cruzadas con sesiones 01-03 (sin referencias a secciones inexistentes)
- [ ] **IDX-04**: Asegurar que cada figura del index.md tiene una celda correspondiente en el notebook que la genera

### Notebook (lab.ipynb)

- [ ] **LAB-01**: **Ej 3 — LDPC BP realista**: implementar BP completo sobre un código LDPC de n≈400 bits (H dispersa real o generada), 3-15 iteraciones, visualizar convergencia de LLRs, generar `bp-messages.png` y `ldpc-ber-waterfall.png`
- [ ] **LAB-02**: **Ej 4 — Polar N=64**: encoder completo (matriz $G_{64}$), selección de bits congelados por Z de Bhattacharyya, decodificador SC con árbol factor recursivo, comparar SC vs SCL-L=8, generar `polar-polarization.png`
- [ ] **LAB-03**: **Ej 6 — Integrador OFDM+FEC**: reutilizar `ofdm_tx`, `apply_channel`, `ofdm_rx_no_channel`, `zf_equalizer` de la sesión 03; añadir capa LDPC codec; simular BER coded vs uncoded; generar `ofdm-ldpc-ber.png`
- [ ] **LAB-04**: Notebook ejecutable de principio a fin sin errores (orden correcto de celdas, sin undefined variables)
- [ ] **LAB-05**: Ejercicio 1 (Shannon) y Ejercicio 6 (waterfall) actualizados para generar versiones publicables de `shannon-capacity.png` y `waterfall-curves.png`

## v2 Requirements (deferred)

- Implementación HARQ con Chase combining (sesión 05)
- Decodificador BP con aceleración (min-sum approximation)
- SCL con L=32 para mostrar convergencia al límite ML
- Análisis EXIT charts (nivel investigación)

## Out of Scope

- Turbo codes — reemplazados por LDPC en 5G NR; no hay justificación pedagógica suficiente dado el tiempo
- Viterbi / convolutional codes — pre-4G, fuera del alcance del curso
- Implementación hardware-aware del decodificador LDPC (layered decoding, etc.)
- Rate-matching detallado de 3GPP TS 38.212 — nivel de implementación, no de comprensión

## Traceability

| REQ | Phase |
|-----|-------|
| FIG-01, IDX-01, IDX-02, IDX-03 | Phase 1: Index.md polish |
| FIG-02, FIG-03, LAB-05 | Phase 2: Existing figures polish |
| FIG-04, FIG-05, LAB-01 | Phase 3: LDPC figures + BP simulation |
| FIG-06, FIG-07, LAB-02 | Phase 4: Polar figures + SC/SCL simulation |
| FIG-08 | Phase 3 (output of LAB-01) |
| FIG-09, LAB-03 | Phase 5: OFDM+FEC integrator |
| IDX-04, LAB-04 | Phase 6: Integration & QA |
