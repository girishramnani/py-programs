from PyQt4.QtGui import QDialog

__author__ = 'Girish'
from Qt.tree import Ui_Dialog

class Tree(QDialog ,Ui_Dialog):
    def __init__(self):
        QDialog.__init__(self)

