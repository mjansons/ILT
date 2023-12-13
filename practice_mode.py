from dataclasses import dataclass
import random
import question_stats

# A mode in which questions are given non-stop so that the user can practice. 
# Questions that are answered correctly become less likely to appear,
# while questions that are answered incorrectly become more likely to appear.
# Hint: you may want to look into weighted random choices. 
# The probabilities should not be reset when the program restarts.

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


@dataclass
class QuestionAsker:

    selected_question: list = None

    def quiz_question(self):

        list_answers = [self.selected_question[0]["r_answer"], self.selected_question[0]["w_answer_1"], self.selected_question[0]["w_answer_2"], self.selected_question[0]["w_answer_3"]]
        
        random.shuffle(list_answers)

        a, b, c, d = list_answers
    
        print(f"\n{self.selected_question[0]['question']}\n\na. {a}\nb. {b}\nc. {c}\nd. {d}\n\nTo exit practice mode, type 'done'\n")
        
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
        print(f"\n{self.selected_question[0]['question']}\n\nTo exit practice mode, type 'done'\n")
        
        while True:
            answer = input("Answer: ").casefold()
            if not answer:
                print("\nType at least something!\n")
            if answer == "done":
                raise BackToMain
            else:
                return answer
            
    def ask(self, question):
        self.selected_question = question
        if self.selected_question[0]["type"] == "quizquestion":
            return self.quiz_question()
        else:
            return self.freeform_question()
            

@dataclass
class AnswerEvaluator:
    my_list: list
    question: list
    answer: str

    def evaluate(self):
        if self.question[0]['r_answer'] == self.answer:
            self.update_correct()
            print("\nCorrect!\n")
        else: 
            self.update_wrong()
            print(f"\nIncorrect! The Right answer was {self.question[0]['r_answer']}\n")

    def update_correct(self):
        for original_question in self.my_list:
            if original_question["id"] == self.question[0]["id"]:
                old_shown = int(original_question["shown"])
                old_percentage = float(original_question["answered"])
                original_question["answered"] = round(((old_shown * old_percentage) + 1) / (old_shown + 1), 2)
                original_question["shown"] = int(original_question["shown"]) + 1

    def update_wrong(self):
        for original_question in self.my_list:
            if original_question["id"] == self.question[0]["id"]:
                old_shown = int(original_question["shown"])
                old_percentage = float(original_question["answered"])
                original_question["answered"] = round(((old_shown * old_percentage)) / (old_shown + 1), 2)
                original_question["shown"] = int(original_question["shown"]) + 1


def start_practice_mode():
    while True:
        my_list = question_stats.My_csv_manager.make_dict("questions.csv")
        question = QuestionFinder.select_weighted_question(my_list)
        answer = QuestionAsker().ask(question)
        AnswerEvaluator(my_list, question, answer).evaluate()
        question_stats.My_csv_manager.re_write_csv(my_list, "questions.csv")
    
if __name__ == "__main__":
    start_practice_mode()

