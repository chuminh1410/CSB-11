file_path = 'BTVN\\BTVN Buổi 12\\1.txt'

with open(file_path, 'r') as file:
    lines = file.readlines()

print("List of names:")
for line in lines:
    name = line.strip()
    print(f"- {name}")
