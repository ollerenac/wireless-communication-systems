# Phase 2: Figuras Existentes Polished — Research

**Researched:** 2026-05-28
**Domain:** Matplotlib figure generation, Shannon capacity, analytical BER bounds
**Confidence:** HIGH

---

<user_constraints>
## User Constraints (from CONTEXT.md)

### Locked Decisions

- **D-01:** Puntos de operación en `shannon-capacity.png`: BPSK r=1/2 (η=0.5, Eb/N0≈3 dB), QPSK r=1/2 (η=1.0, ≈6 dB), QPSK r=3/4 (η=1.5, ≈9 dB), 16QAM r=1/2 (η=2.0, ≈13 dB), 64QAM r=3/4 (η=4.5, ≈22 dB)
- **D-02:** Un color por orden de modulación: BPSK→azul, QPSK→verde, 16QAM→naranja, 64QAM→rojo. Colormap global del curso para Fases 3-5.
- **D-03:** Flechas horizontales de gap al límite de Shannon para cada punto de operación.
- **D-04:** Curvas waterfall analíticas (no Monte Carlo). LDPC: shifted Q-function en dominio dB. Polar: shifted Q-function con alpha menor.
- **D-05:** LDPC r=1/2, r=2/3, r=3/4 + Polar r=1/2, r=3/4 + BPSK sin código = 6 curvas.
- **D-06:** Threshold markers: línea vertical discontinua en Eb/N0 teórico de cada código con etiqueta de gap.
- **D-07:** `figsize=(10, 5)` para ambas figuras.
- **D-08:** `plt.savefig('figures/...', dpi=150, bbox_inches='tight')`. DPI=150 estándar del curso.
- **D-09:** Actualización mínima de Cell 1: añadir `'figure.figsize': (10, 5)` al rcParams existente. No cambiar otros parámetros.
- **D-10:** Actualizar Ejercicio 6 en su lugar, sin renombrar ejercicios.
- **D-11:** Reemplazar código actual de Ej6 completamente (eliminar Monte Carlo del LDPC 8,4 simple).
- **D-12:** Actualizar REQUIREMENTS.md: LAB-05 debe decir "Ejercicio 6 (waterfall)" no "Ejercicio 5".

### Claude's Discretion

- Formulación exacta de los valores Eb/N0 para los puntos MCS de 5G NR.
- Implementación concreta del bound analítico para LDPC y Polar.
- Colocación exacta de etiquetas de threshold markers.
- Colores de las curvas del waterfall.

### Deferred Ideas (OUT OF SCOPE)

- Monte Carlo BER para LDPC real (n≈400 bits) — Phase 3
- Curvas BER por modulación — Phase 3/5
- SVG output — Phase 6
- SCL-L=8 en waterfall — Phase 4
</user_constraints>

<phase_requirements>
## Phase Requirements

| ID | Description | Research Support |
|----|-------------|------------------|
| FIG-02 | `shannon-capacity.png` publicable con puntos de operación, colormap consistente, leyenda detallada | Calculados exactamente: fórmula Shannon, valores Eb/N0, posiciones de flechas |
| FIG-03 | `waterfall-curves.png` BER waterfall LDPC (r=1/2, 2/3, 3/4) y Polar vs BPSK sin código, anotadas | Diseñadas curvas analíticas con cliff_dB y alpha validados; coding gain 4-8 dB verificado |
| LAB-05 | Ej1 (Shannon) y Ej6 (waterfall) actualizados para generar versiones publicables de ambas figuras | Cell 3 actual identificada para modificar; Cell 12-13 actual identificada para reemplazar |
</phase_requirements>

---

## Summary

La fase modifica exclusivamente `lab.ipynb`: Cell 3 (Ej1 Shannon) y Cells 12-13 (Ej6 waterfall) se actualizan para generar figuras de calidad publicable, consistentes con el estándar visual de la sesión 03. La sesión 03 tiene un patrón uniforme: `plt.savefig('figures/nombre.png', dpi=150, bbox_inches='tight')` precedido de `plt.tight_layout()`, con rcParams globales en `(12, 5)` sobreescritos localmente donde hace falta. Esta fase usa `(10, 5)` por decisión D-07.

El punto crítico de diseño para FIG-03 es que los thresholds de Shannon para r=1/2, 2/3, 3/4 (BPSK modulation) se agrupan entre -0.82 y -0.41 dB — prácticamente indistinguibles. La separación visual necesaria proviene de un `practical_cliff_dB = shannon_threshold_dB + finite_length_gap_dB` con gaps crecientes según la tasa, que reflejan el comportamiento real de códigos de bloque finito. Con alpha=4.0 para LDPC y alpha=2.5 para Polar, el coding gain a BER=1e-5 resulta en 7.8 dB (r=1/2) a 5.4 dB (r=3/4), consistente con la figcaption del index.md que afirma "4-8 dB".

