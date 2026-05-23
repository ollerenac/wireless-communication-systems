# Phase 2: Corrección de Contenido — Pattern Map

**Mapped:** 2026-05-22
**Files analyzed:** 2 (index.md modified, figures/ directory — 6 PNG additions)
**Analogs found:** 2/2 — index.md is its own analog; figures/ directory already exists

---

## File Classification

| New/Modified File | Role | Data Flow | Closest Analog | Match Quality |
|---|---|---|---|---|
| `index.md` | pedagogical document | transform (formula correction + snippet alignment + figure insertion) | `index.md` itself (existing sections) | exact — same file, same MkDocs-Material stack |
| `figures/*.png` (6 files) | static asset | file-I/O (commit to disk) | `figures/` existing PNGs | exact — same directory, same naming convention |

---

## Pattern Assignments

### `index.md` — Formula corrections, snippet alignment, figure insertion

**Analog:** `index.md` (existing sections — read-only reference)

---

#### Pattern 1: Figure block with `<figure>` wrapper and `<figcaption>`

Used at lines 59–62 and 233–236. This is the pattern for **any new figure reference** that needs a caption (i.e., D-03: adding `mmse-vs-zf-constellation.png` to §4.8).

**Source:** `index.md` lines 59–62 (Figura 1) and lines 233–236 (Figura 2):

```html
<figure markdown="span">
  ![Alt text descriptivo](figures/nombre-archivo.png)
  <figcaption markdown="1">**Figura N.** Descripción completa en español con $math$ inline si aplica.</figcaption>
</figure>
```

Concrete existing instance (lines 233–236):

```html
<figure markdown="span">
  ![El transmisor OFDM es una IFFT](figures/ofdm-ifft-transmitter.png)
  <figcaption markdown="1">**Figura 2.** $N$ símbolos en frecuencia $X[k]$ (izquierda) entran a la IFFT y producen $N$ muestras en tiempo $x[n]$ (derecha). La tasa de muestreo $f_s = N\cdot\Delta f$ es la que garantiza que $\Delta f$ se cancele en el exponente.</figcaption>
</figure>
```

**Decision D-03 note:** `mmse-vs-zf-constellation.png` goes into §4.8 (lines 907–935 region). Per CONTEXT.md Specifics, it closes §4.8 visually before the `---` divider at line 935. Caption/alt-text is at Claude's discretion.

---

#### Pattern 2: Bare image reference (no `<figure>` wrapper)

Several figures in index.md use the bare `![]()` form without a `<figure>` tag. These appear inline within text or inside admonitions. No caption. Used for non-numbered figures.

**Source:** `index.md` line 308, 405, 739, 753, 782, 814, 840, 868, 953, 961:

```markdown
![Alt text descriptivo](figures/nombre-archivo.png)
```

With optional width attribute:

```markdown
![Alt text descriptivo](figures/nombre-archivo.png){ width=600 }
```

---

#### Pattern 3: LaTeX display math block ($$...$$)

**Source:** `index.md` line 229 (IFFT definition — correct form):

```latex
$$x[n] = \frac{1}{\sqrt{N}} \sum_{k=0}^{N-1} X[k]\, e^{j2\pi kn/N}, \quad n = 0, 1, \ldots, N-1$$
```

**BLOCKER-S.01 correction target** — line 240, current erroneous text:

```latex
$$\frac{1}{N}\sum_{n=0}^{N-1} x[n]\, e^{-j2\pi kn/N} = \frac{1}{\sqrt{N}}\sum_{l=0}^{N-1} X[l] \underbrace{\left(\frac{1}{N}\sum_{n=0}^{N-1} e^{j2\pi (l-k)n/N}\right)}_{\text{término de interferencia de }l\text{ sobre }k}$$
```

Must become (outer factor `1/N` → `1/√N`, decision D-06):

```latex
$$\frac{1}{\sqrt{N}}\sum_{n=0}^{N-1} x[n]\, e^{-j2\pi kn/N} = \frac{1}{\sqrt{N}}\sum_{l=0}^{N-1} X[l] \underbrace{\left(\frac{1}{N}\sum_{n=0}^{N-1} e^{j2\pi (l-k)n/N}\right)}_{\text{término de interferencia de }l\text{ sobre }k}$$
```

**MINOR-01 correction target** — line 249, current erroneous text (inside `??? note` block):

```latex
$$\frac{1}{N}\sum_{n=0}^{N-1} x[n]\, e^{-j2\pi kn/N} = \frac{1}{N}\sum_{n=0}^{N-1} \left(\frac{1}{\sqrt{N}} \sum_{l=0}^{N-1} X[l]\, e^{j2\pi ln/N}\right) e^{-j2\pi kn/N}$$
```

