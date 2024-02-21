# File: src/user_input/education_window.py

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

EDUCATION = []

def get_education(education_data):
    print("Getting education data...")
    with open(os.path.join(REF_DATA_DIR, "raw_education_data.json"), "w") as json_file:
        json.dump(education_data, json_file, indent=4)
    print("Education data written to raw_education_data.json successfully.")

def education_module():
    def on_submit():
        education_start_date = f"{start_month.get()} {start_year.get()}"
        education_end_date = f"{end_month.get()} {end_year.get()}"
        print("Submitting education...")
        education_data = {
            "University Name": education_name_var.get().strip(),
            "University Location": education_location_var.get().strip(),
            "Degree": education_degree_var.get().strip(),
            "Start Date": education_start_date,
            "End Date": education_end_date,
            "Coursework": education_details.get("1.0", tk.END).strip().split("\n")
        }
        EDUCATION.append(education_data)
        get_education(EDUCATION)
        
        # Clear input boxes
        education_name_var.set("")
        education_location_var.set("")
        education_degree_var.set("")
        start_month.set("")
        start_year.set("")
        end_month.set("")
        end_year.set("")
        education_details.delete("1.0", tk.END)

    # Create a new window (Toplevel) for the education module
    education_window = tk.Tk()
    education_window.title("Education")
    set_material_design_theme(education_window)

    # Create a heading frame
    heading_frame = create_heading_frame(education_window, "Education")

    # Create single-line text boxes with StringVar
    education_name_var = tk.StringVar()
    education_name_text = create_singleline_textbox(education_window, "University Name", width=30)
    education_name_text.config(textvariable=education_name_var)

    education_location_var = tk.StringVar()
    education_location_text = create_singleline_textbox(education_window, "University Location", width=30)
    education_location_text.config(textvariable=education_location_var)

    education_degree_var = tk.StringVar()
    education_degree_text = create_singleline_textbox(education_window, "Degree", width=30)
    education_degree_text.config(textvariable=education_degree_var)

    # Create date selection sections
    start_month = tk.StringVar()
    start_year = tk.StringVar()
    end_month = tk.StringVar()
    end_year = tk.StringVar()
    create_date_selection(education_window, "Start Date", start_month, start_year)
    create_date_selection(education_window, "End Date", end_month, end_year)

    # Create a multi-line text box
    education_details = create_multiline_textbox(education_window, "Coursework List (put each entry on its own line):", height=20, width=50)

    # Create a button with a custom function
    submit_button = create_button(education_window, "Submit Education", on_submit)

    # Adjust the placement of the button below the multi-line text box
    submit_button.grid(row=education_window.grid_size()[1], column=0, padx=10, pady=10)

    education_window.mainloop()

if __name__ == "__main__":
    education_module()
