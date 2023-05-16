import random
import time 

timer = 30
harder = 5

def clock():
    global timer 
    timer -= 1 
    if timer != 0:
        print("You have", timer, "seconds left")
        timer = timer - 1
        time.sleep(1)

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


def main_game():
    print("== FREAKING MATH CONSOLE ==")
    print("Give correct answers to get scores.")
    score = 0
    game_over = False
    while not game_over:
        question, correct_answer, incorrect_answer  = generate_question()
        random_ans = random.choice([correct_answer,incorrect_answer])
        print(question, "=", random_ans )
        
        clock()
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