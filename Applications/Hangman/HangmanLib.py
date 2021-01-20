import csv
import random

from numpy import genfromtxt

import FontLibrary


MAX_PHRASE_LENGTH = 20 # Only allow phrases that can fit in a single line on the paper

# Gallows
GALLOWS_X = -80.0
GALLOWS_Y = 125.0
GALLOWS_W = 75.0
GALLOWS_H = 130.0
NOOSE_X = GALLOWS_X + 0.8*GALLOWS_W  #(g_x + 0.8*g_w, g_y + 0.8*g_h)
NOOSE_Y = GALLOWS_Y + 0.8*GALLOWS_H

# Head
HEAD_RADIUS = 10
HEAD_X = NOOSE_X
HEAD_Y = NOOSE_Y - HEAD_RADIUS

BODY_HEIGHT = 30
BODY_WIDTH = 5

# Body
BODY_X1 = HEAD_X - (BODY_WIDTH)/2.0
BODY_Y1 = HEAD_Y - HEAD_RADIUS - BODY_HEIGHT
BODY_X2 = HEAD_X + (BODY_WIDTH)/2.0
BODY_Y2 = HEAD_Y - HEAD_RADIUS

ARM_WIDTH = 40
ARM_HEIGHT = 40
LEG_HEIGHT = 40
LEG_WIDTH = 40
NECK_LENGTH = 5

# Left Arm
LEFT_ARM_X1 = BODY_X1 - ARM_WIDTH
LEFT_ARM_Y1 = BODY_Y2 - NECK_LENGTH
LEFT_ARM_X2 = BODY_X1
LEFT_ARM_Y2 = BODY_Y2 + ARM_HEIGHT - NECK_LENGTH

# Right Arm
RIGHT_ARM_X1 = BODY_X2
RIGHT_ARM_Y1 = BODY_Y2 - NECK_LENGTH
RIGHT_ARM_X2 = BODY_X2 + ARM_WIDTH
RIGHT_ARM_Y2 = BODY_Y2 + ARM_HEIGHT - NECK_LENGTH

# Left Leg
LEFT_LEG_X1 = BODY_X1 - LEG_WIDTH
LEFT_LEG_Y1 = BODY_Y1 - LEG_HEIGHT
LEFT_LEG_X2 = BODY_X1
LEFT_LEG_Y2 = BODY_Y1

# Right Leg
RIGHT_LEG_X1 = BODY_X2
RIGHT_LEG_Y1 = BODY_Y1 - LEG_HEIGHT
RIGHT_LEG_X2 = BODY_X2 + LEG_WIDTH
RIGHT_LEG_Y2 = BODY_Y1

# Category cloud
CLOUD_X = 50.0
CLOUD_Y = 185.0
CLOUD_W = 125.0
CLOUD_H = 100.0

CAT_LABEL_W = CLOUD_W / 2.0
CAT_LABEL_X = CLOUD_X + 0.5*CLOUD_W - 0.5*CAT_LABEL_W
CAT_LABEL_Y = CLOUD_Y + 0.55*CLOUD_H

CAT_NAME_W = CLOUD_W/2.0
CAT_NAME_X = CLOUD_X + 0.5*CLOUD_W - 0.5*CAT_NAME_W
CAT_NAME_Y = CLOUD_Y + 0.15*CLOUD_H

# Guess table
GUESS_TABLE_X = CLOUD_X
GUESS_TABLE_Y = GALLOWS_Y
GUESS_TABLE_W = CLOUD_W
GUESS_TABLE_H = 30

GUESS_LABEL_W = GUESS_TABLE_W / 2.0
GUESS_LABEL_X = GUESS_TABLE_X + 0.5*GUESS_TABLE_W - 0.5*GUESS_LABEL_W
GUESS_LABEL_Y = GUESS_TABLE_Y + 1.1*GUESS_TABLE_H

GUESS_W = GUESS_TABLE_W*0.50
GUESS_X = GUESS_TABLE_X + 0.5*GUESS_TABLE_W - 0.5*GUESS_W
GUESS_Y = GUESS_TABLE_Y + 0.2*GUESS_TABLE_H

# Blanks
BLANKS_X = -75.0
BLANKS_Y = 75.0
BLANKS_W = 250.0


def load_phrases(file_list):
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


def random_phrase(phrase_data):
    """
    Returns a random phrase and category from the loaded phrase data
    """
    index = random.randint(0, len(phrase_data)-1)
    pair = phrase_data[index]
    return pair[0], pair[1]


def blankify(phrase, guessed_letters):
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


def get_letters(phrase):
    """
    Returns a list of all unique letters that need to be guessed to win
    """
    letters = []
    for letter in phrase:
        if letter.isalpha() and not letter.lower() in letters:
            letters.append(letter.lower())

    return sorted(letters)


def draw_letter(bot, c, x, y, width):
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


def draw_string(bot, s, x, y, container_width):
    num_chars = len(s)
    num_seps = num_chars - 1

    full_width = container_width / num_chars
    sep_width = 0.2*full_width
    letter_width = full_width - sep_width

    for ii in range(len(s)):
        xi = x + ii*(full_width)
        draw_letter(bot, s[ii], xi, y, letter_width)


