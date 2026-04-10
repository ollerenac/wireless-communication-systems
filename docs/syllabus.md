# Programa del Curso

## Sistemas de Comunicaciones Inalámbricas

- **Nivel**: Máster Universitario (MSc / MEng)
- **Modalidad**: Autónoma, acceso abierto
- **Sesiones**: 15 sesiones semanales
- **Sitio web**: [ollerenac.github.io/wireless-communication-systems](https://ollerenac.github.io/wireless-communication-systems/)
- **Repositorio**: [github.com/ollerenac/wireless-communication-systems](https://github.com/ollerenac/wireless-communication-systems)
- **Licencia**: [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)

---

## Descripción

Este curso ofrece un tratamiento riguroso, a nivel de posgrado, de los sistemas de comunicaciones inalámbricas — desde los fundamentos de la capa física hasta las tecnologías más avanzadas de 5G y 6G. Cada sesión combina teoría matemática con un laboratorio práctico en Python, para que el estudiante desarrolle tanto profundidad analítica como habilidades de implementación.

El curso se organiza en tres arcos temáticos:

1. **Fundamentos de Capa Física** (Sesiones 1–5): modelado de canal, modulación, OFDM, codificación de canal, acceso múltiple
2. **Sistemas Multi-Antena** (Sesiones 6–8): MIMO, MIMO masivo, estimación de canal
3. **Tecnologías Avanzadas y Emergentes** (Sesiones 9–15): 5G NR, mmWave, RIS, ISAC, radio cognitiva, IA/ML, 6G

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
| 02 | Modulación Digital y Análisis de BER | BPSK, QPSK, M-QAM, codificación Gray, derivación de BER, diagramas de constelación, 1024-QAM en 5G NR | Cadena TX-RX completa; curvas BER para BPSK/QPSK/16-QAM/64-QAM; constelaciones |
| 03 | Sistemas OFDM e Implementación | Concepto multiportadora, transceptor IFFT/FFT, prefijo cíclico, ICI, eficiencia espectral, PAPR | Transceptor OFDM completo; simulación sobre canal con desvanecimiento selectivo en frecuencia |
| 04 | Codificación de Canal: LDPC y Códigos Polares | Límite de Shannon, grafo de Tanner LDPC, belief propagation, códigos Polares, SCD, selección en 5G NR | LDPC y Polar; curvas BER waterfall; comparativa sin codificación |
| 05 | Acceso Múltiple: OFDMA, NOMA y Gestión de Recursos | FDMA/TDMA/CDMA/OFDMA, asignación de subportadoras, NOMA con SIC, emparejamiento de usuarios, planificador proporcional-justo | Asignación OFDMA multiusuario; NOMA con SIC; comparativa NOMA vs OMA; planificador proporcional-justo |
| 06 | Fundamentos MIMO y Capacidad | SISO→MIMO, matriz de canal, SVD, relleno de agua, capacidad, compromiso diversidad-multiplexación, código Alamouti | Capacidad MIMO vía SVD; water-filling; multiplexación espacial vs diversidad Alamouti |
| 07 | MIMO Masivo y Conformación de Haz Digital | Endurecimiento del canal, propagación favorable, precodificadores MRT y ZF, contaminación de pilotos, arrays 64–512 antenas, beamforming híbrido | Precodificadores MRT/ZF para M=8,32,128 antenas y K=4 usuarios; tasa suma vs #antenas |
| 08 | Estimación de Canal: Métodos Clásicos | Estimación basada en pilotos, estimador LS, estimador MMSE, filtro de Wiener, cuadrícula de pilotos OFDM, SRS/DMRS en 5G NR | Estimadores LS y MMSE sobre cuadrícula OFDM; MSE vs SNR; efecto de la densidad de pilotos |
| 09 | Arquitectura 5G NR: Interfaz Radio y Numerología | Numerología μ y espaciado de subportadoras, estructura de trama y ranura NR, cuadrícula de recursos, FR1/FR2, HARQ, adaptación de enlace, tablas MCS | Visualizador de cuadrícula NR para μ=0,1,2,3; adaptación de enlace con CQI; throughput vs SNR |
| 10 | Comunicaciones mmWave y Sub-THz | Espectro 24–100 GHz, propagación mmWave, arrays de antenas, beamforming híbrido, gestión de haz en 5G NR FR2, sub-THz para 6G, modelos de canal THz | Pérdida de propagación mmWave vs frecuencia y distancia; patrones de array ULA; beamforming analógico |
| 11 | Superficies Inteligentes Reconfigurables (RIS) | RIS pasiva vs activa, campo cercano/lejano, canal en cascada, matriz de desfase, optimización de fases, RIS vs relé, estándarización 6G | Optimización de fases; SNR vs #elementos RIS; mapas de cobertura con/sin RIS |
| 12 | Detección e Integración con Comunicaciones (ISAC) | Forma de onda dual, radar OFDM, estimación rango-Doppler, resolución en rango, compromiso detección-comunicación, aplicaciones V2X | Forma de onda OFDM compartida; mapa rango-Doppler 2D FFT; SINR comms vs SNR radar |
| 13 | Radio Cognitiva y Gestión Dinámica de Espectro | Usuarios primarios/secundarios, detección de espectro (energía, filtro adaptado, ciclostacionaria), curva ROC, acceso dinámico al espectro, IoT/LPWAN: LoRa, NB-IoT, Sigfox | Detector de energía; curva ROC (Pd vs Pfa); presupuestos de enlace LoRa/NB-IoT/Sigfox |
| 14 | IA/ML para Comunicaciones Inalámbricas | Taxonomía ML para sistemas inalámbricos, CNN para clasificación de modulación (AMC), autoencoder TX+RX conjunto, DNN para estimación de canal, visión general de RL para asignación de recursos | Clasificador CNN AMC; autoencoder con constelación aprendida; estimador DNN vs LS/MMSE |
| 15 | 6G: Fronteras, Investigación Abierta y Redes Especializadas | Requisitos ITU-R IMT-2030, canal THz y absorción molecular, MIMO libre de celdas, redes no terrestres (NTN) LEO/MEO/GEO, aprendizaje federado, hoja de ruta 6G | Canal THz vs mmWave; presupuesto de enlace satélite LEO; FedAvg para estimación distribuida |

---

## Evaluación

Este es un curso abierto y autónomo sin evaluación calificada. Cada sesión incluye:

- **≥ 5 ejercicios** con soluciones de referencia paso a paso
- **1 laboratorio Python** (cuaderno Jupyter, ejecutable en Google Colab sin instalación local)

Se recomienda al estudiante intentar los ejercicios de forma independiente antes de consultar las soluciones.

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
