import random
import sys

def hangmanGame():
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





    # Liste med dyreord tatt fra github
    animals = ('ant baboon badger bat bear beaver camel cat clam cobra cougar coyote crow deer dog donkey duck dinosaur eagle ferret fox frog goat goose hawk lion lizard llama mole monkey moose mouse mule newt otter owl panda parrot pigeon python rabbit ram rat raven rhino salmon seal shark sheep skunk sloth snake spider stork swan tiger toad trout turkey turtle weasel whale wolf wombat zebra ').split()

    # List med egendefinerte ord
    places = ["prague", "paris", "london", "singapore", "rome", "norway", "australia", "bar", "oslo", "pub", "svalbard"]

    superheroes = ["batman", "prophet", "flash", "superman", "spiderman", "wonderwoman", "daredevil"]

    villains = [ "joker", "sandman", "kingpin"]

    monsters = ["godzilla", "kraken", "medusa", "Troll", "hydra"]

    verbs = ["jump", "fart", "shit", "puke"]

    things = ["art", "cart", "car", "table", "shoe"]

    edibles = ["pepsi", "pizza", "water", "manchego", "bree"]

    categories_list = [animals, places, superheroes, villains, monsters, verbs, things, edibles, random.randint(0,7)]
    categories_list_name = ["animals", "places", "superheroes", "villains", "monsters", "verbs", "things", "edibles", "random"]
    # Lager en kategorimaskin hvor vi trekker ut et tilfeldig valg fra liste spesifisert av brukeren
    # Brukeren fanges i en loop frem til brukeren oppgir et eneste tall
    correct_category_input = False
    while correct_category_input == False:
        player_category_choice = (input(f"Please pick a category by specifying a number:\n0 animals\n1 places\n2 superheroes\n3 villains\n4 monsters\n5 verbs\n6 things\n7 edibles\n8 random\n"))
        # Check if player has input a single charackter
        if len(player_category_choice) == 1:
            # Try checking if player input is a valid integer string format, if its not and raises a ValueError, return player to start of loop. If valid, transform player input string into an integer value
            
            try:
                player_category_choice = int(player_category_choice)
                # if this is true, return player to start of while loop
                if player_category_choice == 9:
                    continue
            # ValueError raised? return player to start of while loop
            except ValueError:
                continue
            # No exceptions? Run this code
            else: 
                player_category_choice == int
                correct_category_input = True

    # Set category choice = player category choice
    category_choice = categories_list[player_category_choice]
    # Set the category to be printed = player category choice
    category_printed = categories_list_name[player_category_choice]

    # Choose the list corresponding to the players choice
    if category_choice == animals:
        wordsList = animals
    elif category_choice == places:
        wordsList = places
    elif category_choice == superheroes:
        wordsList = superheroes
    elif category_choice == villains:
        wordsList = villains
    elif category_choice == monsters:
        wordsList = monsters
    elif category_choice == verbs:
        wordsList = verbs
    elif category_choice == things:
        wordsList = things
    elif category_choice == edibles:
        wordsList = edibles
    elif category_choice == categories_list[8]:
        wordsList = categories_list[random.randint(0,7)]
    
    # Print the category chosen by user for them to see
    print(f"You have chosen {category_printed} as your category!")

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


    print(f"{' '.join(hidden_word)} <-- The word to guess has {len(hidden_word)} letters\n")



























    *guessed_letters, = []
    life_count = 6
    while life_count > 0:
        guessed_right = len(goal_word)
        correct_input = False
        while correct_input == False:
            player_guess = input("Please guess single a charackter: ").upper()
            if len(player_guess) == 1:
                try:
                    if int(player_guess) in range(0,9):
                        continue
                except ValueError:
                    correct_input = True
                

        guessed_letters.append(player_guess)

        for everyChar in range(0,len(goal_word)):
            if goal_word[everyChar] != player_guess:
                guessed_right -= 1
            elif goal_word[everyChar] == player_guess:
                hidden_word[everyChar] = player_guess
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

        print(f"The category is: {category_printed}")
        print(f"{' '.join(hidden_word)} <-- The word to guess has {len(hidden_word)} letters\n")
        #print("Your Guesses so far:")
        print(f"{' '.join(guessed_letters)} <-- Your guesses so far \n")
        print(f"You have {life_count} lives left!\n")
        print("***************************************************************************")

        if ''.join(goal_word) == ''.join(hidden_word):
            print(f"The word was: {''.join(goal_word)}!")
            print("YOU WIN!")
            print(HANGMANPICS[7])
            break

        if life_count == 0:
            print("YOU LOSE!")
            print(f"The word was: {''.join(goal_word)}")
            break
           # play_again = input("Do you want to play again? Press y for Yes and n for No\n")
           # if play_again.lower() == "y":
           #     life_count = 6
           # else: sys.exit()

playOnBool = True
while (playOnBool):
    
    hangmanGame()
    play_again = input("Do you want to play again? Press y for Yes and n for No\n")
    if play_again.lower() == "y" or play_again.lower() == "ye" or play_again.lower() == "yes":
        playOnBool = True
    else: sys.exit()

