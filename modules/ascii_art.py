from termcolor import colored
from pyfiglet import figlet_format


def input_gatherer():
    s = input("what do you want to print: ")
    c = input("what colour do you want to print in: ")
    avail_colours = ('red', 'green', 'cyan', 'yellow',
                     'blue', 'white', 'grey', 'magenta')
    while not s or (c not in avail_colours):
        if type(s) != str:
            s = input("What do you want to print: ")
        elif c not in avail_colours:
            c = input("What colour do you want to print: ")
    return (s, c)


user_input = input_gatherer()

# prints to the terminal

print(colored(figlet_format(user_input[0]), user_input[1]))
