"""Ejecuta todas las celdas de codigo del Notebook de diagnostico.

Permite validar de forma reproducible que el Notebook carga e inspecciona los
datasets sin depender de la interfaz grafica de Jupyter.
"""
import json
import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent
NOTEBOOK_PATH = PROJECT_ROOT / "notebooks" / "diagnostico_calidad.ipynb"

if not NOTEBOOK_PATH.exists():
    print(f"No se encontro el notebook en: {NOTEBOOK_PATH}")
    sys.exit(1)

with NOTEBOOK_PATH.open(encoding="utf-8") as file:
    notebook = json.load(file)

namespace = {}
for index, cell in enumerate(notebook["cells"]):
    if cell.get("cell_type") != "code":
        continue
    source = "".join(cell.get("source", []))
    print(f"--- Executing cell {index} (id={cell.get('id')}) ---")
    try:
        exec(compile(source, f"cell_{index}", "exec"), namespace)
        print("OK")
    except Exception:
        import traceback

        traceback.print_exc()
        print("FAILED")
        sys.exit(1)

print("Notebook ejecutado correctamente.")
