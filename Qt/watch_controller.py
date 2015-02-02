__author__ = 'Girish'
from PyQt4.QtCore import *
from PyQt4.QtGui import *
import sys
from Qt.watch import Ui_Dialog
import datetime
import time
from threading import Timer

class working(QDialog,Ui_Dialog):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Time")
        self.setupUi(self)
        self.t = QTimer()
        self.t.timeout.connect(self.functioning)
        self.t.start(1000)

    def functioning(self):
        t = time.localtime()
        h = time.strftime("%H",t)
        m = time.strftime("%M",t)
        s = time.strftime("%S",t)
        self.hour.setProperty("value",h)
        self.second.setProperty("value",s)
        self.minute.setProperty("value",m)






import time
t =time.localtime()

app = QApplication(sys.argv)
dia =working()
dia.show()
app.exec_()



