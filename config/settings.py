APP_NAME = "Operation Conquest"
WINDOW_WIDTH = 1200
WINDOW_HEIGHT = 800
MAX_LEADERBOARD_ENTRIES = 10
COLORS = {
    "background": "#0B0F19",
    "card": "#161B22",
    "card_light": "#21262D",

    "primary": "#D4AF37",      # Gold
    "secondary": "#8B5CF6",    # Purple

    "success": "#22C55E",
    "danger": "#EF4444",
    "warning": "#F59E0B",

    "text": "#F8FAFC",
    "muted_text": "#94A3B8"
}




FONTS = {

    "title": ("Orbitron", 26, "bold"),

    "subtitle": ("Montserrat", 15),

    "heading": ("Montserrat", 18, "bold"),

    "normal": ("Montserrat", 12),

    "small": ("Montserrat", 10),

    "button": ("Montserrat", 13, "bold"),

    "question": ("Orbitron", 30, "bold"),

    "score": ("Montserrat", 16, "bold")
}

DIFFICULTY_SETTINGS = {

    "Easy": {
        "operators": ["+", "-"],
        "min_number": 1,
        "max_number": 20,
        "time_limit": 30
    },

    "Medium": {
        "operators": ["*", "/"],
        "min_number": 2,
        "max_number": 50,
        "time_limit": 30
    },

    "Hard": {
        "operators": ["**", "//", "+", "-", "*"],
        "min_number": 2,
        "max_number": 100,
        "time_limit": 30
    }
}



RATINGS = {

    95: "Master",

    85: "Expert",

    70: "Skilled",

    50: "Apprentice",

    0: "Beginner"
}


ACHIEVEMENTS = {

    "Perfect Score":
        "Answer every question correctly.",

    "Speed Demon":
        "Average response time below 3 seconds.",

    "Accuracy King":
        "Accuracy above 90%.",

    "Math Warrior":
        "Score above 70%.",

    "Conqueror":
        "Finish Hard difficulty with at least 80% accuracy."
}


CORRECT_MESSAGES = [

    "Excellent!",
    "Brilliant!",
    "Outstanding!",
    "Perfect!",
    "Amazing!",
    "Great Work!",
    "Math Master!",
    "Keep It Up!"
]


WRONG_MESSAGES = [

    "Keep Trying!",
    "You Can Do It!",
    "Don't Give Up!",
    "Learn And Conquer!",
    "Stay Focused!",
    "Practice Makes Perfect!",
    "Almost There!",
    "Try The Next One!"
]


MOTIVATIONAL_QUOTES = [

    "Success is the sum of small efforts repeated daily.",

    "Every expert was once a beginner.",

    "Mistakes help you learn faster.",

    "Consistency beats talent.",

    "One more question, one step closer to mastery.",

    "Great things take practice.",

    "Learning never exhausts the mind.",

    "Conquer today's challenge."
]

LEADERBOARD_FILE = "data/leaderboard.json"