import random
import string

## This module contains the core functionality for PassGen.
## It defines the available character sets and provides functions
## to create secure random passwords based on the user's selected
## character types and desired password length.

uppercaseLetters = list(string.ascii_uppercase) ##array of uppercases letters
lowercaseLetters = list(string.ascii_lowercase) ##array of lowercase letters
numbers = list(string.digits) ##array of numbers
specialCharacters = list(string.punctuation) ##array of special characters

## Function that creates an array of possible list of characters for the password and the initial password
## to meet basic requirements. It uses the checkbuttons to trigger actions.
def addParameters(upper, lower, num, chars):
    lochars = []
    pswd = []

    if upper:
        lochars.append(uppercaseLetters)
        pswd.append(random.choice(uppercaseLetters))

    if lower:
        lochars.append(lowercaseLetters)
        pswd.append(random.choice(lowercaseLetters))

    if num:
        lochars.append(numbers)
        pswd.append(random.choice(numbers))

    if chars:
        lochars.append(specialCharacters)
        pswd.append(random.choice(specialCharacters))

    return pswd, lochars

## Funtion that finishes the password creation.
def generatePassword(pswd, length, lochars):

    currentLength = len(pswd) 

    for i in range(length - currentLength):
        ch = random.choice(random.choice(lochars))
        pswd.append(ch)

    random.shuffle(pswd)
    final = "".join(pswd)
    return final