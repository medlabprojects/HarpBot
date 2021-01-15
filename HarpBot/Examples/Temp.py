import math


L1 = 170 # mm
L2 = 150 # mm


def f(theta1, theta2):
  theta1 = math.radians(theta1)
  theta2 = math.radians(theta2)
  
  x = L1*math.cos(theta1) + L2*math.cos(theta1 + theta2)
  y = L1*math.sin(theta1) + L2*math.sin(theta1 + theta2)
  return x, y


x, y = f(30, -45)
print('x = ', x, 'y = ', y)