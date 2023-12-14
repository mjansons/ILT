from abc import ABC
import csv
from dataclasses import dataclass
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

    # this makes sure that every time I access this attribute, it generates a unique one
    @property
    def unique_id(self):
        return int(time.time_ns()/10000)


@dataclass
class QuizQuestion(Question):
    question_type: str = "quizquestion"

    def __init__(self, question, right_answer, wrong_answer_1, wrong_answer_2, wrong_answer_3):
        self.question = question
        self.right_answer = right_answer
        self.wrong_answer_1 = wrong_answer_1
        self.wrong_answer_2 = wrong_answer_2
        self.wrong_answer_3 = wrong_answer_3

@dataclass
class FreeformQuestion(Question):
    question_type: str = "freeform"

    def __init__(self, question, right_answer):
        self.question = question
        self.right_answer = right_answer

@dataclass
class QuestionProcessor:
    def __init__(self, question_object, file_path):
        self.asked_question = question_object
        self.file_path = file_path

    def add_to_file(self):
        """create a csv file and populate it with all attribute values"""
        with open(self.file_path, "a", newline="", encoding="utf-8") as file:
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
            if os.path.getsize(self.file_path) == 0:
                writer.writeheader()
            writer.writerow(
                {
                    "type": self.asked_question.question_type,
                    "id": self.asked_question.unique_id,
                    "status": self.asked_question.status,
                    "question": self.asked_question.question,
                    "r_answer": self.asked_question.right_answer,
                    "w_answer_1": self.asked_question.wrong_answer_1,
                    "w_answer_2": self.asked_question.wrong_answer_2,
                    "w_answer_3": self.asked_question.wrong_answer_3,
                    "shown": self.asked_question.shown,
                    "answered": self.asked_question.answered,
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

        if selection == "1":
            question = QuizQuestion(
                input("Question: "),
                input("Correct Answer: "),
                input("Wrong Answer Option 1: "),
                input("Wrong Answer Option 2: "),
                input("Wrong Answer Option 3: "),
            )
        elif selection == "2":
            question = FreeformQuestion(
                input("Question: "),
                input("Correct Answer: "),
            )
        elif selection == "3":
            raise BackToMain
        else:
            print("\nInvalid Selection!\n")
            continue

        quiz_question = QuestionProcessor(question, "questions.csv")
        quiz_question.add_to_file()
        print("Success!")

if __name__ == "__main__":
    start_question_mode()