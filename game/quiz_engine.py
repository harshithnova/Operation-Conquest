# Quiz Engine
# Responsible for generating questions
import random


class QuizEngine:

    def __init__(self, difficulty):

        self.difficulty = difficulty

    def generate_question(self):

        if self.difficulty == "Easy":
            return self.easy_question()

        elif self.difficulty == "Medium":
            return self.medium_question()

        else:
            return self.hard_question()

    def easy_question(self):

        num1 = random.randint(1, 20)
        num2 = random.randint(1, 20)

        operator = random.choice(["+", "-"])

        if operator == "+":
            answer = num1 + num2
        else:
            answer = num1 - num2

        question = f"{num1} {operator} {num2}"

        return question, answer

    def medium_question(self):

        operator = random.choice(["*", "/"])

        if operator == "*":

            num1 = random.randint(2, 15)
            num2 = random.randint(2, 15)

            answer = num1 * num2

        else:

            num2 = random.randint(2, 12)
            answer = random.randint(2, 12)

            num1 = num2 * answer

        question = f"{num1} {operator} {num2}"

        return question, answer

    def hard_question(self):

        question_type = random.randint(1, 3)

        if question_type == 1:

            base = random.randint(2, 8)
            power = random.randint(2, 4)

            question = f"{base}^{power}"
            answer = base ** power

        elif question_type == 2:

            num1 = random.randint(20, 150)
            num2 = random.randint(2, 15)

            question = f"{num1} // {num2}"
            answer = num1 // num2

        else:

            a = random.randint(5, 30)
            b = random.randint(2, 10)
            c = random.randint(1, 10)

            question = f"({a} + {b}) * {c}"
            answer = (a + b) * c

        return question, answer