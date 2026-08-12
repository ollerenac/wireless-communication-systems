---
gsd_state_version: '1.0'
status: paused
progress:
  total_phases: 0
  completed_phases: 0
  total_plans: 0
  completed_plans: 0
  percent: 0
---

# Project State

## Project Reference

See: .planning/PROJECT.md (updated 2026-07-07)

**Core value:** Help the instructor understand and teach MIMO concepts clearly, with mathematically correct Spanish course notes, labs, figures, and lecture guidance.
**Current focus:** Session 07 network design — 4G/5G architecture + design criteria over a Sionna RT ray-traced Lima scene.

## Current Position

Phase: N/A of N/A (quick-task study workflow, no active milestone roadmap)
Plan: N/A of N/A
Status: Session 07 lab backbone complete (commit `f986354`); index.md for the session not yet written
Last activity: 2026-08-01 — Built and validated the full Sionna RT pipeline (Blender+Blosm OSM → Mitsuba scene → 8-part design notebook over San Isidro, Lima) with consolidated coverage/SINR/throughput/handover/densification/MIMO analyses.

Progress: [░░░░░░░░░░] 0%

## Performance Metrics

**Velocity:**
- Total plans completed: 11 quick plans recovered from `.planning/quick/`
- Average duration: Not tracked
- Total execution time: Not tracked

**By Phase:**

| Phase | Plans | Total | Avg/Plan |
|-------|-------|-------|----------|
| Quick Session 06 MIMO improvements | 11 | 11 | Not tracked |

**Recent Trend:**
- Last 5 plans: `260702-precoder-zf`, `260702-marchenko-pastur`, `260703-svd-wf-example`, `260703-s3-digest`, plus pause commit
- Trend: Stable

*Updated after each plan completion*

## Accumulated Context

### Decisions

Decisions are logged in PROJECT.md Key Decisions table.
Recent decisions affecting current work:

- Voz editorial (2026-08-06): **tuteo** (segunda persona) es la voz oficial de todo el material del curso — lecciones, guías y notas. Decisión no retroactiva: lo ya escrito no se toca. La forma impersonal queda descartada como estándar.
- Registro léxico (2026-08-11): **"cálculo"**, nunca "cuenta" (no natural en español peruano); **"la publicidad"**, nunca "folleto". Barrido retroactivo aplicado a Sesión 07 (lección, notebook, guion). Regla didáctica: ningún símbolo entra a una fórmula sin nombrarse en palabras en su primer uso; glosario de siglas como respaldo.
- Registro léxico (2026-08-11b): **"perilla" prohibida** (anglicismo de *knob*, nadie la usa). Usar **"variable"** para `ESCENA` (lo que el alumno cambia) y **"parámetro"** para ajustes de diseño (tilt, azimut). Barrido aplicado a lección, guía y ambos notebooks.
- Sin fórmulas inventadas (2026-08-12): todo número/fórmula de la lección es (a) matemática verificable, (b) referencia publicada verificada por web (citada: NGMN 5G White Paper "50 Mbps everywhere"; ITU-R M.2410 user experienced data rate = p5, 100/50 Mbps urbano denso), o (c) **decisión del diseñador declarada como tal**. Síntesis propia con aura de fórmula = prohibida.
- R4 se ADOPTA, no se deriva (2026-08-12): toda derivación de throughput de borde desde la demanda es inválida por (i) circularidad — necesita el despliegue real, que es resultado de Fases 2-4 — y (ii) incoherencia de verificación — el mapa F6 es mono-usuario, un requisito "bajo carga" no es lo que se mide. Planteamiento vigente: piso = servicio prometido (Tabla 0.3) → referencia de la industria (NGMN 50 / ITU-R 100) → adopción declarada. UL = columna UL de Tabla 0.3 sobre servicios prometidos. R5 gobierna la carga (sí derivable); R4 la calidad por usuario. Dos intentos de fórmula (N_borde, processor sharing) fueron removidos por esto.
- Registro léxico (2026-08-12b): **"ancla" prohibida** → **"referencia de la industria"**. **"promesa/prometer" prohibidos** → **"oferta (comercial)"/"ofrecer"**. **"piso" prohibido** → **"mínimo técnico"** (lenguaje real de planificación, no de blog).
- Títulos (2026-08-12): serios y directos, sin coletillas coloquiales ("qué te da y qué te quita", "De promesas a números" = prohibidos). Patrón: sustantivo + complemento técnico ("Requisitos del proyecto", "Análisis del espectro licenciado"). Aplica a lección y exámenes; los títulos de Fases 1-6 de la lección aún tienen coletillas — barrer al tocar cada fase.
- Registro léxico (2026-08-12): **"encargo" prohibido** (nadie lo usa en planificación de redes). Usar **"el proyecto"** en prosa general y **"términos de referencia (TdR)"** para el documento con las cláusulas. Barrido aplicado a lección, design.ipynb y ambos notebooks de examen.
- Tablas numeradas (2026-08-11): toda tabla de la lección S07 lleva **`Tabla <fase>.<n> — descripción`** en negrita antes de la tabla. Se aplica fase por fase conforme se modifican (Fase 0: 0.1 RSRP, 0.2 SINR, 0.3 servicios, 0.4 R_usuario hora cargada, 0.5 requisitos). El examen referencia tablas por número como pista ("verifica la Tabla 0.2").

