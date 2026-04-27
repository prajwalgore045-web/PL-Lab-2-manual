import random
import tkinter as tk
from tkinter import messagebox

word_bank = [
    "python","coding","developer","programming","computer","keyboard","internet",
    "software","hardware","database","network","security","machine","learning",
    "artificial","intelligence","science","engineering","technology","algorithm",
    "function","variable","compiler","debugging","encryption","firewall","server",
    "client","browser","website","application","mobile","android","windows",
    "linux","ubuntu","terminal","command","script","automation","framework",
    "library","package","module","syntax","object","class","inheritance",
    "polymorphism","exception","interface","thread","process","virtual",
    "cloud","storage","backup","recovery","hosting","domain","api","json","html",
    "css","javascript","react","node","express","django","flask","streamlit",
    "bootstrap","tailwind","docker","kubernetes","git","github","version",
    "control","repository","commit","branch","merge","push","pull","clone",
    "request","response","protocol","http","https","ftp","smtp","tcp","udp",
    "encryption","hashing","authentication","authorization","token","session",
    "cookie","cache","buffer","queue","stack","array","linkedlist","tree",
    "graph","searching","sorting","binary","linear","recursion","iteration",
    "dynamic","greedy","backtracking","optimization","testing","deployment",
    "monitoring","logging","analytics","visualization","dashboard","interface",
    "frontend","backend","fullstack","devops","agile","scrum","kanban","waterfall"
]

word = random.choice(word_bank)
guessed_word_list = ['_'] * len(word)
attempts = 10
guessed_letters = []


def update_display():
    word_label.config(text=" ".join(guessed_word_list))
    attempts_label.config(text=f"Attempts Left: {attempts}")
    guessed_label.config(text="Guessed: " + ", ".join(guessed_letters))


def check_guess():
    global attempts

    guess = entry.get().lower()
    entry.delete(0, tk.END)

    if len(guess) != 1 or not guess.isalpha():
        messagebox.showwarning("Invalid", "Enter only ONE letter!")
        return

    if guess in guessed_letters:
        messagebox.showinfo("Repeated", "Already guessed!")
        return

    guessed_letters.append(guess)

    if guess in word:
        for i in range(len(word)):
            if word[i] == guess:
                guessed_word_list[i] = guess
    else:
        attempts -= 1

    update_display()

    if "_" not in guessed_word_list:
        messagebox.showinfo("Winner 🎉", f"You guessed: {word}")
        reset_game()

    elif attempts == 0:
        messagebox.showerror("Game Over ❌", f"Word was: {word}")
        reset_game()


def reset_game():
    global word, guessed_word_list, attempts, guessed_letters

    word = random.choice(word_bank)
    guessed_word_list = ['_'] * len(word)
    attempts = 10
    guessed_letters = []

    update_display()


root = tk.Tk()
root.title("Word Guessing Game")
root.geometry("450x500")
root.config(bg="#E3F2FD")


title = tk.Label(
    root,
    text="🎮 Word Guessing Game",
    font=("Arial", 22, "bold"),
    bg="#E3F2FD",
    fg="#F8AAE3"
)
title.pack(pady=15)


word_label = tk.Label(
    root,
    text=" ".join(guessed_word_list),
    font=("Arial", 28, "bold"),
    bg="#E3F2FD"
)
word_label.pack(pady=20)


attempts_label = tk.Label(
    root,
    text=f"Attempts Left: {attempts}",
    font=("Arial", 14),
    bg="#E3F2FD"
)
attempts_label.pack()


guessed_label = tk.Label(
    root,
    text="Guessed: ",
    font=("Arial", 12),
    bg="#E3F2FD"
)
guessed_label.pack(pady=8)


entry = tk.Entry(
    root,
    font=("Arial", 18),
    width=5,
    justify="center"
)
entry.pack(pady=15)


guess_btn = tk.Button(
    root,
    text="Guess",
    font=("Arial", 14),
    bg="#1976D2",
    fg="white",
    width=14,
    command=check_guess
)
guess_btn.pack(pady=6)


reset_btn = tk.Button(
    root,
    text="New Game",
    font=("Arial", 12),
    bg="#388E3C",
    fg="white",
    width=14,
    command=reset_game
)
reset_btn.pack(pady=10)


info = tk.Label(
    root,
    text="Type one letter and click Guess",
    font=("Arial", 11),
    bg="#E3F2FD"
)
info.pack(pady=12)


update_display()
root.mainloop()
