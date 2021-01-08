import matplotlib.pyplot as plt
import numpy as np


X_AXIS_LIM_LO = -210
X_AXIS_LIM_HI = 210
Y_AXIS_LIM_LO = -210
Y_AXIS_LIM_HI = 210

FIG_SIZE_X = 6
FIG_SIZE_Y = 6


class HarpPlot:
    def __init__(self):
        self.fig, self.ax = plt.subplots(figsize=(FIG_SIZE_X, FIG_SIZE_Y))
        self.reset_figure()

        
    def reset_figure(self):
        self.ax.clear()
        
        self.ax.set(xlabel='x (mm)', ylabel='y (mm)', title='HarpPlot')
        self.ax.grid()
        
        plt.autoscale(False)
        plt.xlim(X_AXIS_LIM_LO, X_AXIS_LIM_HI)
        plt.ylim(Y_AXIS_LIM_LO, Y_AXIS_LIM_HI)
        
    def add_line(self, p1, p2, line_color='k', line_width=1, marker_color='r', marker_size=5):
        return self.ax.plot((p1[0], p2[0]), (p1[1], p2[1]), '-o', color=line_color, linewidth=line_width, markersize=marker_size, markeredgecolor=marker_color, markerfacecolor=marker_color)
      
    def add_point(self, x, y, color='k', size=5):
        return self.ax.plot(x, y, 'o', linestyle='None', markersize=size, markeredgecolor=color, markerfacecolor=color)
        
    def draw(self):
        plt.draw()
        plt.pause(1e-6)

    def show(self):
        plt.show()

    # Wrapper functions for ease-of-use
    def point(self, x, y, color='k', size=5):
        return self.add_point(x, y, color, size)

    def line(self, x1, y1, x2, y2, line_color='k', line_width=1, marker_color='r', marker_size=5):
        return self.add_line([x1, y1], [x2, y2], line_color, line_width, marker_color, marker_size)

    def circle(self, center_x, center_y, radius, color='k'):
        circ = plt.Circle((center_x, center_y), radius, color=color, fill=False)
        return self.ax.add_artist(circ)

def plot_random_pts():
    hp = HarpPlot()
      
    x = np.arange(-3,4)
    y = np.arange(-3,4)
      
    for xi in x:
        for yi in y:
            color = np.random.random((1,3)).flatten()
            hp.add_point(xi, yi, color=color)
            hp.draw()
      
  
if __name__ == "__main__":
  plot_random_pts()
