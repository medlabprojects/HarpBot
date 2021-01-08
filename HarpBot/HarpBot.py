import math
import time

import numpy as np

import HarpPlot


# Robot parameters to be measured/calibrated
BASE_X_OFFSET = -10.0 # (mm), x distance from the world frame to the robot base
BASE_Y_OFFSET = -10.0 # (mm), y distance from the world frame to the robot base
JOINT_1_OFFSET = 0.0 # (deg), angular offset for joint 1, gets added to q1 in kinematics
JOINT_2_OFFSET = 0.0 # (deg), angular offset for joint 2, gets added to q2 in kinematics
LINK_1_LENGTH = 120.0 # (mm)
LINK_2_LENGTH = 60.0 # (mm)

GOTO_STEP_SIZE = 25 # (mm) The max distance that the robot will move in one step when going to a new position

# Size of paper (8.5x11)
PAPER_WIDTH = 279.4
PAPER_HEIGHT = 215.9
PAPER_Y_OFFSET = 10 # How far in front of the robot the bottom edge of the paper is placed (mm)


# Utility functions for Forward and Inverse kinematics
def forward_kinematics(joint_angle_1, joint_angle_2):
    # The base of the robot p0 is at the default position
    x0 = BASE_X_OFFSET
    y0 = BASE_Y_OFFSET
    
    # To get from p0 to p1, we add the distance that link 1 gives us to p0
    theta1 = joint_angle_1 + JOINT_1_OFFSET # Add the variable angle to the measured motor offset
    x1 = x0 + LINK_1_LENGTH*math.cos(math.radians(theta1))
    y1 = y0 + LINK_1_LENGTH*math.sin(math.radians(theta1))
    
    # Do essentially the same thing to get to p2 from p1
    theta2 = theta1 + joint_angle_2 + JOINT_2_OFFSET # Same as above except that this angle is referenced w.r.t. joint 1, so we need to add theta1 as well
    x2 = x1 + LINK_2_LENGTH*math.cos(math.radians(theta2))
    y2 = y1 + LINK_2_LENGTH*math.sin(math.radians(theta2))
    
    return x2, y2, x1, y1, x0, y0 # Return all of the joint positions to caller

def inverse_kinematics(x, y):
    x1 = x - BASE_X_OFFSET
    y1 = y - BASE_Y_OFFSET
    
    c2 = (x1**2 + y1**2 - LINK_1_LENGTH**2 - LINK_2_LENGTH**2)/(2*LINK_1_LENGTH*LINK_2_LENGTH)
    
    # For s2, we could take positive or negative here.
    # We will take positive for "elbow down" configuration.
    s2 = math.sqrt(1 - c2**2) 
    
    psi2 = math.atan2(s2, c2)
    psi1 = math.atan2(y1, x1) - math.atan2(LINK_2_LENGTH*s2, LINK_1_LENGTH + LINK_2_LENGTH*c2)
    
    joint_angle_1 = math.degrees(psi1 - JOINT_1_OFFSET)
    joint_angle_2 = math.degrees(psi2 - JOINT_2_OFFSET)
    
    return joint_angle_1, joint_angle_2

def is_in_workspace(x, y):
    # Function to determine if a point is within the reachable workspace
    dist_from_center = math.sqrt(x**2 + y**2)

    return dist_from_center <= (LINK_1_LENGTH + LINK_2_LENGTH) and \
           dist_from_center >= (LINK_1_LENGTH - LINK_2_LENGTH)



class HarpBot:

    # The speed at which the robot can move (m/s)
    

    def __init__(self):
        """
        Creates a new instance of HarpBot
        """

        # Initialize robot to zero position
        self.joint_angles = [0, 0]

        # Position of the pen
        [px, py, _, _, _, _] = forward_kinematics(self.joint_angles[0], self.joint_angles[1])
        self.xpos = px
        self.ypos = py
    
        # Initialize a HarpPlot instance
        self.hp = HarpPlot.HarpPlot()

        self.is_pen_down = True # When pen is down, the robot will draw as it moves

        # Whether or not the physical robot is connected
        # When false, HarpBlot will only plot its motion. When True, it will issue serial
        # commands to control hardware
        self.robot_enabled = False

        # The lines used to draw the robot arm
        self.robot_lines = []


    def attach_robot(self):
        """
        Call this function to tell HarpBot that it is connected to actual robot hardware
        """
        self.robot_enabled = True

    def send_serial_command(self):
        """
        Sends the robot's current configuration to the Arduino over serial.
        """
        # TODO
        # Variables to use: self.xpos, self.ypos, self.joint_angles
        pass

    def pen_up(self):
        """ Lifts the pen"""
        self.is_pen_down = False

    def pen_down(self):
        """ Sets the pen down """
        self.is_pen_down = True


    
    def draw_scene(self):
        self.draw_workspace()
        self.clear_robot()
        self.draw_robot()

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
        
        # Fist check to make sure the point is in the workspace
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
        
        

    def set_position(self, x, y):
        """
        Sets the position to the given x,y coordinate
        """

        if is_in_workspace(x, y):

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

            

            self.draw_scene()

            if self.robot_enabled:
                self.send_serial_command()
        else:
            # Not in the valid workspace
            print("Cannot move to out-of-range point (" + str(x) + ", " + str(y) + ")")


    def animate_robot():        
        t_max = 5
        t0 = time.time()
        
        pts = None
        
        while(True):
            hp.reset_figure()
            t = time.time()
            
            q1 = math.degrees(t)
            q2 = -3*math.degrees(t)
            
            pt = draw_robot(q1, q2, hp)
            
            if pts is None:
                pts = pt
            else:
                pts = np.vstack((pts, pt))
                hp.add_point(pts[:,0], pts[:,1], color='blue', size=3)
            
            hp.draw()
            
            if (t - t0) > t_max:
                break
      
    def draw_workspace(self):

        # Draw the limits of the robot
        inner_radius = LINK_1_LENGTH - LINK_2_LENGTH
        outer_radius = LINK_1_LENGTH + LINK_2_LENGTH
        self.hp.circle(0, 0, inner_radius, color='r')
        self.hp.circle(0, 0, outer_radius, color='r')

        # Draw the placement of the paper
        paper_x1 = -PAPER_WIDTH / 2
        paper_y1 = PAPER_Y_OFFSET
        paper_x2 = PAPER_WIDTH / 2
        paper_y2 = PAPER_Y_OFFSET + PAPER_HEIGHT

        self.hp.line(paper_x1, paper_y1, paper_x1, paper_y2, line_color='gray')
        self.hp.line(paper_x1, paper_y1, paper_x2, paper_y1, line_color='gray')
        self.hp.line(paper_x2, paper_y2, paper_x1, paper_y2, line_color='gray')
        self.hp.line(paper_x2, paper_y2, paper_x2, paper_y1, line_color='gray')

        self.hp.draw()


if __name__ == "__main__":
    bot = HarpBot()
    bot.draw_workspace()

    bot.pen_up()
    bot.goto_point(100, 80)
    bot.pen_down()
    bot.goto_point(-100, 80)
    bot.goto_point(-100, 130)
    bot.goto_point(100, 130)
    bot.goto_point(100, 80)
    bot.pen_up()
    bot.goto_point(-100, 80)
    bot.goto_point(-180, 0)
