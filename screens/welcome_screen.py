# Welcome Screen
# First screen shown when the application starts


import tkinter as tk
from tkinter import ttk
from config.settings import *

# Import next screen
from screens.quiz_screen import QuizScreen


class WelcomeScreen:

    def __init__(self, root):

        self.root = root

        self.player_name = tk.StringVar()

        self.difficulty = tk.StringVar(value="Easy")

        self.question_count = tk.IntVar(value=10)

        self.build_ui()

    
    # Clear Window
  

    def clear_window(self):

        for widget in self.root.winfo_children():
            widget.destroy()

  
    # Start Game
    

    def start_game(self):

        name = self.player_name.get().strip()

        if name == "":
            name = "Player"

        QuizScreen(
            self.root,
            player_name=name,
            difficulty=self.difficulty.get(),
            total_questions=self.question_count.get()
        )


    # Create UI


    def build_ui(self):

        self.clear_window()

        self.root.configure(
            bg=COLORS["background"]
        )

        main_frame = tk.Frame(
            self.root,
            bg=COLORS["background"]
        )

        main_frame.pack(
            fill="both",
            expand=True
        )


        # Title


        title = tk.Label(
            main_frame,
            text="⚔ OPERATION CONQUEST ⚔",
            font=FONTS["title"],
            fg=COLORS["primary"],
            bg=COLORS["background"]
        )

        title.pack(pady=(50, 10))

        subtitle = tk.Label(
            main_frame,
            text="Conquer Mathematics. Build Your Legacy.",
            font=FONTS["subtitle"],
            fg=COLORS["muted_text"],
            bg=COLORS["background"]
        )

        subtitle.pack(pady=(0, 30))


        # Main Card


        card = tk.Frame(
            main_frame,
            bg=COLORS["card"],
            padx=30,
            pady=30
        )

        card.pack()

        # Name


        tk.Label(
            card,
            text="Player Name",
            font=FONTS["heading"],
            bg=COLORS["card"],
            fg=COLORS["text"]
        ).pack(pady=10)

        name_entry = tk.Entry(
            card,
            textvariable=self.player_name,
            font=FONTS["normal"],
            width=25,
            justify="center"
        )

        name_entry.pack(pady=10)


        # Difficulty


        tk.Label(
            card,
            text="Difficulty",
            font=FONTS["heading"],
            bg=COLORS["card"],
            fg=COLORS["text"]
        ).pack(pady=(20, 10))

        difficulty_frame = tk.Frame(
            card,
            bg=COLORS["card"]
        )

        difficulty_frame.pack()

        for difficulty in ["Easy", "Medium", "Hard"]:

            tk.Radiobutton(
                difficulty_frame,
                text=difficulty,
                variable=self.difficulty,
                value=difficulty,
                font=FONTS["normal"],
                bg=COLORS["card"],
                fg=COLORS["text"],
                selectcolor=COLORS["card_light"]
            ).pack(
                side="left",
                padx=10
            )

        # Question Count


        tk.Label(
            card,
            text="Questions",
            font=FONTS["heading"],
            bg=COLORS["card"],
            fg=COLORS["text"]
        ).pack(pady=(20, 10))

        ttk.Combobox(
            card,
            textvariable=self.question_count,
            values=[10, 15, 20],
            state="readonly",
            width=10
        ).pack()


        # Start Button


        start_button = tk.Button(
            card,
            text="🚀 Start Conquest",
            font=FONTS["button"],
            bg=COLORS["primary"],
            fg="black",
            bd=0,
            padx=20,
            pady=10,
            command=self.start_game
        )

        start_button.pack(pady=30)

        name_entry.focus()