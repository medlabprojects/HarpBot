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
  

def draw_robot(joint_angle_1, joint_angle_2, hp):
  # First get the points defining where the robot is in space
  x2, y2, x1, y1, x0, y0 = forward_kinematics(joint_angle_1, joint_angle_2)
  
  # First I want to draw a little base triangle using lines and points
  triangle_size = 20
  hp.add_line((x0, y0), 
              (x0 + triangle_size, y0 - triangle_size), 
              line_width=2, marker_color='k', marker_size=1)
  hp.add_line((x0 + triangle_size, y0 - triangle_size), 
              (x0 - triangle_size, y0 - triangle_size), 
              line_width=2, marker_color='k', marker_size=1)
  hp.add_line((x0 - triangle_size, y0 - triangle_size), 
              (x0, y0), 
              line_width=2, marker_color='k', marker_size=1)
  hp.add_line((x0 - 2*triangle_size, y0 - triangle_size), 
              (x0 + 2*triangle_size, y0 - triangle_size), 
              line_width=2, marker_color='k', marker_size=1)
              
  # Now just draw a line segment for each of the two robot links
  hp.add_line((x0,y0), (x1,y1), line_color='orange', line_width=4, marker_color='red', marker_size=10)
  hp.add_line((x1,y1), (x2,y2), line_color='orange', line_width=4, marker_color='red', marker_size=10)
  
  return (x2, y2) # Return the tip of the robot for drawing action


def animate_robot():
  hp = HarpPlot.HarpPlot()
  
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
  

def analyze_workspace():
  hp = HarpPlot.HarpPlot()
  
  
  pts = None
  
  q1 = np.arange(0, 360, 10)
  q2 = q1
  
  for q1i in q1:
    for q2i in q2:
      hp.reset_figure()
      pt = draw_robot(q1i, q2i, hp)
    
      if pts is None:
        pts = pt
      else:
        pts = np.vstack((pts, pt))
        hp.add_point(pts[:,0], pts[:,1], color='blue', size=3)
      
      hp.draw()


if __name__ == "__main__":
  q1 = 10
  q2 = 20
  
  x, y, _, _, _, _ = forward_kinematics(10, 20)
  q1_ik, q2_ik = inverse_kinematics(x, y)
 
  
  assert (abs(q1_ik - q1) < 1e-6 and abs(q2_ik - q2) < 1e-6), "Inverse kinematics no worky"
  
  animate_robot()
  
  analyze_workspace()
  