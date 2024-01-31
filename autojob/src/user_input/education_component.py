# File: autojob/src/user_input/education_module.py

import tkinter as tk
from ui_theme import set_material_design_theme
from ui_elements import create_heading_frame, create_singleline_textbox, create_date_selection, create_multiline_textbox, create_button

def education_module(parent_frame):
    # Create a heading frame within the collapsible frame
    heading_frame = create_heading_frame(parent_frame, "Education")

    # Create single-line text boxes with StringVar
    education_name_var = tk.StringVar()
    education_name_text = create_singleline_textbox(parent_frame, "University Name", width=30)
    education_name_text.config(textvariable=education_name_var)

    education_location_var = tk.StringVar()
    education_location_text = create_singleline_textbox(parent_frame, "University Location", width=30)
    education_location_text.config(textvariable=education_location_var)

    education_degree_var = tk.StringVar()
    education_degree_text = create_singleline_textbox(parent_frame, "Degree", width=30)
    education_degree_text.config(textvariable=education_degree_var)

    # Create date selection sections
    start_month = tk.StringVar()
    start_year = tk.StringVar()
    end_month = tk.StringVar()
    end_year = tk.StringVar()
    create_date_selection(parent_frame, "Start Date", start_month, start_year)
    create_date_selection(parent_frame, "End Date", end_month, end_year)

    # Create a multi-line text box
    education_details = create_multiline_textbox(parent_frame, "Coursework List (put each entry on its own line):", height=20, width=50)

    # Create a button with a custom function
    submit_button = create_button(parent_frame, "Submit Education", lambda: get_education(education_name_var, education_location_var, education_degree_var, education_details, start_month, start_year, end_month, end_year))

    # Adjust the placement of the button below the multi-line text box
    submit_button.grid(row=parent_frame.grid_size()[1], column=0, padx=10, pady=10)

if __name__ == "__main__":
    # You can add a button to open the collapsible education module in the main window
    open_education_button = tk.Button(root, text="Open Education Module", command=lambda: education_module(CollapsibleFrame(root, text="Education")))
    open_education_button.grid(row=9, column=0, padx=10, pady=10)
    root.mainloop()
