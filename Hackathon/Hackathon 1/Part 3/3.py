import calendar

month = int(input("Input a month: "))

if month < 1 or month > 12:
    print("Invalid input. Enter a month between 1 and 12.")
else:
    year = 2023 
    num_days = calendar.monthrange(year, month)[1]
    print("Number of days:", num_days)
