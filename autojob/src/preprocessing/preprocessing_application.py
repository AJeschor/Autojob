# File: autojob/src/preprocessing/preprocessing_application.py

# Import necessary libraries and modules
import os
import sys
from tqdm import tqdm

# Set up directory paths and import custom modules
current_directory = os.path.dirname(os.path.abspath(__file__))
project_directory = os.path.dirname(os.path.dirname(current_directory))
sys.path.append(project_directory)

from autojob.src.keywords.keyword_utils import merge_similar_strings, merge_keyterms
from autojob.src.preprocessing.preprocessing_text import process_text
from autojob.src.preprocessing.preprocessing_functions import (
    load_and_preprocess_job_data,
    extract_original_values,
    sanitize_folder_name,
    create_destination_folder_and_copy,
    preprocess_text,
    save_preprocessed_data,
    save_job_information,
    save_textacy_results
)

# Function to apply job processing to a directory of job posts
def apply_job_processing(JOB_POSTS_DIR, PREPROCESSED_DIR):
    """
    Process job posts, extract information, and save preprocessed data.

    Args:
        JOB_POSTS_DIR (str): Path to the directory containing job post files.
        PREPROCESSED_DIR (str): Path to the directory for saving preprocessed data.
    """
    # Create the destination directory if it does not exist
    if not os.path.exists(PREPROCESSED_DIR):
        os.makedirs(PREPROCESSED_DIR)

    # Get list of job post files in the source directory
    job_post_files = [f for f in os.listdir(JOB_POSTS_DIR) if os.path.isfile(os.path.join(JOB_POSTS_DIR, f))]

    # Use tqdm to display a progress bar
    for job_post_file in tqdm(job_post_files, desc="Processing Files", unit="file"):
        src_file_path = os.path.join(JOB_POSTS_DIR, job_post_file)

        try:
            # Load and preprocess job data
            data, preprocessed_description = load_and_preprocess_job_data(src_file_path)

            # Extract original values from job data
            post_id, original_company, original_position_name, original_job_type, original_location, original_salary, original_posting_date, original_url, original_external_apply_link = extract_original_values(data)

            # Sanitize folder name for destination
            sanitized_folder_name = sanitize_folder_name(f"{post_id} - {original_company} - {original_position_name}")
            dest_folder_path = os.path.join(PREPROCESSED_DIR, sanitized_folder_name)

            # Create destination folder and copy original post data
            create_destination_folder_and_copy(src_file_path, dest_folder_path, post_id, original_company, original_position_name)

            # Process text and extract information
            job_info_group, results_group, textacy_results, processed_text = process_text(preprocessed_description)

            # Save preprocessed data to a file
            save_preprocessed_data(dest_folder_path, post_id, data, preprocessed_description, processed_text, results_group)
            
            # Save textacy results to a file
            save_textacy_results(dest_folder_path, post_id, textacy_results)

            # Save job information to a separate file
            save_job_information(dest_folder_path, post_id, data, original_company, original_position_name, original_job_type, original_location, original_salary, original_posting_date, original_url, original_external_apply_link, job_info_group)
            
        except Exception as e:
            # Handle other exceptions here, print the filename causing the error
            print(f"Error in processing file {job_post_file}: {e}")

    print(f"Processed and transferred {len(job_post_files)} files from {JOB_POSTS_DIR} to {PREPROCESSED_DIR}.")
