import csv
from dataclasses import dataclass


@dataclass
class Statistics:
    question_list = list = []

    def make_dict(self):
        with open("questions.csv") as file:
            reader = csv.DictReader(file)
            for row in reader:
                self.question_list.append(
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

    def print_stats(self):
        for question in self.question_list:
            print(
                f"ID: {question['id']},",
                # f"Type: {question['type']}",
                f"\nStatus: {question['status']},",
                f"Question: {question['question']},",
                f"Right Answer: {question['r_answer']},",
                # f"Wrong Answer 1: {question['w_answer_1']},",
                # f"Wrong Answer 2: {question['w_answer_2']},",
                # f"Wrong Answer 3: {question['w_answer_3']},",
                f"Times Shown: {question['shown']},",
                f"Answered Correctly: {question['answered']},",
                "\n",
            )


def reveal_stats():
    stuff = Statistics()
    stuff.make_dict()
    stuff.print_stats()


if __name__ == "__main__":
    reveal_stats()
