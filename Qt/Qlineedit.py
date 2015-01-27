__author__ = 'Girish'
from PyQt4.QtCore import *
from PyQt4.QtGui import *
import sys
class demo(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QWidgets demo")
        line_edit = QLineEdit()
        close = QPushButton("close")
        close.clicked.connect(self.close)
        layout = QVBoxLayout()
        layout.addWidget(line_edit)
        layout.addWidget(close)
        self.setLayout(layout)

        self.setFocus()



app = QApplication(sys.argv)
dialog = demo()
dialog.show()
app.exec_()