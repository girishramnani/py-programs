from PyQt4.QtGui import QDialog, QApplication

__author__ = 'Girish'



from Qt import signin

class View(QDialog,signin.Ui_Dialog):
    def __init__(self):
        QDialog.__init__(self)
        self.setupUi(self)
import sys
app = QApplication(sys.argv)
dialog = View()
dialog.show()
app.exec_()