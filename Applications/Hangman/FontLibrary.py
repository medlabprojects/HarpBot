import sys
sys.path.append("../../Harpbot")

from HarpBot import HarpBot
import HangmanLib


# These constants set the aspect ratio of the letters. 
# Really, the only one that's a choice is MAX_LETTER_Y = 1.5 
# TODO: incorporate these constants into the draw_<> functions below.
MIN_LETTER_X = 0.0
MAX_LETTER_X = 1.0
MIN_LETTER_Y = 0.0
MAX_LETTER_Y = 1.5


def draw_A(hb, x, y, s):
  hb.pen_up()
  hb.goto_point(x,y) #point number 1
  hb.pen_down() #starts drawing
  hb.goto_point(x + s*.35, y + s*1.5) #point 2
  hb.goto_point(x + s*.65, y + s*1.5) #point 3
  hb.goto_point(x + s*1, y + s*0) #point 4
  hb.goto_point(x + s*.75, y + s*0) #point 5
  hb.goto_point(x + s*.65, y + s*.65) #point 6
  hb.goto_point(x + s*.35, y + s*.65) #point 7
  hb.goto_point(x + s*.25, y + s*0) #point 8
  hb.goto_point(x,y) #back to start!! Done with outline
  hb.pen_up() #doing the middle of the A
  hb.goto_point(x + s*.45, y + s*.85) #point 9
  hb.pen_down()#starts drawing
  hb.goto_point(x + s*.55, y + s*.85) #point 10
  hb.goto_point(x + s*.55, y + s*1.2) #point 11
  hb.goto_point(x + s*.45, y + s*1.2) #point 12
  hb.goto_point(x + s*.45, y + s*.85) #point 9
  hb.pen_up()


def draw_B(hb, x, y, s):
  hb.pen_up()
  hb.goto_point(x,y) #point number 1/17
  hb.pen_down() #starts drawing
  hb.goto_point(x + s*0, y + s*1.5) #point 2
  hb.goto_point(x + s*.75, y + s*1.5) #point 3
  hb.goto_point(x + s*.9, y + s*1.25) #point 4
  hb.goto_point(x + s*.9, y + s*1) #point 5
  hb.goto_point(x + s*.75, y + s*.75) #point 6
  hb.goto_point(x + s*.9, y + s*.5) #point 7
  hb.goto_point(x + s*.9, y + s*.25) #point 8
  hb.goto_point(x + s*.75, y + s*0) #point 9
  hb.goto_point(x,y) #point number 1
  hb.pen_up()
  hb.goto_point(x + s*.25, y + s*.25) #point 10
  hb.pen_down()
  hb.goto_point(x + s*.6, y + s*.25) #point 11
  hb.goto_point(x + s*.6, y + s*.5) #point 12
  hb.goto_point(x + s*.25, y + s*.5) #point 13
  hb.goto_point(x + s*.25, y + s*.25) #point 10
  hb.pen_up()
  hb.goto_point(x + s*.25, y + s*1) #point 14
  hb.pen_down()
  hb.goto_point(x + s*.6, y + s*1) #point 15
  hb.goto_point(x + s*.6, y + s*1.25) #point 16
  hb.goto_point(x + s*.25, y + s*1.25) #point 17
  hb.goto_point(x + s*.25, y + s*1) #point 14
  hb.pen_up()
  hb.goto_point(x,y)
  hb.pen_up()


def draw_C(hb, x, y, s):
  hb.pen_up()
  hb.goto_point(x + s*.2,y + s*0) #point number 1
  hb.pen_down() #starts drawing
  hb.goto_point(x + s*0, y + s*.2) #point 2
  hb.goto_point(x + s*0, y + s*1.3) #point 3
  hb.goto_point(x + s*.2, y + s*1.5) #point 4
  hb.goto_point(x + s*1, y + s*1.5) #point 5
  hb.goto_point(x + s*1, y + s*1.25) #point 6
  hb.goto_point(x + s*.3, y + s*1.25) #point 7
  hb.goto_point(x + s*.3, y + s*.25) #point 8
  hb.goto_point(x + s*1, y + s*.25) #point 9
  hb.goto_point(x + s*1, y + s*0) #point 10
  hb.goto_point(x + s*.2,y + s*0) #point number 1
  hb.pen_up()