**Recomendación primaria:** Usar curva Q desplazada en dominio dB (`Q(alpha*(Eb/N0_dB - cliff_dB))`) para todas las curvas codificadas. Sencillo, limpio, cero tiempo de ejecución, demuestra la diferencia cualitativa entre waterfall y decaimiento sin código.

---

## Architectural Responsibility Map

| Capability | Primary Tier | Secondary Tier | Rationale |
|------------|-------------|----------------|-----------|
| Generación de figuras | Notebook (lab.ipynb) | — | Figuras son output del código Python; el index.md solo las referencia |
| Almacenamiento figuras | `figures/` directory | — | Patrón establecido; ya existen los PNGs que serán sobreescritos |
| Referencia en site | index.md `<figure>` blocks | — | Ya implementado en Phase 1; solo actualizar comentario de celda |
| rcParams globales | Cell 1 (setup) | — | Un solo punto de verdad para estilo; D-09: cambio mínimo |

---

## Standard Stack

### Core (ya instalado en el notebook)

| Librería | Versión verificada | Propósito | Por qué estándar |
|----------|--------------------|-----------|------------------|
| numpy | 2.x (disponible) | Cálculo vectorizado de curvas BER y Shannon | Ya importado como `np` en Cell 1 |
| matplotlib.pyplot | 3.x (disponible) | Generación y guardado de figuras | Ya importado como `plt` en Cell 1 |
| scipy.special.erfc | disponible | Función Q via `0.5*erfc(x/sqrt(2))` | Ya definida como `Q(x)` en Cell 1 |

No hay nuevas dependencias. Todo el código de Phase 2 usa únicamente lo que ya existe en Cell 1.

**Verificación de entorno:** [VERIFIED: codebase grep] — Cell 1 del notebook ya tiene `import numpy as np`, `import matplotlib.pyplot as plt`, `from scipy.special import erfc`, y la función `Q(x)`.

---

## Package Legitimacy Audit

No aplica — esta fase no instala ningún paquete externo. Todas las dependencias ya están presentes en el notebook.

---

## Architecture Patterns

### Patrón de generación de figuras (Sesión 03)

Flujo exacto observado en todas las figuras publicables de session 03:

```
1. [Cell 2, setup global]  plt.rcParams['figure.figsize'] = (12, 5)
                           plt.rcParams['font.size'] = 11
                           plt.rcParams['axes.grid'] = True
                           plt.rcParams['grid.alpha'] = 0.3

2. [en cada celda de figura]
   fig, ax = plt.subplots(figsize=(X, Y))   # override local si necesario
   ...código de plotting...
   plt.tight_layout()
   plt.savefig('figures/nombre.png', dpi=150, bbox_inches='tight')
   plt.show()
```

**Observación clave:** La mayoría de las figuras de session 03 usan `dpi=150`. Algunas figuras más complejas (time-domain, per-subcarrier) usan `dpi=300`. La decisión D-08 establece `dpi=150` para todas las figuras de esta fase — consistente con la mayoría de session 03.

**facecolor='white':** Algunas figuras de session 03 añaden `facecolor='white'` al savefig (ej: `ofdm-time-domain.png`, `ofdm-per-subcarrier-ber.png`). No es universal. Para esta fase no es necesario — el fondo por defecto es blanco con `axes.grid` activado.

### Estructura recomendada de proyecto (sin cambios)

```
04-channel-coding/
├── lab.ipynb          # modificar Cell 1, Cell 3, Cell 12-13
├── index.md           # solo actualizar comentario línea 245
└── figures/
    ├── shannon-capacity.png    # sobreescribir
    └── waterfall-curves.png    # sobreescribir
```

### Patrón de `<figure>` blocks en index.md (Sesión 03)

[VERIFIED: codebase grep] — Formato exacto de todas las figuras de session 03:

```html
<figure markdown="span">
  ![Alt text descriptivo](figures/nombre.png)
  <!-- generada por celda N de lab.ipynb -->   ← comentario a actualizar
  <figcaption markdown="1">**Figura N.** Primera línea descriptiva.
  Segunda línea de contexto pedagógico con ecuaciones LaTeX si aplica.
  </figcaption>
</figure>
```

El bloque existente para `waterfall-curves.png` (index.md línea 243-249) ya tiene este formato correcto. Solo debe actualizarse el comentario en línea 245.

### Anti-Patterns a Evitar

