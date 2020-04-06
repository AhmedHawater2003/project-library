# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '2.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
from library_class import Library


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(604, 436)
        Form.setStyleSheet("background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 107, 182, 255)) ")
        self.gridLayout = QtWidgets.QGridLayout(Form)
        self.gridLayout.setObjectName("gridLayout")
        self.add_book = QtWidgets.QGroupBox(Form)
        font = QtGui.QFont()
        font.setFamily("MV Boli")
        font.setPointSize(18)
        self.add_book.setFont(font)
        self.add_book.setAutoFillBackground(False)
        self.add_book.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:1 rgba(0, 174, 255, 128));\n"
"color: rgb(255, 255, 255);")
        self.add_book.setObjectName("add_book")
        self.formLayout_4 = QtWidgets.QFormLayout(self.add_book)
        self.formLayout_4.setObjectName("formLayout_4")
        self.title_label = QtWidgets.QLabel(self.add_book)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.title_label.setFont(font)
        self.title_label.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:1 rgba(0, 174, 255, 0));\n"
"color: black;")
        self.title_label.setObjectName("title_label")
        self.formLayout_4.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.title_label)
        self.title_input = QtWidgets.QLineEdit(self.add_book)
        self.title_input.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);\n"
"    border-style: outset;\n"
"    border-width: 2px;\n"
"    border-radius: 10px;\n"
"min-width:20em;\n"
"border-color: white\n"
" ")
        self.title_input.setObjectName("title_input")
        self.formLayout_4.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.title_input)
        self.version_label = QtWidgets.QLabel(self.add_book)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.version_label.setFont(font)
        self.version_label.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:1 rgba(0, 174, 255, 0));\n"
"color: black;")
        self.version_label.setObjectName("version_label")
        self.formLayout_4.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.version_label)
        self.version_input = QtWidgets.QLineEdit(self.add_book)
        self.version_input.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);\n"
"    border-style: outset;\n"
"    border-width: 2px;\n"
"    border-radius: 10px;\n"
"min-width:20em;\n"
"border-color: white\n"
" ")
        self.version_input.setObjectName("version_input")
        self.formLayout_4.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.version_input)
        self.PB_label = QtWidgets.QLabel(self.add_book)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.PB_label.setFont(font)
        self.PB_label.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:1 rgba(0, 174, 255, 0));\n"
"color: black;")
        self.PB_label.setObjectName("PB_label")
        self.formLayout_4.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.PB_label)
        self.PB_input = QtWidgets.QLineEdit(self.add_book)
        self.PB_input.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);\n"
"    border-style: outset;\n"
"    border-width: 2px;\n"
"    border-radius: 10px;\n"
"min-width:20em;\n"
"border-color: white\n"
" ")
        self.PB_input.setObjectName("PB_input")
        self.formLayout_4.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.PB_input)
        self.AN_label = QtWidgets.QLabel(self.add_book)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.AN_label.setFont(font)
        self.AN_label.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:1 rgba(0, 174, 255, 0));\n"
"color: black;")
        self.AN_label.setObjectName("AN_label")
        self.formLayout_4.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.AN_label)
        self.Aid_input = QtWidgets.QLineEdit(self.add_book)
        self.Aid_input.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);\n"
"    border-style: outset;\n"
"    border-width: 2px;\n"
"    border-radius: 10px;\n"
"min-width:20em;\n"
"border-color: white\n"
" ")
        self.Aid_input.setObjectName("AN_input")
        self.formLayout_4.setWidget(7, QtWidgets.QFormLayout.LabelRole, self.Aid_input)
        self.addBook_submit = QtWidgets.QPushButton(self.add_book)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Black")
        font.setPointSize(8)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(10)
        self.addBook_submit.setFont(font)
        self.addBook_submit.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.addBook_submit.setStyleSheet("background-color: white;\n"
"border-style: outset;\n"
"border-width: 2px;\n"
"border-radius: 10px;\n"
"border-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 90, 153, 255));\n"
"min-width: 6em;\n"
"padding: 2px;\n"
"color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 62, 106, 255));\n"
"font: 87 8pt \"Segoe UI Black\";")
        self.addBook_submit.setFlat(False)
        self.addBook_submit.setObjectName("addBook_submit")
        self.formLayout_4.setWidget(8, QtWidgets.QFormLayout.LabelRole, self.addBook_submit)
        self.gridLayout.addWidget(self.add_book, 0, 0, 1, 1)
        self.groupBox_2 = QtWidgets.QGroupBox(Form)
        font = QtGui.QFont()
        font.setFamily("MV Boli")
        font.setPointSize(18)
        self.groupBox_2.setFont(font)
        self.groupBox_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.groupBox_2.setAutoFillBackground(False)
        self.groupBox_2.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:1 rgba(0, 174, 255, 128));\n"
