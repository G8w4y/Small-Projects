# #user_name = input("What is your name?\n")

# #print(len(user_name))

# #print(3 * (3 + 3) / 3 - 3)

# #print(round(2,6666,2)) <-- Altså rund av dette tallet til 2 plaser etter komma
# #print(8 // 3) <-- dette er en floor division, noe som runder tallet
# #ned til nærmeste hele tall

# # Hvis man ønsker å gjøre en operasjon med den tidligere verdien av seg selv
# # verdi = verdi + 1
# # verdi += 1
# # verdi -= 1
# # verdi *= et tall
# # verdi /= et tall

# # f-string er kraftige saker! Skriv f før en stringverdi når du skal printe noe
# # og python gjør alle type-conversions i print-statementen for deg ex.
# # height = 2
# # score = 14
# # print(f"Your score is {score}, your height is {height}") vil printe ut
# # Your score is 14, your height is 2

# # Python string formatting
# # "sam has {0} red balls and {1} yellow balls".format(12,13), 12 og 13 blir condition 0 og 1
# # Hvis du ønsker å være presis med floating nubers f.eks
# # syntax: {[argument_index_or_keyword]:[width][.precision][type]}
# # f.eks "Floating point {0:.2f}".format(345.7916732) Her blir condition 0 erstattet med decimalentallet
# # 345.7916732 i teksten, men ikke nok med det. vi velger å ikke spesifisere width
# # men vi velger å spesifisere presisjonen i decimalene til 2 decimaler
# # Output blir da: Floating point 345.79





# ######Even number checker############
# # 🚨 Don't change the code below 👇
# number = int(input("Which number do you want to check? "))
# # 🚨 Don't change the code above 👆

# #Write your code below this line 👇
# if number % 2 == 0:
#     print("This is an even number.")
# else: print("This is an odd number.")

# ########Leap year checker##############
# # 🚨 Don't change the code below 👇
# year = int(input("Which year do you want to check? "))
# # 🚨 Don't change the code above 👆

# #Write your code below this line 👇
# if int(year) % 4 == 0 or int(year) % 400 == 0:
#     print("Leap year.")
# else: print("Not leap year.")


# ##########Pizza order practice#########
# # 🚨 Don't change the code below 👇
# print("Welcome to Python Pizza Deliveries!")
# size = input("What size pizza do you want? S, M, or L ")
# add_pepperoni = input("Do you want pepperoni? Y or N ")
# extra_cheese = input("Do you want extra cheese? Y or N ")
# # 🚨 Don't change the code above 👆

# #Write your code below this line 👇
# size_cost = 0
# extras_cost = 0
# if extra_cheese == "y" or extra_cheese == "Y":
#     extras_cost += 1
# if size == "s" or size == "S":
#     size_cost = 15
#     if add_pepperoni == "y" or add_pepperoni == "Y":
#         extras_cost += 2
# elif size == "m" or size == "M":
#     size_cost = 20
#     if add_pepperoni == "y" or add_pepperoni == "Y":
#         extras_cost += 3
# elif size == "l" or size == "L":
#     size_cost = 25
#     if add_pepperoni == "y" or add_pepperoni == "Y":
#         extras_cost += 3

# print("Your final bill is: $" + str(int(size_cost + extras_cost)) + ".")

# ############## Appending Love Calculator ##########
# # 🚨 Don't change the code below 👇
# print("Welcome to the Love Calculator!")
# name1 = input("What is your name? \n")
# name2 = input("What is their name? \n")
# # 🚨 Don't change the code above 👆

# #Write your code below this line 👇
# name1 = name1.lower()
# name2 = name2.lower()
# count1 = 0
# count2 = 0
# count1 += name1.count("t") + name1.count("r") + name1.count("u") + name1.count("e") + name2.count("t") + name2.count("r") + name2.count("u") + name2.count("e")
# count2 += name1.count("l") + name1.count("o") + name1.count("v") + name1.count("e") + name2.count("l") + name2.count("o") + name2.count("v") + name2.count("e")
# #print(str(count1)+str(count2))
# if int(str(count1)+str(count2)) < 10 or int(str(count1)+str(count2)) > 90:
#     print("Your score is " + str(count1)+str(count2) + ", you go together like coke and mentos.")
# elif 40 < int(str(count1)+str(count2)) < 50:
#     print("Your score is " + str(count1)+str(count2) + ", you are alright together.")
# else: print("Your score is " + str(count1)+str(count2) + ".")

