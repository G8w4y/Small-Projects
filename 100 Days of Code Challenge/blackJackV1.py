import random
import sys

player_hand = []
bot_hand = []
bot_hidden_hand = ["X","X","X","X","X","X","X",]
bot_shown_hand = []
deck = [11,11,11,11,2,2,2,2,3,3,3,3,4,4,4,4,5,5,5,5,6,6,6,6,7,7,7,7,8,8,8,8,9,9,9,9,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10]
#print(type(deck[0]))
#print(player_hand)
def hit(which_hand):
    "This function takes the player or the bot as the parameter and hits them with a new card from the deck. Removing that card from being drawn in the future."
    if which_hand == player_hand:
        #print(deck)
        #print(player_hand)
        player_hand.append(deck.pop(random.choice(deck)))
        #print(deck)
        #print(player_hand)
        #print(type(player_hand))
        #return player_hand

    elif which_hand == bot_hand:
        bot_hand.append(deck.pop(random.choice(deck)))
        #print(bot_hand)
        #return bot_hand

def game_start():
    hit(player_hand)
    hit(bot_hand)
    hit(player_hand)
    hit(bot_hand)

def play_again():
    another_go = input(f"Would you like to play again?\nType 'y' to go again or 'n' to exit.\n").lower()
    if another_go == "y":
        restart_game = True
        return restart_game
    elif another_go == "n":
        sys.exit()

def show_hands():
    bot_shown_hand.append(bot_hand[0])
    for card in range(1, len(bot_hand)):
        bot_shown_hand.append(bot_hidden_hand[card])
    print(f"Dealers hand consists of: {bot_shown_hand}")
    print(f"Your hand consists of: {player_hand}\nAnd a total of {sum(player_hand)} points")

def hit_or_stand():

keep_playing = True
while keep_playing:
    print("Hello and welcome to BlackJack!")
    new_game = input(f"Type 'y' if you would like to play and 'n' if you would like to exit.\n").lower()
    if new_game == "y":
        game_start()
    else: sys.exit()
    
    # Calls the show hands function that reveals the bot and the players hands.
    show_hands()









    keep_playing = play_again()
    if keep_playing == True:
        continue



