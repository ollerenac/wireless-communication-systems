---
phase: quick-260701-mhk
plan: 01
type: execute
wave: 1
depends_on: []
files_modified:
  - docs/sessions/06-mimo-systems/index.md
autonomous: true
requirements:
  - MEJORA-EXPLICABILIDAD
  - MEJORA-NARRATIVA
  - EJERCICIOS-ASIMILACION
must_haves:
  truths:
    - "Cada sección de teoría (§1–§6) abre con intuición/analogía antes del álgebra"
    - "§3 SVD incluye un ejemplo numérico 2×2 resuelto a mano y verificable"
    - "El instructor puede seguir un arco intuición → ejemplo → formalismo en cada sección"
    - "Existen ejercicios de asimilación FÁCILES con solución colapsable"
    - "mkdocs build --strict pasa limpio"
  artifacts:
    - docs/sessions/06-mimo-systems/index.md
  key_links:
    - "Las 8 figuras existentes (figures/*.png) siguen referenciadas sin regenerarse"
    - "Ecuaciones \\tag{N} existentes conservan su numeración o se renumeran de forma consistente"
---

<objective>
Hacer la Sesión 06 (MIMO) enseñable. El instructor mismo la encuentra difícil de digerir y de impartir. La lección es correcta en contenido pero salta directo al formalismo (SVD eq.4, límites DMT) sin rampa de intuición, sin números concretos, y sin ejercicios fáciles de asimilación.

Este plan reescribe `index.md` para explicabilidad y secuencia narrativa (intuición → ejemplo → formalismo por sección, con analogías concretas y UN ejemplo numérico 2×2 resuelto a mano), y añade un set de ejercicios de asimilación FÁCILES (concept-checks inline + drills 2×2 calculables a mano con solución).

Purpose: que el profesor entienda y explique la clase; que los alumnos asimilen los conceptos antes de la matemática pesada.
Output: `index.md` mejorado, mismas figuras, `mkdocs build --strict` limpio.
</objective>

<execution_context>
@$HOME/.claude/gsd-core/workflows/execute-plan.md
</execution_context>

<context>
@docs/sessions/06-mimo-systems/index.md
@docs/sessions/06-mimo-systems/lab.ipynb
@docs/sessions/05-channel-coding/index.md
</context>

<constraints>
- Idioma español; términos técnicos en inglés en cursiva (*fading*, *beamforming*, *water-filling*, *channel hardening*).
- NO regenerar figuras. Reutilizar los 8 PNG existentes en `figures/`. No se ejecuta el notebook. Los comentarios HTML `<!-- generada por celda N -->` de cada figura se conservan.
- Conservar TODO el contenido técnico correcto: ecuaciones (1)–(16), tablas, figuras. Se AÑADE andamiaje; no se borra rigor. Si se renumeran ecuaciones al insertar el ejemplo 2×2, renumerar de forma consistente en todo el archivo (incluyendo el §Resumen).
- Estilo casa: `<figure markdown="span">` para figuras, `\tag{N}` para ecuaciones, admonitions colapsables `??? example "..."` / `??? question "..."` para ejemplos y soluciones (ver sesión 05 líneas 193, 459, 627).
- `mkdocs build --strict` DEBE pasar limpio tras los cambios.
- No tocar `lab.ipynb`. Los TODO del notebook (`precoder_zf`, histograma Marchenko-Pastur) son los ejercicios computacionales "pesados" y quedan como están; los ejercicios FÁCILES viven en `index.md`.
</constraints>

<tasks>

<task type="auto">
  <name>Task 1: Añadir andamiaje de intuición, analogías y ejemplo numérico 2×2 a la teoría</name>
  <files>docs/sessions/06-mimo-systems/index.md</files>
  <action>
Reescribir las seis secciones de teoría siguiendo el arco **intuición → ejemplo → formalismo**. NO borrar ecuaciones ni figuras; INSERTAR párrafos de intuición ANTES del álgebra en cada sección. Analogías concretas obligatorias (una por sección, en prosa, no en admonition):