def draw_D(hb, x, y, s):
  hb.pen_up()
  hb.goto_point(x,y) #point number 1
  hb.pen_down() #starts drawing
  hb.goto_point(x + s*0, y + s*1.5) #point 2
  hb.goto_point(x + s*.8, y + s*1.5) #point 3
  hb.goto_point(x + s*1, y + s*1.2) #point 4
  hb.goto_point(x + s*1, y + s*.3) #point 5
  hb.goto_point(x + s*.8, y + s*0) #point 6
  hb.goto_point(x,y) #point number 1
  hb.pen_up() #now onto the inside
  hb.goto_point(x + s*.2, y + s*.3) #point 7
  hb.pen_down() #starts drawing
  hb.goto_point(x + s*.2, y + s*1.2) #point 8
  hb.goto_point(x + s*.75, y + s*1.2) #point 9
  hb.goto_point(x + s*.75, y + s*.3) #point 10
  hb.goto_point(x + s*.2, y + s*.3) #point 7
  hb.pen_up()


def draw_E(hb, x, y, s):
  hb.pen_up()
  hb.goto_point(x,y) #point number 1
  hb.pen_down() #starts drawing
  hb.goto_point(x + s*0, y + s*1.5) #point 2
  hb.goto_point(x + s*1, y + s*1.5) #point 3
  hb.goto_point(x + s*1, y + s*1.25) #point 4
  hb.goto_point(x + s*.25, y + s*1.25) #point 5
  hb.goto_point(x + s*.25, y + s*.925) #point 6
  hb.goto_point(x + s*.75, y + s*.925) #point 7
  hb.goto_point(x + s*.75, y + s*.675) #point 8
  hb.goto_point(x + s*.25, y + s*.675) #point 9
  hb.goto_point(x + s*.25, y + s*.25) #point 10
  hb.goto_point(x + s*1, y + s*.25) #point 11
  hb.goto_point(x + s*1, y + s*0) #point 12
  hb.goto_point(x,y) #point number 1
  hb.pen_up()


def draw_F(hb, x, y, s):
  hb.pen_up()
  hb.goto_point(x + s*0, y + s*0) # Point 0
  hb.pen_down()
  hb.goto_point(x + s*0.25,  y + s*0) # Point 1
  hb.goto_point(x + s*0.25,  y + s*.75) # Point 2
  hb.goto_point(x + s*1,     y + s*.75) # 3
  hb.goto_point(x + s*1,     y + s*1)#4
  hb.goto_point(x + s*0.25,  y + s*1)#5
  hb.goto_point(x + s*0.25,  y + s*1.1)#6
  hb.goto_point(x + s*1,     y + s*1.1)#7
  hb.goto_point(x + s*1,     y + s*1.5)#8
  hb.goto_point(x + s*0,     y + s*1.5)#9
  hb.goto_point(x + s*0,     y + s*0)#0
  hb.pen_up()
  

def draw_G(hb, x, y, s):
  hb.pen_up()
  hb.goto_point(x + s*0, y + s*0) # Point 0
  hb.pen_down()
  hb.goto_point(x + s*1,   y + s*0) # Point 1
  hb.goto_point(x + s*1,   y + s*.8) # Point 2
  hb.goto_point(x + s*.5,  y + s*.8) # 3
  hb.goto_point(x + s*.5,  y + s*.6)#4
  hb.goto_point(x + s*0.75,  y + s*.6)#5
  hb.goto_point(x + s*0.75,  y + s*.4)#6
  hb.goto_point(x + s*.25,     y + s*.4)#7
  hb.goto_point(x + s*.25,     y + s*1)#8
  hb.goto_point(x + s*1,     y + s*1)#9
  hb.goto_point(x + s*1,     y + s*1.5)#9
  hb.goto_point(x + s*0,     y + s*1.5)#10
  hb.goto_point(x + s*0,     y + s*0)#0
  hb.pen_up()
  