- **No usar `plt.rcParams.update({...})` con todos los parámetros:** D-09 especifica cambio mínimo — solo añadir `'figure.figsize': (10, 5)`. No sobrescribir `font.size`, `axes.grid`, ni `grid.alpha` que ya están bien.
- **No reutilizar `simulate_ldpc_bler()` de Cell 13:** Está diseñado para Monte Carlo del LDPC (8,4) pequeño. Se descarta completamente (D-11).
- **No poner `figsize=(8, 5)`:** El valor actual en Cell 3 y Cell 13 es `(8, 5)`. Cambiar a `(10, 5)` (D-07).

---

## Don't Hand-Roll

| Problema | No construir | Usar en cambio | Por qué |
|----------|-------------|----------------|---------|
| Función Q | Implementación propia de integración numérica | `Q(x) = 0.5*erfc(x/sqrt(2))` ya en Cell 1 | Ya definida, numericamente estable |
| Waterfall con Monte Carlo | Simulación BP en Ej6 (código actual Cell 13) | Curva Q desplazada analítica | MC tarda 10-60s, resultado ruidoso, no aporta sobre Phase 3 |
| Colormap personalizado | Dict de colores ad-hoc por curva | Constantes de color nombradas en el bloque de plotting | Consistencia entre celdas, legibilidad |

---

## Verified Values for FIG-02 (Shannon Capacity)

[VERIFIED: computación Python en esta sesión de investigación]

### Puntos de operación MCS (locked, D-01)

Estos son puntos prácticos de operación del sistema 5G NR — no los mínimos de Shannon. Los mínimos de Shannon se calculan a continuación para las flechas de gap (D-03).

| Modulación | r | η (bit/s/Hz) | Eb/N0_op (dB) | Color (D-02) |
|-----------|---|--------------|---------------|--------------|
| BPSK | 1/2 | 0.5 | 3.0 | `'steelblue'` |
| QPSK | 1/2 | 1.0 | 6.0 | `'mediumseagreen'` |
| QPSK | 3/4 | 1.5 | 9.0 | `'mediumseagreen'` |
| 16QAM | 1/2 | 2.0 | 13.0 | `'darkorange'` |
| 64QAM | 3/4 | 4.5 | 22.0 | `'firebrick'` |

**Nota sobre colores:** D-02 dice BPSK→azul, QPSK→verde, 16QAM→naranja, 64QAM→rojo. Los nombres exactos arriba son la representación matplotlib recomendada — distinguibles visualmente y consistentes con el standard de la sesión.

### Mínimos de Shannon (para flechas de gap D-03)

Fórmula: `Eb/N0_Shannon = (2^η - 1) / η` (lineal), convertido a dB.

[VERIFIED: computación Python con numpy en esta sesión]

| Punto MCS | η | Eb/N0_Shannon (dB) | Gap (dB) |
|-----------|---|---------------------|----------|
| BPSK r=1/2 | 0.5 | **-0.82 dB** | 3.82 dB |
| QPSK r=1/2 | 1.0 | **0.00 dB** | 6.00 dB |
| QPSK r=3/4 | 1.5 | **0.86 dB** | 8.14 dB |
| 16QAM r=1/2 | 2.0 | **1.76 dB** | 11.24 dB |
| 64QAM r=3/4 | 4.5 | **6.82 dB** | 15.18 dB |

**Observación:** El context D-01 menciona "Eb/N0 ≈ 10 dB" para 64QAM 3/4 (el punto único que tenía la Cell 3 original). El valor de 22 dB es el correcto para D-01, que representa el punto de operación del *sistema* (no la capacidad de Shannon del punto). La Cell 3 actual usa 10 dB para el único punto — ese valor era arbitrario en el borrador original.

---

## Verified Values for FIG-03 (Waterfall Curves)

[VERIFIED: computación Python en esta sesión de investigación]

### Thresholds de Shannon por tasa (para D-06 threshold markers)

Fórmula: `Eb/N0_threshold_dB = 10*log10((2^r - 1) / r)`

| Código | r | Threshold Shannon (dB) |
|--------|---|------------------------|
| LDPC r=1/2 | 0.5 | **-0.817 dB** |
| LDPC r=2/3 | 0.667 | **-0.550 dB** |
| LDPC r=3/4 | 0.75 | **-0.414 dB** |
| Polar r=1/2 | 0.5 | **-0.817 dB** |
| Polar r=3/4 | 0.75 | **-0.414 dB** |

**Advertencia crítica de diseño:** Los thresholds de Shannon están todos comprendidos entre -0.82 y -0.41 dB. Si se usa solo el threshold teórico para centrar las curvas analíticas, las 5 curvas codificadas se superpondrán visualmente. La separación visible requiere `practical_cliff_dB` con gaps crecientes según la tasa (ver implementación abajo).

### Parámetros de las curvas analíticas

