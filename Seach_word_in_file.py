import tkinter as tk
from tkinter import filedialog

# Function to handle file selection and display its content
def select_file():
    file_path = filedialog.askopenfilename(
        title="Select a File",
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
    )
    if file_path:
        try:
            with open(file_path, 'r') as file:
                content = file.read()  # Read the file's content
                text_box.config(text=content)  # Update the label with the file's content
        except Exception as e:
            text_box.config(text="Error reading file!")  # Display an error if file can't be read
            print(f"Error: {e}")

# Create the main application window
root = tk.Tk()
root.title("Resizable Box with File Display")
root.geometry("500x400")  # Initial size of the window

# Configure the grid for resizing
root.rowconfigure(0, weight=1)  # The box row
root.rowconfigure(1, weight=0)  # The button row (fixed size)
root.columnconfigure(0, weight=1)  # Center column for both widgets

# Create a frame (the resizable box)
box = tk.Frame(root, bg="lightgray", highlightbackground="black", highlightthickness=1)
box.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)  # Expand in all directions

# Add a label (the text inside the box)
text_box = tk.Label(
    box,
    text="This is some text!",
    bg="lightgray",
    font=("Arial", 12),
    wraplength=450,  # Wrap text based on box width
    justify="left",  # Align text to the left
    anchor="nw"  # Align text to the top-left corner of the box
)
text_box.pack(fill="both", expand=True, padx=5, pady=5)  # Make the label fill the box

# Add a button below the box
file_button = tk.Button(root, text="Select a File", command=select_file, font=("Arial", 10))
file_button.grid(row=1, column=0, pady=10)  # Fixed position below the box

# Update the wraplength dynamically when the window resizes
def update_wraplength(event):
    text_box.config(wraplength=box.winfo_width() - 10)  # Adjust wraplength to box width

box.bind("<Configure>", update_wraplength)  # Bind the resize event to update wraplength

# Run the application
root.mainloop()
