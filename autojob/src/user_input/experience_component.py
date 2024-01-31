# File: autojob/src/user_input/experience_module.py

import tkinter as tk
from ui_theme import set_material_design_theme
from ui_elements import create_heading_frame, create_singleline_textbox, create_date_selection, create_multiline_textbox, create_button

def experience_module(parent_frame):
    # Create a heading frame within the collapsible frame
    heading_frame = create_heading_frame(parent_frame, "Work Experiences")

    # Create single-line text boxes with StringVar
    experience_name_var = tk.StringVar()
    experience_name_text = create_singleline_textbox(parent_frame, "Company Name", width=30)
    experience_name_text.config(textvariable=experience_name_var)

    experience_location_var = tk.StringVar()
    experience_location_text = create_singleline_textbox(parent_frame, "Company Location", width=30)
    experience_location_text.config(textvariable=experience_location_var)

    experience_role_var = tk.StringVar()
    experience_role_text = create_singleline_textbox(parent_frame, "Role", width=30)
    experience_role_text.config(textvariable=experience_role_var)

    # Create date selection sections
    start_month = tk.StringVar()
    start_year = tk.StringVar()
    end_month = tk.StringVar()
    end_year = tk.StringVar()
    create_date_selection(parent_frame, "Start Date", start_month, start_year)
    create_date_selection(parent_frame, "End Date", end_month, end_year)

    # Create a multi-line text box
    experience_details = create_multiline_textbox(parent_frame, "Experience Details (put each entry on its own line):", height=20, width=50)

    # Create a button with a custom function
    submit_button = create_button(parent_frame, "Submit Experience", lambda: get_experiences(experience_name_var, experience_location_var, experience_role_var, experience_details, start_month, start_year, end_month, end_year))

    # Adjust the placement of the button below the multi-line text box
    submit_button.grid(row=parent_frame.grid_size()[1], column=0, padx=10, pady=10)

if __name__ == "__main__":
    # You can add a button to open the collapsible experience module in the main window
    open_experience_button = tk.Button(root, text="Open Experiences Module", command=lambda: experience_module(CollapsibleFrame(root, text="Work Experiences")))
    open_experience_button.grid(row=8, column=0, padx=10, pady=10)
    root.mainloop()
