from PyQt4 import Qt
from PyQt4.QtGui import QDialog, QSpinBox, QLabel

__author__ = 'Girish'


class PenPropertyDlg(QDialog):

    def __init__(self,parent=None):
        QDialog.__init__(self,parent)
        self.setParent(parent)
        self.widthLabel = QLabel("&Width")
        self.widthLabel.setAlignment(Qt.Qt.AlignRight)
        self.spinbox = QSpinBox(self)



