import csv
import random

import FontLibrary


MAX_PHRASE_LENGTH = 20 # Only allow phrases that can fit in a single line on the paper


def LoadPhrases(file_list):
    """
    Loads phrases and categories from 'data.csv'
    """
    phrase_category_pairs = []

    for filename in file_list:
        line_num = 1
        with open(filename, 'r', encoding='utf-8') as f:
            reader = csv.reader(f, delimiter=',')
            print("Parsing " + filename)
            for row in reader:
                try:
                    category = row[0]
                    phrase = row[1]

                    # Don't include if phrase or category requires special characters,
                    # or if the phrase is too long
                    if all(x.isalpha() or x.isspace() for x in phrase) and \
                       all(x.isalpha() or x.isspace() for x in category) and \
                       len(phrase.strip()) <= MAX_PHRASE_LENGTH:
                        phrase_category_pairs.append((category.strip(), phrase.lower().strip()))

                except Exception as e:
                    print("Skipping line " + str(line_num) + " due to error:")
                    print(e)

                line_num = line_num + 1

    print("Loaded " + str(len(phrase_category_pairs)) + " phrases")
    return phrase_category_pairs


def RandomPhrase(phrase_data):
    """
    Returns a random phrase and category from the loaded phrase data
    """
    index = random.randint(0, len(phrase_data)-1)
    pair = phrase_data[index]
    return pair[0], pair[1]


def Blankify(phrase, guessed_letters):
    # Returns a string with any unguessed letters as blanks
    blanked_str = ""
    blanked_str_nospace =""
    for c in phrase:
        if c.isalpha():
            if c in guessed_letters:
                blanked_str_nospace += c
                blanked_str += c + " "
            else:
                blanked_str_nospace += "_"
                blanked_str += "_ "
        else: # Non-alpha character, such as a space.
            blanked_str_nospace += c
            blanked_str += c + " "

    return blanked_str.strip(), blanked_str_nospace.strip()


def GetLetters(phrase):
    """
    Returns a list of all unique letters that need to be guessed to win
    """
    letters = []
    for letter in phrase:
        if letter.isalpha() and not letter.lower() in letters:
            letters.append(letter.lower())

    return sorted(letters)


def DrawLetter(bot, c, x, y, width):
    if c.upper() == 'A': FontLibrary.draw_A(bot, x, y, width)
    elif c.upper() == 'B': FontLibrary.draw_B(bot, x, y, width)
    elif c.upper() == 'C': FontLibrary.draw_C(bot, x, y, width)
    elif c.upper() == 'D': FontLibrary.draw_D(bot, x, y, width)
    elif c.upper() == 'E': FontLibrary.draw_E(bot, x, y, width)
    elif c.upper() == 'F': FontLibrary.draw_F(bot, x, y, width)
    elif c.upper() == 'G': FontLibrary.draw_G(bot, x, y, width)
    elif c.upper() == 'H': FontLibrary.draw_H(bot, x, y, width)
    elif c.upper() == 'I': FontLibrary.draw_I(bot, x, y, width)
    elif c.upper() == 'J': FontLibrary.draw_J(bot, x, y, width)
    elif c.upper() == 'K': FontLibrary.draw_K(bot, x, y, width)
    elif c.upper() == 'L': FontLibrary.draw_L(bot, x, y, width)
    elif c.upper() == 'M': FontLibrary.draw_M(bot, x, y, width)
    elif c.upper() == 'N': FontLibrary.draw_N(bot, x, y, width)
    elif c.upper() == 'O': FontLibrary.draw_O(bot, x, y, width)
    elif c.upper() == 'P': FontLibrary.draw_P(bot, x, y, width)
    elif c.upper() == 'Q': FontLibrary.draw_Q(bot, x, y, width)
    elif c.upper() == 'R': FontLibrary.draw_R(bot, x, y, width)
    elif c.upper() == 'S': FontLibrary.draw_S(bot, x, y, width)
    elif c.upper() == 'T': FontLibrary.draw_T(bot, x, y, width)
    elif c.upper() == 'U': FontLibrary.draw_U(bot, x, y, width)
    elif c.upper() == 'V': FontLibrary.draw_V(bot, x, y, width)
    elif c.upper() == 'W': FontLibrary.draw_W(bot, x, y, width)
    elif c.upper() == 'X': FontLibrary.draw_X(bot, x, y, width)
    elif c.upper() == 'Y': FontLibrary.draw_Y(bot, x, y, width)
    elif c.upper() == 'Z': FontLibrary.draw_Z(bot, x, y, width)
    elif c == '_': FontLibrary.draw_Underscore(bot, x, y, width)
    elif c == ' ': pass
    else: print('Error: Character {} not supported.'.format(c))


def DrawString(bot, s, x, y, container_width):

    print("DrawString()")
    num_chars = len(s)
    num_seps = num_chars - 1

    full_width = container_width / num_chars
    sep_width = 0.2*full_width
    letter_width = full_width - sep_width

    for ii in range(len(s)):
        xi = x + ii*(full_width)
        DrawLetter(bot, s[ii], xi, y, letter_width)


def DrawHangman(bot, num_wrong_guesses):
    if num_wrong_guesses == 1:
        DrawHead()
    elif num_wrong_guesses == 2:
        DrawSpine()
    elif num_wrong_guesses == 3:
        DrawLArm()
    elif num_wrong_guesses == 4:
        DrawRArm()
    elif num_wrong_guesses == 5:
        DrawLLeg()
    elif num_wrong_guesses == 6:
        DrawRLeg()
    else: print('Incorrect num_wrong_guesses: {}'.format(num_wrong_guesses))


###### HANGMAN DRAWING FUNCTIONS ######
def DrawHead():
  print('Drawing Head')

def DrawLArm():
  print('Drawing Left Arm')

def DrawRArm():
  print('Drawing Right Arm')

def DrawLLeg():
  print('Drawing Left Leg')

def DrawRLeg():
  print('Drawing Right Leg')

def DrawSpine():
  print('Drawing Spine')
