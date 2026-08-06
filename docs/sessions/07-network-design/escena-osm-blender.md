---
title: "Guía: crear tu escena OSM con Blender"
description: "De OpenStreetMap a un XML de Mitsuba listo para Sionna RT: instalar Blender 4.2 en la VM Windows, descargar el mapa con Blosm, asignar materiales ITU y exportar con los ejes correctos."
---

# Guía: crear tu escena de ciudad para el notebook

Esta guía produce lo único que el notebook de diseño necesita de ti: una
carpeta con un archivo `.xml` y sus mallas (`meshes/`), que se carga con

```python
scene = load_scene("escenas/mi_escena/mi_escena.xml")
```

El proceso completo está demostrado en video —
**[tutorial en YouTube](https://youtu.be/PIdn1R7FSrg?si=V8-HVuCvWGZG6v39)** —
y aquí en pasos verificables. Entorno: la **VM Windows (VirtualBox)** del
curso, sin GPU. Los pasos de instalación detallados (con solución de
problemas) están en la
[guía extendida](borrador/blender-4.2-vm-windows.md).

## 1. Instalar Blender 4.2 LTS (una sola vez)

1. Descarga **Blender 4.2 LTS** de `blender.org/download/lts` — versión
   **ZIP portable**, no el instalador. No uses una versión más nueva: los
   add-ons se prueban contra las LTS.
2. Descomprime en una ruta corta sin espacios ni OneDrive: `C:\blender42`.
3. **Parche OpenGL** (obligatorio en la VM): baja el paquete **MSVC** de
   `github.com/pal1000/mesa-dist-win` (Releases), descomprime y ejecuta
   **`perappdeploy.cmd`** apuntando a `C:\blender42` (x64, Desktop
   OpenGL). Sin esto Blender no abre en VirtualBox.
4. Lanza Blender **siempre desde PowerShell** y deja esa ventana abierta —
   ahí aparecen los errores reales:

   ```powershell
   & "C:\blender42\blender.exe"
   ```

   Los mensajes MESA/ZINK en la terminal son normales en la VM.

## 2. Instalar los dos add-ons (una sola vez)

Necesitas exactamente dos, ambos en ZIP compatibles con Blender 4.2:

| Add-on | Para qué | Dónde |
|---|---|---|
| **Blosm** | descargar el mapa OSM con edificios 3D | gumroad (blosm) |
| **mitsuba-blender** | exportar la escena al XML que lee Sionna | github.com/mitsuba-renderer/mitsuba-blender |

Para cada uno: **Edit → Preferences → Add-ons → Install...** → seleccionar
el ZIP → activar la casilla. Si el add-on muestra un botón **Install
dependencies**, púlsalo y espera sin interrumpir (Blender parecerá
congelado). Marca verde = listo. Si algo falla, la
[guía extendida](borrador/blender-4.2-vm-windows.md) tiene la tabla de
problemas frecuentes.

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
notebook no truena: corre y devuelve resultados absurdos en silencio.
Síntomas de una escena acostada:

- el radio map sale como una **tira delgada** (una dimensión de ~10
  celdas),
- cobertura "milagrosa" (SINR > 0 en ~99% del área),
- casi no se encuentran trayectos (`trayectos: 1`).

Exporta a una carpeta propia: `mi_escena/mi_escena.xml` (el export crea
`meshes/` al lado; el XML referencia esas mallas con rutas relativas —
mueve la carpeta completa, nunca el XML solo).

## 6. Verificar antes de trabajar (30 segundos)

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