# Må ha med biblioteket for random shit
# import random

# random_integer = random.randint(0,5)

# random_float = random.random()
# print(random_integer)
# print(random_float)

# import random

# random_number = random.randint(0,1)
# if random_number > 0.5:
#     print("Heads")
# else: print("Tails")

####### Random Norwegian county generator ########
# import random
# norske_fylker = ["Agder", "Vestfold & Telemark", "Oslo", "innlandet", "Møre & Romsdal", "Vestland", "Viken", "Rogaland", "Nordland", "Trøndelag", "Troms & Finnmark"]
# print(norske_fylker[random.randint(0, (len(norske_fylker) - 1))])

# List data structure: https://docs.python.org/3/tutorial/datastructures.html

# ###### Meal buy roulette ######
# import random
# # Split string method, splits string based on criteria of comma followed by a space
# names_string = input("Give me everybody's names, separated by a comma. ")
# names = names_string.split(", ")
# # 🚨 Don't change the code above 👆

# #Write your code below this line 👇
# print(f"{names[random.randint(0, (len(names) - 1))]} is going to buy the meal today!")
# # Kan også bruke random.choice(names), dette er en funksjon som vil velge et tilfeldig element i listen names

########## Nested lists ###################
# fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
# vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]
 
# dirty_dozen = [fruits, vegetables]

#print(dirty_dozen)
# print(dirty_dozen[0])
# print(dirty_dozen[0])
# Altså, fra liste ved element 1, print element 2 fra den listen. Eller fra den andre listen i vår liste av lister, print tredje element fra denne listen.
#print(dirty_dozen[1][2])

# ######### For loop test ###########
# list_of_items = ["Suitcase", "Duffelbag", "Messenger bag"]
# for item in list_of_items:
#     #do something to each item
#     print(item)

# ######### Average height calc ##############
# # 🚨 Don't change the code below 👇
# student_heights = input("Input a list of student heights ").split()
# for n in range(0, len(student_heights)):
#   student_heights[n] = int(student_heights[n])
# # 🚨 Don't change the code above 👆

# #Write your code below this row 👇
# sum_heights = 0
# for e in range(0,len(student_heights)):
#     sum_heights +=  student_heights[e]
# rounded_average_height = round(sum_heights / len(student_heights))
# print(rounded_average_height)

##### Return highest value from list of values ####
# # 🚨 Don't change the code below 👇
# student_scores = input("Input a list of student scores ").split()
# for n in range(0, len(student_scores)):
#   student_scores[n] = int(student_scores[n])
# print(student_scores)
# # 🚨 Don't change the code above 👆

# #Write your code below this row 👇
# student_scores_descending = sorted(student_scores, reverse = True)
# highest_score = student_scores_descending[0]
# #print(student_scores_descending)
# print(f"The highest score in the class is: {highest_score}")

## eventuelt gjør denne det samme som koden over ##
# highest_score = 0
## For every score in the list student_scores
# for score in student_scores:
#     if score > highest_score:
#     highest_score = score

######## create list within range and sum all even numbers ####
#Write your code below this row 👇
# * before variable and , after unpacks the contents of the list when we call it later
# *list100, = range(1,101,1)
# sum_even = 0
# #print(list100)
# for e in range(0,len(list100)):
#     if list100[e] % 2 == 0:
#         sum_even += list100[e]

# print(sum_even)

## eventuelt
# total_evens = 0
# for number in range(1, 101):
#     if number % 2 == 0:
#         total_evens += number

# print(total_evens)

###### FizzBuzz solution generator ####
#Write your code below this row 👇
# Create list from 1 to 100 and unpack it when called
#*list100, = range(1,101,1)

#For every element in list print Fizz if divisable by 3, Buzz by 5, FizzBuzz by both, else print the list value at the element
# for e in range(0, len(list100)):
#     if list100[e] % 3 == 0 and list100[e] % 5 == 0:
#         print("FizzBuzz")
#     elif list100[e] % 3 == 0:
#         print("Fizz")
#     elif list100[e] % 5 == 0:
#         print("Buzz")
#     else: print(list100[e])

