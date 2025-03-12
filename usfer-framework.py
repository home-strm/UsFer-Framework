from cryptography.fernet import Fernet
from colorama import Fore
import time
import click
import os.path
# Imports required modules.

fileCheck = os.path.exists("encKey.txt") # Checks if files exists.

if fileCheck == True:
    with open("encKey.txt", mode="rb") as keyRaw:
        key = keyRaw.read()
        f = Fernet(key)
else:
    with open("encKey.txt", mode="wb") as keyRaw:
        key = Fernet.generate_key()
        keyRaw.write(key)
        f = Fernet(key)
# If file exists, key is read. If not, a new key is generated and saved to 'encKey.txt'.

def mainMenu():
    global option
    click.clear()
    print(Fore.GREEN + "     ____ ___      ___________              ")        
    print(Fore.GREEN + "    |    |   \_____\_   _____/__________    ")
    print(Fore.GREEN + "    |    |   /  ___/|    __)/ __ \_  __ \   ")
    print(Fore.GREEN + "    |    |  /\___ \ |     \\  ___/|  | \/   ")
    print(Fore.GREEN + "    |______//____  >\___  / \___  >__|      ")
    print(Fore.GREEN + "                 \/     \/      \/          ")
    print(Fore.GREEN + "                                            ")
    time.sleep(2)
    print(Fore.RED + "                   OPTIONS                 ")
    print(Fore.WHITE + " 1. Generate new key.   2 . Encrypt string.")
    print(Fore.WHITE + " 3. Decrypt string.     4 . Exit.          ")
    print()
    option = input("[1,2,3,4] : ")
    mainProcess()
# Main menu function, gives user options to chose what they want to do.

def mainProcess():
    if option == "1":
        global f
        click.clear()
        genKey = Fernet.generate_key()
        print(Fore.GREEN + "Generated key: ")
        print(Fore.WHITE + genKey.decode())
        input("Press any key to save and continue.")
        with open("encKey.txt", mode="wb") as encKeyRaw:
            encKeyRaw.write(genKey)
            f = Fernet(genKey)
        mainMenu()
    elif option == "2":
        click.clear()
        token = input("Enter text to encrypt: ")
        click.clear()
        tokenEnc = f.encrypt(token.encode())
        print(Fore.GREEN + "Encrypted string: " + tokenEnc.decode())
        input(Fore.WHITE + "Press any key to save and continue.")
        click.clear()
        encFileName = input("Filename: "), ".txt"
        with open(str(encFileName), mode="wb") as tokenEncRaw:
            tokenEncRaw.write(tokenEnc)
        mainMenu()
    elif option == "3":
        click.clear()
        print(Fore.GREEN + "Please input the filename of the encrypted string saved.")
        fileName = input(Fore.WHITE + "Input: "), ".txt"
        with open(str(fileName), mode="rb") as fileNameRaw:
            fileContents = fileNameRaw.read()
            fileDecrypt = f.decrypt(fileContents)
            click.clear()
            print(Fore.GREEN + "The contents of the decrypted file are: ")
            print(Fore.WHITE + fileDecrypt.decode())
            input("Press any key to save and continue.")
            click.clear()
            newFileName = input("Filename: "), ".txt"
            with open(str(newFileName), mode="w") as newDecFile:
                newDecFile.write(fileDecrypt.decode())
            mainMenu()
    elif option == "4":
        click.clear()
        exit()
# Main process, allows the program to function.

mainMenu()
# Calls the mainMenu() fucntion to start the program.