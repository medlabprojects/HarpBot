"""
Python script for playing Hangman with HarpBot
"""

import sys
sys.path.append("../../Harpbot")
import HangmanLib as HL
from HarpBot import HarpBot
from numpy import genfromtxt

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
category_phrase_list = HL.LoadPhrases(phrase_files)


##########################################
##          STUDENT FUNCTIONS           ##
##########################################

def draw_category(bot, category):
    ## Student code here! ##
    print("Drawing category: " + category)
    c_x = -150.0;
    c_y = 200.0;
    c_w = 130.0;
    c_h = 40.0;

    # Draws rectangle
    bot.pen_up()
    bot.goto_point(c_x + 0.0, c_y + 0.0)
    bot.pen_down()
    bot.goto_point(c_x + 1.0*c_w, c_y + 0.0)
    bot.goto_point(c_x + 1.0*c_w, c_y + 1.0*c_h)
    bot.goto_point(c_x + 0.0, c_y + 1.0*c_h)
    bot.goto_point(c_x + 0.0, c_y + 0.0)
    bot.pen_up()

    # Draws cloud -- currently shades the cloud - coords are not adjacent
    # cloud_coords = genfromtxt('image_outlines/cloud_coords.csv', delimiter=',')
    # bot.pen_up()
    # for ii in range(len(cloud_coords)):
    #     bot.goto_point(c_x + cloud_coords[ii,0]*c_w, c_y + cloud_coords[ii,1]*c_h)
    #     if ii == 0:
    #         bot.pen_down()
    #     if ii == len(cloud_coords):
    #         bot.pen_up()


    # TODO: draw the word "category" on top of box
    # TODO: draw category in box using DrawString()

def draw_blanks(bot, phrase):
    ## Student code here! ##
    print("Drawing blanks!")



def draw_gallows(bot):
    ## Student code here! ##

    print("Drawing hangman!")

    g_x = 25.0
    g_y = 25.0
    g_h = 240.0
    g_w = 150.0

    bot.pen_up()
    bot.goto_point(g_x + 0.0*g_w, g_y + 0.0*g_h)    # 1
    bot.pen_down()
    bot.goto_point(g_x + 0.3*g_w, g_y + 0.2*g_h)    # 2
    bot.goto_point(g_x + 0.3*g_w, g_y + 1.0*g_h)    # 3
    bot.goto_point(g_x + 0.8*g_w, g_y + 1.0*g_h)    # 4
    bot.goto_point(g_x + 0.8*g_w, g_y + 0.9*g_h)    # 5
    bot.goto_point(g_x + 0.4*g_w, g_y + 0.9*g_h)    # 6
    bot.goto_point(g_x + 0.4*g_w, g_y + 0.2*g_h)    # 7
    bot.goto_point(g_x + 0.7*g_w, g_y + 0.0*g_h)    # 8
    bot.goto_point(g_x + 0.6*g_w, g_y + 0.0*g_h)    # 9
    bot.goto_point(g_x + 0.35*g_w, g_y + 0.15*g_h)  # 10
    bot.goto_point(g_x + 0.1*g_w, g_y + 0.0*g_h)    # 11
    bot.goto_point(g_x + 0.0*g_w, g_y + 0.0*g_h)    # 12
    bot.pen_up()
    bot.goto_point(g_x + 0.8*g_w, g_y + 0.9*g_h)    # 13
    bot.pen_down()
    bot.goto_point(g_x + 0.8*g_w, g_y + 0.8*g_h)    # 14 -- noose location
    bot.pen_up()
    bot.go_home()


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
    draw_gallows(bot)

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
    bot.go_home()
    play_game(bot)
    is_first_game = False

print("Bye!")
