import os
import subprocess

def menu()-> int:
    menu_desc = '''
    1.Configuration

    2.Reality ping

    3.Export Links

    ___________________________

    0.Exit


    '''
    print(menu_desc)

    num = int(input("please write a number from above and press enter: "))

    return num

def configuration():
    pass

while (True):
    choice = menu()
    match choice:
        case 1:
            print("Option 1 selected")
        case 2:
            os.system("clear")
            domain = str(input("Enter Your Domain(e.g. digikala.com): "))
            result = os.system("xray tls ping " + domain)
            print(result)
        case 3:
            print("Option 3 selected")
        case 0:
            print("Exiting program")
            break
        case _:
            print("wrong value selected")

        
