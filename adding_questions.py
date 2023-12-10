import csv
from dataclasses import dataclass
from abc import ABC, abstractmethod
import time
import os

# default is a free-form question
@dataclass
class Question(ABC):
    question_type: str = None
    unique_id: int = int(time.time())
    status: str = "active"
    question: str = None
    right_answer: str = None
    wrong_answer_1: str = None
    wrong_answer_2: str = None
    wrong_answer_3: str = None
    answer: str = None
    shown: int = 0
    answered: float = 0

    @abstractmethod
    def get(self):
        ...

    def add_to_file(self):
        with open("questions.csv", "a", newline='', encoding='utf-8') as file:
            writer = csv.DictWriter(file, fieldnames=["type", "id", "status", "question", "r_answer", "w_answer_1", "w_answer_2", "w_answer_3", "shown", "answered"])
            #only create headers if the file is empty.
            if os.path.getsize("questions.csv") == 0:
                writer.writeheader()
            writer.writerow({"type": self.question_type, "id": self.unique_id, "status": self.status, "question": self.question, "r_answer": self.right_answer, "w_answer_1": self.wrong_answer_1, "w_answer_2": self.wrong_answer_2, "w_answer_3": self.wrong_answer_3, "shown": self.shown, "answered": self.answered})

@dataclass
class QuizQuestion(Question):
    question_type: str = "quizquestion"

    def get(self):
        self.question = input("Question: ")
        self.right_answer = input("Correct Answer: ")
        self.wrong_answer_1 = input("Wrong Answer Option 1: ")
        self.wrong_answer_2 = input("Wrong Answer Option 2: ")
        self.wrong_answer_3 = input("Wrong Answer Option 3: ")


@dataclass
class FreeformQuestion(Question):
    question_type: str = "freeform"

    def get(self):
        self.question = input("Question: ")
        self.right_answer = input("Correct Answer: ")




while True:
    print("What type of question would you like to add?\n1. Quiz\n2. Freeform\n3. Return To Modes")
    selection = input("Option: ")

    #Quiz Question
    if selection == "1":
        question = QuizQuestion()
        question.get()
        question.add_to_file()
        continue

    #Freeform Question
    elif selection == "2":
        question = FreeformQuestion()
        question.get()
        question.add_to_file()
        continue

    #Back to Menu
    elif selection == "3":
        break
        ... # raise BackToMainMenuError

    # If selection not in ["1", "2", "3"]:
    else:
        print("\nInvalid Selection!\n")

    