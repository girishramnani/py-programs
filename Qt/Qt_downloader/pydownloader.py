from PyQt4.QtGui.QApplication import QApplication
from PyQt4.QtGui.QDialog import QDialog

__author__ = 'Girish'


class Py_downloader(QDialog):
    def __init__(self):
        super().__init__()
    





app = QApplication()
main_window = Py_downloader()
main_window.show()
app.exec_()