def draw_H(hb, x, y, s):
  hb.pen_up()
  hb.goto_point(x + s*0, y + s*0) # Point 0
  hb.pen_down()
  hb.goto_point(x + s*.25,   y + s*0) # Point 1
  hb.goto_point(x + s*.25,   y + s*.5) # Point 2
  hb.goto_point(x + s*.75,  y + s*.5) # 3
  hb.goto_point(x + s*.75,  y + s*0)#4
  hb.goto_point(x + s*1,  y + s*0)#5
  hb.goto_point(x + s*1,  y + s*1.5)#6
  hb.goto_point(x + s*.75,     y + s*1.5)#7
  hb.goto_point(x + s*.75,     y + s*1)#8
  hb.goto_point(x + s*.25,     y + s*1)#9
  hb.goto_point(x + s*.25,     y + s*1.5)#9
  hb.goto_point(x + s*0,     y + s*1.5)#10
  hb.goto_point(x + s*0,     y + s*0)#0
  hb.pen_up()
  

def draw_I(hb, x, y, s):
  hb.pen_up()
  hb.goto_point(x + s*0.25, y + s*0) # Point 0
  hb.pen_down()
  hb.goto_point(x + s*0.25,   y + s*.25) # Point 1
  hb.goto_point(x + s*.65,   y + s*.25) # Point 2
  hb.goto_point(x + s*.65,  y + s*1.25) # 3
  hb.goto_point(x + s*0.25,  y + s*1.25)#4
  hb.goto_point(x + s*0.25,  y + s*1.5)#5
  hb.goto_point(x + s*1.25,  y + s*1.5)#6
  hb.goto_point(x + s*1.25,     y + s*1.25)#7
  hb.goto_point(x + s*.9,     y + s*1.25)#8
  hb.goto_point(x + s*.9,     y + s*.25)#9
  hb.goto_point(x + s*1.25,     y + s*.25)#9
  hb.goto_point(x + s*1.25,     y + s*0)#10
  hb.goto_point(x + s*0.25,     y + s*0)#0
  hb.pen_up()
  

def draw_J(hb, x, y, s):
  hb.pen_up()
  hb.goto_point(x + s*0, y + s*0) # Point 0
  hb.pen_down()
  hb.goto_point(x + s*.75,   y + s*0) # Point 1
  hb.goto_point(x + s*.75,   y + s*1.25) # Point 2
  hb.goto_point(x + s*1,  y + s*1.25) # 3
  hb.goto_point(x + s*1,  y + s*1.5)#4
  hb.goto_point(x + s*0,  y + s*1.5)#5
  hb.goto_point(x + s*0,  y + s*1.25)#6
  hb.goto_point(x + s*.5,     y + s*1.25)#7
  hb.goto_point(x + s*.5,     y + s*.25)#8
  hb.goto_point(x + s*.25,     y + s*.25)#9
  hb.goto_point(x + s*.25,     y + s*.5)#9
  hb.goto_point(x + s*0,     y + s*.5)#10
  hb.goto_point(x + s*0,     y + s*0)#0
  hb.pen_up()
  

def draw_K(hb, x, y, s):
  hb.pen_up()
  hb.goto_point(x + s*0, y + s*0) # Point 1
  hb.pen_down()
  hb.goto_point(x + s*.25,   y + s*0) # Point 2
  hb.goto_point(x + s*.25,   y + s*0.5) # Point 3
  hb.goto_point(x + s*0.7,   y + s*0) # Etc.
  hb.goto_point(x + s*1,     y + s*0)
  hb.goto_point(x + s*0.35,  y + s*.75)
  hb.goto_point(x + s*1,     y + s*1.5)
  hb.goto_point(x + s*0.7,   y + s*1.5)
  hb.goto_point(x + s*0.25,  y + s*1)
  hb.goto_point(x + s*0.25,  y + s*1.5)
  hb.goto_point(x + s*0,     y + s*1.5) # Point 11
  hb.goto_point(x + s*0,     y + s*0)
  hb.pen_up()


def draw_L(hb, x, y, s):
  hb.pen_up()
  hb.goto_point(x + s*0, y + s*0) # Point 1
  hb.pen_down()
  hb.goto_point(x + s*0,    y + s*1.5) # Point 2
  hb.goto_point(x + s*.3,   y + s*1.5) # Point 3
  hb.goto_point(x + s*.3,   y + s*.3) # Point 4
  hb.goto_point(x + s*1,    y + s*0.3)
  hb.goto_point(x + s*1,    y + s*0)
  hb.goto_point(x + s*0,    y + s*0) # Point 7
  hb.pen_up()


