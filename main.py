import adding_questions
import question_stats
import status_change
import practice_mode
import test_mode
import sys

def main():

    test_mode.TestMode.create_txt("test_results.txt")
    adding_questions.QuestionProcessor.create_csv("questions.csv")

    while True:
        barrier_stats = test_mode.Barrier().mode_barrier()
        try:
            print("\nMenu:")
            print(
                "1. Add Questions\n"
                "2. View Stats\n"
                "3. Disable/enable questions\n"
                "4. Practice\n"
                "5. Do a test\n"
                "6. Wipe all files\n"
                "7. Exit\n"
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
                if barrier_stats[0] < 2:
                    print("At least 1 questions must be added, before you can start this mode")
                    continue
                else:
                    status_change.start_status_mode()

            # Practice
            elif what == "4":
                if barrier_stats[0] < 7:
                    print("At least 5 questions must be added, before you can start this mode")
                    continue
                elif barrier_stats[1] < 5:
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
                    test_mode.start_test_mode()
                    continue

            # Wipe
            elif what == "6":
                # wipe txt
                test_mode.TestMode.wipe_file("test_results.txt")
                # wipe csv
                adding_questions.QuestionProcessor.wipe_file("questions.csv")
                continue

            # Exit Program
            elif what == "7":
                sys.exit("\nAdios!\n")

            else:
                print("Invalid Option Selected")

        except (adding_questions.BackToMain, status_change.BackToMain, practice_mode.BackToMain, test_mode.BackToMain,) as e:
            continue
            
if __name__ == "__main__":
    main()