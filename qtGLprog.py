import OpenGL
from OpenGL.GLU import *
from OpenGL.GL import *
from PyQt4 import QtGui
import sys

class TestWindow(QtGui.QMainWindow):
    def __init__(self):
        super(TestWindow, self).__init__()
        # initialize the GL widget
        self.widget = QtGui.GLPlotWidget()
        # [...] (set data for the OpenGL widget)
        # put the window at the screen position (100, 100)
        self.setGeometry(100, 100, self.widget.width, self.widget.height)
        self.setCentralWidget(self.widget)
        self.show()

# create the Qt App and window
app = QtGui.QApplication(sys.argv)
window = TestWindow()
window.show()
app.exec_()
