# autojob/src/webscraper/get_actor_settings.py

import os
import requests
import json

# Define the constant for the API token file location
PROJECT_DIRECTORY = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
API_TOKEN_FILE = os.path.join(PROJECT_DIRECTORY, 'src', 'utils', 'apify_api_token.json')

def load_api_token():
    """
    Load API token from apify_api_token.json file.

    Returns:
    - str or None: The API token if found, otherwise None.
    """
    try:
        with open(API_TOKEN_FILE, "r") as token_file:
            return json.load(token_file).get("API_TOKEN")
    except FileNotFoundError:
        print(f"Error: {API_TOKEN_FILE} not found.")
        return None

def fetch_data(api_token, endpoint):
    """
    Fetch data from the specified API endpoint using the provided API token.

    Parameters:
    - api_token (str): The API token.
    - endpoint (str): The API endpoint.

    Returns:
    - dict or None: The fetched data if successful, otherwise None.
    """
    # Construct the API endpoint URL with the API token as a query parameter
    url = f"https://api.apify.com/v2/acts/misceres~indeed-scraper/{endpoint}"
    
    # Define query parameters with the API token
    params = {
        "token": api_token
    }

    # Make a GET request to fetch the data
    response = requests.get(url, params=params)

    # Check if the request was successful (HTTP status code 200)
    if response.status_code == 200:
        # Parse the JSON response to obtain the data
        data = response.json()
        return data
    else:
        # If the request was not successful, print the status code and response content
        print(f"Failed to retrieve data from {endpoint}. Status code: {response.status_code}")
        print(response.text)
        return None

# Load API token
api_token = load_api_token()

