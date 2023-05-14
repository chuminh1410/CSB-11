import random

def generate_question():
    num1 = random.randint(1, 20)
    num2 = random.randint(1, 20)
    operator = random.choice(['+', '-', '*', '/'])
    operator_incor = random.choice(['+', '-'])
    question = f"{num1} {operator} {num2}"
    incorrect_answer = f"{eval(question)} {operator} {num1}"
    correct_answer = eval(question)
    if operator == '/':
        while num1 % num2 != 0:
            num1 = random.randint(1, 20)
            num2 = random.randint(1, 20)
            question = f"{num1} {operator} {num2}"
            correct_answer = eval(question)
    return question, correct_answer, eval(incorrect_answer)


def main_game():
    print("== FREAKING MATH CONSOLE ==")
    print("Give correct answers to get scores.")
    score = 0
    game_over = False
    while not game_over:
        question, correct_answer, incorrect_answer  = generate_question()
        random_ans = random.choice([correct_answer,incorrect_answer])
        print(question, "=", random_ans )
        answer = int(input("1 for True, 0 for False: "))
        if answer == 1 and random_ans == correct_answer :
            score += 1
            print("Score:", score)
        elif answer == 0 and random_ans != correct_answer:
            score += 1
            print("Score:", score)
        else:
            print("Incorrect.")
            game_over = True
    print("== GAME OVER ==")
    print("Your total score is", score)

main_game()