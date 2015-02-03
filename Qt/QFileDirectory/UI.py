from PyQt4.QtGui import QDialog, QVBoxLayout, QApplication

__author__ = 'Girish'

from Qt.QFileDirectory.Tree import DirTree

class FileDirectory(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        self.qvb = QVBoxLayout()
        work =DirTree(self)
        self.qvb.addWidget(work)
        self.resize(400,400)
        self.show()

import sys

t = QApplication(sys.argv)
app = FileDirectory()
t.exec_()

