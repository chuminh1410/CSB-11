numbers = {'I': 1, 'II': 2, 'III': 3, 'IV': 4, 'V': 5,
           'VI': 6, 'VII': 7, 'VIII': 8, 'IX': 9, 'X': 10}

numbers_2 = {'XI': 11, 'XII': 12, 'XIII': 13, 'XIV': 14, 'XV': 15,
             'XVI': 16, 'XVII': 17, 'XVIII': 18, 'XIX': 19, 'XX': 20}

numbers.update(numbers_2)

roman_number = input("Input a Roman number: ")

if roman_number in numbers:
    arabic_number = numbers[roman_number]
    print("Arabic number:", arabic_number)
else:
    print("Not found.")
