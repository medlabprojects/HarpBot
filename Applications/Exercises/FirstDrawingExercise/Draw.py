import sys
sys.path.append("../../../Harpbot")
from HarpBot import HarpBot, PAPER_WIDTH, PAPER_HEIGHT, PAPER_X_OFFSET, PAPER_Y_OFFSET



# Create a new robot instance
bot = HarpBot()

# Start in the home position
bot.go_home()

# Set animation parameters
bot.animation_on = True
bot.animation_skip = 5 # Draw every 5th frame

################################################
#                FUNCTION GUIDE                #
################################################

########## PEN CONTROL ##########
# bot.pen_down()     will place the pen on the paper
# bot.pen_up()       will lift the pen of the paper

########## MOVING ##########
# bot.goto_point(x,y) 

# This function will move the robot to a new position in its workspace.
# The x and y coordinates are integers given in millimeters.
# The point must be reachable by the robot or it won't do anything!

# Valid points can be determined by their distance from the origin (0, 0), 
# which is the base of the robot. 
# The robot can reach the pen to a minimum of 15 millimeters from the origin,
# and a maximum of 305 millimeters.

################################################
#                   EXAMPLE                    #
################################################
# Uncomment this code to run the example!
'''
bot.goto_point(20,20) # Move to point (20, 20)
bot.pen_down()  # Put the pen down to start drawing
bot.goto_point(40, 20) # Move to point (40,20) while the pen is down
bot.goto_point(40, 40) # Continue to point (40, 40)
bot.goto_point (20, 40) # Continue to point (40, 40)
bot.goto_point(20, 20) # Go back to point (20, 20) to complete a square
bot.pen_up() # Lift the pen off the paper
bot.goto_point(100, 100) # Go to point (100, 100)
bot.pen_down() # Put the pen down to start drawing
bot.goto_point(120, 100) # Move to point (120, 100) while the pen is down
bot.goto_point(120, 120) # Continue to point (120, 120)
bot.goto_point(100, 120) # Continue to point (100, 120)
bot.goto_point(100, 100) # Go back to point (100, 100)
bot.pen_up() # Lift the pen off the paper when we're finished drawing
'''

####################################################
############## YOUR CODE GOES HERE #################




####################################################
####################################################
# Wait for a key press before closing the plot
input('Press any key to continue')