Must become (both outer `1/N` factors → `1/√N`, decision D-08):

```latex
$$\frac{1}{\sqrt{N}}\sum_{n=0}^{N-1} x[n]\, e^{-j2\pi kn/N} = \frac{1}{\sqrt{N}}\sum_{n=0}^{N-1} \left(\frac{1}{\sqrt{N}} \sum_{l=0}^{N-1} X[l]\, e^{j2\pi ln/N}\right) e^{-j2\pi kn/N}$$
```

**BLOCKER-S.02 correction target** — line 1029, current erroneous text:

```latex
$$\eta_{\text{neta}} = \underbrace{\frac{N_{CP}}{N + N_{CP}}}_{\text{overhead CP}} \times \underbrace{\frac{N - N_{\text{guard}} - N_{\text{pilot}}}{N}}_{\text{overhead frecuencial}} \times \log_2 M \times r_c$$
```

Must become (fraction inverted, label updated, decisions D-07):

```latex
$$\eta_{\text{neta}} = \underbrace{\frac{N}{N + N_{CP}}}_{\text{eficiencia temporal}} \times \underbrace{\frac{N - N_{\text{guard}} - N_{\text{pilot}}}{N}}_{\text{overhead frecuencial}} \times \log_2 M \times r_c$$
```

---

#### Pattern 4: Collapsible admonition (`??? note` / `??? example`)

**Source:** `index.md` lines 242–259 (complete `??? note` block):

```markdown
??? note "¿Cómo se pasa de $x[n]$ a la suma sobre $X[l]$?"
    La definición de $x[n]$ de la sección anterior es:

    $$x[n] = \frac{1}{\sqrt{N}} \sum_{l=0}^{N-1} X[l]\, e^{j2\pi ln/N}$$

    Se sustituye directamente dentro de la operación del receptor:

    $$\frac{1}{N}\sum_{n=0}^{N-1} x[n]\, e^{-j2\pi kn/N} = ...$$
```

Key rules:
- `???` = collapsible (closed by default); `!!!` = always-open
- 4-space indent for all content inside the block
- Fenced math blocks inside admonitions use the same `$$...$$` syntax
- Images inside admonitions use bare `![]()` (no `<figure>` wrapper)

Example of image inside admonition (lines 811–814):

```markdown
??? example "Verificación"
    La figura compara BER de ZF y MMSE sobre el canal de referencia. A SNR baja, MMSE supera a ZF en las subportadoras débiles; a SNR alta ambos convergen:

    ![BER ZF vs MMSE](figures/ofdm-ber-equalizers.png)
```

---

#### Pattern 5: Python code snippet block

**Source:** `index.md` lines 806–809 (current MMSE inline snippet):

```markdown
```python
SNR_lin   = 10 ** (SNR_dB / 10)
X_hat     = (np.conj(H) / (np.abs(H)**2 + 1/SNR_lin)) * Y
```
```

**MINOR-03 correction target** — replace lines 806–808 with full function signature from notebook (decision D-09):

```python
def mmse_equalizer(Y, h, N, SNR_dB):
    """MMSE: regulariza la inversión del canal → limita amplificación de ruido en fades."""
    H   = np.fft.fft(h, n=N)
    SNR = 10 ** (SNR_dB / 10)
    return (np.conj(H) / (np.abs(H)**2 + 1/SNR)) * Y
```

**Source:** `index.md` lines 886–895 (current LS inline snippet):

```python
pilot_spacing = 8
pilot_idx     = np.arange(0, N, pilot_spacing)
X_pilot       = np.ones(len(pilot_idx))            # pilotos BPSK: valor conocido = +1

# Estimación LS en posiciones piloto
H_ls = Y[pilot_idx] / X_pilot

# Interpolación lineal al resto de subportadoras
H_est = np.interp(np.arange(N), pilot_idx, H_ls)
```

**MINOR-04 correction target** — replace lines 886–895 with full function signature from notebook (decision D-09):

```python
def ls_channel_estimate(Y, pilot_idx, X_pilot, N):
    """Estimación LS en pilotos + interpolación lineal a todas las subportadoras."""
    H_ls = Y[pilot_idx] / X_pilot
    H_est = (np.interp(np.arange(N), pilot_idx, H_ls.real) +
             1j * np.interp(np.arange(N), pilot_idx, H_ls.imag))
    return H_est
```

---

#### Pattern 6: §4.8 section structure (insertion point for D-03)

