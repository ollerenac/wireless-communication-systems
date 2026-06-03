# Phase 4: Polar Lab + Figuras — Research

**Researched:** 2026-05-29
**Domain:** Polar codes, SC/SCL decoding, Monte Carlo BER, matplotlib figure design
**Confidence:** HIGH

---

## Summary

Phase 4 añade tres deliverables concretos al notebook: (1) un encoder Polar N=64 con selección de bits congelados por parámetro de Bhattacharyya (AWGN), (2) un decodificador SC recursivo y un decodificador SCL con lista L=8, con comparación BER Monte Carlo, y (3) dos figuras: `polar-butterfly.png` (FIG-06, diagrama de la transformación butterfly G_2→G_8) y `polar-polarization.png` (FIG-07, histograma de Z(W_N^{(i)}) para N=64 mostrando la polarización bimodal).

El código base ya contiene (Celdas 12 y 14): `bhattacharyya_tree(Z0, N)` para BEC, `f_func(a, b)` y `g_func(a, b, u_hat)` para LLR recursivo, y `sc_decode_n4` para N=4. Phase 4 REUTILIZA estas funciones — no las redefine. El encoder usa G_N = F^{⊗n} (sin bit-reversal) por coherencia con el árbol de Bhattacharyya del notebook.

La decisión clave es usar Z_0 = exp(−Rc·EbN0_lin) como parámetro de Bhattacharyya inicial para AWGN, lo que es exacto (Arıkan 2009, eq. posterior a (60)) y permite reutilizar `bhattacharyya_tree` del notebook sin modificaciones. El set de bits congelados se selecciona a Eb/N0 = 3 dB (punto de diseño conservador), que produce un ranking estable para el rango de simulación 1–5 dB.

**Primary recommendation:** Polar N=64 con k=32 (tasa 1/2), encoder Kronecker G_64, SC recursivo O(N²) y SCL-8 con path metric log-likelihood, n_blocks=300, 9 puntos SNR en [1.0, 5.0] dB. Timing estimado: SC ~3s, SCL ~25s total.

---

## Architectural Responsibility Map

| Capability | Primary Tier | Secondary Tier | Rationale |
|------------|-------------|----------------|-----------|
| Polar encoder N=64 | Notebook (Python) | — | G_64 = F^{⊗6}, numpy kron |
| AWGN Bhattacharyya Z_0 | Notebook (Python) | — | Z_0 = exp(−Rc·γ), reutiliza bhattacharyya_tree existente |
| SC decoder recursivo | Notebook (Python) | — | Reutiliza f_func/g_func de Cell 14 |
| SCL-L=8 decoder | Notebook (Python) | — | Path metric log-likelihood, poda top-L |
| polar-butterfly.png | Notebook (Python) | — | Diagrama matplotlib de red butterfly N=8 |
| polar-polarization.png | Notebook (Python) | — | Histograma Z(W_N^{(i)}) N=64 |
| Figure display in site | index.md (MkDocs) | — | `<figure markdown="span">` blocks en §4.1 |

---

## Polar Encoder — G_N = F^{⊗n}

### Construcción y uso

```python
def build_polar_G(N):
    """G_N = F^{⊗n}, F = [[1,0],[1,1]], sin bit-reversal."""
    F = np.array([[1, 0], [1, 1]], dtype=int)
    n = int(np.log2(N))
    G = F.copy()
    for _ in range(n - 1):
        G = np.kron(G, F)   # crece: 2→4→8→16→32→64
    return G

G64 = build_polar_G(64)   # 64×64 int matrix, cómputo único

def polar_encode(u, G):
    """Codifica u (vector N bits) → codeword x."""
    return G @ u % 2
```

**Verificación:** G_4 = F⊗F = [[1,0,0,0],[1,1,0,0],[1,0,1,0],[1,1,1,1]]. Para u=[0,0,1,0]: x = [0,0,1,1]. ✓

**Consistencia encoder/decoder (CRÍTICO):** Con G_N = F^{⊗n} (sin B_N), el canal sintético de índice i en `bhattacharyya_tree` corresponde al bit u[i] en natural order. El decoder recursivo en este research es consistente con esta convención. No usar bit-reversal en ninguno de los dos. [VERIFIED: consistencia algebraica verificada por inducción para N=4]

---

## AWGN Bhattacharyya Z_0 y Selección de Bits Congelados

### Fórmula exacta de Z_0 para BPSK AWGN

Para BPSK sobre AWGN con potencia de señal unitaria (E_s = 1) y varianza de ruido σ²:

```
Z_0(BPSK AWGN) = exp(−1/(2σ²)) = exp(−E_s/N_0)
```

Para sistema codificado con tasa Rc = k/N, a Eb/N0 = γ (lineal):
- σ² = 1/(2·Rc·γ)  →  1/(2σ²) = Rc·γ

**Fórmula de uso:**
```python
Z0_awgn = np.exp(-Rc * EbN0_lin)   # EbN0_lin = 10**(EbN0_dB/10)
```

