import tkinter as tk
from tkinter import messagebox

# Functions for calculations
def add():
    try:
        result.set(float(entry1.get()) + float(entry2.get()))
    except ValueError:
        messagebox.showerror("Invalid input", "Please enter valid numbers.")

def subtract():
    try:
        result.set(float(entry1.get()) - float(entry2.get()))
    except ValueError:
        messagebox.showerror("Invalid input", "Please enter valid numbers.")

def multiply():
    try:
        result.set(float(entry1.get()) * float(entry2.get()))
    except ValueError:
        messagebox.showerror("Invalid input", "Please enter valid numbers.")

def divide():
    try:
        if float(entry2.get()) == 0:
            messagebox.showerror("Math Error", "Cannot divide by zero.")
        else:
            result.set(float(entry1.get()) / float(entry2.get()))
    except ValueError:
        messagebox.showerror("Invalid input", "Please enter valid numbers.")

# Main window
root = tk.Tk()
root.title("Calculator")
root.geometry("300x350")  # Window size

# Center all columns
root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=1)

# Inputs
tk.Label(root, text="First number:").grid(row=0, column=0, columnspan=2, pady=10)
entry1 = tk.Entry(root, justify='center')
entry1.grid(row=1, column=0, columnspan=2, padx=30)

tk.Label(root, text="Second number:").grid(row=2, column=0, columnspan=2, pady=10)
entry2 = tk.Entry(root, justify='center')
entry2.grid(row=3, column=0, columnspan=2, padx=30)

# Buttons
tk.Button(root, text="Add", width=12, command=add).grid(row=4, column=0, pady=10)
tk.Button(root, text="Subtract", width=12, command=subtract).grid(row=4, column=1)
tk.Button(root, text="Multiply", width=12, command=multiply).grid(row=5, column=0)
tk.Button(root, text="Divide", width=12, command=divide).grid(row=5, column=1)

# Result display
tk.Label(root, text="Result:").grid(row=6, column=0, columnspan=2, pady=10)
result = tk.StringVar()
tk.Entry(root, textvariable=result, state='readonly', justify='center').grid(row=7, column=0, columnspan=2, padx=30)

# Footer
footer = tk.Label(root, text="Made with ❤️ by Ayyoub", fg="gray")
footer.grid(row=8, column=0, columnspan=2, pady=20)

# Run the GUI
root.mainloop()
