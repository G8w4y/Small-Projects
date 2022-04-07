import random
import string

*numbersList, = range(0,10)
numbersList = list(map(str,numbersList))

#print(numbersList)

*alphabetList, = list(string.ascii_letters)
*symbolsList, = list(string.punctuation)
#print(numbersList)
#print(alphabetList)
#print(symbolsList)

passwordLength = int(input("How long do you need your password to be?\n"))
numbersNeeded = int(input("How many numbers do you want in your password?\n"))
symbolsNeeded = int(input("How many symbols do you want?\n"))

characktersNeeded = passwordLength - numbersNeeded - symbolsNeeded
password = []
password.append(random.choices(alphabetList,k=characktersNeeded))
[password] = password
#print(password)

passwordNumbers = []
passwordNumbers.append(random.choices(numbersList, k=numbersNeeded))
[passwordNumbers] = passwordNumbers
#print(passwordNumbers)

passwordSymbols = []
passwordSymbols.append(random.choices(symbolsList,k=symbolsNeeded))
[passwordSymbols] = passwordSymbols

#print(passwordSymbols)
for everyElement in range(0,numbersNeeded):
    password += passwordNumbers[everyElement]

for everyElement in range(0,symbolsNeeded):
    password += passwordSymbols[everyElement]
random.shuffle(password)
password = ''.join(password)

print(password)
