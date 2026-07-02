---
slug: marchenko-pastur
status: complete
created: 2026-07-02
completed: 2026-07-02
commit: baf9508
---

# Summary — Ejercicio 1: Marchenko-Pastur resuelto

## Hecho
Celda 7 de lab.ipynb: bloque TODO reemplazado por solución de referencia:
- Histograma de autovalores lambda = sigma^2/Nr (2000 realizaciones 4×4)
  con overlay de la PDF Marchenko-Pastur analítica (beta=1, soporte [0,4]).
- Verificación Frobenius ||H||_F^2 = sum(sigma_k^2): 14.175320 = 14.175320 ✓
  (identidad del §3.1 de la teoría).
- figures/mimo-marchenko-pastur.png generado. Ajuste empírico-teórico
  excelente; cola finita-N visible más allá de lambda=4.

## Bugs evitados/corregidos del TODO original
1. Instruía guardar como mimo-svd-channels.png → habría pisado la Figura 3
   del index (diagrama SVD). Guardado como mimo-marchenko-pastur.png.
2. Print "expected mean" usaba fórmula dudosa (sqrt(pi/4)*2 ≈ 1.77; el valor
   correcto para MP beta=1 es 2·8/(3pi) ≈ 1.70). Eliminado, reemplazado por
   la verificación Frobenius que sí conecta con la teoría.
3. Divergencia 1/sqrt(lambda) de la PDF en 0 (beta=1): primer intento
   destruyó la escala y (densidad ~318 en 0). Fix: grid desde
   lambda_minus+0.02 + ylim(0, 1.4).

## Verificación
- JSON OK; mkdocs build --strict pasa
- Figura inspeccionada visualmente: histograma sigue curva MP

## Commits
- baf9508 — feat(06-mimo): Ejercicio 1 resuelto
- (artifacts) — docs(quick-260702-mp): plan + summary
