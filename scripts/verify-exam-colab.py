#!/usr/bin/env python3
"""Smoke-test the published exam notebook and its selectable scene archives."""

from __future__ import annotations

import argparse
import json
import os
import re
import tempfile
import xml.etree.ElementTree as ET
from pathlib import Path
from zipfile import ZipFile


ROOT = Path(__file__).resolve().parents[1]
NOTEBOOK = ROOT / "docs/sessions/07-network-design/examen-alumno.ipynb"
SCENES = ROOT / "docs/sessions/07-network-design/escenas"
EXAM_PAGE = ROOT / "docs/exams/examen-diseno-red.md"
MKDOCS = ROOT / "mkdocs.yml"
SCENE_NAMES = ("jesus-maria-01", "san-isidro-01")
COLAB_URL = (
    "https://colab.research.google.com/github/ollerenac/"
    "wireless-communication-systems/blob/main/docs/sessions/"
    "07-network-design/examen-alumno.ipynb"
)


def load_setup_cell() -> str:
    notebook = json.loads(NOTEBOOK.read_text(encoding="utf-8"))
    assert notebook["nbformat"] == 4, "el notebook no usa nbformat 4"
    code_cells = [cell for cell in notebook["cells"] if cell["cell_type"] == "code"]
    assert all(
        cell.get("execution_count") is None and not cell.get("outputs", [])
        for cell in code_cells
    ), "el notebook publicado conserva outputs"

    setup = next(
        "".join(cell["source"])
        for cell in code_cells
        if "ESCENARIOS =" in "".join(cell["source"])
    )
    selector = '# @param ["jesus-maria-01", "san-isidro-01"]'
    assert selector in setup, "falta el selector desplegable de mapas para Colab"
    assert all(name in setup for name in SCENE_NAMES), "selector de mapas incompleto"
    return setup


def validate_archive(scene_name: str) -> None:
    archive = SCENES / f"{scene_name}.zip"
    expected_xml = f"{scene_name}/{scene_name}.xml"
    assert archive.is_file(), f"falta {archive.relative_to(ROOT)}"

    with ZipFile(archive) as bundle:
        members = bundle.namelist()
        assert bundle.testzip() is None, f"ZIP corrupto: {archive.name}"
        assert expected_xml in members, f"{archive.name} no contiene {expected_xml}"
        assert all(
            not Path(member).is_absolute() and ".." not in Path(member).parts
            for member in members
        ), f"{archive.name} contiene una ruta insegura"


def execute_download_flow(setup: str, scene_name: str, load_with_sionna: bool) -> None:
    local_setup = re.sub(
        r'^ESCENA = .+$',
        f'ESCENA = "{scene_name}"',
        setup,
        count=1,
        flags=re.MULTILINE,
    )
    public_url = (
        'url = ("https://ollerenac.github.io/wireless-communication-systems/"\n'
        '           f"sessions/07-network-design/escenas/{ESCENA}.zip")'
    )
    local_url = f'url = f"file://{SCENES.as_posix()}/{{ESCENA}}.zip"'
    assert public_url in local_setup, "cambió la URL pública esperada de los mapas"
    local_setup = local_setup.replace(public_url, local_url, 1)

    with tempfile.TemporaryDirectory(prefix=f"exam-{scene_name}-") as directory:
        previous = Path.cwd()
        os.chdir(directory)
        try:
            namespace: dict[str, object] = {}
            exec(compile(local_setup, str(NOTEBOOK), "exec"), namespace)
            xml_path = Path(namespace["ruta_xml"])
            assert xml_path.is_file(), f"la preparación no extrajo {xml_path}"

            tree = ET.parse(xml_path)
            references = [
                node.attrib["value"]
                for node in tree.findall('.//string[@name="filename"]')
            ]
            missing = [path for path in references if not (xml_path.parent / path).is_file()]
            assert not missing, f"{scene_name}: archivos referenciados ausentes: {missing[:3]}"

            if load_with_sionna:
                from sionna.rt import load_scene

                scene = load_scene(str(xml_path))
                assert len(scene.objects) > 0, f"Sionna cargó {scene_name} sin objetos"
        finally:
            os.chdir(previous)


def validate_publication_links() -> None:
    page = EXAM_PAGE.read_text(encoding="utf-8")
    nav = MKDOCS.read_text(encoding="utf-8")
    assert COLAB_URL in page, "la página del examen no enlaza a Colab"
    assert "exams/examen-diseno-red.md" in nav, "el examen no está en la navegación"
    for scene_name in SCENE_NAMES:
        assert f"escenas/{scene_name}.zip" in page, f"falta enlace de {scene_name}"


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--with-sionna",
        action="store_true",
        help="Carga también cada XML con Sionna RT (requiere sionna-rt).",
    )
    args = parser.parse_args()

    setup = load_setup_cell()
    validate_publication_links()
    for scene_name in SCENE_NAMES:
        validate_archive(scene_name)
        execute_download_flow(setup, scene_name, args.with_sionna)
        print(f"{scene_name}: descarga, extracción y XML verificados")
    print("Examen Colab: verificación completa")


if __name__ == "__main__":
    main()
