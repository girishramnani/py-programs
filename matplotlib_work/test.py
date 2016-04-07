__author__ = 'Girish'
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation


def animate(i,matrix,mat_plot):
    x_axis = np.random.randint(0,40)
    y_axis =np.random.randint(0,40)
    matrix[x_axis,y_axis] = 1
    mat_plot.set_array(matrix)
    return mat_plot


matrix = np.zeros((40,40))
matrix[20:22,23:26] =1
fig1 = plt.figure()

plt.xlabel('x')
plt.title('test')

mat_plot = plt.spy(matrix)
# matrix[1:4,1:4] =1
# mat_plot.set_array(matrix)

#
line_ani = animation.FuncAnimation(fig1, animate, range(25), fargs=(matrix,mat_plot),
    interval=50, blit=True)

plt.show()
