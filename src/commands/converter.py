import nbformat

from nbconvert import PythonExporter
from src.config.settings import BASE_DIR
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent.parent
def convert_ipynb_to_py(notebook_path, output_path):
    with open(notebook_path) as nb_file:
        nb_contents = nb_file.read()
        notebook = nbformat.reads(nb_contents, as_version=4)
    
    exporter = PythonExporter()
    source_code, _ = exporter.from_notebook_node(notebook)
    source_code.replace("data/F1_training.csv", str(BASE_DIR / "algo" / "data" / "F1_training.csv"))
    source_code.replace("model.pickle", str(BASE_DIR / "algo" / "model.pickle"))
    with open(output_path, "w") as py_file:
        py_file.write(source_code)


notebook_path = "src/algo/training.ipynb"
output_path = "src/algo/converted_script.py"
convert_ipynb_to_py(notebook_path, output_path)
