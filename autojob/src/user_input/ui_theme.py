# File: src/user_input/ui_theme.py

import tkinter as tk
from tkinter import ttk

# Create a function to set the Material Design dark color theme and fonts
def set_material_design_theme(root):
    root.tk_setPalette(background='#121212', foreground='white', activeBackground='#6200ea', activeForeground='white')
    
    # Apply the theme to TButton (buttons)
    ttk.Style().configure('TButton', foreground='white', background='#6200ea', font=('Arial', 12))
    ttk.Style().map('TButton', background=[('active', '#6200ea')])

    # Apply the theme to TLabel (labels)
    ttk.Style().configure('TLabel', foreground='white', background='#121212', font=('Arial', 14, 'bold'))

    # Apply the theme to TFrame (frames)
    ttk.Style().configure('TFrame', background='#121212')

    # Apply the theme to TEntry (entry widgets)
    ttk.Style().configure('TEntry', fieldbackground='#121212', foreground='white', font=('Arial', 12))

    # Apply the theme to TText (text widgets)
    ttk.Style().configure('TText', fieldbackground='#121212', foreground='white', font=('Arial', 12))

    # Apply the theme to TCombobox (spinboxes)
    ttk.Style().configure('TCombobox', fieldbackground='#121212', foreground='white', font=('Arial', 12))
    ttk.Style().map('TCombobox', fieldbackground=[('readonly', '#121212')])
    
if __name__ == "__main__":
    # Create a root tkinter instance
    root = tk.Tk()
    
    # Call the set_material_design_theme function to apply the theme
    set_material_design_theme(root)
    
    # Run the main loop
    root.mainloop()
