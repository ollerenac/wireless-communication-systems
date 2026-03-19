# Sistemas de Comunicaciones Inalámbricas

Curso de máster de acceso abierto sobre sistemas de comunicaciones inalámbricas — desde fundamentos de capa física hasta tecnologías emergentes de 5G/6G.

**Sitio web**: [ollerenac.github.io/wireless-communication-systems](https://ollerenac.github.io/wireless-communication-systems/)
**Licencia**: [![CC BY 4.0](https://img.shields.io/badge/License-CC%20BY%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by/4.0/)

---

## Estructura del Curso

15 sesiones semanales de 3 horas cada una (~90 min teoría + ~90 min laboratorio Python), organizadas en tres arcos temáticos:

### Arco 1 — Fundamentos de Capa Física (Sesiones 1–5)

| # | Carpeta | Título | Apuntes | Laboratorio |
|---|---------|--------|---------|-------------|
| 01 | `docs/sessions/01-channel-modeling/` | Modelado del Canal Inalámbrico | [index.md](docs/sessions/01-channel-modeling/index.md) | [lab.ipynb](docs/sessions/01-channel-modeling/lab.ipynb) |
| 02 | `docs/sessions/02-digital-modulation/` | Modulación Digital y Análisis de BER | — | — |
| 03 | `docs/sessions/03-ofdm-systems/` | Sistemas OFDM e Implementación | — | — |
| 04 | `docs/sessions/04-channel-coding/` | Codificación de Canal: LDPC y Polar | — | — |
| 05 | `docs/sessions/05-multiple-access/` | Acceso Múltiple: OFDMA, NOMA y RRM | — | — |

### Arco 2 — Sistemas Multi-Antena (Sesiones 6–8)

| # | Carpeta | Título | Apuntes | Laboratorio |
|---|---------|--------|---------|-------------|
| 06 | `docs/sessions/06-mimo-fundamentals/` | Fundamentos MIMO y Capacidad | — | — |
| 07 | `docs/sessions/07-massive-mimo/` | MIMO Masivo y Conformación de Haz Digital | — | — |
| 08 | `docs/sessions/08-channel-estimation/` | Estimación de Canal: Métodos Clásicos | — | — |

### Arco 3 — Tecnologías Avanzadas y Emergentes (Sesiones 9–15)

| # | Carpeta | Título | Apuntes | Laboratorio |
|---|---------|--------|---------|-------------|
| 09 | `docs/sessions/09-5g-nr/` | Arquitectura 5G NR: Interfaz Radio y Numerología | — | — |
| 10 | `docs/sessions/10-mmwave/` | Comunicaciones mmWave y Sub-THz | — | — |
| 11 | `docs/sessions/11-ris/` | Superficies Inteligentes Reconfigurables (RIS) | — | — |
| 12 | `docs/sessions/12-isac/` | Detección e Integración con Comunicaciones (ISAC) | — | — |
| 13 | `docs/sessions/13-cognitive-radio/` | Radio Cognitiva y Gestión Dinámica de Espectro | — | — |
| 14 | `docs/sessions/14-ml-wireless/` | IA/ML para Comunicaciones Inalámbricas | — | — |
| 15 | `docs/sessions/15-6g-frontiers/` | 6G: Fronteras, Investigación Abierta y Redes Especializadas | — | — |

---

## Prerrequisitos

Para seguir el curso con aprovechamiento, el estudiante debe tener conocimientos sólidos en:

| Área | Contenidos clave |
|------|-----------------|
| Señales y Sistemas | Transformada de Fourier, convolución, filtrado |
| Probabilidad y Estadística | Variables aleatorias, distribuciones, ruido gaussiano |
| Comunicaciones Digitales | Modulación en banda base, filtro adaptado, SNR |
| Álgebra Lineal | Operaciones matriciales, SVD, valores propios |
| Programación | Python básico (NumPy, Matplotlib), cuadernos Jupyter |

---

## Opción A — Sitio Web (recomendado, sin instalación)

Navega el curso en el sitio web publicado. Cada sesión incluye apuntes con matemáticas renderizadas y un botón **Abrir en Colab** para ejecutar el laboratorio en el navegador sin instalar nada:

**[ollerenac.github.io/wireless-communication-systems](https://ollerenac.github.io/wireless-communication-systems/)**

---

## Opción B — Clonar el Repositorio (uso local)

### 1. Clonar

```bash
git clone https://github.com/ollerenac/wireless-communication-systems.git
cd wireless-communication-systems
```

### 2. Instalar dependencias del sitio

```bash
pip install -r requirements.txt
```

### 3. Vista previa local del sitio

```bash
mkdocs serve
# Abre http://127.0.0.1:8000 en tu navegador
```

### 4. Ejecutar un laboratorio localmente

```bash
# Instalar Jupyter si no está disponible
pip install jupyter

# Abrir el laboratorio de una sesión concreta
jupyter notebook docs/sessions/01-channel-modeling/lab.ipynb
```

Cada laboratorio declara sus dependencias Python en su primera celda de código (`%pip install ...`). Ejecútalas para reproducir todos los resultados.

> **Alternativa sin instalación**: cada notebook incluye un badge **Open in Colab** que abre el laboratorio directamente en Google Colab desde el repositorio de GitHub — sin subir archivos ni instalar nada localmente.

---

## Contribuir

¿Encuentras un error o quieres añadir contenido? Consulta [CONTRIBUTING.md](CONTRIBUTING.md) para el workflow de contribución y los criterios de calidad del contenido.

---

## Licencia y Atribución

Todo el contenido se publica bajo [Creative Commons Atribución 4.0 Internacional (CC BY 4.0)](https://creativecommons.org/licenses/by/4.0/).

Eres libre de compartir, adaptar y redistribuir este material para cualquier propósito — incluso comercial — siempre que cites la fuente:

> *Sistemas de Comunicaciones Inalámbricas* por ollerenac
> https://github.com/ollerenac/wireless-communication-systems
> Licencia CC BY 4.0
