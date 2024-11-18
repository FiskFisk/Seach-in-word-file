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
            # Attempt to open the file with UTF-8 encoding
            with open(file_path, 'r', encoding='utf-8') as file:
                content = file.read()  # Read the file's content
                text_box.delete(1.0, tk.END)  # Clear existing content
                text_box.insert(tk.END, content)  # Insert new content
        except UnicodeDecodeError:
            # If UTF-8 fails, try with 'latin1' encoding (common fallback)
            try:
                with open(file_path, 'r', encoding='latin1') as file:
                    content = file.read()
                    text_box.delete(1.0, tk.END)  # Clear existing content
                    text_box.insert(tk.END, content)
            except Exception as e:
                text_box.delete(1.0, tk.END)
                text_box.insert(tk.END, "Error reading file!")  # Display a generic error
                print(f"Error: {e}")
        except Exception as e:
            text_box.delete(1.0, tk.END)
            text_box.insert(tk.END, "Error reading file!")  # Display a generic error
            print(f"Error: {e}")

# Create the main application window
root = tk.Tk()
root.title("Resizable Box with Scrollable Text")
root.geometry("500x400")  # Initial size of the window

# Configure the grid for resizing
root.rowconfigure(0, weight=1)  # The box row
root.rowconfigure(1, weight=0)  # The button row (fixed size)
root.columnconfigure(0, weight=1)  # Center column for both widgets

# Create a frame (the resizable box)
box = tk.Frame(root, bg="lightgray", highlightbackground="black", highlightthickness=1)
box.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)  # Expand in all directions

# Add a Scrollbar
scrollbar = tk.Scrollbar(box)
scrollbar.pack(side="right", fill="y")  # Attach scrollbar to the right of the box

# Add a Text widget (scrollable text box)
text_box = tk.Text(
    box,
    wrap="word",  # Wrap text at words
    font=("Arial", 12),
    yscrollcommand=scrollbar.set,  # Link scrollbar to Text widget
    bg="lightgray"
)
text_box.pack(fill="both", expand=True, padx=5, pady=5)  # Make the Text widget fill the box

# Configure the scrollbar to work with the Text widget
scrollbar.config(command=text_box.yview)

# Add a button below the box
file_button = tk.Button(root, text="Select a File", command=select_file, font=("Arial", 10))
file_button.grid(row=1, column=0, pady=10)  # Fixed position below the box

# Run the application
root.mainloop()
