# Programa del Curso

## Sistemas de Comunicaciones Inalámbricas

- **Nivel**: Máster Universitario (MSc / MEng)
- **Modalidad**: Autónoma, acceso abierto
- **Sesiones**: 16 sesiones semanales
- **Sitio web**: [ollerenac.github.io/wireless-communication-systems](https://ollerenac.github.io/wireless-communication-systems/)
- **Repositorio**: [github.com/ollerenac/wireless-communication-systems](https://github.com/ollerenac/wireless-communication-systems)
- **Licencia**: [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)

---

## Descripción

Este curso ofrece un tratamiento riguroso, a nivel de posgrado, de los sistemas de comunicaciones inalámbricas — desde los fundamentos de la capa física hasta las tecnologías más avanzadas de 5G y 6G. Cada sesión combina teoría matemática con un laboratorio práctico en Python, para que el estudiante desarrolle tanto profundidad analítica como habilidades de implementación.

El curso se organiza en tres arcos temáticos:

1. **Fundamentos de Capa Física** (Clases 1–7): canal inalámbrico, modulación digital, OFDM, laboratorio GNU Radio, codificación de canal
2. **Sistemas Multi-Antena y 5G** (Clases 9–11): MIMO y MIMO masivo, arquitectura 5G NR, comunicaciones mmWave
3. **Seminarios y Tendencias** (Clases 12–16): IA en comunicaciones, Software-Defined Radio, Wireless IoT, 6G, examen final

---

## Público Objetivo

Estudiantes de posgrado en ingeniería eléctrica, ingeniería de telecomunicaciones o áreas afines que buscan un tratamiento completo y moderno de los sistemas inalámbricos. El curso también es adecuado para profesionales de la industria que deseen incorporarse a la investigación en 5G/6G o al diseño inalámbrico basado en IA.

---

## Prerrequisitos

El estudiante debe tener conocimientos sólidos a nivel de grado en las siguientes áreas:

| Área | Contenidos clave |
|------|-----------------|
| Señales y Sistemas | Transformada de Fourier, convolución, filtrado, análisis en frecuencia |
| Probabilidad y Estadística | Variables aleatorias, distribuciones de probabilidad, esperanza, ruido gaussiano |
| Comunicaciones Digitales | Modulación en banda base, teorema de muestreo, filtro adaptado, SNR |
| Álgebra Lineal | Operaciones matriciales, descomposición en valores propios, SVD |
| Programación | Python básico (NumPy, Matplotlib); cuadernos Jupyter |

---

## Resultados de Aprendizaje

Al finalizar este curso, el estudiante será capaz de:

1. Modelar canales inalámbricos incluyendo pérdidas de propagación, sombreado y desvanecimiento multitrayecto
2. Diseñar esquemas de modulación digital y calcular la tasa de error de bit (BER) analíticamente
3. Implementar transceptores OFDM y sistemas de codificación de canal (LDPC, Polar) desde primeros principios
4. Gestionar el acceso múltiple mediante OFDMA, NOMA y planificadores de recursos de radio
5. Analizar la capacidad de canales MIMO y diseñar precodificadores (MRT, ZF, water-filling)
6. Estimar el canal inalámbrico con métodos clásicos (LS, MMSE) y entender su contexto en 5G NR
7. Evaluar tecnologías emergentes: 5G NR, mmWave, RIS, ISAC y radio cognitiva
8. Aplicar técnicas de IA/ML al diseño de sistemas inalámbricos y describir las fronteras del 6G

---

## Sesiones del Curso

| # | Título | Contenidos | Laboratorio Python |
|---|--------|-----------|-------------------|
| 01 | Modelado del Canal Inalámbrico | Path loss, modelo log-distancia, sombreado log-normal, multitrayecto, Rayleigh/Rician, coherencia, Doppler, modelos 3GPP TR 38.901 | Rayleigh/Rician; BER vs SNR; CDF y probabilidad de interrupción; calculadora de presupuesto de enlace |
| 02 | Modelado del Canal Inalámbrico | Canal multipath, perfil de potencia de retardo (PDP), ancho de banda de coherencia, tiempo de coherencia, espectro Doppler, caracterización estadística | — |
| 03 | Modulación Digital y Análisis de BER | BPSK, QPSK, M-QAM, codificación Gray, derivación de BER, diagramas de constelación, 1024-QAM en 5G NR | Cadena TX-RX completa; curvas BER para BPSK/QPSK/16-QAM/64-QAM; constelaciones |
| 04 | Sistemas OFDM e Implementación (I) | Concepto multiportadora, transceptor IFFT/FFT, prefijo cíclico, ISI e ICI, eficiencia espectral, PAPR | — |
| 05 | Sistemas OFDM e Implementación (II) | Ecualización ZF y MMSE, estimación de canal LS con pilotos, BER de OFDM en canal selectivo en frecuencia | Transceptor OFDM completo; ecualizadores ZF/MMSE; curvas BER waterfall |
| 06 | Lab OFDM con GNU Radio | Cadena OFDM visual en GNU Radio Companion, canal AWGN y multipath, prefijo cíclico, constelación en tiempo real, medición de BER | GNU Radio Companion: flujo TX/RX OFDM |
| 07 | Codificación de Canal: LDPC y Códigos Polares | Límite de Shannon, grafo de Tanner LDPC, belief propagation, códigos Polares, decodificador SC, selección en 5G NR | LDPC y Polar; curvas BER waterfall; comparativa sin codificación |
| 08 | Examen Parcial | — | — |
| 09 | Fundamentos MIMO y MIMO Masivo | SISO→MIMO, matriz de canal, SVD, water-filling, capacidad, compromiso diversidad-multiplexación, MRT y ZF, endurecimiento del canal, propagación favorable, contaminación de pilotos, arrays 64–512 antenas | Capacidad MIMO vía SVD; precodificadores MRT/ZF para M=8,32,128 antenas y K=4 usuarios |
| 10 | Arquitectura 5G NR: Interfaz Radio y Numerología | Numerología μ y espaciado de subportadoras, estructura de trama y ranura NR, cuadrícula de recursos, FR1/FR2, HARQ, adaptación de enlace, tablas MCS | Visualizador de cuadrícula NR para μ=0,1,2,3; adaptación de enlace con CQI; throughput vs SNR |
| 11 | Comunicaciones mmWave | Espectro 24–100 GHz, propagación mmWave, arrays de antenas, beamforming híbrido, gestión de haz en 5G NR FR2 | Pérdida de propagación mmWave vs frecuencia y distancia; patrones de array ULA; beamforming analógico |
| 12 | Seminario — IA en Comunicaciones Inalámbricas | Lectura y discusión de papers: taxonomía ML para comunicaciones, CNN para clasificación de modulación (AMC), autoencoder TX+RX, DNN para estimación de canal | — |
| 13 | Seminario — Software-Defined Radio | Lectura y discusión de papers: arquitecturas SDR, GNU Radio, plataformas USRP, diseño de formas de onda, aplicaciones en radio cognitiva | GNU Radio: modulación SDR en tiempo real |
| 14 | Seminario — Wireless IoT | Lectura y discusión de papers: LoRa, NB-IoT, Sigfox, presupuestos de enlace LPWAN, edge computing, protocolos de capa baja para IoT | — |
| 15 | 6G: Fronteras e Investigación Abierta | Requisitos ITU-R IMT-2030, canal THz y absorción molecular, MIMO libre de celdas, redes no terrestres (NTN) LEO/MEO, aprendizaje federado, hoja de ruta 6G | — |
| 16 | Examen Final | — | — |

---

## Evaluación

| Componente | Peso |
|---|:---:|
| Examen Parcial (Clase 08) | 30% |
| Examen Final (Clase 16) | 30% |
| Promedio de Laboratorios (4 labs) | 40% |

La nota final es el promedio ponderado de los tres componentes, todos sobre 20 puntos. Los laboratorios previstos son:

- **Lab 1** — Sistemas OFDM (Clase 05)
- **Lab 2** — Lab OFDM con GNU Radio (Clase 06)
- **Lab 3** — Fundamentos MIMO y MIMO Masivo (Clase 09)
- **Lab 4** — Software-Defined Radio (Clase 13)

---

## Cómo Usar Este Curso

### Opción A — Sitio web (recomendado)
Navega las sesiones en el sitio web del curso. Cada página incluye apuntes de la sesión, ejercicios con soluciones desplegables y un botón **Abrir en Colab** para el cuaderno de laboratorio.

### Opción B — Clonar el repositorio
```bash
git clone https://github.com/ollerenac/wireless-communication-systems.git
cd wireless-communication-systems
pip install -r requirements.txt
mkdocs serve          # vista previa en http://127.0.0.1:8000
```

---

## Licencia y Atribución

Todo el contenido del curso se publica bajo la licencia [Creative Commons Atribución 4.0 Internacional (CC BY 4.0)](https://creativecommons.org/licenses/by/4.0/).

Eres libre de compartir, adaptar y redistribuir este material para cualquier propósito — incluso comercial — siempre que se otorgue el crédito correspondiente:

> *Sistemas de Comunicaciones Inalámbricas* por ollerenac, bajo licencia CC BY 4.0.
> Fuente: https://github.com/ollerenac/wireless-communication-systems
