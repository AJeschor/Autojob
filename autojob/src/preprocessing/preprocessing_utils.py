# File: autojob/src/preprocessing/preprocessing_utils.py

import os
import sys
import re
import json
import spacy
import numpy as np
from spacy.lang.en.stop_words import STOP_WORDS

# Set up project paths and import custom modules
current_directory = os.path.dirname(os.path.abspath(__file__))
project_directory = os.path.dirname(os.path.dirname(current_directory))
sys.path.append(project_directory)

from autojob.src.utils.spacy_init import SpacyInitializer, nlp
from autojob.src.preprocessing.acronyms import acronym_list
from autojob.src.preprocessing.contractions_dict import all_contractions
from autojob.src.preprocessing.custom_stopwords import custom_stop_word_list

# Regular expressions for extracting phone numbers
PHONE_NUMBER_PATTERNS = [
    r'\(\d{3}\)[ -]?\d{3}[ -]?\d{4}',
    r'\d{3}[.-]?\d{3}[.-]?\d{4}',
    r'\d{10}', 
    r'\+\d{1}\s?\(\d{3}\)[ -]?\d{3}[ -]?\d{4}',
    r'\+?1?[ -]?\(?\d{3}\)?[ -]?\d{3}[ -]?\d{4}',
    r'\+?1?[ -]?\(?\d{3}\)?[ -]?\d{3}[ -]?\d{4}',
]

# Regular expressions for extracting links
LINKS = [
    r'https?://\S+',
    r'www\.\S+',
    r'(?<=\.)\b(?:com|org|net|gov|edu|co\.uk)\b',
    r'(?<=\.)\S+\.(?:com|org|net|gov|edu|co\.uk|\S{2,})(?=(?:\s|\. |, ))',
]

# Regular expression for extracting emails
EMAIL_PATTERN = r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b"

# List of excluded entity types during SpaCy processing
EXCLUDED_ENTITY_TYPES = ['PERSON', 'FAC', 'GPE', 'LOC', 'WORK_OF_ART', 'TIME', 'PERCENT', 'MONEY', 'ORDINAL', 'CARDINAL', 'DATE', 'LANGUAGE', 'LAW', 'NORP', 'ORG', 'PRODUCT']

# Function to extract phone numbers, links, and emails from text
def extract_string_info(text):
    """
    Extracts phone numbers, links, and emails from the given text.

    Args:
        text (str): Input text to extract information from.

    Returns:
        tuple: A tuple containing lists of extracted phone numbers, links, and emails.
    """
    # Initialize empty lists for extracted information
    extracted_phone_numbers = []
    extracted_links = {
        "HTTP/HTTPS Links": [],
        "WWW Links": [],
        "TLDs": [],
        "General Links": [],
    }
    extracted_emails = []

    # Extract phone numbers using defined patterns
    for pattern in PHONE_NUMBER_PATTERNS:
        extracted_phone_numbers.extend(re.findall(pattern, text))

    # Extract links using defined patterns and categorize them
    for pattern in LINKS:
        if pattern == LINKS[0]:
            extracted_links["HTTP/HTTPS Links"].extend(set(re.findall(pattern, text)))
        elif pattern == LINKS[1]:
            extracted_links["WWW Links"].extend(set(re.findall(pattern, text)))
        elif pattern == LINKS[2]:
            extracted_links["TLDs"].extend(set(re.findall(pattern, text)))
        elif pattern == LINKS[3]:
            extracted_links["General Links"].extend(set(re.findall(pattern, text)))

    # Extract emails using the defined pattern
    extracted_emails.extend(set(re.findall(EMAIL_PATTERN, text)))
    
    return extracted_phone_numbers, extracted_links, extracted_emails

# Function to extract information such as locations, dates, entities, etc., using SpaCy NLP
def extract_spacy_info(doc):
    """
    Extracts information such as locations, dates, entities, etc., using SpaCy NLP.

    Args:
        doc (spacy.Doc): SpaCy Doc object representing the processed text.

    Returns:
        tuple: A tuple containing lists of extracted information such as locations, dates, entities, etc.
    """
    # Initialize empty lists for different types of information
    extracted_gpe_locations = []
    extracted_loc_locations = []
    extracted_dates = []
    extracted_languages = []
    extracted_laws = []
    extracted_norps = []
    extracted_orgs = []
    extracted_persons = []
    extracted_products = []
    extracted_money = []
    
    # Extract entities using the provided SpaCy Doc object
    for ent in doc.ents:
        if ent.label_ == 'GPE':
            extracted_gpe_locations.append(ent.text)
        elif ent.label_ == 'LOC':
            extracted_loc_locations.append(ent.text)
        elif ent.label_ == 'DATE':
            extracted_dates.append(ent.text)
        elif ent.label_ == 'LANGUAGE':
            extracted_languages.append(ent.text)
        elif ent.label_ == 'LAW':
            extracted_laws.append(ent.text)
        elif ent.label_ == 'NORP':
            extracted_norps.append(ent.text)
        elif ent.label_ == 'ORG':
            extracted_orgs.append(ent.text)
        elif ent.label_ == 'PERSON':
            extracted_persons.append(ent.text)
        elif ent.label_ == 'PRODUCT':
            extracted_products.append(ent.text)
        elif ent.label_ == 'MONEY':
            noun_phrases = [chunk.text for chunk in doc.noun_chunks if ent.start <= chunk.start < ent.end]
            extracted_money.append({'amount': ent.text, 'noun_phrases': noun_phrases})
  
    return (
        extracted_gpe_locations, 
        extracted_loc_locations,
        extracted_dates, 
        extracted_languages, 
        extracted_laws, 
        extracted_norps, 
        extracted_orgs, 
        extracted_persons, 
        extracted_products,
        extracted_money
    )
    
