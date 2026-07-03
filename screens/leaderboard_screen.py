# ==========================================================
# Leaderboard Screen
# Displays Top 10 Players
# ==========================================================

import tkinter as tk

from config.settings import *
from game.leaderboard import Leaderboard

from screens.welcome_screen import WelcomeScreen


class LeaderboardScreen:

    def __init__(self, root):

        self.root = root

        self.leaderboard = Leaderboard()

        self.build_ui()

    # ==================================================
    # Clear Window
    # ==================================================

    def clear_window(self):

        for widget in self.root.winfo_children():
            widget.destroy()

    # ==================================================
    # Build UI
    # ==================================================

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
            expand=True,
            padx=20,
            pady=20
        )

        # ----------------------------------------------
        # Title
        # ----------------------------------------------

        title = tk.Label(
            main_frame,
            text="🏅 LEADERBOARD 🏅",
            font=FONTS["title"],
            bg=COLORS["background"],
            fg=COLORS["warning"]
        )

        title.pack(
            pady=20
        )

        subtitle = tk.Label(
            main_frame,
            text="Top 10 Conquerors",
            font=FONTS["subtitle"],
            bg=COLORS["background"],
            fg=COLORS["muted_text"]
        )

        subtitle.pack(
            pady=(0, 20)
        )

        # ----------------------------------------------
        # Table Card
        # ----------------------------------------------

        table_card = tk.Frame(
            main_frame,
            bg=COLORS["card"],
            padx=20,
            pady=20
        )

        table_card.pack(
            fill="both",
            expand=False,
            pady=10
        )

        # ----------------------------------------------
        # Table Headers
        # ----------------------------------------------

        headers = [
            "Rank",
            "Player",
            "Score",
            "Accuracy",
            "Difficulty",
            "Date"
        ]

        for col, header in enumerate(headers):

            label = tk.Label(
                table_card,
                text=header,
                font=FONTS["heading"],
                bg=COLORS["card"],
                fg=COLORS["primary"],
                width=15
            )

            label.grid(
                row=0,
                column=col,
                padx=5,
                pady=10
            )

        # ----------------------------------------------
        # Load Scores
        # ----------------------------------------------

        scores = self.leaderboard.get_top_scores()

        if not scores:

            empty_label = tk.Label(
                table_card,
                text="No Scores Available Yet",
                font=FONTS["normal"],
                bg=COLORS["card"],
                fg=COLORS["danger"]
            )

            empty_label.grid(
                row=1,
                column=0,
                columnspan=6,
                pady=20
            )

        else:

            for row, score in enumerate(scores, start=1):

                values = [

                    row,

                    score["name"],

                    score["score"],

                    f'{score["accuracy"]}%',

                    score["difficulty"],

                    score["date"]
                ]

                for col, value in enumerate(values):

                    cell = tk.Label(
                        table_card,
                        text=value,
                        font=FONTS["normal"],
                        bg=COLORS["card"],
                        fg=COLORS["text"],
                        width=15
                    )

                    cell.grid(
                        row=row,
                        column=col,
                        padx=5,
                        pady=5
                    )

        # ----------------------------------------------
        # Buttons
        # ----------------------------------------------

        button_frame = tk.Frame(
            main_frame,
            bg=COLORS["background"]
        )

        button_frame.pack(
            pady=20
        )

        back_button = tk.Button(
            button_frame,
            text="⬅ Back To Home",
            font=FONTS["button"],
            bg=COLORS["primary"],
            fg="black",
            bd=0,
            padx=20,
            pady=10,
            command=lambda: WelcomeScreen(self.root)
        )

        back_button.grid(
            row=0,
            column=0,
            padx=10
        )

        exit_button = tk.Button(
            button_frame,
            text="❌ Exit",
            font=FONTS["button"],
            bg=COLORS["danger"],
            fg="white",
            bd=0,
            padx=20,
            pady=10,
            command=self.root.destroy
        )

        exit_button.grid(
            row=0,
            column=1,
            padx=10
        )