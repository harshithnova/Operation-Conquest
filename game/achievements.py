# Achievement System
class AchievementManager:

    def __init__(self):
        pass

    def get_achievements(
            self,
            accuracy,
            avg_time,
            difficulty,
            correct,
            total_questions):

        unlocked = []

        if correct == total_questions:
            unlocked.append("🏆 Perfect Score")

        if avg_time <= 3:
            unlocked.append("⚡ Speed Demon")

        if accuracy >= 90:
            unlocked.append("🎯 Accuracy King")

        if accuracy >= 70:
            unlocked.append("⚔ Math Warrior")

        if difficulty == "Hard" and accuracy >= 80:
            unlocked.append("👑 Conqueror")

        return unlocked

    def get_rating(self, accuracy):

        if accuracy >= 95:
            return "Master"

        elif accuracy >= 85:
            return "Expert"

        elif accuracy >= 70:
            return "Skilled"

        elif accuracy >= 50:
            return "Apprentice"

        return "Beginner"