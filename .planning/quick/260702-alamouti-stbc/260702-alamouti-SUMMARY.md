---
slug: alamouti-stbc
status: complete
created: 2026-07-02
completed: 2026-07-02
commit: 62cd8e9
---

# Summary — Alamouti concreto (STBC)

## Hecho
Alamouti pasa de nombrado a mostrado en `docs/sessions/06-mimo-systems/index.md`:
1. **§4 DMT**, caja `??? example` tras los vértices extremos: esquema 2×1,
   tabla de dos ranuras (s1/s2, -s2*/s1*), señales recibidas, combinador
   lineal, resultado s_hat = (|h1|^2+|h2|^2)s → diversidad orden 2, tasa 1,
   sin CSIT. Enlaza con V-BLAST del §3.3 como vértice opuesto.
2. **Ejercicios de Asimilación A5**: Alamouti a mano con h1=1, h2=j →
   combinador recupera 2·s1, con solución paso a paso.

## Verificación
- álgebra del combinador verificada: términos cruzados en s2 se cancelan,
  -j^2 duplica s1 → 2·s1 ✓
- mkdocs build --strict: pasa (solo INFO CLAUDE.md fuera de nav)

## Commits
- 62cd8e9 — feat(06-mimo): Alamouti §4 + Ejercicio A5
- (artifacts) — docs(quick-260702-alamouti): plan + summary