"color: rgb(255, 255, 255);")
        self.groupBox_2.setObjectName("groupBox_2")
        self.formLayout_3 = QtWidgets.QFormLayout(self.groupBox_2)
        self.formLayout_3.setObjectName("formLayout_3")
        self.name_label = QtWidgets.QLabel(self.groupBox_2)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.name_label.setFont(font)
        self.name_label.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:1 rgba(0, 174, 255, 0));\n"
"color: black;")
        self.name_label.setObjectName("name_label")
        self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.name_label)
        self.name_input = QtWidgets.QLineEdit(self.groupBox_2)
        self.name_input.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);\n"
"    border-style: outset;\n"
"    border-width: 2px;\n"
"    border-radius: 10px;\n"
"min-width:20em;\n"
"border-color: white\n"
" ")
        self.name_input.setObjectName("name_input")
        self.formLayout_3.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.name_input)
        self.phone_label = QtWidgets.QLabel(self.groupBox_2)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.phone_label.setFont(font)
        self.phone_label.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:1 rgba(0, 174, 255, 0));\n"
"color: black;")
        self.phone_label.setObjectName("phone_label")
        self.formLayout_3.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.phone_label)
        self.phone_input = QtWidgets.QLineEdit(self.groupBox_2)
        self.phone_input.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);\n"
"    border-style: outset;\n"
"    border-width: 2px;\n"
"    border-radius: 10px;\n"
"min-width:20em;\n"
"border-color: white\n"
" ")
        self.phone_input.setObjectName("phone_input")
        self.formLayout_3.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.phone_input)
        self.email_label = QtWidgets.QLabel(self.groupBox_2)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.email_label.setFont(font)
        self.email_label.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:1 rgba(0, 174, 255, 0));\n"
"color: black;")
        self.email_label.setObjectName("email_label")
        self.formLayout_3.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.email_label)
        self.email_input = QtWidgets.QLineEdit(self.groupBox_2)
        self.email_input.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);\n"
"    border-style: outset;\n"
"    border-width: 2px;\n"
"    border-radius: 10px;\n"
"min-width:20em;\n"
"border-color: white\n"
" ")
        self.email_input.setObjectName("email_input")
        self.formLayout_3.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.email_input)
        self.addAuthor_submit = QtWidgets.QPushButton(self.groupBox_2)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Black")
        font.setPointSize(8)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(10)
        self.addAuthor_submit.setFont(font)
        self.addAuthor_submit.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.addAuthor_submit.setStyleSheet("background-color: white;\n"
"border-style: outset;\n"
"border-width: 2px;\n"
"border-radius: 10px;\n"
"border-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 90, 153, 255));\n"
"min-width: 6em;\n"
"padding: 2px;\n"
"color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 62, 106, 255));\n"
"font: 87 8pt \"Segoe UI Black\";")
        self.addAuthor_submit.setFlat(False)
        self.addAuthor_submit.setObjectName("addAuthor_submit")
        self.formLayout_3.setWidget(8, QtWidgets.QFormLayout.LabelRole, self.addAuthor_submit)
        self.nationality_input = QtWidgets.QLineEdit(self.groupBox_2)
        self.nationality_input.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);\n"
"    border-style: outset;\n"
"    border-width: 2px;\n"
"    border-radius: 10px;\n"
"min-width:20em;\n"
"border-color: white\n"
" ")
        self.nationality_input.setObjectName("nationality_input")
        self.formLayout_3.setWidget(7, QtWidgets.QFormLayout.LabelRole, self.nationality_input)
        self.nationality_label = QtWidgets.QLabel(self.groupBox_2)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.nationality_label.setFont(font)
        self.nationality_label.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:1 rgba(0, 174, 255, 0));\n"
