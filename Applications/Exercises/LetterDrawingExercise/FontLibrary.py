import sys
sys.path.append("../../../HarpBot")
sys.path.append("../../Hangman")

from HarpBot import HarpBot
import HangmanLib


# These constants set the aspect ratio of the letters. 
# Really, the only one that's a choice is MAX_LETTER_Y = 1.5 
# TODO: incorporate these constants into the draw_<> functions below.
MIN_LETTER_X = 0.0
MAX_LETTER_X = 1.0
MIN_LETTER_Y = 0.0
MAX_LETTER_Y = 1.5


def draw_testbox(hb, x, y, s):
    # Use this function to see if your letter is drawn the correct size! It should
    # fit perfectly fit inside the box when you use the same x,y, and s
    hb.pen_up()
    hb.goto_point(x,y)
    hb.pen_down()
    hb.goto_point(x + s, y);
    hb.goto_point(x + s, y + s*1.5)
    hb.goto_point(x, y + s*1.5)
    hb.goto_point(x, y)
    hb.pen_up()


def draw_A(hb, x, y, s):
    # x: The x-coordinate to draw the letter "A"
    # y: The y-coordinate to draw the letter "A"

    # s: The scaling factor 
    # When s = 1 the letter should be 1mm wide and 1.5mm tall
    # Realistically the 's' parameter will be a greater number, and the 
    # letters will be drawn larger. When testing your draw function, try 
    # letting s = 50 (5 centimeter x 7.5 centimeter)

    # Always start by raising the pen, so when we go to the point we want to draw the 'A'
    # we aren't dragging ink across the paper
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
    # To be written by students!
    pass

def draw_C(hb, x, y, s):
    # To be written by students!
    pass
    
def draw_D(hb, x, y, s):
    # To be written by students!
    pass

def draw_E(hb, x, y, s):
    # To be written by students!
    pass

def draw_F(hb, x, y, s):
    # To be written by students!
    pass

def draw_G(hb, x, y, s):
    # To be written by students!
    pass
    
def draw_H(hb, x, y, s):
    # To be written by students!
    pass

def draw_I(hb, x, y, s):
    # To be written by students!
    pass

def draw_J(hb, x, y, s):
    # To be written by students!
    pass

def draw_K(hb, x, y, s):
    # To be written by students!
    pass
    
def draw_L(hb, x, y, s):
    # To be written by students!
    pass

def draw_M(hb, x, y, s):
    # To be written by students!
    pass

def draw_N(hb, x, y, s):
    # To be written by students!
    pass

def draw_O(hb, x, y, s):
    # To be written by students!
    pass
    
def draw_P(hb, x, y, s):
    # To be written by students!
    pass

def draw_Q(hb, x, y, s):
    # To be written by students!
    pass

def draw_R(hb, x, y, s):
    # To be written by students!
    pass

def draw_S(hb, x, y, s):
    # To be written by students!
    pass
    
def draw_T(hb, x, y, s):
    # To be written by students!
    pass

def draw_U(hb, x, y, s):
    # To be written by students!
    pass

def draw_V(hb, x, y, s):
    # To be written by students!
    pass

def draw_W(hb, x, y, s):
    # To be written by students!
    pass
    
def draw_X(hb, x, y, s):
    # To be written by students!
    pass

def draw_Y(hb, x, y, s):
    # To be written by students!
    pass

def draw_Z(hb, x, y, s):
    # To be written by students!
    pass

def draw_Underscore(hb, x, y, s):
    # To be written by students!
    pass

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
