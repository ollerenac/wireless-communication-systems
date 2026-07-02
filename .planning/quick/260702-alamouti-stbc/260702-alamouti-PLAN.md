---
slug: alamouti-stbc
created: 2026-07-02
mode: quick-inline
---

# Quick Task — Alamouti concreto (STBC)

## Problema
Alamouti/STBC citado por nombre en el vértice DMT r=0 (§4) pero nunca
mostrado. Es el esquema de diversidad más fácil y hand-computable — el "hola
mundo" del space-time coding. Dejarlo solo nombrado priva al estudiante del
único esquema de diversidad reproducible a mano.

## Solución
1. **§4 DMT**: caja `??? example` tras los vértices extremos — esquema
   Alamouti 2×1, tabla de dos ranuras, combinador, resultado
   s_hat = (|h1|^2+|h2|^2)s → diversidad orden 2, tasa 1, sin CSIT.
2. **Ejercicios de Asimilación**: nuevo A5 (Alamouti a mano) con h1=1, h2=j
   → combinador recupera 2·s1, con solución.

## Verificación
- álgebra del combinador verificada (cross-terms se cancelan)
- mkdocs build --strict pasa
- \mathbf, no \boldsymbol

## Commits
1. feat(06-mimo): esquema Alamouti concreto en §4 DMT + Ejercicio A5
2. docs(quick-260702-alamouti): plan + summary
