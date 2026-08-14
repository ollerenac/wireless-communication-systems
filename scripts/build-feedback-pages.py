#!/usr/bin/env python3
"""Genera las páginas de retroalimentación como HTML suelto bajo docs/f/.

Se emiten como .html (no .md) a propósito: MkDocs copia los archivos que no son
Markdown sin procesarlos, así que estas páginas no entran al índice de búsqueda,
ni al sitemap.xml, ni a la navegación. La única forma de llegar es con la URL
completa, que lleva un código aleatorio.

Uso:
    python scripts/build-feedback-pages.py            # genera (códigos estables)
    python scripts/build-feedback-pages.py --rotar    # fuerza códigos nuevos
"""
from __future__ import annotations

import argparse
import json
import re
import secrets
import sys
import unicodedata
from pathlib import Path

import markdown

RAIZ = Path(__file__).resolve().parent.parent
ENTREGAS = RAIZ / "exams" / "final-01"
SALIDA = RAIZ / "docs" / "f"
MAPA = ENTREGAS / ".enlaces.json"  # nombre -> código, para no rotar sin querer
BASE_URL = "https://ollerenac.github.io/wireless-communication-systems/f"

DIGITOS_CODIGO = 12

PLANTILLA = """<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="robots" content="noindex, nofollow, noarchive, nosnippet">
<title>{titulo}</title>
<style>
  :root {{
    --fondo: #ffffff; --texto: #1f2328; --tenue: #59636e;
    --borde: #d1d9e0; --acento: #1c6bba; --suave: #f6f8fa;
  }}
  @media (prefers-color-scheme: dark) {{
    :root {{
      --fondo: #0d1117; --texto: #e6edf3; --tenue: #9198a1;
      --borde: #30363d; --acento: #6cb0ff; --suave: #161b22;
    }}
  }}
  * {{ box-sizing: border-box; }}
  body {{
    margin: 0; padding: 2.5rem 1.25rem 5rem;
    background: var(--fondo); color: var(--texto);
    font: 16px/1.65 -apple-system, "Segoe UI", Roboto, "Helvetica Neue", sans-serif;
  }}
  main {{ max-width: 46rem; margin: 0 auto; }}
  .aviso {{
    border: 1px solid var(--borde); border-left: 3px solid var(--acento);
    background: var(--suave); padding: .7rem .9rem; border-radius: 5px;
    font-size: .87rem; color: var(--tenue); margin-bottom: 2.5rem;
  }}
  h1 {{ font-size: 1.6rem; line-height: 1.25; margin: 0 0 1.2rem; }}
  h2 {{
    font-size: 1.18rem; margin: 2.4rem 0 .8rem;
    padding-bottom: .3rem; border-bottom: 1px solid var(--borde);
  }}
  h3 {{ font-size: 1rem; margin: 1.8rem 0 .6rem; }}
  p, li {{ margin: 0 0 .85rem; }}
  code {{
    background: var(--suave); border: 1px solid var(--borde);
    border-radius: 4px; padding: .1em .35em; font-size: .875em;
  }}
  .tabla {{ overflow-x: auto; margin: 1.2rem 0; }}
  table {{ border-collapse: collapse; width: 100%; font-size: .92rem; }}
  th, td {{ border: 1px solid var(--borde); padding: .45rem .7rem; text-align: left; }}
  th {{ background: var(--suave); font-weight: 600; }}
  hr {{ border: 0; border-top: 1px solid var(--borde); margin: 2.5rem 0; }}
  blockquote {{
    margin: 1.2rem 0; padding-left: 1rem;
    border-left: 3px solid var(--borde); color: var(--tenue);
  }}
  footer {{
    margin-top: 4rem; padding-top: 1rem; border-top: 1px solid var(--borde);
    font-size: .82rem; color: var(--tenue);
  }}
</style>
</head>
<body>
<main>
<div class="aviso">
  Página personal y no listada. Su dirección es única para ti — no aparece en el
  menú ni en el buscador del curso. Evita reenviarla.
</div>
{cuerpo}
<footer>
  Comunicaciones Inalámbricas · Retroalimentación del examen final ·
  ¿Dudas sobre la calificación? Escríbeme y la revisamos.
</footer>
</main>
</body>
</html>
"""


def slug(nombre: str) -> str:
    s = unicodedata.normalize("NFKD", nombre).encode("ascii", "ignore").decode().lower()
    return re.sub(r"-+", "-", re.sub(r"[^a-z0-9]+", "-", s)).strip("-")


def codigo() -> str:
    """Código numérico aleatorio, sin ceros a la izquierda."""
    return str(secrets.randbelow(9 * 10 ** (DIGITOS_CODIGO - 1)) + 10 ** (DIGITOS_CODIGO - 1))


def titulo_de(md: str, respaldo: str) -> str:
    m = re.search(r"^#\s+(.+)$", md, re.M)
    return m.group(1).strip() if m else respaldo


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--rotar", action="store_true",
                    help="genera códigos nuevos e invalida los enlaces anteriores")
    args = ap.parse_args()

    fuentes = sorted(ENTREGAS.glob("*/feedback.md"))
    if not fuentes:
        print("No hay feedback.md en", ENTREGAS, file=sys.stderr)
        return 1

    mapa = {} if args.rotar or not MAPA.exists() else json.loads(MAPA.read_text())
    SALIDA.mkdir(parents=True, exist_ok=True)
    for viejo in SALIDA.glob("*.html"):
        viejo.unlink()

    md = markdown.Markdown(extensions=["tables", "attr_list", "sane_lists"])
    enlaces = []
    for fuente in fuentes:
        carpeta = fuente.parent.name
        texto = fuente.read_text()
        titulo = titulo_de(texto, carpeta.title())

        base = slug(carpeta.replace("EXAMEN FINAL", ""))
        mapa.setdefault(carpeta, codigo())
        nombre_archivo = f"{base}-{mapa[carpeta]}.html"

        md.reset()
        cuerpo = md.convert(texto)
        # envolver tablas para que puedan desplazarse en pantallas angostas
        cuerpo = cuerpo.replace("<table>", '<div class="tabla"><table>')
        cuerpo = cuerpo.replace("</table>", "</table></div>")

        (SALIDA / nombre_archivo).write_text(
            PLANTILLA.format(titulo=titulo, cuerpo=cuerpo))
        enlaces.append((carpeta, f"{BASE_URL}/{nombre_archivo}"))

    MAPA.write_text(json.dumps(mapa, ensure_ascii=False, indent=1))

    # robots.txt: refuerzo por si algún enlace se filtra a un buscador
    robots = RAIZ / "docs" / "robots.txt"
    regla = "User-agent: *\nDisallow: /wireless-communication-systems/f/\n"
    if not robots.exists() or "/f/" not in robots.read_text():
        robots.write_text(regla)

    print(f"{len(enlaces)} páginas en {SALIDA.relative_to(RAIZ)}\n")
    for carpeta, url in enlaces:
        print(f"  {carpeta[:30]:32s} {url}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
