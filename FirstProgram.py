import random
#Anthony Varela, 2026
"""
print("hello world");

list = [1,2,3,4,5];

for i in list:
    print(i);

    sum = 0
for i in range(1,6,1):
    print(i)
    sum += i
print("sum is: ", sum)

limit = 6
start = 1
sh = 0
while start < limit:
    print(start)
    sh += start
    start += 1

print("sh is: ", sh)

liss = []

for i in range(1,6):
    print(i)
    liss.append(i)
print(liss)

nums = range(1,6) would work too
range(start inclusive, end exclusive, increment value)

for i in range(5): swap range with nums
    print("number " + str( i + 1), end=' ');

init = 0

while init < length:
    print(init, end=' ') used to print a series of things on the same line
    init += 1

"""

##We ask the user to provide the parameters for generating the password
while True: ##infinite loop until we break out of it
    length = int(input("Please introduce the length of the password (8 or more characters): ")) ##store the input in a variable
    if length > 8: ##check if the input is long enough
        break ##if so, exit the loop
    print("Password not long enough, try again") ##if it's not print this line and keep looping

print("Desired password length: " , length)

while True: 
    bol1 = str(input("Uppercases in it: (y/n): "))
    if bol1 == "y" or bol1 == "n": 
        break 
    print("(y/n)")

while True: 
    bol2 = str(input("Lowercases in it: (y/n): "))
    if bol2 == "y" or bol2 == "n": 
        break 
    print("(y/n)")

while True: 
    bol3 = str(input("Numbers in it: (y/n): "))
    if bol3 == "y" or bol3 == "n": 
        break 
    print("(y/n)")    

while True: 
    bol4 = str(input("Special characters in it: (y/n): "))
    if bol4 == "y" or bol4 == "n": 
        break 
    print("(y/n)")

#Function that generates the password
def ppskGenerator():
    print("Generating password...")

ppskGenerator()
