# Phase 3: Mejora de Narrativa - Discussion Log

> **Audit trail only.** Do not use as input to planning, research, or execution agents.
> Decisions are captured in CONTEXT.md — this log preserves the alternatives considered.

**Date:** 2026-05-22
**Phase:** 3-Mejora de Narrativa
**Areas discussed:** Transiciones §4, Introducción (NARR-02), Referencias cruzadas §7 Síntesis (NARR-03), 4 PNGs modificados sin commitear

---

## Transiciones §4

### Estilo de frases de transición

| Option | Description | Selected |
|--------|-------------|----------|
| Patrón pregunta–respuesta | Igual que 4.5→4.6: nombra la limitación del bloque y anuncia el remedio. Narrativa rica, el alumno sigue la lógica causal. | ✓ |
| Frase de puente directa | Una oración factual al final del bloque: "Con los símbolos QAM listos, el siguiente paso es…" Concisa, menos dramática. | |
| Apertura del bloque siguiente | En lugar de cerrar el bloque, abrir el siguiente con contexto. | |

**User's choice:** Patrón pregunta-respuesta (igual que 4.5→4.6)
**Notes:** La transición 4.5→4.6 existente se usa como template canónico.

### Ubicación de las transiciones

| Option | Description | Selected |
|--------|-------------|----------|
| Al final del bloque que cierra | Donde está la transición 4.5→4.6 ya existente. | ✓ |
| Al inicio del bloque que abre | El nuevo bloque se presenta a sí mismo con su motivación. | |

**User's choice:** Al final del bloque que cierra

### Transición 4.6→4.7

| Option | Description | Selected |
|--------|-------------|----------|
| Puente desde la suposición de H conocida | "ZF y MMSE asumen que H[k] es conocido. En la práctica hay que estimarlo." | ✓ |
| Puente desde la limitación de FEC | Continuar el hilo de FEC → dependencia de estimación pobre. | |
| Claude decide | El agente elige el mejor puente. | |

**User's choice:** Puente desde la suposición de H conocida
**Notes:** §4.5 y §4.6 usan `h_channel` como si fuera conocido; §4.7 es donde se estima. La transición cierra esa suposición implícita.

### Cierre §4.8→§5

| Option | Description | Selected |
|--------|-------------|----------|
| Cierre de cadena + pregunta de rendimiento | "Con el demapper, la cadena completa está cerrada. ¿Qué tan bien funciona? La curva BER de §5." | ✓ |
| Solo cierre descriptivo | "El demapper completa la cadena transmisor–canal–receptor." | |

**User's choice:** Cierre de cadena + pregunta de rendimiento

### Coherencia de la cadena §4 (pregunta adicional)

**User's request:** ¿Los bloques de §4 forman una cadena completa donde se puede seguir el flujo bits→symbols→OFDM→canal→receptor→bits? Actualmente no — los snippets trabajan en bloques aislados con variables inconsistentes (X vs X_tx, ausencia de y_noisy en §4.4).

| Option | Description | Selected |
|--------|-------------|----------|
| Bloque de cierre §4 | Un snippet al final de §4 que demuestra la cadena completa con variables consistentes. No toca los bloques existentes. | ✓ |
| Unificar nombres de variables en snippets existentes | Más invasivo — cambia código existente. | |
| Tabla resumen al inicio de §4 | Sin nuevo código ejecutable; muestra el flujo de un vistazo. | |

**User's choice:** Bloque de cierre §4 (un solo snippet completo)

### Un snippet o dos

| Option | Description | Selected |
|--------|-------------|----------|
| Un solo snippet completo | bits→...→bits_hat en ~15 líneas, con comentarios por sección. | ✓ |
| Dos snippets: ideal + con estimación | Primero con H conocido, luego con H estimado via pilotos. | |

**User's choice:** Un solo snippet completo
**Notes:** Usuario preguntó sobre FEC — aclarado que el snippet es "uncoded OFDM" (baseline correcto para esta sesión). FEC en capa física existe en NR (LDPC) pero se cubre en Sesión 04. El argumento es correcto: uncoded OFDM = exactamente lo que mide §5.

### Nota explícita sobre FEC

| Option | Description | Selected |
|--------|-------------|----------|
| Sí, nota breve explícita | "Este es el transceptor sin codificación de canal — la BER de §5 mide exactamente este sistema." | ✓ |
| No, el snippet habla por sí mismo | Sin mención explícita de FEC. | |

**User's choice:** Sí, nota breve explícita

---

## Introducción (NARR-02)

### Tipo de gap

| Option | Description | Selected |
|--------|-------------|----------|
| Sí, el puente Sesión 02 → OFDM | La Sesión 02 establece M-QAM y SNR sobre AWGN. El gap: no se dice explícitamente que ese supuesto no se cumple aquí. | ✓ |
| Sí, hay otro gap específico | — | |
| No, validación + retoque menor | La motivación está bien. | |

