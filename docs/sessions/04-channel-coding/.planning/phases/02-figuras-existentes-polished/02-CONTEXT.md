# Phase 2: Figuras Existentes Polished - Context

**Gathered:** 2026-05-28
**Status:** Ready for planning

<domain>
## Phase Boundary

Upgrade the two existing notebook cells (Ejercicio 1 — Shannon capacity, Ejercicio 6 — waterfall curves) to generate publication-quality PNG figures saved to `figures/`. This phase modifies `lab.ipynb` only — no changes to `index.md` beyond confirming the existing `<figure>` block for `waterfall-curves.png` is correct.

**Deliverables:**
- `figures/shannon-capacity.png` — publication-quality Shannon curve with 5G NR MCS operating points
- `figures/waterfall-curves.png` — multi-rate analytical BER waterfall (LDPC r=1/2, 2/3, 3/4 + Polar r=1/2, 3/4 + uncoded BPSK)
- Notebook cells that generate both figures via `plt.savefig(...)`

**Out of scope:** Full BP Monte Carlo simulation (Phase 3), Polar N=64 encoder (Phase 4), exercise renumbering, changes to `index.md` narrative, OFDM+LDPC integrator (Phase 5).

</domain>

<decisions>
## Implementation Decisions

### Shannon operating points — Figura `shannon-capacity.png` (FIG-02)

- **D-01:** Mostrar los siguientes puntos de operación del conjunto MCS de 5G NR — conecta directamente con la tabla MCS de la Sesión 02:
  - BPSK r=1/2 (η ≈ 0.5 bit/s/Hz, Eb/N0 ≈ 3 dB)
  - QPSK r=1/2 (η ≈ 1.0 bit/s/Hz, Eb/N0 ≈ 6 dB)
  - QPSK r=3/4 (η ≈ 1.5 bit/s/Hz, Eb/N0 ≈ 9 dB)
  - 16QAM r=1/2 (η ≈ 2.0 bit/s/Hz, Eb/N0 ≈ 13 dB)
  - 64QAM r=3/4 (η ≈ 4.5 bit/s/Hz, Eb/N0 ≈ 22 dB)
- **D-02:** Un color por orden de modulación con flechas de anotación:
  - BPSK → azul, QPSK → verde, 16QAM → naranja, 64QAM → rojo
  - Estos mismos colores se usan para curvas BER de las mismas modulaciones en Fases 3–5 (colormap global del curso)
  - Cada punto tiene `ax.annotate()` con flecha `->` apuntando a la coordenada exacta
- **D-03:** Flechas horizontales de "gap al límite de Shannon" para CADA punto de operación — muestra la distancia al límite de Shannon a la misma η. Este gap visualiza el potencial de mejora con mejores códigos.

### Waterfall simulation approach — Figura `waterfall-curves.png` (FIG-03)

- **D-04:** Usar **aproximaciones analíticas** (no Monte Carlo). Opciones:
  - LDPC: union bound sobre el waterfall cliff usando la distribución de peso del ensemble regular de Gallager, o equivalentemente, la curva Eb/N0 vs BER del canal BIAWGNC con capacity-achieving threshold marcado
  - Polar: curva de capacidad del canal sintético (Bhattacharyya bound) para visualizar el waterfall
  - Justificación: runs instantly, resultado limpio, se alinea con la duración de 15 min del Ejercicio 6. La simulación Monte Carlo real viene en Fase 3 (LAB-01, n≈400 bits, ≥10k trials).
- **D-05:** Tasas incluidas:
  - LDPC: r=1/2, r=2/3, r=3/4 (tres curvas)
  - Polar: r=1/2, r=3/4 (dos curvas)
  - BPSK sin código como baseline (curva Q(sqrt(2*Eb/N0)))
  - Total: 6 curvas en un solo eje
- **D-06:** Marcadores de umbral (threshold markers): una línea vertical discontinua en el Eb/N0 teórico de cada código, con etiqueta de texto que muestra el gap respecto al BPSK sin código. Permite leer la ganancia de codificación directamente del gráfico.

### Figure style

- **D-07:** `figsize=(10, 5)` para ambas figuras — más ancho que el actual (8,5), ligeramente más estrecho que sesión 03 (12,5). Acomoda las etiquetas de anotación sin saturar.
- **D-08:** `plt.savefig('figures/shannon-capacity.png', dpi=150, bbox_inches='tight')` y equivalente para waterfall. DPI=150 es el estándar de calidad para MkDocs-Material sin archivos excesivamente grandes.
- **D-09:** Actualización **mínima** del cell de setup (Cell 1): añadir `'figure.figsize': (10, 5)` al `rcParams.update({...})` existente. No cambiar otros parámetros — evita efectos no deseados en otras celdas.

### Exercise numbering (LAB-05)

- **D-10:** **Actualizar Ejercicio 6 en su lugar** — no renombrar ni reordenar ejercicios. El Ejercicio 6 actual ("Curvas waterfall: LDPC vs sin codificación") se upgradea para generar FIG-03.
- **D-11:** **Reemplazar el código actual de Ej6 completamente** — eliminar la simulación Monte Carlo del código LDPC (8,4) simple y escribir desde cero la celda con curvas analíticas multi-tasa. Celda más limpia y sin confusión con la simulación completa BP que viene en Fase 3.
- **D-12:** Actualizar `REQUIREMENTS.md` para que LAB-05 diga "Ejercicio 6 (waterfall)" en lugar de "Ejercicio 5 (waterfall)" — corrige la discrepancia entre el spec y la realidad del notebook.

