import HarpBot


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


hb = HarpBot.HarpBot()

# Toggle the pen to keep the robot SAFE
hb.pen_down()
hb.pen_up()

draw_Z(hb, 50, 0, 150)

# Lift the pen up and then go home
hb.pen_up()
hb.go_home()
