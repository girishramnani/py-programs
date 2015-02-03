from PyQt4.QtGui import QDialog, QApplication, QPixmap
from PyQt4.QtGui import QSplashScreen

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
'''for splash'''
# splash_image = QPixmap()
# splash =QSplashScreen(splash_image)
# splash.finish(dialog)
app.exec_()