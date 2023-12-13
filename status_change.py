import csv
import os
import question_stats


class BackToMain(Exception):
    pass


class Status:
    def __init__(self, my_dict):
        self.my_dict = my_dict

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


def start_status_mode():
    # make a dict from My_csv_manager class function
    my_list = question_stats.My_csv_manager.make_dict("questions.csv")

    status_obj = Status(my_list)

    while True:
        print(
            "\nWhat do you want to do?\n1. Print Questions\n2. Change Status\n3. Go to main menu"
        )
        option = input("\nOption: ")

        # Print all questions
        if option == "1":
            question_stats.Statistics.print_stats(my_list)

        # Change status
        elif option == "2":
            question_stats.Statistics.print_stats(my_list)
            while True:
                selected_id = input("\nChange status for ID: ").casefold()
                response = status_obj.validate_id(selected_id)

                if response == True:
                    status_obj.update_status(selected_id)
                    question_stats.My_csv_manager.re_write_csv(my_list, "questions.csv")
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
