number = int(input("Input a number: "))

while number <=0 :
    number = int(input("Input a number that is larger than 0: "))
    
count = len(str(number))
print(f"This number has {count} digit(s)")