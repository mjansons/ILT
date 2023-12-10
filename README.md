Here's a high-level task breakdown structure for my interactive learning tool:

Main Program Flow:

Create a main program loop that allows users to choose different modes.
Implement the menu with options for adding questions, viewing statistics, disabling/enabling questions, practice mode, test mode, and (bonus) profile select.

Question Class:
Create a class for handling questions.
Implement subclasses for quiz questions and free-form text questions.
Include methods for displaying questions, checking answers, and updating question statistics.
File Handling:

Implement file I/O for storing questions, enabled/disabled status, and (bonus) user profiles and their statistics.
Ensure the program loads previous data when started and saves updates when closing.
Adding Questions:

Implement the logic for adding quiz and free-form text questions.
Ensure questions are saved to the file.
Statistics Viewing:

Implement the logic for displaying question statistics.
Disable/Enable Questions:

Implement the logic for disabling/enabling questions.
Update the file with the enabled/disabled status.
Practice Mode:

Implement weighted random question selection.
Create a loop for continuous practice until the user decides to exit.
Test Mode:

Implement random question selection for tests.
Record and display scores.
Save scores to a separate results.txt file with timestamps.
Bonus: Profile Select:

Implement user profiles with individual statistics.
Update practice and test modes to consider profile-specific probabilities.
Unit Testing:

Write at least three unit tests to ensure critical functionalities are working as expected.
Code Quality and Readability:

Ensure the code is well-organized, follows PEP 8 conventions, and is readable.
Usability:

Test the program to ensure it's user-friendly and intuitive.
Additional Features (Optional):

Consider implementing additional features that could enhance the usability and functionality of the program, such as a "full reset" option.
Documentation:

Provide comments and documentation for your code to explain complex parts or logic.
Peer Programming:

Conduct at least one session of peer programming, and ensure the initial repository is available on GitHub.
Remember to regularly test and debug your code as you progress through each feature. Additionally, keep the user experience in mind to create a seamless and intuitive learning tool.

Notes to myself:
Need to remember to allow users to edit questions that they have added in case mistakes were made. Another option in adding_questions.py
