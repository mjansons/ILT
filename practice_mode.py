from dataclasses import dataclass
import random
import question_stats

# A mode in which questions are given non-stop so that the user can practice. 
# Questions that are answered correctly become less likely to appear,
# while questions that are answered incorrectly become more likely to appear.
# Hint: you may want to look into weighted random choices. 
# The probabilities should not be reset when the program restarts.



# percentage = times shown / answered correctly




"""adjust weight and frequency stats"""
# if answered correctly: 
    # answered correctly + ?%
        # new_percent = ((times shown * answered correctly) + 1) / (times shown + 1)
    # times shown +1
        # new_times_shown = times shown + 1

# if answered incorrectly:
    # times shown +1
        # new_times_shown = times shown + 1





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

    selected_question: list

    def ask_quiz_question(self):

        list_answers = [self.selected_question[0]["r_answer"], self.selected_question[0]["w_answer_1"], self.selected_question[0]["w_answer_2"], self.selected_question[0]["w_answer_3"]]
        
        random.shuffle(list_answers)

        a, b, c, d = list_answers
    
        print(f"\n{self.selected_question[0]['question']}\n\na. {a}\nb. {b}\nc. {c}\nd. {d}\n")
        
        while True:
            answer = input("Answer: ").casefold()
            if answer == "a":
                return a
            elif answer == "b":
                return b
            elif answer == "c":
                return c
            elif answer == "d":
                return d
            else:
                print("\nNo such answer, select a, b, c, or d!\n")

    def ask_freeform_question(self):
        print(f"\n{self.selected_question[0]['question']}\n")
        
        while True:
            answer = input("Answer: ").casefold()
            if not answer:
                print("\nType at least something!\n")
            else:
                return answer
            
    def ask(self):
        if self.selected_question[0]["type"] == "quizquestion":
            return self.ask_quiz_question()
        else:
            return self.ask_freeform_question()
            

@dataclass
class AnswerManager:
    ...

    
my_list = question_stats.My_csv_manager.make_dict("questions.csv")
question = QuestionFinder.select_weighted_question(my_list)
answer = QuestionAsker(question).ask()
print(answer)




#     # - answer evaluator
#     # EVALUATE ANSWER
#     # UPDATE THE DICT

        #value = 3.14159265359
        # #Round to 2 digits after the decimal point
        # rounded_value = round(value, 2)

#     # GIVE FEEDBACK - Whether it was correct or not and if not what was the right answer















# # LOOP
# while True:
#     # GET THE LIST from FILE
#     my_list = question_stats.My_csv_manager.make_dict("questions.csv")

#     # - question selector
#     # SELECT A QUESTION FROM ALL ACTIVE QUESTIONS

#     # - question asker
#     # ASK THAT QUESTION

#     # - answer evaluator
#     # EVALUATE ANSWER
#     # UPDATE THE DICT
#     # GIVE FEEDBACK - Whether it was correct or not and if not what was the right answer

#     # RE_WRITE THE FILE
#     question_stats.My_csv_manager.re_write_csv(my_list, "questions.csv")





