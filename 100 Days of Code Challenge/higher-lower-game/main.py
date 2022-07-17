from art import logo
from art import vs
from game_data import data
import random
import os

clear = lambda: os.system('cls' if os.name=='nt' else 'clear')

HIGHER_LOWER_LIST = ['none','none']

def pick_random_data_entry_from_list():
    #print(data[random.randint(0,len(data) - 1)])
    random_entry = data[random.randint(0,len(data) - 1)]
    return random_entry

def pick_different_starter_entries():
    HIGHER_LOWER_LIST[0] = pick_random_data_entry_from_list()
    HIGHER_LOWER_LIST[1] = pick_random_data_entry_from_list()
    while HIGHER_LOWER_LIST[0] == HIGHER_LOWER_LIST[1]:
        HIGHER_LOWER_LIST[1] = pick_random_data_entry_from_list()

#Create a function that picks a data_point from the game_data list and displays its key:values in a good manner
def display_values():
    entry_a = HIGHER_LOWER_LIST[0]
    print(f"Name: {entry_a['name']}\nDescription: {entry_a['description']} from {entry_a['country']}.\nFollower count: {entry_a['follower_count']} million.")

    print(vs)
    entry_b = HIGHER_LOWER_LIST[1]
    print(f"Name: {entry_b['name']}\nDescription: {entry_b['description']} from {entry_b['country']}.\nFollower count: ???\nDoes {entry_b['name']} have a higher(1) or Lower(2) follower count than {entry_a['name']}?")
    #print(type(entry_a))


#Create a function that takes a player guessed input and compares the guess with the follower count of the two data_points
def guess_and_check():
    #Check to see if the guessed number is actually a whole number, and nothing else
    while True:
        try:
            player_guess = int(input("Type '1' for Higher and '2' for lower: "))
            break
        except ValueError or player_guess != 1 or player_guess != 2:
            print("Oops! You typed in something other than a '1' or a '2'.")
            continue
    
    if HIGHER_LOWER_LIST[0]['follower_count'] == HIGHER_LOWER_LIST[1]['follower_count']:
        number_to_guess = 0
        player_guess = 0
    elif HIGHER_LOWER_LIST[0]['follower_count'] > HIGHER_LOWER_LIST[1]['follower_count']:
        number_to_guess = 2
    elif HIGHER_LOWER_LIST[0]['follower_count'] < HIGHER_LOWER_LIST[1]['follower_count']:
        number_to_guess = 1
    
    if player_guess == number_to_guess:
        return True
    else:
        return False

    
    



#Create a function that swaps data_point A with data_point B and chooses a new and unique random entry for B
def swap_and_new_entry():
    HIGHER_LOWER_LIST[0] = HIGHER_LOWER_LIST[1]
    HIGHER_LOWER_LIST[1] = pick_random_data_entry_from_list()
    while HIGHER_LOWER_LIST[0] == HIGHER_LOWER_LIST[1]:
        HIGHER_LOWER_LIST[1] = pick_random_data_entry_from_list()

#Create a loop that continues to ask for guesses for as long as the player guesses correctly
def the_game():
    clear()
    #Create a welcome statement
    print(logo)
    print("Welcome to the Higher/Lower game!")
    score_counter = 0
    pick_different_starter_entries()

    still_alive = True
    while still_alive:
        clear()
        print(logo)
        display_values()
        print(f"Score so far: {score_counter}")
        if guess_and_check() == True:
            swap_and_new_entry()
            score_counter += 1
            continue
        else:
            print(f"That's too bad. You got the wront guess! {HIGHER_LOWER_LIST[0]['name']} has {HIGHER_LOWER_LIST[0]['follower_count']} million followers,\nwhile {HIGHER_LOWER_LIST[1]['name']} has {HIGHER_LOWER_LIST[1]['follower_count']} million followers.\nFinal score is: {LIFE_COUNTER}")
            still_alive = False
    
        play_again = input("Would you like to play again? ").lower()
        if "y" in play_again:
            pick_different_starter_entries()
            the_game()
        else: 
            break



#Create a score counter that counts for as long as the player guesses correctly

# for item in range(len(HIGHER_LOWER_LIST)):
#     print(HIGHER_LOWER_LIST[item])

#swap_and_new_entry()

# for item in range(len(HIGHER_LOWER_LIST)):
#     print(HIGHER_LOWER_LIST[item])

#entry_a = HIGHER_LOWER_LIST[0].get('name')
#print(entry_a)
#display_values()
clear()
#Create a welcome statement
print(logo)
print("Welcome to the Higher/Lower game!")
ready_to_play = input("The game where you guess who has more or less followers on Instagram than the other! Type 'yes' if you wan't to play and 'no' to exit: ").lower()
if "y" in ready_to_play:
    the_game()
