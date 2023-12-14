import pytest
from status_change import Status 
import os
from adding_questions import QuestionProcessor, QuizQuestion, FreeformQuestion
import csv

def test_validate_id():
    # Arrange
    my_dict = [{"id": "test_id"}]
    status = Status(my_dict)

    # Act
    result = status.validate_id("test_id")

    # Assert
    assert result == True


def test_update_status():
    # Arrange
    my_dict = [{"id": "test_id", "status": "active"}]
    status = Status(my_dict)

    # Act
    status.update_status("test_id")

    # Assert
    assert my_dict[0]["status"] == "inactive"


def test_create_csv():
    # Arrange
    file_path = "test_questions.csv"
    QuestionProcessor.create_csv(file_path)

    # Assert
    assert os.path.exists(file_path)  # check if the file exists

    # Clean up
    os.remove(file_path)  # remove the file after the test


    
def test_add_quiz_question_to_file():
    # Arrange
    question = QuizQuestion("Test question", "Test answer", "Wrong answer 1", "Wrong answer 2", "Wrong answer 3")
    processor = QuestionProcessor(question, "test_questions.csv")

    # Act
    processor.add_to_file()

    # Assert
    with open("test_questions.csv", "r", newline="", encoding="utf-8") as file:
        reader = csv.reader(file)
        lines = list(reader)
        assert lines[-1][3] == "Test question"  # check if the last question in the file is the one we added

    # Clean up
    os.remove("test_questions.csv")  # remove the file after the test

def test_add_freeform_question_to_file():
    # Arrange
    question = FreeformQuestion("Test question", "Test answer")
    processor = QuestionProcessor(question, "test_questions.csv")

    # Act
    processor.add_to_file()

    # Assert
    with open("test_questions.csv", "r", newline="", encoding="utf-8") as file:
        reader = csv.reader(file)
        lines = list(reader)
        assert lines[-1][3] == "Test question"  # check if the last question in the file is the one we added

    # Clean up
    os.remove("test_questions.csv")  # remove the file after the test