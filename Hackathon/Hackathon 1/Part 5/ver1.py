import random

def generate_question():
    num1 = random.randint(1, 20)
    num2 = random.randint(1, 20)
    operator = random.choice(['+', '-', '*', '/'])
    question = f"{num1} {operator} {num2}"
    answer = eval(question)
    return question, answer

def play_game():
    print("== FREAKING MATH CONSOLE ==")
    print("Give correct answers to get scores.")
    score = 0
    game_over = False
    while not game_over:
        question, answer = generate_question()
        print(question)
        user_answer = int(input("1 for True, 0 for False: "))
        if user_answer == int(answer == True):
            score += 1
            print("Score:", score)
        else:
            print("Incorrect.")
            game_over = True
    print("== GAME OVER ==")
    print("Your total score is", score)

play_game()


