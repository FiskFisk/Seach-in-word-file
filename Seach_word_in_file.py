import customtkinter as ctk
from tkinter import filedialog, ttk
import tkinter as tk

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
                text_box.delete("1.0", tk.END)  # Clear existing content
                text_box.insert(tk.END, content)  # Insert new content
        except UnicodeDecodeError:
            # If UTF-8 fails, try with 'latin1' encoding (common fallback)
            try:
                with open(file_path, 'r', encoding='latin1') as file:
                    content = file.read()
                    text_box.delete("1.0", tk.END)  # Clear existing content
                    text_box.insert(tk.END, content)
            except Exception as e:
                text_box.delete("1.0", tk.END)
                text_box.insert(tk.END, "Error reading file!")  # Display a generic error
                print(f"Error: {e}")

# Function to highlight search term in the text box
def search_word():
    search_term = search_entry.get()
    if search_term:
        text_box.tag_remove("highlight", "1.0", tk.END)  # Remove previous highlights
        start_pos = "1.0"
        count = 0  # Initialize match count
        while True:
            start_pos = text_box.search(search_term, start_pos, stopindex=tk.END, nocase=True)
            if not start_pos:
                break
            end_pos = f"{start_pos}+{len(search_term)}c"
            text_box.tag_add("highlight", start_pos, end_pos)
            text_box.tag_configure("highlight", background="yellow", foreground="black")
            start_pos = end_pos  # Move start position after the found word
            count += 1  # Increment match count
        
        # Update match count label
        result_label.configure(text=f"Matches found: {count}")
    else:
        result_label.configure(text="No search term entered.")

# Initialize the CustomTkinter application
ctk.set_appearance_mode("System")  # Use system theme (can also be "Dark" or "Light")
ctk.set_default_color_theme("blue")  # Set color theme (e.g., "blue", "green")

app = ctk.CTk()  # Create the main application window
app.title("Seach word in file")
app.geometry("600x400")  # Set initial size

# Configure grid layout
app.grid_rowconfigure(0, weight=1)  # Row for the text box (resizable)
app.grid_rowconfigure(1, weight=0)  # Row for the search entry and button (fixed size)
app.grid_columnconfigure(0, weight=1)  # Single column layout

# Create a frame for the text box
text_frame = ctk.CTkFrame(app, corner_radius=10)
text_frame.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

# Add a styled scrollbar and scrollable Text widget
style = ttk.Style()
style.theme_use("clam")  # Use a modern theme
style.configure(
    "Vertical.TScrollbar",
    gripcount=0,
    background="lightgray",
    troughcolor="gray20",
    bordercolor="black",
    arrowcolor="black",
    relief="flat",
)

scrollbar = ttk.Scrollbar(text_frame, orient="vertical", style="Vertical.TScrollbar")
text_box = tk.Text(
    text_frame,
    wrap="word",  # Wrap text at word boundaries
    font=("Arial", 12),
    height=10,
    width=50,
    yscrollcommand=scrollbar.set  # Link the scrollbar to the text box
)
scrollbar.config(command=text_box.yview)
scrollbar.pack(side="right", fill="y")
text_box.pack(fill="both", expand=True, padx=5, pady=5)

# Create a frame for search input and button
search_frame = ctk.CTkFrame(app)
search_frame.grid(row=1, column=0, padx=10, pady=10, sticky="ew")

# Add a search entry box
search_entry = ctk.CTkEntry(search_frame, placeholder_text="Enter search term", font=("Arial", 12))
search_entry.pack(side="left", padx=5, pady=5, fill="x", expand=True)

# Add a search button
search_button = ctk.CTkButton(
    search_frame,
    text="Search",
    command=search_word,
    font=("Arial", 12),
    corner_radius=8
)
search_button.pack(side="right", padx=5, pady=5)

# Add a styled frame to display match count
result_frame = ctk.CTkFrame(app, corner_radius=10, border_width=1, border_color="gray")
result_frame.grid(row=2, column=0, padx=10, pady=5, sticky="ew")

result_label = ctk.CTkLabel(
    result_frame,
    text="Matches found: 0",
    font=("Arial", 12),
    anchor="w"
)
result_label.pack(fill="both", expand=True, padx=10, pady=5)

# Add a button to select a file
file_button = ctk.CTkButton(
    app,
    text="Select a File",
    command=select_file,
    font=("Arial", 12),
    corner_radius=8
)
file_button.grid(row=3, column=0, pady=10)

# Run the application
app.mainloop()
