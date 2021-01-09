import time

import serial


def xy_to_gcode(x, y):
  code = 'G0 X{:.3f} Y{:.3F}\r\n'.format(x, y)
  return bytes(code, 'utf-8')

PEN_UP_GCODE = b'G0 Z5\r\n'
PEN_DOWN_GCODE = b'G0 Z-5\r\n'


class HarpBotSerial:
  def __init__(self, port='COM4', baudrate=115200):
    self.connected = False
    
    # Now try to connect to the robot. User will be able to detect if it worked based on on self.connected
    try:
      self.ser = serial.Serial(port=port, baudrate=baudrate, timeout=3)
      if self.ser.is_open:
        self.connected = True
    except:
      pass
    
    if self.connected:
      print("Connected to HarpBot on port {} with baudrate {}.".format(port, baudrate))
      self.pen_down()
      self.pen_up()
    else:
      print("Connection to HarpBot failed on port {} with baudrate {}.".format(port, baudrate))
    
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
    #time.sleep(0.01)
    
    
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
  