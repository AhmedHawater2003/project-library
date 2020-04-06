# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '3.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QTableWidget, QTableWidgetItem
import sqlite3
from show_books import Show_Books
from show_authors import Show_Authors
conn = sqlite3.connect("library.db")
c = conn.cursor()


class Inquire_Buttons(object):

    def setupUi(self, Form):
        Form.setFixedSize(583, 164)
        Form.setObjectName("Form")
        Form.resize(583, 164)
        Form.setStyleSheet("background-color:white")
        self.show_books = QtWidgets.QPushButton(Form)
        self.show_books.setGeometry(QtCore.QRect(0, 0, 281, 161))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(31)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.show_books.setFont(font)
        self.show_books.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.show_books.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0.661017 rgba(255, 80, 0, 255), stop:1 rgba(255, 132, 18, 255));\n"
"color: black;\n")
        self.show_books.setObjectName("show_books")
        self.show_authors = QtWidgets.QPushButton(Form)
        self.show_authors.setGeometry(QtCore.QRect(280, 0, 301, 161))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(31)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.show_authors.setFont(font)
        self.show_authors.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.show_authors.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0.661017 rgba(188, 25, 0, 255), stop:1 rgba(220, 44, 0, 255));\n"
"color:black;\n")
        self.show_authors.setObjectName("show_authors")

        self.show_books.clicked.connect(self.mama)
        self.show_authors.clicked.connect(self.papa)
        
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.show_books.setText(_translate("Form", "Show Books"))
        self.show_authors.setText(_translate("Form", "Show Authors"))

    def mama(self):
        self.form = QtWidgets.QWidget()
        self.ui =Show_Books()
        self.ui.setupUi(self.form)
        self.form.show()

    def papa(self):
        self.form = QtWidgets.QWidget()
        self.ui = Show_Authors()
        self.ui.setupUi(self.form)
        self.form.show()

        


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Inquire_Buttons()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
