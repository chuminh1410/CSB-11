from termcolor import colored

user_input = input(colored("HELLO", "red"))
#Where string is the prompt for the input command and color
#is a valid termcolor color
print(colored(user_input,"blue"))