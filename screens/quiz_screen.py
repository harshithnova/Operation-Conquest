# Quiz Screen
# Main gameplay screen
# 

import tkinter as tk
from tkinter import ttk
import time
from random import choice

from config.settings import *
from game.quiz_engine import QuizEngine
from game.statistics import Statistics


class QuizScreen:

    def __init__(
            self,
            root,
            player_name,
            difficulty,
            total_questions):

        self.root = root

        self.player_name = player_name
        self.difficulty = difficulty
        self.total_questions = total_questions

        # Quiz Engine

        self.engine = QuizEngine(difficulty)

        self.stats = Statistics()

        # Game Variables

        self.current_question_number = 0

        self.current_answer = None

        self.score = 0

        self.question_start_time = time.time()

        # Timer

        self.time_limit = DIFFICULTY_SETTINGS[
            difficulty
        ]["time_limit"]

        self.time_left = self.time_limit

        self.timer_job = None

        # UI

        self.build_ui()

        self.load_question()

    # Clear Window

    def clear_window(self):

        for widget in self.root.winfo_children():
            widget.destroy()

    # Build UI

    def build_ui(self):

        self.clear_window()

        self.root.configure(
            bg=COLORS["background"]
        )

        # Main Container

        self.main_frame = tk.Frame(
            self.root,
            bg=COLORS["background"]
        )

        self.main_frame.pack(
            fill="both",
            expand=True,
            padx=20,
            pady=20
        )

        # Header

        self.create_header()

        # Progress Bar

        self.create_progress_bar()

        # Question Card

        self.create_question_card()

        # Stats Section

        self.create_stats_section()

        # Feedback Label

        self.feedback_label = tk.Label(
            self.main_frame,
            text="",
            font=FONTS["heading"],
            bg=COLORS["background"],
            fg=COLORS["success"]
        )

        self.feedback_label.pack(
            pady=10
        )

    # Header

    def create_header(self):

        header = tk.Frame(
            self.main_frame,
            bg=COLORS["background"]
        )

        header.pack(
            fill="x",
            pady=10
        )

        self.player_label = tk.Label(
            header,
            text=f"Player: {self.player_name}",
            font=FONTS["heading"],
            bg=COLORS["background"],
            fg=COLORS["text"]
        )

        self.player_label.pack(
            side="left"
        )

        self.score_label = tk.Label(
            header,
            text="Score: 0",
            font=FONTS["heading"],
            bg=COLORS["background"],
            fg=COLORS["primary"]
        )

        self.score_label.pack(
            side="right"
        )

    # Progress Bar

    def create_progress_bar(self):

        progress_frame = tk.Frame(
            self.main_frame,
            bg=COLORS["background"]
        )

        progress_frame.pack(
            fill="x",
            pady=10
        )

        self.progress_label = tk.Label(
            progress_frame,
            text="Question 0 / 0",
            font=FONTS["normal"],
            bg=COLORS["background"],
            fg=COLORS["text"]
        )

        self.progress_label.pack()

        self.progress_bar = ttk.Progressbar(
            progress_frame,
            length=800,
            mode="determinate"
        )

        self.progress_bar.pack(
            pady=5
        )

    # Question Card

    def create_question_card(self):

        self.question_card = tk.Frame(
            self.main_frame,
            bg=COLORS["card"],
            padx=30,
            pady=30
        )

        self.question_card.pack(
            fill="x",
            pady=20
        )

        # Difficulty

        self.difficulty_label = tk.Label(
            self.question_card,
            text=f"Difficulty: {self.difficulty}",
            font=FONTS["normal"],
            bg=COLORS["card"],
            fg=COLORS["warning"]
        )

        self.difficulty_label.pack()

        # Question

        self.question_label = tk.Label(
            self.question_card,
            text="Question Here",
            font=FONTS["question"],
            bg=COLORS["card"],
            fg=COLORS["text"]
        )

        self.question_label.pack(
            pady=20
        )

        # Answer Entry

        self.answer_entry = tk.Entry(
            self.question_card,
            font=("Segoe UI", 18),
            justify="center",
            width=15
        )

        self.answer_entry.pack(
            pady=10
        )

        # Enter Key Support

        self.answer_entry.bind(
            "<Return>",
            self.submit_answer
        )

        # Submit Button

        self.submit_button = tk.Button(
            self.question_card,
            text="Submit Answer",
            font=FONTS["button"],
            bg=COLORS["primary"],
            fg="black",
            bd=0,
            padx=15,
            pady=10,
            command=self.submit_answer
        )

        self.submit_button.pack(
            pady=15
        )

        # Timer Text

        self.timer_label = tk.Label(
            self.question_card,
            text="Time Left",
            font=FONTS["heading"],
            bg=COLORS["card"],
            fg=COLORS["success"]
        )

        self.timer_label.pack(
            pady=10
        )

        # Timer Bar

        self.timer_bar = ttk.Progressbar(
            self.question_card,
            length=400,
            mode="determinate"
        )

        self.timer_bar.pack(
            pady=5
        )

    # Stats Section


    def create_stats_section(self):

        stats_frame = tk.Frame(
            self.main_frame,
            bg=COLORS["background"]
        )

        stats_frame.pack(
            pady=10
        )

        self.correct_label = tk.Label(
            stats_frame,
            text="Correct: 0",
            font=FONTS["normal"],
            bg=COLORS["background"],
            fg=COLORS["success"]
        )

        self.correct_label.grid(
            row=0,
            column=0,
            padx=20
        )

        self.wrong_label = tk.Label(
            stats_frame,
            text="Wrong: 0",
            font=FONTS["normal"],
            bg=COLORS["background"],
            fg=COLORS["danger"]
        )

        self.wrong_label.grid(
            row=0,
            column=1,
            padx=20
        )

        self.accuracy_label = tk.Label(
            stats_frame,
            text="Accuracy: 0%",
            font=FONTS["normal"],
            bg=COLORS["background"],
            fg=COLORS["text"]
        )

        self.accuracy_label.grid(
            row=0,
            column=2,
            padx=20
        )

        self.streak_label = tk.Label(
            stats_frame,
            text="Streak: 0",
            font=FONTS["normal"],
            bg=COLORS["background"],
            fg=COLORS["secondary"]
        )

        self.streak_label.grid(
            row=0,
            column=3,
            padx=20
        )


    # Load New Question


    def load_question(self):

        self.current_question_number += 1

        question, answer = self.engine.generate_question()

        self.current_answer = answer

        self.question_label.config(
            text=question
        )

        self.progress_label.config(
            text=f"Question {self.current_question_number} / {self.total_questions}"
        )

        progress = (
            (self.current_question_number - 1)
            / self.total_questions
        ) * 100

        self.progress_bar["value"] = progress

        self.answer_entry.delete(0, tk.END)

        self.answer_entry.focus()

        self.question_start_time = time.time()

        self.start_timer()

           

    # Start Timer


    def start_timer(self):

        if self.timer_job:
            self.root.after_cancel(
                self.timer_job
            )

        self.time_left = self.time_limit

        self.timer_bar["maximum"] = self.time_limit
        self.timer_bar["value"] = self.time_limit

        self.update_timer()

    # Update Timer


    def update_timer(self):

        self.timer_label.config(
            text=f"⏳ Time Left: {self.time_left}s"
        )

        self.timer_bar["value"] = self.time_left

        if self.time_left <= 0:

            self.feedback_label.config(
                text="⏰ Time's Up!",
                fg=COLORS["danger"]
            )

            self.auto_submit()

            return

        self.time_left -= 1

        self.timer_job = self.root.after(
            1000,
            self.update_timer
        )


    # Auto Submit


    def auto_submit(self):

        response_time = (
            time.time() -
            self.question_start_time
        )

        self.stats.add_wrong(
            response_time
        )

        self.feedback_label.config(
            text=f"Correct Answer: {self.current_answer}",
            fg=COLORS["danger"]
        )

        self.update_stats_display()

        self.root.after(
            1200,
            self.next_question
        )


    # Submit Answer


    def submit_answer(self, event=None):

        if self.timer_job:
            self.root.after_cancel(
                self.timer_job
            )

        user_input = self.answer_entry.get().strip()

        try:

            user_answer = float(user_input)

        except:

            self.feedback_label.config(
                text="Enter a valid number!",
                fg=COLORS["warning"]
            )

            self.start_timer()

            return

        response_time = (
            time.time() -
            self.question_start_time
        )

        correct = False

        try:

            if float(user_answer) == float(self.current_answer):
                correct = True

        except:

            if str(user_input) == str(self.current_answer):
                correct = True

        if correct:

            self.handle_correct(
                response_time
            )

        else:

            self.handle_wrong(
                response_time
            )

        self.update_stats_display()

        self.root.after(
            1200,
            self.next_question
        )


    # Correct Answer
  

    def handle_correct(self, response_time):

        self.score += 1

        self.stats.add_correct(
            response_time
        )

        message = choice(
            CORRECT_MESSAGES
        )

        self.feedback_label.config(
            text=f"✅ {message}",
            fg=COLORS["success"]
        )

        self.score_label.config(
            text=f"Score: {self.score}"
        )


    # Wrong Answer


    def handle_wrong(self, response_time):

        self.stats.add_wrong(
            response_time
        )

        message = choice(
            WRONG_MESSAGES
        )

        self.feedback_label.config(
            text=f"❌ {message} | Answer: {self.current_answer}",
            fg=COLORS["danger"]
        )


    # Update Stats Display


    def update_stats_display(self):

        self.correct_label.config(
            text=f"Correct: {self.stats.correct}"
        )

        self.wrong_label.config(
            text=f"Wrong: {self.stats.wrong}"
        )

        self.streak_label.config(
            text=f"Streak: {self.stats.current_streak}"
        )

        accuracy = self.stats.accuracy()

        self.accuracy_label.config(
            text=f"Accuracy: {accuracy}%"
        )


    # Next Question


    def next_question(self):

        if self.current_question_number >= self.total_questions:

            self.finish_quiz()

            return

        self.load_question()


    # Finish Quiz


    def finish_quiz(self):
        self.submit_button.config(
        state="disabled"
        )

        self.answer_entry.config(
        state="disabled"
        )

        if self.timer_job:
            self.root.after_cancel(
                self.timer_job
            )

        from screens.result_screen import ResultScreen

        ResultScreen(
            root=self.root,
            player_name=self.player_name,
            difficulty=self.difficulty,
            score=self.score,
            total_questions=self.total_questions,
            statistics=self.stats
        )