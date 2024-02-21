# File: src/user_input/experience_module.py

import tkinter as tk
from ui_theme import set_material_design_theme
from ui_functions import create_heading_frame, create_singleline_textbox, create_date_selection, create_multiline_textbox, create_button

EXPERIENCE = []

def get_experiences(main_window, experience_name_var, experience_location_var, experience_role_var, experience_details, experience_start_date, experience_end_date):
    print("Getting experience data...")
    experience_data = {
        "Company Name": experience_name_var.get().strip(),
        "Company Location": experience_location_var.get().strip(),
        "Role": experience_role_var.get().strip(),
        "Start Date": experience_start_date,
        "End Date": experience_end_date,
        "Description": experience_details.get("1.0", tk.END).strip().split("\n")
    }

    EXPERIENCE.append(experience_data)
    print("Experience added successfully:", experience_data)
    
    # Clear the input fields after submission
    experience_name_var.set("")
    experience_location_var.set("")
    experience_role_var.set("")
    experience_details.delete("1.0", tk.END)

def experience_module(main_window):
    def on_submit():
        experience_start_date = f"{start_month.get()} {start_year.get()}"
        experience_end_date = f"{end_month.get()} {end_year.get()}"
        print("Submitting experience...")
        get_experiences(
            main_window,
            experience_name_var,
            experience_location_var,
            experience_role_var,
            experience_details,
            experience_start_date,
            experience_end_date
        )

    # Create a new window (Toplevel) for the experiences module
    experience_window = tk.Toplevel(main_window)
    experience_window.title("Work Experiences")

    set_material_design_theme(experience_window)

    # Create a heading frame
    heading_frame = create_heading_frame(experience_window, "Work Experiences")

    # Create single-line text boxes with StringVar
    experience_name_var = tk.StringVar()
    experience_name_text = create_singleline_textbox(experience_window, "Company Name", width=30)
    experience_name_text.config(textvariable=experience_name_var)

    experience_location_var = tk.StringVar()
    experience_location_text = create_singleline_textbox(experience_window, "Company Location", width=30)
    experience_location_text.config(textvariable=experience_location_var)

    experience_role_var = tk.StringVar()
    experience_role_text = create_singleline_textbox(experience_window, "Role", width=30)
    experience_role

if __name__ == "__main__":
    root = tk.Tk()
    # You can add a button to open the experience module in the main window
    open_experience_button = tk.Button(root, text="Open Experiences Module", command=lambda: experience_module(root))
    open_experience_button.pack()
    root.mainloop()
