from dataclasses import dataclass
import random
import question_stats
from typing import Union

class BackToMain(Exception):
    pass

@dataclass
class QuestionFinder:

    @staticmethod
    def select_weighted_question(the_list):
        # filter active questions
        active_questions = [question for question in the_list if question["status"] == "active"]
        # get percentage data 
        list_of_percentages = [question["answered"] for question in active_questions]
        # invert values and make sure they always at least +0.01
        weights = [abs(0.99 - float(percentage)) for percentage in list_of_percentages]
        # getting the question
        selected_question = random.choices(active_questions, weights=weights, k=1)
        return selected_question
    
    @staticmethod
    def select_random_questions(the_list, amount):
        # filter active questions
        active_questions = [question for question in the_list if question["status"] == "active"]
        # getting the question
        selected_questions = random.sample(active_questions, k=amount)
        return selected_questions


@dataclass
class QuestionAsker:

    selected_question: list

    def quiz_question(self):

        list_answers = [self.selected_question[0]["r_answer"], self.selected_question[0]["w_answer_1"], self.selected_question[0]["w_answer_2"], self.selected_question[0]["w_answer_3"]]
        
        random.shuffle(list_answers)

        a, b, c, d = list_answers
    
        print(f"\n{self.selected_question[0]['question']}\n\na. {a}\nb. {b}\nc. {c}\nd. {d}\n\nTo exit, type 'done'\n")
        
        while True:
            answer = input("Answer: ").casefold()
            if answer == "done":
                raise BackToMain
            elif answer == "a":
                return a
            elif answer == "b":
                return b
            elif answer == "c":
                return c
            elif answer == "d":
                return d
            else:
                print("\nNo such answer, select a, b, c, or d!\n")

    def freeform_question(self):
        if isinstance(self.selected_question, list):
            question_data = self.selected_question[0]

        elif isinstance(self.selected_question, dict):
            question_data = self.selected_question

        print(f"\n{question_data['question']}\n\nTo exit, type 'done'\n")
        
        while True:
            answer = input("Answer: ").casefold()
            if not answer:
                print("\nType at least something!\n")
            if answer == "done":
                raise BackToMain
            else:
                return answer
            
    def ask(self):
        if self.selected_question[0]["type"] == "quizquestion":
            return self.quiz_question()
        else:
            return self.freeform_question()
            

@dataclass
class AnswerEvaluator:
    my_list: list
    selected_question: list
    answer: str

    def evaluate(self):
        if self.selected_question[0]['r_answer'] == self.answer:
            self.update_correct()
            print("\nCorrect!")
            return True
        else: 
            self.update_wrong()
            print(f"\nIncorrect! The Right answer was: {self.selected_question[0]['r_answer']}")

    def update_correct(self):
        for original_question in self.my_list:
            if original_question["id"] == self.selected_question[0]["id"]:
                old_shown = int(original_question["shown"])
                old_percentage = float(original_question["answered"])
                original_question["answered"] = round(((old_shown * old_percentage) + 1) / (old_shown + 1), 2)
                original_question["shown"] = int(original_question["shown"]) + 1

    def update_wrong(self):
        for original_question in self.my_list:
            if original_question["id"] == self.selected_question[0]["id"]:
                old_shown = int(original_question["shown"])
                old_percentage = float(original_question["answered"])
                original_question["answered"] = round(((old_shown * old_percentage)) / (old_shown + 1), 2)
                original_question["shown"] = int(original_question["shown"]) + 1


def start_practice_mode():
    while True:
        my_list = question_stats.My_csv_manager.make_dict("questions.csv")
        question = QuestionFinder.select_weighted_question(my_list)
        answer = QuestionAsker(question).ask()
        AnswerEvaluator(my_list, question, answer).evaluate()
        question_stats.My_csv_manager.re_write_csv(my_list, "questions.csv")
    
if __name__ == "__main__":
    start_practice_mode()

