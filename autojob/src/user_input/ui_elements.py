# File: autojob/src/user_input/ui_elements.py

import tkinter as tk
from tkinter import ttk

MONTHS = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sept", "Oct", "Nov", "Dec"]
YEARS = [str(i) for i in range(1950, 2050)]

# Function to create a month spinbox
def create_month_spinbox(parent_frame, month_variable):
    month_spinbox = ttk.Combobox(parent_frame, values=MONTHS, textvariable=month_variable)
    max_width = max(len(month) for month in MONTHS) + 2
    month_spinbox.config(width=max_width)
    month_spinbox.grid(sticky="we", padx=20)
    return month_spinbox

# Function to create a year spinbox
def create_year_spinbox(parent_frame, year_variable):
    year_spinbox = ttk.Combobox(parent_frame, values=YEARS, textvariable=year_variable)
    max_width = max(len(year) for year in YEARS) + 2
    year_spinbox.config(width=max_width)
    year_spinbox.grid(sticky="we", padx=20)
    return year_spinbox

# Function to create a date selection section
def create_date_selection(parent_frame, label_text, month_variable, year_variable):
    frame = tk.Frame(parent_frame)
    frame.grid(sticky="we", pady=10)

    label = tk.Label(frame, text=label_text, font=('Arial', 12))
    label.grid(sticky="w", padx=20)

    create_month_spinbox(frame, month_variable)
    create_year_spinbox(frame, year_variable)

# Function to create a single-line text box
def create_singleline_textbox(parent_frame, label_text, width):
    frame = tk.Frame(parent_frame)
    frame.grid(sticky="we", padx=20, pady=(10, 0))

    label = tk.Label(frame, text=label_text, font=('Arial', 14, 'bold'))
    label.grid(sticky="w")

    entry = tk.Entry(frame, width=width)
    entry.grid(sticky="we", pady=(0, 10))

    return entry

# Function to create a multi-line text box
def create_multiline_textbox(parent_frame, label_text, height, width):
    frame = tk.Frame(parent_frame)
    frame.grid(sticky="we", padx=20, pady=(10, 0))

    label = tk.Label(frame, text=label_text, font=('Arial', 14, 'bold'))
    label.grid(sticky="w")

    textbox = tk.Text(frame, height=height, width=width)
    textbox.grid(sticky="we", pady=(0, 10))

    return textbox

# Function to create a centered Header Title with more space
def create_heading_frame(parent_frame, title_label):
    header_frame = tk.Frame(parent_frame, bg='#121212')
    header_frame.grid(pady=(20, 10), sticky="we")  # Increased pady

    # Create a Label for the heading title
    heading_label = tk.Label(header_frame, text=title_label, font=('Arial', 18, 'bold'), fg='white', bg='#121212')
    heading_label.grid(sticky="we")

    return header_frame

# Function to create a button
def create_button(parent_frame, button_text, command):
    button = tk.Button(parent_frame, text=button_text, command=command, font=('Arial', 12))
    button.grid(sticky="we", padx=10, pady=10)

    return button
