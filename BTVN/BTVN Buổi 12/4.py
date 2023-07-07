import datetime

print("== Input file content below ==")
lines = []

while True:
    line = input()
    if line == "":
        break
    lines.append(line)

file_path = "BTVN\\BTVN Buổi 12\\input-logs.txt"

with open(file_path, 'a') as file:
    current_time = datetime.datetime.now()

    file.write(f"\n== Inputs at {current_time} ==\n")

    file.write("\n".join(lines) + "\n")

print("== Input recorded in input-logs.txt ==")
