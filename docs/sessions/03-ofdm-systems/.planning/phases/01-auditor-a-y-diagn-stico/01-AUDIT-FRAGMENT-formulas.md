# Fragmento — Fórmulas y Enunciados Incorrectos

## 1. Fórmulas y Enunciados Incorrectos

**BLOCKER-01**: La operación de demodulación del receptor en la demostración de ortogonalidad usa factor `1/N` en lugar de `1/√N`, produciendo un resultado `X[k]/√N` en vez de `X[k]`.
- **Ubicación:** `index.md` línea 240
- **Texto actual:** "$$\frac{1}{N}\sum_{n=0}^{N-1} x[n]\, e^{-j2\pi kn/N} = \frac{1}{\sqrt{N}}\sum_{l=0}^{N-1} X[l] \underbrace{\left(\frac{1}{N}\sum_{n=0}^{N-1} e^{j2\pi (l-k)n/N}\right)}_{\text{término de interferencia de }l\text{ sobre }k}$$"

**BLOCKER-02**: La fórmula de eficiencia espectral neta etiqueta el factor `N_CP / (N + N_CP)` como "overhead CP" pero lo usa como multiplicador directo de eficiencia; el factor correcto de eficiencia temporal es `N / (N + N_CP)`. Aplicando la fórmula tal como está escrita con los valores del ejemplo (N_CP=144, N=2048) se obtendría `eta ≈ 0.066 × ... ≈ 0.22 bit/s/Hz` en lugar de los `≈ 3.5 bit/s/Hz` que produce el cálculo numérico en la misma sección (que usa correctamente `(1-0.066)`).
- **Ubicación:** `index.md` línea 1029
- **Texto actual:** "$$\eta_{\text{neta}} = \underbrace{\frac{N_{CP}}{N + N_{CP}}}_{\text{overhead CP}} \times \underbrace{\frac{N - N_{\text{guard}} - N_{\text{pilot}}}{N}}_{\text{overhead frecuencial}} \times \log_2 M \times r_c$$"

**MINOR-01**: En la demostración de ortogonalidad (nota desplegable), el desarrollo intermedio en línea 249 aplica el factor `1/N` a la operación del receptor, siendo consistente con BLOCKER-01; la nota interna ratifica el error del cuerpo principal.
- **Ubicación:** `index.md` línea 249
- **Texto actual:** "$$\frac{1}{N}\sum_{n=0}^{N-1} x[n]\, e^{-j2\pi kn/N} = \frac{1}{N}\sum_{n=0}^{N-1} \left(\frac{1}{\sqrt{N}} \sum_{l=0}^{N-1} X[l]\, e^{j2\pi ln/N}\right) e^{-j2\pi kn/N}$$"

---
Total de hallazgos: 2 blockers, 1 minors
