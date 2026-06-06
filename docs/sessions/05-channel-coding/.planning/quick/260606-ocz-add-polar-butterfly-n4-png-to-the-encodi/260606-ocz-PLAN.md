---
phase: quick-260606-ocz
plan: 01
type: execute
wave: 1
depends_on: []
files_modified: [index.md, lab.ipynb]
autonomous: true
requirements: [DOC-POLAR-N4-FIG]

must_haves:
  truths:
    - "El admonition de §4.1 muestra la figura polar-butterfly-n4.png al inicio, antes de '**Escenario.**'"
    - "lab.ipynb contiene una celda de código que genera figures/polar-butterfly-n4.png"
    - "mkdocs build --strict pasa sin errores"
  artifacts:
    - path: "index.md"
      provides: "Bloque <figure markdown=\"span\"> dentro del admonition §4.1 (indentado 4 espacios)"
      contains: "polar-butterfly-n4.png"
    - path: "lab.ipynb"
      provides: "Celda de código generadora de polar-butterfly-n4.png insertada tras cell 15"
      contains: "figures/polar-butterfly-n4.png"
    - path: "figures/polar-butterfly-n4.png"
      provides: "Figura N=4 ya generada (existe)"
  key_links:
    - from: "index.md §4.1"
      to: "figures/polar-butterfly-n4.png"
      via: "etiqueta <img> dentro de <figure markdown=\"span\">"
      pattern: "polar-butterfly-n4\\.png"
---

<objective>
Añadir la figura de apoyo `polar-butterfly-n4.png` al ejemplo de encoding butterfly N=4 en §4.1 de `index.md`, y añadir la celda generadora correspondiente en `lab.ipynb` (manteniendo el notebook como ground truth de las figuras).

Purpose: La figura ilustra visualmente el cálculo paso a paso del ejemplo N=4, mejorando la pedagogía y la paridad de calidad con la sesión 03.
Output: Bloque `<figure>` en index.md + nueva celda de código en lab.ipynb.
</objective>

<execution_context>
@$HOME/.claude/get-shit-done/workflows/execute-plan.md
@$HOME/.claude/get-shit-done/templates/summary.md
</execution_context>

<context>
@./CLAUDE.md

# Punto de inserción en index.md — el admonition empieza en línea 332:
#   332  ??? example "Ejemplo: encoding butterfly N=4 paso a paso"
#   333  (línea en blanco)
#   334      **Escenario.** Código Polar $N=4$, tasa $r_c=1/2$...
# El bloque <figure> va indentado 4 espacios, entre línea 333 y 334
# (después de la línea en blanco que sigue a "??? example", antes de "**Escenario.**").

# Punto de inserción en lab.ipynb:
# Cell 15 (index 15) es la celda combinada que contiene el encoder Polar N=64
# Y la generación de FIG-06 polar-butterfly.png (N=8) con savefig al final.
# La nueva celda N=4 se inserta INMEDIATAMENTE DESPUÉS de cell 15 (nuevo índice 16).
# El notebook tiene 22 celdas en total.
</context>

<tasks>

<task type="auto">
  <name>Task 1: Insertar bloque figure N=4 en §4.1 de index.md</name>
  <files>index.md</files>
  <action>
Insertar, dentro del admonition `??? example "Ejemplo: encoding butterfly N=4 paso a paso"` (empieza en línea 332), un bloque `<figure markdown="span">` indentado 4 espacios. Va después de la línea en blanco (333) y ANTES del párrafo `**Escenario.**` (línea 334). El bloque exacto a insertar (cada línea con 4 espacios de indentación para permanecer dentro del admonition):

    <figure markdown="span">
      ![Red butterfly Arikan para código Polar N=4](figures/polar-butterfly-n4.png)
      <!-- generada por celda 16 de lab.ipynb -->
      <figcaption markdown="1">**Red butterfly para el ejemplo.** Código Polar $N=4$, $k=2$, tasa $r_c=1/2$. Los nodos de entrada (izquierda) muestran los valores del vector $\mathbf{u}=[0,0,1,0]$: los salmón son bits congelados (fijados a 0), los azules son bits de información. Los valores intermedios $w_i$ entre etapas y la codeword de salida $\mathbf{x}=[1,0,1,0]$ (cuadrados, derecha) corresponden paso a paso al cálculo detallado a continuación.</figcaption>
    </figure>

Dejar una línea en blanco (indentada o vacía) entre el cierre `</figure>` y el párrafo `**Escenario.**` para que MkDocs no fusione bloques. Usar la misma sintaxis `<figure markdown="span">` que el resto del archivo.
  </action>
  <verify>
    <automated>grep -n "polar-butterfly-n4.png" index.md && grep -q "Red butterfly para el ejemplo" index.md && echo OK</automated>
  </verify>
  <done>El admonition §4.1 contiene el bloque figure con polar-butterfly-n4.png indentado 4 espacios, antes de "**Escenario.**".</done>
</task>

<task type="auto">
  <name>Task 2: Insertar celda generadora N=4 en lab.ipynb y verificar build</name>
  <files>lab.ipynb</files>
  <action>
Insertar una nueva celda de código en `lab.ipynb` en el índice 16 (inmediatamente después de cell 15, la celda que termina con `plt.savefig('figures/polar-butterfly.png', ...)`). Editar el JSON del notebook con la herramienta Edit (NO regenerar el notebook completo). La nueva celda tiene `cell_type: "code"`, `metadata: {}`, `outputs: []`, `execution_count: null`, y `source` = el script Python especificado en el contexto de planning (verbatim, dividido por líneas como array JSON de strings con `\n` al final de cada línea excepto la última).

El script genera `figures/polar-butterfly-n4.png` con N=4, frozen_set={0,1}, u=[0,0,1,0] → x=[1,0,1,0], dos etapas XOR, nodos salmón/azules, salidas verde/rojo, leyenda y título "Red butterfly Arikan — código Polar N=4, k=2, tasa 1/2".

Tras editar, validar que el JSON del notebook es parseable: `python3 -c "import json; json.load(open('lab.ipynb'))"`. Luego ejecutar `mkdocs build --strict` desde la raíz del proyecto donde está mkdocs.yml para confirmar que el build pasa con la nueva figura referenciada.
  </action>
  <verify>
    <automated>python3 -c "import json; nb=json.load(open('lab.ipynb')); assert any('polar-butterfly-n4.png' in ''.join(c['source']) for c in nb['cells'] if c['cell_type']=='code'), 'celda N4 ausente'; print('NB OK')"</automated>
  </verify>
  <done>lab.ipynb es JSON válido, contiene la celda generadora de polar-butterfly-n4.png tras cell 15, y `mkdocs build --strict` pasa.</done>
</task>

</tasks>

<verification>
- `grep "polar-butterfly-n4.png" index.md` devuelve la referencia dentro del admonition §4.1
- `python3 -c "import json; json.load(open('lab.ipynb'))"` no lanza error
- La celda N=4 existe en lab.ipynb después de cell 15
- `mkdocs build --strict` termina con código 0
</verification>

<success_criteria>
- La figura polar-butterfly-n4.png aparece al inicio del ejemplo §4.1, antes de "**Escenario.**", correctamente indentada dentro del admonition.
- lab.ipynb contiene la celda generadora verbatim, JSON válido.
- mkdocs build --strict pasa sin errores ni warnings de figura faltante.
</success_criteria>

<output>
Create `.planning/quick/260606-ocz-add-polar-butterfly-n4-png-to-the-encodi/260606-ocz-SUMMARY.md` when done
</output>
