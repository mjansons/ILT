import csv
from dataclasses import dataclass
from abc import ABC
import time
import os

class BackToMain(Exception):
    pass

@dataclass
class Question(ABC):
    """master class for questions"""
    question_type: str = None
    unique_id: int = None
    status: str = "active"
    question: str = None
    right_answer: str = None
    wrong_answer_1: str = None
    wrong_answer_2: str = None
    wrong_answer_3: str = None
    answer: str = None
    shown: int = 0
    answered: float = 0

    @property
    def unique_id(self):
        return int(time.time_ns()/10000)
    
@dataclass
class QuizQuestion(Question):
    question_type: str = "quizquestion"

    def __init__(self):
        self.question = input("Question: ")
        self.right_answer = input("Correct Answer: ")
        self.wrong_answer_1 = input("Wrong Answer Option 1: ")
        self.wrong_answer_2 = input("Wrong Answer Option 2: ")
        self.wrong_answer_3 = input("Wrong Answer Option 3: ")


@dataclass
class FreeformQuestion(Question):
    question_type: str = "freeform"

    def __init__(self):
        self.question = input("Question: ")
        self.right_answer = input("Correct Answer: ")


@dataclass
class QuestionProcessor:
    def __init__(self, object):
        self.question_object = object

    def add_to_file(self):
        """create a csv file and populate it with all attribute values"""
        with open("questions.csv", "a", newline="", encoding="utf-8") as file:
            writer = csv.DictWriter(
                file,
                fieldnames=[
                    "type",
                    "id",
                    "status",
                    "question",
                    "r_answer",
                    "w_answer_1",
                    "w_answer_2",
                    "w_answer_3",
                    "shown",
                    "answered",
                ],
            )
            # only create headers if the file is empty.
            if os.path.getsize("questions.csv") == 0:
                writer.writeheader()
            writer.writerow(
                {
                    "type": self.question_object.question_type,
                    "id": self.question_object.unique_id,
                    "status": self.question_object.status,
                    "question": self.question_object.question,
                    "r_answer": self.question_object.right_answer,
                    "w_answer_1": self.question_object.wrong_answer_1,
                    "w_answer_2": self.question_object.wrong_answer_2,
                    "w_answer_3": self.question_object.wrong_answer_3,
                    "shown": self.question_object.shown,
                    "answered": self.question_object.answered,
                }
            )
    @staticmethod
    def wipe_file(file_path):
        with open(file_path, "w", newline="", encoding="utf-8"):
            pass

    @staticmethod
    def create_csv(file_path):
        if not os.path.exists(file_path):
            with open(file_path, "w", newline="", encoding="utf-8") as file:
                pass
    


def start_question_mode():
    while True:
        print(
            "\nWhat type of question would you like to add?\n1. Quiz\n2. Freeform\n3. Go to Main Menu"
        )
        selection = input("\nOption: ")

        # Quiz Question
        if selection == "1":
            question = QuizQuestion()
            quiz_question = QuestionProcessor(question)
            quiz_question.add_to_file()
            print("Success!")
            continue

        # Freeform Question
        elif selection == "2":
            question = FreeformQuestion()
            quiz_question = QuestionProcessor(question)
            quiz_question.add_to_file()
            print("Success!")
            continue

        # Back to Menu
        elif selection == "3":
            raise BackToMain

        # If selection not in ["1", "2", "3"]:
        else:
            print("\nInvalid Selection!\n")


if __name__ == "__main__":
    start_question_mode()