# Class for multiple-string-substitution
class Xlator(dict):
    """
    All-in-one multiple-string-substitution class.
    """
    def __init__(self, translation_dict, *args, **kwargs):
        """
        Initializes the Xlator with the given translation dictionary.

        Args:
            translation_dict (dict): Dictionary for string substitutions.
        """
        super(Xlator, self).__init__(*args, **kwargs)
        self.translation_dict = translation_dict
        self._regex = self._make_regex()

    def _make_regex(self):
        """Build re object based on the keys of the current dictionary."""
        # Use word boundaries to match whole words
        pattern = r"\b" + r"\b|\b".join(map(re.escape, self.translation_dict.keys())) + r"\b"
        return re.compile(pattern)

    def __call__(self, text):
        """
        Translates text using the provided translation dictionary.

        Args:
            text (str): Input text for translation.

        Returns:
            str: Translated text.
        """
        return self._regex.sub(self._replace, text)

    def _replace(self, match):
        """
        Handler invoked for each regex match during translation.

        Args:
            match (re.Match): Match object representing the matched pattern.

        Returns:
            str: Replacement for the matched pattern.
        """
        return self.translation_dict[match.group(0)]

# Function to extract terms being substituted by Xlator from text
def extract_substituted_terms(text, xlator_instance):
    """
    Extracts terms being substituted by Xlator from the given text.

    Args:
        text (str): Input text containing substitutions.
        xlator_instance (Xlator): Instance of Xlator for substitution.

    Returns:
        list: List of substituted terms.
    """
    # Find all matches using the Xlator's regex pattern
    matches = xlator_instance._regex.finditer(text)
    
    # Extract and return the matched terms
    substituted_terms = [match.group(0) for match in matches]
    
    return substituted_terms

# Function to filter unnecessary fields from the annotation dictionary
def filter_annotations(ann):
    """
    Filters unnecessary fields from the annotation dictionary.

    Args:
        ann (dict): Input annotation dictionary.

    Returns:
        dict: Filtered annotation dictionary.
    """
    # Remove 'text' field from the dictionary
    ann.pop('text', None)
    
    if 'results' in ann:
        results = ann['results']
        
        # Process 'full_matches' entries
        if 'full_matches' in results:
            for match in results['full_matches']:
                match['skill_id'] = match.pop('doc_node_value', None)
                match.pop('doc_node_id', None)
                match.pop('type', None)
                match.pop('len', None)
        
        # Process 'ngram_scored' entries
        if 'ngram_scored' in results:
            for ngram in results['ngram_scored']:
                ngram['skill_id'] = ngram.pop('doc_node_value', None)
                ngram.pop('doc_node_id', None)
                ngram.pop('type', None)
                ngram.pop('len', None)
        
        # Combine and filter out redundant entries
        combined_results = results.get('full_matches', []) + results.get('ngram_scored', [])
        unique_results = {result['skill_id']: result for result in combined_results}.values()
        
        # Sort the list of dictionaries by 'score' in descending order
        sorted_results = sorted(unique_results, key=lambda x: x['score'], reverse=True)
        
        # Update the 'results' field with the sorted and unique list
        ann['results'] = sorted_results
    
    return ann
    
# annotations = skill_extractor.annotate(processed_text)
# skillner_results = filter_annotations(annotations)  
    

# Function to convert non-serializable types to a serializable format
def convert_to_serializable(obj):
    """
    Converts non-serializable types to a serializable format.

    Args:
        obj: Object to be serialized.

    Returns:
        JSON serializable object.

    Raises:
        TypeError: If the object's type is not supported for JSON serialization.

    Note:
        This function handles conversion for NumPy (`np.int64`). It converts Spacy Tokens to strings
        and raises an error for unsupported types.

    """
    if isinstance(obj, np.int64):
        return int(obj)
    elif isinstance(obj, spacy.tokens.Token):
        return str(obj)
    raise TypeError(f"Object of type {type(obj)} is not JSON serializable")

def sanitize_folder_name(name):
    """
    Sanitizes a folder name by replacing problematic characters uch as '/', '\', '.', and ':' with underscores.

    Args:
        name (str): The input folder name to be sanitized.

    Returns:
        str: The sanitized folder name with problematic characters replaced by underscores.
    """
    return name.replace('/', '_').replace('\\', '_').replace(':', '_').replace('.', '_')

