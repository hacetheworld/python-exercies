import pyfiglet
from termcolor import colored
import colorama
colorama.init()

message = input('What Message do you want to print : ')
color = input('In what color : ')
result = pyfiglet.figlet_format(message)
print(colored(result, color=color))
