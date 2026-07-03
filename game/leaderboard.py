
# Leaderboard System
# Handles reading and writing JSON leaderboard
import json
import os
from datetime import datetime


class Leaderboard:

    def __init__(self):

        self.file_path = "data/leaderboard.json"

        self.create_file()

    def create_file(self):

        folder = "data"

        if not os.path.exists(folder):
            os.makedirs(folder)

        if not os.path.exists(self.file_path):

            with open(self.file_path, "w") as file:
                json.dump([], file)

    def load_scores(self):

        try:

            with open(self.file_path, "r") as file:

                return json.load(file)

        except:

            return []

    def save_score(
            self,
            player_name,
            score,
            accuracy,
            difficulty):

        scores = self.load_scores()

        scores.append({
            "name": player_name,
            "score": score,
            "accuracy": accuracy,
            "difficulty": difficulty,
            "date": datetime.now().strftime("%Y-%m-%d")
        })

        scores.sort(
            key=lambda x: x["score"],
            reverse=True
        )

        scores = scores[:10]

        with open(self.file_path, "w") as file:

            json.dump(
                scores,
                file,
                indent=4
            )

    def get_top_scores(self):

        return self.load_scores()