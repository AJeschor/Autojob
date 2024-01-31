# File: autojob/src/user_input/project_component.py

import tkinter as tk
from ui_theme import set_material_design_theme
from ui_elements import create_heading_frame, create_singleline_textbox, create_date_selection, create_multiline_textbox, create_button

def project_module(parent_frame):
    # Create a heading frame within the collapsible frame
    heading_frame = create_heading_frame(parent_frame, "Projects & Research")

    # Create single-line text boxes with StringVar
    project_name_var = tk.StringVar()
    project_name_text = create_singleline_textbox(parent_frame, "Project Name", width=30)
    project_name_text.config(textvariable=project_name_var)

    project_link_var = tk.StringVar()
    project_link_text = create_singleline_textbox(parent_frame, "Project Link", width=30)
    project_link_text.config(textvariable=project_link_var)

    project_role_var = tk.StringVar()
    project_role_text = create_singleline_textbox(parent_frame, "Project Role", width=30)
    project_role_text.config(textvariable=project_role_var)

    # Create date selection sections
    start_month = tk.StringVar()
    start_year = tk.StringVar()
    end_month = tk.StringVar()
    end_year = tk.StringVar()
    create_date_selection(parent_frame, "Start Date", start_month, start_year)
    create_date_selection(parent_frame, "End Date", end_month, end_year)

    # Create a multi-line text box
    project_details = create_multiline_textbox(parent_frame, "Project Details (put each entry on its own line):", height=20, width=50)

    # Create a button with a custom function
    submit_button = create_button(parent_frame, "Submit Project", lambda: get_projects(project_name_var, project_link_var, project_role_var, project_details, start_month, start_year, end_month, end_year))

    # Adjust the placement of the button below the multi-line text box
    submit_button.grid(row=parent_frame.grid_size()[1], column=0, padx=10, pady=10)

if __name__ == "__main__":
    # You can add a button to open the collapsible experience module in the main window
    open_experience_button = tk.Button(root, text="Open Projects Module", command=lambda: experience_module(CollapsibleFrame(root, text="Projects & Research")))
    open_experience_button.grid(row=8, column=0, padx=10, pady=10)
    root.mainloop()
