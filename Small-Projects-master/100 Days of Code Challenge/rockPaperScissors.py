import random
import time
import sys

rock = ("""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""")


paper = ("""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""")

scissors = ("""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
""")

#print(scissors)

list_choices = [rock,paper,scissors,"quit"]
computer_score = 0
player_score = 0
loose = "The computer won.\nYou loose!"
win = "You won! The computer lost."
again = "Go again!"

while int(player_score) != 3 or int(computer_score) != 3:
    if player_score == 3:
        sys.exit()
    elif computer_score == 3:
        sys.exit()
    
    player_choice = list_choices[int(input("What do you choose? Type 0 for Rock, 1 for paper, 2 for scissors or 3 to exit "))]
    
    if player_choice == "quit":
        sys.exit()
    
    computer_choice = random.choice(list_choices)
    print("3...")
    time.sleep(1)
    print("2..")
    time.sleep(1)
    print("1...")
    time.sleep(1)
    print("GO!")

    print(player_choice)
    print("\n\n   VS   \n\n")
    print(computer_choice)

    if player_choice == rock and computer_choice == scissors:
        print(win)
        player_score += 1
    elif computer_choice == rock and player_choice == scissors:
        print(loose)
        computer_score += 1
    elif player_choice == paper and computer_choice == rock:
        print(win)
        player_score += 1
    elif computer_choice == paper and player_choice == rock:
        print(loose)
        computer_score += 1
    elif player_choice == scissors and computer_choice == paper:
        print(win)
        player_score += 1
    elif computer_choice == scissors and player_choice == paper:
        print(loose)
        computer_score += 1
    
    if player_score != 3 or computer_score != 3:
        print(again)
    
    final_score = f"the final score is {player_score} points for the human vs {computer_score} points for the computer!"
    running_score = f"{player_score} points for the human, VS {computer_score} points for the computer."

    print(running_score)

else: print(final_score)