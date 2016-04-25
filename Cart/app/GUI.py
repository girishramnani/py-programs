from PyQt4.QtCore import Qt
from PyQt4.QtCore import QPoint
from PyQt4.QtGui import QMainWindow, QApplication, QMenu, QTextCursor, QAction

import sys
from mainWindow import Ui_MainWindow

import file_to_list as fl
class window(QMainWindow,Ui_MainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.basic_actions()
        self.MainTextArea.setContextMenuPolicy(Qt.CustomContextMenu)
        self.MainTextArea.customContextMenuRequested.connect(self.openMenu)
        self.MainTextArea.textChanged.connect(lambda :self.fetch_())

    def fetch_(self):
        self.word = self.MainTextArea.toPlainText()[-50:].rsplit(" ",maxsplit=2)[-1]

    def insert(self,word):
        def func():
            self.MainTextArea.textCursor().insertText(word[len(self.word):])
        return func

    def openMenu(self,position):
        menu = QMenu()

        if self.word=='':
            menu.addAction("Nothing Found !!")
        else:
            list_words= self.fetch_word()
            if len(list_words) != 0:
                for word in list_words :
                    act = QAction(word,menu)
                    act.triggered.connect(self.insert(word))
                    menu.addAction(act)
            else:
                menu.addAction("Nothing Found !!")
        menu.exec_(self.MainTextArea.mapToGlobal(self.location()))
        menu.show()

    def location(self):
        return QPoint(self.MainTextArea.cursorRect().x()+10,self.MainTextArea.cursorRect().y()+10)

    def fetch_word(self):
        return list(self.database.search(self.word))[:20]


    def  basic_actions(self):
        self.actionExit.triggered.connect(self.exit)
        self.database = fl.Lister()
        self.word =""

    def exit(self):
        sys.exit(0)

app = QApplication(sys.argv)
w = window()
w.show()
app.exec_()