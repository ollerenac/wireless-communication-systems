---
quick_id: 260523-r
slug: note-frecuencias-negativas-subcarriers-fig
status: complete
date: 2026-05-23
---

# Summary: Nota sobre frecuencias negativas en figura ofdm-subcarriers

**Qué se hizo:** Se insertó un párrafo explicativo entre la imagen `ofdm-subcarriers.png` y el texto descriptivo en §2 de `index.md`. El párrafo explica que el eje horizontal usa la representación en banda base centrada (índices −N/2 a N/2−1 en la DFT), que los índices negativos corresponden a subportadoras de índice alto (k > N/2), y que la figura muestra 6 subportadoras representativas.

**Por qué:** El código de la notebook traza sincs en sc ∈ {−2, −1, 0, 1, 2, 3} sobre f ∈ [−3, 3] — un diagrama pedagógico, no el espectro real de N=64 subportadoras. Sin contexto, los índices negativos confunden a quien espera k = 0…N−1.

**Archivo:** `docs/sessions/03-ofdm-systems/index.md` (2 oraciones insertadas entre líneas 308–310)
