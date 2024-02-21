# File: autojob/src/preprocessing/preprocessing_functions.py

import os
import re
import sys
import json
import shutil
import spacy
import textacy.preprocessing as tprep
from spacy.lang.en.stop_words import STOP_WORDS

# Set up directory paths and import custom modules
current_directory = os.path.dirname(os.path.abspath(__file__))
project_directory = os.path.dirname(os.path.dirname(current_directory))
sys.path.append(project_directory)

from autojob.src.preprocessing.acronyms import acronym_list
from autojob.src.preprocessing.contractions_dict import all_contractions
from autojob.src.preprocessing.custom_stopwords import custom_stop_word_list
from autojob.src.keywords.keyword_utils import merge_similar_strings, merge_keyterms
from autojob.src.preprocessing.preprocessing_utils import (
    extract_spacy_info,
    extract_string_info,
    Xlator,
    filter_annotations,
    convert_to_serializable,
    extract_substituted_terms,
    EXCLUDED_ENTITY_TYPES,
    sanitize_folder_name
)

def preprocess_text(input_text):
    """
    Preprocesses the input text by translating acronyms, contractions, and normalizing.

    Args:
        input_text (str): Input text for preprocessing.

    Returns:
        str: Preprocessed text.
    """
    # Initialize Xlator with the acronym_list and translate acronyms in the input_text
    acronym_translator = Xlator(acronym_list)
    translated_acronyms_text = acronym_translator(input_text)

    # Initialize Xlator with the all_contractions and translate contractions in the text
    contractions_translator = Xlator(all_contractions)
    translated_contractions_text = contractions_translator(translated_acronyms_text)

    # Normalize text using textacy (as per your original implementation)
    preprocessed_text = tprep.normalize.bullet_points(translated_contractions_text)
    preprocessed_text = tprep.normalize.unicode(preprocessed_text)
    preprocessed_text = tprep.normalize.quotation_marks(preprocessed_text)
    preprocessed_text = tprep.normalize.hyphenated_words(preprocessed_text)
    preprocessed_text = tprep.normalize.repeating_chars(preprocessed_text, chars="-")
    preprocessed_text = preprocessed_text.replace('\n', ' ').replace('\r', '').replace('*', '')
    preprocessed_text = tprep.normalize.whitespace(preprocessed_text)

    # Return the preprocessed text
    return preprocessed_text

def postprocess_text(text):
    """
    Postprocesses the text by applying various transformations and filtering.

    Args:
        text (str): Text for postprocessing.

    Returns:
        str: Postprocessed text.
    """
    # Apply various postprocessing steps using textacy functions and regular expressions
    text = tprep.remove.accents(text)
    text = tprep.replace.currency_symbols(text, repl=" ")
    text = tprep.replace.emails(text, repl=" ")
    text = tprep.replace.emojis(text, repl=" ")
    text = tprep.replace.hashtags(text, repl=" ")
    text = tprep.replace.phone_numbers(text, repl=" ")
    text = tprep.replace.numbers(text, repl=" ")
    text = tprep.replace.urls(text, repl=" ")
    text = tprep.replace.user_handles(text, repl=" ")
    text = tprep.remove.html_tags(text)
    text = re.sub(r"[\S]+\.(net|com|org|info|edu|gov|uk|de|ca|jp|fr|au|us|ru|ch|it|nel|se|no|es|mil)[\S]*\s?", '', text)
    text = tprep.remove.punctuation(text, only=r',":;!?%©@*()-[]{}/#%†')
    text = tprep.normalize.unicode(text)    
    # Replace contractions
    for key, value in all_contractions.items():
        text = re.sub(re.escape(key), value, text, flags=re.IGNORECASE)
    
    # Normalize quotation marks and whitespace
    text = tprep.normalize.quotation_marks(text)
    text = tprep.normalize.whitespace(text)
    
    # Remove both Spacy and custom stopwords
    spacy_stopwords = STOP_WORDS
    custom_stopwords = set(custom_stop_word_list)
    all_stopwords = spacy_stopwords.union(custom_stopwords)
    
    # Filter out stopwords and remove newlines
    text = ' '.join(word for word in text.split() if word.lower() not in all_stopwords)
    text = text.replace('\n', ' ').replace('\r', '')
    
    return text

# Function to load and preprocess job post data
def load_and_preprocess_job_data(file_path):
    """
    Load job post data from a file, preprocess the description, and return the data.

    Args:
        file_path (str): Path to the job post file.

    Returns:
        tuple: A tuple containing job data and preprocessed description.
    """
    with open(file_path, 'r') as f:
        data = json.load(f)

    description_text = data.get('description', '')
    preprocessed_description = preprocess_text(description_text)

    return data, preprocessed_description

