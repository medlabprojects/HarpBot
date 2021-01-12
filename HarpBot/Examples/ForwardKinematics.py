import math


# Example 1 ##############################
def f1(theta):
  L = 1
  x = L*math.cos(math.radians(theta))
  y = L*math.sin(math.radians(theta))
  
  return x, y

# Example 2 #############################
def f2(l):
  theta = 30
  x = l*math.cos(math.radians(theta))
  y = l*math.sin(math.radians(theta))
  
  return x, y

# Example 3 ##################
def f3(theta1, theta2):
  L1 = 3
  L2 = 2
  
  x1 = L1*math.cos(math.radians(theta1))
  y1 = L1*math.sin(math.radians(theta1))
  
  x = x1 + L2*math.cos(math.radians(theta1 + theta2))
  y = y1 + L2*math.sin(math.radians(theta1 + theta2))
  
  return x, y


def print_xy(x, y):
  print('x = {:.2f}'.format(x), ' and ', 'y = {:.2f}'.format(y))
  

# Example 1
x, y = f1(30)
print_xy(x, y)


# Example 2
x, y = f2(4)
print_xy(x, y)


# Example 3, HarpBot kinematics
x, y = f3(45, 30)
print_xy(x, y)
