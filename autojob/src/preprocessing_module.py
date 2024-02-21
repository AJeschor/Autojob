# autojob/src/preprocessing_module.py

import os
import sys
from autojob.src.preprocessing.preprocessing_application import apply_job_processing
from autojob.src.preprocessing.input_files_processing import update_job_posts, split_input_postings

current_directory = os.path.dirname(os.path.abspath(__file__))
project_directory = os.path.dirname(current_directory)
sys.path.append(project_directory)

INPUT_FILES_DIR = os.path.join(project_directory, 'input_files')
ALL_POSTINGS_DIR = os.path.join(project_directory, 'src', 'tmp', 'all_postings')
JOB_POSTS_DIR = os.path.join(project_directory, 'src', 'tmp', 'job_posts')
PREPROCESSED_DIR = os.path.join(project_directory, 'src', 'tmp', 'preprocessed_files')

def prompt_to_run_function(func, args, func_name, message):
    user_input = input(f"{message} (y/n): ").strip().lower()
    if user_input == 'y':
        func(*args)
        print(f"{func_name} executed successfully!")
    elif user_input == 'n':
        print(f"{func_name} skipped.")
    else:
        print("Invalid input. Skipping function.")

def preprocessing_operations():
    split_args = (INPUT_FILES_DIR, ALL_POSTINGS_DIR)
    update_args = (ALL_POSTINGS_DIR, JOB_POSTS_DIR)
    apply_args = (JOB_POSTS_DIR, PREPROCESSED_DIR)

    prompt_to_run_function(split_input_postings, split_args, "split_input_postings", "Split the bulk input files?")
    prompt_to_run_function(update_job_posts, update_args, "update_job_posts", "Update the job post database from the split input files?")
    prompt_to_run_function(apply_job_processing, apply_args, "apply_processing", "Apply processing and keyword extraction to job posts?")

if __name__ == "__main__":
    preprocessing_operations()
