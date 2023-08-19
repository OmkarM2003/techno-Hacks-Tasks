import tkinter as tk
import random


class RockPaperScissorsGame:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Rock-Paper-Scissors Game")
        self.root.geometry("400x350")
        self.root.configure(bg="#f9f9f9")

        self.score = 0
        self.game_over = False

        self.title_label = tk.Label(
            self.root,
            text="Rock-Paper-Scissors",
            font=("Helvetica", 20, "bold"),
            bg="#f9f9f9",
        )
        self.title_label.pack(pady=20)

        self.choices_frame = tk.Frame(self.root, bg="#f9f9f9")
        self.choices_frame.pack()

        self.choices = ["rock", "paper", "scissors"]
        self.buttons = []
        for choice in self.choices:
            button = tk.Button(
                self.choices_frame,
                text=choice.capitalize(),
                font=("Helvetica", 14),
                padx=20,
                pady=10,
                bd=0,
                bg="#e0e0e0",
                activebackground="#d3d3d3",
                command=lambda c=choice: self.play(c),
            )
            self.buttons.append(button)
            button.pack(side=tk.LEFT, padx=10)

        self.result_label = tk.Label(
            self.root, text="", font=("Helvetica", 14), bg="#f9f9f9"
        )
        self.result_label.pack(pady=20)

        self.score_label = tk.Label(
            self.root, text="Score: 0", font=("Helvetica", 14), bg="#f9f9f9"
        )
        self.score_label.pack()

        self.restart_button = tk.Button(
            self.root,
            text="Restart",
            font=("Helvetica", 12),
            bg="#e0e0e0",
            activebackground="#d3d3d3",
            command=self.restart_game,
        )
        self.restart_button.pack(pady=10)

        self.root.mainloop()

    def play(self, user_choice):
        if not self.game_over:
            choices = ["rock", "paper", "scissors"]
            computer_choice = random.choice(choices)

            result = ""
            result_color = ""

            if user_choice == computer_choice:
                result = "It's a tie!"
                result_color = "#333333"
            elif (
                (user_choice == "rock" and computer_choice == "scissors")
                or (user_choice == "paper" and computer_choice == "rock")
                or (user_choice == "scissors" and computer_choice == "paper")
            ):
                result = "You win!"
                result_color = "green"
                self.score += 1
            else:
                result = "You Lost!"
                result_color = "red"
                self.game_over = True

            self.result_label.config(
                text=f"Computer chose {computer_choice}. {result}", fg=result_color
            )
            self.score_label.config(text=f"Score: {self.score}")

            if self.game_over:
                self.restart_button.config(state=tk.NORMAL)

    def restart_game(self):
        self.score = 0
        self.game_over = False
        self.result_label.config(text="")
        self.score_label.config(text="Score: 0")
        self.restart_button.config(state=tk.DISABLED)


if __name__ == "__main__":
    game = RockPaperScissorsGame()
