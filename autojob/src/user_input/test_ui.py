import tkinter as tk
from tkinter import Text

def calculate_dimensions():
    # Get screen width and height
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    # Define ratios with thinner margins and gutter
    margin_ratio = 0.05  # Adjust as needed for thinner margins
    gutter_ratio = 0.05  # Adjust as needed for thinner gutter
    main_area_ratio = 0.9  # Adjust as needed

    # Calculate sizes
    margin_size = int(screen_width * margin_ratio)
    gutter_size = int(screen_width * gutter_ratio)
    main_area_size = int(screen_width * main_area_ratio / 2)  # Divide by 2 for two equal main areas

    return margin_size, gutter_size, main_area_size

# Create the main Tkinter window
root = tk.Tk()

# Call the function to calculate dimensions
margin_size, gutter_size, main_area_size = calculate_dimensions()

# Create frames for main areas
frame1 = tk.Frame(root, width=main_area_size, height=root.winfo_screenheight(), bg="lightblue")
frame1.pack(side=tk.LEFT, padx=(margin_size, 0))  # Only apply left margin

frame2 = tk.Frame(root, width=main_area_size, height=root.winfo_screenheight(), bg="lightgreen")
frame2.pack(side=tk.LEFT, padx=(gutter_size, margin_size))  # Gutter in the middle, apply right margin

# Add placeholder text to main areas
text_area1 = Text(frame1, wrap=tk.WORD, bg="lightblue")
text_area1.insert(tk.END, "Lorem Ipsum Text - Main Area 1")
text_area1.pack(expand=True, fill=tk.BOTH)

text_area2 = Text(frame2, wrap=tk.WORD, bg="lightgreen")
text_area2.insert(tk.END, "Lorem Ipsum Text - Main Area 2")
text_area2.pack(expand=True, fill=tk.BOTH)

root.title("Two Main Areas UI")
root.geometry(f"{root.winfo_screenwidth()}x{root.winfo_screenheight()}")

root.mainloop()
