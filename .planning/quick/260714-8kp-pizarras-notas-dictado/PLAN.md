---
task: Verificar suficiencia de notas de dictado MIMO y reforzar soporte de pizarra
slug: pizarras-notas-dictado
date: 2026-07-14
type: quick
status: complete
---

# Quick 260714-8kp — Pizarras en notas de dictado Sesión 06

## Pedido

Releer `docs/sessions/06-mimo-systems/index.md` completo, verificar si
`artifact-notas-dictado-mimo.html` basta para narrar toda la clase con
whiteboard, y mejorar con guías de dibujo/pizarra donde falten.

## Diagnóstico

- Narrativa: suficiente. 7 bloques cubren §1–§7; scripts hablados por bloque;
  11/12 figuras de la lección referenciadas (falta solo marchenko-pastur,
  que es de laboratorio).
- Pizarra: débil. 1 sola caja "Pizarra recomendada" (bloque 3) y sin pasos.
  La lección tiene 5 momentos de álgebra pensados para pizarra que el
  artifact no explota.

## Tareas

1. Bloque 2: pizarra fases alineadas (beamforming) vs al azar + SU/MU sketch;
   incluir "capas al mismo tiempo y misma banda" (nota de espectro de §2).
2. Bloque 3: expandir pizarra existente con pasos del ejemplo 2×2 de §3.1
   (v1/v2, σ², chequeo Frobenius); añadir frase H[k] por subportadora.
3. Bloque 4: pizarra Alamouti en 4 líneas + pizarra DMT (vértices 2×2).
4. Bloque 5: pizarra ZF ×2.22 (inversa en vivo) + ecuación downlink con
   término de interferencia subrayado.
5. Bloque 6: pizarra water-filling como recipiente (números del material).
6. Bloque 7: pizarra contaminación de pilotos en 2 celdas + contraste FDD/TDD.
7. `mkdocs build --strict`, commit, push, verificar origin sync.
