<!-- GSD:project-start source:PROJECT.md -->
## Project

**Sesión 04 — Codificación de Canal: LDPC y Códigos Polar**

Clase 04 de un curso de posgrado en sistemas de comunicaciones inalámbricas. Cubre la codificación de canal moderna: del límite de Shannon a LDPC con belief propagation y Polar con cancelación sucesiva, tal como se usan en 5G NR. El material existe como `index.md` (narrativa pedagógica publicada en el site) y `lab.ipynb` (notebook ejecutable, fuente de verdad de código y figuras).

**Estado actual:** Borrador funcional — index.md correcto en contenido, lab.ipynb con ejercicios básicos. Objetivo: paridad de calidad con la sesión 03 (figuras publicables, BP Monte Carlo realista, Polar N=64, ejercicio integrador OFDM+LDPC).

**Core Value:** El `index.md` debe explicar rigurosamente lo que el `lab.ipynb` demuestra — cada sección teórica tiene una figura publicable generada por código, el notebook implementa la teoría a escala real, y el ejercicio integrador conecta el transceptor OFDM de la sesión 03 con el codec FEC de esta sesión.

### Constraints

- **Idioma:** Todo en español, terminología técnica en inglés
- **Compatibilidad:** El index.md debe seguir siendo válido MkDocs-Material (figuras con `<figure markdown="span">`, admonitions `??? note/example`)
- **Referencia:** `../03-ofdm-systems/` es el estándar de calidad — figuras, narrativa, estructura
- **Notebook:** El lab.ipynb es ground truth — las figuras del index.md deben generarse desde el notebook
- **Reutilización:** El ejercicio integrador (fase 5) reutiliza sin modificación las funciones OFDM de la sesión 03
<!-- GSD:project-end -->

<!-- GSD:workflow-start source:GSD defaults -->
## GSD Workflow Enforcement

Before using Edit, Write, or other file-changing tools, start work through a GSD command so planning artifacts and execution context stay in sync.

Use these entry points:
- `/gsd-quick` for small fixes, doc updates, and ad-hoc tasks
- `/gsd-debug` for investigation and bug fixing
- `/gsd-execute-phase` for planned phase work

Do not make direct repo edits outside a GSD workflow unless the user explicitly asks to bypass it.
<!-- GSD:workflow-end -->

<!-- GSD:profile-start -->
## Developer Profile

> Profile not yet configured. Run `/gsd-profile-user` to generate your developer profile.
> This section is managed by `generate-claude-profile` -- do not edit manually.
<!-- GSD:profile-end -->