Para Rc=0.5, Eb/N0=3 dB (γ=2.0): Z_0 = exp(−0.5×2.0) = exp(−1.0) ≈ 0.368
Para Rc=0.5, Eb/N0=0 dB (γ=1.0): Z_0 = exp(−0.5) ≈ 0.607

### Selección de bits congelados

```python
N_polar = 64
k_polar = 32    # tasa 1/2

# Punto de diseño: Eb/N0 = 3 dB
EbN0_design_lin = 10**(3.0/10)
Rc_polar = k_polar / N_polar
Z0_design = np.exp(-Rc_polar * EbN0_design_lin)

# Reutilizar bhattacharyya_tree de Cell 12
Z_channels = bhattacharyya_tree(Z0_design, N_polar)

# Bits congelados: los k_polar canales con mayor Z (peores)
frozen_set = set(np.argsort(Z_channels)[k_polar:])
info_set   = set(np.argsort(Z_channels)[:k_polar])

print(f"Z_0 = {Z0_design:.4f}, frozen={len(frozen_set)}, info={len(info_set)}")
```

**Estabilidad del ranking:** El ranking de canales (no los valores de Z) es estable para Z_0 ∈ [0.2, 0.8], es decir, para Eb/N0 ≈ 1–5 dB a tasa 1/2. El punto de diseño a 3 dB es adecuado para simulaciones en [1, 5] dB. [ASSUMED — estabilidad de orden verificada empíricamente en literatura; no simulado en esta sesión]

---

## SC Decoder Recursivo — N=64

### Función auxiliar: LLR para bit i dado árbol parcial

La implementación usa f_func y g_func YA DEFINIDAS en Cell 14. No redefinir.

```python
def compute_llr_for_bit(llr_ch, u_hat, target_bit, N):
    """
    Calcula el LLR para el bit target_bit dado:
    - llr_ch: LLRs del canal (shape N)
    - u_hat: decisiones parciales (shape N); solo [0..target_bit-1] son válidas
    Complejidad: O(N) por llamada.
    """
    def recurse(llr_in, lo, hi):
        n_sub = hi - lo
        if n_sub == 1:
            return llr_in[0]
        half = n_sub // 2
        mid  = lo + half
        if target_bit < mid:
            # target en sub-bloque izquierdo: combinar con f_func (rama XOR)
            llr_left = np.array([f_func(llr_in[j], llr_in[j + half])
                                  for j in range(half)])
            return recurse(llr_left, lo, mid)
        else:
            # target en sub-bloque derecho: combinar con g_func usando u_hat[lo:mid]
            u_left = u_hat[lo:mid]
            llr_right = np.array([g_func(llr_in[j], llr_in[j + half], u_left[j])
                                   for j in range(half)])
            return recurse(llr_right, mid, hi)
    return recurse(llr_ch, 0, N)
```

### Decodificador SC general

```python
def sc_decode_polar(llr_ch, frozen_set, N):
    """
    Decodificador SC para código Polar de longitud N.
    llr_ch:     LLRs del canal (shape N)
    frozen_set: set de índices de bits congelados
    Devuelve:   u_hat (N bits estimados)
    """
    u_hat = np.zeros(N, dtype=int)
    for i in range(N):
        llr_i = compute_llr_for_bit(llr_ch, u_hat, i, N)
        u_hat[i] = 0 if i in frozen_set else (1 if llr_i < 0 else 0)
    return u_hat
```

**Complejidad:** O(N²) total (O(N) por bit × N bits). Para N=64: 64×63 ≈ 4000 llamadas f_func/g_func por decode. [ASSUMED — la implementación eficiente O(N log N) usa caché de árbol; para N=64 la versión naive es suficientemente rápida]

---

## SCL-L=8 Decoder

### Path metric

El path metric es la suma de penalizaciones log-likelihood para cada decisión:

```
pm += log(1 + exp(−LLR_i · (1 − 2·u_i)))
```

Forma numéricamente estable:
```python
x = -llr_i * (1 - 2 * bit_val)  # > 0 si decisión es incorrecta
delta = max(0.0, x) + np.log1p(np.exp(-abs(x)))   # softplus estable
```

Paths con menor `pm` son más probables. Se mantienen los L mejores.

### Implementación

```python
def scl_decode_polar(llr_ch, frozen_set, N, L=8):
    """
    Decodificador SCL para código Polar de longitud N, lista L.
    Devuelve u_hat del path con menor path metric.
    """
    # paths: lista de (path_metric, u_hat_array)
    paths = [(0.0, np.zeros(N, dtype=int))]

    for i in range(N):
        new_paths = []
        for pm, u in paths:
            llr_i = compute_llr_for_bit(llr_ch, u, i, N)
            if i in frozen_set:
                new_paths.append((pm, u.copy()))   # u_i=0 forzado, sin penalización
            else:
                for bit_val in [0, 1]:
                    u_new = u.copy()
                    u_new[i] = bit_val
                    x = -llr_i * (1 - 2 * bit_val)
                    delta = max(0.0, x) + np.log1p(np.exp(-abs(x)))
                    new_paths.append((pm + delta, u_new))
        # Poda: mantener los L paths con menor metric
        new_paths.sort(key=lambda p: p[0])
        paths = new_paths[:L]

    return paths[0][1]   # u_hat del mejor path
```

