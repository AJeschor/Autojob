# File: src/user_input/input_ui.py

import os
import sys
import json
import tkinter as tk
from tkinter import ttk
import project_module
import education_module
import experience_module
from ui_theme import set_material_design_theme
from update_resume_structure import update_structure
from ui_functions import create_heading_frame, create_singleline_textbox, create_multiline_textbox

# Set up directory paths and import custom modules
current_directory = os.path.dirname(os.path.abspath(__file__))
project_directory = os.path.dirname(os.path.dirname(current_directory))
sys.path.append(project_directory)
REF_DATA_DIR = os.path.join(project_directory, 'src', 'ref', 'resume_files')
OUTPUT_FILE_PATH = os.path.join(REF_DATA_DIR, "raw_resume_data.json")

root = tk.Tk()
root.title("Main Window")
set_material_design_theme(root)

# Create a heading frame
heading_frame = create_heading_frame(root, "Resume Input")

# Full Name
full_name_textbox = create_singleline_textbox(root, "User Name", width=30)

# User Location
user_location_textbox = create_singleline_textbox(root, "User Location", width=30)

# Email
email = create_singleline_textbox(root, "Email", width=30)

# Phone Number
phone_number = create_singleline_textbox(root, "Phone Number", width=30)

# LinkedIn Profile
linkedin_profile_url = create_singleline_textbox(root, "LinkedIn Profile", width=30)

# GitHub Profile
github_profile_url = create_singleline_textbox(root, "GitHub Profile", width=30)

# Skills Textbox
skills = create_multiline_textbox(root, "Skills (put each entry on its own line):", height=20, width=50)

# Create a button to open the project module UI
open_project_button = tk.Button(root, text="Open Project Window", command=lambda: project_module.project_module(root))
open_project_button.grid(row=8, column=0, padx=10, pady=10)  # Use grid here

# Create a button to open the experience module UI
open_experience_button = tk.Button(root, text="Open Experience Window", command=lambda: experience_module.experience_module(root))
open_experience_button.grid(row=9, column=0, padx=10, pady=10)  # Use grid here

# Create a button to open the education module UI
open_education_button = tk.Button(root, text="Open Education Window", command=lambda: education_module.education_module(root))
open_education_button.grid(row=10, column=0, padx=10, pady=10)  # Use grid here

# Make the resume
def get_data():
    print("Gathering user input...")
    # Gather user input
    name = full_name_textbox.get().strip()
    email_text = email.get().strip()
    phone_number_text = phone_number.get().strip()
    linkedin = linkedin_profile_url.get().strip()
    github = github_profile_url.get().strip()
    user_location = user_location_textbox.get().strip()

    # Include the user location in the heading dictionary
    HEADING = {
        "name": name,
        "email": email_text,
        "phone_number": phone_number_text,
        "linkedin": linkedin,
        "github": github,
        "user_location": user_location,
    }

    skills_text = skills.get("1.0", tk.END).strip()
    skills_list = [skill.strip() for skill in skills_text.splitlines()]

    # Create a dictionary to store the resume data
    resume_data = {
        "heading": HEADING,
        "skills": skills_list,
        "experiences": experience_module.EXPERIENCE,
        "projects": project_module.PROJECTS,
        "education": education_module.EDUCATION,
    }

    print("Updating resume structure...")
    # Call the update_structure function to modify the structure
    update_structure(resume_data)

    print("Saving data to JSON file...")
    # Save the data as a JSON file in the specified directory
    with open(OUTPUT_FILE_PATH, "w") as json_file:
        json.dump(resume_data, json_file, indent=4)

# Submit button
submit_button = tk.Button(root, text="Submit", command=get_data, font=('Arial', 14))
submit_button.grid(row=11, column=0, padx=10, pady=10)

root.mainloop()
