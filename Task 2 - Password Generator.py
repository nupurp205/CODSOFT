import tkinter as tk
from tkinter import messagebox
import random
import string

# Function to generate password
def generate_password():
    try:
        length = int(length_entry.get())
        if length <= 0:
            raise ValueError
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid positive number.")
        return

    # Characters to use in password
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))

    result_entry.delete(0, tk.END)
    result_entry.insert(0, password)

# GUI Setup
root = tk.Tk()
root.title("🔐 Password Generator")
root.geometry("400x200")
root.resizable(False, False)

# Widgets
title_label = tk.Label(root, text="Password Generator", font=("Helvetica", 16, "bold"))
title_label.pack(pady=10)

length_label = tk.Label(root, text="Enter Password Length:")
length_label.pack()

length_entry = tk.Entry(root, justify='center', font=("Helvetica", 12))
length_entry.pack(pady=5)

generate_btn = tk.Button(root, text="Generate Password", command=generate_password, bg="green", fg="white")
generate_btn.pack(pady=10)

result_label = tk.Label(root, text="Generated Password:")
result_label.pack()

result_entry = tk.Entry(root, justify='center', font=("Helvetica", 12), width=30)
result_entry.pack(pady=5)

# Run the application
root.mainloop()
