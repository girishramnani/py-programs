__author__ = 'Girish'

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import pprint

def life(X):

    def roll(x,y):
        return np.roll(np.roll(X,y,axis=0),x,axis=1)


    while True:
        Y = roll(0,1)+roll(1,0)+roll(-1,0)+roll(0,-1)+roll(1,1)+roll(-1,1)+roll(-1,-1)+roll(1,-1)

        X = np.logical_or(np.logical_and(X,Y ==2),Y==3)
        X =  X.astype(int)
        yield X

matrix = np.zeros((40,40))
matrix[24,21:33] = 1
matrix[25,22] =1

def simPoints(inputmat):
    mat_plot.set_array(inputmat)
    return mat_plot

# ##
# ##   set up figure for plotting:
# ##
fig = plt.figure()
ax = fig.add_subplot(111)
mat_plot = plt.spy(matrix)

# I'm still unfamiliar with the following line of code:
##


time_template = 'Time = %.1f s'    # prints running simulation time
time_text = ax.text(0.05, 0.9, '', transform=ax.transAxes)
## Now call the animation package: (simData is the user function
## serving as the argument for simPoints):
ani = animation.FuncAnimation(fig, simPoints, lambda : life(matrix), blit=False,\
     interval=50, repeat=True)
plt.show()