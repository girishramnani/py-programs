


from PyQt4.QtCore import *
from PyQt4.QtGui import *
import sys

class HelloWorld(QDialog):
    def __init__(self):
        super().__init__()
        layout = QGridLayout()


        self.label = QLabel("hello world")
        line_edit = QLineEdit()
        button = QPushButton("close")

        layout.addWidget(self.label,0,0)
        layout.addWidget(line_edit,0,1)
        layout.addWidget(button,1,1)

        self.setLayout(layout)
        button.clicked.connect(self.close)

        # more addition

        line_edit.textChanged.connect(self.changeTextLabel)

    def changeTextLabel(self,text):
        self.label.setText(text)

app  =QApplication(sys.argv)
dialog = HelloWorld()
dialog.show()
app.exec_()

