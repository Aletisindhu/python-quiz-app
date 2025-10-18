import random
from colorama import Fore, Style, init

# Initialize colorama for colorful terminal output
init(autoreset=True)

# ---------------- QUIZ DATA ---------------- #
quiz_data = [
    {
        "question": "What is the correct file extension for Python files?",
        "options": ["A. .pt", "B. .pyt", "C. .py", "D. .python"],
        "answer": "C"
    },
    {
        "question": "Which function is used to display output in Python?",
        "options": ["A. print()", "B. display()", "C. echo()", "D. show()"],
        "answer": "A"
    },
    {
        "question": "Which of the following is a mutable data type in Python?",
        "options": ["A. tuple", "B. list", "C. str", "D. int"],
        "answer": "B"
    },
    {
        "question": "What will be the output of: print(type([]))?",
        "options": ["A. <class 'list'>", "B. <class 'tuple'>", "C. <class 'set'>", "D. <class 'dict'>"],
        "answer": "A"
    },
    {
        "question": "Which keyword is used to create a function in Python?",
        "options": ["A. func", "B. define", "C. def", "D. function"],
        "answer": "C"
    },
    {
        "question": "What is the output of: print(2 ** 3)?",
        "options": ["A. 6", "B. 8", "C. 9", "D. Error"],
        "answer": "B"
    },
    {
        "question": "What will be the result of: bool(0)?",
        "options": ["A. True", "B. False", "C. 0", "D. None"],
        "answer": "B"
    },
    {
        "question": "Which of these statements creates a dictionary?",
        "options": ["A. {}", "B. []", "C. ()", "D. {{}}"],
        "answer": "A"
    },
    {
        "question": "Which module in Python is used for random number generation?",
        "options": ["A. random", "B. randint", "C. math", "D. os"],
        "answer": "A"
    },
    {
        "question": "What is the output of: len('Python')?",
        "options": ["A. 5", "B. 6", "C. 7", "D. Error"],
        "answer": "B"
    },
    {
        "question": "Which keyword is used to handle exceptions in Python?",
        "options": ["A. error", "B. except", "C. catch", "D. handle"],
        "answer": "B"
    },
    {
        "question": "What does the 'break' statement do in a loop?",
        "options": ["A. Skips one iteration", "B. Ends the loop", "C. Stops program execution", "D. Repeats the loop"],
        "answer": "B"
    },
    {
        "question": "Which function returns the number of items in a list?",
        "options": ["A. count()", "B. length()", "C. size()", "D. len()"],
        "answer": "D"
    },
    {
        "question": "Which of these is not a core data type in Python?",
        "options": ["A. Lists", "B. Tuples", "C. Class", "D. Dictionary"],
        "answer": "C"
    },
    {
        "question": "How do you start a comment in Python?",
        "options": ["A. //", "B. #", "C. <!--", "D. /*"],
        "answer": "B"
    },
    {
        "question": "What will be printed by: print('Hello' + 'World')?",
        "options": ["A. Hello World", "B. Hello+World", "C. HelloWorld", "D. Error"],
        "answer": "C"
    },
    {
        "question": "Which keyword is used to create a class in Python?",
        "options": ["A. def", "B. func", "C. class", "D. structure"],
        "answer": "C"
    },
    {
        "question": "What is the output of: print(10 // 3)?",
        "options": ["A. 3.33", "B. 3", "C. 4", "D. Error"],
        "answer": "B"
    },
    {
        "question": "Which function is used to get user input in Python?",
        "options": ["A. input()", "B. get()", "C. read()", "D. ask()"],
        "answer": "A"
    },
    {
        "question": "What is the output of: print(3 == 3.0)?",
        "options": ["A. True", "B. False", "C. Error", "D. None"],
        "answer": "A"
    }
]

# ---------------- FUNCTIONS ---------------- #
def ask_question(question_data):
    """Ask one question and return True if correct, else False."""
    print(Fore.CYAN + question_data["question"])
    for option in question_data["options"]:
        print(Fore.YELLOW + option)
    user_answer = input(Fore.WHITE + "Enter your answer (A, B, C, D): ").upper()
    if user_answer == question_data["answer"]:
        print(Fore.GREEN + "✅ Correct!\n")
        return True
    else:
        print(Fore.RED + f"❌ Wrong! The correct answer is {question_data['answer']}.\n")
        return False


# ---------------- MAIN PROGRAM ---------------- #
if __name__ == "__main__":
    score = 0
    total_questions = 5  # number of random questions to ask

    print(Fore.MAGENTA + Style.BRIGHT + "🐍 Welcome to the Python Quiz Game! 🧠\n")
    random.shuffle(quiz_data)

    for i in range(total_questions):
        print(Fore.BLUE + f"Question {i + 1} of {total_questions}\n" + "-" * 30)
        if ask_question(quiz_data[i]):
            score += 1

    percentage = (score / total_questions) * 100

    print(Fore.CYAN + "-" * 40)
    print(Fore.MAGENTA + f"🏁 You scored {score}/{total_questions} ({percentage:.0f}%)")

    if percentage == 100:
        print(Fore.GREEN + "🌟 Excellent! Python Master!")
    elif percentage >= 60:
        print(Fore.YELLOW + "👍 Good work! Keep practicing.")
    else:
        print(Fore.RED + "💪 Don’t worry, practice makes perfect!")

    print(Fore.CYAN + "-" * 40)
