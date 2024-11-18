import customtkinter as ctk
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
                text_box.delete("1.0", ctk.END)  # Clear existing content
                text_box.insert(ctk.END, content)  # Insert new content
        except UnicodeDecodeError:
            # If UTF-8 fails, try with 'latin1' encoding (common fallback)
            try:
                with open(file_path, 'r', encoding='latin1') as file:
                    content = file.read()
                    text_box.delete("1.0", ctk.END)  # Clear existing content
                    text_box.insert(ctk.END, content)
            except Exception as e:
                text_box.delete("1.0", ctk.END)
                text_box.insert(ctk.END, "Error reading file!")  # Display a generic error
                print(f"Error: {e}")
        except Exception as e:
            text_box.delete("1.0", ctk.END)
            text_box.insert(ctk.END, "Error reading file!")  # Display a generic error
            print(f"Error: {e}")

# Initialize the CustomTkinter application
ctk.set_appearance_mode("System")  # Use system theme (can also be "Dark" or "Light")
ctk.set_default_color_theme("blue")  # Set color theme (e.g., "blue", "green")

app = ctk.CTk()  # Create the main application window
app.title("CustomTkinter File Viewer")
app.geometry("600x400")  # Set initial size

# Configure grid layout
app.grid_rowconfigure(0, weight=1)  # Row for the text box (resizable)
app.grid_rowconfigure(1, weight=0)  # Row for the button (fixed size)
app.grid_columnconfigure(0, weight=1)  # Single column layout

# Create a frame for the text box
text_frame = ctk.CTkFrame(app, corner_radius=10)
text_frame.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

# Add a scrollable Text widget
text_box = ctk.CTkTextbox(
    text_frame,
    wrap="word",  # Wrap text at word boundaries
    font=("Arial", 12),
    corner_radius=10,
    activate_scrollbars=True  # Enable scrolling
)
text_box.pack(fill="both", expand=True, padx=5, pady=5)

# Add a button to select a file
file_button = ctk.CTkButton(
    app,
    text="Select a File",
    command=select_file,
    font=("Arial", 12),
    corner_radius=8
)
file_button.grid(row=1, column=0, pady=10)

# Run the application
app.mainloop()