**Complejidad:** O(N² · L) por decode = 64²·8 ≈ 32,768 f_func/g_func calls. Para n_blocks=300, 9 SNR points: ~88M calls, estimado ~25 segundos en Python. [ASSUMED — basado en timing de bp_awgn de fase anterior; SCL es ~6× más lento que SC puro]

**Mejora esperada sobre SC:** SCL-8 debe mejorar ~1–2 dB a BER=10⁻³ respecto a SC básico para N=64, tasa 1/2. El criterio de éxito requiere ≥1 dB a BER=10⁻³. [ASSUMED — literatura de Tal & Vardy (2015); no simulado numéricamente en esta sesión]

---

## Monte Carlo Parameters

### Código, tasa y frozen set

| Parámetro | Valor |
|-----------|-------|
| N | 64 |
| k | 32 (tasa 1/2) |
| Rc | 32/64 = 0.5 |
| Frozen set | 32 canales de mayor Z (diseño a 3 dB) |
| LLR canal | `2 * y / sigma2`, sigma2 = `1/(2*Rc*EbN0_lin)` |

### Rango SNR y bloques

```python
EbN0_dB_arr = np.arange(1.0, 5.5, 0.5)   # 9 puntos: 1.0, 1.5, ..., 5.0 dB
n_blocks = 300
```

La región de waterfall para SC (N=64, tasa 1/2) está en ~3–4 dB; para SCL-8 en ~2–3 dB.

### Loop Monte Carlo

```python
rng_polar = np.random.default_rng(99)

def run_polar_mc(frozen_set, info_idx, N, k, decoder_fn, EbN0_dB_arr,
                 n_blocks=300):
    """
    decoder_fn: sc_decode_polar o scl_decode_polar (parcialmente aplicado)
    info_idx:   sorted list of information bit indices
    """
    Rc = k / N
    floor = 1.0 / (n_blocks * k)
    BER = []
    for EbN0_dB in EbN0_dB_arr:
        EbN0_lin = 10**(EbN0_dB / 10)
        sigma2 = 1.0 / (2 * Rc * EbN0_lin)
        sigma  = np.sqrt(sigma2)
        bit_errors = 0
        for _ in range(n_blocks):
            # bits de información aleatorios
            msg = rng_polar.integers(0, 2, size=k)
            u = np.zeros(N, dtype=int)
            u[list(info_idx)] = msg
            # Encode
            x = polar_encode(u, G64)
            # BPSK: 0→+1, 1→-1
            bpsk = 1 - 2*x
            y = bpsk + sigma * rng_polar.standard_normal(N)
            llr_ch = 2 * y / sigma2
            # Decode
            u_hat = decoder_fn(llr_ch, frozen_set, N)
            # Contar errores solo en bits de información
            bit_errors += np.sum(u_hat[list(info_idx)] != msg)
        BER.append(max(bit_errors / (n_blocks * k), floor))
    return np.array(BER)
```

**Diferencia respecto a LDPC MC:** Para Polar se cuentan errores solo en bits de información (k=32), no en toda la codeword (N=64). El floor es 1/(n_blocks·k) = 1/(300·32) ≈ 1e-4.

**Nota sigma:** La fórmula `sigma2 = 1/(2*Rc*EbN0_lin)` es idéntica a la de Phase 3. No usar la fórmula invertida. [VERIFIED en Phase 3 por simulación numérica]

---

## FIG-06 (polar-butterfly.png) — Diseño

### Layout

- **Objetivo:** Diagrama de red butterfly para N=8 (3 etapas), mostrando la composición recursiva G_2→G_4→G_8
- **Figure size:** `figsize=(10, 5)`, `dpi=150`
- **No es figura de datos** — diagrama matplotlib puro con patches y lines
- **Color coding:** inputs frozen (salmon), inputs info (steelblue), output nodes (lightgray)
- **XOR gates:** círculos pequeños con "⊕" en texto

### Estructura del diagrama

```
Inputs (izquierda)    Etapa 1    Etapa 2    Etapa 3    Outputs (derecha)
u_0 (frozen) ────────────⊕────────⊕────────⊕──────── x_0
                          │        │        │
u_1 (frozen) ────────────┘────────⊕────────⊕──────── x_1
                                   │        │
u_2 (frozen) ────────────⊕────────┘────────⊕──────── x_2
                          │                 │
u_3 (frozen) ────────────┘─────────────────⊕──────── x_3
                                             │
u_4 (info)   ────────────⊕────────⊕────────┘──────── x_4
                          │        │
u_5 (info)   ────────────┘────────⊕────────────────── x_5
                                   │
u_6 (info)   ────────────⊕────────┘────────────────── x_6
                          │
u_7 (info)   ────────────┘──────────────────────────── x_7
```

