import question_stats
import practice_mode
from datetime import datetime, timezone
import csv
import os


class BackToMain(Exception):
    pass


class Barrier:
    @staticmethod
    def mode_barrier():
        line_count = question_stats.My_csv_manager.get_line_count()
        my_list = question_stats.My_csv_manager.make_dict("questions.csv")
        active_questions = len(
            [question for question in my_list if question["status"] == "active"]
        )
        return (line_count, active_questions)


class TestMode:
    @staticmethod
    def get_question_amount():
        while True:
            try:
                barrier_info = Barrier().mode_barrier()
                print(
                    f"\nThere are {barrier_info[1]} currently active questions!\nHow long would you like your test to be?"
                )
                selected_amount = int(input("\nTest length: "))
                if 0 < selected_amount <= barrier_info[1]:
                    print("\nGood Luck!")
                    return selected_amount
                else:
                    print("Invalid selection!")
            except Exception:
                print("Invalid selection!")
                continue

    @staticmethod
    def log_test(question_amount, score):
        current_datetime = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S")
        line = [f"Test on: {current_datetime}, Score: {score}/{question_amount}"]
        with open("test_results.txt", "a", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow(line)

    @staticmethod
    def wipe_file(file_path):
        with open(file_path, "w", newline="", encoding="utf-8") as file:
            pass

    @staticmethod
    def create_txt(file_path):
        if not os.path.exists(file_path):
            with open(file_path, "w", newline="", encoding="utf-8") as file:
                pass



def start_test_mode():
    question_amount = TestMode.get_question_amount()
    my_list = question_stats.My_csv_manager.make_dict("questions.csv")
    selected_questions = practice_mode.QuestionFinder.select_random_questions(
        my_list, question_amount
    )
    score = 0
    for question in selected_questions:
        question = [question]
        answer = practice_mode.QuestionAsker(question).ask()
        result = practice_mode.AnswerEvaluator(my_list, question, answer).evaluate()
        if result == True:
            score += 1
    TestMode.log_test(question_amount, score)
    question_stats.My_csv_manager.re_write_csv(my_list, "questions.csv")
    print(f"Final score: {score}/{question_amount}\n")


if __name__ == "__main__":
    start_test_mode()