Fórmula: `BER_code = Q(alpha * (Eb/N0_dB - cliff_dB))`

donde `cliff_dB = shannon_threshold_dB + finite_length_gap_dB`

El `finite_length_gap_dB` refleja que códigos de bloque finito (n~400-1000 bits) operan típicamente 1-4 dB sobre la capacidad de Shannon. LDPC converge más al límite que Polar para bloques medianos. Gap creciente con la tasa porque códigos de alta tasa tienen menos redundancia para corregir errores.

[VERIFIED: computación Python — coding gain a BER=1e-5 es 7.8 dB (r=1/2) a 5.4 dB (r=3/4), consistente con figcaption del index.md que afirma "4-8 dB"]

| Curva | r | Shannon_thr (dB) | FL_gap (dB) | cliff_dB | alpha | Color waterfall |
|-------|---|-------------------|-------------|----------|-------|-----------------|
| LDPC r=1/2 | 0.5 | -0.82 | 1.5 | **0.68** | 4.0 | `'steelblue'` |
| LDPC r=2/3 | 2/3 | -0.55 | 2.5 | **1.95** | 4.0 | `'dodgerblue'` |
| LDPC r=3/4 | 0.75 | -0.41 | 3.5 | **3.09** | 4.0 | `'royalblue'` |
| Polar r=1/2 | 0.5 | -0.82 | 2.5 | **1.68** | 2.5 | `'darkorange'` |
| Polar r=3/4 | 0.75 | -0.41 | 4.0 | **3.59** | 2.5 | `'orange'` |
| BPSK sin código | — | — | — | — | — | `'black'` |

**Separación a BER=1e-3:**
- LDPC r=1/2: 1.46 dB, LDPC r=2/3: 2.72 dB, LDPC r=3/4: 3.86 dB
- Polar r=1/2: 2.92 dB, Polar r=3/4: 4.82 dB
- Curvas perfectamente separadas en el rango de interés pedagógico.

**Rango del eje X:** 0 a 10 dB — todas las curvas codificadas ya están en el piso (<1e-6) antes de 6 dB; BPSK sin código llega a ~2e-4 en 8 dB.

---

## Code Examples

### Patrón rcParams Session 03 (copy/paste ready)

[VERIFIED: codebase read session 03 lab.ipynb Cell 2]

```python
# Session 03 setup cell (Cell 2) — patrón de referencia
plt.rcParams['figure.figsize'] = (12, 5)
plt.rcParams['font.size'] = 11
plt.rcParams['axes.grid'] = True
plt.rcParams['grid.alpha'] = 0.3
```

### Modificación mínima de Cell 1 (D-09)

[VERIFIED: codebase read lab.ipynb Cell 1]

Cell 1 actual del notebook de sesión 04:
```python
plt.rcParams.update({
    'figure.dpi': 120,
    'font.size': 11,
    'axes.grid': True,
    'grid.alpha': 0.3,
})
```

Cambio a aplicar — añadir UNA línea:
```python
plt.rcParams.update({
    'figure.dpi': 120,
    'font.size': 11,
    'axes.grid': True,
    'grid.alpha': 0.3,
    'figure.figsize': (10, 5),   # ← añadir esta línea (D-09)
})
```

### Patrón savefig (copy/paste ready)

[VERIFIED: codebase read session 03 lab.ipynb — patrón uniforme en 11 figuras]

```python
plt.tight_layout()
plt.savefig('figures/shannon-capacity.png', dpi=150, bbox_inches='tight')
plt.show()
```

```python
plt.tight_layout()
plt.savefig('figures/waterfall-curves.png', dpi=150, bbox_inches='tight')
plt.show()
```

### FIG-02: Cell 3 completa (Shannon capacity con MCS points + gap arrows)

