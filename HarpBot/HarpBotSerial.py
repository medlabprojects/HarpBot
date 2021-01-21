import time

import serial

is_pen_up = False

def xy_to_gcode(x, y):
  global is_pen_up
  
  code = 'G0X{:.3f}Y{:.3F}'.format(x, y)
  if is_pen_up:
    code += 'Z5.000'
  else:
    code += 'Z-5.000'
  
  code += '\n'
  return bytes(code, 'utf-8')

PEN_UP_GCODE = b'G0Z5\n'
PEN_DOWN_GCODE = b'G0Z-5\n'


class HarpBotSerial:
  def __init__(self, port='COM4', baudrate=250000):
    self.connected = False
    
    # Now try to connect to the robot. User will be able to detect if it worked based on on self.connected
    try:
      self.ser = serial.Serial(port=port, baudrate=baudrate, timeout=3)
      if self.ser.is_open:
        self.connected = True
    except Exception as e:
      print(e)
      
    if self.connected:
      print("Connected to HarpBot on port {} with baudrate {}.".format(port, baudrate))
      self.pen_down()
      self.pen_up()
    else:
      print("Connection to HarpBot failed on port {} with baudrate {}.".format(port, baudrate))
    
  def goto(self, x, y):
    self.ser.write(xy_to_gcode(x, y))
    is_error = self.wait_for_ok()
    if is_error:
      self.goto(x, y)
      
  def pen_up(self):
    global is_pen_up
    is_pen_up = True
    self.ser.write(PEN_UP_GCODE)
    is_error = self.wait_for_ok()
    if is_error:
      self.pen_up()
      
  def pen_down(self):
    global is_pen_up
    is_pen_up = False
    self.ser.write(PEN_DOWN_GCODE)
    is_error = self.wait_for_ok()
    if is_error:
      self.pen_down()
      
  def wait_for_ok(self):
    line = self.ser.readline()
    if 'error' in str(line):
      print(str(line))
      return True
    
    return False
    
    
if __name__ == "__main__":
  hb = HarpBotSerial()
  
  # Toggle pen up and down twice
  hb.pen_down()
  hb.pen_up()
  hb.pen_down()
  hb.pen_up()
  
  # Move in a square pattern
  hb.goto(100, 100)
  hb.goto(100, 200)
  hb.goto(0, 200)
  hb.goto(0, 100)
  hb.goto(100, 100)
  
  # Go back to home
  hb.goto(305, 0)
  