import os, shutil
from init_venv import venv_path

shutil.rmtree(venv_path) if os.path.exists(venv_path) else None