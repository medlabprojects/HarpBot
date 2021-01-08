import math
import time

import serial
import numpy as np


def xy_to_gcode(x, y):
  code = 'G0 X{:.3f} Y{:.3F}\r\n'.format(x, y)
  return bytes(code, 'utf-8')

PEN_UP_GCODE = b'G0 Z5\r\n'
PEN_DOWN_GCODE = b'G0 Z-5\r\n'


class HarpBotSerial:
  def __init__(self, port='COM4', baudrate=115200):
    self.ser = serial.Serial(port=port, 
                             baudrate=baudrate,
                             timeout=3)
    
    self.pen_down()
    self.pen_up()
    
    assert(self.ser.is_open), "Connection to robot failed on port {} with baudrate {}.".format(port, baudrate)
  
  def goto(self, x, y):
    self.ser.write(xy_to_gcode(x, y))
    self.wait_for_ok()
    
  def pen_up(self):
    self.ser.write(PEN_UP_GCODE)
    self.wait_for_ok()
    
  def pen_down(self):
    self.ser.write(PEN_DOWN_GCODE)
    self.wait_for_ok()
  
  def wait_for_ok(self):
    line = self.ser.readline()
    print(line)
    
if __name__ == "__main__":
  import keyboard
  
  hbs = HarpBotSerial()
  x = 310
  y = 0
  
  delta = 1
  
  hbs.pen_up()
  
  print('Use the arrow keys to move the robot around. Press spacebar to toggle the pen up and down. Press esc to stop.')
  
  while True:  # making a loop
    xy_changed = False
    
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
    
    if xy_changed:
      hbs.goto(x, y)
      print('x: {}, y: {}'.format(x, y))
      
    if keyboard.is_pressed('u'):
      hbs.pen_up()
    elif keyboard.is_pressed('d'):
      hbs.pen_down()
    
    if keyboard.is_pressed('esc'):
      break
      
    time.sleep(0.01)