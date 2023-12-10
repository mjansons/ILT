import adding_questions
import question_stats
import sys
import adding_questions


while True:
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
            pass

        # Practice
        elif what == "4":
            pass

        # Test
        elif what == "5":
            pass

        # Exit Program
        elif what == "6":
            sys.exit("\nAdios!\n")

        else:
            print("Invalid Option Selected")

    except adding_questions.BackToMain as e:
        continue
