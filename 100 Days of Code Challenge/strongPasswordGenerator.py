import random
import string

#Create a list of integers starting at 0 and ending with 9
*numbersList, = range(0,10)
# Convert each integer into a string and put them back where they where. (At the element position that they previously had)
numbersList = list(map(str,numbersList))

#print(numbersList)
# Create a list containing every ASCII-letter from a-z followed by A-Z
*alphabetList, = list(string.ascii_letters)
# Create a list containing every ASCII-symbol available to the ASCII-language
*symbolsList, = list(string.punctuation)
#print(numbersList)
#print(alphabetList)
#print(symbolsList)
# Prompt the user for input and get total password length
passwordLength = int(input("How long do you need your password to be?\n"))
# Prompt user for number of numbers
numbersNeeded = int(input("How many numbers do you want in your password?\n"))
# Prompt user for number of symbols
symbolsNeeded = int(input("How many symbols do you want?\n"))

# Create a value containing the number of charackters the password will have
characktersNeeded = passwordLength - numbersNeeded - symbolsNeeded
# Create empty password list
password = []
# Append a random element from the whole list of alphabetList to the empty passwords list, append new elements as many times as the value of characktersNeeded variable.
password.append(random.choices(alphabetList,k=characktersNeeded))
# The list password is now a list in a list, like so [[x,y,z]]. We need to unpack the outer list layer
[password] = password
#print(password)

# Create empty passwordNumbers list
passwordNumbers = []
# Append a random element from the whole list of numbersList to the empty passwordNumbers, append new elements as many times as the value of numbersNeeded variable.
passwordNumbers.append(random.choices(numbersList, k=numbersNeeded))
# The list passwordNumbers is now a list in a list, like so [[x,y,z]]. We need to unpack the outer list layer
[passwordNumbers] = passwordNumbers
#print(passwordNumbers)

# Create empty passwordSymbols list
passwordSymbols = []
# Append a random element from the whole list of symbolsList to the empty passwordSymbols list, append new elements as many times as the value of symbolsNeeded variable.
passwordSymbols.append(random.choices(symbolsList,k=symbolsNeeded))
# The list passwordSymbols is now a list in a list, like so [[x,y,z]]. We need to unpack the outer list layer
[passwordSymbols] = passwordSymbols

#print(passwordSymbols)
# We now want to append our list of numbers to our existing list of charackters in the passwords list
# Append each element from passwordNumbers to password
for everyElement in range(0,numbersNeeded):
    password += passwordNumbers[everyElement]

# We now want to append our list of symbols to our existing list of charackters and numbers in the passwords list
# Append each element from passwordSymbols to password
for everyElement in range(0,symbolsNeeded):
    password += passwordSymbols[everyElement]
# Shuffle the password list
random.shuffle(password)
# Make the list into one long word by joining the strings in each element without stating any seperator between the ''.
password = ''.join(password)

print(password)