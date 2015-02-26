from PyQt4.QtGui import QDialog, QTextBrowser, QVBoxLayout, QLineEdit, QApplication
from itertools import  permutations as pr
__author__ = 'Girish'
class port:
        def __init__(self,view):
            self.view = view
        def write(self,*args):
            print(args)
            self.view.append(args[0])
class evaluator(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        self.text_browser = QTextBrowser()
        layout= QVBoxLayout()
        self.line_edit = QLineEdit()

        layout.addWidget(self.line_edit)
        layout.addWidget(self.text_browser)
        self.line_edit.returnPressed.connect(self.evaluate)
        self.setLayout(layout)


    def evaluate(self):
        text =self.line_edit.text()

        import sys
        temp = sys.stdout
        p =port(self.text_browser)
        sys.stdout = p
        t = eval(text)
        self.text_browser.append("<b> {} </b>".format(t if t!=None else ""))
        self.line_edit.setText("")
import sys
app = QApplication(sys.argv)
t = evaluator()
t.show()
app.exec_()