"color: black;")
        self.nationality_label.setObjectName("nationality_label")
        self.formLayout_3.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.nationality_label)
        self.gridLayout.addWidget(self.groupBox_2, 0, 1, 1, 1)
        self.groupBox_3 = QtWidgets.QGroupBox(Form)
        font = QtGui.QFont()
        font.setFamily("MV Boli")
        font.setPointSize(18)
        self.groupBox_3.setFont(font)
        self.groupBox_3.setAutoFillBackground(False)
        self.groupBox_3.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:1 rgba(0, 174, 255, 128));\n"
"color: rgb(255, 255, 255);")
        self.groupBox_3.setObjectName("groupBox_3")
        self.formLayout = QtWidgets.QFormLayout(self.groupBox_3)
        self.formLayout.setObjectName("formLayout")
        self.bookID_label = QtWidgets.QLabel(self.groupBox_3)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.bookID_label.setFont(font)
        self.bookID_label.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:1 rgba(0, 174, 255, 0));\n"
"color: rgb(0, 0, 0);")
        self.bookID_label.setObjectName("bookID_label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.bookID_label)
        self.bookID_input = QtWidgets.QLineEdit(self.groupBox_3)
        self.bookID_input.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);\n"
"    border-style: outset;\n"
"    border-width: 2px;\n"
"    border-radius: 10px;\n"
"min-width:20em;\n"
"border-color: white\n"
" ")
        self.bookID_input.setObjectName("bookID_input")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.bookID_input)
        self.removeBook_submit = QtWidgets.QPushButton(self.groupBox_3)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Black")
        font.setPointSize(8)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(10)
        self.removeBook_submit.setFont(font)
        self.removeBook_submit.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.removeBook_submit.setStyleSheet("background-color: white;\n"
"border-style: outset;\n"
"border-width: 2px;\n"
"border-radius: 10px;\n"
"border-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 90, 153, 255));\n"
"min-width: 6em;\n"
"padding: 2px;\n"
"color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 62, 106, 255));\n"
"font: 87 8pt \"Segoe UI Black\";")
        self.removeBook_submit.setFlat(False)
        self.removeBook_submit.setObjectName("removeBook_submit")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.removeBook_submit)
        self.gridLayout.addWidget(self.groupBox_3, 1, 0, 1, 1)
        self.groupBox_4 = QtWidgets.QGroupBox(Form)
        font = QtGui.QFont()
        font.setFamily("MV Boli")
        font.setPointSize(18)
        font.setBold(False)
        font.setWeight(50)
        self.groupBox_4.setFont(font)
        self.groupBox_4.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.groupBox_4.setAutoFillBackground(False)
        self.groupBox_4.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:1 rgba(0, 174, 255, 128));\n"
"color: rgb(255, 255, 255);")
        self.groupBox_4.setObjectName("groupBox_4")
        self.formLayout_2 = QtWidgets.QFormLayout(self.groupBox_4)
        self.formLayout_2.setObjectName("formLayout_2")
        self.authorID_label = QtWidgets.QLabel(self.groupBox_4)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.authorID_label.setFont(font)
        self.authorID_label.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:1 rgba(0, 174, 255, 0));\n"
"color: rgb(0, 0, 0);")
        self.authorID_label.setObjectName("authorID_label")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.authorID_label)
        self.authorID_input = QtWidgets.QLineEdit(self.groupBox_4)
        self.authorID_input.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);\n"
