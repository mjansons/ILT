import csv
import os
import question_stats

def main():

    """MAKE A DICTIONARY"""
    my_list = question_stats.Statistics().make_dict("questions.csv")

    """PRINT DETAILS FOR THE USER TO SEE"""
    def print_stats(my_dict):
        print("\nQuestions:\n")
        for question in my_dict:
            print(
                f"ID: {question['id']},",
                f"\nStatus: {question['status']},",
                f"Question: {question['question']},",
                f"Right Answer: {question['r_answer']},"
                "\n",
            )

    """TRY TO SELECT ID TO CHANGE STATUS"""

    def validate_id(the_list, id_to_check):
        found_id = "invalid"
        for question in the_list:
            if question["id"] == id_to_check:
                found_id = "valid"
        return found_id
    
    
    """CHANGE THE VALUE IN THE LIST"""
    def update_list(the_id, the_list):
        for question in the_list:
            if question["id"] == the_id:
                if question["status"] == "active":
                    question["status"] = "inactive"
                elif question["status"] == "inactive":
                    question["status"] = "active"
                
    
    """REWRITE THE FILE"""
    def re_write_csv(list):
        with open("questions.csv", "w", newline="", encoding="utf-8") as file:
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
            writer.writeheader()
            for row in list:
                writer.writerow(
                    {
                        "type": row["type"],
                        "id": row["id"],
                        "status": row["status"],
                        "question": row["question"],
                        "r_answer": row["r_answer"],
                        "w_answer_1": row["w_answer_1"],
                        "w_answer_2": row["w_answer_2"],
                        "w_answer_3": row["w_answer_3"],
                        "shown": row["shown"],
                        "answered": row["answered"],
                    }
                )

    def run(the_dict):
        print_stats(the_dict)

        selected_id = input("Change status for ID: ").casefold()

        if validate_id(the_dict, selected_id) == "valid":
            update_list(selected_id, the_dict)
            re_write_csv(the_dict)
        else:
            print("Incorrect ID")


    
    run(my_list)  

main()
    






#so I managed to get the stats that I want to be checked for status
#need to now make functionality to actually change the status of those questions