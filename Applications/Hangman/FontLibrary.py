import sys
sys.path.append("../../Harpbot")
from HarpBot import HarpBot

import HangmanLib


def draw_Underscore(hb, x, y, s):
  # Move pen up before going to start position Point 1
  hb.pen_up()
  hb.goto_point(x + s*0, y + s*0) # Point 1
  
  # Pen down to start the drawing
  hb.pen_down()
  
  # Move in the correct waypoint motion
  hb.goto_point(x + s*1, y + s*0) # Point 2
  hb.goto_point(x + s*1, y + s*0.1) # Point 3
  hb.goto_point(x + s*0, y + s*0.1) # Etc.
  hb.goto_point(x + s*0, y + s*0)
  
  # Pen up before drawing next thing
  hb.pen_up()


def draw_Z(hb, x, y, s):
  # Move pen up before going to start position Point 1
  hb.pen_up()
  hb.goto_point(x + s*0, y + s*0) # Point 1
  
  # Pen down to start the drawing
  hb.pen_down()
  
  # Move in the correct waypoint motion
  hb.goto_point(x + s*1,   y + s*0) # Point 2
  hb.goto_point(x + s*1,   y + s*0.375) # Point 3
  hb.goto_point(x + s*0.4, y + s*0.375) # Etc.
  hb.goto_point(x + s*1,   y + s*1.125)
  hb.goto_point(x + s*1,   y + s*1.5)
  hb.goto_point(x + s*0,   y + s*1.5)
  hb.goto_point(x + s*0,   y + s*1.125)
  hb.goto_point(x + s*0.6, y + s*1.125)
  hb.goto_point(x + s*0,   y + s*0.375)
  hb.goto_point(x + s*0,   y + s*0)
  
  # Pen up before drawing next thing
  hb.pen_up()


if __name__ == "__main__":
  hb = HarpBot()

  # Toggle the pen to keep the robot SAFE
  hb.pen_down()
  hb.pen_up()

  HangmanLib.DrawString(hb, 'ABCDE', 10, 200, 150)
  HangmanLib.DrawString(hb, 'FGHIJ', 10, 175, 150)
  HangmanLib.DrawString(hb, 'KLMNO', 10, 150, 150)
  HangmanLib.DrawString(hb, 'PQRST', 10, 125, 150)
  HangmanLib.DrawString(hb, 'UVWXYZ_', 10, 100, 150)

  # Lift the pen up and then go home
  hb.pen_up()
  hb.go_home()