# Function to extract original values from job post data
def extract_original_values(data):
    """
    Extract original values from job post data.

    Args:
        data (dict): Job post data.

    Returns:
        tuple: A tuple containing various original values.
    """
    post_id = data.get('id', 'unknown')
    original_company = data.get('company', 'unknown')
    original_position_name = data.get('positionName', 'unknown')
    original_job_type = data.get('jobType', 'unknown')
    original_location = data.get('location', 'unknown')
    original_salary = data.get('salary', 'unknown')
    original_posting_date = data.get('postingDateParsed', 'unknown')
    original_url = data.get('url', 'unknown')
    original_external_apply_link = data.get('externalApplyLink', 'unknown')

    return (
        post_id, original_company, original_position_name,
        original_job_type, original_location, original_salary,
        original_posting_date, original_url, original_external_apply_link
    )

# Function to create destination folder and copy original post data
def create_destination_folder_and_copy(src_file_path, dest_folder_path, post_id, original_company, original_position_name):
    """
    Create destination folder, copy the original post data to the destination.

    Args:
        src_file_path (str): Path to the source file.
        dest_folder_path (str): Path to the destination folder.
        post_id (str): Unique identifier for the job post.
        original_company (str): Original company name.
        original_position_name (str): Original position name.
    """
    if not os.path.exists(dest_folder_path):
        os.makedirs(dest_folder_path)

    dest_original_file_path = os.path.join(dest_folder_path, f"{post_id} - original_post.json")
    shutil.copy(src_file_path, dest_original_file_path)

# Function to save preprocessed data to a file
def save_preprocessed_data(dest_folder_path, post_id, data, preprocessed_description, processed_text, results_group):
    """
    Save preprocessed data to a file.

    Args:
        dest_folder_path (str): Path to the destination folder.
        post_id (str): Unique identifier for the job post.
        data (dict): Job post data.
        preprocessed_description (str): Preprocessed job description.
        processed_text (str): Processed job description.
        results_group (dict): Extracted results group.
    """
    dest_preprocessed_file_path = os.path.join(dest_folder_path, f"{post_id} - preprocessed.json")

    # Remove usage of merged_keywords
    data.pop('company', None)
    data.pop('positionName', None)
    data.pop('jobType', None)
    data.pop('location', None)
    data.pop('salary', None)
    data.pop('postingDateParsed', None)
    data.pop('url', None)
    data.pop('externalApplyLink', None)

    data['preprocessed_description'] = preprocessed_description
    data['processed_description'] = processed_text
    data['results_group'] = results_group

    with open(dest_preprocessed_file_path, 'w') as f:
        json.dump(data, f, indent=4, default=convert_to_serializable)


# Function to save job information to a separate file
def save_job_information(dest_folder_path, post_id, data, original_company, original_position_name, original_job_type, original_location, original_salary, original_posting_date, original_url, original_external_apply_link, job_info_group):
    """
    Save job information to a separate file.

    Args:
        dest_folder_path (str): Path to the destination folder.
        post_id (str): Unique identifier for the job post.
        data (dict): Original job post data.
        original_company (str): Original company name.
        original_position_name (str): Original position name.
        original_job_type (str): Original job type.
        original_location (str): Original job location.
        original_salary (str): Original job salary.
        original_posting_date (str): Original posting date.
        original_url (str): Original job URL.
        original_external_apply_link (str): Original external apply link.
        job_info_group (dict): Extracted job information group.
    """
    dest_job_info_file_path = os.path.join(dest_folder_path, f"{post_id} - job_info.json")

    job_info_data = {
        'id': post_id,
        'company': original_company,
        'positionName': original_position_name,
        'jobType': original_job_type,
        'location': original_location,
        'salary': original_salary,
        'postingDateParsed': original_posting_date,
        'url': original_url,
        'externalApplyLink': original_external_apply_link,
        'job_info_group': job_info_group,
        'companyDescription': data.get('companyDescription', 'unknown'),
        'description': data.get('description', 'unknown')
    }

    with open(dest_job_info_file_path, 'w') as f:
        json.dump(job_info_data, f, indent=4, default=convert_to_serializable)

def save_textacy_results(dest_folder_path, post_id, textacy_results):
    """
    Save textacy_results data to a file.

    Args:
        dest_folder_path (str): Path to the destination folder.
        post_id (str): Unique identifier for the job post.
        textacy_results (dict): Extracted textacy results.
    """
    # Merge keyterms
    merged_keyterms = merge_keyterms(textacy_results)
    
    # Merge similar strings
    merged_strings = merge_similar_strings(merged_keyterms)

    # Create the file path
    textacy_results_file_path = os.path.join(dest_folder_path, f"{post_id} - textacy_results.json")

    # Write the merged and cleaned data to the file
    with open(textacy_results_file_path, 'w') as f:
        json.dump(merged_strings, f, indent=4)

