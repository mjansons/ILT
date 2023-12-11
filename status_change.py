import csv
import os
import question_stats


class BackToMain(Exception):
    pass


class Status:
    def __init__(self, my_dict):
        self.my_dict = my_dict

    def print_stats(self):
        """print some details from dict"""
        print("\nQuestions:\n")
        for question in self.my_dict:
            print(
                f"ID: {question['id']},",
                f"\nStatus: {question['status']},",
                f"Question: {question['question']},",
                f"Right Answer: {question['r_answer']}," "\n",
            )

    def validate_id(self, id_to_check):
        """validate id"""
        found_id = False
        for question in self.my_dict:
            if question["id"] == id_to_check:
                found_id = True
        return found_id

    def update_status(self, the_id):
        """change the status in the list"""
        for question in self.my_dict:
            if question["id"] == the_id:
                if question["status"] == "active":
                    question["status"] = "inactive"
                elif question["status"] == "inactive":
                    question["status"] = "active"

    def re_write_csv(self):
        """rewrite the file"""
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
            for row in self.my_dict:
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


def start_status_mode():
    # make a dict from Statistics class function
    my_list = question_stats.Statistics().make_dict("questions.csv")
    status_obj = Status(my_list)

    while True:
        print(
            "\nWhat do you want to do?\n1.Print Questions\n2.Change Status\n3.Go to main menu"
        )
        option = input("\nOption: ")

        # Print all questions
        if option == "1":
            status_obj.print_stats()
            print("Success, look up!")
        
        # Change status
        elif option == "2":
            while True:
                selected_id = input("\nChange status for ID: ").casefold()
                response = status_obj.validate_id(selected_id)

                if response == True:
                    status_obj.update_status(selected_id)
                    status_obj.re_write_csv()
                    print("\nDone!")
                    break

                else:
                    print("\nIncorrect ID!")
                    continue
        
        # Go to main menu
        elif option == "3":
            raise BackToMain

        else:
            print("\nInvalid option selected")
            continue


if __name__ == "__main__":
    start_status_mode()
