import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

class CalculatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculator")

        self.label_num1 = ttk.Label(root, text="Enter the first number:", font=('Arial', 12))
        self.label_num1.pack(pady=10)

        self.entry_num1 = ttk.Entry(root, font=('Arial', 12))
        self.entry_num1.pack(pady=10)

        self.label_num2 = ttk.Label(root, text="Enter the second number:", font=('Arial', 12))
        self.label_num2.pack(pady=10)

        self.entry_num2 = ttk.Entry(root, font=('Arial', 12))
        self.entry_num2.pack(pady=10)

        self.label_operation = ttk.Label(root, text="Enter the operation (+, -, *, /):", font=('Arial', 12))
        self.label_operation.pack(pady=10)

        self.entry_operation = ttk.Entry(root, font=('Arial', 12))
        self.entry_operation.pack(pady=10)

        self.calculate_button = ttk.Button(root, text="Calculate", command=self.calculate, style='TButton')
        self.calculate_button.pack(pady=10)

        self.label_result = ttk.Label(root, text="", font=('Arial', 12))
        self.label_result.pack(pady=10)

    def calculate(self):
        try:
            num1 = float(self.entry_num1.get())
            num2 = float(self.entry_num2.get())
            operation = self.entry_operation.get()

            if operation == '+':
                result = num1 + num2
            elif operation == '-':
                result = num1 - num2
            elif operation == '*':
                result = num1 * num2
            elif operation == '/':
                if num2 == 0:
                    messagebox.showinfo("Division Error", "Cannot divide by zero.")
                    return
                result = num1 / num2
            else:
                messagebox.showinfo("Invalid Operation", "Please enter a valid operation (+, -, *, /).")
                return

            self.label_result.config(text=f"Result: {result}")

        except ValueError:
            messagebox.showinfo("Invalid Input", "Please enter valid numbers.")

if __name__ == "__main__":
    root = tk.Tk()
    app = CalculatorApp(root)

    # Styling the button
    style = ttk.Style()
    style.configure('TButton', font=('Arial', 12))

    root.mainloop()
