# File: src/user_input/update_resume_structure.py

import json

# Function to update the structure of the resume_data dictionary
def update_structure(resume_data):
    # Split coursework entries and initialize additional fields
    for education_entry in resume_data.get("education", []):
        for course_entry in education_entry.get("coursework", []):
            course_code, course_name = map(str.strip, course_entry.split('|'))
            course_entry["course_code"] = course_code
            course_entry["course_name"] = course_name
            course_entry["course_score"] = ""
            course_entry["course_keywords"] = ""

        # Rename and convert keys to lowercase with underscores
        education_entry_lower = {key.lower(): value for key, value in education_entry.items()}
        resume_data["education"].remove(education_entry)
        resume_data["education"].append(education_entry_lower)

    # Update skills array
    resume_data["skills"] = [{"id": i + 1, "skill": skill.lower(), "keywords": "", "score": ""} for i, skill in enumerate(resume_data.get("skills", []))]

    # Update experiences and projects arrays
    for entry_type, description_field in [("experiences", "work_experience_description"), ("projects", "projects/research_description")]:
        for entry in resume_data.get(entry_type, []):
            entry[description_field] = [{"id": i + 1, "content": desc, "keywords": "", "score": ""} for i, desc in enumerate(entry.get("description", []))]
            entry.pop("description", None)

    # Rename and convert keys to lowercase with underscores
    resume_data["heading"] = {key.lower(): value for key, value in resume_data.get("heading", {}).items()}
    resume_data["work_experience"] = resume_data.pop("experiences", [])
    resume_data["projects/research"] = resume_data.pop("projects", [])


# Example usage:
# if __name__ == "__main__":
#     with open("path/to/your/resume.json", "r") as file:
#         resume_data = json.load(file)
#     update_structure(resume_data)
#     # Now, resume_data is updated with the new structure
#     # Save the updated data back to the file or use it as needed
#     with open("path/to/your/updated_resume.json", "w") as file:
#         json.dump(resume_data, file, indent=2)
