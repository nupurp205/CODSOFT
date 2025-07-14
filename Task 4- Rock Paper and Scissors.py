import tkinter as tk
from tkinter import messagebox
import random

# Global scores
user_score = 0
computer_score = 0

# Options and emojis
options = ['Rock', 'Paper', 'Scissors']
icons = {'Rock': '🪨', 'Paper': '📄', 'Scissors': '✂️'}

# Game logic
def play(user_choice):
    global user_score, computer_score

    computer_choice = random.choice(options)

    if user_choice == computer_choice:
        result = "It's a Tie!"
    elif (
        (user_choice == "Rock" and computer_choice == "Scissors") or
        (user_choice == "Scissors" and computer_choice == "Paper") or
        (user_choice == "Paper" and computer_choice == "Rock")
    ):
        result = "You Win!"
        user_score += 1
    else:
        result = "Computer Wins!"
        computer_score += 1

    update_display(user_choice, computer_choice, result)

# Update display with choices and result
def update_display(user, comp, result):
    user_choice_label.config(text=f"You chose: {icons[user]} {user}")
    comp_choice_label.config(text=f"Computer chose: {icons[comp]} {comp}")
    result_label.config(text=result)
    score_label.config(text=f"Score — You: {user_score}  |  Computer: {computer_score}")

# Reset game
def reset_game():
    global user_score, computer_score
    user_score = 0
    computer_score = 0
    result_label.config(text="")
    user_choice_label.config(text="")
    comp_choice_label.config(text="")
    score_label.config(text="Score — You: 0  |  Computer: 0")

# --- GUI Setup ---
root = tk.Tk()
root.title("🎮 Rock Paper Scissors Game")
root.state("zoomed")  # Maximize window

# --- Styling ---
title_font = ("Helvetica", 28, "bold")
button_font = ("Helvetica", 16)
result_font = ("Helvetica", 20, "bold")
label_font = ("Helvetica", 16)

# --- Title ---
tk.Label(root, text="Rock Paper Scissors", font=title_font, fg="#333").pack(pady=30)

# --- Choice Buttons ---
button_frame = tk.Frame(root)
button_frame.pack(pady=20)

tk.Button(button_frame, text="🪨 Rock", font=button_font, width=12, bg="#FFDDC1", command=lambda: play("Rock")).grid(row=0, column=0, padx=20)
tk.Button(button_frame, text="📄 Paper", font=button_font, width=12, bg="#C1FFD7", command=lambda: play("Paper")).grid(row=0, column=1, padx=20)
tk.Button(button_frame, text="✂️ Scissors", font=button_font, width=12, bg="#C1D4FF", command=lambda: play("Scissors")).grid(row=0, column=2, padx=20)

# --- Output Area ---
output_frame = tk.Frame(root)
output_frame.pack(pady=40)

user_choice_label = tk.Label(output_frame, text="", font=label_font)
user_choice_label.pack(pady=5)

comp_choice_label = tk.Label(output_frame, text="", font=label_font)
comp_choice_label.pack(pady=5)

result_label = tk.Label(output_frame, text="", font=result_font, fg="#222")
result_label.pack(pady=10)

score_label = tk.Label(root, text="Score — You: 0  |  Computer: 0", font=label_font)
score_label.pack(pady=10)

# --- Reset Button ---
tk.Button(root, text="🔁 Play Again", font=button_font, bg="#FFB6B6", command=reset_game).pack(pady=20)

# Run the app
root.mainloop()
