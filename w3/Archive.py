import os
import zipfile
from pathlib import Path
from glob import glob

with zipfile.ZipFile("main.zip") as zip:
    zip.extractall()

py_dir = list()

path = Path('main')
py_file = list(glob("**/*.py"))

for path in py_file:
    path = str(path).split("//")
    py_dir.append(path[0])

py_dir = sorted(py_dir)

for ind, dir_name in enumerate(py_dir):
    print(str(ind), dir_name)
