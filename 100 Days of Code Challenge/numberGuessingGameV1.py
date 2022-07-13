import random
import sys
import os
clear = lambda: os.system('cls' if os.name=='nt' else 'clear')
number_to_guess = int

# TO DO number 1:
# Create a randomly generated number between 1 and 100 for the player to guess.
def random_number():
    number = random.randint(1,100)
    return number

# TO DO number 2:
# Create a while loop that runs for as long as the player wants to continue playing
# Done

# TO DO number 3:
# Create a lifecounter that counts the number of guesses that are remaining
# Done

# TO DO number 4:
# Create a way for the player to guess the number, each failed attempt removes a counter from the lifecounter
# Done

# TO DO number 5: 
# Create a hard and easy dificulty with 5 or 10 lives on the lifecounter
# Done

#To Do number 6:
# Create a function that checks what number has been guessed, and tells the user if that number is too high or too low.
def number_high_or_low(a,b):
    """This function compares the guessed number with the number to guess. Returning 1 if they are not similar, and 0 if they are similar. As well as if the number guessed is too high or too low."""
    number_to_check = int(a)
    number_to_guess = int(b)
    if number_to_check > number_to_guess:
        print("Too high!")
        return 1
    elif number_to_check < number_to_guess:
        print("Too low!")
        return 1
    else:
        print(f"You guessed it! The secret number was {number_to_guess}")
        return 0



def choose_difficulty(difficulty_chosen):
    if difficulty_chosen == "easy":
        return 10
    elif difficulty_chosen == "medium":
        return 7
    elif difficulty_chosen == "hard":
        return 5
    else:
        print("\n**INPUT ERROR** Enabling Insane difficulty!\n")
        return 1

def the_game():
    keep_playing = True
    
    
    while keep_playing:
        clear()
        print("Hello and welcome to the number guesssing game!\nI'm thinking of a number between 1 and 100.")
        number_to_guess = random_number()
        #print(f"Psst. The secret number is {number_to_guess}")
        life_counter = choose_difficulty(difficulty_chosen = input("What difficulty would you like to play at?\nType 'easy', 'medium' or 'hard':\n").lower())
        print(f"You have {life_counter} lives remaining")
        guessed_number = 0


        while guessed_number != number_to_guess:
            
            if life_counter == 0:
                print(f"You loose! \nThe number to guess was {number_to_guess}.")
                break

            guessed_number = int(input(f"Guess a number! "))
            if guessed_number != number_to_guess:
                life_counter -= number_high_or_low(guessed_number,number_to_guess)
                print(f"You have {life_counter} lives remaining!")
                continue
            elif guessed_number == number_to_guess:
                print(f"Congratualtions! You guess it! With {life_counter} lives remaining!\nThe number to guess was {number_to_guess}.")

        continue_playing = input("Would you like to play again?").lower()
        if "y" in continue_playing:
            continue
        else: keep_playing = False

the_game()