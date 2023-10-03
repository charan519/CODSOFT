import tkinter as tk

def calculate():
    try:
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
        operation = operation_var.get()

        if operation == "+":
            result = num1 + num2
        elif operation == "-":
            result = num1 - num2
        elif operation == "*":
            result = num1 * num2
        elif operation == "/":
            if num2 != 0:
                result = num1 / num2
            else:
                result_label.config(text="Error: Cannot divide by zero!")
                return
        else:
            result_label.config(text="Error: Invalid operation!")
            return

        result_label.config(text="Result: " + str(result))
    except ValueError:
        result_label.config(text="Error: Invalid input!")

# Create the main window
root = tk.Tk()
root.title("Simple Calculator")

# Create input fields for numbers
entry_num1 = tk.Entry(root)
entry_num1.pack(pady=10)

entry_num2 = tk.Entry(root)
entry_num2.pack(pady=10)

# Create operation choice
operation_var = tk.StringVar()
operation_choices = ["+", "-", "*", "/"]
operation_var.set("+")
operation_menu = tk.OptionMenu(root, operation_var, *operation_choices)
operation_menu.pack(pady=10)

# Create calculate button
calculate_button = tk.Button(root, text="Calculate", command=calculate)
calculate_button.pack(pady=10)

# Create result label
result_label = tk.Label(root, text="Result: ")
result_label.pack()

# Start the GUI event loop
root.mainloop()