Para N=8 con k=4 (tasa 1/2): frozen={0,1,2,4} (canales de mayor Z), info={3,5,6,7}.

### Código de generación (esqueleto)

```python
def draw_butterfly(N, frozen_set, ax):
    """Dibuja la red butterfly Arıkan para código Polar de longitud N."""
    n = int(np.log2(N))
    node_x = np.linspace(0.1, 0.9, n + 2)   # columnas: inputs + n etapas + outputs
    node_y = np.linspace(0.05, 0.95, N)[::-1]  # filas: bits 0..N-1 de arriba a abajo

    # Dibujar conexiones por etapa
    # En etapa s (0-indexed), stride = 2^(s+1), half = stride//2
    # Conexión XOR: fila i se conecta con fila i+half
    for s in range(n):
        stride = 2 ** (s + 1)
        half   = stride // 2
        x_in   = node_x[s + 1]   # columna de entrada a esta etapa
        x_out  = node_x[s + 2]   # columna de salida de esta etapa
        for base in range(0, N, stride):
            for offset in range(half):
                i_top = base + offset
                i_bot = base + offset + half
                # Línea directa (bit que NO se mezcla en esta etapa desde i_top)
                ax.plot([x_in, x_out], [node_y[i_top], node_y[i_top]],
                        'k-', lw=1.0, alpha=0.6, zorder=1)
                # Línea cruzada: i_bot → i_top (rama XOR)
                ax.plot([x_in, (x_in+x_out)/2], [node_y[i_bot], node_y[i_top]],
                        'k-', lw=1.0, alpha=0.6, zorder=1)
                ax.plot([(x_in+x_out)/2, x_out], [node_y[i_top], node_y[i_top]],
                        'k-', lw=1.0, alpha=0.6, zorder=1)
                # Línea directa para i_bot después del XOR
                ax.plot([(x_in+x_out)/2, x_out], [node_y[i_bot], node_y[i_bot]],
                        'k-', lw=1.0, alpha=0.6, zorder=1)
                # XOR gate (círculo pequeño)
                ax.plot((x_in+x_out)/2, node_y[i_top], 'o',
                        color='white', ms=8, markeredgecolor='k', markeredgewidth=0.8, zorder=3)
                ax.text((x_in+x_out)/2, node_y[i_top], '⊕',
                        ha='center', va='center', fontsize=6, zorder=4)

    # Nodos de input
    for i in range(N):
        color = 'salmon' if i in frozen_set else 'steelblue'
        ax.plot(node_x[0], node_y[i], 'o', color=color, ms=14, zorder=5,
                markeredgecolor='k', markeredgewidth=0.5)
        label = f'$u_{i}$' + (' (f)' if i in frozen_set else '')
        ax.text(node_x[0] - 0.04, node_y[i], label,
                ha='right', va='center', fontsize=7.5)

    # Nodos de output
    for i in range(N):
        ax.plot(node_x[-1], node_y[i], 's', color='lightgray', ms=10, zorder=5,
                markeredgecolor='k', markeredgewidth=0.5)
        ax.text(node_x[-1] + 0.03, node_y[i], f'$x_{i}$',
                ha='left', va='center', fontsize=7.5)

    ax.axis('off')

# Figura: N=8 con k=4
N_fig = 8
Z_fig = bhattacharyya_tree(np.exp(-0.5 * 2.0), N_fig)
frozen_fig = set(np.argsort(Z_fig)[N_fig//2:])

fig, ax = plt.subplots(figsize=(10, 5))
draw_butterfly(N_fig, frozen_fig, ax)
ax.set_title('Red butterfly Arıkan — código Polar (N=8, k=4, tasa 1/2)\n'
             'Azul = bits de información, salmón = bits congelados (≡0)', fontsize=10)
plt.tight_layout()
plt.savefig('figures/polar-butterfly.png', dpi=150, bbox_inches='tight')
plt.show()
```

**Criterio de calidad FIG-06 (REQUIREMENTS.md):** "transformación G_2 y composición recursiva hasta G_4 o G_8, con los canales sintéticos etiquetados". El diseño cumple para N=8 (G_8 = F^{⊗3}).

---

## FIG-07 (polar-polarization.png) — Diseño

### Layout

- **Objetivo:** Histograma de Z(W_N^{(i)}) para N=64 mostrando distribución bimodal
- **Figure size:** `figsize=(10, 5)`, `dpi=150`
- **Bins:** 30 bins uniformes en [0, 1]
- **Color:** `steelblue` para canales info (Z < 0.5), `salmon` para canales frozen (Z ≥ 0.5)

### Código de generación

