# File: autojob/src/user_input/ui_functions.py

import os
import json
import tkinter as tk

import os
import sys

# Get the current script's directory and project directory
current_directory = os.path.dirname(os.path.abspath(__file__))
project_directory = os.path.dirname(os.path.dirname(current_directory))
sys.path.append(project_directory)

# Define the path to the JSON file
REF_DATA_DIR = os.path.join(project_directory, 'ref')
TMP_DIR = os.path.join(project_directory, 'tmp')
OUTPUT_FILE_PATH = os.path.join(REF_DATA_DIR, "raw_resume_data.json")

def get_data():
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

    # Call the update_structure function to modify the structure
    update_structure(resume_data)

    # Save the data as a JSON file in the specified directory
    with open(OUTPUT_FILE_PATH, "w") as json_file:
        json.dump(resume_data, json_file, indent=4)



PROJECTS = []

def get_projects(project_name_var, project_link_var, project_role_var, project_details, start_month, start_year, end_month, end_year):
    project_start_date = f"{start_month.get()} {start_year.get()}"
    project_end_date = f"{end_month.get()} {end_year.get()}"

    project_data = {
        "Project Title": project_name_var.get().strip(),
        "Project Link": project_link_var.get().strip(),
        "Role": project_role_var.get().strip(),
        "Start Date": project_start_date,
        "End Date": project_end_date,
        "Description": project_details.get("1.0", tk.END).strip().split("\n")
    }

    PROJECTS.append(project_data)

    project_name_var.set("")
    project_link_var.set("")
    project_role_var.set("")
    project_details.delete("1.0", tk.END)
    
EXPERIENCE = []

def get_experience(experience_name_var, experience_location_var, experience_role_var, experience_details, start_month, start_year, end_month, end_year):
    experience_start_date = f"{start_month.get()} {start_year.get()}"
    experience_end_date = f"{end_month.get()} {end_year.get()}"

    experience_data = {
        "Company Name": experience_name_var.get().strip(),
        "Company Location": experience_location_var.get().strip(),
        "Role": experience_role_var.get().strip(),
        "Start Date": experience_start_date,
        "End Date": experience_end_date,
        "Description": experience_details.get("1.0", tk.END).strip().split("\n")
    }

    EXPERIENCE.append(experience_data)

    experience_name_var.set("")
    experience_location_var.set("")
    experience_role_var.set("")
    experience_details.delete("1.0", tk.END)


EDUCATION = []

def get_education(education_name_var, education_location_var, education_degree_var, education_details, start_month, start_year, end_month, end_year):
    education_start_date = f"{start_month.get()} {start_year.get()}"
    education_end_date = f"{end_month.get()} {end_year.get()}"

    education_data = {
        "University Name": education_name_var.get().strip(),
        "University Location": education_location_var.get().strip(),
        "Degree": education_degree_var.get().strip(),
        "Start Date": education_start_date,
        "End Date": education_end_date,
        "Coursework": education_details.get("1.0", tk.END).strip().split("\n")
    }

    EDUCATION.append(education_data)

    education_name_var.set("")
    education_location_var.set("")
    education_degree_var.set("")
    education_details.delete("1.0", tk.END)

# Function to update the structure of the resume_data dictionary
def update_structure(resume_data):
    # Split coursework entries and initialize additional fields
    for education_entry in resume_data.get("educations", []):
        for course_entry in education_entry.get("coursework", []):
            course_code, course_name = map(str.strip, course_entry.split('|'))
            course_entry["course_code"] = course_code
            course_entry["course_name"] = course_name
            course_entry["course_score"] = ""
            course_entry["course_keywords"] = ""

        # Rename and convert keys to lowercase with underscores
        education_entry_lower = {key.lower().replace(" ", "_"): value for key, value in education_entry.items()}
        resume_data["educations"].remove(education_entry)
        resume_data["educations"].append(education_entry_lower)

    # Update skills array
    resume_data["skills"] = [{"id": i + 1, "skill": skill.lower().replace(" ", "_"), "keywords": "", "score": ""} for i, skill in enumerate(resume_data.get("skills", []))]

    # Update experiences and projects arrays
    for entry_type, description_field in [("experiences", "work_experience_description"), ("projects", "projects/research_description")]:
        for entry in resume_data.get(entry_type, []):
            entry[description_field] = [{"id": i + 1, "content": desc, "keywords": "", "score": ""} for i, desc in enumerate(entry.get("description", []))]
            entry.pop("description", None)

    # Rename and convert keys to lowercase with underscores
    resume_data["heading"] = {key.lower().replace(" ", "_"): value for key, value in resume_data.get("heading", {}).items()}
    resume_data["work_experience"] = resume_data.pop("experiences", [])
    resume_data["projects/research"] = resume_data.pop("projects", [])
