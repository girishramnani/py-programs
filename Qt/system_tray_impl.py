from PyQt4.QtCore import QTimer

__author__ = 'Girish'
import shelve
from PyQt4.QtGui import QIcon, QSystemTrayIcon, QApplication

__author__ = 'girish'
import requests
from bs4 import BeautifulSoup as Soup

import os
import sys

class Message_display:
    def __init__(self):
        self.t =QApplication(sys.argv)
        icon = QIcon("jBli3.png")
        self.tray = QSystemTrayIcon(icon)

        self.tray.show()
        self.tray.showMessage("Downloading","sdf")

    def show_message(self,download):
        def show():
            self.tray.showMessage("Downloading",download)
        return show
    def exec_(self):
        self.t.exec_()



