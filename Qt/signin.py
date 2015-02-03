# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'signin.ui'
#
# Created: Tue Feb  3 21:20:51 2015
#      by: PyQt4 UI code generator 4.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(316, 241)
        Dialog.setStyleSheet(_fromUtf8("QLineEdit:focus {\n"
"border-color: blue;\n"
"\n"
"\n"
"}\n"
"\n"
""))
        self.frame = QtGui.QFrame(Dialog)
        self.frame.setGeometry(QtCore.QRect(0, 0, 401, 51))
        self.frame.setStyleSheet(_fromUtf8("\n"
"QFrame{\n"
"    background-color: qlineargradient(spread:pad, x1:0.511, y1:0.607955, x2:0.494, y2:0, stop:0 rgba(189, 233, 255, 218), stop:1 rgba(255, 255, 255, 255));\n"
"\n"
"}\n"
"QToolButton {\n"
"background-color:transparent;\n"
"border:none;\n"
"border-radius:10%;\n"
"}\n"
"QToolButton:checked, QToolButton:pressed{\n"
"    background-color: rgb(0, 85, 255);\n"
"\n"
"}\n"
"QToolButton:hover{\n"
"background-color:rgb(224,232,246);\n"
"}\n"
"QToolButton:checked:hover{\n"
"background-color:rgb(193,210,238);}"))
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.facebook = QtGui.QToolButton(self.frame)
        self.facebook.setGeometry(QtCore.QRect(30, 10, 41, 31))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/index.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.facebook.setIcon(icon)
        self.facebook.setIconSize(QtCore.QSize(32, 32))
        self.facebook.setCheckable(True)
        self.facebook.setAutoExclusive(True)
        self.facebook.setObjectName(_fromUtf8("facebook"))
        self.twitter = QtGui.QToolButton(self.frame)
        self.twitter.setGeometry(QtCore.QRect(140, 10, 41, 31))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(":/index1.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.twitter.setIcon(icon1)
        self.twitter.setIconSize(QtCore.QSize(32, 32))
        self.twitter.setCheckable(True)
        self.twitter.setAutoExclusive(True)
        self.twitter.setObjectName(_fromUtf8("twitter"))
        self.google = QtGui.QToolButton(self.frame)
        self.google.setGeometry(QtCore.QRect(240, 10, 41, 31))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8(":/index2.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.google.setIcon(icon2)
        self.google.setIconSize(QtCore.QSize(32, 32))
        self.google.setCheckable(True)
        self.google.setChecked(False)
        self.google.setAutoExclusive(True)
        self.google.setAutoRaise(False)
        self.google.setObjectName(_fromUtf8("google"))
        self.lineEdit = QtGui.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(100, 80, 151, 20))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.lineEdit_2 = QtGui.QLineEdit(Dialog)
        self.lineEdit_2.setGeometry(QtCore.QRect(100, 130, 151, 20))
        self.lineEdit_2.setEchoMode(QtGui.QLineEdit.Password)
        self.lineEdit_2.setObjectName(_fromUtf8("lineEdit_2"))
        self.progressBar = QtGui.QProgressBar(Dialog)
        self.progressBar.setGeometry(QtCore.QRect(20, 190, 171, 21))
        self.progressBar.setStyleSheet(_fromUtf8("QProgressBar {\n"
"text-align:center;\n"
"}"))
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName(_fromUtf8("progressBar"))
        self.pushButton = QtGui.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(220, 190, 75, 23))
        self.pushButton.setStyleSheet(_fromUtf8("QPushButton {\n"
"background-color:rgb(0, 85, 230);\n"
"color:rgb(255, 255, 255);\n"
"    font: 11pt;\n"
"border:1px solid transparent;\n"
"border-radius:4px;\n"
"\n"
"}"))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.label = QtGui.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(30, 80, 51, 20))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(30, 130, 46, 13))
        self.label_2.setObjectName(_fromUtf8("label_2"))

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
        self.facebook.setText(_translate("Dialog", "Facebook", None))
        self.twitter.setText(_translate("Dialog", "Twitter", None))
        self.google.setText(_translate("Dialog", "Google+", None))
        self.pushButton.setText(_translate("Dialog", "Log In", None))
        self.label.setText(_translate("Dialog", "Username", None))
        self.label_2.setText(_translate("Dialog", "Password", None))

import Qt.girish_rc