### Claude's Discretion

- Formulación exacta de los valores Eb/N0 para los puntos del conjunto MCS de 5G NR (calcular desde la tasa espectral y capacidad de Shannon).
- Implementación concreta del bound analítico para LDPC (union bound vs. Gallager bound — Claude elige el más pedagógicamente claro).
- Implementación del bound analítico para Polar (Bhattacharyya o capacity-bound — Claude elige).
- Colocación exacta de etiquetas de texto de los threshold markers para evitar solapamiento.
- Colores de las curvas del waterfall (puede reutilizar el mapa de colores de D-02 asignado por tasa, o un colormap lineal por tasa — Claude decide).

</decisions>

<canonical_refs>
## Canonical References

**Downstream agents MUST read these before planning or implementing.**

### Fuente de verdad del material

- `lab.ipynb` — notebook a modificar. Cell 1 = setup/rcParams, Cell 3 = Ej1 Shannon (modificar), Cell 12-13 = Ej6 waterfall (reemplazar)
- `index.md` — verificar que la `<figure>` block de `waterfall-curves.png` (línea ~245) tiene el comment `<!-- será generada por lab.ipynb — Fase 2 -->` que debe convertirse en `<!-- generada por celda X de lab.ipynb -->` al finalizar

### Estándar de calidad

- `../03-ofdm-systems/lab.ipynb` — referencia de estilo de figura: rcParams globales, savefig calls, colormap, anotaciones. Leer cells con `savefig` para ver el patrón exacto.
- `../03-ofdm-systems/index.md` — formato de los `<figure>` blocks ya aprobados con figcaption de 2 líneas

### Planificación del proyecto

- `.planning/ROADMAP.md` — Phase 2 goal y success criteria (FIG-02, FIG-03, LAB-05)
- `.planning/REQUIREMENTS.md` — especificación detallada de FIG-02, FIG-03, LAB-05
- `.planning/phases/01-index-polish/01-CONTEXT.md` — D-04 define el format de `<figure>` blocks; D-03 define los 6 ejercicios del estado target (con Ej6 = waterfall en el notebook actual)

### Contexto de sesiones anteriores

- `../02-modulation-demodulation/` — tabla MCS de 5G NR usada en D-01 para los puntos de operación. Verificar los valores exactos de Eb/N0 por modulación y tasa.

</canonical_refs>

<code_context>
## Existing Code Insights

### Reusable Assets

- `Cell 1 rcParams` — dict de configuración global, sólo añadir `'figure.figsize': (10, 5)` (D-09)
- `Cell 3 Shannon` — estructura existente reutilizable (eje, labels, xlim/ylim); ampliar con D-01/D-02/D-03
- `Q(x)` function (Cell 1) — ya definida como `0.5 * erfc(x / np.sqrt(2))` — usar para la curva BPSK baseline de FIG-03
- `simulate_ldpc_bler()` (Cell 13) — NO reutilizar en Phase 2 (es Monte Carlo; se descarta y reemplaza)

### Established Patterns

- `plt.subplots(figsize=(8, 5))` → cambiar a `(10, 5)` en ambas celdas modificadas
- `plt.savefig(...)` — no existe en ninguna celda actualmente; debe añadirse al final de Cell 3 y al final de la nueva Cell 12/13
- Importaciones ya presentes: `numpy`, `matplotlib.pyplot`, `scipy.special.erfc` — no hay que reimportar

### Integration Points

- `figures/` directory ya existe con `shannon-capacity.png` y `waterfall-curves.png` (serán sobreescritos)
- `index.md` línea ~245: el comentario del `<figure>` block para waterfall debe actualizarse de "será generada" a "generada por celda X" una vez Phase 2 complete

</code_context>

<specifics>
## Specific Ideas

- Los colores del mapa global del curso (D-02): BPSK=azul, QPSK=verde, 16QAM=naranja, 64QAM=rojo. Esto es una decisión de alcance del curso — establecida aquí para que Fases 3, 4 y 5 usen el mismo colormap.
- Las flechas de gap en FIG-02 (D-03) deben ser horizontales — `ax.annotate` con `arrowprops` de A=(Eb/N0_operacion, η) a B=(Eb/N0_Shannon_en_eta, η).
- El threshold marker de waterfall (D-06) es una línea vertical en el Eb/N0 de la capacidad de Shannon para cada tasa r: `Eb/N0_threshold = (2^r - 1)/r` (en lineal) = `10*log10((2^r-1)/r)` dB.

</specifics>

<deferred>
## Deferred Ideas

- Monte Carlo BER para LDPC real (n≈400 bits) con waterfall visible — Phase 3 (LAB-01, FIG-08)
- Curvas BER por modulación (BPSK, QPSK, 16QAM, 64QAM) — Phase 3/5 outputs
- SVG output para figuras vectoriales — posible en Phase 6 (QA), requiere verificar plugin MkDocs
- SCL-L=8 curvas en el waterfall — Phase 4 (LAB-02), cuando el decodificador SCL esté implementado

</deferred>

---

*Phase: 02-figuras-existentes-polished*
*Context gathered: 2026-05-28*
