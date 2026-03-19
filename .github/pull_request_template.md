## Sesión NN — Título del tema

<!-- Reemplaza NN y el título. Describe brevemente los cambios en 1-2 líneas. -->

---

## Checklist de revisión de contenido

Marca cada ítem antes de solicitar revisión. Un PR no puede mergearse hasta que todos estén marcados.

### Estructura y archivos

- [ ] Carpeta nombrada `NN-kebab-case` bajo `docs/sessions/`
- [ ] Los tres archivos obligatorios presentes: `index.md`, `lab.ipynb`, `figures/`
- [ ] Frontmatter de `index.md` válido: `title`, `session`, `description` presentes; `status: draft` añadido si la sesión no está finalizada
- [ ] Sesión añadida al nav en `mkdocs.yml`

### Contenido de `index.md`

- [ ] Las 7 secciones obligatorias presentes en orden: Objetivos de Aprendizaje, Introducción, Teoría, Síntesis, Ejercicios, Laboratorio Python, Lecturas Recomendadas
- [ ] Mínimo 5 ejercicios con soluciones paso a paso en bloques `??? example "Solución"`
- [ ] El último ejercicio es integrador (combina ≥3 conceptos de la sesión)
- [ ] La `## Síntesis` enumera **todas** las dimensiones conceptuales introducidas, con implicaciones de diseño y referencias a sesiones futuras
- [ ] La última subsección técnica incluye un ejemplo numérico end-to-end ligado a un estándar real (3GPP TR 38.901 u otro)
- [ ] Los términos técnicos de dominio están en inglés (shadowing, fading, delay spread, BER…); primera aparición con glosa en español entre paréntesis

### Ecuaciones y figuras

- [ ] Toda ecuación clave va precedida de su motivación física o geométrica
- [ ] Todos los parámetros de cada ecuación están definidos inmediatamente tras su aparición
- [ ] Toda figura va seguida de un párrafo de lectura guiada (panel a panel, takeaway explícito)
- [ ] Las figuras son PNG a 300 DPI con fondo blanco, en `figures/`

### Notebook (`lab.ipynb`)

- [ ] Celda 1: título de la sesión + badge Open in Colab apuntando a la URL raw correcta en GitHub
- [ ] Celda 2: objetivos del laboratorio
- [ ] Celda 3: `%pip install` + imports + configuración matplotlib
- [ ] Celda 4: repaso teórico conciso
- [ ] Al menos 5 ejercicios con preguntas de reflexión
- [ ] Celda final: conclusiones + lecturas adicionales
- [ ] Outputs borrados (`jupyter nbconvert --clear-output docs/sessions/NN-topic/lab.ipynb`)

### Verificación técnica

- [ ] `mkdocs serve` construye sin errores y las ecuaciones renderizan en el navegador
- [ ] El badge Colab abre el notebook correctamente desde GitHub
- [ ] Las soluciones de los ejercicios son correctas (verificadas a mano o con código)
- [ ] El código Python del notebook ejecuta sin errores en Colab
