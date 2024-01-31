# main_processing.py

import os

# Define project directory paths
input_files_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'input_files')
ref_data_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'ref_data')
keywords_dir = os.path.dirname(os.path.abspath(__file))
cleaned_data_dir = os.path.join(keywords_dir, 'cleaned_data')
keyword_results_dir = os.path.join(keywords_dir, 'keyword_results')
