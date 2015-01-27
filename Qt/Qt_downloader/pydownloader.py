from PyQt4.QtGui import QApplication
from PyQt4.QtGui import QDialog
from PyQt4.QtGui import QLineEdit
from PyQt4.QtGui import QProgressBar
from PyQt4.QtGui import QPushButton
from PyQt4.QtGui import QVBoxLayout

__author__ = 'Girish'
import sys

class Py_downloader(QDialog):
    def __init__(self):
        super().__init__()

        layout = QVBoxLayout()



        Url = QLineEdit()
        save_location  = QLineEdit()
        progress = QProgressBar()
        button  = QPushButton("Download")

        layout.addWidget(Url)
        layout.addWidget(save_location)
        layout.addWidget(progress)
        layout.addWidget(button)

        self.layout(layout)







app = QApplication(sys.argv)
main_window = Py_downloader()
main_window.show()
app.exec_()