**User's choice:** El puente Sesión 02 → OFDM
**Notes:** Falta decir que la Sesión 02 asumió AWGN plano y que ese supuesto se rompe en canal frequency-selective.

### Qué falta en el puente

| Option | Description | Selected |
|--------|-------------|----------|
| Nombrar el trade-off explícito | "La Sesión 02 resolvió el canal AWGN plano. Aquí el canal es selectivo en frecuencia — el receptor ya no puede usar un único coeficiente de igualación." | ✓ |
| Añadir la pregunta que se quedó sin resolver | "La pregunta que dejamos abierta: ¿qué ocurre cuando el canal es frequency-selective? OFDM es la respuesta." | |
| Claude decide el retoque | — | |

**User's choice:** Nombrar el trade-off explícito

### Preview de secciones

| Option | Description | Selected |
|--------|-------------|----------|
| No, la intro ya cierra bien | La última frase ya hace de preview: "símbolos QAM → IFFT → CP → canal → FFT → ecualización de un tap". | ✓ |
| Sí, agregar frase de roadmap | Mapear §1–§7 al arco narrativo. | |

**User's choice:** No agregar preview adicional

---

## Referencias Cruzadas §7 Síntesis (NARR-03)

### Formato de referencias

| Option | Description | Selected |
|--------|-------------|----------|
| Parenthetical al final (§X) | Al final de la "Implicación de diseño": "(§2)" o "como se desarrolla en §X." | ✓ |
| Oración de cierre explícita | "Este resultado se desarrolla en §2 (Ortogonalidad y DFT), donde…" | |
| En la línea de Implicación de diseño | Reescribir la línea para incluir la referencia naturalmente. | |

**User's choice:** Parenthetical al final (§X)

### Dimensión 4 — referencia múltiple

| Option | Description | Selected |
|--------|-------------|----------|
| (§4.5, §4.6, §4.7) — las tres | El alumno sabe exactamente dónde buscar cada parte. | ✓ |
| (§4) — sección padre | Referencia a la sección de la cadena completa. | |

**User's choice:** (§4.5, §4.6, §4.7) — las tres

### Caption Figura 3

**User's question:** ¿Cuántos paneles tiene mmse-vs-zf-constellation.png?

**Finding:** `plt.subplots(1, 3)` confirmado en Cell 18 del notebook. La figura tiene 3 paneles: **izquierda** = α[k] (factor de contracción MMSE por subportadora), **centro** = constelación ZF, **derecha** = constelación MMSE.

**Caption actual (incorrecto):** "ZF (izquierda) amplifica ruido… MMSE (derecha) la contiene…" — solo menciona 2 paneles.

| Option | Description | Selected |
|--------|-------------|----------|
| Corregir para mencionar los 3 paneles | Caption completo: izquierda α[k], centro ZF, derecha MMSE. | ✓ |
| Corregir solo el orden | Cambiar izq/der → izq/centro/der. | |

**User's choice:** Corregir para mencionar los 3 paneles con descripción completa

---

## 4 PNGs modificados sin commitear

| Option | Description | Selected |
|--------|-------------|----------|
| Commitear en Fase 3 si son mejoras | El agente inspecciona visualmente antes de commitear. Si mejor contraste/legibilidad → commit. | ✓ |
| Revertir — no fueron aprobados en Fase 2 | git checkout -- figures/*.png | |
| Claude decide por archivo | Inspeccionar y commitear solo los que mejoran objetivamente. | |

**User's choice:** Commitear si son mejoras (inspección previa)
**Notes:** Los 4 PNGs fueron re-generados probablemente con el colormap turbo del commit previo. Tamaños cambiaron (cp-illustration: 124690→123047; ofdm-subcarriers: 386283→321860; zf-equalizer-effect: 143336→145468; zf-equalizer-qam-comparison: 426252→427476).

### Bug WR-01 (doble separador ---)

| Option | Description | Selected |
|--------|-------------|----------|
| Corregir en el mismo plan que transiciones §4 | 1 línea de fix, no merece plan propio. | ✓ |
| Quick-fix fuera del plan | — | |

**User's choice:** En el mismo plan que transiciones

---

## Claude's Discretion

- Redacción exacta de las 5 transiciones nuevas (4.1→4.2, 4.2→4.3, 4.3→4.4, 4.4→4.5, 4.7→4.8) — siguiendo el patrón pregunta-respuesta; Claude adapta al contenido específico de cada bloque.
- Longitud de cada transición.
- Ubicación exacta del bloque de cierre §4 dentro de §4.8.
- Si el snippet de cierre usa ZF o permite elegir ecualizador con parámetro.

## Deferred Ideas

- Demostrar el efecto de densidad de pilotos en estimación LS vs MMSE — Sesión 08.
- Ejercicio interactivo para el bloque de cierre §4 — sección de Ejercicios (otra fase).
- Soft decisions (LLR) — §4.8 los menciona; implementación en Sesión 04.
