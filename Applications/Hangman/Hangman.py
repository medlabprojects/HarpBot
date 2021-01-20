"""
Python script for playing Hangman with HarpBot
"""

import sys

sys.path.append("../../Harpbot")
import HangmanLib as HL
from HarpBot import HarpBot


PAPER_WIDTH = 279.4
PAPER_HEIGHT = 215.9
PAPER_X_OFFSET = -87 # How far from the robot the left edge of the paper is placed (mm)
PAPER_Y_OFFSET = 66.1

WRONG_GUESSES_TO_LOSE = 6 # TODO - Set to however many pieces of the man are drawn


######## SET THE INPUT FILES THAT YOU WANT TO PLAY WITH HERE ########
phrase_files = ["datasets/real_robots.csv",
                "datasets/fictional_robots.csv",
                "datasets/spongebob.csv"]

# Load the category/phrase pairs
category_phrase_list = HL.load_phrases(phrase_files)


##########################################
##          STUDENT FUNCTIONS           ##
##########################################

def correct_guess(bot, letter, letter_position_list, phrase):
    # Draw letter in all of the spots listed in letter_position_list

    spaced_str = list(' '*len(phrase))
    for pos in letter_position_list:
        spaced_str[pos] = letter

    dist_to_blanks = 3.0
    HL.draw_string(bot, "".join(spaced_str), HL.BLANKS_X, HL.BLANKS_Y + dist_to_blanks, HL.BLANKS_W)

    bot.go_home()

    print("Correct guess!")
    print("Letter: " + letter)
    print("Positions: " + str(letter_position_list))


def wrong_guess(bot, letter, num_wrong_guesses):
    # Draw letter in guessing table
    padded_letter = ' '*(num_wrong_guesses - 1) + letter
    padded_letter += ' '*(6 - len(padded_letter))

    HL.draw_string(bot, padded_letter, HL.GUESS_X, HL.GUESS_Y, HL.GUESS_W)

    # Draw body part corresponding to num_wrong_guesses
    HL.draw_hangman(bot, num_wrong_guesses)

    bot.go_home()

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
    HL.draw_category(bot, category)

    # Draw the blanks for the phrase
    HL.draw_blanks(bot, phrase)

    # Draw an empty hangman
    HL.draw_gallows(bot)

    # Draw the guessing table
    HL.draw_guessing_table(bot)

    bot.go_home()

    print("Setup complete!")
    print("-" * 40)

################################ play_game ##########################
# Loop to run entire game
def play_game(bot):

    # Choose a random category/phrase pair from the list
    category, phrase = HL.random_phrase(category_phrase_list)
    setup_game(bot, category, phrase)

    # The list of letters that need to be guessed to win
    phrase_letters = HL.get_letters(phrase)

    # Loop until the game is over
    game_over = False

    # Variables
    guessed_letters = []  # The guessed letters so far
    incorrect_guesses = 0 # The number of incorrect guesses

    while not game_over:
        print("_" * 30 + "\n")
        msg, _ = HL.blankify(phrase, guessed_letters)
        print(msg + "\n") # Print the guessed word so far
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
            correct_guess(bot, letter, char_positions, phrase)

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
is_first_game = True
while True:
    bot = HarpBot()
    ### If the player has already played a game, ask if they want to play again
    if not is_first_game:
        play_again = ask_yn("Would you like to play again? ")
        if not play_again:
            break # Breaks out of the loop and ends the program
        else:
            # Prompt user to set up paper
            press_enter = input("Please set up a new sheet of paper, and press enter.")

    play_game(bot)
    bot.go_home()
    del bot
    is_first_game = False

print("Bye!")
