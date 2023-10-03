import tkinter as tk
import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def generate_and_display_password():
    try:
        length = int(length_entry.get())
        if length <= 0:
            result_label.config(text="Password length must be greater than 0.")
            return
        
        password = generate_password(length)
        result_label.config(text="Generated Password: " + password)
    except ValueError:
        result_label.config(text="Invalid input. Please enter a valid number.")

# Create the main window
root = tk.Tk()
root.title("Password Generator")

# Create input field for password length
length_label = tk.Label(root, text="Enter Password Length:")
length_label.pack(pady=10)

length_entry = tk.Entry(root)
length_entry.pack(pady=5)

# Create generate button
generate_button = tk.Button(root, text="Generate Password", command=generate_and_display_password)
generate_button.pack(pady=10)

# Create result label
result_label = tk.Label(root, text="")
result_label.pack()

# Start the GUI event loop
root.mainloop()
