# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '5.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QTableWidget, QTableWidgetItem
import sqlite3
from library_class import Library
conn = sqlite3.connect("library.db")
c = conn.cursor()


class Show_Authors(object):

    def show_all(self):
        Library.showing_table(self,"SELECT * FROM author ORDER BY name", "SELECT COUNT(*) FROM author ORDER BY name")

    def showAsearsh(self):
        Library.showing_table(self, f"SELECT * FROM author WHERE name = '{self.authorName_input.text()}' ORDER BY name ",
        f"SELECT COUNT(*) FROM author WHERE name = '{self.authorName_input.text()}' ORDER BY name ")

    def setupUi(self, Form):
        Form.setMaximumSize(900, 514)
        Form.setObjectName("Form")
        Form.resize(898, 514)
        Form.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.tableWidget = QtWidgets.QTableWidget(Form)
        self.tableWidget.setGeometry(QtCore.QRect(0, 0, 901, 441))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setBold(True)
        font.setWeight(75)
        self.tableWidget.setFont(font)
        self.tableWidget.setStyleSheet("alternate-background-color:rgb(255, 139, 75);\n"
"background-color:rgb(212, 64, 22, 255);\n"
"")
        self.tableWidget.setAlternatingRowColors(True)
        self.tableWidget.setRowCount(0)
        self.tableWidget.setColumnCount(5)
        self.tableWidget.setObjectName("tableWidget")
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("MV Boli")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("MV Boli")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("MV Boli")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("MV Boli")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("MV Boli")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(4, item)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(180)
        self.tableWidget.horizontalHeader().setMinimumSectionSize(39)
        self.tableWidget.horizontalHeader().setSortIndicatorShown(True)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.verticalHeader().setVisible(False)
        self.tableWidget.verticalHeader().setDefaultSectionSize(30)
        self.tableWidget.verticalHeader().setMinimumSectionSize(23)
        self.tableWidget.verticalHeader().setSortIndicatorShown(False)
        self.tableWidget.verticalHeader().setStretchLastSection(False)
        self.buttons_frame = QtWidgets.QFrame(Form)
        self.buttons_frame.setGeometry(QtCore.QRect(-10, 440, 911, 81))
        self.buttons_frame.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.buttons_frame.setStyleSheet("background-color: rgba(212, 64, 22, 255);")
        self.buttons_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.buttons_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.buttons_frame.setObjectName("buttons_frame")
        self.reset = QtWidgets.QPushButton(self.buttons_frame)
        self.reset.setGeometry(QtCore.QRect(400, 45, 86, 22))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold SemiConden")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.reset.setFont(font)
        self.reset.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.reset.setStyleSheet("border-style: outset;\n"
"background-color: rgb(255, 139, 75);\n"
"border-width: 2px;\n"
"border-radius: 5px;\n"
"min-width: 6em;\n"
"padding: 2px;\n"
"border-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0.392045 rgba(255, 90, 0, 255), stop:1 rgba(160, 0, 0, 255));")
        self.reset.setObjectName("reset")
        self.authorName_label = QtWidgets.QLabel(self.buttons_frame)
        self.authorName_label.setGeometry(QtCore.QRect(21, 3, 131, 20))
        font = QtGui.QFont()
        font.setFamily("MV Boli")
        font.setPointSize(11)
        self.authorName_label.setFont(font)
        self.authorName_label.setStyleSheet("background-color: rgba(221, 105, 72, 10);")
        self.authorName_label.setObjectName("authorName_label")
        self.authorName_label.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.authorName_searsh = QtWidgets.QPushButton(self.buttons_frame)
        self.authorName_searsh.setGeometry(QtCore.QRect(21, 45, 86, 23))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold SemiConden")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.authorName_searsh.setFont(font)
        self.authorName_searsh.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.authorName_searsh.setAutoFillBackground(False)
        self.authorName_searsh.setStyleSheet("border-style: outset;\n"
"background-color: rgb(255, 139, 75);\n"
"border-width: 2px;\n"
"border-radius: 5px;\n"
"min-width: 6em;\n"
"padding: 2px;\n"
"border-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0.392045 rgba(255, 90, 0, 255), stop:1 rgba(160, 0, 0, 255));")
        self.authorName_searsh.setObjectName("authorName_searsh")
        self.authorName_input = QtWidgets.QLineEdit(self.buttons_frame)
        self.authorName_input.setGeometry(QtCore.QRect(20, 22, 113, 20))
        self.authorName_input.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-style: outset;\n"
"border-width: 2px;\n"
"border-radius: 5px;\n"
"border-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0.392045 rgba(255, 90, 0, 255), stop:1 rgba(160, 0, 0, 255));\n"
"min-width: 6em;\n"
"padding: 2px")
        self.authorName_input.setObjectName("authorName_input")
        self.show_all()

        self.reset.clicked.connect(self.show_all)
        self.authorName_searsh.clicked.connect(self.showAsearsh)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Form", "Author ID"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Form", "Name"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Form", "Phone"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("Form", "Email"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("Form", "Nationality"))
        self.reset.setText(_translate("Form", "ReSet"))
        self.authorName_label.setText(_translate("Form", "Author Name :"))
        self.authorName_searsh.setText(_translate("Form", "Searsh"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Show_Authors()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
