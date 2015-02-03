from PyQt4.QtGui import QDialog, QApplication, QPixmap, QIcon, QSystemTrayIcon, QMenu, QAction
from PyQt4.QtGui import QSplashScreen

__author__ = 'Girish'


from Qt import signin

class View(QDialog,signin.Ui_Dialog):
    def __init__(self):
        QDialog.__init__(self)
        self.setupUi(self)
        systry = QIcon("jBli3.png")
        systry_icon = QSystemTrayIcon(systry,self)
        menu =QMenu()
        restore  = QAction("Restore",self)

        close = QAction("Close",self)
        menu.addAction(restore)
        menu.addAction(close)
        systry_icon.setContextMenu(menu)

        systry_icon.show()
        systry_icon.showMessage("heyo","Hello")
        close.triggered.connect(self.close)

import sys
app = QApplication(sys.argv)
dialog = View()
dialog.show()

'''for splash'''
# splash_image = QPixmap()
# splash =QSplashScreen(splash_image)
# splash.finish(dialog)
app.exec_()