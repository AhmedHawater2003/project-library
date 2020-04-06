# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '4.ui'
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

class Show_Books(object):

    def show_Asearsh(self):
        Library.showing_table(self,
f"""SELECT book_id, title, version, publishing_date, name, book.author_id
FROM book
JOIN author
	on book.author_id = author.author_id
where book.author_id = {self.authorId_input.text()}
ORDER BY title""",

f"""SELECT count(*)
FROM book
JOIN author
        on book.author_id = author.author_id
WHERE book.author_id = {self.authorId_input.text()}
ORDER BY title""")
        self.authorId_input.setText("")

    
    def show_all(self):
        Library.showing_table(self,
f"""SELECT book_id, title, version, publishing_date, name, book.author_id
FROM book
JOIN author
	on book.author_id = author.author_id
ORDER BY title""",

f"""SELECT count(*)
FROM book
JOIN author
        on book.author_id = author.author_id
ORDER BY title""")


    def show_Bsearsh(self):
        Library.showing_table(self,
f"""SELECT book_id, title, version, publishing_date, name, book.author_id
FROM book
JOIN author
	on book.author_id = author.author_id
where title = '{self.bookID_input.text()}' 
ORDER BY title""",

f"""SELECT count(*)
FROM book
JOIN author
        on book.author_id = author.author_id
WHERE title = '{self.bookID_input.text()}' 
ORDER BY title""")
        self.bookID_input.setText("")

        

    def setupUi(self, Form):
        Form.setMaximumSize(900, 514)
        Form.setObjectName("Form")
        Form.resize(900, 514)
        Form.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.tableWidget = QtWidgets.QTableWidget(Form)
        self.tableWidget.setGeometry(QtCore.QRect(0, 0, 901, 441))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.tableWidget.setFont(font)
        self.tableWidget.setStyleSheet("alternate-background-color: rgba(194, 32, 0, 180);\n"
"background-color: rgba(255, 90, 0, 200);\n"
"")
        self.tableWidget.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.tableWidget.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.tableWidget.setLineWidth(1)
        self.tableWidget.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.tableWidget.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.tableWidget.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContentsOnFirstShow)
        self.tableWidget.setAutoScroll(True)
        self.tableWidget.setAutoScrollMargin(16)
        self.tableWidget.setDragEnabled(True)
        self.tableWidget.setAlternatingRowColors(True)
        self.tableWidget.setIconSize(QtCore.QSize(0, 0))
        self.tableWidget.setShowGrid(True)
        self.tableWidget.setCornerButtonEnabled(True)
        self.tableWidget.setRowCount(0)
        self.tableWidget.setColumnCount(6)
        self.tableWidget.setObjectName("tableWidget")
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        font = QtGui.QFont()
        font.setFamily("MV Boli")
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(False)
        item.setFont(font)
        item.setBackground(QtGui.QColor(255, 255, 255))
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        item.setForeground(brush)
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("MV Boli")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        item.setBackground(QtGui.QColor(255, 255, 255))
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
        font.setPointSize(12)
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
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("MV Boli")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(5, item)
        self.tableWidget.horizontalHeader().setVisible(True)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(True)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(150)
        self.tableWidget.horizontalHeader().setSortIndicatorShown(True)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.verticalHeader().setVisible(False)
        self.tableWidget.verticalHeader().setCascadingSectionResizes(True)
        self.tableWidget.verticalHeader().setHighlightSections(True)
        self.tableWidget.verticalHeader().setSortIndicatorShown(False)
        self.tableWidget.verticalHeader().setStretchLastSection(False)
        self.buttos_frame = QtWidgets.QFrame(Form)
        self.buttos_frame.setGeometry(QtCore.QRect(-10, 440, 911, 81))
        self.buttos_frame.setStyleSheet("background-color: rgba(255, 100, 0, 200);")
        self.buttos_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.buttos_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.buttos_frame.setLineWidth(1)
        self.buttos_frame.setObjectName("buttos_frame")
        self.authorId_input = QtWidgets.QLineEdit(self.buttos_frame)
        self.authorId_input.setGeometry(QtCore.QRect(765, 22, 133, 20))
        self.authorId_input.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-style: outset;\n"
