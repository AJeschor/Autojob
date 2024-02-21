# File: src/user_input/project_module.py

import tkinter as tk
from ui_theme import set_material_design_theme
from ui_functions import create_heading_frame, create_singleline_textbox, create_date_selection, create_multiline_textbox, create_button

PROJECTS = []

def get_projects(main_window, project_name_var, project_link_var, project_role_var, project_details, project_start_date, project_end_date):
    print("Getting project data...")
    project_data = {
        "Project Title": project_name_var.get().strip(),
        "Project Link": project_link_var.get().strip(),
        "Role": project_role_var.get().strip(),
        "Start Date": project_start_date,
        "End Date": project_end_date,
        "Description": project_details.get("1.0", tk.END).strip().split("\n")
    }

    PROJECTS.append(project_data)
    print("Project added successfully:", project_data)
    
    # Clear the input fields after submission
    project_name_var.set("")
    project_link_var.set("")
    project_role_var.set("")
    project_details.delete("1.0", tk.END)

def project_module(main_window):
    def on_submit():
        project_start_date = f"{start_month.get()} {start_year.get()}"
        project_end_date = f"{end_month.get()} {end_year.get()}"
        print("Submitting project...")
        get_projects(
            main_window,
            project_name_var,
            project_link_var,
            project_role_var,
            project_details,
            project_start_date,
            project_end_date
        )

    # Create a new window (Toplevel) for the projects module
    project_window = tk.Toplevel(main_window)
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
    root = tk.Tk()
    # You can add a button to open the project module in the main window
    open_project_button = tk.Button(root, text="Open Projects Module", command=lambda: project_module(root))
    open_project_button.pack()
    root.mainloop()
