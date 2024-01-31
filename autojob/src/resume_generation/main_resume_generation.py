# main_res_gen.py

import os
import sys
import json

# Get the current script's directory and project directory
current_directory = os.path.dirname(os.path.abspath(__file__))
project_directory = os.path.dirname(os.path.dirname(current_directory))
sys.path.append(project_directory)

# Define the path to the JSON file
ref_data_dir = os.path.join(project_directory, 'ref')
tex_files_dir = os.path.join(project_directory, 'ref', 'tex_files')

def read_resume_data():
    # Define the path to the JSON file
    json_file_path = os.path.join(ref_data_dir, 'resume_data.json')
    
    # Check if the file exists
    if os.path.exists(json_file_path):
        with open(json_file_path, 'r') as json_file:
            resume_data = json.load(json_file)
        return resume_data
    else:
        print("resume_data.json not found in the ref_data directory.")
        return None
        
def replace_headers(content, data):
    # Replace placeholders with corresponding values from data
    content = content.replace("{user-name}", data["heading"]["name"])
    content = content.replace("{user-email}", data["heading"]["email"])
    content = content.replace("{user-phonenumber}", data["heading"]["phone_number"])
    content = content.replace("{user-linkedIn}", data["heading"]["linkedin"])
    content = content.replace("{user-gitHub}", data["heading"]["github"])
    content = content.replace("{user-country}", data.get("country", ""))
    content = content.replace("{user-city}", data.get("city", ""))
    return content

# Create a dictionary to store the file contents
file_contents = {}

# Define a list of file names
file_names = ['custom_environments.tex', 'header.tex', 'education.tex', 'experience.tex', 'projects.tex', 'skills.tex']

# Load resume data
resume_data = read_resume_data()

if not resume_data:
    exit(1)

# Iterate through the file names and read the contents from the tex_files_dir
for file_name in file_names:
    file_path = os.path.join(tex_files_dir, file_name)
    if os.path.exists(file_path):
        with open(file_path, 'r') as file:
            file_contents[file_name.split('.')[0]] = file.read()
    else:
        print(f"{file_name} not found in the tex_files directory.")

# Replace placeholders in each file's content
for key, value in file_contents.items():
    file_contents[key] = replace_headers(value, resume_data)

# Now you have the contents of each file with placeholders replaced by values from the JSON data.
# You can access and use these modified strings as needed.

# Example usage of read_resume_data function
print("Resume data loaded and placeholders replaced successfully.")

# Print the updated contents
for key, value in file_contents.items():
    print(f'Updated Contents of {key}:')
    print(value)