- Session 07: scope agreed in conversation (no formal AskUserQuestion round): 4G architecture as stepping stone → 5G evolution → procedures that a designer configures → design parameters for a small network. Sionna RT is the lab vehicle.
- Session 07: Sionna framed as *evaluator, not planner* — students propose sites/tilt/power, the ray tracer shows consequences. This is the pedagogical core.
- Session 07: OSM/Blosm scene (shareable, ITU materials) chosen over Google 3D Tiles (no material semantics, license forbids redistribution).
- Session 07: exploration runs at 10^5 rays / reporting runs at 10^6 with diffuse reflection — "se explora barato, se reporta caro" is itself a lesson.
- Env: `ran-design` conda env (python 3.12, sionna 2.0.1); `LD_LIBRARY_PATH=$CONDA_PREFIX/lib` persisted via `conda env config vars set` to fix system-libstdc++ conflict (CXXABI_1.3.15). Non-interactive shells still need manual export.
- Sionna 2.x API differences vs 0.x tutorials: `PathSolver`/`RadioMapSolver` replace `compute_paths`/`coverage_map`; `paths.cir()` → numpy gets a leading [real, imag] axis; `mi.Point3f` rejects `np.float64` (cast to `float`); headless `render_to_file` needs an explicit `Camera`.

- Session 06: Keep the 2x2 SVD example as the construction anchor; use the 3x3 example for water-filling.
- Session 06: Keep the active focus on MIMO teaching readiness; admin and future-session work are deferred until explicitly requested.
- Lab 06: `precoder_zf` and Marchenko-Pastur exercises were converted from student TODOs to instructor reference solutions.
- Session 06: New requested direction is implementation-first. The next rewrite should start from deployment decisions such as coverage, throughput, interference, density, CSI overhead, rank selection, and precoder choice.
- Session 06: Implementation-first rewrite completed in commit `6d1e0d3`; next optional content step is aligning `lab.ipynb` with a scenario-driven rank/precoder selector.
- Session 06: Three deterministic Matplotlib figures now support the implementation-first framing: network symptom to MIMO strategy, rank/precoder decision flow, and CSI overhead scaling.
- Session 06: Instructor-facing HTML artifact now provides narrative dictation notes, teaching transitions, figure explanations, student questions and common pitfalls.

### Pending Todos

- **Session 07 next:** write `docs/sessions/07-network-design/index.md` wrapping the 8 notebook parts with the 4G/5G architecture + procedures theory (skeleton agreed: why architecture → minimal EPC → 5G evolution/NSA-SA → designer-facing procedures → small-network parameters → integrative case).
- Session 07: sectorization step — 3×`tr38901` sectors with azimuth/tilt per BS (replaces the iso-element simplification in Part 2).
- Session 07: decide final scene (current San Isidro test scene vs another Lima district / campus); fix OSM building heights by hand for key buildings in Blender if needed.
- Session 07: `altura_en(x, y)` helper (vertical ray cast) so students can snap BS to rooftops.
- Session 07: triage `catalogo_ejercicios.md` and `clase2_ej23_rediseno.ipynb` (instructor drafts committed as-is, not yet integrated).
- Session 06 (dormant): study loop open for further questions; understand-anything graph incremental update pending.
- Deferred admin: distribute Parcial 01 feedback after the instructor provides student email addresses.
- Long-term backlog: Session 05 Polar BER N=64 Monte Carlo exercises 5-6; Session 03 OFDM+LDPC integrator.