```python
# FIG-07: polar-polarization.png
N_vis = 64
Z0_vis = np.exp(-Rc_polar * EbN0_design_lin)   # usa Z0 del frozen set (3 dB)
Z_vis = bhattacharyya_tree(Z0_vis, N_vis)

# Separar por rol
Z_frozen = Z_vis[list(frozen_set)]
Z_info   = Z_vis[list(info_set)]

bins = np.linspace(0, 1, 31)
fig, ax = plt.subplots(figsize=(10, 5))
ax.hist(Z_frozen, bins=bins, color='salmon',    alpha=0.7, label='Bits congelados (32)',
        edgecolor='white', lw=0.3)
ax.hist(Z_info,   bins=bins, color='steelblue', alpha=0.7, label='Bits de información (32)',
        edgecolor='white', lw=0.3)
ax.axvline(0.5, color='gray', ls='--', lw=1.2, label='Umbral de selección')
ax.set_xlabel('Parámetro de Bhattacharyya $Z(W_{64}^{(i)})$')
ax.set_ylabel('Número de canales sintéticos')
ax.set_title(f'Polarización del canal — $N=64$, diseño $E_b/N_0=3\\ \\mathrm{{dB}}$, $r_c=1/2$\n'
             f'Canales sintéticos polarizados hacia $Z\\approx0$ (buenos) y $Z\\approx1$ (malos)')
ax.legend(fontsize=9)
plt.tight_layout()
plt.savefig('figures/polar-polarization.png', dpi=150, bbox_inches='tight')
plt.show()
print(f"Canales con Z < 0.05: {np.sum(Z_vis < 0.05)}")
print(f"Canales con Z > 0.95: {np.sum(Z_vis > 0.95)}")
```

**Distribución esperada para N=64, Z_0=0.368:** La polarización a N=64 ya es fuerte. Se espera que ~25–30 canales tengan Z < 0.05 y ~25–30 tengan Z > 0.95, con pocos canales intermedios. La distribución bimodal debe ser claramente visible. [ASSUMED — estimado basado en la convergencia geométrica de la recursión Z^- = 2Z-Z², Z^+ = Z² para Z_0 ≈ 0.37]

---

## Notebook Cell Layout

### Estado actual (18 celdas, 0-17)

| Celda | Tipo | Contenido |
|-------|------|-----------|
| 0 | md | Header lab |
| 1 | code | Setup (imports, rcParams) |
| 2 | md | Ex1 descripción |
| 3 | code | shannon-capacity.png |
| 4 | md | Ex2 descripción |
| 5 | code | Hamming síndrome |
| 6 | md | Ex3 descripción LDPC BP |
| 7 | code | H_ldpc (8,4) + bp_bsc + tanner-graph.png |
| 8 | code | Gallager LDPC + bp_awgn + bp_awgn_track |
| 9 | code | bp-messages.png (FIG-05) |
| 10 | code | Monte Carlo LDPC + ldpc-ber-waterfall.png (FIG-08) |
| 11 | md | **Ex4 Polar Bhattacharyya** ← punto de referencia |
| 12 | code | `bhattacharyya_tree` N=8 BEC |
| 13 | md | **Ex5 SC decoder N=4** |
| 14 | code | `f_func`, `g_func`, `sc_decode_n4` + demo ← INSERTAR DESPUÉS DE AQUÍ |
| 15 | md | Ex6 waterfall descripción ← empujar a celda 18 |
| 16 | code | waterfall-curves.png analítico ← empujar a celda 19 |
| 17 | md | Resumen ← empujar a celda 20 |

### Celdas nuevas a insertar (DESPUÉS de celda 14, ANTES de celda 15)

**Nueva celda 15 (Cell A):** Polar N=64 encoder + Z_0 AWGN + frozen set + polar-butterfly.png (FIG-06)

Contenido:
```python
# ── Ejercicio 4 (continuación) — Polar N=64: encoder y bits congelados ─────
# Encoder: G_64 = F^{⊗6}, sin bit-reversal (coherente con bhattacharyya_tree)

def build_polar_G(N):
    """..."""
    # [código completo de la sección Polar Encoder arriba]

G64 = build_polar_G(64)
N_polar, k_polar = 64, 32
Rc_polar = k_polar / N_polar

# Bits congelados: Bhattacharyya AWGN, punto de diseño 3 dB
EbN0_design_lin = 10**(3.0/10)
Z0_design = np.exp(-Rc_polar * EbN0_design_lin)   # = exp(-Rc*gamma)
Z_polar   = bhattacharyya_tree(Z0_design, N_polar)
info_idx   = list(np.argsort(Z_polar)[:k_polar])
frozen_set = set(np.argsort(Z_polar)[k_polar:])
print(f"Z_0 = {Z0_design:.4f}, frozen={len(frozen_set)}, info={len(info_idx)}")
print(f"Canales Z<0.05: {np.sum(Z_polar<0.05)}, Z>0.95: {np.sum(Z_polar>0.95)}")

# [código draw_butterfly y generación polar-butterfly.png]
```

**Nueva celda 16 (Cell B):** SC recursivo + SCL-L=8 (definiciones de funciones solamente)

