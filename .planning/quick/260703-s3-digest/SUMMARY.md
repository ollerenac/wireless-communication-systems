---
task: Analizar duplicación entre ejemplos 2×2 (§3.1) y 3×3 (§3.2) y hacer §3 más digerible
date: 2026-07-03
status: complete
commit: be793b5
---

# Summary

## Análisis entregado
Tabla de solape: construir-SVD-por-atajo, Frobenius y desacoplados estaban duplicados; lo único nuevo del 3×3 era el water-filling numérico.

## Decisión
No reemplazar §3.1 (pedido literal): romperia 5 referencias cruzadas (§3.3 ZF ×2,22, párrafo WF σ₂²=0,25, Introducción, A2, pizarra del guión) y perdería la única interpretación física buena (ejes en fase/contrafase). En su lugar: división de trabajo explícita.

## Cambios (be793b5)
- Caja 3×3 recortada ~40%: título "Ejemplo numérico: water-filling en un canal 3×3"; abre declarando su único trabajo; SVD comprimida a una línea (columnas ortogonales → normas = σ; Frobenius entre paréntesis); paso "canales desacoplados" eliminado (ec. 5 lo cubre); water-filling + capacidad + nota de notación intactos.
- Mapa de la sección añadido al final de la intro de §3: tres movimientos, un ejemplo por herramienta.
- Espejo en Artifact (beat 3×3 reescrito con "división de trabajo").
