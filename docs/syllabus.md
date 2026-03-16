# Programa del Curso

## Sistemas de Comunicaciones Inalámbricas

**Nivel**: Máster Universitario (MSc / MEng)
**Modalidad**: Autónoma, acceso abierto
**Sesiones**: 15 sesiones semanales
**Sitio web**: [ollerenac.github.io/wireless-communication-systems](https://ollerenac.github.io/wireless-communication-systems/)
**Repositorio**: [github.com/ollerenac/wireless-communication-systems](https://github.com/ollerenac/wireless-communication-systems)
**Licencia**: [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)

---

## Descripción

Este curso ofrece un tratamiento riguroso, a nivel de posgrado, de los sistemas de comunicaciones inalámbricas — desde los fundamentos de la capa física hasta las técnicas más avanzadas de 5G/6G y el diseño de sistemas nativos con inteligencia artificial. Cada sesión combina teoría matemática con un laboratorio práctico en Python, para que el estudiante desarrolle tanto profundidad analítica como habilidades de implementación.

El curso se organiza en tres arcos temáticos:

1. **Fundamentos de Capa Física** (Sesiones 1–4): modelado de canal, modulación, OFDM, codificación de canal
2. **Sistemas Multi-Antena y PHY Avanzada** (Sesiones 5–7): MIMO, MIMO masivo, estimación de canal
3. **IA/ML para Sistemas Inalámbricos y Tecnologías Emergentes** (Sesiones 8–15): aprendizaje automático, aprendizaje profundo, aprendizaje por refuerzo, RIS, ISAC, 6G y redes especializadas

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
2. Diseñar y analizar esquemas de modulación digital y calcular la tasa de error de bit (BER)
3. Implementar y simular transceptores OFDM desde primeros principios
4. Aplicar técnicas de codificación de canal (LDPC, Polar) y evaluar la ganancia de codificación
5. Analizar la capacidad de canales MIMO y diseñar precodificadores de conformación de haz
6. Implementar estimadores de canal clásicos y basados en aprendizaje automático
7. Aplicar técnicas de aprendizaje automático y aprendizaje profundo al diseño de sistemas inalámbricos
8. Diseñar sistemas de comunicación extremo a extremo basados en autoencoders
9. Formular y resolver problemas de asignación de recursos mediante aprendizaje por refuerzo
10. Evaluar tecnologías emergentes como RIS, ISAC, THz y MIMO libre de celdas

---

## Sesiones del Curso

| # | Título | Contenidos | Laboratorio Python |
|---|--------|-----------|-------------------|
| 01 | Modelado del Canal Inalámbrico | Pérdida de propagación, modelo log-distancia, sombreado, desvanecimiento multitrayecto, distribuciones de Rayleigh y Rician, ancho de banda y tiempo de coherencia, dispersión Doppler | Simular canales de desvanecimiento Rayleigh y Rician; graficar BER vs SNR; generar respuestas impulsionales del canal |
| 02 | Modulación Digital y Análisis de BER | BPSK, QPSK, M-QAM, codificación Gray, derivación de BER, diseño de constelaciones, 1024-QAM en 5G NR | Implementar cadena TX-RX completa; calcular curvas de BER para BPSK/QPSK/16-QAM/64-QAM; visualizar diagramas de constelación |
| 03 | Sistemas OFDM e Implementación | Concepto multiportadora, transceptor IFFT/FFT, prefijo cíclico, interferencia entre portadoras, eficiencia espectral, PAPR | Construir un transceptor OFDM completo con FFT/IFFT; simular sobre canal con desvanecimiento |
| 04 | Codificación de Canal: LDPC y Códigos Polares | Límite de capacidad de Shannon, grafo de Tanner LDPC, decodificación por propagación de creencias, códigos Polares, decodificación por cancelación sucesiva, selección de códigos en 5G NR | Codificar/decodificar con LDPC y códigos Polares; graficar curvas BER en cascada; comparar con línea base sin codificación |
| 05 | Fundamentos MIMO y Capacidad | Evolución SISO→MIMO, matriz de canal, descomposición SVD, relleno de agua, análisis de capacidad, compromiso diversidad-multiplexación, código Alamouti | Calcular capacidad del canal MIMO vía SVD; simular relleno de agua; comparar multiplexación espacial vs diversidad |
| 06 | MIMO Masivo y Conformación de Haz Digital | Endurecimiento del canal, propagación favorable, precodificador MRT, precodificador ZF, contaminación de pilotos, arrays de 64–512 antenas, gNB en 5G | Simular MIMO masivo en enlace descendente con precodificadores MRT y ZF; graficar tasa suma vs número de antenas |
| 07 | Estimación de Canal: Clásica y Basada en Aprendizaje | Estimación basada en pilotos, estimador LS, estimador MMSE, compressive sensing para canales dispersos, estimadores basados en redes neuronales | Implementar estimadores LS y MMSE; comparar MSE vs SNR; entrenar un estimador DNN y evaluar |
| 08 | Aprendizaje Automático para Redes Inalámbricas: Fundamentos | Taxonomía de ML, casos de uso en comunicaciones, CNN para datos IQ, clasificación automática de modulación (AMC), diseño de conjuntos de datos | Entrenar un clasificador CNN de modulación automática sobre muestras IQ sintéticas; evaluar precisión vs SNR |
| 09 | Comunicaciones Aprendidas Extremo a Extremo | Autoencoder como TX+RX conjunto, canal como capa no diferenciable, constelaciones aprendidas, marco Sionna | Construir un transceptor autoencoder en PyTorch; entrenar sobre canal AWGN; visualizar constelación aprendida; comparar BER |
| 10 | Aprendizaje Profundo para Detección MIMO | Problema de detección MIMO, desenvolvimiento profundo, arquitectura OAMP-Net, ecualización basada en DL, complejidad vs rendimiento | Implementar detector OAMP-Net de desenvolvimiento profundo; comparar BER vs MMSE-SIC para MIMO 4×4 con 16-QAM |
| 11 | Aprendizaje por Refuerzo para Asignación de Recursos | Formulación MDP, Q-learning, DQN, repetición de experiencias, asignación de potencia multiusuario, investigación 3GPP/IEEE en RL | Entrenar un agente DQN para asignación de potencia en enlace descendente multiusuario; comparar tasa suma vs relleno de agua |
| 12 | Superficies Inteligentes Reconfigurables (RIS) | RIS pasiva vs activa, modelo de canal en cascada, matriz de desfase, optimización por gradiente, contexto 6G | Modelar enlace asistido por RIS; optimizar desfases para maximizar SNR; graficar SNR vs número de elementos |
| 13 | Detección e Integración con Comunicaciones (ISAC) | Forma de onda dual, radar OFDM, estimación rango-Doppler, compromiso detección-comunicación, aplicaciones en vehículos autónomos | Diseñar forma de onda OFDM compartida; simular mapa rango-Doppler de radar; calcular SINR de comunicación vs SNR de detección |
| 14 | Fronteras del 6G: THz, MIMO Libre de Celdas y Aprendizaje Federado | Modelos de canal THz (>100 Gbps, absorción molecular), MIMO libre de celdas con APs distribuidos, FedAvg para estimación de canal distribuida | Simular modelo de canal THz o implementar aprendizaje federado para estimación de canal |
| 15 | Sistemas Inalámbricos Especializados | Radio cognitiva y detección de espectro, IoT/LPWAN (LoRa, NB-IoT, Sigfox), satélite (LEO/MEO/GEO), redes vehiculares (V2X, C-V2X) | Implementar detección de espectro por energía; calcular balances de enlace para IoT, satélite y escenarios vehiculares |

---

## Evaluación

Este es un curso abierto y autónomo sin evaluación calificada. Cada sesión incluye:

- **≥ 3 ejercicios** con soluciones de referencia paso a paso
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
