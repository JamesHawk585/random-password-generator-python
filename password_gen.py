from prettycli import red, bold
from simple_term_menu import TerminalMenu
import os
import random 

class Cli():
    def start(self): 
        # os.system("clear")
        print('Random Password Generaor')
        options = ["Generate Random Password"]
        terminal_menu = TerminalMenu(options)
        menu_entry_index = terminal_menu.show()
        selection = options[menu_entry_index]
        return selection
    
def generate_random_password(selection):
    password_length = 10
    lowercase_chars = 'abcdefghijklmnopqrstuvwxyz'
    uppercase_chars = lowercase_chars.upper()
    numbers = '0123456789'
    special_chars = '/!@#$%^&*()-_=}+[]{`|;:/,.<>?/\"'
    password=''
    my_string = lowercase_chars + uppercase_chars + numbers + special_chars
    for x in range(password_length):
        random_char = random.randrange(1, 93)
        password += my_string[random_char]
    print(password)
    return password

def handle_selection(selection): 
    generate_random_password(selection)

        # print(my_string[random_char])

app = Cli()
selection = app.start()
handle_selection(selection)


    