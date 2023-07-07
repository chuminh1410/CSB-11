while True:
    name = input("Input file name: ")
    file_name = "BTVN\\BTVN Buổi 12\\" + name
    try:
        with open(file_name, 'r') as file:
            file_content = file.read()

        print("File content:")
        print(file_content)
        break

    except FileNotFoundError:
        print("File not found.")