def draw_hangman(bot, num_wrong_guesses):
    if num_wrong_guesses == 1:
        draw_head(bot)
    elif num_wrong_guesses == 2:
        draw_spine(bot)
    elif num_wrong_guesses == 3:
        draw_left_arm(bot)
    elif num_wrong_guesses == 4:
        draw_right_arm(bot)
    elif num_wrong_guesses == 5:
        draw_left_leg(bot)
    elif num_wrong_guesses == 6:
        draw_right_leg(bot)
    else: print('Incorrect num_wrong_guesses: {}'.format(num_wrong_guesses))


def draw_category(bot, category):
    # Draws cloud
    cloud_coords = genfromtxt('image_outlines/cloud_coords.csv', delimiter=',')
    bot.pen_up()
    for ii in range(len(cloud_coords)):
        bot.goto_point(CLOUD_X + cloud_coords[ii,0]*CLOUD_W, CLOUD_Y + cloud_coords[ii,1]*CLOUD_H)
        if ii == 0:
            bot.pen_down()
        if ii == len(cloud_coords):
            bot.pen_up()

    # TODO: draw the word "category" on top of box
    draw_string(bot, "category", CAT_LABEL_X, CAT_LABEL_Y, CAT_LABEL_W)
    draw_string(bot, category, CAT_NAME_X, CAT_NAME_Y, CAT_NAME_W)


def draw_blanks(bot, phrase):
    _, blankified_phrase = blankify(phrase,[])
    draw_string(bot, blankified_phrase, BLANKS_X, BLANKS_Y, BLANKS_W)


def draw_gallows(bot):
    bot.pen_up()
    bot.goto_point(GALLOWS_X + 0.00*GALLOWS_W, GALLOWS_Y + 0.00*GALLOWS_H)    # 1
    bot.pen_down()
    bot.goto_point(GALLOWS_X + 0.30*GALLOWS_W, GALLOWS_Y + 0.20*GALLOWS_H)    # 2
    bot.goto_point(GALLOWS_X + 0.30*GALLOWS_W, GALLOWS_Y + 1.00*GALLOWS_H)    # 3
    bot.goto_point(GALLOWS_X + 0.80*GALLOWS_W, GALLOWS_Y + 1.00*GALLOWS_H)    # 4
    bot.goto_point(GALLOWS_X + 0.80*GALLOWS_W, GALLOWS_Y + 0.95*GALLOWS_H)    # 5
    bot.goto_point(GALLOWS_X + 0.40*GALLOWS_W, GALLOWS_Y + 0.95*GALLOWS_H)    # 6
    bot.goto_point(GALLOWS_X + 0.40*GALLOWS_W, GALLOWS_Y + 0.20*GALLOWS_H)    # 7
    bot.goto_point(GALLOWS_X + 0.70*GALLOWS_W, GALLOWS_Y + 0.00*GALLOWS_H)    # 8
    bot.goto_point(GALLOWS_X + 0.60*GALLOWS_W, GALLOWS_Y + 0.00*GALLOWS_H)    # 9
    bot.goto_point(GALLOWS_X + 0.35*GALLOWS_W, GALLOWS_Y + 0.15*GALLOWS_H)    # 10
    bot.goto_point(GALLOWS_X + 0.10*GALLOWS_W, GALLOWS_Y + 0.00*GALLOWS_H)    # 11
    bot.goto_point(GALLOWS_X + 0.00*GALLOWS_W, GALLOWS_Y + 0.00*GALLOWS_H)    # 12
    bot.pen_up()
    bot.goto_point(GALLOWS_X + 0.80*GALLOWS_W, GALLOWS_Y + 0.95*GALLOWS_H)    # 13
    bot.pen_down()
    bot.goto_point(GALLOWS_X + 0.80*GALLOWS_W, GALLOWS_Y + 0.80*GALLOWS_H)    # 14 -- noose location
    bot.pen_up()


def draw_guessing_table(bot):
    bot.draw_rectangle(GUESS_TABLE_X, GUESS_TABLE_Y, GUESS_TABLE_X + GUESS_TABLE_W, GUESS_TABLE_Y + GUESS_TABLE_H)
    eps = 3
    bot.draw_rectangle(GUESS_TABLE_X + eps, GUESS_TABLE_Y + eps, GUESS_TABLE_X + GUESS_TABLE_W - eps, GUESS_TABLE_Y + GUESS_TABLE_H - eps)
    draw_string(bot, 'GUESSES', GUESS_LABEL_X, GUESS_LABEL_Y, GUESS_LABEL_W)

def draw_head(bot):
    bot.draw_circle(HEAD_X, HEAD_Y, HEAD_RADIUS)

def draw_left_arm(bot):
    bot.draw_rectangle(LEFT_ARM_X1, LEFT_ARM_Y1, LEFT_ARM_X2, LEFT_ARM_Y2)

def draw_right_arm(bot):
    bot.draw_rectangle(RIGHT_ARM_X1, RIGHT_ARM_Y1, RIGHT_ARM_X2, RIGHT_ARM_Y2)

def draw_left_leg(bot):
    bot.draw_rectangle(LEFT_LEG_X1, LEFT_LEG_Y1, LEFT_LEG_X2, LEFT_LEG_Y2)

def draw_right_leg(bot):
    bot.draw_rectangle(RIGHT_LEG_X1, RIGHT_LEG_Y1, RIGHT_LEG_X2, RIGHT_LEG_Y2)

def draw_spine(bot):
    bot.draw_rectangle(BODY_X1, BODY_Y1, BODY_X2, BODY_Y2)
