year = input("What year is it? ")

if len(year) == 4 and year.isdigit():
    print("\t\t\t. : .")
    print("\t\t      '.  :  .'")
    print("HAPPY NEW YEAR","     .   '.:.'   .")
    print("!!!", year, "!!!","       .   '.:.'   .")
    print("\t\t      .'  :  '.")
    print("\t\t        ' : '")
else:
    print("Invalid input! Please enter a valid year (4 digits).")
