import math
import time

import numpy as np

import HarpPlot
import HarpBotSerial



# Robot parameters to be measured/calibrated
LINK_1_LENGTH = 160.0 # (mm)
LINK_2_LENGTH = 145.0 # (mm)

# Home position of the robot
HOME_X = LINK_1_LENGTH + LINK_2_LENGTH
HOME_Y = 0

GOTO_STEP_SIZE = 3 # (mm) The max distance that the robot will move in one step when going to a new position

# Size of paper (8.5x11)
PAPER_WIDTH = 279.4
PAPER_HEIGHT = 215.9
PAPER_X_OFFSET = -87 # How far from the robot the left edge of the paper is placed (mm)
PAPER_Y_OFFSET = 66.1 # How far in front of the robot the bottom edge of the paper is placed (mm)


# Utility functions for Forward and Inverse kinematics
def forward_kinematics(joint_angle_1, joint_angle_2):
    x0 = 0
    y0 = 0

    # To get from p0 to p1, we add the distance that link 1 gives us to 0
    x1 = x0 + LINK_1_LENGTH*math.cos(math.radians(joint_angle_1))
    y1 = y0 + LINK_1_LENGTH*math.sin(math.radians(joint_angle_1))

    # Do essentially the same thing to get to p2 from p1
    theta12 = joint_angle_1 + joint_angle_2  # Same as above except that this angle is referenced w.r.t. joint 1, so we need to add theta1 as well
    x2 = x1 + LINK_2_LENGTH*math.cos(math.radians(theta12))
    y2 = y1 + LINK_2_LENGTH*math.sin(math.radians(theta12))

    return x2, y2, x1, y1, x0, y0 # Return all of the joint positions to caller

def inverse_kinematics(x, y):
    c2 = (x**2 + y**2 - LINK_1_LENGTH**2 - LINK_2_LENGTH**2)/(2*LINK_1_LENGTH*LINK_2_LENGTH)

    # For s2, we could take positive or negative here.
    # We will take negative for "elbow up" configuration.
    s2 = -math.sqrt(1 - c2**2)

    psi2 = math.atan2(s2, c2)
    psi1 = math.atan2(y, x) - math.atan2(LINK_2_LENGTH*s2, LINK_1_LENGTH + LINK_2_LENGTH*c2)

    joint_angle_1 = math.degrees(psi1)
    joint_angle_2 = math.degrees(psi2)

    return joint_angle_1, joint_angle_2

def is_in_workspace(x, y):
    # Function to determine if a point is within the reachable workspace
    dist_from_center = math.sqrt(x**2 + y**2)

    return dist_from_center <= (LINK_1_LENGTH + LINK_2_LENGTH) and \
           dist_from_center >= (LINK_1_LENGTH - LINK_2_LENGTH)


