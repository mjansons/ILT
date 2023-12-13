import adding_questions
import question_stats
import status_change
import practice_mode
import sys

def main():

    while True:
        barrier_stats = mode_barrier()
        try:
            print("\nMenu:")
            print(
                "1. Add Questions\n"
                "2. View Stats\n"
                "3. Disable/enable questions\n"
                "4. Practice\n"
                "5. Do a test\n"
                "6. Exit\n"
            )
            what = input("Option: ")
            
            # Add questions
            if what == "1":
                adding_questions.start_question_mode()

            # View stats
            elif what == "2":
                question_stats.reveal_stats()
                continue

            # Disable/enable questions
            elif what == "3":
                status_change.start_status_mode()

            # Practice
            elif what == "4":
                if barrier_stats[0] < 7:
                    print("At least 5 questions must be added, before you can start this mode")
                    continue
                elif barrier_stats[1] < 6:
                    print("At least 5 questions must be Enabled, before you can start this mode.")
                    continue
                else:
                    practice_mode.start_practice_mode()

            # Test
            elif what == "5":
                if barrier_stats[0] < 7:
                    print("At least 5 questions must be added, before you can start this mode")
                    continue
                elif barrier_stats[1] < 6:
                    print("At least 5 questions must be Enabled, before you can start this mode.")
                    continue
                else:
                    ...

            # Exit Program
            elif what == "6":
                sys.exit("\nAdios!\n")

            else:
                print("Invalid Option Selected")

        except (adding_questions.BackToMain, status_change.BackToMain, practice_mode.BackToMain) as e:
            continue


def mode_barrier():
    line_count = question_stats.My_csv_manager.get_line_count()
    my_list = question_stats.My_csv_manager.make_dict("questions.csv")
    active_questions = len([question for question in my_list if question["status"] == "active"])
    return (line_count, active_questions)

            
if __name__ == "__main__":
    main()