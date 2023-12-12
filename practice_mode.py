from dataclasses import dataclass
import random
import question_stats

# A mode in which questions are given non-stop so that the user can practice. 

# Questions that are answered correctly become less likely to appear,

# while questions that are answered incorrectly become more likely to appear.
# Hint: you may want to look into weighted random choices. 
# The probabilities should not be reset when the program restarts.

# get list of questions, e.g. with ids:
# question_list = ["3243324", "234532233", "12345324"]
# weights = 




# percentage = times shown / answered correctly
# weights = [1 - percentage + 0.01 for question in list_of_questions]

# list_of_questions = [question["id"] for question in list_of_questions if question["status"] == "active"]
# chosen_question = random.choices(list_of_questions)




"""adjust weight and frequency stats"""
# if answered correctly: 
    # answered correctly + ?%
        # new_percent = ((times shown * answered correctly) + 1) / (times shown + 1)
    # times shown +1
        # new_times_shown = times shown + 1

# if answered incorrectly:
    # times shown +1
        # new_times_shown = times shown + 1





#     # - question selector
#     # SELECT A QUESTION FROM ALL ACTIVE QUESTIONS

@dataclass
class QuestionPresenter:

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


        



#     # - question asker
#     # ASK THAT QUESTION

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





