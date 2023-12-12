import csv
from dataclasses import dataclass


@dataclass
class Statistics:
    @staticmethod
    def print_stats(question_dict):
        print("")
        for question in question_dict:
            print(
                f"ID: {question['id']}",
                # f"Type: {question['type']}",
                f"\nStatus: {question['status']}",
                f"\nQuestion: {question['question']}",
                f"\nRight Answer: {question['r_answer']}",
                f"\nWrong Answer 1: {question['w_answer_1']}" if question['type'] == "quizquestion" else "",
                f"\nWrong Answer 2: {question['w_answer_2']}" if question['type'] == "quizquestion" else "",
                f"\nWrong Answer 3: {question['w_answer_3']}" if question['type'] == "quizquestion" else "",
                f"\nTimes Shown: {question['shown']}",
                f"\nAnswered Correctly: {question['answered']}",
                "\n",
            )
        print("Success, look up!")


@dataclass
class My_csv_manager:
    @staticmethod
    def make_dict(file_path="questions.csv"):
        question_list = []
        with open(file_path) as file:
            reader = csv.DictReader(file)
            for row in reader:
                question_list.append(
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
        return question_list

    # I will use this function in another part of my program, not in statistics mode.
    @staticmethod
    def re_write_csv(question_dict, file_path="questions.csv"):
        """rewrite the file"""
        with open(file_path, "w", newline="", encoding="utf-8") as file:
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
            for row in question_dict:
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


def reveal_stats():
    the_questions = My_csv_manager.make_dict("questions.csv")
    Statistics.print_stats(the_questions)


if __name__ == "__main__":
    reveal_stats()
