import os
from pathlib import Path
import logging 


# logging.basicConfig(level="INFO", format='[%(asctime)s] : %(message)s : ')
logging.basicConfig(level=20, format='[%(asctime)s] : %(message)s : ')

package_name = "deepClassifier"


list_of_files = [
    ".github/workflows/.gitkeep",
    f"src/{package_name}/__init__.py",
    f"src/{package_name}/components/__init__.py",
    f"src/{package_name}/utils/__init__.py",
    f"src/{package_name}/config/__init__.py",
    f"src/{package_name}/pipeline/__init__.py",
    f"src/{package_name}/entity/__init__.py",
    f"src/{package_name}/constants/__init__.py",
    "configs/config.yaml",
    "dvc.yaml",
    "params.yaml",
    "init_setup.sh",
    "requirements.txt",
    "requirements_dev.txt",
    "setup.py",
    "setup.cfg",
    "pyproject.toml",
    "tox.ini",
    "research/trials.ipynb",
]
#Data Version Control dvc
#tox for testing your projects locally 


for filpath in list_of_files:
    filepath = Path(filpath)
    filedir, filename = os.path.split(filepath)
    if filedir !="":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating Directory : {filename} for file : {filepath}")

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) ==0):
        with open(filepath, "w") as f:
            pass # Create an Empty File
            logging.info(f"Creating empty file : {filename}")
    else:
        logging.info(f"File {filename} already Exist ")