```python
# ── Curva de Shannon ──────────────────────────────────────────────────────────
eta = np.linspace(0.05, 6, 500)
EbN0_lin = (2**eta - 1) / eta
EbN0_dB  = 10 * np.log10(EbN0_lin)
shannon_limit_dB = 10 * np.log10(np.log(2))  # -1.59 dB (limite absoluto eta→0)

fig, ax = plt.subplots(figsize=(10, 5))
ax.plot(EbN0_dB, eta, 'b-', lw=2.5, label='Límite de Shannon $C = \\log_2(1+SNR)$')
ax.fill_betweenx(eta, EbN0_dB, 25, alpha=0.06, color='blue', label='Región no alcanzable')
ax.axvline(shannon_limit_dB, color='red', ls='--', lw=1.5,
           label=f'Límite absoluto {shannon_limit_dB:.2f} dB')

# ── MCS operating points ──────────────────────────────────────────────────────
MCS = [
    # (nombre, eta, Eb/N0_op_dB, color)
    ('BPSK $r=1/2$',   0.5, 3.0,  'steelblue'),
    ('QPSK $r=1/2$',   1.0, 6.0,  'mediumseagreen'),
    ('QPSK $r=3/4$',   1.5, 9.0,  'mediumseagreen'),
    ('16-QAM $r=1/2$', 2.0, 13.0, 'darkorange'),
    ('64-QAM $r=3/4$', 4.5, 22.0, 'firebrick'),
]

for label, eta_op, ebno_op, color in MCS:
    # Punto de operación
    ax.scatter([ebno_op], [eta_op], s=70, color=color, zorder=5)
    ax.annotate(label, xy=(ebno_op, eta_op),
                xytext=(ebno_op + 0.5, eta_op + 0.2),
                fontsize=8, color=color,
                arrowprops=dict(arrowstyle='->', color=color, lw=0.8))
    # Mínimo de Shannon al mismo eta
    ebno_shannon = 10 * np.log10((2**eta_op - 1) / eta_op)
    gap = ebno_op - ebno_shannon
    # Flecha horizontal de gap (D-03)
    ax.annotate('', xy=(ebno_shannon, eta_op), xytext=(ebno_op, eta_op),
                arrowprops=dict(arrowstyle='<->', color='gray', lw=1.0))
    ax.text((ebno_op + ebno_shannon) / 2, eta_op + 0.12,
            f'{gap:.1f} dB', ha='center', va='bottom', fontsize=7.5, color='gray')

ax.set_xlabel('$E_b/N_0$ (dB)')
ax.set_ylabel('Eficiencia espectral $\\eta$ (bit/s/Hz)')
ax.set_title('Región de Shannon — Capacidad del canal AWGN y puntos de operación 5G NR')
ax.set_xlim(-3, 25)
ax.set_ylim(0, 6.2)
ax.legend(fontsize=9, loc='upper left')
plt.tight_layout()
plt.savefig('figures/shannon-capacity.png', dpi=150, bbox_inches='tight')
plt.show()
```

### FIG-03: Cell 12-13 completa (Waterfall curves analíticas)

```python
# ── Curvas waterfall analíticas (D-04, D-05) ─────────────────────────────────
EbN0_dB = np.linspace(-2, 12, 500)
EbN0_lin = 10**(EbN0_dB / 10)

# Curva baseline: BPSK sin código
ber_bpsk = Q(np.sqrt(2 * EbN0_lin))

# Función auxiliar: waterfall analítico
def ber_code(EbN0_dB_arr, cliff_dB, alpha):
    """BER analítica con forma waterfall: Q(alpha*(Eb/N0 - cliff_dB))."""
    return Q(alpha * (EbN0_dB_arr - cliff_dB))

# Parámetros de cada curva (shannon_thr + finite_length_gap)
#   cliff_dB = 10*log10((2^r-1)/r) + gap
CODES = [
    # (nombre, cliff_dB, alpha, color, ls)
    ('LDPC $r_c=1/2$',  0.68, 4.0, 'steelblue',   '-'),
    ('LDPC $r_c=2/3$',  1.95, 4.0, 'dodgerblue',  '--'),
    ('LDPC $r_c=3/4$',  3.09, 4.0, 'royalblue',   ':'),
    ('Polar $r_c=1/2$', 1.68, 2.5, 'darkorange',  '-'),
    ('Polar $r_c=3/4$', 3.59, 2.5, 'orange',      '--'),
]

fig, ax = plt.subplots(figsize=(10, 5))
ax.semilogy(EbN0_dB, ber_bpsk, 'k-', lw=2, label='BPSK sin código')

for name, cliff, alpha, color, ls in CODES:
    ber = np.maximum(ber_code(EbN0_dB, cliff, alpha), 1e-7)
    ax.semilogy(EbN0_dB, ber, color=color, lw=1.8, ls=ls, label=name)

# ── Threshold markers (D-06) ─────────────────────────────────────────────────
for r_val, label in [(0.5, '1/2'), (2/3, '2/3'), (0.75, '3/4')]:
    thr_dB = 10 * np.log10((2**r_val - 1) / r_val)
    ax.axvline(thr_dB, color='gray', ls=':', lw=0.8, alpha=0.7)
    ax.text(thr_dB + 0.05, 5e-1, f'$C(r={label})$', fontsize=7,
            color='gray', rotation=90, va='top')

ax.set_xlabel('$E_b/N_0$ (dB)')
ax.set_ylabel('BER')
ax.set_title('Curvas waterfall — LDPC, Polar y BPSK sin código (canal AWGN)')
ax.set_xlim(-2, 10)
ax.set_ylim(1e-6, 1.1)
ax.legend(fontsize=9, loc='lower left')
plt.tight_layout()
plt.savefig('figures/waterfall-curves.png', dpi=150, bbox_inches='tight')
plt.show()
```

