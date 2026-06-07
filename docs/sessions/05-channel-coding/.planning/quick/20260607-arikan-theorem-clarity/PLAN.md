---
slug: arikan-theorem-clarity
date: 2026-06-07
status: in-progress
---

# Quick Task: Mejorar legibilidad del teorema de polarización de Arıkan

## Goal

Mejorar la legibilidad del párrafo del teorema de Arıkan (index.md ~líneas 403-407):
- Añadir oración de setup antes de la fórmula
- Agregar `\overbrace` con etiqueta "nº de canales con Z≈0" sobre el numerador
- Reformular conclusión: los códigos Polar **alcanzan** (no se aproximan a) C(W)

## File to change

- `index.md` líneas 403-407

## Acceptance

- mkdocs build --strict pasa sin errores
- El párrafo mejorado está commitado
