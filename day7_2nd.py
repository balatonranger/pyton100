#!/usr/bin/env python3
"""
Graphical Hangman game using tkinter.
Save as hangman_gui.py and run: python hangman_gui.py
"""

import tkinter as tk
from tkinter import messagebox
import random
import string

# ----- Configuration -----
WORDS = [
    "python", "hangman", "interface", "canvas", "widget", "function",
    "variable", "algorithm", "computer", "program", "developer", "keyboard"
]
MAX_WRONG = 6  # number of wrong guesses allowed

# ----- Game logic class -----
class HangmanGame:
    def __init__(self, words, max_wrong=6):
        self.words = words
        self.max_wrong = max_wrong
        self.reset()

    def reset(self):
        self.secret = random.choice(self.words).lower()
        self.guessed = set()
        self.wrong = 0
        self.finished = False

    def guess(self, ch):
        ch = ch.lower()
        if self.finished or not ch or ch in self.guessed:
            return None
        self.guessed.add(ch)
        if ch not in self.secret:
            self.wrong += 1
        if self.is_won() or self.is_lost():
            self.finished = True
        return ch in self.secret

    def masked_word(self):
        return " ".join([c if c in self.guessed else "_" for c in self.secret])

    def is_won(self):
        return all(c in self.guessed for c in self.secret)

    def is_lost(self):
        return self.wrong >= self.max_wrong

# ----- GUI class -----
class HangmanGUI(tk.Tk):
    def __init__(self, game):
        super().__init__()
        self.title("Hangman")
        self.resizable(False, False)
        self.game = game

        # Canvas for drawing
        self.canvas = tk.Canvas(self, width=300, height=350, bg="white")
        self.canvas.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

        # Word label
        self.word_var = tk.StringVar()
        self.word_label = tk.Label(self, textvariable=self.word_var, font=("Consolas", 20))
        self.word_label.grid(row=1, column=0, columnspan=2, pady=(0,10))

        # Letter buttons frame
        self.buttons_frame = tk.Frame(self)
        self.buttons_frame.grid(row=2, column=0, columnspan=2, padx=10, pady=(0,10))

        # Create letter buttons
        self.letter_buttons = {}
        letters = string.ascii_uppercase
        for i, ch in enumerate(letters):
            btn = tk.Button(self.buttons_frame, text=ch, width=3, command=lambda c=ch: self.on_letter(c))
            btn.grid(row=i//9, column=i%9, padx=2, pady=2)
            self.letter_buttons[ch] = btn

        # Restart button
        self.restart_btn = tk.Button(self, text="Restart", command=self.restart)
        self.restart_btn.grid(row=3, column=0, sticky="ew", padx=10, pady=(0,10))

        # Quit button
        self.quit_btn = tk.Button(self, text="Quit", command=self.destroy)
        self.quit_btn.grid(row=3, column=1, sticky="ew", padx=10, pady=(0,10))

        # Bind keyboard
        self.bind("<Key>", self.on_key)

        # Initial draw
        self.update_ui()

    def on_letter(self, ch):
        if self.game.finished:
            return
        result = self.game.guess(ch)
        self.letter_buttons[ch].config(state="disabled")
        self.update_ui()
        if self.game.finished:
            self.show_result()

    def on_key(self, event):
        ch = event.char.upper()
        if ch in self.letter_buttons and self.letter_buttons[ch]['state'] == 'normal':
            self.on_letter(ch)

    def restart(self):
        self.game.reset()
        for btn in self.letter_buttons.values():
            btn.config(state="normal")
        self.update_ui()

    def update_ui(self):
        # Update masked word
        self.word_var.set(self.game.masked_word())

        # Redraw hangman
        self.canvas.delete("all")
        self.draw_gallows()
        self.draw_hangman(self.game.wrong)

    def show_result(self):
        if self.game.is_won():
            messagebox.showinfo("Hangman", f"You won! The word was: {self.game.secret}")
        else:
            messagebox.showinfo("Hangman", f"You lost. The word was: {self.game.secret}")
        # disable remaining buttons
        for btn in self.letter_buttons.values():
            btn.config(state="disabled")

    # ----- Drawing helpers -----
    def draw_gallows(self):
        # base
        self.canvas.create_line(20, 320, 280, 320, width=4)
        # upright
        self.canvas.create_line(60, 320, 60, 40, width=4)
        # beam
        self.canvas.create_line(60, 40, 180, 40, width=4)
        # rope
        self.canvas.create_line(180, 40, 180, 80, width=2)

    def draw_hangman(self, stage):
        # stage 1: head
        if stage >= 1:
            self.canvas.create_oval(155, 80, 205, 130, width=2)  # head
        # stage 2: body
        if stage >= 2:
            self.canvas.create_line(180, 130, 180, 210, width=2)  # body
        # stage 3: left arm
        if stage >= 3:
            self.canvas.create_line(180, 150, 150, 180, width=2)
        # stage 4: right arm
        if stage >= 4:
            self.canvas.create_line(180, 150, 210, 180, width=2)
        # stage 5: left leg
        if stage >= 5:
            self.canvas.create_line(180, 210, 155, 260, width=2)
        # stage 6: right leg
        if stage >= 6:
            self.canvas.create_line(180, 210, 205, 260, width=2)
        # optional: face when lost
        if stage >= self.game.max_wrong:
            # eyes
            self.canvas.create_line(165, 95, 175, 105, width=2)
            self.canvas.create_line(175, 95, 165, 105, width=2)
            self.canvas.create_line(185, 95, 195, 105, width=2)
            self.canvas.create_line(195, 95, 185, 105, width=2)
            # mouth
            self.canvas.create_arc(165, 105, 195, 125, start=0, extent=-180, style="arc", width=2)

# ----- Run the game -----
def main():
    random.seed()  # system time
    game = HangmanGame(WORDS, MAX_WRONG)
    app = HangmanGUI(game)
    app.mainloop()

if __name__ == "__main__":
    main()
