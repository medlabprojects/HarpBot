"""
Python script for playing Hangman with HarpBot
"""

import sys
sys.path.append("../../Harpbot")
import HangmanLib as HL
from HarpBot import HarpBot


WRONG_GUESSES_TO_LOSE = 5 # TODO - Set to however many pieces of the man are drawn


######## SET THE INPUT FILES THAT YOU WANT TO PLAY WITH HERE ########
phrase_files = ["datasets/real_robots.csv",
                "datasets/fictional_robots.csv",
                "datasets/spongebob.csv"]

# Load the category/phrase pairs
category_phrase_list = HL.LoadPhrases(phrase_files)


##########################################
##          STUDENT FUNCTIONS           ##
##########################################

def draw_category(bot, category):
    ## Student code here! ##
    print("Drawing category: " + category)

def draw_blanks(bot, phrase):
    ## Student code here! ##
    print("Drawing blanks!")

def draw_empty_hangman(bot):
    ## Student code here! ##
    print("Drawing hangman!")

def draw_guessing_table(bot):
    ## Student code here! ##
    print("Drawing guessing table!")

def correct_guess(bot, letter, letter_position_list):
    ## Student code here! ##
    print("Correct guess!")
    print("Letter: " + letter)
    print("Positions: " + str(letter_position_list))

def wrong_guess(bot, letter, num_wrong_guesses):
    ## Student code here! ##
    print("Wrong guess: " + letter)
    print("Wrong guesses so far: " + str(num_wrong_guesses))

def win_game(bot):
    ## Student code here! ##
    print("The player has won!")

def lose_game(bot):
    ## Student code here! ##
    print("The player has lost.")

##########################################
##           PROVIDED FUNCTIONS         ##
##########################################

########################## guess_letter ############################
def guess_letter():
    letter = input("Please guess a letter: ")
    return letter

################################ new_game ###########################
# Sets up a new game
def setup_game(bot, category, phrase):

    # Write what the category is
    draw_category(bot, category)

    # Draw the blanks for the phrase
    draw_blanks(bot, phrase)

    # Draw an empty hangman
    draw_empty_hangman(bot)

    # Draw the guessing table
    draw_guessing_table(bot)

    print("Setup complete!")
    print("-" * 40)

################################ play_game ##########################
# Loop to run entire game
def play_game(bot):

    # Choose a random category/phrase pair from the list
    category, phrase = HL.RandomPhrase(category_phrase_list)
    setup_game(bot, category, phrase)

    # The list of letters that need to be guessed to win
    phrase_letters = HL.GetLetters(phrase)

    # Loop until the game is over
    game_over = False

    # Variables
    guessed_letters = []  # The guessed letters so far
    incorrect_guesses = 0 # The number of incorrect guesses

    while not game_over:
        print("_" * 30 + "\n")
        print(HL.Blankify(phrase, guessed_letters) + "\n") # Print the guessed word so far
        print("Category: " + category) # Print what the category is
        print("Guessed letters: " + str(guessed_letters)) # Print the guessed letters so far
        print("Wrong guesses: " + str(incorrect_guesses)) # Print the number of incorrect guesses so far


        ############## Guess a letter ##################
        letter = guess_letter().lower() # Ask the player to guess a letter. Make sure it's lowercase

        ############### Error Checking ################
        if letter in guessed_letters:
            print("You've already guessed that letter!")
            continue # Proceed to next loop iteration
        if len(letter) != 1:
            print("Please type a single character from the alphabet")
            continue # Proceed to next loop iteration
        guessed_letters.append(letter) # Add guess to the list


        ############# Determine if guess is right or wrong #############
        if not letter in phrase_letters:
            # Wrong guess
            incorrect_guesses = incorrect_guesses + 1
            wrong_guess(bot, letter, incorrect_guesses) # Process the incorrect guess
        else:
            # Correct guess!
            # Get the positions where the letter is in the phrase
            char_positions = [pos for pos, char in enumerate(phrase) if char == letter]
            correct_guess(bot, letter, char_positions)

        ################ Determine if the game is over #################
        # Check if the player has won or lost
        is_winner = all(char in guessed_letters for char in phrase_letters)
        is_loser = incorrect_guesses >= WRONG_GUESSES_TO_LOSE
        if is_winner:
            win_game(bot)
            game_over = True
        elif is_loser:
            lose_game(bot)
            game_over = True

    print("The phrase was: " + phrase)
    print("Good game!")

################################# ask_yn #################################
# It asks a yes/no question, and the user must type either "Y" or "yes"
# for 'yes', and "N" or "no" for no. If the user types anything different,
# then the program tells the user to try again.

# The input of the ask_yn function is a String, the question that
# you want to ask.

# The output of ask_yn is the Boolean True if the user said "Yes".
# The output of ask_yn is the Boolean False if the user said "No".
def ask_yn(question):
    while True:
        print(question)
        answer = input("Please choose Yes (y) or No (n)): ")

        # The strip() function just removes any extra spaces from the
        # front or end of the string.
        answer = answer.strip()

        if answer.lower() == "yes" or answer.lower() == "y":
            return True # The user said 'yes'
        elif answer.lower() == "no" or answer.lower() == "n":
            return False # The user said 'no'
        else:
            # Invalid response. Don't return anything so we
            # go through the while loop again
            print("Unknown response: " + answer)



### MAIN LOOP ###
bot = HarpBot()
is_first_game = True
while True:
    ### If the player has already played a game, ask if they want to play again
    if not is_first_game:
        play_again = ask_yn("Would you like to play again? ")
        if not play_again:
            break # Breaks out of the loop and ends the program
        else:
            # Prompt user to set up paper
            press_enter = input("Please set up a new sheet of paper, and press enter.")
    bot.pen_up()
    bot.goto_point(305, 0)
    play_game(bot)
    is_first_game = False

print("Bye!")