Contenido:
```python
# ── SC recursivo general y SCL-L=8 ──────────────────────────────────────────
# Usa f_func y g_func ya definidas en la celda anterior (Ex5)

def compute_llr_for_bit(llr_ch, u_hat, target_bit, N):
    """..."""
    # [código completo de la sección SC Decoder]

def sc_decode_polar(llr_ch, frozen_set, N):
    """..."""
    # [código completo]

def scl_decode_polar(llr_ch, frozen_set, N, L=8):
    """..."""
    # [código completo]

# Demo rápida a SNR=4 dB
# [demo con 1 bloque para verificar funcionamiento]
```

**Nueva celda 17 (Cell C):** Monte Carlo BER SC vs SCL + polar-polarization.png (FIG-07)

Contenido:
```python
# ── Monte Carlo BER: SC vs SCL-8 + polar-polarization.png (FIG-07) ──────────
# NOTA: esta celda tarda ~30 s (SC ~3s, SCL ~25s)

# [run_polar_mc function]
# [BER SC]
# [BER SCL]
# [figura BER comparativa]
# [polar-polarization.png]
```

### Estado después de inserción (21 celdas, 0-20)

| Celda | Contenido |
|-------|-----------|
| 14 | `f_func`, `g_func`, `sc_decode_n4` (inalterada) |
| **15 (nueva)** | Polar N=64 encoder + G64 + frozen set + **polar-butterfly.png** |
| **16 (nueva)** | SC recursivo + SCL-L=8 (definiciones) + demo |
| **17 (nueva)** | Monte Carlo SC vs SCL + **polar-polarization.png** |
| 18 (era 15) | Ex6 waterfall descripción (desplazada) |
| 19 (era 16) | waterfall-curves.png analítico (desplazada) |
| 20 (era 17) | Resumen (desplazado) |

---

## index.md Changes

### Puntos de inserción en §4.1

El §4.1 "Polarización del Canal" está en líneas 210–231:
- Línea 229: fin del párrafo de límite de polarización ("...en los canales malos.")
- Línea 231: gancho narrativo "La pregunta natural es:..."

**FIG-06 y FIG-07 se insertan ENTRE las líneas 229 y 231**, siguiendo el patrón de Phase 3 (figuras antes del gancho narrativo).

### Change 1 — Insertar FIG-06 (polar-butterfly.png) después de línea 229

Insertar entre "...en los canales malos." (línea 229) y "La pregunta natural es..." (línea 231):

```markdown

<figure markdown="span">
  ![Red butterfly Arıkan — composición recursiva de G_2 hasta G_8](figures/polar-butterfly.png)
  <!-- generada por celda 15 de lab.ipynb -->
  <figcaption markdown="1">**Figura 6.** Red butterfly de Arıkan para el código Polar $(N=8,\ k=4)$. Cada etapa aplica la transformación $G_2$ a pares de bits: el bit superior se mezcla con el inferior mediante XOR (nodos $\oplus$), creando el canal sintético peor ($W^{(-)}$); el bit inferior se lleva directamente, creando el canal mejor ($W^{(+)}$). Componer $n = \log_2 N$ etapas de este proceso produce $N$ canales sintéticos. Los nodos azules son bits de información (canales buenos, $Z$ pequeño); los salmón son bits congelados a cero (canales malos, $Z$ grande).
  </figcaption>
</figure>
```

### Change 2 — Insertar FIG-07 (polar-polarization.png) después de FIG-06, antes de línea 231

```markdown
<figure markdown="span">
  ![Histograma de Bhattacharyya Z(W_{64}^{(i)}) — polarización bimodal](figures/polar-polarization.png)
  <!-- generada por celda 17 de lab.ipynb -->
  <figcaption markdown="1">**Figura 7.** Distribución del parámetro de Bhattacharyya $Z(W_{64}^{(i)})$ para los $N=64$ canales sintéticos de un código Polar de tasa $r_c=1/2$, evaluado a $E_b/N_0=3\ \mathrm{dB}$. La distribución bimodal — con modos en torno a $Z\approx0$ (canales casi perfectos, azul) y $Z\approx1$ (canales casi inútiles, salmón) — es la manifestación del teorema de polarización: a medida que $N$ crece, la fracción de canales intermedios tiende a cero y los canales se polarizan completamente.
  </figcaption>
</figure>

```

**Nota sobre números de celda en comentarios:** Las celdas nuevas son 15 (butterfly), 16 (SC+SCL), 17 (MC+polarization), consistente con los índices 0-based del JSON del notebook tras la inserción.

---

## Common Pitfalls

### Pitfall 1: Z_0 AWGN incorrecto

**Síntoma:** La polarización de N=64 parece débil (histograma casi uniforme, no bimodal).
**Causa:** Usar Z_0 = ε = 0.5 (BEC) en lugar de Z_0 = exp(−Rc·γ) para AWGN.
**Cómo evitar:** Calcular `Z0 = np.exp(-Rc_polar * EbN0_design_lin)` antes de llamar a `bhattacharyya_tree`. [ASSUMED — si se usa ε=0.5 con N=64, Z todavía polariza pero la distribución del frozen set no corresponde al canal AWGN]

