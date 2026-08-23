## First version of PassGen
"""
import random
import string
import time
## Anthony Varela, 2026
## Personal project. This is my first python project.
## This password generator performs the function of providing strong passwords to users.

##Version before making updates. Changes were suggested by ChatGPT and I implemented them.

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
"""
## Second enhanced version of PassGen.
"""
import random
import string
import time
import tkinter as tk
## Anthony Varela, 2026
## Personal project and my first Python project.
## A password generator that creates strong, randomized passwords based on user preferences.

uppercaseLetters = list(string.ascii_uppercase) ##array of uppercases letters
lowercaseLetters = list(string.ascii_lowercase) ##array of lowercase letters
numbers = list(string.digits) ##array of numbers
specialCharacters = list(string.punctuation) ##array of special characters

## First function of the code. It tries to get the desired length; if it's a number goes to the try block, if it's 
## equal or greater than 12, it will delay one second, print the message, and return the specified length.
## If it's a number but not greater than 12, it will print Password not long enough and stay inside the while loop.
## If it goes to the except ValueError, it means that the input was not a number; this will print the message and
## call (return) the function again to show the message from the beginning again.
## It returns the length of the password.
def passwordLength():
    try:
        while True:
            length = int(input("Please introduce the length of the password (12 or more characters): ")) 
            if length >= 12:
                time.sleep(1)
                print("Desired password length: " , length)
                return length
            print("Password not long enough, try again")
    except ValueError:
        print("Please insert a number")
        return passwordLength()

## Second function of the code. This function repeats four preferences asked to the user. If the input for a block 
## is y/n, it will check if it's an option and break out of the loop. If the input is not one of the
## specified characters for answers, it will print the message and stay in the while loop.
## At the end we check if there is at least one option marked as yes; if there is not, it will print 
## the message and call (return) the function again.
## It returns the values for each of the options.
def askUserParameters():
    while True: 
        upper = input("Uppercases in it: (y/n): ").lower()
        if upper in ("y", "n"):
            break 
        print("(y/n)")

    while True: 
        lower = input("Lowercases in it: (y/n): ").lower()
        if lower in ("y", "n"):
            break 
        print("(y/n)")

    while True: 
        num = input("Numbers in it: (y/n): ").lower()
        if num in ("y", "n"):
            break 
        print("(y/n)")    

    while True: 
        chars = input("Special characters in it: (y/n): ").lower()
        if chars in ("y", "n"):
            break 
        print("(y/n)")

    if upper == "n" and lower == "n" and num == "n" and chars == "n":
        print("You have to select at least one option as yes!") 
        return askUserParameters()
    
    return upper, lower, num, chars

## Third function of the code. This function adds the selected parameters to a list of lists (lochars) of possible characters
## for the password (pswd) if they are marked as yes. Additionally, for each of the options, if they are marked as yes,
## it will add one character to pswd to ensure that there is at least one character for each option selected.
## It returns the initial password and the list of lists of possible characters to choose from.
def addParameters(upper, lower, num, chars):
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

    return pswd, lochars

##Fourth function of the code. This function generates the password based on the variables pswd, length and lochars.
## It prints a message, delays for a second; then we get the current length of the password (pswd).
## The for loop goes from 0 (i) to the final length (length - currentLength). During each iteration, we append a random character
## from one of the list(s) in lochars. Once it meets the final length, it shuffles the password (pswd|array).
## Lastly we make a variable to store and join an empty string with the characters in pswd.
## It returns the password as a string.
def generatePassword(pswd, length, lochars):

    print("Generating password...") 
    time.sleep(1)
    currentLength = len(pswd) 

    for i in range(length - currentLength):
        ch = random.choice(random.choice(lochars))
        pswd.append(ch)

    random.shuffle(pswd)
    final = "".join(pswd)
    return final

## While loop that triggers the program with passwordLength(). 
## It uses each of the variables (each variable triggers a function and stores a variable(s)). It prints the final password
## Then we use another loop to ask the user if they want to generate another password or stop the program.
## If the input is y/n, it will break out of the inner loop and see if the answer is no to break out of the outter while loop. 
## If the answer is not y/n, it will print the message and stay in the inner while loop. If the answer is yes, it will repeat
## again the outter loop.
## It prints the password(s)
while True:
    length = passwordLength()
    upper, lower, num, chars = askUserParameters()
    pswd, lochars = addParameters(upper, lower, num, chars)
    final = generatePassword(pswd, length, lochars)
    print(final)      

    while True:
        again = input("Would like to create another password? (y,n): ")
        if again in ("y", "n"):
            break
        print("Please enter y or n")

    if again == "n":
        print("Thank you for using PassGen!")
        break
"""