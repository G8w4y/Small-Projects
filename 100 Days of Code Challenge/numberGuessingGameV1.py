import random
import sys
import os
clear = lambda: os.system('cls' if os.name=='nt' else 'clear')
keep_playing = True

# TO DO number 1:
# Create a randomly generated number between 1 and 100 for the player to guess.

# TO DO number 2:
# Create a while loop that runs for as long as the player wants to continue playing

# TO DO number 3:
# Create a lifecounter that counts the number of guesses that are remaining

# TO DO number 4:
# Create a way for the player to guess the number, each failed attempt removes a counter from the lifecounter

# TO DO number 5: 
# Create a hard and easy dificulty with 5 or 10 lives on the lifecounter
def choose_difficulty(difficulty_chosen = input("What difficulty would you like to play at? Type 'easy', 'medium' or 'hard'?").lower()):
    if difficulty_chosen == "easy":
        return 10
    elif difficulty_chosen == "medium":
        return 7
    else: return 5

def the_game():

    while keep_playing:
        print("Hello and welcome to the number guesssing game!")
        life_counter = choose_difficulty()
        print(life_counter)

        continue_playing = input("Would you like to play again?").lower()
        if continue_playing == "yes":
            the_game()
        else: keep_playing = False

the_game()