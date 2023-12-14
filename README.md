# Interactive Learning Tool

The Interactive Learning Tool is a Python program designed to help users create, manage, and practice with custom quiz questions. It provides various features, including adding questions, viewing statistics, disabling/enabling questions, practicing, and taking tests.

## Getting Started

These instructions will help you set up and run the Interactive Learning Tool on your local machine.

### Prerequisites

Make sure you have Python 3 installed on your machine. You can download it from [python.org](https://www.python.org/downloads/).

### Installing

1. Clone the repository to your local machine:

   ```bash
   git clone https://github.com/mjansons/ILT.git
   ```

2. Change into the project directory:

   ```bash
   cd interactive-learning-tool
   ```

3. Install the required dependencies:

   for the whole dependency list generate a requirement's txt by typing this in bash:

   pip freeze > requirements.txt

   it will generate a requirements.txt file

   to install everything from it:

   pip install -r requirements.txt

   If this doesn't work, I believe you only need pytest. Everything else should come with python3.
   pip install pytest

## Usage

To run the program, execute the following command in your terminal:

```bash
python3 main.py

```

If you want you may also delete questions.csv and test_results.txt, but they will be re-created when the program starts.