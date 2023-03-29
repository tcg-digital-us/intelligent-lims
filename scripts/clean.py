import os, shutil
from init_venv import venv_path

src_cache_path = "build/src/__pycache__"
scripts_cache_path = "scripts/__pycache__"

shutil.rmtree(venv_path) if os.path.exists(venv_path) else None
shutil.rmtree(src_cache_path) if os.path.exists(src_cache_path) else None
shutil.rmtree(scripts_cache_path) if os.path.exists(scripts_cache_path) else None