### Pitfall 2: Inconsistencia encoder/decoder por bit-reversal

**Síntoma:** BER > BER sin código incluso a alto SNR (el decoder no recupera los bits correctos).
**Causa:** El encoder usa G_N = B_N·F^{⊗n} (con bit-reversal) pero el decoder asume G_N = F^{⊗n}, o viceversa.
**Cómo evitar:** Usar G_N = F^{⊗n} (sin B_N) tanto en encoder (Kronecker) como en decoder (recursivo desde índice 0). El `bhattacharyya_tree` existente es consistente con esta convención. [VERIFIED — consistencia algebraica verificada para N=4]

### Pitfall 3: Redefinir f_func / g_func en nuevas celdas

**Síntoma:** NameError o comportamiento incorrecto si las definiciones anteriores tienen un bug que se "hereda".
**Causa:** Copiar/pegar f_func y g_func en Cell B sin verificar que coinciden con Cell 14.
**Cómo evitar:** Las nuevas celdas NO redefinen f_func/g_func. El comentario en el código debe decir explícitamente "# f_func y g_func definidas en Ex5 (celda 14)".

### Pitfall 4: Contar errores en bits congelados (frozen bits)

**Síntoma:** BER artificialmente alta porque se comparan los N=64 bits de u_hat contra los N=64 bits transmitidos, incluyendo los k_frozen=32 bits congelados que siempre son 0.
**Causa:** `np.sum(u_hat != u_transmitted)` sobre todos los N bits.
**Cómo evitar:** `np.sum(u_hat[list(info_idx)] != msg)` — comparar solo los k=32 bits de información. El denominador del BER también es k, no N.

### Pitfall 5: SCL path pruning incorrecto (empate en metric)

**Síntoma:** SCL no mejora sobre SC, o resultados no reproducibles.
**Causa:** `new_paths.sort(key=...)` no es estable para ties; las cópias de arrays `u.copy()` son O(N) pero necesarias.
**Cómo evitar:** El `sort` de Python es estable; no hay problema con empates. Verificar que `u.copy()` se llama ANTES de modificar `u_new[i]` para no contaminar paths existentes.

### Pitfall 6: MC lento por falta de vectorización

**Síntoma:** La celda de Monte Carlo tarda >5 minutos.
**Causa:** compute_llr_for_bit usa list comprehensions anidadas con f_func/g_func (tanh/arctanh escalares).
**Cómo evitar:** Con N=64 y n_blocks=300, el tiempo estimado es ~30s total (SC+SCL). Si supera 60s, reducir n_blocks a 200. No vectorizar por ahora — la claridad pedagógica prima sobre la velocidad para N=64.

---

## Validation Architecture

### Test Framework

| Property | Value |
|----------|-------|
| Framework | Notebook outputs como integration tests |
| Quick run | Cell B demo a SNR=5 dB: SC y SCL deben recuperar mensaje correctamente |
| Full run | `jupyter nbconvert --execute lab.ipynb` (Phase 6) |
| Figure check | `os.path.getsize('figures/polar-butterfly.png') > 30000` y `polar-polarization.png > 30000` |

### Phase Requirements → Test Map

| ID | Behavior | Test Type | Verificación concreta |
|----|----------|-----------|----------------------|
| LAB-02 | SC BER < BER BPSK sin código a SNR > umbral | MC output | `assert BER_SC[-1] < 0.5*erfc(np.sqrt(10**(4.5/10)))` (BER_SC a 4.5 dB < BER_uncoded) |
| LAB-02 | SCL-8 mejora ≥1 dB a BER=10⁻³ vs SC | visual+numeric | `EbN0_SCL_at_1e3 + 1.0 <= EbN0_SC_at_1e3` |
| FIG-06 | polar-butterfly.png existe y es no-trivial | file check | `os.path.getsize('figures/polar-butterfly.png') > 30_000` |
| FIG-07 | polar-polarization.png bimodal visible | file+print | `assert np.sum(Z_polar < 0.1) >= 10 and np.sum(Z_polar > 0.9) >= 10` |

### Precondición crítica

**Todas las celdas de Phase 4 asumen que Cell 14 ya fue ejecutada** (define f_func, g_func). Si se ejecuta Cell 16 (SC+SCL) sin ejecutar Cell 14 primero, se obtendrá NameError. El planner debe asegurar que las células nuevas tienen la advertencia apropiada en comentarios.

---

## Environment Availability

| Dependencia | Requerida por | Disponible | Fuente |
|-------------|--------------|------------|--------|
| numpy | Encoder, decoder, MC | ✓ | Cell 1 existente |
| scipy.special.erfc | BER teórica en figura | ✓ | Cell 1 existente |
| matplotlib | polar-butterfly.png, polar-polarization.png | ✓ | Cell 1 existente |
| matplotlib.patches (Patch) | Leyenda butterfly | ✓ | Cell 12 ya importa |
| bhattacharyya_tree | Frozen set selection + FIG-07 | ✓ | Cell 12 existente |
| f_func, g_func | SC + SCL decoders | ✓ | Cell 14 existente |

