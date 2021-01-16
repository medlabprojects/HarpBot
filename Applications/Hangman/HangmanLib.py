import csv
import random

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
    for c in phrase:
        if c.isalpha():
            if c in guessed_letters:
                blanked_str = blanked_str + c + " "
            else:
                blanked_str = blanked_str + "_ "
        else: # Non-alpha character, such as a space.
            blanked_str = blanked_str + c + " "

    return blanked_str.strip()

def GetLetters(phrase):
    """
    Returns a list of all unique letters that need to be guessed to win
    """
    letters = []
    for letter in phrase:
        if letter.isalpha() and not letter.lower() in letters:
            letters.append(letter.lower())

    return sorted(letters)