"    border-style: outset;\n"
"    border-width: 2px;\n"
"    border-radius: 10px;\n"
"min-width:20em;\n"
"border-color: white\n"
" ")
        self.authorID_input.setObjectName("authorID_input")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.authorID_input)
        self.removeAutor_submit = QtWidgets.QPushButton(self.groupBox_4)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Black")
        font.setPointSize(8)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(10)
        self.removeAutor_submit.setFont(font)
        self.removeAutor_submit.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.removeAutor_submit.setStyleSheet("background-color: white;\n"
"border-style: outset;\n"
"border-width: 2px;\n"
"border-radius: 10px;\n"
"border-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 90, 153, 255));\n"
"min-width: 6em;\n"
"padding: 2px;\n"
"color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 62, 106, 255));\n"
"font: 87 8pt \"Segoe UI Black\";")
        self.removeAutor_submit.setFlat(False)
        self.removeAutor_submit.setObjectName("removeAutor_submit")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.removeAutor_submit)
        self.gridLayout.addWidget(self.groupBox_4, 1, 1, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        Form.setTabOrder(self.title_input, self.version_input)
        Form.setTabOrder(self.version_input, self.PB_input)
        Form.setTabOrder(self.PB_input, self.Aid_input)
        Form.setTabOrder(self.Aid_input, self.addBook_submit)
        Form.setTabOrder(self.addBook_submit, self.name_input)
        Form.setTabOrder(self.name_input, self.phone_input)
        Form.setTabOrder(self.phone_input, self.email_input)
        Form.setTabOrder(self.email_input, self.nationality_input)
        Form.setTabOrder(self.nationality_input, self.addAuthor_submit)
        Form.setTabOrder(self.addAuthor_submit, self.bookID_input)
        Form.setTabOrder(self.bookID_input, self.removeBook_submit)
        Form.setTabOrder(self.removeBook_submit, self.authorID_input)
        Form.setTabOrder(self.authorID_input, self.removeAutor_submit)

        self.addAuthor_submit.clicked.connect(self.add_author_submittting)
        self.addBook_submit.clicked.connect(self.add_book_submitting)
        self.removeAutor_submit.clicked.connect(self.remove_author_submitting)
        self.removeBook_submit.clicked.connect(self.remove_book_submitting)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.add_book.setTitle(_translate("Form", "Add Book"))
        self.title_label.setText(_translate("Form", "Title :"))
        self.version_label.setText(_translate("Form", "Version :"))
        self.PB_label.setText(_translate("Form", "Publishing Date (dd-mm-yyyy) :"))
        self.AN_label.setText(_translate("Form", "Author ID : "))
        self.addBook_submit.setText(_translate("Form", "Submit"))
        self.groupBox_2.setTitle(_translate("Form", "Add Author"))
        self.name_label.setText(_translate("Form", "Name :"))
        self.phone_label.setText(_translate("Form", "Phone :"))
        self.email_label.setText(_translate("Form", "Email :"))
        self.addAuthor_submit.setText(_translate("Form", "Submit"))
        self.nationality_label.setText(_translate("Form", "Nationality :"))
        self.groupBox_3.setTitle(_translate("Form", "Remove Book"))
        self.bookID_label.setText(_translate("Form", "Book ID :"))
        self.removeBook_submit.setText(_translate("Form", "Submit"))
        self.groupBox_4.setTitle(_translate("Form", "Remove Author"))
        self.authorID_label.setText(_translate("Form", "Author ID :"))
        self.removeAutor_submit.setText(_translate("Form", "Submit"))

    def show_pop(self):
        msg = QMessageBox()
        msg.setWindowTitle("Unfinshied Form")
        msg.setText("Please, Complete teh form's data before submitting!")
        msg.setIcon(QMessageBox.Information)
        msg.exec_()

    def add_author_submittting(self):
        name = self.name_input.text()
        phone = self.phone_input.text()
        email = self.email_input.text()
        nationality = self.nationality_input.text() 
        test = Library()
        if name=='' or phone=='' or email=='':
                self.name_input.setText("")
                self.phone_input.setText("")
                self.email_input.setText("")
                self.nationality_input.setText("")
                self.show_pop()

        else:
                test.add_author(name, phone, email, nationality)
                self.name_input.setText("")
                self.phone_input.setText("")
                self.email_input.setText("")
                self.nationality_input.setText("")

    def add_book_submitting(self):
        title = self.title_input.text()
        PB = self.PB_input.text()
        version = self.version_input.text()
        author_ID = self.Aid_input.text()
        test = Library()
        if title=='' or PB =='' or version=='' or author_ID=='':
                self.title_input.setText("")
                self.PB_input.setText("")
                self.version_input.setText("")
                self.Aid_input.setText("")
                self.show_pop()

        else:
                test.add_book(title,PB, version, author_ID)
                self.title_input.setText("")
                self.PB_input.setText("")
                self.version_input.setText("")
                self.Aid_input.setText("")

    def remove_author_submitting(self):
        if self.authorID_input.text() == "":
                pass
        else:
                author_ID = self.authorID_input.text()
                test = Library()
                test.remove_author(author_ID)
                self.authorID_input.setText('')

    def remove_book_submitting(self):
        if self.bookID_input.text() == "":
                pass
        else:
                book_ID = self.bookID_input.text()
                test = Library()
                test.remove_book(book_ID)
                self.bookID_input.setText('')




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
