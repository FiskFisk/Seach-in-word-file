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
root.title("Text in a Box with File Input")
root.geometry("300x250")  # Adjusted size to fit the button

# Create a frame (the box)
box = tk.Frame(root, bg="lightgray", width=200, height=100, highlightbackground="black", highlightthickness=1)
box.pack(pady=20)  # Add padding to center the box

# Add a label (the text inside the box)
label = tk.Label(box, text="This is some text!", bg="lightgray", font=("Arial", 12))
label.place(relx=0.5, rely=0.5, anchor="center")  # Center the label within the box

# Add a button below the box
file_button = tk.Button(root, text="Select a File", command=select_file, font=("Arial", 10))
file_button.pack(pady=20)  # Add padding to separate the button from the box

# Run the application
root.mainloop()
