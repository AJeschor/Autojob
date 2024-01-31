# jobbert_test.py

import requests
from transformers import pipeline 

def initialize_fill_mask_pipeline_inference(api_url, api_token):
    """
    Initialize the fill-mask pipeline with the Inference API.
    Args:
        api_url (str): The Inference API URL for the model.
        api_token (str): Your Hugging Face API token.
    Returns:
        dict: The initialized pipeline response.
    """
    headers = {"Authorization": f"Bearer {api_token}"}
    payload = {"inputs": "Initialize fill-mask pipeline."}
    response = requests.post(api_url, headers=headers, json=payload)
    
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"Failed to initialize pipeline. Status code: {response.status_code}")

def find_keyword_matches(job_postings, keywords_phrases, fill_mask_pipeline_inference):
    """
    Find related words for keywords/phrases in job postings using the Inference API pipeline.
    Args:
        job_postings (list): List of job postings with descriptions.
        keywords_phrases (list): List of keywords and phrases to find related words for.
        fill_mask_pipeline_inference (dict): The initialized fill-mask pipeline response.
    Returns:
        dict: A dictionary with job titles as keys and related words for keywords/phrases.
    """
    matches = {}

    for posting in job_postings:
        matches[posting["job_title"]] = {}

        for keyword in keywords_phrases:
            related_word = find_related_word(fill_mask_pipeline_inference, posting['description'], keyword)
            matches[posting["job_title"]][keyword] = related_word

    return matches

def find_related_word(pipeline_response, description, keyword):
    """
    Find a related word using the initialized Inference API pipeline response.
    Args:
        pipeline_response (dict): The initialized pipeline response from the Inference API.
        description (str): The job posting description.
        keyword (str): The keyword to find a related word for.
    Returns:
        str: The related word.
    """
    result = requests.post(pipeline_response["generated_text"])
    return result.json()[0]["generated_text"]

# Example usage (you can run this part as a standalone script)
if __name__ == "__main__":
    API_URL = "https://api-inference.huggingface.co/models/jjzha/jobbert-base-cased"
    API_TOKEN = "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"

    # Initialize the fill-mask pipeline using the Inference API
    fill_mask_pipeline_inference = initialize_fill_mask_pipeline_inference(API_URL, API_TOKEN)

    job_postings = [
        {"job_title": "Software Engineer", "description": "We are hiring a Software Engineer."},
        {"job_title": "Data Analyst", "description": "Looking for a Data Analyst with Python skills."},
    ]
    keywords_phrases = ["Software Engineer", "Python"]

    result = find_keyword_matches(job_postings, keywords_phrases, fill_mask_pipeline_inference)
    print(result)

