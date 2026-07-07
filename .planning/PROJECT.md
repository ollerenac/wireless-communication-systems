# Sistemas de Comunicaciones Inalambricas

## What This Is

Open-access master's course materials for wireless communication systems, from physical-layer fundamentals through 5G/6G topics. The current workstream is instructional preparation and clarity improvement for Session 06 MIMO so the instructor can teach the material fluently.

## Core Value

Help the instructor understand and teach MIMO concepts clearly, with mathematically correct Spanish course notes, labs, figures, and lecture guidance.

## Requirements

### Validated

- [x] Published course site remains the primary delivery format for students.
- [x] Session 06 MIMO content includes expanded treatment of receiver detection, Alamouti STBC, CSI acquisition, SVD/water-filling, and detector BER comparisons.
- [x] Figure and notebook updates are verified before publication; notebook cells for targeted figures are executed via extracted scripts rather than full `nbconvert --execute`.
- [x] Session 06 MIMO lesson is refocused around implementation and network-design decisions: antenna strategy, CSI, rank, precoding, user separation, Massive MIMO and deployment constraints.
- [x] Session 06 MIMO lesson includes three reproducible implementation-oriented figures for network symptom mapping, rank/precoder selection, and CSI overhead scaling.

### Active

- [ ] Continue the Session 06 MIMO study loop: answer conceptual questions, improve `index.md` or the lecture-script artifact when clarity gaps appear, and keep focus on lecture readiness.
- [ ] Deep-review Session 06 sections 4-6 when the user asks for more clarity in those parts.
- [ ] Optionally update `lab.ipynb` to add an explicit scenario-driven rank/precoder selector matching the new lesson framing.

### Out of Scope

- Parcial 01 email distribution — deferred until the instructor provides student email addresses and explicitly resumes the admin task.
- Session 07 5G NR content — deferred during the active MIMO study loop.
- Committing a persistent `guion-clase.md` — deferred until the user asks; current lecture script lives as an external artifact.
- Running broad understanding/indexing over the repository root — avoid scanning `exams/**` because it can contain PII.

## Context

- Current active mode: preparation for teaching Session 06 MIMO.
- Latest recovered handoff: `.planning/HANDOFF.json` and `.continue-here.md`, dated 2026-07-04 after the 2026-07-03 study session.
- Lecture-script artifact URL: https://claude.ai/code/artifact/05541ca0-6518-40aa-8f2c-a9f5a4de6a87
- The source HTML for the lecture-script artifact was in an ephemeral scratchpad. In a fresh session, fetch the artifact URL before redeploying with the same URL if iteration is needed.
- Current repo divergence from handoff: `docs/sessions/06-mimo-systems/figures/svd-based-mimo/` is untracked and contains NPTEL water-filling source screenshots plus transcript.

## Constraints

- **Focus**: During this study loop, do not offer Parcial 01 emails, Session 07, or `guion-clase.md` unless the user asks.
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
| Reframe Session 06 from theory-first capacity/SVD toward deployment/design decisions. | The user clarified that the course audience is more implementation-oriented and needs to know when to use each antenna arrangement in real networks. | Good |
| Generate new implementation figures with deterministic Matplotlib scripts instead of image generation. | The diagrams need exact Spanish labels, stable layout, and reproducible updates for course maintenance. | Good |

---
*Last updated: 2026-07-07 after adding reproducible implementation figures to Session 06 MIMO.*
