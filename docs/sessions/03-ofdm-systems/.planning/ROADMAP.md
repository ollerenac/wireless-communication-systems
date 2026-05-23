# Roadmap: Sesión 03 — Sistemas OFDM

## Overview

Cuatro fases de trabajo editorial para dejar `index.md` y `lab.ipynb` listos para publicar y dictar en clase. Primero se audita sin tocar nada, luego se corrigen los errores encontrados, luego se fortalece la narrativa, y finalmente se hace un pase de revisión final.

## Phases

**Phase Numbering:**
- Integer phases (1, 2, 3): Planned milestone work
- Decimal phases (2.1, 2.2): Urgent insertions (marked with INSERTED)

Decimal phases appear between their surrounding integers in numeric order.

- [x] **Phase 1: Auditoría y Diagnóstico** - Leer notebook y index.md completos; catalogar todos los errores antes de tocar nada (completed 2026-05-22)
- [x] **Phase 2: Corrección de Contenido** - Corregir errores de fórmulas, referencias rotas y desalineación de código (completed 2026-05-22)
- [x] **Phase 3: Mejora de Narrativa** - Fortalecer hilo conductor de §4, mejorar introducción e integrar síntesis de §7 (completed 2026-05-23)
- [x] **Phase 4: Revisión Final** - Verificar coherencia global, correr notebook de punta a punta y confirmar publicabilidad (completed 2026-05-22)

## Phase Details

### Phase 1: Auditoría y Diagnóstico
**Goal**: El equipo tiene un inventario completo de todos los problemas — sin haber cambiado una sola línea del documento
**Depends on**: Nothing (first phase)
**Requirements**: CORR-01, CORR-02, CORR-03, LAB-01 (diagnóstico de todos)
**Success Criteria** (what must be TRUE):
  1. Existe una lista numerada de cada enunciado falso o fórmula incorrecta encontrada en index.md, con número de sección y línea
  2. Existe una lista de todas las referencias a figuras en index.md cruzada contra los archivos reales en `figures/` — cada discrepancia marcada explícitamente
  3. Existe un diff conceptual de cada snippet Python en index.md versus su equivalente en lab.ipynb, marcando coincidencia o desalineación
  4. Existe un registro de si lab.ipynb corre de punta a punta sin error de celda, con el número de celda de cualquier fallo encontrado
**Plans**: 4 plans
  - [x] 01-01-PLAN.md — Auditar fórmulas y enunciados de index.md (§4, §6 prioritarios; §1, §2, §5, §7 solo errores de contenido) → 01-AUDIT-FRAGMENT-formulas.md
  - [x] 01-02-PLAN.md — Auditar referencias de figuras cruzadas contra disco → 01-AUDIT-FRAGMENT-figuras.md
  - [x] 01-03-PLAN.md — Auditar snippets Python (index.md vs lab.ipynb) + ejecutar notebook end-to-end → 01-AUDIT-FRAGMENT-codigo.md, 01-AUDIT-FRAGMENT-notebook.md
  - [x] 01-04-PLAN.md — Ensamblar informe final 01-AUDIT-FINDINGS.md desde los 4 fragmentos con renumeración global

### Phase 2: Corrección de Contenido
**Goal**: Todos los errores de corrección catalogados en la fase 1 están corregidos en index.md y lab.ipynb
**Depends on**: Phase 1
**Requirements**: CORR-01, CORR-02, CORR-03, LAB-01
**Success Criteria** (what must be TRUE):
  1. Cada enunciado falso y fórmula incorrecta identificada en fase 1 ha sido corregida — no quedan items abiertos de esa lista
  2. Todas las referencias a figuras en index.md apuntan a archivos que existen en `figures/`; no hay referencias rotas ni figuras huérfanas sin referenciar
  3. Todos los snippets Python de index.md coinciden con el comportamiento real del lab.ipynb (misma API, mismas variables, mismo orden lógico)
  4. lab.ipynb corre de inicio a fin sin ningún error de celda en el entorno de trabajo
**Plans**: 3 plans
  - [x] 02-01-PLAN.md — Versionar 6 PNGs generadas + verificar lab.ipynb (CORR-02, LAB-01) [Wave 1]
  - [x] 02-02-PLAN.md — Corregir fórmulas LaTeX BLOCKER-S.01/S.02/MINOR-01 en §2 y §6 (CORR-01) [Wave 1]
  - [x] 02-03-PLAN.md — Alinear snippets MMSE/LS + insertar figura en §4.8 (CORR-01, CORR-02, CORR-03) [Wave 2]

### Phase 3: Mejora de Narrativa
**Goal**: El flujo pedagógico del documento es coherente: cada sección motiva la siguiente y la síntesis final conecta con el desarrollo
**Depends on**: Phase 2
**Requirements**: NARR-01, NARR-02, NARR-03
**Success Criteria** (what must be TRUE):
  1. Cada bloque 4.1–4.8 termina con una frase de transición que nombra el problema que resuelve y el problema que deja pendiente para el siguiente bloque
  2. La Introducción menciona explícitamente las sesiones 01–02 y establece la motivación de OFDM sin saltos lógicos detectables al leer en secuencia
  3. Cada una de las 5 dimensiones de §7 incluye una referencia explícita a la sección donde se desarrolló ese concepto
**Plans**: 4 plans
  - [x] 03-01-PLAN.md — Insertar 6 transiciones §4 + bloque de cierre §4 (cadena bits→bits_hat) + fix bug WR-01 (NARR-01)
  - [x] 03-02-PLAN.md — Insertar frase puente Sesión 02 → OFDM en Introducción (NARR-02)
  - [x] 03-03-PLAN.md — Cross-refs §7 (5 dimensiones) + corregir caption Figura 3 (3 paneles) (NARR-03)
  - [x] 03-04-PLAN.md — Inspección visual de 4 PNGs modificados + commit/revert por archivo (D-16)

### Phase 4: Revisión Final
**Goal**: El documento completo está listo para publicar — coherente, sin errores detectables, ejecutable
**Depends on**: Phase 3
**Requirements**: (revisión transversal — todos los requisitos validados)
**Success Criteria** (what must be TRUE):
  1. Una lectura de corrido de index.md de §1 a §7 no revela contradicciones, saltos ni referencias rotas
  2. lab.ipynb corre limpio de punta a punta con `Run All` — cero errores, outputs generados
  3. Un profesor puede dictar la clase usando solo index.md y lab.ipynb sin necesitar ninguna corrección de última hora
**Plans**: 3 plans
  - [x] 04-01-PLAN.md — Verificación estructural automática de index.md (4 checks) + reporte de publicabilidad
  - [x] 04-02-PLAN.md — Verificación y alineación del notebook lab.ipynb (LAB-01)
  - [x] 04-03-PLAN.md — Cierre de tracking (REQUIREMENTS.md + PROJECT.md) + exit criterion mkdocs build

## Progress

**Execution Order:**
Phases execute in numeric order: 1 → 2 → 3 → 4

| Phase | Plans Complete | Status | Completed |
|-------|----------------|--------|-----------|
| 1. Auditoría y Diagnóstico | 4/4 | Complete   | 2026-05-22 |
| 2. Corrección de Contenido | 3/3 | Complete   | 2026-05-22 |
| 3. Mejora de Narrativa | 4/4 | Complete   | 2026-05-23 |
| 4. Revisión Final | 3/3 | Complete   | 2026-05-23 |
