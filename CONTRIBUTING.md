# Guía de Contribución

Gracias por contribuir a *Sistemas de Comunicaciones Inalámbricas*. Esta guía describe el workflow de contribución, la estructura de carpetas y los criterios de calidad que todo contenido debe cumplir antes de ser publicado.

---

## Workflow de Contribución

### 1. Crear una rama de trabajo

```bash
git checkout -b sesion-NN-descripcion-breve
# Ejemplo: git checkout -b sesion-02-digital-modulation
```

### 2. Añadir o editar contenido

Sigue la [Estructura de Sesión](#estructura-de-sesión) y el [Checklist de Calidad](#checklist-de-calidad-de-contenido) descritos abajo.

### 3. Verificar localmente

```bash
pip install -r requirements.txt
mkdocs serve   # Comprueba que el sitio construye sin errores y las ecuaciones renderizan
```

### 4. Limpiar outputs del notebook

```bash
jupyter nbconvert --clear-output docs/sessions/NN-topic/lab.ipynb
```

### 5. Abrir un Pull Request

- Título conciso: `Sesión NN — Título del tema`
- Describe brevemente los cambios en el cuerpo del PR
- El checklist del PR template se completará automáticamente

### 6. Revisión y merge

Un maintainer revisará el contenido contra el [Checklist de Calidad](#checklist-de-calidad-de-contenido). Una vez aprobado, el merge a `main` desencadena el redeploy automático del sitio.

---

## Estructura de Sesión

Cada sesión vive en su propia carpeta bajo `docs/sessions/`:

```
docs/sessions/NN-topic-name/
├── index.md      # Apuntes de teoría + ejercicios
├── lab.ipynb     # Laboratorio Python (~90 min)
└── figures/      # Figuras PNG (300 DPI, fondo blanco)
    ├── figura-1.png
    └── figura-2.png
```

### Convención de nombres

| Elemento | Formato | Ejemplo |
|----------|---------|---------|
| Carpeta de sesión | `NN-kebab-case` | `02-digital-modulation` |
| Figuras | `nombre-descriptivo.png` | `ber-vs-snr.png` |
| Notebooks | siempre `lab.ipynb` | `lab.ipynb` |

---

## Frontmatter obligatorio en `index.md`

```yaml
---
title: "Sesión NN — Título de la Sesión"
session: NN
description: "Descripción breve de una línea para SEO y navegación."
---
```

Mientras la sesión está en desarrollo, añadir `status: draft` para que aparezca con el badge WIP en el sitio:

```yaml
---
title: "Sesión NN — Título"
session: NN
description: "..."
status: draft
---
```

Eliminar `status: draft` una vez completada la revisión técnica.

---

## Estructura de `index.md`

Cada `index.md` debe seguir este orden de secciones:

1. `## Objetivos de Aprendizaje` — lista numerada de 4–6 objetivos verificables
2. `## Introducción` — motivación del tema, por qué importa en este curso
3. `## Teoría` — subsecciones numeradas con teoría, derivaciones y figuras
4. `## Síntesis` — inventario completo de conceptos introducidos con implicaciones de diseño
5. `## Ejercicios` — mínimo 5 ejercicios con soluciones (ver criterios abajo)
6. `## Laboratorio Python` — enlace Colab badge + descripción de los ejercicios del lab
7. `## Lecturas Recomendadas` — referencias bibliográficas con capítulo/sección específica

---

## Checklist de Calidad de Contenido

Este checklist implementa la metodología pedagógica establecida en la Sesión 01. Todo PR debe satisfacerlo antes del merge.

### Narrativa y transiciones

- [ ] Cada subsección abre respondiendo la pregunta dejada abierta por la anterior (transición implícita — sin anuncios del tipo "a continuación veremos")
- [ ] La frase de cierre de cada subsección crea la necesidad de la siguiente
- [ ] Cuando se extiende un modelo, se declara explícitamente la suposición que hacía el modelo anterior antes de relajarla

### Ecuaciones y derivaciones

- [ ] Toda ecuación clave va precedida de su motivación física o geométrica
- [ ] La cadena lógica (fenómeno físico → pasos intermedios → fórmula) es visible
- [ ] Todos los parámetros de cada ecuación están definidos inmediatamente tras su aparición
- [ ] Cuando un concepto tiene representaciones duales (frecuencia/tiempo, dispersión/coherencia), se incluye una tabla de dualidad

### Figuras

- [ ] Toda figura va seguida de un párrafo de lectura guiada: panel a panel, en orden, con el takeaway explícito
- [ ] Cuando dos modelos contrastan, se incluye una figura de comparación lado a lado
- [ ] Las figuras son PNG a 300 DPI con fondo blanco, generadas desde el notebook o con matplotlib

### Conceptos asumidos por expertos

- [ ] Todo concepto que un experto da por sentado pero un estudiante puede no entender recibe una explicación física explícita antes de su uso matemático
- [ ] La prueba: ¿puede un estudiante con los prerrequisitos del curso seguir la explicación sin referencias adicionales?

### Estructura de la sesión

- [ ] La última subsección técnica integra todos los parámetros de la sesión en un estándar o sistema real (p.ej. 3GPP TR 38.901) con un ejemplo numérico end-to-end
- [ ] La `## Síntesis` enumera **todas** las dimensiones conceptuales introducidas, con implicaciones de diseño y referencias a sesiones futuras donde se abordan las técnicas de mitigación
- [ ] Los ejercicios progresan de concepto único (temas individuales) a integrador; el último ejercicio combina ≥3 conceptos distintos de la sesión

### Ejercicios

- [ ] Mínimo 5 ejercicios por sesión
- [ ] Todos incluyen solución paso a paso en bloque colapsable: `??? example "Solución"`
- [ ] Mix de ejercicios analíticos (lápiz y papel) y computacionales
- [ ] El último ejercicio es integrador (combina ≥3 conceptos de la sesión)

### Terminología

- [ ] Los términos técnicos de dominio están en inglés aunque el texto circundante esté en español (shadowing, fading, multipath fading, delay spread, coherence bandwidth, beamforming, water-filling, cyclic prefix, outage, BER, SNR, etc.)
- [ ] En la primera aparición: término en inglés seguido de glosa en español entre paréntesis — p.ej. *shadowing* (efecto sombra)
- [ ] No se usan traducciones inventadas al español como etiqueta principal

### Notebook (`lab.ipynb`)

- [ ] Celda 1: título de la sesión + badge Open in Colab
- [ ] Celda 2: objetivos del laboratorio (lista numerada)
- [ ] Celda 3: `%pip install` de dependencias + imports + configuración matplotlib
- [ ] Celda 4: repaso teórico conciso que conecta con `index.md`
- [ ] Celdas de ejercicio: al menos 5 ejercicios con preguntas de reflexión
- [ ] Celda final: conclusiones + lecturas adicionales
- [ ] Outputs borrados antes del commit (`jupyter nbconvert --clear-output`)
- [ ] Badge Colab apunta a la URL correcta del archivo raw en GitHub

---

## Actualizar la Navegación

Tras añadir una nueva sesión, actualizar `mkdocs.yml`:

```yaml
nav:
  - Inicio: index.md
  - Programa: syllabus.md
  - Sesiones:
    - "01 — Modelado del Canal": sessions/01-channel-modeling/index.md
    - "02 — Modulación Digital": sessions/02-digital-modulation/index.md
    # añadir aquí la nueva sesión
```

---

## Preguntas

Abre un [issue en GitHub](https://github.com/ollerenac/wireless-communication-systems/issues) con la etiqueta `question` para cualquier duda sobre contenido o proceso.
