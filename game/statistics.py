# ==========================================================
# Statistics Manager
# Tracks all game statistics
# ==========================================================

import time


class Statistics:

    def __init__(self):

        self.correct = 0
        self.wrong = 0

        self.current_streak = 0
        self.highest_streak = 0

        self.response_times = []

        self.quiz_start_time = time.time()

    def add_correct(self, response_time):

        self.correct += 1

        self.current_streak += 1

        if self.current_streak > self.highest_streak:
            self.highest_streak = self.current_streak

        self.response_times.append(response_time)

    def add_wrong(self, response_time):

        self.wrong += 1

        self.current_streak = 0

        self.response_times.append(response_time)

    def total_questions(self):

        return self.correct + self.wrong

    def accuracy(self):

        total = self.total_questions()

        if total == 0:
            return 0

        return round((self.correct / total) * 100, 2)

    def average_response_time(self):

        if not self.response_times:
            return 0

        return round(
            sum(self.response_times) / len(self.response_times),
            2
        )

    def total_duration(self):

        return round(
            time.time() - self.quiz_start_time,
            2
        )