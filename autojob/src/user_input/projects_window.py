# File: src/user_input/projects_window.py

import os
import sys
import json
import tkinter as tk
from ui_theme import set_material_design_theme
from ui_functions import create_heading_frame, create_singleline_textbox, create_date_selection, create_multiline_textbox, create_button

current_directory = os.path.dirname(os.path.abspath(__file__))
project_directory = os.path.dirname(os.path.dirname(current_directory))
sys.path.append(project_directory)
REF_DATA_DIR = os.path.join(project_directory, 'src', 'ref', 'resume_files')

PROJECTS = []

def get_projects(project_data):
    print("Getting project data...")
    with open(os.path.join(REF_DATA_DIR, "raw_projects_data.json"), "w") as json_file:
        json.dump(project_data, json_file, indent=4)
    print("Project data written to raw_projects_data.json successfully.")

def project_module():
    def on_submit():
        project_start_date = f"{start_month.get()} {start_year.get()}"
        project_end_date = f"{end_month.get()} {end_year.get()}"
        print("Submitting project...")
        project_data = {
            "Project Title": project_name_var.get().strip(),
            "Project Link": project_link_var.get().strip(),
            "Role": project_role_var.get().strip(),
            "Start Date": project_start_date,
            "End Date": project_end_date,
            "Description": project_details.get("1.0", tk.END).strip().split("\n")
        }
        PROJECTS.append(project_data)
        get_projects(PROJECTS)
        
        # Clear input boxes
        project_name_var.set("")
        project_link_var.set("")
        project_role_var.set("")
        start_month.set("")
        start_year.set("")
        end_month.set("")
        end_year.set("")
        project_details.delete("1.0", tk.END)

    # Create a new window (Toplevel) for the projects module
    project_window = tk.Tk()
    project_window.title("Projects & Research")
    set_material_design_theme(project_window)

    # Create a heading frame
    heading_frame = create_heading_frame(project_window, "Projects & Research")

    # Create single-line text boxes with StringVar
    project_name_var = tk.StringVar()
    project_name_text = create_singleline_textbox(project_window, "Project Name", width=30)
    project_name_text.config(textvariable=project_name_var)

    project_link_var = tk.StringVar()
    project_link_text = create_singleline_textbox(project_window, "Project Link", width=30)
    project_link_text.config(textvariable=project_link_var)

    project_role_var = tk.StringVar()
    project_role_text = create_singleline_textbox(project_window, "Project Role", width=30)
    project_role_text.config(textvariable=project_role_var)

    # Create date selection sections
    start_month = tk.StringVar()
    start_year = tk.StringVar()
    end_month = tk.StringVar()
    end_year = tk.StringVar()
    create_date_selection(project_window, "Start Date", start_month, start_year)
    create_date_selection(project_window, "End Date", end_month, end_year)

    # Create a multi-line text box
    project_details = create_multiline_textbox(project_window, "Project Details (put each entry on its own line):", height=20, width=50)

    # Create a button with a custom function
    submit_button = create_button(project_window, "Submit Project", on_submit)

    # Adjust the placement of the button below the multi-line text box
    submit_button.grid(row=project_window.grid_size()[1], column=0, padx=10, pady=10)

    project_window.mainloop()

if __name__ == "__main__":
    project_module()