### Gap arrow pattern (anotación horizontal matplotlib)

[ASSUMED — patrón matplotlib estándar no verificado en Context7 para esta versión exacta]

```python
# Flecha horizontal de doble punta: FROM operating point TO Shannon limit
ax.annotate('',
    xy=(ebno_shannon_dB, eta_op),    # arrowhead AT Shannon curve
    xytext=(ebno_op_dB, eta_op),     # tail AT operating point
    arrowprops=dict(arrowstyle='<->', color='gray', lw=1.0))

# Etiqueta de gap centrada sobre la flecha
gap_dB = ebno_op_dB - ebno_shannon_dB
ax.text(
    (ebno_op_dB + ebno_shannon_dB) / 2,
    eta_op + 0.12,
    f'{gap_dB:.1f} dB',
    ha='center', va='bottom', fontsize=7.5, color='gray')
```

**Nota de colocación:** `xytext` del `ax.annotate` de etiqueta del punto MCS debe desplazarse hacia la derecha del punto para evitar solapamiento con la flecha de gap. El offset `(ebno_op + 0.5, eta_op + 0.2)` funciona bien para todos los puntos excepto QPSK r=1/2 y QPSK r=3/4 (mismo color, están próximos en η). Para esos dos, considerar offsets alternativos o etiquetar solo uno.

---

## Exact Lines to Update in index.md

### Línea 245 (única modificación a index.md en Phase 2)

**Actual (línea 245):**
```html
  <!-- será generada por lab.ipynb — Fase 2 -->
```

**Target (actualizar al final de Phase 2):**
```html
  <!-- generada por celda 12 de lab.ipynb -->
```

El número de celda exacto depende de si el reemplazo de Ej6 ocurre en la misma posición de Cell 12-13. Si se mantiene la estructura actual (Cell 12 = markdown, Cell 13 = código), la celda de código es la 13. Usar `celda 13` o simplemente `lab.ipynb`.

### Línea 30 de REQUIREMENTS.md (D-12)

**Actual:**
```
- [ ] **LAB-05**: Ejercicio 1 (Shannon) y Ejercicio 5 (waterfall) actualizados...
```

**Target:**
```
- [ ] **LAB-05**: Ejercicio 1 (Shannon) y Ejercicio 6 (waterfall) actualizados...
```

---

## Common Pitfalls

### Pitfall 1: QPSK r=1/2 y QPSK r=3/4 tienen el mismo color (verde)
**Qué pasa:** En D-02, QPSK es un color. Pero en la figura Shannon hay dos puntos QPSK con distinta tasa — quedarían del mismo color y la etiqueta se superpone si ambas tienen offset igual.
**Por qué pasa:** D-02 asigna colores por MODULACIÓN, no por tasa. Dos puntos QPSK con tasas distintas comparten color.
**Cómo evitar:** Usar el mismo color `'mediumseagreen'` para ambos puntos (correcto según D-02), pero dar offsets de anotación distintos:
- QPSK r=1/2: offset `(+0.5, +0.2)` (etiqueta a la derecha-arriba)
- QPSK r=3/4: offset `(+0.5, -0.3)` (etiqueta a la derecha-abajo)
**Señal de alerta:** Si en la preview las dos etiquetas QPSK se solapan.

### Pitfall 2: `figsize=(8,5)` no actualizado
**Qué pasa:** Cell 3 actual usa `fig, ax = plt.subplots(figsize=(8, 5))`. Si no se cambia a `(10, 5)`, la figura guardada no coincide con D-07.
**Por qué pasa:** El rcParams update en Cell 1 afecta `plt.subplots()` sin argumentos, pero NO sobreescribe el `figsize` explícito dentro de `plt.subplots(figsize=...)`.
**Cómo evitar:** Cambiar explícitamente `figsize=(8, 5)` → `figsize=(10, 5)` en ambas celdas modificadas. La clave en rcParams actúa de fallback, pero con `figsize=` explícito en `subplots()` la clave de rcParams no tiene efecto.

### Pitfall 3: Waterfall curves saturan en NaN/0 por debajo del floor
**Qué pasa:** `Q(alpha * (EbN0_dB - cliff))` da valores < 1e-300 para EbN0 alto, que pueden aparecer como 0 en el eje log y generar gaps o warnings.
**Por qué pasa:** La función Q decae gaussianamente — para alpha=4 y 5 dB sobre el cliff, el argumento es ~20 y la función vale ~1e-90.
**Cómo evitar:** Aplicar `np.maximum(ber_curve, 1e-7)` antes de `ax.semilogy(...)`. El floor 1e-7 está por debajo del ylim mínimo de 1e-6, así que no se ve pero evita problemas numéricos.

