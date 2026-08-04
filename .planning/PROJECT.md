# Sistemas de Comunicaciones Inalambricas

## What This Is

Open-access master's course materials for wireless communication systems, from physical-layer fundamentals through 5G/6G topics. The current workstream is building Session 07 (network design: 4G/5G architecture, designer-facing procedures, and small-network design criteria) around a Sionna RT ray-traced scene of Lima; Session 06 MIMO is complete and in dormant study-loop mode.

## Core Value

Help the instructor understand and teach MIMO concepts clearly, with mathematically correct Spanish course notes, labs, figures, and lecture guidance.

## Requirements

### Validated

- [x] Published course site remains the primary delivery format for students.
- [x] Session 06 MIMO content includes expanded treatment of receiver detection, Alamouti STBC, CSI acquisition, SVD/water-filling, and detector BER comparisons.
- [x] Figure and notebook updates are verified before publication; notebook cells for targeted figures are executed via extracted scripts rather than full `nbconvert --execute`.
- [x] Session 06 MIMO lesson is refocused around implementation and network-design decisions: antenna strategy, CSI, rank, precoding, user separation, Massive MIMO and deployment constraints.
- [x] Session 06 MIMO lesson includes three reproducible implementation-oriented figures for network symptom mapping, rank/precoder selection, and CSI overhead scaling.
- [x] Session 06 MIMO now has a standalone instructor narrative artifact for dictating the implementation-first class.

### Active

- [ ] Session 07: write `index.md` — 4G architecture as stepping stone, 5G evolution (SBA, NSA/SA, slicing), procedures a designer configures (registration, RACH, paging/TA, handover A3), small-network design parameters — wrapping the 8-part `test_scene.ipynb` lab.
- [ ] Session 07: sectorize the lab (3×tr38901 + azimuth/tilt per BS) and add rooftop-snap helper.
- [ ] Session 07: settle the definitive Lima scene and building heights; package `blends/test_scene/` for students (OSM attribution "© OpenStreetMap contributors").
- [ ] Session 06 (dormant): answer study-loop questions when they return; optional `lab.ipynb` rank/precoder selector.

### Out of Scope

- Parcial 01 email distribution — deferred until the instructor provides student email addresses and explicitly resumes the admin task.
- Committing a persistent `guion-clase.md` — deferred until the user asks; current lecture script lives as an external artifact.
- Google 3D Tiles for the Sionna scene — rejected (no material semantics, redistribution forbidden by license).
- Running broad understanding/indexing over the repository root — avoid scanning `exams/**` because it can contain PII.

## Context

- Current active mode: preparation for teaching Session 06 MIMO.
- Latest recovered handoff: `.planning/HANDOFF.json` and `.continue-here.md`, dated 2026-07-04 after the 2026-07-03 study session.
- Lecture-script artifact URL: https://claude.ai/code/artifact/05541ca0-6518-40aa-8f2c-a9f5a4de6a87
- The source HTML for the lecture-script artifact was in an ephemeral scratchpad. In a fresh session, fetch the artifact URL before redeploying with the same URL if iteration is needed.
- Local-only recovered source material: `docs/sessions/06-mimo-systems/figures/svd-based-mimo/` contains NPTEL water-filling screenshots plus transcript and is intentionally ignored.

## Context (Session 07 tooling)

- Dictation-notes artifact (guion del instructor, grows phase by phase): https://claude.ai/code/artifact/98209b61-23d1-425e-837b-89bf180242a8 — source HTML lives in the session scratchpad (ephemeral): in a fresh session, WebFetch the URL and republish with `url:` to update without minting a new link. Currently covers Fase 0.

- Conda env `ran-design` (python 3.12, sionna 2.0.1, nbconvert). CRITICAL: `LD_LIBRARY_PATH=$CONDA_PREFIX/lib` required (persisted in env config; non-interactive shells must export manually) — otherwise `CXXABI_1.3.15 not found`.
- Scene pipeline: Blender 4.2 LTS (`~/blender-4.2.9-linux-x64/`) + Blosm (OSM import; tokens configured; Google 3D Tiles key deliberately empty) + mitsuba-blender add-on (needs mitsuba 3.5.0 → Blender ≤4.2, python 3.11; Blender 5.x incompatible).
- Material names in exported XML must be `itu_*` (e.g. `mat-itu_concrete`) or `load_scene` rejects them.
- Notebook execution: `python -m nbconvert --to notebook --execute --inplace test_scene.ipynb` inside the env.
- Sionna 2.x vs 0.x tutorials: `PathSolver`/`RadioMapSolver`/`paths.cir()`; no TensorFlow anywhere.

## Constraints

- **Focus**: Parcial 01 emails and `guion-clase.md` stay out of scope unless the user asks. Session 07 is now the active workstream.
- **Math notation**: Use `\mathbf`, never `\boldsymbol`.
- **Markdown headings**: Avoid complex LaTeX in headings because it affects rendered navigation.
- **Notebook execution**: Prefer executing cell 1 plus the target cell through an extracted script; avoid running heavy full-notebook Monte Carlo cells unnecessarily.
- **Verification**: Run `mkdocs build --strict` after content changes when dependencies are available.
- **Privacy**: Treat `exams/**/examen-parcial-soluciones/` as gitignored PII-bearing material.

## Key Decisions

| Decision | Rationale | Outcome |
|----------|-----------|---------|
| Keep the 2x2 SVD example in Section 3.1 instead of replacing it with the 3x3 water-filling example. | The 2x2 example anchors several cross-references and gives the clearest physical interpretation; the 3x3 example now serves water-filling only. | Good |
| Add receiver detection as Section 3.3 and number the detector BER plot as Figure 4b. | Avoids renumbering later sections and figures while closing a conceptual gap. | Good |
| Do not simulate SIC in Figure 4b. | SIC is better left as a natural student exercise; the caption positions it between MMSE and ML. | Good |
| Convert selected Lab 06 TODO exercises into instructor reference solutions. | They were the instructor's pending tasks and can be reversed by restoring `pass` and comments. | Good |
| Scope optional understand-anything work to `docs/sessions/06-mimo-systems/`, not the repository root. | Avoids scanning PII in `exams/**`. | Pending |
| Session 07 built on Sionna RT over an OSM/Blender scene of Lima instead of abstract link-budget spreadsheets. | Students see real street-level propagation; every design knob (site, power, tilt, frequency) has visible consequences. | Good |
| Sionna framed as evaluator, not planner — the design loop belongs to the student. | Matches the course goal: adopt design criteria, not run a tool. | Good |
| Two-tier simulation quality: explore at 10^5 rays, report at 10^6 + diffuse. | Iteration speed for students; comparable official numbers (34% vs 71% showed why mixing tiers misleads). | Good |
| Reframe Session 06 from theory-first capacity/SVD toward deployment/design decisions. | The user clarified that the course audience is more implementation-oriented and needs to know when to use each antenna arrangement in real networks. | Good |
| Generate new implementation figures with deterministic Matplotlib scripts instead of image generation. | The diagrams need exact Spanish labels, stable layout, and reproducible updates for course maintenance. | Good |
| Use `understand-anything` deterministically where possible, but do not fake a complete graph workflow when plugin-specific subagent roles are unavailable. | The full skill targets an interactive codebase knowledge graph; this task needed an instructor narrative artifact for Tema 06. | Good |

---
*Last updated: 2026-07-07 after adding the Session 06 instructor narrative artifact.*
