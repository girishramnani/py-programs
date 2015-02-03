from PyQt4.QtGui import QTreeWidget, QTreeWidgetItem

__author__ = 'Girish'


class DirTree(QTreeWidget):
    def __init__(self,master):
        QTreeWidget.__init__(self,master)


        t =QTreeWidgetItem(self,"grisih")
        t.addChild(QTreeWidgetItem("ramnani"))

