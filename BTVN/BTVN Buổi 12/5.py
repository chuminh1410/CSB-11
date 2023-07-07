with open('BTVN\\BTVN Buổi 12\\question-bank.txt', 'r') as file:
    lines = file.readlines()

question_bank = []
for line in lines:
    question, answer = line.strip().split(',')
    question_bank.append((question.strip(), answer.strip()))

print("Give the correct answers to get points.")

score = 0
total_questions = len(question_bank)

for question, answer in question_bank:
    user_answer = input(f"{question} ")
    if user_answer == answer:
        score += 1

print(f"== You get {score}/{total_questions} points ==")
