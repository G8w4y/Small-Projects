import random
import sys
import os
clear = lambda: os.system('cls' if os.name=='nt' else 'clear')

player_hand = []
house_hand = []
house_hidden_hand = ["X","X","X","X","X","X","X",]
house_shown_hand = []
deck = [11,11,11,11,2,2,2,2,3,3,3,3,4,4,4,4,5,5,5,5,6,6,6,6,7,7,7,7,8,8,8,8,9,9,9,9,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,1011,11,11,11,2,2,2,2,3,3,3,3,4,4,4,4,5,5,5,5,6,6,6,6,7,7,7,7,8,8,8,8,9,9,9,9,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10]
#print(type(deck[0]))
#print(player_hand)
def hit(which_hand):
    "This function takes the player or the bot as the parameter and hits them with a new card from the deck. Removing that exact card from being drawn in the future."
    if which_hand == "player_hand":
        #print(deck)
        #print(player_hand)
        player_hand.append(deck.pop(random.choice(deck)))
        #print(deck)
        #print(player_hand)
        #print(type(player_hand))
        #return player_hand

    elif which_hand == "house_hand":
        house_hand.append(deck.pop(random.choice(deck)))
        #print(bot_hand)
        #return bot_hand

def game_start():
    """Starts the game by dealing two shown cards to the player, and two cards to the house"""
    hit("player_hand")
    hit("house_hand")
    hit("player_hand")
    hit("house_hand")

def play_again():
    another_go = input(f"Would you like to play again?\nType 'y' to go again or 'n' to exit.\n").lower()
    if another_go == "y":
        restart_game = True
        clear()
        return restart_game
    elif another_go == "n":
        sys.exit()

def show_hands():
    print(f"Dealers hand consists of: {house_shown_hand}")
    print(f"Your hand consists of: {player_hand}\nAnd a total of {sum(player_hand)} points")

def show_final_hands():
    print(f"Dealers hand consists of: {house_hand}\nAnd a total of {sum(house_hand)} points")
    print(f"Your hand consists of: {player_hand}\nAnd a total of {sum(player_hand)} points")


def player_hit_or_stand(player_hand):
    # As long as the player hand is below 21, ask them to hit or stand
    while check_bust("player_hand") == False:
        # Calls the show hands function that reveals the bot and the players hands.
        show_hands()
        player_went_bust = check_bust("player_hand")
        # Ask for player action as long as the player is not bust
        if player_went_bust == True:
            break
        elif player_went_bust == False:
            hit_or_stand = input(f"type 'h' for another hit or 's' to stand.\n").lower()
            if hit_or_stand == "h":
                hit("player_hand")
                continue
            elif hit_or_stand == "s":
                break
            else:
                continue

def house_logic():
    if check_bust("house_hand") == True:
        stand = True
        return 'stand'
    if sum(house_hand) == 21 and 11 in house_hand and len(house_hand) == 2:
        natural = True
        return 'natural'
    
    elif sum(house_hand) >= 17 and sum(house_hand) < 21:
        stand = True
        return 'stand'
    
    elif sum(house_hand) < 17:
        hit("house_hand")
    
    else:
        stand = True
        return 'stand'

def check_bust(which_hand):
    if which_hand == "player_hand":
        if sum(player_hand) > 21 and 11 in player_hand:
            player_hand[player_hand.index(11)] = 1
            print(f"Your ace (11) got turned into a 1 so you wouldn't go bust.")
            player_bust = False
            return player_bust

        if sum(player_hand) > 21 and 11 not in player_hand:
            print(f"Oh, no. You wen't bust! With a total hand score of {sum(player_hand)}.\nLet's see if the house fares any better?")
            player_bust = True
            return player_bust
        else:
            player_bust = False
            return player_bust
    
    if which_hand == "house_hand":
        if sum(house_hand) > 21 and 11 in house_hand:
            house_hand[house_hand.index(11)] = 1
            house_bust = False
            return house_bust
        
        if sum(house_hand) > 21 and 11 not in house_hand:
            print(f"The House wen't bust! With a total hand score of {sum(house_hand)}.\n")
            house_bust = True
            return house_bust
        
        else:
            house_bust = False
            return house_bust

def who_won():
    player_natural = False
    house_natural = False
    if sum(player_hand) == 21 and 11 in player_hand and len(player_hand) == 2:
        player_natural = True
    
    if sum(house_hand) == 21 and 11 in house_hand and len(house_hand) == 2:
        house_natural = True

    if player_natural == True and house_natural == False:
        print(f"Player won with a BlackJack of {sum(player_hand)}.")

    if player_natural == False and house_natural == True:
        print(f"The House won with a BlackJack of {sum(player_hand)}.")

    if player_natural == True and house_natural == True:
        print(f"It's a DRAW! Both parties got a Blackjack of 21 points inlcuding an ace!")

    if sum(player_hand) <=21 and sum(player_hand) > sum(house_hand):
        print(f"You WON! With a hand consisting of {sum(player_hand)} points vs the Houses hand of {sum(house_hand)} points.")
    
    if sum(house_hand) <=21 and sum(house_hand) > sum(player_hand):
        print(f"You LOSE! With a hand consisting of {sum(player_hand)} points vs the Houses winning hand of {sum(house_hand)} points.")
    
    if check_bust('player_hand') == True and check_bust('house_hand') == True:
        print(f"It's a DRAW! Both parties went bust.")

    if check_bust('player_hand') == False and check_bust('house_hand') == True:
        print(f"The house went bust. You WON! With a hand consisting of {sum(player_hand)} points vs the Houses hand of {sum(house_hand)} points.")

    if check_bust('player_hand') == True and check_bust('house_hand') == False:
        print(f"You went bust. You LOSE! With a hand consisting of {sum(player_hand)} points vs the Houses hand of {sum(house_hand)} points.")

    if sum(house_hand) == sum(player_hand) and sum(house_hand) <= 21 and sum(player_hand) <= 21 and player_natural == False and house_natural == False:
        print(f"It's a DRAW! Both parties got {sum(player_hand)} points")



########### Main ############
keep_playing = True
while keep_playing:
    player_hand = []
    house_hand = []
    house_hidden_hand = ["X","X","X","X","X","X","X",]
    house_shown_hand = []
    deck = [11,11,11,11,2,2,2,2,3,3,3,3,4,4,4,4,5,5,5,5,6,6,6,6,7,7,7,7,8,8,8,8,9,9,9,9,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10]
    
    print("Hello and welcome to BlackJack!")
    new_game = input(f"Type 'y' if you would like to play and 'n' if you would like to exit.\n").lower()
    if new_game == "y":
        game_start()
    else: sys.exit()

    #Create the dealers hidden hand
    house_shown_hand.append(house_hand[0])
    for card in range(1, len(house_hand)):
        house_shown_hand.append(house_hidden_hand[card])
    
    #show_hands() #Kommenterte ut denne for å teste
    # In blackjack the players are served first
    player_hit_or_stand(player_hand)

    # Followed by the house (dealer), who must abide by some special rules.
    stand = ''
    natural = ''
    while stand == '' and natural == '':
        if house_logic() == 'natural':
            natural = house_logic()
        elif house_logic() == 'stand':
            stand = house_logic
        else:
            continue
    
    show_final_hands()
    who_won()












    keep_playing = play_again()
    if keep_playing == True:
        continue