def draw_M(hb, x, y, s):
  hb.pen_up()
  hb.goto_point(x + s*0, y + s*0) # Point 1
  hb.pen_down()
  hb.goto_point(x + s*.25,   y + s*0) # Point 2
  hb.goto_point(x + s*.25,   y + s*0.9) # Point 3
  hb.goto_point(x + s*0.45,  y + s*0.7) # Point 4
  hb.goto_point(x + s*0.55,  y + s*0.7)
  hb.goto_point(x + s*0.75,  y + s*0.9)
  hb.goto_point(x + s*0.75,  y + s*0)
  hb.goto_point(x + s*1,     y + s*0) # Point 7
  hb.goto_point(x + s*1,     y + s*1.5)
  hb.goto_point(x + s*0.75,  y + s*1.5)
  hb.goto_point(x + s*0.5,   y + s*1.1)
  hb.goto_point(x + s*0.25,  y + s*1.5) # Point 11
  hb.goto_point(x + s*0,     y + s*1.5)
  hb.goto_point(x + s*0,     y + s*0)
  hb.pen_up()


def draw_N(hb, x, y, s):
  hb.pen_up()
  hb.goto_point(x + s*0, y + s*0) # Point 1
  hb.pen_down()
  hb.goto_point(x + s*.25,   y + s*0)   # Point 2
  hb.goto_point(x + s*.25,   y + s*1) # Point 3
  hb.goto_point(x + s*0.75,  y + s*0)   # Point 4
  hb.goto_point(x + s*1,     y + s*0)
  hb.goto_point(x + s*1,     y + s*1.5)
  hb.goto_point(x + s*0.75,  y + s*1.5)
  hb.goto_point(x + s*0.75,  y + s*0.5) # Point 8
  hb.goto_point(x + s*0.25,  y + s*1.5)
  hb.goto_point(x + s*0,     y + s*1.5) #
  hb.goto_point(x + s*0,     y + s*0)   # Point 11
  hb.pen_up()


def draw_O(hb, x, y, s):
  hb.pen_up()
  hb.goto_point(x + s*0, y + s*0) # Point 1
  hb.pen_down()
  hb.goto_point(x + s*1,   y + s*0)   # Point 2
  hb.goto_point(x + s*1,   y + s*1.5) # Point 3
  hb.goto_point(x + s*0,  y + s*1.5)   # Point 4
  hb.goto_point(x + s*0,     y + s*0)
  hb.pen_up()
  hb.goto_point(x + s*0.25,     y + s*0.25) # Point 6
  hb.pen_down()
  hb.goto_point(x + s*0.75,  y + s*0.25)
  hb.goto_point(x + s*0.75,  y + s*1.25) # Point 8
  hb.goto_point(x + s*0.25,  y + s*1.25)
  hb.goto_point(x + s*0.25,     y + s*0.25)
  hb.pen_up()


def draw_P(hb, x, y, s):
  hb.pen_up()
  hb.goto_point(x + s*0, y + s*0)
  hb.pen_down()
  hb.goto_point(x + s*0,   y + s*1.5) 
  hb.goto_point(x + s*.75,   y + s*1.5) 
  hb.goto_point(x + s*.75, y + s*.75) 
  hb.goto_point(x + s*.25,   y + s*.75)
  hb.goto_point(x + s*.25,   y + s*0)
  hb.goto_point(x + s*0,   y + s*0)
  hb.pen_up()
  hb.goto_point(x + s*.25, y + s*(1.5-.2))
  hb.pen_down()
  hb.goto_point(x + s*.55, y + s*(1.5-.2))
  hb.goto_point(x + s*.55, y + s*.95)
  hb.goto_point(x + s*.25, y + s*.95)
  hb.goto_point(x + s*.25, y + s*(1.5-.2))
  hb.pen_up()
  

def draw_Q(hb, x, y, s):
  hb.pen_up()
  hb.goto_point(x + s*0, y + s*0) # Point 1
  hb.pen_down()
  hb.goto_point(x + s*1,       y + s*0) # Point 2
  hb.goto_point(x + s*1.125,   y + s*-.3) # Point 3
  hb.goto_point(x + s*1.5,     y + s*-.3) # Etc.
  hb.goto_point(x + s*1.375,   y + s*0)
  hb.goto_point(x + s*2.125,   y + s*1.125)
  hb.goto_point(x + s*1.375,   y + s*2.25)
  hb.goto_point(x + s*0,       y + s*2.25)
  hb.goto_point(x + s*-.75,    y + s*1.125)
  hb.goto_point(x + s*0,       y + s*0)
  hb.pen_up()
  hb.goto_point(x + s*0.125,   y + s*.375)
  hb.pen_down()
  hb.goto_point(x + s*1.125,   y + s*.375)
  hb.goto_point(x + s*1.65,    y + s*1.125)
  hb.goto_point(x + s*1.125,   y + s*1.85)
  hb.goto_point(x + s*.125,    y + s*1.85)
  hb.goto_point(x + s*-.375,   y + s*1.125)
  hb.goto_point(x + s*.124,    y + s*.375)
  hb.pen_up()


