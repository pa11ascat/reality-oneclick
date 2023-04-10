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

a = menu()

