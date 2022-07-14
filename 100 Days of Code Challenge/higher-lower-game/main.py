#Import the other files and modules
from art import logo
from game_data import data
import random
import os
clear = lambda: os.system('cls' if os.name=='nt' else 'clear')

HIGHER_LOWER_LIST = []

#Create a welcome statement
print(logo)
print("Welcome to the Higher/Lower game!")

#Create a function that picks a data_point from the game_data list and displays its key:values in a good manner
def pick_random_data_entry_from_list():
    #print(data[random.randint(0,len(data) - 1)])
    random_entry = data[random.randint(0,len(data) - 1)]
    return random_entry

def pick_different_starter_entries():
    HIGHER_LOWER_LIST.append(pick_random_data_entry_from_list())
    HIGHER_LOWER_LIST.append(pick_random_data_entry_from_list())
    while HIGHER_LOWER_LIST[0] == HIGHER_LOWER_LIST[1]:
        HIGHER_LOWER_LIST[1] = pick_random_data_entry_from_list()



#Create a function that takes a player guessed input and compares the guess with the follower count of the two data_points

#Create a function that swaps data_point A with data_point B and chooses a new and unique random entry for B
def swap_and_new_entry():
    HIGHER_LOWER_LIST[0] = HIGHER_LOWER_LIST[1]
    HIGHER_LOWER_LIST[1] = pick_random_data_entry_from_list()
    while HIGHER_LOWER_LIST[0] == HIGHER_LOWER_LIST[1]:
        HIGHER_LOWER_LIST[1] = pick_random_data_entry_from_list()

#Create a loop that continues to ask for guesses for as long as the player guesses correctly

#Create a score counter that counts for as long as the player guesses correctly
pick_different_starter_entries()
for item in range(len(HIGHER_LOWER_LIST)):
    print(HIGHER_LOWER_LIST[item])

swap_and_new_entry()

for item in range(len(HIGHER_LOWER_LIST)):
    print(HIGHER_LOWER_LIST[item])

entry_a = HIGHER_LOWER_LIST[0].get('name')
print(entry_a)