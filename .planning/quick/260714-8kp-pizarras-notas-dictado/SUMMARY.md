---
task: Verificar suficiencia de notas de dictado MIMO y reforzar soporte de pizarra
slug: pizarras-notas-dictado
date: 2026-07-14
type: quick
status: complete
---

# Summary — Quick 260714-8kp

## Veredicto de suficiencia

- **Narrativa: suficiente.** Los 7 bloques del artifact cubren §1–§7 de la
  lección; hay script hablado por bloque; 11/12 figuras de la lección
  referenciadas (falta solo `mimo-marchenko-pastur.png`, que es de laboratorio
  y no se dicta).
- **Pizarra: era débil.** Solo 1 caja de pizarra (bloque 3) y sin pasos
  concretos. La lección tiene 5 momentos de álgebra hechos para pizarra que
  el artifact no explotaba.

## Cambios en `artifact-notas-dictado-mimo.html`

7 cajas `<details>` de pizarra nuevas/expandidas + 1 frase:

1. **Bloque 2**: fases alineadas vs al azar (beamforming necesita CSI);
   sketch SU vs MU; punto de espectro "capas al mismo tiempo y misma banda".
2. **Bloque 3**: pizarra existente expandida a 4 pasos con el 2×2 de §3.1
   (v1/v2 por simetría, σ²=2.25/0.25, chequeo Frobenius 2.5=2.25+0.25);
   frase H[k] por subportadora (enlace a Sesión 03).
3. **Bloque 4**: Alamouti en 4 líneas (tabla 2 ranuras, combinador,
   cancelación, caso h1=1, h2=j → 2·s1); DMT a mano con vértices 2×2
   (0,4)-(1,1)-(2,0).
4. **Bloque 5**: ZF ×2.22 (inversa de H^H·H en vivo, reutiliza canal del
   bloque 3); ecuación downlink y_k con término de interferencia subrayado.
5. **Bloque 6**: water-filling como recipiente (escalones N0/σ², nivel μ,
   números 52/13/4 del material; escalón fuera del agua = bajar rank).
6. **Bloque 7**: contaminación de pilotos en 2 celdas (h_hat = h_A + h_B);
   contraste FDD ∝ M vs TDD ∝ K en dos flechas.

## Verificación

`mkdocs build --strict` limpio (0.87 s). Todos los números de pizarra
provienen de ejemplos ya verificados en `index.md` (§3.1, §5.1, water-filling
box, Alamouti box).

## Follow-up (mismo día, pedido en study loop)

Bloque 1 reescrito con protocolo de lectura para tabla/Figura 1:

- Script "recetario médico": síntoma → tratamiento → efecto secundario;
  la habilidad es el protocolo de columnas, no memorizar filas.
- Script "dos extremos": dictar a fondo solo borde de celda (falta energía)
  vs hotspot (falta separación); indoor como pregunta; Massive/FR2 como
  regímenes.
- Pizarra nueva: tabla "qué recurso escasea" (energía / separación /
  descorrelación / CSI / hardware) con pregunta guía "¿qué falta aquí?".
- Nota: la tabla es el índice de la clase (mapa fila → bloque 3/4/5/7).
- Figcaption: división de trabajo — figura en clase, tabla para casa.

Segundo follow-up (study loop, mismo día):

- Bloque 2, pizarra SU/MU expandida: flecha = flujo/capa (no antena),
  requisitos de cada modo, remate "la flecha es información, la antena
  es fierro".
- Bloque 1: P1/P2 enlazadas a filas 1-2 del mapa como verificación de
  los dos extremos.
- Bloque 3: definición de CSI + distinción CSIR/CSIT + "fresco" vs
  tiempo de coherencia + jerarquía de exigencia (Alamouti < beamforming
  < MU-MIMO), enlazada al bloque 7.
- index.md (commit 819da68): R2 de §1 reescrita sin referencia
  adelantada a ZF.
- Bloque 3, pizarra nueva "3+2+1" para la tabla de indicadores de §3.1:
  tres preguntas (capas / usuarios juntos / duración de la foto),
  números del 2×2 reutilizados (κ=3 calculado en vivo → gancho al
  ×2.22), metáfora análisis de laboratorio, filas como índice de
  bloques posteriores.
