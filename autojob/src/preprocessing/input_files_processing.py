# File: autojob/src/preprocessing/input_files_processing.py

"""
This script defines functions for preprocessing input JSON files related to job postings.

Functions:
    1. split_input_postings(INPUT_FILES_DIR, ALL_POSTINGS_DIR):
        - Splits input JSON files into individual job postings with unique filenames based on the 'id' field.
        - Parameters:
            - INPUT_FILES_DIR: The directory containing the input JSON files.
            - ALL_POSTINGS_DIR: The directory where the job postings will be stored.

    2. update_job_posts(ALL_POSTINGS_DIR, JOB_POSTS_DIR):
        - Updates job postings based on the latest posting date and URL.
        - Parameters:
            - ALL_POSTINGS_DIR: The directory containing all job postings.
            - JOB_POSTS_DIR: The directory where the updated job postings will be stored.
"""

import os
import json
from datetime import datetime
from dateutil.parser import isoparse
from textacy.preprocessing import normalize
import textacy.preprocessing as tprep

def split_input_postings(INPUT_FILES_DIR, ALL_POSTINGS_DIR):
    """
    Splits input JSON files into individual job postings with unique filenames based on the 'id' field.

    :param INPUT_FILES_DIR: The directory containing the input JSON files.
    :param ALL_POSTINGS_DIR: The directory where the job postings will be stored.
    """
    print("Running split_input_postings function.")
    
    # Ensure the output directory exists; create if not.
    if not os.path.exists(ALL_POSTINGS_DIR):
        os.makedirs(ALL_POSTINGS_DIR)
    
    # Track the count of each unique 'id' to generate unique filenames.
    id_counts = {}
    for filename in os.listdir(INPUT_FILES_DIR):
        if filename.endswith(".json"):
            input_file_path = os.path.join(INPUT_FILES_DIR, filename)
            with open(input_file_path, 'r', encoding='utf-8') as input_file:
                data = json.load(input_file)
            
            for item in data:
                if 'id' in item:
                    id_value = str(item['id'])
                    if id_value not in id_counts:
                        id_counts[id_value] = 0
                    
                    current_count = id_counts[id_value]
                    output_filename = os.path.join(ALL_POSTINGS_DIR, f"{id_value}_{current_count}.json")
                    id_counts[id_value] += 1

                    # Write individual job postings to separate files.
                    with open(output_filename, 'w') as output_file:
                        json.dump(item, output_file, indent=4, default=str)

    print("\nsplit_input_postings function completed.")

def update_job_posts(ALL_POSTINGS_DIR, JOB_POSTS_DIR):
    """
    Updates job postings based on the latest posting date and URL.

    :param ALL_POSTINGS_DIR: The directory containing all job postings.
    :param JOB_POSTS_DIR: The directory where the updated job postings will be stored.
    """
    print("Running update_job_posts function.")
    
    # Ensure the output directory exists; create if not.
    if not os.path.exists(JOB_POSTS_DIR):
        os.makedirs(JOB_POSTS_DIR)
    
    # Iterate through each job posting file in the input directory.
    for filename in os.listdir(ALL_POSTINGS_DIR):
        if filename.endswith("_0.json"):
            file_base = filename.rsplit("_0.json", 1)[0]
            job_posting_path = os.path.join(ALL_POSTINGS_DIR, filename)
            job_db_path = os.path.join(JOB_POSTS_DIR, filename)
            
            latest_posting_date = None
            latest_posting_url = None

            # Iterate through candidate files to find the latest posting date and URL.
            for candidate_file in os.listdir(ALL_POSTINGS_DIR):
                if candidate_file.startswith(file_base) and candidate_file != filename:
                    posting_path = os.path.join(ALL_POSTINGS_DIR, candidate_file)
                    with open(posting_path, 'r', encoding='utf-8') as candidate_file:
                        candidate_data = json.load(candidate_file)
                        candidate_posting_date = candidate_data.get("postingDateParsed")
                        
                        if candidate_posting_date:
                            candidate_posting_date = isoparse(candidate_posting_date)
                            if latest_posting_date is None or candidate_posting_date > latest_posting_date:
                                latest_posting_date = candidate_posting_date
                                latest_posting_url = str(candidate_data.get("url"))

            # Update the job posting with the latest URL.
            if latest_posting_url:
                with open(job_posting_path, 'r', encoding='utf-8') as job_posting_file:
                    job_posting_data = json.load(job_posting_file)
                    job_posting_data["url"] = latest_posting_url

                with open(job_db_path, 'w', encoding='utf-8') as job_db_file:
                    json.dump(job_posting_data, job_db_file, indent=4, default=str)
            else:
                # If no URL is found, copy the existing file.
                with open(job_posting_path, 'rb') as source_file, open(job_db_path, 'wb') as destination_file:
                    while True:
                        chunk = source_file.read(1024)
                        if not chunk:
                            break
                        destination_file.write(chunk)
    
    print("\nJob post update completed.")
