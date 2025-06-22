# %%
import tkinter as tk
from tkinter import messagebox

# Function to perform the calculation
def calculate():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        operation = operation_var.get()

        if operation == "+":
            result = num1 + num2
        elif operation == "-":
            result = num1 - num2
        elif operation == "*":
            result = num1 * num2
        elif operation == "/":
            if num2 == 0:
                raise ZeroDivisionError("Cannot divide by zero.")
            result = num1 / num2
        elif operation == "%":
            result = num1 % num2
        else:
            raise ValueError("Invalid operation.")

        result_label.config(text=f"Result: {result}")
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numbers.")
    except ZeroDivisionError as e:
        messagebox.showerror("Math Error", str(e))

# Function to clear all input and result
def clear():
    entry1.delete(0, tk.END)
    entry2.delete(0, tk.END)
    operation_var.set("+")
    result_label.config(text="Result:")

# GUI setup
window = tk.Tk()
window.title("Simple GUI Calculator")
window.geometry("300x300")
window.config(padx=20, pady=20)

# Input fields
tk.Label(window, text="Enter first number:").pack()
entry1 = tk.Entry(window)
entry1.pack()

tk.Label(window, text="Enter second number:").pack()
entry2 = tk.Entry(window)
entry2.pack()

# Operation dropdown
tk.Label(window, text="Select operation:").pack()
operation_var = tk.StringVar(window)
operation_var.set("+")  # default value
operation_menu = tk.OptionMenu(window, operation_var, "+", "-", "*", "/", "%")
operation_menu.pack()

# Buttons
tk.Button(window, text="Calculate", command=calculate).pack(pady=10)
tk.Button(window, text="Clear", command=clear).pack()

# Result display
result_label = tk.Label(window, text="Result:", font=("Arial", 12))
result_label.pack(pady=10)

# Start the GUI loop
window.mainloop()



