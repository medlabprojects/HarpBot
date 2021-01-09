import time

import keyboard

import HarpBotSerial

hbs = HarpBotSerial.HarpBotSerial()
x = 305
y = 0

delta = 3
  
hbs.pen_up()
  
print('Use the arrow keys to move the robot around. Press spacebar to toggle the pen up and down. Press esc to stop.')

# Each iteration, check which keys are pressed and move the robot accordingly
while True:
  xy_changed = False  # Use this later to decide whether or not to move the robot at all
  
  # If the left key is pressed, update the x position and then set xy_changed to true
  if keyboard.is_pressed('left'):
    x = x - delta
    xy_changed = True
    
  if keyboard.is_pressed('right'):
    x = x + delta
    xy_changed = True
    
  if keyboard.is_pressed('up'):
    y = y + delta
    xy_changed = True
    
  if keyboard.is_pressed('down'):
    y = y - delta
    xy_changed = True
  
  # If we want to move the robot on this iteration, then do it and print the new position.
  if xy_changed:
    hbs.goto(x, y)
    print('x: {}, y: {}'.format(x, y))
  
  # Now move the pen up or down if requested.
  if keyboard.is_pressed('u'):
    hbs.pen_up()
  elif keyboard.is_pressed('d'):
    hbs.pen_down()
  
  # Break execution is requested.
  if keyboard.is_pressed('esc'):
    hbs.pen_up()
    hbs.goto(305, 0)
    break
  
  # Sleep a bit so that we don't get too many commands too quick.
  time.sleep(0.01)