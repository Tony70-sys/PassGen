import random
import string
import time
## Anthony Varela, 2026
## Personal project. This is my first python project.
## This password generator performs the function of providing strong passwords to users.

uppercaseLetters = list(string.ascii_uppercase) ##Array of all the uppercase letters 
lowercaseLetters = list(string.ascii_lowercase) ##lowercase letters
numbers = list(string.digits) ##numbers
specialCharacters = list(string.punctuation) #special characters

def passwordLength():
    ##We ask the user to provide the parameters for generating the password
    while True: ##infinite loop until we break out of it
        length = int(input("Please introduce the length of the password (8 or more characters): ")) ##store the input in a variable
        if length >= 8: ##check if the input is long enough
            break ##if so, exit the loop
        print("Password not long enough, try again") ##if it's not print this line and keep looping
    time.sleep(1)
    print("Desired password length: " , length)
    ##askUserParameters(length)
    return(length)

def askUserParameters(length):
    while True: 
        upper = str(input("Uppercases in it: (y/n): ")).lower()
        if upper == "y" or upper == "n": 
            break 
        print("(y/n)")

    while True: 
        lower = str(input("Lowercases in it: (y/n): ")).lower()
        if lower == "y" or lower == "n": 
            break 
        print("(y/n)")

    while True: 
        num = str(input("Numbers in it: (y/n): ")).lower()
        if num == "y" or num == "n": 
            break 
        print("(y/n)")    

    while True: 
        chars = str(input("Special characters in it: (y/n): ")).lower()
        if chars == "y" or chars == "n": 
            break 
        print("(y/n)")

    addParameters(upper, lower, num, chars, length)

def addParameters(upper, lower, num, chars, length):
    lochars = []
    pswd = []
    if upper == "y":
        lochars.append(uppercaseLetters)
        pswd.append(random.choice(uppercaseLetters))

    if lower == "y":
        lochars.append(lowercaseLetters)
        pswd.append(random.choice(lowercaseLetters))

    if num == "y":
        lochars.append(numbers)
        pswd.append(random.choice(numbers))

    if chars == "y":
        lochars.append(specialCharacters)
        pswd.append(random.choice(specialCharacters))

    if not lochars:
        print("You have to select at least one option as yes!")
        askUserParameters(length)
    else: 
        generatePassword(pswd, length, lochars)

def generatePassword(pswd, length, lochars):
    #Function that generates the password
    print("Generating password...")
    time.sleep(1)

    currentLength = len(pswd)

    for i in range(0, length - currentLength, 1):
        ch = random.choice(random.choice(lochars))
        pswd.append(ch)

    random.shuffle(pswd)
    final = "".join(pswd)
    print(final)

passwordLength()