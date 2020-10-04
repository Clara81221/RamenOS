import playsound
import time
import getpass
import os
import sys
print("Loading...")
playsound.playsound('Bleep.mp3')
time.sleep(1)
words = ("""
Startup Process
├──System check
   ├──CPU...     OK
   ├──GPU...     OK
   ├──Memory...  OK
   ├──Floppy...  OK
   └──Network... OK
├──System check complete!
└──System specs check
   ├──300 MB Hard Disk Drive
   ├──2683 KB memory loaded
   ├──Intel (R) Pentium 319.7 Mhz/s
   └──3.5 in Floppy
└──Starting driver library
   ├──Intel (R) Graphics Control Panel
   ├──Intel (R) VGA Graphics
   ├──Crucial 3MB Memory
   ├──Takeout Corp. 3.5 in Floppy
   ├──Samsung 300 MB Hard Disk Drive
   └──Takeout Ethernet Network Card
└──Checking for updates...
   └──No update required.
├──Starting RamenOS Interface
├──Beginning Server-Client connection "SUPERHOT Official Discord"
├──Beginning Server-Client connection "Server 383"
├──Beginning Server-Client connection "Server 5"
├──Beginning Server-Client connection "Server 4"
├──Beginning Server-Client connection "Server 3"
├──Beginning Server-Client connection "Server 2"
├──Beginning Server-Client connection "Server 1"
├──Beginning AI Server connection "orientalramen408.github.io/BETAAIPROGRAM"
├──Startup process success
└──Login process
""")
for char in words:
    time.sleep(0.05)
    sys.stdout.write(char)
    sys.stdout.flush()
userRamenUsername = "null"
userRamenPassword = "null"
def loginUsername():
    userRamenUsername = input("USERNAME: ")
    #You can change the user settings to your liking
    if userRamenUsername == "Ramen":
        userRamenPassword()
    else:
        words = "Incorrect Username"
        for char in words:
            time.sleep(0.1)
            sys.stdout.write(char)
            sys.stdout.flush()
        userRamenUsername()
def loginPassword():
    userRamenPassword = getpass.getpass("PASSWORD: ")
    if userRamenPassword == "9378":
        print("Welcome, Ramen")
        time.sleep(2)
        start()
    else:
        playsound.playsound('Denied.mp3')
        words = "Incorrect Password"
        for char in words:
            time.sleep(0.1)
            sys.stdout.write(char)
            sys.stdout.flush()
        userRamenPassword()        
print("""













































""")
time.sleep(.1)
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
    print("""

















































    """)
    print("[O----]")
    print("Loading...")
    time.sleep(1)
    print("""

















































    """)
    print("[OO---]")
    print("Loading...")
    time.sleep(1)
    print("""

















































    """)
    print("[OOO--]")
    print("Loading...")
    time.sleep(1)
    print("""

















































    """)
    print("[OOOO-]")
    print("Loading...")
    time.sleep(1)
    print("""

















































    """)
    print("[OOOOO]")
    print("Loading complete!")
    print("""

















































    """)
    print('Welcome to                                                    ')
    time.sleep(.5)
    print('oooooooooo                                                   ooooooo    oooooooo8 ')
    playsound('RamenOSJingle1.mp3')
    time.sleep(.5)
    print(' 888    888  ooooooo   oo ooo oooo   ooooooooo8 oo oooooo  o888   888o 888        ')
    playsound('RamenOSJingle2.mp3')
    time.sleep(.5)
    print(' 888oooo88   oo   888   888 888 888 888      88  888   888 888     888 888        ')
    playsound('RamenOSJingle3.mp3')
    time.sleep(.5)
    print(' 888  oo88   ooooo888   888 888 888 888oooooo8   888   888 888     888  888oooooo  ')
    playsound('RamenOSJingle4.mp3')
    time.sleep(.5)
    print(' 888  88o  888    888   888 888 888 888          888   888 888o   o888         888 ')
    playsound('RamenOSJingle5.mp3')
    time.sleep(.5)
    print('o888o  88o8 88ooo88 8o o888o888o888o  88oooo888 o888o o888o  88ooo88   o88oooo888')
    playsound('RamenOSJingle6.mp3')
    time.sleep(.1)
    print('-----------------------------------------------------------------------------------')                    
    time.sleep(.1) 
    print('                             [Version 0.9.0.10.4.2020]                       ')
    playsound('ERR.mp3')
    time.sleep(.1) 
    print('                     (c) 2020 Takeout Studios. All rights reserved.         ')
    time.sleep(.1)
    print('                                    Python Edition                          ')
    time.sleep(1)
    #Yooo, that's dope! it actually works! I don't care if it's sloppy, FU
    userInput = input("C:\> ")
    if userInput == "dir":
        print("--Directory of C:\--")
        print("Program Files          [System Folder]")
        print("Program Files (x86)    [System Folder]")
        print("Users                  [Folder]")
        print("RamenOS                [System Folder]")
        start()
    elif userInput == "shutdown /s /t 5":
        print("Leaving in")
        time.sleep(1)
        print("5...")
        playsound("RamenOS Exit1.mp3")
        time.sleep(1)
        print("4...")
        playsound("RamenOS Exit1.mp3")
        time.sleep(1)
        print("3...")
        playsound("RamenOS Exit1.mp3")
        time.sleep(1)
        print("2...")
        playsound("RamenOS Exit1.mp3")
        time.sleep(1)
        print("1...")
        playsound("RamenOS Exit1.mp3")
        time.sleep(1)
        print("Goodbye!")
        playsound("RamenOS Exit5.mp3")
        time.sleep(5)
        quit()
    elif userInput == "shutdown /s /t 5":
        print("Leaving in")
        time.sleep(1)
        print("5...")
        playsound("RamenOS Exit1.mp3")
        time.sleep(1)
        print("4...")
        playsound("RamenOS Exit1.mp3")
        time.sleep(1)
        print("3...")
        playsound("RamenOS Exit1.mp3")
        time.sleep(1)
        print("2...")
        playsound("RamenOS Exit1.mp3")
        time.sleep(1)
        print("1...")
        playsound("RamenOS Exit1.mp3")
        time.sleep(1)
        print("Goodbye!")
        playsound("RamenOS Exit5.mp3")
        time.sleep(5)
        quit()
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
    elif userInput == "clr":
        clear()
    else:
        print("Invalid syntax.")
        start()
loginUsername()
