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

##first function to ask the user for the length of the password
def passwordLength():
    ##We ask the user to provide the parameters for generating the password
    while True: ##infinite loop until we break out of it
        length = int(input("Please introduce the length of the password (8 or more characters): ")) ##store the input in a variable
        if length >= 8: ##check if the input is long enough
            break ##if so, exit the loop
        print("Password not long enough, try again") ##if it's not print this line and keep looping
    time.sleep(1)
    print("Desired password length: " , length)
    askUserParameters(length) ##call next function

##function to ask the user for parameters. It's triggered by the passwordLength function.
##Set of continous while loops until the user introduces the right input, if so, it will break out of the loop.
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

    addParameters(upper, lower, num, chars, length) ##call next function.

##function to add desired characters to the array of possible chars for the password. Triggered by the askUserParameters function
##It check if a condition is met and then appending one symbol from that specific list to the initial password
def addParameters(upper, lower, num, chars, length):
    lochars = [] ##initial empty list that will contain lists (uppercaseLetters, lowercaseLetters, numbers, specialCharacters)
    pswd = [] ##initial password in form of array that will be empty and then chars will be appended to it.
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

    if not lochars: ##check to see if there was at least one option selected (not an empty array (list) of lists)
        print("You have to select at least one option as yes!") ##if empty, 
        askUserParameters(length) ##call the function askUserParameters again
    else: 
        generatePassword(pswd, length, lochars) ##otherwise, proceed to call next function


##actual function that generates the password based on desired type of chars. Triggered by addParameters function.
def generatePassword(pswd, length, lochars):
    print("Generating password...") 
    time.sleep(1)

    currentLength = len(pswd) ##current length of password after meeting base conditions

    for i in range(0, length - currentLength, 1): ## fill the rest of the password with what is left of the 
        ch = random.choice(random.choice(lochars)) ##length and choosing randomly form the list of lists (letters, chars, ...)
        pswd.append(ch) ##append each random item to the password

    random.shuffle(pswd) ##mix the characters in a random order
    final = "".join(pswd) ##join the list of characters to the empty string to create the password
    print(final) ##print the final password

##initial call to the function to trigger the rest.
passwordLength()