def draw_R(hb, x, y, s):
  hb.pen_up()
  hb.goto_point(x + s*0, y + s*0)
  hb.pen_down()
  hb.goto_point(x + s*0,   y + s*1.5) 
  hb.goto_point(x + s*.70,   y + s*1.5) 
  hb.goto_point(x + s*.70, y + s*.75) 
  hb.goto_point(x + s*.5,   y + s*.75)
  hb.goto_point(x + s*.65,   y + s*0)
  hb.goto_point(x + s*.5,   y + s*0)
  hb.goto_point(x + s*.45,   y + s*0)
  hb.goto_point(x + s*.25,   y + s*.75)
  hb.goto_point(x + s*.25,   y + s*0)
  hb.goto_point(x + s*0, y + s*0)
  hb.pen_up()
  

def draw_S(hb, x, y, s):
  hb.pen_up()
  hb.goto_point(x + s*0, y + s*0)
  hb.pen_down()
  hb.goto_point(x + s*1,    y + s*0)
  hb.goto_point(x + s*1,    y + s*1)
  hb.goto_point(x + s*.25,  y + s*1)
  hb.goto_point(x + s*.25,  y + s*1.25)
  hb.goto_point(x + s*1,    y + s*1.25)
  hb.goto_point(x + s*1,    y + s*1.75)
  hb.goto_point(x + s*0,    y + s*1.75)
  hb.goto_point(x + s*0,    y + s*.6)
  hb.goto_point(x + s*.75,  y + s*.6)
  hb.goto_point(x + s*.75,  y + s*.25)
  hb.goto_point(x + s*0,    y + s*.25)
  hb.goto_point(x + s*0,    y + s*0)
  hb.pen_up()


def draw_T(hb, x, y, s):
  hb.pen_up()
  hb.goto_point(x + s*.66, y + s*0)
  hb.pen_down()
  hb.goto_point(x + s*.33,   y + s*.0) 
  hb.goto_point(x + s*.33,   y + s*(1.5-.375)) 
  hb.goto_point(x + s*0, y + s*(1.5-.375)) 
  hb.goto_point(x + s*0,   y + s*1.5)
  hb.goto_point(x + s*1,   y + s*1.5)
  hb.goto_point(x + s*1,   y + s*(1.5-.375))
  hb.goto_point(x + s*.66,   y + s*(1.5-.375))
  hb.goto_point(x + s*.66,   y + s*0)
  hb.pen_up()


def draw_U(hb, x, y, s):
  hb.pen_up()
  hb.goto_point(x + s*0,   y + s*1.4) # Point 1
  hb.pen_down()
  hb.goto_point(x + s*0.16,   y + s*1.4) # Point 2
  hb.goto_point(x + s*0.16, y + s*0.33) # 3
  hb.goto_point(x + s*0.33,   y + s*0.2) #4
  hb.goto_point(x + s*0.67,   y + s*0.2)#5
  hb.goto_point(x + s*0.84,   y + s*0.33)#6
  hb.goto_point(x + s*0.84,   y + s*1.4)#7
  hb.goto_point(x + s*1, y + s*1.4)#8
  hb.goto_point(x + s*1,   y + s*0.33)#9
  hb.goto_point(x + s*0.74,   y + s*0)#10
  hb.goto_point(x + s*0.26,   y + s*0)#11
  hb.goto_point(x + s*0,   y + s*0.33)#12
  hb.goto_point(x + s*0,   y + s*1.4)
  hb.pen_up()
  

