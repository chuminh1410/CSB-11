print("== Input file content below ==")
lines = []

while True:
    line = input()
    if line == "":
        break
    lines.append(line)

file_path = "BTVN\\BTVN Buổi 12\\user-inputs.txt"

with open(file_path, 'w') as file:
    file.write("\n".join(lines))

print("== Input recorded in user-inputs.txt ==")