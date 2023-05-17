import random
import select
import sys
from termcolor import colored 

game_over = False
score = 0
timer = 10
harder = 5
random_color = ""

class TimeoutException(Exception):
    pass

def signal_handler(signum, frame):
    raise TimeoutException("Time is up!")

def timeout_input(prompt, timeout):
    for i in range(timeout, 0, -1):
        if select.select([sys.stdin], [], [], 1)[0]:
            user_input = input()
            break
        sys.stdout.write(f"\r{prompt} (timeout in {i} seconds): ")
        sys.stdout.flush()
    else:
        print()
        user_input = None

    return user_input

def color():
    global random_color
    color_text = ["black","red","green","yellow","blue",
                  "magenta","cyan","white","light_grey",
                  "dark_grey","light_red","light_green",
                  "light_yellow","light_blue","light_magenta","light_cyan"]
    random_color = random.choice(color_text)
    
    

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
    global game_over
    global score
    print("== FREAKING MATH CONSOLE ==")
    print("Give correct answers to get scores.")

    while not game_over:
        color()
        question, correct_answer, incorrect_answer  = generate_question()
        random_ans = random.choice([correct_answer,incorrect_answer])
        print_question = print(question, "=", random_ans )
        print(colored(print_question, random_color))
        
        answer = timeout_input("1 for True, 0 for False", timer)
            
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