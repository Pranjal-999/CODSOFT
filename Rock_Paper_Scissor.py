import tkinter as tk
from tkinter import messagebox
import random

class RockPaperScissorsGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Rock-Paper-Scissors Game")

        self.user_score = 0
        self.computer_score = 0

        self.label_instructions = tk.Label(root, text="Choose one:", font=('Comic Sans MS', 16, 'bold'), fg='purple')
        self.label_instructions.pack(pady=10)

        self.button_rock = tk.Button(root, text="Rock", command=lambda: self.play_round("Rock"),
                                     font=('Arial', 14), fg='green', bg='lightgray')
        self.button_rock.pack(side=tk.LEFT, padx=10)

        self.button_paper = tk.Button(root, text="Paper", command=lambda: self.play_round("Paper"),
                                      font=('Arial', 14), fg='blue', bg='lightgray')
        self.button_paper.pack(side=tk.LEFT, padx=10)

        self.button_scissors = tk.Button(root, text="Scissors", command=lambda: self.play_round("Scissors"),
                                         font=('Arial', 14), fg='red', bg='lightgray')
        self.button_scissors.pack(side=tk.LEFT, padx=10)

        self.label_result = tk.Label(root, text="", font=('Verdana', 14, 'italic'), fg='darkblue')
        self.label_result.pack(pady=10)

        self.label_score = tk.Label(root, text="Score - You: 0, Computer: 0", font=('Helvetica', 12), fg='purple')
        self.label_score.pack(pady=10)

        self.button_play_again = tk.Button(root, text="Play Again", command=self.reset_game,
                                           font=('Arial', 12, 'bold'), fg='white', bg='purple')
        self.button_play_again.pack(pady=10)

    def play_round(self, user_choice):
        choices = ['Rock', 'Paper', 'Scissors']

        computer_choice = random.choice(choices)

        result = self.determine_winner(user_choice, computer_choice)

        self.label_result.config(text=f"Your choice: {user_choice}\nComputer's choice: {computer_choice}\nResult: {result}")

        if result == 'Win':
            self.user_score += 1
        elif result == 'Lose':
            self.computer_score += 1

        self.label_score.config(text=f"Score - You: {self.user_score}, Computer: {self.computer_score}")

        # Disable choice buttons after making a selection
        self.button_rock['state'] = tk.DISABLED
        self.button_paper['state'] = tk.DISABLED
        self.button_scissors['state'] = tk.DISABLED

    @staticmethod
    def determine_winner(user_choice, computer_choice):
        if user_choice == computer_choice:
            return 'Tie'
        elif (
            (user_choice == 'Rock' and computer_choice == 'Scissors') or
            (user_choice == 'Paper' and computer_choice == 'Rock') or
            (user_choice == 'Scissors' and computer_choice == 'Paper')
        ):
            return 'Win'
        else:
            return 'Lose'

    def reset_game(self):
        self.label_result.config(text="")
        self.button_rock['state'] = tk.NORMAL
        self.button_paper['state'] = tk.NORMAL
        self.button_scissors['state'] = tk.NORMAL

if __name__ == "__main__":
    root = tk.Tk()
    app = RockPaperScissorsGame(root)
    root.mainloop()