"border-width: 2px;\n"
"border-radius: 5px;\n"
"border-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0.392045 rgba(255, 90, 0, 255), stop:1 rgba(160, 0, 0, 255));\n"
"min-width: 6em;\n"
"padding: 2px\n"
"")
        self.authorId_input.setObjectName("authorId_input")
        self.authorID_searsh = QtWidgets.QPushButton(self.buttos_frame)
        self.authorID_searsh.setGeometry(QtCore.QRect(810, 45, 86, 23))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold SemiConden")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.authorID_searsh.setFont(font)
        self.authorID_searsh.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.authorID_searsh.setStyleSheet("background-color: rgba(212, 64, 22, 255);\n"
"border-style: outset;\n"
"border-width: 2px;\n"
"border-radius: 5px;\n"
"min-width: 6em;\n"
"padding: 2px;\n"
"border-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0.392045 rgba(255, 90, 0, 255), stop:1 rgba(160, 0, 0, 255));")
        self.authorID_searsh.setObjectName("authorID_searsh")
        self.bookID_searsh = QtWidgets.QPushButton(self.buttos_frame)
        self.bookID_searsh.setGeometry(QtCore.QRect(21, 45, 86, 23))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold SemiConden")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.bookID_searsh.setFont(font)
        self.bookID_searsh.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.bookID_searsh.setStyleSheet("background-color: rgba(212, 64, 22, 255);\n"
"border-style: outset;\n"
"border-width: 2px;\n"
"border-radius: 5px;\n"
"border-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0.392045 rgba(255, 90, 0, 255), stop:1 rgba(160, 0, 0, 255));\n"
"min-width: 6em;\n"
"padding: 2px")
        self.bookID_searsh.setObjectName("bookID_searsh")
        self.bookID_input = QtWidgets.QLineEdit(self.buttos_frame)
        self.bookID_input.setGeometry(QtCore.QRect(20, 22, 133, 20))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.bookID_input.setFont(font)
        self.bookID_input.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.bookID_input.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-style: outset;\n"
"border-width: 2px;\n"
"border-radius: 5px;\n"
"border-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0.392045 rgba(255, 90, 0, 255), stop:1 rgba(160, 0, 0, 255));\n"
"min-width: 6em;\n"
"padding: 2px")
        self.bookID_input.setText("")
        self.bookID_input.setObjectName("bookID_input")
        self.bokkID_label = QtWidgets.QLabel(self.buttos_frame)
        self.bokkID_label.setGeometry(QtCore.QRect(21, 5, 100, 16))
        self.bokkID_label.setStyleSheet("background-color: rgba(255, 100, 0, 10);\n"
"font: 11pt \"MV Boli\";")
        self.bokkID_label.setObjectName("bokkID_label")
        self.authorID_label = QtWidgets.QLabel(self.buttos_frame)
        self.authorID_label.setGeometry(QtCore.QRect(810, 5, 91, 16))
        self.authorID_label.setStyleSheet("background-color: rgba(255, 100, 0, 10);\n"
"font: 11pt \"MV Boli\";\n"
"")
        self.authorID_label.setObjectName("authorID_label")
        self.reset = QtWidgets.QPushButton(self.buttos_frame)
        self.reset.setGeometry(QtCore.QRect(400, 45, 86, 23))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold SemiConden")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.reset.setFont(font)
        self.reset.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.reset.setStyleSheet("background-color: rgba(212, 64, 22, 255);\n"
"border-style: outset;\n"
"border-width: 2px;\n"
"border-radius: 5px;\n"
"min-width: 6em;\n"
"padding: 2px;\n"
"border-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0.392045 rgba(255, 90, 0, 255), stop:1 rgba(160, 0, 0, 255));")
        self.reset.setObjectName("reset")
        self.show_all()

        self.reset.clicked.connect(self.show_all)
        self.authorID_searsh.clicked.connect(self.show_Asearsh)
        self.bookID_searsh.clicked.connect(self.show_Bsearsh)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.tableWidget.setSortingEnabled(True)
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Form", "Book ID"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Form", "Title"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Form", "Version"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("Form", "Publishing Date"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("Form", "Author Name"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("Form", "Author ID"))
        self.authorID_searsh.setText(_translate("Form", "Searsh"))
        self.bookID_searsh.setText(_translate("Form", "Searsh"))
        self.bokkID_label.setText(_translate("Form", "Book Title :"))
        self.authorID_label.setText(_translate("Form", ": Author ID"))
        self.reset.setText(_translate("Form", "ReSet"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    
    ui = Show_Books()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