class HarpBot:
    def __init__(self, port='COM4'):
        """
        Creates a new instance of HarpBot.

        HarpBot is a real live drawing robot that holds a pen and follows commands to draw pictures.
        If the robot is detected on port, the real robot should follow the commands.
        At any rate, this class will animate the robot moving around and drawing using MatPlotLib.
        """


        # Toggle to turn animation on/off
        self.animation_on = True
        self.animation_skip = 10 # Plot every nth frame for speed

        # Initialize robot to zero position
        self.joint_angles = [0, 0]
        self.xpos = HOME_X
        self.ypos = HOME_Y

        self.animation_skip_ctr = 0;

        self.is_pen_down = True # When pen is down, the robot will draw as it moves

        # Whether or not the physical robot is connected
        # When false, HarpBlot will only plot its motion. When True, it will issue serial
        # commands to control hardware
        self.robot_enabled = False

        # Try to initialize the HarpBotSerial object (which sends/recieves serial commands).
        # If it fails, run HarpBot in simulation only mode. If successful, just control the robot with no plot.
        self.hb_ser = HarpBotSerial.HarpBotSerial(port=port)

        # Check if connection was successful
        if self.hb_ser.connected:
            self.robot_enabled = True
            print('Robot successfully connected and enabled for HarpBot')
        else:
            print('Robot could not be enabled for HarpBot.')
        
        if self.animation_on:
            print('Animation set to on. Plotting robot movements with HarpPlot.')
            self.hp = HarpPlot.HarpPlot()
            self.robot_lines = []
            self.draw_workspace()
        else:
            print('Animation set to off. No robot simulation will occur.')
            
    def pen_up(self):
        """ Lifts the pen"""
        self.is_pen_down = False
        if self.robot_enabled:
          self.hb_ser.pen_up()

    def pen_down(self):
        """ Sets the pen down """
        self.is_pen_down = True
        if self.robot_enabled:
          self.hb_ser.pen_down()

    def draw_scene(self):
        #self.draw_workspace()
        if self.animation_skip_ctr % self.animation_skip == 0:
            self.clear_robot()
            self.draw_robot()
            self.animation_skip_ctr = 0

        self.animation_skip_ctr = self.animation_skip_ctr + 1

    def clear_robot(self):
        # Clears the line segments that we drew for the robot
        for line in self.robot_lines:
            line.pop(0).remove()
            #del line

        self.robot_lines = []

    def draw_robot(self):
        # First get the points defining where the robot is in space
        x2, y2, x1, y1, x0, y0 = forward_kinematics(self.joint_angles[0], self.joint_angles[1])
        
        # First I want to draw a little base triangle using lines and points
        triangle_size = 20
        l1 = self.hp.add_line((x0, y0),
                    (x0 + triangle_size, y0 - triangle_size),
                    line_width=2, marker_color='k', marker_size=1)
        l2 = self.hp.add_line((x0 + triangle_size, y0 - triangle_size),
                    (x0 - triangle_size, y0 - triangle_size),
                    line_width=2, marker_color='k', marker_size=1)
        l3 = self.hp.add_line((x0 - triangle_size, y0 - triangle_size),
                    (x0, y0),
                    line_width=2, marker_color='k', marker_size=1)
        l4 = self.hp.add_line((x0 - 2*triangle_size, y0 - triangle_size),
                    (x0 + 2*triangle_size, y0 - triangle_size),
                    line_width=2, marker_color='k', marker_size=1)

        # Now just draw a line segment for each of the two robot links
        l5 = self.hp.add_line((x0,y0), (x1,y1), line_color='orange', line_width=4, marker_color='red', marker_size=10)
        l6 = self.hp.add_line((x1,y1), (x2,y2), line_color='orange', line_width=4, marker_color='red', marker_size=10)

        self.hp.draw()

        # Add the line segments we drew to robot_lines
        self.robot_lines.extend([l1, l2, l3, l4, l5, l6])

    def goto_point(self, x, y):
        """
        Moves the robot to a given x,y coordinate
        """

        # First check to make sure the point is in the workspace
        if not is_in_workspace(x, y):
            # Not in the valid workspace
            print("Cannot move to out-of-range point (" + str(x) + ", " + str(y) + ")")
            return

        # Distance between the new point and the current one
        dx = x - self.xpos
        dy = y - self.ypos
        dist = math.sqrt(dx**2 + dy**2)

        if dist < GOTO_STEP_SIZE:
            # We can make it to the target point in one step
            self.set_position(x, y)
        else:
            # Compute the point in the direction that we want to go
            angle = math.atan2(dy, dx)
            next_x = self.xpos + GOTO_STEP_SIZE * math.cos(angle)
            next_y = self.ypos + GOTO_STEP_SIZE * math.sin(angle)
            self.set_position(next_x, next_y)

            # Recursively call goto_point until we get to our destination
            self.goto_point(x, y)

    def draw_rectangle(self, x1, y1, x2, y2):
        """
        Draws a rectangle bounded by the points (x1, y1) and (x2, y2)
        """
        self.pen_up()
        self.goto_point(x1, y1)
        self.pen_down()
        self.goto_point(x2, y1)
        self.goto_point(x2, y2)
        self.goto_point(x1, y2)
        self.goto_point(x1, y1)
        self.pen_up()

    def draw_circle(self, x, y, r):
        """
        Draws a circle centered at (x,y), with radius r
        """
        PI = 3.1415
        angle = 0

        # Move the pen to where the circle drawing will begin
        self.pen_up()
        self.goto_point(x + r, y) # When angle is zero, the point is just horizontal in x direction (x + r)
        self.pen_down()

        # Use 30 equally-spaced points to appear round
        num_steps = 30
        for i in range(0, num_steps):
            angle += (2*PI/num_steps)
            pt_x = x + r * math.cos(angle)
            pt_y = y + r * math.sin(angle)
            self.goto_point(pt_x, pt_y)

    def set_position(self, x, y):
        """
        Sets the position to the given x,y coordinate
        """

        if not is_in_workspace(x, y):
            print("Cannot move to out-of-range point (" + str(x) + ", " + str(y) + ")")
            return

        # If the robot is enabled, then move the robot, otherwise just do plotting
        if self.robot_enabled:
            self.hb_ser.goto(x, y)
        
        if self.animation_on:
            self.draw_scene()
            # If the pen is down, then draw a line from the previous point to the new point
            if self.is_pen_down:
                self.hp.add_line((self.xpos, self.ypos), (x,y), \
                                line_color = 'b', marker_color = 'b', marker_size=1)

        # If the point is in the accessible work space, set the position!
        self.xpos = x
        self.ypos = y

        # Compute the joint angles
        [j1, j2] = inverse_kinematics(x,y)
        self.joint_angles = [j1, j2]

    def go_home(self):
        self.pen_up()
        self.goto_point(HOME_X, HOME_Y)

    def draw_workspace(self):
        # Draw the limits of the robot
        inner_radius = LINK_1_LENGTH - LINK_2_LENGTH
        outer_radius = LINK_1_LENGTH + LINK_2_LENGTH
        self.hp.circle(0, 0, inner_radius, color='r')
        self.hp.circle(0, 0, outer_radius, color='r')

        # Draw the placement of the paper
        paper_x1 = PAPER_X_OFFSET
        paper_y1 = PAPER_Y_OFFSET
        paper_x2 = PAPER_X_OFFSET + PAPER_WIDTH
        paper_y2 = PAPER_Y_OFFSET + PAPER_HEIGHT

        self.hp.line(paper_x1, paper_y1, paper_x1, paper_y2, line_color='gray')
        self.hp.line(paper_x1, paper_y1, paper_x2, paper_y1, line_color='gray')
        self.hp.line(paper_x2, paper_y2, paper_x1, paper_y2, line_color='gray')
        self.hp.line(paper_x2, paper_y2, paper_x2, paper_y1, line_color='gray')

        self.hp.draw()


if __name__ == "__main__":
    bot = HarpBot()

    bot.pen_down()
    bot.pen_up()
    bot.goto_point(100, 100)
    bot.pen_down()
    bot.goto_point(100, 200)
    bot.goto_point(0, 200)
    bot.goto_point(0, 100)
    bot.goto_point(100, 100)
    bot.pen_up()
    bot.go_home()
