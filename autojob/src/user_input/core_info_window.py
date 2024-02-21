# File: src/user_input/core_info_window.py

import os
import sys
import json
import tkinter as tk
from ui_theme import set_material_design_theme
from ui_functions import create_heading_frame, create_singleline_textbox, create_multiline_textbox

# Set up directory paths and import custom modules
current_directory = os.path.dirname(os.path.abspath(__file__))
project_directory = os.path.dirname(os.path.dirname(current_directory))
sys.path.append(project_directory)
REF_DATA_DIR = os.path.join(project_directory, 'src', 'ref', 'resume_files')

def get_data():
    """Get user input and save it to JSON files."""
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

    print("Saving data to JSON files...")

    # Save the HEADING data as a JSON file
    with open(os.path.join(REF_DATA_DIR, "raw_heading.json"), "w") as heading_file:
        json.dump(HEADING, heading_file, indent=4)

    # Get skills data from the multiline textbox
    skills_text = skills.get("1.0", tk.END).strip()
    skills_list = [skill.strip() for skill in skills_text.splitlines()]

    # Save the skills data as a JSON file
    with open(os.path.join(REF_DATA_DIR, "raw_misc_skills.json"), "w") as skills_file:
        json.dump(skills_list, skills_file, indent=4)

    print("Data saved successfully.")

root = tk.Tk()
root.title("Core Info Window")
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

# Submit button
submit_button = tk.Button(root, text="Submit", command=get_data, font=('Arial', 14))
submit_button.grid(row=11, column=0, padx=10, pady=10)

root.mainloop()
