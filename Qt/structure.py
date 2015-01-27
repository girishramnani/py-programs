__author__ = 'Girish'
'''not bad as all the elements start with Q , so no namespace conflict'''
from PyQt4.QtCore import *
from PyQt4.QtGui import *
import sys

app = QApplication(sys.argv)
dialog = QDialog()
dialog.show()
app.exec_()
