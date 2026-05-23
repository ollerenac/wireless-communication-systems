# Project Retrospective — Sesión 03 OFDM

*A living document updated after each milestone. Lessons feed forward into future planning.*

---

## Milestone: v1.0 — Revisión y Finalización

**Shipped:** 2026-05-23
**Phases:** 4 | **Plans:** 14 | **Sessions:** ~6 (across multiple context windows)

### What Was Built

- `index.md` (1,357 lines): all math errors corrected, all figure references resolved, 8 §4 narrative transitions inserted, §7 Synthesis integrated with 5 cross-references, Introduction bridges Sesiones 01-02
- `lab.ipynb` (44 cells): clean end-to-end execution (exit 0, 17 code cells, 0 errors), exercise order aligned to §4.3→§4.4 narrative progression
- `mkdocs build --strict` passes from repo root; site is publication-ready

### What Worked

- **Audit-first approach (Phase 1)**: Running a zero-change diagnosis before touching anything prevented blind fixes and established a clear priority order (BLOCKER → MINOR). This prevented regressions.
- **Wave-based parallel execution**: Phases 2 and 4 used parallel git worktrees to run independent plans simultaneously — cut wall-clock time roughly in half for the wave.
- **GSD executor inline for Wave 2**: When context was running low, switching from worktree-based subagents to inline sequential execution for Plan 04-03 avoided context-loss risk with no quality degradation.
- **Professor-in-the-loop via AskUserQuestion**: Routing the two `human_needed` items (§4.6→§4.7 quality, exercise order) directly to the professor before closing produced correct decisions in the same session.
- **Template canónico (§4.5) as style anchor**: Having one pre-existing well-formed transition in the document gave the AI a concrete stylistic target for the 7 new transitions. No style drift.

### What Was Inefficient

- **Worktree cleanup after Wave 1**: `gsd-sdk worktree.cleanup-wave` blocked because worktrees were still locked by Claude processes. Manual unlock + merge + remove took ~10 extra steps. A post-task worktree unlock signal would help.
- **Quick task ran inline, not via planner**: The Ej2/Ej3 reorder was done directly in the main context (Python script + nbconvert) rather than spawning the planner pipeline, because context was at 78%. Result was fine but the task directory has a thin PLAN.md. Next time: `/gsd:quick` earlier, before context pressure.
- **VERIFICATION.md files not updated after professor approval**: The two `human_needed` items were resolved interactively but the VERIFICATION.md frontmatter still shows `human_needed`. The resolution was captured in handoff files only. A post-approval update step would produce cleaner artifact history.
- **feature-dev:code-reviewer lacks Write tool**: Reviewer subagent produced findings as inline text; parent had to write REVIEW.md manually. Known tool-set limitation; workaround worked fine but adds one step.

### Patterns Established

- **Audit-before-edit discipline**: Always run Phase 1 as zero-change; produces structured finding list that drives subsequent phase scoping
- **Ground truth is the notebook**: When index.md and lab.ipynb conflict, edit index.md — not the notebook. Established as a hard constraint at project init.
- **`mkdocs build --strict` as formal exit criterion**: Non-negotiable gate before milestone close; catches all rendering issues including math, admonitions, figure refs
- **Human approval captured in .continue-here.md**: Professor editorial decisions are ephemeral; record verbatim text + decision in the session handoff so they survive context compression

### Key Lessons

1. **Pre-edit audit pays for itself**: Phase 1 took ~20% of total time but eliminated all blind rework in Phases 2-3. For document editing projects, resist the temptation to start fixing immediately.
2. **Inline execution beats subagents under context pressure**: At 75-80% context, spawning a planner+executor chain risks the chain running in a degraded context. If the task is small and well-defined, do it inline.
3. **Worktree isolation is worth the setup cost for parallel plans**: Even with the manual cleanup overhead, Wave 1 parallel execution was faster than sequential would have been. The overhead scales sublinearly with number of plans.
4. **Editorial quality requires human in the loop**: Automated checks can verify structural patterns (question present, answer present) but not pedagogical effectiveness. Build in an explicit professor-review gate before declaring "publication-ready."
5. **Verification status should be updated when human resolves items**: If a `human_needed` item is resolved interactively, immediately update the VERIFICATION.md frontmatter in the same session — don't defer to a handoff note.

### Cost Observations

- Model: claude-sonnet-4-6 for primary execution; claude (code-reviewer agent) for Phase 4 code review
- Sessions: ~6 context windows (project spanned multiple days of intermittent work)
- Notable: Wave-based parallel execution provided ~2x throughput on independent plans; the GSD worktree mechanism handled merge coordination automatically in most cases

---

## Cross-Milestone Trends

### Process Evolution

| Milestone | Sessions | Phases | Key Change |
|-----------|----------|--------|------------|
| v1.0 | ~6 | 4 | First milestone; established audit-first pattern, ground-truth discipline, professor-review gate |

### Top Lessons (Verified Across Milestones)

1. Audit before edit — zero-change Phase 1 prevents regression and establishes clear priority
2. Ground truth constraint — designate one artifact as authoritative before editing; resolve conflicts by adjusting the other