- §1 (De SISO a MIMO): analogía del **carril de autopista**. Multiplexación = enviar carga distinta por cada carril (más throughput). Diversidad = enviar la misma carga por todos los carriles como seguro (más fiabilidad). Esta analogía debe preceder a la lista diversidad/multiplexación existente.
- §2 (Modelo matricial): antes de la ec.(1), una frase de intuición: "cada antena receptora oye una mezcla ponderada de lo que enviaron TODAS las antenas transmisoras; la matriz H es la tabla de esas ponderaciones". Conectar $h_{ji}$ a "cuánto de la antena TX $i$ llega a la RX $j$".
- §3 (SVD): analogía de la **mesa de mezclas / ejes naturales del canal**. La SVD encuentra las rotaciones de entrada (V) y salida (U) que convierten un canal enredado (las antenas se interfieren) en faders independientes (subcanales que no se mezclan). Insertar esta intuición ANTES de la ec.(3). Tras la ec.(5), una frase que aterrice: "hemos convertido un problema matricial en $r$ problemas escalares que ya sabemos resolver desde la Sesión 02". Para *water-filling* (tras ec.(6)): analogía de **verter agua en un recipiente de fondo irregular** — los pozos profundos (subcanales fuertes, $N_0/\sigma_k^2$ pequeño) reciben más agua (potencia); los pozos poco profundos pueden quedar secos ($P_k^*=0$).
- §4 (DMT): analogía **seguro vs velocidad** — no se pueden maximizar ambos a la vez. Antes de las definiciones de límite (ec. ganancia mux/div), una frase intuitiva de qué significa cada ganancia sin el $\lim$.
- §5 (MRT/ZF): intuición antes del álgebra. MRT = "apuntar el haz a cada usuario ignorando a los demás" (egoísta, simple). ZF = "elegir haces que caen en los ceros de los demás usuarios" (cooperativo, cancela interferencia pero amplifica ruido). Insertar antes de la ec.(11).
- §6 (Massive MIMO): analogía de la **ley de los grandes números**. *Channel hardening* = promediar muchos dados: la suma se concentra, el *fading* deja de fluctuar. *Favorable propagation* = en un espacio de dimensión alta, dos vectores aleatorios son casi ortogonales (los usuarios dejan de estorbarse solos). Insertar antes de la ec.(14).

**Ejemplo numérico 2×2 (el ancla central)**: añadir una subsección `#### 3.1 Un ejemplo concreto 2×2` al inicio de §3, ANTES de la ec.(3) general, dentro de un `??? example "Ejemplo numérico: SVD y capacidad de un canal 2×2"` colapsable. Usar EXACTAMENTE este canal simétrico calculable a mano:

  H = [[1, 0.5], [0.5, 1]]

Como H es real y simétrica, la SVD coincide con la descomposición espectral. Mostrar paso a paso:
- Valores singulares: σ₁ = 1.5, σ₂ = 0.5 (autovalores de H). Ganancias de subcanal σ₁² = 2.25, σ₂² = 0.25.
- Vectores singulares (columnas de V = U): v₁ = [1, 1]/√2 (dirección +45°), v₂ = [1, −1]/√2 (dirección −45°). Interpretar: "el canal favorece la señal enviada en fase por ambas antenas (v₁) y penaliza la señal en contrafase (v₂)".
- Verificar ‖H‖_F² = 1²+0.5²+0.5²+1² = 2.5 = σ₁²+σ₂² = 2.25+0.25 ✓ (conecta con la Tarea del Ejercicio 1 del lab).
- Capacidad a SNR = 10 dB (= 10 lineal), potencia uniforme P/Nt con Nt=2, usando la ec.(7): C = log₂(1 + (10/2)·2.25) + log₂(1 + (10/2)·0.25) = log₂(12.25) + log₂(2.25) ≈ 3.61 + 1.17 = 4.78 bit/s/Hz.
- Comparar con SISO al mismo SNR: log₂(1+10) = 3.46 bit/s/Hz. Conclusión aterrizada: "dos antenas por lado dan 4.78 vs 3.46 — la ganancia MIMO en números que puedes verificar a mano".

