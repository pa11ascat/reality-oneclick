import os
from enum import Enum
from uuid import UUID

#define some const var
KEYS_LENGTH=43
PRIV_KEY_START=13
SHORT_ID_NUM=1

class Menu(Enum):
    EXIT = 0
    CONFIG = 1
    RPING = 2
    EXPORT = 3
    HOME = -1


def is_valid_uuid(uuid_to_test:str, version: int=4) -> bool:
    try:
        uuid_obj = UUID(uuid_to_test, version=version)
    except ValueError:
        return False
    return str(uuid_obj) == uuid_to_test


def magic_string_maker(string: str) -> (str, int):
    string_list = string.split(",")
    result = ''
    counter = 0
    for counter in range(len(string_list)):
        if counter == len(string_list)-1:
            result = result + '"' + string_list[counter] + '"'
        else:
            result = result + '"' + string_list[counter] + '",\n'
    return result, len(string_list)+1


def menu() -> int:
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
    domain = str(input("Enter Your Domain(e.g. debian.org, -1 to exit): "))
    if domain == "-1":
        return Menu.HOME
    else: 
        result = os.system("xray tls ping " + domain)        
        print(result)
        return Menu.RPING

def configuration():
    os.system("clear")
    #uuid4 setup
    uuid4_vision = input("Import your uuid4 for vision(enter for generating one): ")
    if not(is_valid_uuid(uuid4_vision)):
        uuid4_vision = os.system("xray uuid4")
        print(uuid4_vision+"\n")
    uuid4_h2 = input("Import your uuid4 for h2(enter for generating one): ")
    if not(is_valid_uuid(uuid4_h2)):
        uuid4_h2 = os.system("xray uuid4")
        print(uuid4_h2+"\n")
    
    
    #generating key
    keys = os.system("xray x25519")
    priv_key = keys[PRIV_KEY_START:PRIV_KEY_START+KEYS_LENGTH]
    pub_key = keys[-KEYS_LENGTH,-1]
    os.system(f"echo {keys} > key")

    #getting dest and serverNames

    dest_domain = input("Import dest domain: ")

    serverNames_str = input("Import Allowed domains(e.g. debian.org,ftp.debian.org): ")

    serverNames = magic_string_maker(serverNames_str)

    #short Id

    short_ids_str = input("Import your shortIds(seperated by comma e.g. ss2,dfaf3 or type how many you want and we generate it for you e.g. 5): ")

    shid_str = ""

    if short_ids_str.isnumeric():
        for i in range(int(short_ids_str)):
            shid = os.system("openssl rand -hex 8")
            if i == int(short_ids_str)-1:
                shid_str += f"{shid}"
            else:
                shid_str += f"{shid},"
        
        short_ids, SHORT_ID_NUM = magic_string_maker(shid_str)
            
    else:
        short_ids, SHORT_ID_NUM = magic_string_maker(short_ids_str)

    # download config.json

    #edit config.json


def export() -> str:
    pass


choice = Menu.HOME

while (True):
    if choice == Menu.HOME:
        choice = menu()
    
    match choice:
        case Menu.CONFIG:
            choice = configuration()
        case Menu.RPING:
            choice = reality_ping()
        case Menu.EXPORT:
            print("Option 3 selected")
            choice = Menu.HOME
        case Menu.EXIT:
            print("Exiting program")
            break


        