### Pitfall 4: Los threshold markers se superponen visualmente
**Qué pasa:** Los tres thresholds de Shannon (-0.82, -0.55, -0.41 dB) están a menos de 0.5 dB de diferencia — en el eje x del plot (rango -2 a 10 dB = 12 dB total), eso es <4% del ancho. Las etiquetas de texto de los 5 markers (LDPC r=1/2 y Polar r=1/2 tienen el MISMO threshold: -0.82 dB) se solaparán.
**Por qué pasa:** Shannon threshold `(2^r-1)/r` converge a los mismos valores para r=1/2 (LDPC y Polar) y r=3/4 (LDPC y Polar).
**Cómo evitar:** Dibujar solo 3 líneas de threshold (una por tasa, no por código): r=1/2 (-0.82 dB), r=2/3 (-0.55 dB), r=3/4 (-0.41 dB). Etiqueta genérica `C(r=1/2)` sin distinguir LDPC/Polar.

### Pitfall 5: `os.makedirs('figures', exist_ok=True)` ausente en Cell 1
**Qué pasa:** En el notebook de sesión 04, Cell 1 no tiene la llamada `os.makedirs`. Sin embargo, el directorio `figures/` ya existe, por lo que `plt.savefig('figures/...')` funciona. No es un problema bloqueante, pero si se ejecuta en un entorno limpio (Colab), fallará.
**Cómo evitar:** Añadir `os.makedirs('figures', exist_ok=True)` y el correspondiente `import os` a Cell 1. La sesión 03 ya lo hace (su Cell 2 tiene ambas líneas). Incluirlo en la actualización mínima de D-09.

---

## State of the Art

| Enfoque antiguo | Enfoque actual | Impacto |
|-----------------|----------------|---------|
| Monte Carlo LDPC (8,4) en Ej6 | Curvas analíticas Q-desplazadas | Cero tiempo de ejecución, resultado limpio, correcto para propósito pedagógico |
| Un solo punto 64QAM en Shannon plot | 5 puntos MCS con gap arrows | Conecta con tabla MCS de Sesión 02, muestra diversidad de operaciones 5G NR |
| `plt.show()` sin savefig | `plt.tight_layout(); plt.savefig(...); plt.show()` | Figuras reproducibles almacenadas en `figures/` |
| `figsize=(8,5)` | `figsize=(10,5)` | Más espacio para etiquetas y anotaciones sin saturar |

---

## Assumptions Log

| # | Claim | Section | Risk si es incorrecto |
|---|-------|---------|----------------------|
| A1 | Los valores Eb/N0 de D-01 (3/6/9/13/22 dB) son puntos prácticos del sistema 5G NR, no mínimos de Shannon | Verified Values FIG-02 | Bajo — son locked decisions del usuario, y son plausibles para sistemas prácticos |
| A2 | El patrón `arrowstyle='<->'` para flechas de doble punta en matplotlib.annotate funciona como se describe | Code Examples (gap arrow) | Bajo — patrón estándar matplotlib documentado, muy raramente cambia entre versiones |
| A3 | Los `finite_length_gap_dB` (1.5/2.5/3.5 para LDPC, 2.5/4.0 para Polar) producen la separación visual deseada | Verified Values FIG-03 | Medio — calculados analíticamente pero no visualizados interactivamente; la separación matemática está verificada |
| A4 | `import os` no está en Cell 1 actual | Pitfall 5 / Standard Stack | Bajo — si ya está, añadirlo no causa error; si no está, la falta causaría NameError |

**Si esta tabla está casi vacía:** La mayoría de los valores críticos (thresholds, gaps, separación de curvas, patrón savefig) están verificados por computación Python en esta sesión de investigación.

---

## Open Questions

1. **QPSK r=1/2 vs QPSK r=3/4 — misma eta, mismo color**
   - Lo que sabemos: D-02 asigna verde a QPSK. Las dos tasas (η=1.0 y η=1.5) son puntos distintos en la figura.
   - Lo que no está claro: Si el planner quiere distinguirlos visualmente dentro del mismo color o acepta mismo color con offset de etiqueta.
   - Recomendación: Usar mismo color (correcto según D-02) con offsets distintos de etiqueta. Si el usuario lo nota en revisión, ajustar shading (verde oscuro / verde claro).

2. **Número de celda exacto para el comentario en index.md línea 245**
   - Lo que sabemos: El plan reemplazará Cells 12-13 (markdown Ej6 + código Ej6). La celda de código será la 13 si no se reordena.
   - Lo que no está claro: Si el planner decide dividir en más de una celda o consolida.
   - Recomendación: El planner especifica el número exacto al final del task; el research apunta a "celda 13" como valor probable.

