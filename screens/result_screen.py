# ==========================================================
# Result Screen
# Displays final score, achievements and statistics
# ==========================================================

import tkinter as tk

from config.settings import *

from game.achievements import AchievementManager
from game.leaderboard import Leaderboard

from screens.leaderboard_screen import LeaderboardScreen
from screens.welcome_screen import WelcomeScreen


class ResultScreen:

    def __init__(
            self,
            root,
            player_name,
            difficulty,
            score,
            total_questions,
            statistics):

        self.root = root

        self.player_name = player_name
        self.difficulty = difficulty

        self.score = score
        self.total_questions = total_questions

        self.statistics = statistics

        self.achievement_manager = AchievementManager()

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

        accuracy = self.statistics.accuracy()

        avg_time = self.statistics.average_response_time()

        duration = self.statistics.total_duration()

        rating = self.achievement_manager.get_rating(
            accuracy
        )

        achievements = self.achievement_manager.get_achievements(
            accuracy=accuracy,
            avg_time=avg_time,
            difficulty=self.difficulty,
            correct=self.statistics.correct,
            total_questions=self.total_questions
        )

        # ----------------------------------------------
        # Save Score To Leaderboard
        # ----------------------------------------------

        self.leaderboard.save_score(
            player_name=self.player_name,
            score=self.score,
            accuracy=accuracy,
            difficulty=self.difficulty
        )

        # ----------------------------------------------
        # Main Window
        # ----------------------------------------------

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
            text="🏆 CONQUEST COMPLETE 🏆",
            font=FONTS["title"],
            bg=COLORS["background"],
            fg=COLORS["success"]
        )

        title.pack(
            pady=20
        )

        # ----------------------------------------------
        # Results Card
        # ----------------------------------------------

        result_card = tk.Frame(
            main_frame,
            bg=COLORS["card"],
            padx=20,
            pady=15
        )

        result_card.pack(
            pady=10
        )

        # ----------------------------------------------
        # Statistics
        # ----------------------------------------------

        stats = [

            f"Player: {self.player_name}",

            f"Difficulty: {self.difficulty}",

            f"Score: {self.score}/{self.total_questions}",

            f"Correct Answers: {self.statistics.correct}",

            f"Wrong Answers: {self.statistics.wrong}",

            f"Accuracy: {accuracy}%",

            f"Average Response Time: {avg_time}s",

            f"Highest Streak: {self.statistics.highest_streak}",

            f"Quiz Duration: {duration}s",

            f"Performance Rating: {rating}"
        ]

        for item in stats:

            tk.Label(
                result_card,
                text=item,
                font=FONTS["normal"],
                bg=COLORS["card"],
                fg=COLORS["text"]
            ).pack(
                anchor="w",
                pady=2
            )
        # ----------------------------------------------
        # Achievements Section
        # ----------------------------------------------

        tk.Label(
            result_card,
            text="\n🏆 Achievements",
            font=FONTS["heading"],
            bg=COLORS["card"],
            fg=COLORS["warning"]
        ).pack(pady=(10, 5))

        if achievements:

            for achievement in achievements:

                tk.Label(
                    result_card,
                    text=achievement,
                    font=FONTS["normal"],
                    bg=COLORS["card"],
                    fg=COLORS["success"]
                ).pack(
                    anchor="w",
                    pady=2
                )

        else:

            tk.Label(
                result_card,
                text="No Achievements Unlocked",
                font=FONTS["normal"],
                bg=COLORS["card"],
                fg=COLORS["danger"]
            ).pack(
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

        play_again_btn = tk.Button(
            button_frame,
            text="🔄 Play Again",
            font=FONTS["button"],
            bg=COLORS["primary"],
            fg="black",
            bd=0,
            padx=20,
            pady=10,
            command=lambda: WelcomeScreen(self.root)
        )

        play_again_btn.grid(
            row=0,
            column=0,
            padx=10
        )

        leaderboard_btn = tk.Button(
            button_frame,
            text="🏅 Leaderboard",
            font=FONTS["button"],
            bg=COLORS["warning"],
            fg="black",
            bd=0,
            padx=20,
            pady=10,
            command=self.open_leaderboard
        )

        leaderboard_btn.grid(
            row=0,
            column=1,
            padx=10
        )

        exit_btn = tk.Button(
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

        exit_btn.grid(
            row=0,
            column=2,
            padx=10
        )

    # ==================================================
    # Open Leaderboard
    # ==================================================

    def open_leaderboard(self):

        LeaderboardScreen(self.root)