No requiere instalaciones nuevas. [VERIFIED — Cell 1 importa numpy, scipy.special.erfc, matplotlib]

---

## Open Questions (RESOLVED)

1. **¿Usar BEC o AWGN para selección de frozen bits?**
   - **RESOLVED:** AWGN exacto via Z_0 = exp(-Rc·γ) + recursión BEC (proxy válido). La recursión BEC produce el mismo ranking de canales que density evolution para N=64 con error pequeño. Verificación pedagógica: el histograma de Z_polar debe mostrar bimodalidad clara.

2. **¿G_N con o sin bit-reversal?**
   - **RESOLVED:** Sin bit-reversal (G_N = F^{⊗n}). Es coherente con `bhattacharyya_tree` del notebook, más simple pedagógicamente, y produce código correcto sin necesidad de B_N.

3. **¿N=64 o N=128 para FIG-07?**
   - **RESOLVED:** N=64 (igual que LAB-02). Más coherente pedagógicamente — la misma figura que se simula en Monte Carlo. N=128 daría mejor polarización pero es innecesario.

4. **¿Mostrar polar-butterfly.png para N=8 o N=64?**
   - **RESOLVED:** N=8 en la figura (3 etapas, legible). El código LAB-02 usa N=64 pero la figura es de N=8. La figura lleva título explícito "N=8" para evitar confusión.

5. **¿Qué figura de BER generar (si alguna)?**
   - **RESOLVED:** La figura de BER SC vs SCL se genera en Cell C. NO se guarda como figura numerada (FIG-0X) — es una figura auxiliar dentro de la celda, no referenciada en index.md. Solo FIG-06 y FIG-07 van a index.md.

---

## Sources

### Primary (HIGH confidence)
- lab.ipynb (ground truth) — estructura de 18 celdas, funciones existentes (f_func, g_func, bhattacharyya_tree), convención G_4 = [[1,0,0,0],[1,1,0,0],[1,0,1,0],[1,1,1,1]] verificada
- index.md — líneas exactas 229-231 verificadas en esta sesión para puntos de inserción
- REQUIREMENTS.md — descripción exacta de FIG-06, FIG-07, LAB-02 leída

### Secondary (MEDIUM confidence)
- [ASSUMED] Bhattacharyya Z_0 = exp(-Rc·γ) para BPSK AWGN: derivación algebraica correcta; fórmula exacta de Arıkan (2009) no verificada numéricamente en esta sesión
- [ASSUMED] SCL-8 mejora ~1-2 dB sobre SC para N=64 tasa 1/2: basado en literatura estándar (Tal & Vardy 2015); no simulado numéricamente aquí
- [ASSUMED] Timing: SC ~3s, SCL ~25s para n_blocks=300, 9 SNR points, basado en scaling desde timing Phase 3 (bp_awgn)

### Tertiary (LOW confidence)
- [ASSUMED] Distribución bimodal clara a N=64: estimado de convergencia geométrica de recursión Z; no calculado analíticamente

---

## Assumptions Log

| # | Claim | Section | Riesgo si incorrecto |
|---|-------|---------|----------------------|
| A1 | Z_0 = exp(-Rc·γ) es el Bhattacharyya exacto de BPSK AWGN | Frozen set | Medio — si la fórmula está mal por factor de 2, el frozen set cambia ligeramente pero el código sigue siendo válido pedagógicamente |
| A2 | SCL-8 mejora ≥1 dB sobre SC para N=64 tasa 1/2 | Monte Carlo | Medio — el criterio LAB-02 Success Criterion 2 exige esta mejora; si N=64 es demasiado pequeño para mostrarla, cambiar a N=128 |
| A3 | Timing SC ~3s, SCL ~25s | Monte Carlo | Bajo — si SCL tarda >60s, reducir n_blocks o L |
| A4 | Distribución Z bimodal clara a N=64 | FIG-07 | Bajo — con Z_0=0.368 y n=6 etapas, la recursión cuadrática converge rápido |
| A5 | f_func/g_func de Cell 14 son las del notebook final post-Phase3 | SC/SCL | Bajo — leído el código de Cell 14 en esta sesión; son exactamente f(a,b)=2arctanh(tanh(a/2)tanh(b/2)) y g(a,b,u)=b+(1-2u)a |

---

## Metadata

**Confidence breakdown:**
- Polar encoder (G_N): HIGH — derivación algebraica exacta, verificada para N=4
- Frozen bit selection (Z_0 AWGN): HIGH — fórmula estándar; reutiliza bhattacharyya_tree existente
- SC decoder: HIGH — implementación estándar, coherente con encoder
- SCL decoder: MEDIUM — implementación pedagógica correcta en principio; no simulada numéricamente en esta sesión
- Figure designs: MEDIUM — layouts razonables, apariencia visual no pre-renderizada
- Cell insertion points: HIGH — estructura de notebook verificada directamente

**Research date:** 2026-05-29
**Valid until:** 2026-06-28