El ejemplo 2×2 debe referenciar hacia la Figura 3 (subcanales paralelos) para que el alumno vea el diagrama abstracto instanciado en números.

**Transiciones narrativas**: al final de cada sección añadir una frase-puente de una línea que motive la siguiente (patrón de la sesión 05, "La pregunta natural es: ..."). Concretamente: §3→§4 "ya sabemos la capacidad máxima; ¿qué pasa si en vez de maximizar tasa queremos fiabilidad? → DMT". §4→§5 "hasta aquí un solo enlace punto a punto; ¿y si la BS sirve a varios usuarios a la vez? → precodificación". §5→§6 "MRT era simple pero interferente; ¿cuándo deja de importar la interferencia? → cuando M≫K".

NO usar bloques de código con fences (```) — solo prosa, ecuaciones LaTeX y admonitions.
  </action>
  <verify>
    <automated>cd /home/researcher/Teaching/uni/2026/wireless-communication-systems && grep -c "carril\|mesa de mezclas\|agua\|dados\|seguro" docs/sessions/06-mimo-systems/index.md</automated>
  </verify>
  <done>Cada sección §1–§6 tiene un párrafo de intuición con analogía concreta antes de su álgebra. §3 contiene el ejemplo 2×2 con H=[[1,0.5],[0.5,1]], σ={1.5,0.5}, capacidad 4.78 bit/s/Hz, en un `??? example` colapsable. Existen frases-puente entre secciones. Ninguna ecuación ni figura existente fue borrada; renumeración consistente si se insertaron ecuaciones.</done>
</task>

<task type="auto">
  <name>Task 2: Añadir ejercicios de asimilación fáciles (concept-checks inline + sección de drills 2×2)</name>
  <files>docs/sessions/06-mimo-systems/index.md</files>
  <action>
Añadir ejercicios FÁCILES de asimilación (no problemas de desafío). Dos ubicaciones, ambas en `index.md`:

**(A) Concept-checks inline** — al final de cada sección §1–§6, un admonition colapsable `??? question "Comprueba tu comprensión"` con 1–2 preguntas conceptuales de respuesta corta y su respuesta al final del mismo bloque. Ejemplos del nivel esperado (usar estos o equivalentes):
- §1: "¿Qué estrategia elegirías para un enlace de emergencia con SNR baja: diversidad o multiplexación? ¿Por qué?" (Resp: diversidad — la fiabilidad importa más que la tasa.)
- §2: "En un sistema 4×4, ¿cuántos números complejos tiene H?" (Resp: 16.)
- §3: "Si un valor singular σ_k es casi cero, ¿qué le pasa a ese subcanal?" (Resp: ganancia σ_k²≈0, water-filling no le asigna potencia, queda seco.)
- §4: "En la curva DMT de un 2×2, ¿qué diversidad d obtienes si exiges r=2 streams?" (Resp: d=(2−2)(2−2)=0.)
- §5: "¿Por qué ZF puede empeorar a MRT cuando la SNR es baja?" (Resp: ZF amplifica el ruido al invertir HH^H; a SNR baja el ruido domina la interferencia.)
- §6: "¿Por qué con M≫K basta MRT sin invertir matrices?" (Resp: favorable propagation → interferencia inter-usuario →0.)

**(B) Sección dedicada `## Ejercicios de Asimilación`** — insertar ENTRE `## Laboratorio` y `## Resumen`. Contiene 4 drills calculables a mano/papel, cada uno con enunciado + `??? example "Solución"` colapsable con los pasos numéricos. Todos con matrices 2×2 o vectores pequeños. Concretamente:

- **Drill 1 (SVD a mano)**: dado H=[[2, 0],[0, 1]], escribir σ₁, σ₂ y las ganancias de subcanal. (Sol: σ={2,1}, ganancias {4,1}, V=U=I porque ya es diagonal.)
- **Drill 2 (capacidad)**: para el canal del Drill 1 a SNR=10 dB con potencia uniforme (Nt=2), calcular la capacidad con la ec.(7). (Sol: log₂(1+5·4)+log₂(1+5·1)=log₂21+log₂6≈4.39+2.58=6.97 bit/s/Hz.)
- **Drill 3 (MRT)**: dado el canal de un solo usuario h=[1, j] (M=2), calcular el vector MRT normalizado w=h^H/‖h‖. (Sol: ‖h‖=√2, w=[1, −j]/√2; verificar potencia ‖w‖²=1.)
- **Drill 4 (ortogonalidad / favorable propagation)**: dados h₁=[1, 0] y h₂=[0, 1], calcular |h₁^H h₂|. Repetir con h₁=[1,1]/√2, h₂=[1,−1]/√2. (Sol: 0 en ambos → canales ortogonales, interferencia nula con MRT.)

Añadir una frase introductoria a la sección: "Estos ejercicios se resuelven con lápiz y papel en pocos minutos; su objetivo es afianzar la intuición antes de abrir el laboratorio computacional." Y una frase de cierre que remita al `lab.ipynb` para los ejercicios computacionales (SVD Monte Carlo, precoder_zf, Massive MIMO).

NO usar fences de código. Respuestas en prosa/LaTeX dentro de los admonitions.
  </action>
  <verify>
    <automated>cd /home/researcher/Teaching/uni/2026/wireless-communication-systems && grep -c "Comprueba tu comprensión\|## Ejercicios de Asimilación\|Solución" docs/sessions/06-mimo-systems/index.md</automated>
  </verify>
  <done>Cada sección §1–§6 termina con un `??? question "Comprueba tu comprensión"`. Existe la sección `## Ejercicios de Asimilación` entre Laboratorio y Resumen con 4 drills 2×2, cada uno con `??? example "Solución"` y pasos numéricos. Todos calculables a mano.</done>
</task>

<task type="auto">
  <name>Task 3: Verificar build estricto</name>
  <files>docs/sessions/06-mimo-systems/index.md</files>
  <action>
Ejecutar `mkdocs build --strict` desde la raíz del repo y corregir cualquier warning/error que introdujeron los cambios (referencias rotas, sintaxis de admonition, LaTeX mal cerrado, figuras faltantes). Verificar visualmente en el HTML generado que: (1) las 8 figuras siguen apareciendo, (2) los admonitions `???` colapsan, (3) las ecuaciones renderizadas no tienen `\tag` duplicados. NO regenerar figuras — si una figura falta es un error de referencia a corregir, no de generación.
  </action>
  <verify>
    <automated>cd /home/researcher/Teaching/uni/2026/wireless-communication-systems && mkdocs build --strict 2>&1 | tail -5</automated>
  </verify>
  <done>`mkdocs build --strict` termina sin warnings ni errores. Las 8 figuras existentes se referencian correctamente. No hay ecuaciones con `\tag{N}` duplicado.</done>
</task>

</tasks>

<verification>
- `mkdocs build --strict` pasa limpio (Task 3).
- Cada sección §1–§6 abre con intuición/analogía y cierra con concept-check.
- §3 tiene el ejemplo 2×2 resuelto (H=[[1,0.5],[0.5,1]], C≈4.78).
- Sección `## Ejercicios de Asimilación` presente con 4 drills + soluciones.
- Ninguna figura regenerada; los 8 PNG originales intactos (git status no muestra cambios en figures/).
</verification>

<success_criteria>
- El instructor puede leer cada sección de arriba a abajo siguiendo intuición → ejemplo → formalismo sin saltos abruptos al álgebra.
- Un alumno puede resolver los 4 drills con lápiz y papel y autoverificar con las soluciones.
- Contenido técnico original conservado (16 ecuaciones, 8 figuras, tablas).
- Build estricto limpio.
</success_criteria>

<output>
Modificar en sitio `docs/sessions/06-mimo-systems/index.md`. No crear SUMMARY (tarea quick).
</output>
