from PyQt4.QtGui import QDialog, QHBoxLayout, QSpinBox, QDial, QApplication, QPushButton

__author__ = 'Girish'

class Form(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        layout =QHBoxLayout()
        self.spin = QSpinBox()
        self.dial =QDial()
        self.dial.setNotchesVisible(True)


        layout.addWidget(self.dial)
        layout.addWidget(self.spin)

        self.setLayout(layout)
        self.dial.valueChanged.connect(self.spin.setValue)
        self.spin.valueChanged.connect(self.dial.setValue)
        self.setWindowTitle("signals")

    """one of the ways to get data from the signal"""
    # def clicked(self):
    #     button = self.sender()
    #     if button is None or not isinstance(button, QPushButton):
    #          return
    #     self.label.setText("You clicked button '%s'" % button.text())


import sys
app =QApplication(sys.argv)
fp = Form()
fp.show()
app.exec_()
