import os
import shutil

# Constants
EXCLUDED_DIRECTORIES = {'tmp', 'ref', '.git', '__pycache__', 'dist', 'build', '*.egg-info'}
CONFIG_FILE = 'config.ini'

def copy_config_to_py_directories(root_dir):
    for dirpath, dirnames, filenames in os.walk(root_dir, topdown=True):
        # Exclude directories specified in EXCLUDED_DIRECTORIES and their subdirectories
        dirnames[:] = [d for d in dirnames if d not in EXCLUDED_DIRECTORIES]
        
        # Check if the directory contains any .py files or __init__.py
        if any(fname.endswith('.py') or fname == '__init__.py' for fname in filenames):
            # Copy config.ini to this directory
            config_dest = os.path.join(dirpath, CONFIG_FILE)
            if not os.path.exists(config_dest):
                shutil.copy(CONFIG_FILE, config_dest)
                print(f"Copied {CONFIG_FILE} to {dirpath}")

# Usage: Provide the root directory where you want to start searching for .py files
copy_config_to_py_directories('.')