### Blockers/Concerns

- Student email addresses are needed before Parcial 01 feedback can be sent.
- The lecture-script source HTML was ephemeral; fetch the artifact URL before editing/redeploying the existing artifact.
- `docs/sessions/06-mimo-systems/figures/svd-based-mimo/` is kept as local-only recovered source material and is intentionally ignored.

### Quick Tasks Completed

| # | Description | Date | Commit | Directory |
|---|-------------|------|--------|-----------|
| 260707-3ok | Analizar reenfoque implementativo de docs/sessions/06-mimo-systems/index.md | 2026-07-07 | n/a-analysis-only | [260707-3ok-analizar-reenfoque-implementativo-de-doc](./quick/260707-3ok-analizar-reenfoque-implementativo-de-doc/) |
| 260707-3v6 | Reescribir Sesion 06 MIMO con enfoque implementativo y decisiones de red | 2026-07-07 | 6d1e0d3 | [260707-3v6-reescribir-sesion-06-mimo-con-enfoque-im](./quick/260707-3v6-reescribir-sesion-06-mimo-con-enfoque-im/) |
| 260707-4b5 | Agregar figuras implementativas a Sesion 06 MIMO | 2026-07-07 | df85cbf | [260707-4b5-agregar-figuras-implementativas-a-sesion](./quick/260707-4b5-agregar-figuras-implementativas-a-sesion/) |
| 260707-53z | Crear artifact narrativo para dictar Tema 06 MIMO usando contexto understand-anything | 2026-07-07 | 92e6ee1 | [260707-53z-crear-artifact-narrativo-para-dictar-tem](./quick/260707-53z-crear-artifact-narrativo-para-dictar-tem/) |
| 260714-8kp | Verificar suficiencia de notas de dictado y agregar 7 guias de pizarra | 2026-07-14 | 21e4678 | [260714-8kp-pizarras-notas-dictado](./quick/260714-8kp-pizarras-notas-dictado/) |

## Deferred Items

| Category | Item | Status | Deferred At |
|----------|------|--------|-------------|
| Admin | Parcial 01 feedback emails | Waiting for student email addresses | 2026-07-04 handoff |
| Course content | Session 07 Arquitectura 5G NR | Deferred by active study-mode focus | 2026-07-04 handoff |
| Documentation | Persistent `guion-clase.md` | Deferred until requested | 2026-07-04 handoff |

## Session Continuity

Last session: 2026-08-11 (pausa via gsd-pause-work, contexto al limite)
Stopped at: Sesion 07 dictable de punta a punta (Fases 0-6). Hoy ademas: ronda didactica completa (desplegables, glosario, simbolos nombrados), registro lexico aplicado, sistema de mapas Colab (perilla ESCENA, zips en el sitio, sin git clone), mapa san-isidro-01 publicado (Z-up verificado). Todo pusheado (7fc0cb7).
Pendiente: cierre de la leccion, 4 figuras SVG, smoke test Colab (usuario), opcional parametrizar Fases 4-6 para mapas nuevos.
Resume file: `.planning/HANDOFF.json` + `.planning/.continue-here.md`

### Previous session continuity (2026-08-01)

Last session: 2026-08-01
Stopped at: Session 07 lab backbone committed (`f986354`). Full pipeline validated: Blender 4.2 LTS + Blosm (OSM, San Isidro ~1.3×0.8 km) + mitsuba-blender → `blends/test_scene/untitled.xml` (materials renamed to `itu_concrete`/`itu_metal` via sed) → `test_scene.ipynb` with 8 executed parts and all figures. Key numbers: 71.2% baseline coverage (3 BS, SINR>0 dB), 592/159 Mbps median/edge, LTE-vs-5G deficit 3.4 pts, 8→1 handovers with A3, densification 3→6 sites = 71→92% (95% target unreachable → repositioning lesson), MIMO κ>30 dB almost everywhere, delay spread 60 ns.
On resume: next deliverable is Session 07 `index.md` (theory wrap); check unpushed commits (`git log origin/main..HEAD` — several pending at pause time, user asked for commits only, push not requested).
Resume file: none
