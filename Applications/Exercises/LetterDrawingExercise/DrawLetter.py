# This exercise is designed for the student to draw a letter that will be used
# by the Hangman application

import sys
sys.path.append("../../../Harpbot")
from HarpBot import HarpBot, PAPER_WIDTH, PAPER_HEIGHT, PAPER_X_OFFSET, PAPER_Y_OFFSET
from FontLibrary import draw_testbox, draw_A

# Create a new robot instance
bot = HarpBot()

# Start in the home position
bot.go_home()

# Set animation parameters
bot.animation_on = True
bot.animation_skip = 5 # Draw every 5th frame


# The X,Y coordinate to draw your letter at
x = 100
y = 100

# The scale to draw your letter
# Scale is in millimeters, with s=1 giving a letter that is 1mm wide by 1.5mm tall.
# so 50 will give a letter that is 5 centimeter wide and 7.5 centimeters tall
s = 50

####################################################
############## YOUR CODE GOES HERE #################

# Draw the test box that the letter should fit inside
draw_testbox(bot, x, y, s)

# Draw your letter using x,y and s! Make sure it fits perfectly in the box!
draw_A(bot, x, y, s)   # Change "draw_A" to whichever function in FontLibrary.py you are implementing!


# Return the robot to its home position after drawing
bot.go_home()
####################################################
# Wait for a key press before closing the plot
bot.draw_scene() # Draw any frames that are still waiting
input('Press any key to continue')