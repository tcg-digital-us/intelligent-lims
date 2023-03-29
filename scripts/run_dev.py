import sys
import os
import subprocess
from init_venv import venv_path, site_packages, pip_cmd, python_cmd

# Install the required packages
subprocess.run([pip_cmd, "install", "-r", "build/requirements.txt"])

# Update the sys.path to include the virtual environment's site-packages
sys.path.insert(0, site_packages)

# Now you can import packages installed in the virtual environment
# import some_package

# Run your main script
subprocess.run([python_cmd, 'build/src/main.py'])
