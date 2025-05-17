# Welcome to Harika's Python Quiz Game!
# This is a beginner-friendly quiz to test your knowledge.

def welcome():
    print("Welcome to the Python Quiz Game!")
    name = input("What's your name? ")
    print(f"Hi {name}! Let's begin the quiz. Best of luck!\n")

# List of questions and answers
questions = [
    {
        "question": "What is the output of 3 * 1 ** 3?",
        "options": ["1", "3", "9", "None"],
        "answer": "3"
    },
    {
        "question": "Which keyword is used for function in Python?",
        "options": ["function", "def", "define", "fun"],
        "answer": "def"
    },
    {
        "question": "What data type is the result of: 5 / 2?",
        "options": ["int", "float", "double", "decimal"],
        "answer": "float"
    },
    {
        "question": "What symbol is used to comment a single line in Python?",
        "options": ["//", "#", "/*", "<!--"],
        "answer": "#"
    }
]

def ask_question(q):
    print("\n" + q["question"])
    for idx, option in enumerate(q["options"], 1):
        print(f"{idx}. {option}")

    while True:
        try:
            choice = int(input("Your answer (1-4): "))
            if 1 <= choice <= 4:
                return q["options"][choice - 1] == q["answer"]
            else:
                print("Please choose a number between 1 and 4.")
        except ValueError:
            print("Please enter a valid number.")

def run_quiz():
    score = 0
    for q in questions:
        if ask_question(q):
            print("Correct!")
            score += 1
        else:
            print(f"Oops! The correct answer was: {q['answer']}")

    print("\nQuiz completed!")
    print(f"You got {score} out of {len(questions)} correct.")

if __name__ == "__main__":
    welcome()
    run_quiz()
