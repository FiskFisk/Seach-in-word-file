import tkinter as tk
from tkinter import filedialog

# Function to handle file selection
def select_file():
    file_path = filedialog.askopenfilename(
        title="Select a File",
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
    )
    if file_path:
        print(f"Selected file: {file_path}")

# Create the main application window
root = tk.Tk()
root.title("Resizable Box with File Input")
root.geometry("400x300")  # Initial size of the window

# Configure the grid for resizing
root.rowconfigure(0, weight=1)  # The box row
root.rowconfigure(1, weight=0)  # The button row (fixed size)
root.columnconfigure(0, weight=1)  # Center column for both widgets

# Create a frame (the resizable box)
box = tk.Frame(root, bg="lightgray", highlightbackground="black", highlightthickness=1)
box.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)  # Expand in all directions

# Add a label (the text inside the box)
label = tk.Label(box, text="This is some text!", bg="lightgray", font=("Arial", 12))
label.place(relx=0.5, rely=0.5, anchor="center")  # Center the label within the box

# Add a button below the box
file_button = tk.Button(root, text="Select a File", command=select_file, font=("Arial", 10))
file_button.grid(row=1, column=0, pady=10)  # Fixed position below the box

# Run the application
root.mainloop()
