import tkinter as tk

# Create the main application window
root = tk.Tk()
root.title("Text in a Box")
root.geometry("300x200")  # Set the size of the window

# Create a frame (the box)
box = tk.Frame(root, bg="lightgray", width=200, height=100, highlightbackground="black", highlightthickness=1)
box.pack(pady=50)  # Add padding to center the box vertically

# Add a label (the text inside the box)
label = tk.Label(box, text="This is some text!", bg="lightgray", font=("Arial", 12))
label.place(relx=0.5, rely=0.5, anchor="center")  # Center the label within the box

# Run the application
root.mainloop()
