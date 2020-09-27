import time
import getpass
print('Welcome to                                                    ')
print(' ______  ______  __    __  ______  __   __  ______  ______    ')
print('/\  == \/\  __ \/\ "-./  \/\  ___\/\ "-.\ \/\  __ \/\  ___\   ')
print('\ \  __<\ \  __ \ \ \-./\ \ \  __\\ \ \-.  \ \ \/\ \ \___  \  ')
print(' \ \_\ \_\ \_\ \_\ \_\ \ \_\ \_____\ \_\\"\_\ \_____\/\_____\ ')
print('  \/_/ /_/\/_/\/_/\/_/  \/_/\/_____/\/_/ \/_/\/_____/\/_____/ ')
print('                                                              ')                    
print('                 [Version 0.3.0.2020.9.27]                    ')
print('       (c) 2020 Takeout Studios. All rights reserved.         ')
print('                      Python Edition                          ')
print('Beta Protocol ACTIVE')
print("Unfortunately, during the beta, you only may view the code used. RamenOS will not run in it's current form. Type 'leave' to exit")
userInput='o'

def users():
    userInput = input(r"C:\Users\> ")
    if userInput == "dir":
        print(r"--Directory of C:\Users--")
        print("Desktop      [Folder]")
        print("Documents    [Folder]")
        print("Downloads    [Folder]")
        print("Games        [Folder]")
        print("Music        [Folder]")
        print("Pictures     [Folder]")
        print("Videos       [Folder]")
        users()
    if userInput == "cd Desktop":
        print("Not implemented")
    if userInput == "cd Documents":
        print("Not implemented")
    if userInput == "cd Downloads":
        print("Not implemented")
    if userInput == "cd Games":
        print("Not implemented")
    if userInput == "cd Music":
        print("Not implemented")
    if userInput == "cd Pictures":
        print("Not implemented")
    if userInput == "cd Videos":
        print("Not implemented")
    if userInput == "cd ..":
        start()
def start():
    userInput = input("C:\> ")
    if userInput == "dir":
        print("--Directory of C:\--")
        print("Program Files          [System Folder]")
        print("Program Files (x86)    [System Folder]")
        print("Users                  [Folder]")
        print("RamenOS                [System Folder]")
        start()
    elif userInput == "cd Program Files":
        print("Files hidden to protect vital system files!")
        start()
    elif userInput == "cd Program Files (x86)":
        print("Files hidden to protect vital system files!")
        start()
    elif userInput == "cd Users":
        users()
    elif userInput == "cd RamenOS":
        print("Files hidden to protect vital system files!")
        start()
    elif userInput == "cd ..":
        print("Already in root directory!")
        start()
    else:
        print("Invalid syntax.")
        start()
def beta():
    userInput = input("BETA COMMANDS> ")
    if userInput == "leave":
        print("Leaving in")
        time.sleep(1)
        print("5...")
        time.sleep(1)
        print("4...")
        time.sleep(1)
        print("3...")
        time.sleep(1)
        print("2...")
        time.sleep(1)
        print("1...")
        time.sleep(1)
        print("Goodbye!")
        time.sleep(1)
        quit()
    elif userInput == "admin.disableBeta = 'true'":
        sure = "n"
        sure = input(r"Are you sure? (Y/N): ")
        if sure == "n":
            print("Cancelled.")
            beta()
        elif sure == "y":
            print("Password input hidden.")
            password = "null"
            password = getpass.getpass(r"Please input admin passcode: ")
            if password == "ilikeboobz":
                print("Starting RamenOS Beta")
                start()
            else:
                print("Invalid password. Quitting...")
                time.sleep(1)
                quit()
        else:
            print("Invalid Syntax.")
            beta()
    else:
        print("Invalid Syntax.")
        beta()
beta()
#Beta Protocol
