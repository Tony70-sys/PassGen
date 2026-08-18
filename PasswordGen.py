import random
import string
## Anthony Varela, 2026
## Personal project. This is my first python project.
## This password generator performs the function of providing strong passwords to users.

##We ask the user to provide the parameters for generating the password
while True: ##infinite loop until we break out of it
    length = int(input("Please introduce the length of the password (8 or more characters): ")) ##store the input in a variable
    if length > 8: ##check if the input is long enough
        break ##if so, exit the loop
    print("Password not long enough, try again") ##if it's not print this line and keep looping

print("Desired password length: " , length)

while True: 
    upper = str(input("Uppercases in it: (y/n): "))
    if upper == "y" or upper == "n": 
        break 
    print("(y/n)")

while True: 
    lower = str(input("Lowercases in it: (y/n): "))
    if lower == "y" or lower == "n": 
        break 
    print("(y/n)")

while True: 
    num = str(input("Numbers in it: (y/n): "))
    if num == "y" or num == "n": 
        break 
    print("(y/n)")    

while True: 
    chars = str(input("Special characters in it: (y/n): "))
    if chars == "y" or chars == "n": 
        break 
    print("(y/n)")

uppercaseLetters = list(string.ascii_uppercase) ##Array of all the uppercase letters 
lowercaseLetters = list(string.ascii_lowercase) ##lowercase letters
numbers = list(string.digits) ##numbers
specialCharacters = list(string.punctuation) #special characters

lochars = []

if upper == "y":
 lochars.append(uppercaseLetters)

if lower == "y":
 lochars.append(lowercaseLetters)

if num == "y":
 lochars.append(numbers)

if chars == "y":
 lochars.append(specialCharacters)
    

#Function that generates the password
def ppskGenerator():
    print("Generating password...")

ppskGenerator()

print(lochars)