---

## Environment Availability

| Dependencia | Requerida por | Disponible | Versión | Fallback |
|-------------|--------------|-----------|---------|----------|
| numpy | Cálculo BER/Shannon | ✓ | Cell 1 | — |
| matplotlib | Figuras | ✓ | Cell 1 | — |
| scipy.special.erfc | Función Q | ✓ | Cell 1 | — |
| directorio `figures/` | `plt.savefig(...)` | ✓ | Existe con 2 PNGs | — |

Ninguna dependencia faltante. Esta fase puede ejecutarse en el entorno actual sin ninguna instalación adicional.

---

## Validation Architecture

### Test Framework

| Propiedad | Valor |
|-----------|-------|
| Framework | Ejecución manual del notebook (nbconvert para CI) |
| Config | Sin pytest — outputs visuales |
| Quick run | `jupyter nbconvert --to notebook --execute lab.ipynb --output /tmp/test.ipynb` |
| Full suite | Mismo comando + verificar que `figures/` contiene los PNGs actualizados |

### Phase Requirements → Test Map

| Req ID | Comportamiento | Tipo de test | Comando | ¿Archivo existe? |
|--------|----------------|-------------|---------|-----------------|
| FIG-02 | `figures/shannon-capacity.png` existe y tiene >5 KB | Smoke | `test -f figures/shannon-capacity.png && python3 -c "import os; assert os.path.getsize('figures/shannon-capacity.png') > 5000"` | ✓ (sobreescribir) |
| FIG-03 | `figures/waterfall-curves.png` existe y tiene >5 KB | Smoke | `test -f figures/waterfall-curves.png && python3 -c "import os; assert os.path.getsize('figures/waterfall-curves.png') > 5000"` | ✓ (sobreescribir) |
| LAB-05 | Notebook ejecuta Cell 1-13 sin errores | Integration | `jupyter nbconvert --to notebook --execute lab.ipynb --ExecutePreprocessor.timeout=120` | ✓ |

### Sampling Rate

- **Per task commit:** Inspección visual de las figuras generadas + verificar que existen en `figures/`
- **Per wave merge:** Ejecución completa del notebook desde Cell 1 hasta Cell 13
- **Phase gate:** Notebook ejecuta limpio + ambas figuras presentes + inspección visual confirma calidad

### Wave 0 Gaps

Ninguno — infraestructura de test suficiente con inspección visual + ejecución del notebook. No se requieren archivos de test adicionales para esta fase.

---

## Security Domain

No aplica — fase de generación de figuras para material educativo. Sin autenticación, inputs de usuario, datos externos, ni secretos. `security_enforcement: true` en config pero ninguna categoría ASVS es relevante para notebooks de visualización offline.

---

## Sources

### Primary (HIGH confidence)

- Codebase read: `lab.ipynb` (sesión 04) — Cell 1, Cell 3, Cell 12-13 leídas en su totalidad
- Codebase read: `../03-ofdm-systems/lab.ipynb` — Cells 2 (setup), 16, 18, 22, 24, 27, 30, 35, 38, 41 con todos los patrones savefig/rcParams
- Codebase read: `../03-ofdm-systems/index.md` — líneas 59-62 para formato `<figure>` blocks
- Codebase read: `index.md` sesión 04 — líneas 240-250 para el bloque `<figure>` de waterfall-curves.png
- Computación Python verificada: valores exactos de Eb/N0 Shannon para todos los puntos MCS, thresholds de waterfall, separación de curvas analíticas, coding gain a BER=1e-5

### Secondary (MEDIUM confidence)

- `.planning/phases/02-figuras-existentes-polished/02-CONTEXT.md` — decisiones bloqueadas D-01 a D-12, valores Eb/N0 de D-01 aceptados como locked

### Tertiary (LOW confidence)

Ninguna — no se usaron WebSearch ni fuentes no verificadas.

---

## Metadata

**Confidence breakdown:**

- Standard Stack: HIGH — todo verificado en codebase del proyecto
- Architecture Patterns: HIGH — extraídos directamente del notebook de referencia (sesión 03)
- Verified Values (FIG-02): HIGH — calculados con numpy en esta sesión, fórmulas Shannon estándar
- Verified Values (FIG-03): HIGH (parámetros) / MEDIUM (separación visual) — valores calculados analíticamente pero no renderizados
- Pitfalls: HIGH — observados directamente en el código actual del notebook

**Research date:** 2026-05-28
**Valid until:** 2026-06-28 (stable domain — matplotlib patterns y fórmulas Shannon no cambian)
