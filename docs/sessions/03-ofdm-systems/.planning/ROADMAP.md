# Roadmap: Sesión 03 — Sistemas OFDM

## Overview

Cuatro fases de trabajo editorial para dejar `index.md` y `lab.ipynb` listos para publicar y dictar en clase. Primero se audita sin tocar nada, luego se corrigen los errores encontrados, luego se fortalece la narrativa, y finalmente se hace un pase de revisión final.

## Phases

**Phase Numbering:**
- Integer phases (1, 2, 3): Planned milestone work
- Decimal phases (2.1, 2.2): Urgent insertions (marked with INSERTED)

Decimal phases appear between their surrounding integers in numeric order.

- [ ] **Phase 1: Auditoría y Diagnóstico** - Leer notebook y index.md completos; catalogar todos los errores antes de tocar nada
- [ ] **Phase 2: Corrección de Contenido** - Corregir errores de fórmulas, referencias rotas y desalineación de código
- [ ] **Phase 3: Mejora de Narrativa** - Fortalecer hilo conductor de §4, mejorar introducción e integrar síntesis de §7
- [ ] **Phase 4: Revisión Final** - Verificar coherencia global, correr notebook de punta a punta y confirmar publicabilidad

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
**Plans**: TBD

### Phase 2: Corrección de Contenido
**Goal**: Todos los errores de corrección catalogados en la fase 1 están corregidos en index.md y lab.ipynb
**Depends on**: Phase 1
**Requirements**: CORR-01, CORR-02, CORR-03, LAB-01
**Success Criteria** (what must be TRUE):
  1. Cada enunciado falso y fórmula incorrecta identificada en fase 1 ha sido corregida — no quedan items abiertos de esa lista
  2. Todas las referencias a figuras en index.md apuntan a archivos que existen en `figures/`; no hay referencias rotas ni figuras huérfanas sin referenciar
  3. Todos los snippets Python de index.md coinciden con el comportamiento real del lab.ipynb (misma API, mismas variables, mismo orden lógico)
  4. lab.ipynb corre de inicio a fin sin ningún error de celda en el entorno de trabajo
**Plans**: TBD

### Phase 3: Mejora de Narrativa
**Goal**: El flujo pedagógico del documento es coherente: cada sección motiva la siguiente y la síntesis final conecta con el desarrollo
**Depends on**: Phase 2
**Requirements**: NARR-01, NARR-02, NARR-03
**Success Criteria** (what must be TRUE):
  1. Cada bloque 4.1–4.8 termina con una frase de transición que nombra el problema que resuelve y el problema que deja pendiente para el siguiente bloque
  2. La Introducción menciona explícitamente las sesiones 01–02 y establece la motivación de OFDM sin saltos lógicos detectables al leer en secuencia
  3. Cada una de las 5 dimensiones de §7 incluye una referencia explícita a la sección donde se desarrolló ese concepto
**Plans**: TBD

### Phase 4: Revisión Final
**Goal**: El documento completo está listo para publicar — coherente, sin errores detectables, ejecutable
**Depends on**: Phase 3
**Requirements**: (revisión transversal — todos los requisitos validados)
**Success Criteria** (what must be TRUE):
  1. Una lectura de corrido de index.md de §1 a §7 no revela contradicciones, saltos ni referencias rotas
  2. lab.ipynb corre limpio de punta a punta con `Run All` — cero errores, outputs generados
  3. Un profesor puede dictar la clase usando solo index.md y lab.ipynb sin necesitar ninguna corrección de última hora
**Plans**: TBD

## Progress

**Execution Order:**
Phases execute in numeric order: 1 → 2 → 3 → 4

| Phase | Plans Complete | Status | Completed |
|-------|----------------|--------|-----------|
| 1. Auditoría y Diagnóstico | 0/? | Not started | - |
| 2. Corrección de Contenido | 0/? | Not started | - |
| 3. Mejora de Narrativa | 0/? | Not started | - |
| 4. Revisión Final | 0/? | Not started | - |
