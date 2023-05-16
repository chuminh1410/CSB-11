import random
from threading import Timer

game_over = False
score = 0
timer = 10
harder = 5


def generate_question():
    global harder
    harder += 5
    num1 = random.randint(1 + harder , 50 + harder)
    num2 = random.randint(1 + harder , 50 + harder)
    num_random = random.randint(1 + harder , 50 + harder)
    operator = random.choice(['+', '-', '*', '/'])
    operator_incor = random.choice(['+', '-'])
    question = f"{num1} {operator} {num2}"
    incorrect_answer = f"{eval(question)} {operator_incor} {num_random}"
    correct_answer = eval(question)
    if operator == '/':
        while num1 % num2 != 0:
            num1 = random.randint(1 + harder , 50 + harder)
            num2 = random.randint(1 + harder , 50 + harder)
            question = f"{num1} {operator} {num2}"
            correct_answer = eval(question)
    return question, correct_answer, eval(incorrect_answer)

def times_up():
    global game_over
    game_over = True

    print("Times up!!!. Press any key to quit.")

def main_game():
    global game_over
    global score

    print("== FREAKING MATH CONSOLE ==")
    print("Give correct answers to get scores.")

    while not game_over:
        question, correct_answer, incorrect_answer  = generate_question()
        random_ans = random.choice([correct_answer,incorrect_answer])
        print(question, "=", random_ans )
        
        t = Timer(timer, times_up)
        t.start()
        prompt = "1 for True, 0 for False. You have %d seconds to choose the correct answer...\n" % timer
        answer = input(prompt)
        t.cancel()
            
        if answer == "1" and random_ans == correct_answer:
            score += 1
            print("Score:", score)
        elif answer == "0" and random_ans != correct_answer:
            score += 1
            print("Score:", score)
        else:
            print("Incorrect.")
            game_over = True
    print("== GAME OVER ==")
    print("Your total score is", score)

main_game()