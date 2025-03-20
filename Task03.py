#Quiz Game
class Question:
    def __init__(self, prompt, answer):
        self.prompt = prompt
        self.answer = answer
def run_quiz(questions):
    score = 0
    for question in questions:
        print(question.prompt)
        user_answer = input("Your answer: ")
        if user_answer.lower() == question.answer.lower():
            score += 1
            print("Correct!\n")
        else:
            print(f"Wrong! The correct answer was: {question.answer}\n")    
    print(f"You scored {score} out of {len(questions)}.")
def main():
    questions = [
        Question("What is the capital of India?\n(a) Maharashtra\n(b) New Delhi\n(c) Punjab\n(d) Haryana\n", "b"),
        Question("What is 2 * 3?\n(a) 3\n(b) 4\n(c) 5\n(d) 6\n", "d"),
        Question("What is the smallest planet in our solar system?\n(a) Earth\n(b) Mars\n(c) Mercury\n(d) Saturn\n", "c"),
        Question("What is the chemical symbol for oxygen?\n(a) O2\n(b) H2O\n(c) CO2\n(d) NaCl\n", "a"),
        Question("Who wrote 'Sonnets'?\n(a) Charles Dickens\n(b) Mark Twain\n(c) William Shakespeare\n(d) Jane Austen\n", "c"),
    ]
    print("Welcome to the Quiz Game!")
    run_quiz(questions)
if __name__ == "__main__":
    main()