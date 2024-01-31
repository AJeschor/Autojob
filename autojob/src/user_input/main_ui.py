# File: autojob/src/user_input/main_ui.py

import os
import json
import tkinter as tk
from tkinter import ttk
from ui_theme import set_material_design_theme
from ui_functions import update_structure, get_data, get_experience, get_projects, get_education
from ui_elements import create_heading_frame, create_singleline_textbox, create_multiline_textbox
from education_component import education_module
from project_component import project_module
from experience_component import experience_module

class CollapsibleFrame(ttk.Frame):
    def __init__(self, master, text="", *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        self.is_expanded = tk.BooleanVar(value=True)

        frame_label = ttk.Label(self, text=text)
        frame_label.grid(row=0, column=0, sticky="w", columnspan=2)  # Set columnspan to 2

        toggle_button = ttk.Button(self, text="Collapse/Expand", command=self.toggle)
        toggle_button.grid(row=0, column=1, sticky="e")

        self.columnconfigure(0, weight=1)

    def toggle(self):
        if self.is_expanded.get():
            self.grid_remove()
        else:
            self.grid()
        self.is_expanded.set(not self.is_expanded.get())

root = tk.Tk()
root.title("Main Window")
set_material_design_theme(root)

# Create a heading frame
heading_frame = create_heading_frame(root, "Resume Input")
heading_frame.grid(row=0, column=0, sticky="w")  # Set row and column for the heading frame

# Full Name
full_name_textbox = create_singleline_textbox(root, "User Name", width=30)
full_name_textbox.grid(row=0, column=0, sticky="w")  # Set row and column for the full_name_textbox

# User Location
user_location_textbox = create_singleline_textbox(root, "User Location", width=30)
user_location_textbox.grid(row=0, column=0, sticky="w")  # Set row and column for the user_location_textbox

# Email
email = create_singleline_textbox(root, "Email", width=30)
email.grid(row=0, column=0, sticky="w")  # Set row and column for the email

# Phone Number
phone_number = create_singleline_textbox(root, "Phone Number", width=30)
phone_number.grid(row=0, column=0, sticky="w")  # Set row and column for the phone_number

# LinkedIn Profile
linkedin_profile_url = create_singleline_textbox(root, "LinkedIn Profile", width=30)
linkedin_profile_url.grid(row=0, column=0, sticky="w")  # Set row and column for the linkedin_profile_url

# GitHub Profile
github_profile_url = create_singleline_textbox(root, "GitHub Profile", width=30)
github_profile_url.grid(row=0, column=0, sticky="w")  # Set row and column for the github_profile_url

# Skills Textbox
skills = create_multiline_textbox(root, "Skills (put each entry on its own line):", height=20, width=50)
skills.grid(row=0, column=0, sticky="w")  # Set row and column for the skills

root.mainloop()
