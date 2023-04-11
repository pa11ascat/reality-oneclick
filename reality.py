import os
from enum import Enum

class Menu(Enum):
    EXIT = 0
    CONFIG = 1
    RPING = 2
    EXPORT = 3
    HOME = -1

def menu()-> int:
    menu_desc = '''
    ----------------------------
    1.Configuration

    2.Reality ping

    3.Export Links

    0.Exit
    ___________________________

    '''
    print(menu_desc)

    num = int(input("please write a number from above and press enter: "))
    if num == 0:
        return Menu.EXIT
    elif num == 1:
        return Menu.CONFIG
    elif num == 2:
        return Menu.RPING
    elif num == 3:
        return Menu.EXPORT
    else:
        return Menu.HOME

def reality_ping():
    print("----------------------------")
    domain = str(input("Enter Your Domain(e.g. digikala.com, -1 to exit): "))
    if domain == "-1":
        return Menu.HOME
    else: 
        result = os.system("xray tls ping " + domain)        
        print(result)
        return Menu.RPING

def configuration():
    return Menu.HOME

choice = Menu.HOME

while (True):
    if choice == Menu.HOME:
        choice = menu()
    
    match choice:
        case Menu.CONFIG:
            print("Option 1 selected")
            choice = configuration()
        case Menu.RPING:
            choice = reality_ping()
        case Menu.HOME:
            print("Option 3 selected")
            choice = Menu.HOME
        case 0:
            print("Exiting program")
            break


        
