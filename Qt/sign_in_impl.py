from PyQt4.QtCore import Qt
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
        self.progressBar.setContextMenuPolicy(Qt.CustomContextMenu)
        self.progressBar.customContextMenuRequested.connect(self.showContextMenu)

        systry_icon.show()
        systry_icon.showMessage("heyo","Hello",QSystemTrayIcon.Warning)
        close.triggered.connect(self.close)
    def showContextMenu(self,position):
        menu =QMenu(self)
        reset = QAction("reset",self)
        menu.addAction(reset)
        reset.triggered.connect(self.progressBar.reset)
        menu.popup(self.progressBar.mapToGlobal(position))

import sys
app = QApplication(sys.argv)
dialog = View()
dialog.show()

'''for splash'''
# splash_image = QPixmap()
# splash =QSplashScreen(splash_image)
# splash.finish(dialog)
app.exec_()