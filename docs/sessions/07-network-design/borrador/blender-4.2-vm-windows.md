# Instalar Blender 4.2 LTS y sus add-ons en una VM Windows (VirtualBox)

Procedimiento probado en una máquina virtual Windows sobre VirtualBox, donde no hay
aceleración OpenGL por hardware.

## Antes de empezar

- **No hace falta instalar Python.** Blender trae el suyo incluido (versión 3.11 en
  Blender 4.2). Los add-ons instalan sus paquetes dentro de ese Python, no en el del
  sistema.
- **Da igual Windows 10 u 11.** El procedimiento es idéntico en ambos.
- Necesitas unos 5 GB libres y un descompresor que abra archivos `.7z` (7-Zip).

---

## Paso 1 — Descargar Blender 4.2 LTS

Ve a `blender.org/download/lts` y baja la versión **4.2 LTS** para Windows, en formato
**ZIP (portable)**, no el instalador.

No uses la versión más reciente de Blender. Los add-ons se prueban contra las versiones
LTS, y usar una más nueva es la causa más común de fallos.

Descomprime el ZIP en una ruta corta y sin espacios, por ejemplo:

```
C:\blender42
```

Evita el Escritorio, Descargas y cualquier carpeta sincronizada con OneDrive.

Verifica que exista `C:\blender42\blender.exe`.

---

## Paso 2 — Parche de OpenGL (Mesa3D)

Blender exige OpenGL 4.3. VirtualBox no se lo da a Windows, así que sin este paso
Blender no abre. Mesa lo reemplaza por un renderizador que usa el procesador.

1. Entra a `github.com/pal1000/mesa-dist-win` y abre la sección **Releases**.
2. Baja el paquete **MSVC** más reciente (archivo `.7z`).
3. Descomprímelo en una carpeta temporal.
4. Ejecuta **`perappdeploy.cmd`** (NO uses `systemwidedeploy.cmd`, que da problemas
   dentro de VirtualBox).
5. Cuando pregunte, responde:
   - Carpeta del programa: `C:\blender42`
   - Arquitectura: **x64**
   - Driver: **Desktop OpenGL**

Este parche solo afecta a esa carpeta de Blender. Si instalas otra versión de Blender
después, hay que repetirlo para ella.

---

## Paso 3 — Comprobar que Blender abre

Abre PowerShell y ejecuta:

```powershell
& "C:\blender42\blender.exe"
```

Lánzalo así, desde PowerShell, y no cierres esa ventana: los errores de los add-ons
aparecen ahí. Es la única forma de ver qué falla realmente.

Si Blender abre, el paso 2 salió bien. Verás mensajes sobre MESA o ZINK en la terminal;
son normales y puedes ignorarlos.

> Dentro de Blender también puedes abrir esa consola con
> **Window → Toggle System Console**.

---

## Paso 4 — Instalar el add-on

1. Descarga el ZIP del add-on. **Revisa que la página diga que soporta Blender 4.2.**
   Un ZIP viejo fallará aunque todo lo demás esté bien.
2. En Blender: **Edit → Preferences → Add-ons → Install...**
3. Selecciona el ZIP y pulsa **Install Add-on**.
4. Búscalo por nombre y marca la casilla para activarlo.

Si ya tenías otra versión del mismo add-on, desinstálala primero.

---

## Paso 5 — Instalar las dependencias del add-on

Algunos add-ons necesitan paquetes de Python adicionales. Despliega el add-on en
Preferences: si aparece un botón **Install dependencies**, púlsalo.

Blender parecerá congelado mientras descarga. **No lo interrumpas.**

Cuando termine debe aparecer una marca de verificación verde.

### Si el botón falla

Un mensaje como *"Failed to install... return code 1"* no dice nada útil. Instala el
paquete a mano para ver el error verdadero:

```powershell
$py = "C:\blender42\4.2\python\bin\python.exe"
& $py -m pip install NOMBRE_DEL_PAQUETE
```

Detalles importantes:

- El `&` inicial es obligatorio cuando el comando está en una variable.
- Usa **ese** `python.exe`, el que está dentro de la carpeta de Blender. Si usas otro,
  el paquete se instala donde Blender no lo va a encontrar.

Para ver qué versiones hay disponibles para ese Python:

```powershell
& $py -m pip index versions NOMBRE_DEL_PAQUETE
```

Si la versión que el add-on necesita no aparece en esa lista, no existe compilada para
ese Python. Ese es el problema, y no se arregla actualizando pip.

---

## Paso 6 — Comprobar que funcionó

Con el add-on activo y la marca verde, busca sus opciones en los menús de Blender
(normalmente en **File → Import** / **File → Export**, o como motor de render).

Haz una prueba mínima antes de trabajar en serio: exporta o importa la escena por
defecto y mira la terminal de PowerShell. Si no hay errores, ya está listo.

---

## Problemas frecuentes

| Síntoma | Causa | Solución |
|---|---|---|
| "A graphics card with support for OpenGL 4.3 is required" | Falta el parche Mesa | Paso 2 |
| "Failed to install... return code 1" | No existe versión compilada del paquete para ese Python | Instalar con pip a mano (Paso 5) para ver el error |
| "Found pip X v1.2.3. Supported version is v0.9.8" | El add-on espera otra versión | Usar un add-on más nuevo, o bajar la versión del paquete |
| El add-on no muestra nada y el botón está gris | Falló al registrarse | Ver el traceback en la terminal |
| `ImportError: cannot import name ...` | El add-on es de una versión anterior del paquete | Instalar la versión exacta que el add-on pide |
| `MESA: error: ZINK: vkCreateInstance failed` | Mesa buscó Vulkan y no lo halló | Ignorar, es normal en una VM |

---

## Nota sobre rendimiento

Sin GPU, todo el dibujado corre en el procesador. Blender abre y funciona, pero el
visor va lento con escenas grandes. Trabaja con pocos objetos y mallas ligeras.

Para trabajo pesado, las alternativas son ejecutar Blender directamente en el equipo
anfitrión, o asignarle una GPU real a la máquina virtual (passthrough).
