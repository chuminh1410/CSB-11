number_list = ['I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX', 'X',
               'XI', 'XII', 'XIII', 'XIV', 'XV', 'XVI', 'XVII', 'XVIII', 'XIX', 'XX']

numbers = {}

for i in range(len(number_list)):
    numbers[number_list[i]] = i + 1

roman_number = input("Input a Roman number: ")

if roman_number in numbers:
    arabic_number = numbers[roman_number]
    print("Arabic number:", arabic_number)
else:
    print("Not found.")
