---
task: Analizar duplicación entre ejemplos 2×2 (§3.1) y 3×3 (§3.2) y hacer §3 más digerible
date: 2026-07-03
mode: quick-inline
---

# Plan

## Análisis (entregado en chat)
Duplicación real: ambos ejemplos enseñaban "construir SVD por atajo" + chequeo Frobenius + canales desacoplados. Único aporte nuevo del 3×3: water-filling numérico.

## Decisión: división de trabajo, NO reemplazo
Reemplazar §3.1 por el 3×3 (pedido literal del usuario) rompería 5 referencias cruzadas: §3.3 (ZF ×2,22 reusa la H 2×2), párrafo water-filling (σ₂²=0,25 candidato a secarse), Introducción, Ejercicio A2, momento pizarra del guión. Además el 3×3 no cabe en pizarra y su V=permutación no tiene historia física. Justificación entregada al usuario.

## Tareas
1. Recortar caja 3×3 ~40%: título sin "SVD y"; primera línea declara división de trabajo; "La SVD, en una línea" (columnas ortogonales → normas = σ, Frobenius como paréntesis de una línea); eliminar paso de canales desacoplados (ec. 5 ya lo cubre); conservar íntegros water-filling numérico + capacidad + nota de notación.
2. Mapa de la sección al final de la intro de §3: tres movimientos, un ejemplo por herramienta (§3.1 construir/física, §3.2 repartir potencia, §3.3 receptor solo).
3. Build strict, commit, espejo en Artifact.
