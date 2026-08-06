---
title: "Guía: crear tu escena OSM con Blender"
description: "De OpenStreetMap a un XML de Mitsuba listo para Sionna RT: instalar Blender 4.2 en Windows, descargar el mapa con Blosm, asignar materiales ITU y exportar con los ejes correctos."
---

# Guía: crear tu escena de ciudad para el notebook

Esta guía produce lo único que el notebook de diseño necesita de ti: una carpeta con un archivo `.xml` y sus mallas (`meshes/`), que se carga en los procedimientos del notebook con:

```python
scene = load_scene("escenas/mi_escena/mi_escena.xml")
```

El proceso completo está demostrado en video —
**[tutorial en YouTube](https://youtu.be/PIdn1R7FSrg?si=V8-HVuCvWGZG6v39)** —
y aquí en pasos verificables. 

El entorno: **Sistemas basados en Windows**. 

## 1. Instalar Blender 4.2 LTS (una sola vez)

1. Descarga **Blender 4.2 LTS** de [https://www.blender.org/download/lts/4-2/#versions](https://www.blender.org/download/lts/4-2/#versions) — versión **ZIP portable**, NO el instalador. No uses una versión más nueva: los add-ons son estables en las versiones LTS. Descomprime en una ruta corta sin espacios ni OneDrive. Ejemplos de rutas: `C:\blender42` o `C:\Users\<usuario>\Downloads`. En el tutorial de Youtube, descargamos Blender en la carpeta de Descargas/Downloads pero puedes mover ese .zip a cualquier otra carpeta.
2. **Parche OpenGL** (**ATENCIÓN: solo ejecuta este paso si usas Windows en una VM o si al iniciar Blender aparece el error** `A graphics card with support for OpenGL 4.3 is required`): baja el paquete **MSVC** (mesa3d-26.1.6-release-msvc.7z) de [https://github.com/pal1000/mesa-dist-win/releases](https://github.com/pal1000/mesa-dist-win/releases), descomprime y ejecuta **`perappdeploy.cmd`** apuntando a la ruta de la carpeta de Blender que contenga el ejecutable `blender.exe` (x64, Desktop OpenGL). Prestar atención en el vídeo para ejecutar los pasos con precisión.
3. Una vez que el paso anterior crea los archivos parche dentro de la carpeta de Blender, proceder a lanzar Blender **siempre desde PowerShell** y deja esa ventana abierta — ahí aparecen los errores reales:

      ```powershell
      & "[ruta a la carpeta que contiene al blender]\blender.exe"
      ```
   Por ejemplo, en mi caso:

      ```powershell
      & "C:\Users\<usuario>\Downloads\blender-4.2.23-windows-x64\blender-4.2.23-windows-x64\blender.exe"
      ```
   Los mensajes MESA/ZINK en la terminal son normales en la VM.

## 2. Instalar los dos add-ons (una sola vez)

Necesitas exactamente dos, ambos en ZIP compatibles con Blender 4.2:

| Add-on | Para qué | Descarga |
|---|---|---|
| **Blosm** | descargar el mapa OSM con edificios 3D | [blosm_2.7.27.zip](add-ons/blosm_2.7.27.zip) |
| **mitsuba-blender** | exportar la escena al XML que lee Sionna | [mitsuba-blender.zip](add-ons/mitsuba-blender.zip) |

Los ZIP son copias alojadas en el curso, con las versiones probadas contra
Blender 4.2 (ambos add-ons son de licencia libre — GPL/BSD — así que la
redistribución es legítima). 

Para cada uno: **Edit → Preferences → Add-ons → Install...** → seleccionar
el ZIP → activar la casilla. Si el add-on muestra un botón **Install
dependencies**, púlsalo y espera sin interrumpir (Blender parecerá
congelado).

## 3. Descargar el área con Blosm

1. Panel lateral (tecla `N`) → pestaña **Blosm**.
2. Elige el rectángulo del área: para esta clase, del orden de
   **1.5 × 1 km** (como San Isidro). Más grande = la malla pesa, el ray
   tracing tarda y Overpass puede cortar la descarga; en la VM sin GPU el
   visor además se arrastra.
3. Importa con **buildings 3D**. Revisa a ojo: si un edificio clave sale
   con altura absurda (OSM no siempre la tiene), corrígela a mano en
   Blender (`S`, `Z` para escalar en altura).

## 4. Materiales: el paso que decide la física

Sionna asigna propiedades electromagnéticas **por el nombre del
material**. Renombra los materiales de los objetos a nombres de la
librería ITU (los que usamos en el curso):

| Nombre en Blender | Úsalo para |
|---|---|
| `itu_concrete` | paredes de edificios |
| `itu_metal` | techos/estructuras metálicas |
| `itu_brick` | construcciones de ladrillo |
| `itu_medium_dry_ground` | el suelo |

Un material con cualquier otro nombre exporta igual — pero Sionna no
sabrá qué es y la física de reflexión/penetración saldrá mal sin avisar.

## 5. Exportar a Mitsuba — cuidado con los ejes

**File → Export → Mitsuba (.xml)**, y en las opciones del export:

> **Forward = Y, Up = Z**

Este es el error más caro de todo el flujo: si exportas con la convención
por defecto de Mitsuba (Y-up), la ciudad queda **acostada** — y el
notebook no detecta este error (porque no es un error en esencia sino una mala elección de la perspectiva del mapa): corre y devuelve resultados absurdos en silencio.
Síntomas de una escena acostada:

- el radio map sale como una **tira delgada** (una dimensión de ~10
  celdas),
- cobertura "milagrosa" (SINR > 0 en ~99% del área),
- casi no se encuentran trayectos (`trayectos: 1`).

Exporta a una carpeta propia como se sugiere en el vídeo o usando un criterio propio como por ejemplo: `mi_escena/mi_escena.xml` (el export crea `meshes/` al lado; el XML referencia esas mallas con rutas relativas — mueve la carpeta completa, nunca el XML solo).

## 6. Verificar antes de trabajar (30 segundos) - OPCIONAL

En el entorno `ran-design`:

```python
from sionna.rt import load_scene
import numpy as np

scene = load_scene("escenas/mi_escena/mi_escena.xml")
bb = scene.mi_scene.bbox()
print("extensión XYZ:", np.round(np.array(bb.max) - np.array(bb.min), 1))
```

La extensión **chica (decenas de metros, las alturas) debe estar en Z**,
y las dos grandes (cientos de metros) en X e Y. Si la chica está en Y:
la escena está acostada — vuelve al paso 5.

Con eso verificado, apunta el notebook a tu escena y a diseñar.
