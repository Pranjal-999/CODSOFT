import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import random
import string

class PasswordGeneratorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Password Generator")

        self.label_length = ttk.Label(root, text="Enter the length of the password:", font=('Arial', 12))
        self.label_length.pack(pady=10)

        self.entry_length = ttk.Entry(root, font=('Arial', 12))
        self.entry_length.pack(pady=10)

        self.generate_button = ttk.Button(root, text="Generate Password", command=self.generate_password, style='TButton')
        self.generate_button.pack(pady=10)

        self.label_generated_password = ttk.Label(root, text="", font=('Arial', 12, 'italic'))
        self.label_generated_password.pack(pady=10)

    def generate_password(self):
        try:
            length = int(self.entry_length.get())

            if length <= 0:
                messagebox.showinfo("Invalid Length", "Please enter a positive integer.")
                return

            characters = string.ascii_letters + string.digits + string.punctuation
            password = ''.join(random.choice(characters) for _ in range(length))

            self.label_generated_password.config(text=f"Generated Password: {password}")

        except ValueError:
            messagebox.showinfo("Invalid Input", "Please enter a valid integer for password length.")

if __name__ == "__main__":
    root = tk.Tk()
    app = PasswordGeneratorApp(root)

    # Styling the button
    style = ttk.Style()
    style.configure('TButton', font=('Arial', 12))

    root.mainloop()
