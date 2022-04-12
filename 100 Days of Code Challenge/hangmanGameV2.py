import random
import sys

HANGMANPICS = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''', '''
         +---+
         |   |
             |
YAY!         |
\O/          |
 |           |
/ \    =========''']
# Liste med dyreord tatt fra github
words = ('ant baboon badger bat bear beaver camel cat clam cobra cougar coyote crow deer dog donkey duck eagle ferret fox frog goat goose hawk lion lizard llama mole monkey moose mouse mule newt otter owl panda parrot pigeon python rabbit ram rat raven rhino salmon seal shark sheep skunk sloth snake spider stork swan tiger toad trout turkey turtle weasel whale wolf wombat zebra ').split()

# List med egendefinerte ord
myWords = ["prophet", "godzilla", "jump", "batman", "joker", "kraken", "medusa", "dinosaur", "prague", "paris", "london", "singapore", "rome", "norway", "Australia", "fart", "art", "cart", "shit", "car", "bar", "pepsi", "pizza", "baby", "flash"]

# Liste over ord som det er mulig å få i Hangmanspillet
wordsList = words + myWords

# Shuffler rundt på elementene i listen slik at det blir mer tilfeldig
random.shuffle(wordsList)

# Velger ut et tilfeldig ord
*goal_word, = random.choice(wordsList).upper()

#print(type(goal_word))
#print(goal_word)

hidden_word = []
#print(hidden_word)
for everyChar in range(0,len(goal_word)):
    hidden_word.append("_")

# for testing
#print(hidden_word)
#print(goal_word)

# Print Welcome statement
print(''' 
 __          __  _                            _          _    _                                         _ 
 \ \        / / | |                          | |        | |  | |                                       | |
  \ \  /\  / /__| | ___ ___  _ __ ___   ___  | |_ ___   | |__| | __ _ _ __   __ _ _ __ ___   __ _ _ __ | |
   \ \/  \/ / _ \ |/ __/ _ \| '_ ` _ \ / _ \ | __/ _ \  |  __  |/ _` | '_ \ / _` | '_ ` _ \ / _` | '_ \| |
    \  /\  /  __/ | (_| (_) | | | | | |  __/ | || (_) | | |  | | (_| | | | | (_| | | | | | | (_| | | | |_|
     \/  \/ \___|_|\___\___/|_| |_| |_|\___|  \__\___/  |_|  |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_(_)
                                                                             __/ |                        
                                                                            |___/                        

''')

print(HANGMANPICS[0])
print(f"{' '.join(hidden_word)} <-- The word to guess has {len(hidden_word)} letters\n")

*guessed_letters, = []
life_count = 6
while life_count > 0:
    guessed_right = len(goal_word)
    player_choice = input("Please guess a charackter: ").upper()
    guessed_letters.append(player_choice)

    for everyChar in range(0,len(goal_word)):
        if goal_word[everyChar] != player_choice:
            guessed_right -= 1
        elif goal_word[everyChar] == player_choice:
            hidden_word[everyChar] = player_choice
            guessed_right += 1
    if guessed_right == 0:
        life_count -= 1



    if life_count == 6:
        print(HANGMANPICS[0])
    elif life_count == 5:
        print(HANGMANPICS[1])
    elif life_count == 4:
        print(HANGMANPICS[2])
    elif life_count == 3:
        print(HANGMANPICS[3])
    elif life_count == 2:
        print(HANGMANPICS[4])
    elif life_count == 1:
        print(HANGMANPICS[5])
    elif life_count == 0:
        print(HANGMANPICS[6])

    print(f"{' '.join(hidden_word)} <-- The word to guess has {len(hidden_word)} letters\n")
    #print("Your Guesses so far:")
    print(f"{' '.join(guessed_letters)} <-- Your guesses so far \n")
    print(f"You have {life_count} lives left!\n")
    print("***************************************************************************")

    if ''.join(goal_word) == ''.join(hidden_word):
        print(f"The word was: {''.join(goal_word)}!")
        print("YOU WIN!")
        print(HANGMANPICS[7])
        sys.exit()
    if life_count == 0:
        print("YOU LOSE!")
        print(f"The word was: {''.join(goal_word)}")
        sys.exit()
