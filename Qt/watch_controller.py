__author__ = 'Girish'
from PyQt4.QtCore import *
from PyQt4.QtGui import *
import sys
from Qt.watch import Ui_Dialog
import datetime
import time

class working(QDialog,Ui_Dialog):
    def __init__(self):

        super().__init__()
        self.setWindowTitle("Time")
        self.setupUi(self)
        self.functioning()
    def functioning(self):

        t = time.localtime()
        w = time.strftime("%H %M",t)

        



import time
t =time.localtime()

app = QApplication(sys.argv)
dia =working()
dia.show()
app.exec_()



