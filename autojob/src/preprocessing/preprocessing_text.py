# File: autojob/src/preprocessing/preprocessing_text.py

# Import necessary libraries and modules
import os
import sys

# Set up directory paths and import custom modules
current_directory = os.path.dirname(os.path.abspath(__file__))
project_directory = os.path.dirname(os.path.dirname(current_directory))
sys.path.append(project_directory)

from autojob.src.utils.spacy_init import SpacyInitializer, nlp
from autojob.src.keywords.ex_textacy import ke_txcy_textrank, ke_txcy_scake, ke_txcy_positionrank, ke_txcy_singlerank
from autojob.src.preprocessing.preprocessing_functions import (
    postprocess_text,
    preprocess_text
)
from autojob.src.preprocessing.preprocessing_utils import (
    extract_spacy_info,
    extract_string_info,
    EXCLUDED_ENTITY_TYPES
)

# Function to process input text
def process_text(input_text):
    """
    Process the input text by applying various text preprocessing and information extraction techniques.

    Parameters:
    - input_text (str): The input text to be processed.

    Returns:
    - Tuple: A tuple containing dictionaries with extracted information and processed text.
      1. job_info_group (dict): Dictionary containing extracted job-related information.
      2. results_group (dict): Dictionary containing various processed results.
      3. textacy_results (dict): Dictionary containing keyterms extracted using textacy.
      4. processed_text (str): The final processed text.
    """
    # Preprocess input text
    preprocessed_text = preprocess_text(input_text)
    
    # Extract phone numbers, links, and emails from preprocessed text
    extracted_phone_numbers, extracted_links, extracted_emails = extract_string_info(preprocessed_text)

    # Process text using spaCy
    doc = nlp(preprocessed_text)
    
    # Extract various information using spaCy
    extracted_gpe_locations, extracted_loc_locations, extracted_dates, extracted_languages, extracted_laws, extracted_norps, extracted_orgs, extracted_persons, extracted_products, extracted_money = extract_spacy_info(doc)
    
    extracted_location_data = extracted_gpe_locations + extracted_loc_locations

    # Filter tokens based on excluded entity types
    lemmatized_tokens_result = [token.lemma_ for token in doc if token.ent_type_ not in EXCLUDED_ENTITY_TYPES]

    # Combine lemmatized and original tokens
    combined_lemmatized_tokens = ' '.join(lemmatized_tokens_result)
    
    # Postprocess combined tokens
    combined_lemmatized_tokens = postprocess_text(combined_lemmatized_tokens)

    processed_text = combined_lemmatized_tokens
    
    # Process lemmatized tokens using spaCy
    doc_lemmatized = nlp(combined_lemmatized_tokens)
    
    # Extract noun chunks
    extracted_noun_chunks = [chunk.text for chunk in doc_lemmatized.noun_chunks]
    extracted_noun_chunks = sorted(extracted_noun_chunks, key=lambda x: len(x), reverse=True)
    
    # Extract keyterms using different algorithms
    keyterms_textrank = ke_txcy_textrank(doc_lemmatized)
    keyterms_singlerank = ke_txcy_singlerank(doc_lemmatized)
    keyterms_positionrank = ke_txcy_positionrank(doc_lemmatized)
    keyterms_scake = ke_txcy_scake(doc_lemmatized)
    
    # Group results into dictionaries
    job_info_group = {
        'extracted_phone_numbers': list(set(extracted_phone_numbers)),
        'extracted_links': list(set(extracted_links)),
        'extracted_emails': list(set(extracted_emails)),
        'extracted_location_data': list(set(extracted_location_data)),
        'extracted_dates': list(set(extracted_dates)),
        'extracted_languages': list(set(extracted_languages)),
        'extracted_laws': list(set(extracted_laws)),
        'extracted_norps': list(set(extracted_norps)),
        'extracted_orgs': list(set(extracted_orgs)),
        'extracted_persons': list(set(extracted_persons)),
        'extracted_products': list(set(extracted_products)),
        'extracted_money': extracted_money,
        'processed_text': processed_text
    }
    
    results_group = {
        'extracted_noun_chunks': list(set(extracted_noun_chunks)),
        'combined_lemmatized_tokens': combined_lemmatized_tokens
    }
    
    textacy_results = {
        'scake_keyterms': keyterms_scake,
        'textrank_keyterms': keyterms_textrank,
        'singlerank_keyterms': keyterms_singlerank,
        'positionrank_keyterms': keyterms_positionrank
    }
    
    return job_info_group, results_group, textacy_results, processed_text
