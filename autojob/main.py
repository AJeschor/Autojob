# autojob/main.py

import sys
import os

current_directory = os.path.dirname(os.path.abspath(__file__))
project_directory = os.path.dirname(current_directory)
sys.path.append(project_directory)

from autojob.src.preprocessing_module import preprocessing_operations
from autojob.src.webscraper_module import run_webscraper_once_prompt
# from autojob.src.keyword_module import run_keyword_functions

if __name__ == "__main__":
    run_webscraper_once_prompt()
    preprocessing_operations()
