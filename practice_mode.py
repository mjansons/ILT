# A mode in which questions are given non-stop so that the user can practice. 

# Qquestions that are answered correctly become less likely to appear,

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
