# autojob/src/webscraper_module.py

import json
import os
import sys
from autojob.src.webscraper.webscraper_actor import WebscraperActor

# Set up paths using definitions from preprocessing_module.py
current_directory = os.path.dirname(os.path.abspath(__file__))
project_directory = os.path.dirname(current_directory)
sys.path.append(project_directory)

# Define directory paths
INPUT_FILES_DIR = os.path.join(project_directory, 'input_files')

# Define path for config_settings.json inside the 'utils' directory
CONFIG_SETTINGS_PATH = os.path.join(project_directory, 'src', 'utils', 'webscraper_settings.json')

def run_webscraper_once_prompt():
    """Prompt the user to run the webscraper once and execute it if the user agrees."""
    
    try:
        # Read configuration settings from config_settings.json
        with open(CONFIG_SETTINGS_PATH, "r") as config_file:
            config_data = json.load(config_file)["Webscraper_Settings"]
        
        # Instantiate the WebscraperActor with INPUT_FILES_DIR as the output_directory argument
        actor = WebscraperActor(output_directory=INPUT_FILES_DIR)
        
        # Set RUN_INPUT using values from config_settings.json
        actor.RUN_INPUT = config_data["RUN_INPUT"]
        
        while True:
            user_input = input("Do you want to run the webscraper once? (y/n/exit): ").strip().lower()
            
            if user_input == 'y':
                print("Running webscraper...")
                actor.run_apify_actor()
                break
            elif user_input == 'n':
                print("Skipping webscraper.")
                break
            elif user_input == 'exit':
                print("Exiting.")
                sys.exit()
            else:
                print("Invalid input. Try again.")
            
    except Exception as e:
        print(f"An error occurred: {e}")