**Source:** `index.md` lines 907–935 (complete §4.8 QAM Demapper section):

The section ends at line 935 with a `---` divider before `### 5. Rendimiento End-to-End`. The `mmse-vs-zf-constellation.png` figure reference (D-03) should be inserted before the closing `---` at line 935, after the last paragraph of §4.8 (line 933). Use a bare `<figure>` block (Pattern 1) since this is a pedagogically-numbered figure with a caption.

Insertion point: between line 933 (end of LLR paragraph) and line 935 (`---`).

---

### `figures/*.png` — 6 new PNG files to commit

**Analog:** existing files in `figures/` directory

All 6 files already exist on disk (generated during Phase 1 audit notebook execution). Decision D-01 says to commit them as-is. No `index.md` changes needed for 4 of them (D-04); one (`mmse-vs-zf-constellation.png`) gets a reference added per D-03.

| File | Already on disk | index.md reference needed |
|------|-----------------|---------------------------|
| `figures/ofdm-ber-equalizers.png` | YES | NO — refs already exist at lines 814, 953 |
| `figures/ofdm-per-subcarrier-ber.png` | YES | NO — ref already exists at line 961 |
| `figures/mmse-vs-zf-constellation.png` | YES | YES — add per D-03 |
| `figures/channel-estimation-pilots.png` | YES | NO — D-04 |
| `figures/qpsk-decision-regions.png` | YES | NO — D-04 |
| `figures/ofdm-time-domain.png` | YES | NO — D-04 |
| `figures/cp-effect-constellation.png` | YES | NO — D-04 |

Naming convention in `figures/`: lowercase, hyphen-separated, `.png` extension. All new files already follow this convention.

---

## Shared Patterns

### Math inline within prose

**Apply to:** all formula corrections in §2 (line 240, 249) and §6 (line 1029)

Inline math uses single `$...$`. Display math uses `$$...$$` on its own line. `\underbrace{...}_{label}` for annotated expressions. `\text{...}` for non-italic text within math. Convention in this document: `\,` thin space before differential-style terms, `\ldots` for ellipsis in sequences.

**Source:** `index.md` line 240 (existing display math with underbrace):

```latex
$$\frac{1}{N}\sum_{n=0}^{N-1} x[n]\, e^{-j2\pi kn/N} = \frac{1}{\sqrt{N}}\sum_{l=0}^{N-1} X[l] \underbrace{\left(\frac{1}{N}\sum_{n=0}^{N-1} e^{j2\pi (l-k)n/N}\right)}_{\text{término de interferencia de }l\text{ sobre }k}$$
```

### Section heading format

**Apply to:** §4.8 insertion (D-03)

Sections use `####` for subsections (e.g., `#### 4.8 QAM Demapper`). The entry line pattern below each heading is bold: `**Entrada:** ... — **Operación:** ... — **Salida:** ...`. New figure goes after the body text, before the closing `---`.

---

## No Analog Found

No files in this phase lack an analog. All patterns are present in `index.md` itself. The figure files are binary PNGs with no code pattern to extract.

---

## Edit Sequence for Planner

The following edit order minimizes diff conflicts (each edit targets a non-overlapping line range):

| Order | Target | Lines | Decision | Change |
|-------|--------|-------|----------|--------|
| 1 | `index.md` line 240 | 240 | D-06/BLOCKER-S.01 | `1/N` → `1/√N` outer factor |
| 2 | `index.md` line 249 | 249 | D-08/MINOR-01 | `1/N` → `1/√N` in note block |
| 3 | `index.md` line 1029 | 1029 | D-07/BLOCKER-S.02 | invert fraction + relabel |
| 4 | `index.md` lines 806–808 | 806–809 | D-09/MINOR-03 | replace inline with full function |
| 5 | `index.md` lines 886–895 | 886–896 | D-09/MINOR-04 | replace inline with full function |
| 6 | `index.md` after line 933 | 934 (insert) | D-03/MINOR-02 | add `<figure>` block for `mmse-vs-zf-constellation.png` |
| 7 | `figures/` (git add) | — | D-01 | commit 6 PNG files |

Edits 1–6 are in ascending line order. Edits 4 and 5 change the number of lines (expanding the snippet), so line numbers for edit 6 shift by the net line delta of edits 4+5 — planner must account for this when computing the final insertion line.

---

## Metadata

**Analog search scope:** `index.md` (1326 lines), `figures/` directory, `.planning/phases/01-auditor-a-y-diagn-stico/01-AUDIT-FINDINGS.md`
**Files scanned:** 3
**Pattern extraction date:** 2026-05-22
