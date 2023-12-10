import csv
import question_stats

list = question_stats.Statistics()
list = list.make_dict("questions.csv")


def print_stats():
    for question in list:
        print(
            f"ID: {question['id']},",
            f"\nStatus: {question['status']},",
            f"Question: {question['question']},",
            f"Right Answer: {question['r_answer']},"
            "\n",
        )

print_stats()

#so I managed to get the stats that I want to be checked for status
#need to now make functionality to actually change the status of those questions