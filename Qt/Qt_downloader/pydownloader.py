from PyQt4.QtGui.QApplication import QApplication
from PyQt4.QtGui.QDialog import QDialog
from PyQt4.QtGui.QLineEdit import QLineEdit
from PyQt4.QtGui.QProgressBar import QProgressBar
from PyQt4.QtGui.QPushButton import QPushButton
from PyQt4.QtGui.QVBoxLayout import QVBoxLayout

__author__ = 'Girish'


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






app = QApplication()
main_window = Py_downloader()
main_window.show()
app.exec_()