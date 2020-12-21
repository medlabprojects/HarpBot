import matplotlib.pyplot as plt
import numpy as np
import time


class HarpPlot:
  def __init__(self):
    self.fig, self.ax = plt.subplots(figsize=(6, 6))
    self.reset_figure()
    
  def reset_figure(self):
    self.ax.clear()
    
    self.ax.set(xlabel='x (mm)', ylabel='y (mm)',
                title='HarpPlot')
    self.ax.grid()
    
    plt.autoscale(False)
    plt.xlim(-3, 3)
    plt.ylim(-3, 3)
    
  def add_line(self, p1, p2, line_color='k', line_width=1, marker_color='r', marker_size=5):
    self.ax.plot((p1[0], p2[0]), (p1[1], p2[1]), '-o', color=line_color, linewidth=line_width, markersize=marker_size, markeredgecolor=marker_color, markerfacecolor=marker_color)
  
  def add_point(self, x, y, color=(0.0, 0.0, 0.0), size=5):
    self.ax.plot(x, y, 'o', linestyle='None', markersize=size, markeredgecolor=color, markerfacecolor=color)
    
  def draw(self):
    plt.draw()
    plt.pause(1e-6)

  def show(self):
    plt.show()
    

def plot_random_pts():
  hp = HarpPlot()
  
  x = np.arange(-3,4)
  y = np.arange(-3,4)
  
  for xi in x:
    for yi in y:
      color = np.random.random((1,3)).flatten()
      hp.add_point(xi, yi, color=color)
      hp.draw()
  
  
def draw_robot(q1, q2, hp):
  x0 = 0
  y0 = 0
  
  x1 = x0 + np.cos(q1)
  y1 = y0 + np.sin(q1)
  
  x2 = x1 + 0.75*np.cos(q2)
  y2 = y1 + 0.75*np.sin(q2)
    
  hp.add_line((x0,y0), (x1,y1), line_color='k', line_width=1, marker_color='r', marker_size=5)
  hp.add_line((x1,y1), (x2,y2), line_color='k', line_width=1, marker_color='r', marker_size=5)
  
  return (x2, y2)

def animate_robot():
  hp = HarpPlot()
  
  t_max = 10
  t0 = time.time()
  
  pts = None
  
  while(True):
    hp.reset_figure()
    t = time.time()
    
    q1 = t;
    q2 = -2*t;
    
    pt = draw_robot(q1, q2, hp)
    
    if pts is None:
      pts = pt
    else:
      pts = np.vstack((pts, pt))
      hp.add_point(pts[:,0], pts[:,1])
    
    hp.draw()
    
    if (t - t0) > t_max:
      break
  
  
if __name__ == "__main__":
  plot_random_pts()
  animate_robot()
  