def draw_V(hb, x, y, s):
  hb.pen_up()
  hb.goto_point(x+s*0, y+s*1.25)#point1
  hb.pen_down()
  hb.goto_point(x+s*0.25, y+s*1.25)#2
  hb.goto_point(x+s*0.5, y+s*0.5)#3
  hb.goto_point(x+s*0.75, y+s*1.25)#4
  hb.goto_point(x+s*1, y+s*1.25)#5
  hb.goto_point(x+s*0.5, y+s*0)#6
  hb.goto_point(x+s*0, y+s*1.25)#7
  hb.pen_up()
  

def draw_W(hb, x, y, s):
  hb.pen_up()
  hb.goto_point(x+s*0,y+s*1.25)#1
  hb.pen_down()
  hb.goto_point(x+s*0.25,y+s*0)#2
  hb.goto_point(x+s*0.5,y+s*0.25)#3
  hb.goto_point(x+s*0.75,y+s*0)#4
  hb.goto_point(x+s*1,y+s*1.25)#5
  hb.goto_point(x+s*0.85,y+s*1.25)#6
  hb.goto_point(x+s*0.65,y+s*0.25)#7
  hb.goto_point(x+s*0.5,y+s*0.45)#8
  hb.goto_point(x+s*0.35,y+s*0.25)#9
  hb.goto_point(x+s*0.15,y+s*1.25)#10
  hb.goto_point(x+s*0,y+s*1.25)#11
  hb.pen_up()


def draw_X(hb, x, y, s):
  hb.pen_up()
  hb.goto_point(x+s*0,y+s*0)#1
  hb.pen_down()
  hb.goto_point(x+s*0.375,y+s*0.75)#2 and 0.375=3/8
  hb.goto_point(x+s*0,y+s*1.5)#3
  hb.goto_point(x+s*0.25,y+s*1.5)#4
  hb.goto_point(x+s*0.5,y+s*1.125)#5 0.625=5/8
  hb.goto_point(x+s*0.75,y+s*1.5)#6
  hb.goto_point(x+s*1,y+s*1.5)#7
  hb.goto_point(x+s*0.625,y+s*0.75)#8
  hb.goto_point(x+s*1,y+s*0)#9
  hb.goto_point(x+s*0.75,y+s*0)#10
  hb.goto_point(x+s*0.5,y+s*0.375)#11
  hb.goto_point(x+s*0.25,y+s*0)#12
  hb.goto_point(x+s*0,y+s*0)#13
  hb.pen_up()
  

def draw_Y(hb, x, y, s,):
  hb.pen_up()
  hb.goto_point(x + s*0,   y + s*1.5) # Point 1
  hb.pen_down()
  hb.goto_point(x + s*0.25,   y + s*1.5) # Point 2
  hb.goto_point(x + s*0.5, y + s*1.1) # 3
  hb.goto_point(x + s*0.75,   y + s*1.5) #4
  hb.goto_point(x + s*1,   y + s*1.5)#5
  hb.goto_point(x + s*0.6,   y + s*0.7)#6
  hb.goto_point(x + s*0.6,   y + s*0)#7
  hb.goto_point(x + s*0.4, y + s*0)#8
  hb.goto_point(x + s*0.4,   y + s*0.7)#9
  hb.goto_point(x + s*0,   y + s*1.5)
  hb.pen_up()
  

def draw_Z(hb, x, y, s):
  hb.pen_up()
  hb.goto_point(x + s*0, y + s*0) # Point 1
  hb.pen_down()
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
  hb.pen_up()
  

def draw_Underscore(hb, x, y, s):
  hb.pen_up()
  hb.goto_point(x + s*0, y + s*0) # Point 1
  hb.pen_down()
  hb.goto_point(x + s*1, y + s*0) # Point 2
  hb.goto_point(x + s*1, y + s*0.1) # Point 3
  hb.goto_point(x + s*0, y + s*0.1) # Etc.
  hb.goto_point(x + s*0, y + s*0)
  hb.pen_up()
  

if __name__ == "__main__":
  hb = HarpBot()

  # Toggle the pen to keep the robot SAFE
  hb.pen_down()
  hb.pen_up()

  HangmanLib.draw_string(hb, 'ABCDEFG', -20, 200, 140)
  HangmanLib.draw_string(hb, 'HIJKLMN', -20, 160, 140)
  HangmanLib.draw_string(hb, 'OPQRSTU', -20, 120, 140)
  HangmanLib.draw_string(hb, 'VWXYZ _', -20, 80,  140)

  # Lift the pen up and then go home
  hb.pen_up()
  hb.go_home()
