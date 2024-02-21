# File: src/user_input/experience_window.py

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

EXPERIENCE = []

def get_experiences(experience_data):
    print("Getting experience data...")
    EXPERIENCE.append(experience_data)
    with open(os.path.join(REF_DATA_DIR, "raw_experience_data.json"), "w") as json_file:
        json.dump(EXPERIENCE, json_file, indent=4)
    print("Experience data written to raw_experience_data.json successfully.")

def clear_input_boxes():
    experience_name_var.set('')
    experience_location_var.set('')
    experience_role_var.set('')
    start_month.set('')
    start_year.set('')
    end_month.set('')
    end_year.set('')
    experience_details.delete('1.0', tk.END)

def experience_module():
    def on_submit():
        experience_start_date = f"{start_month.get()} {start_year.get()}"
        experience_end_date = f"{end_month.get()} {end_year.get()}"
        print("Submitting experience...")
        experience_data = {
            "Company Name": experience_name_var.get().strip(),
            "Company Location": experience_location_var.get().strip(),
            "Role": experience_role_var.get().strip(),
            "Start Date": experience_start_date,
            "End Date": experience_end_date,
            "Description": experience_details.get("1.0", tk.END).strip().split("\n")
        }
        get_experiences(experience_data)
        clear_input_boxes()

    # Create a new window (Toplevel) for the experiences module
    experience_window = tk.Tk()
    experience_window.title("Work Experiences")
    set_material_design_theme(experience_window)

    # Create a heading frame
    heading_frame = create_heading_frame(experience_window, "Work Experiences")

    # Create single-line text boxes with StringVar
    global experience_name_var, experience_location_var, experience_role_var, start_month, start_year, end_month, end_year, experience_details
    experience_name_var = tk.StringVar()
    experience_name_text = create_singleline_textbox(experience_window, "Company Name", width=30)
    experience_name_text.config(textvariable=experience_name_var)

    experience_location_var = tk.StringVar()
    experience_location_text = create_singleline_textbox(experience_window, "Company Location", width=30)
    experience_location_text.config(textvariable=experience_location_var)

    experience_role_var = tk.StringVar()
    experience_role_text = create_singleline_textbox(experience_window, "Role", width=30)
    experience_role_text.config(textvariable=experience_role_var)

    # Create date selection sections
    start_month = tk.StringVar()
    start_year = tk.StringVar()
    end_month = tk.StringVar()
    end_year = tk.StringVar()
    create_date_selection(experience_window, "Start Date", start_month, start_year)
    create_date_selection(experience_window, "End Date", end_month, end_year)

    # Create a multi-line text box
    experience_details = create_multiline_textbox(experience_window, "Experience Details (put each entry on its own line):", height=20, width=50)

    # Create a button with a custom function
    submit_button = create_button(experience_window, "Submit Experience", on_submit)

    # Adjust the placement of the button below the multi-line text box
    submit_button.grid(row=experience_window.grid_size()[1], column=0, padx=10, pady=10)

    experience_window.mainloop()

if __name__ == "__main__":
    experience_module()
