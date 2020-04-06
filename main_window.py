# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '1.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from add_remove import Ui_Form
from inquire_buttons import Inquire_Buttons


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(640, 266)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.inquire_Pbutton = QtWidgets.QPushButton(self.centralwidget)
        self.inquire_Pbutton.setGeometry(QtCore.QRect(0, 0, 311, 271))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold SemiConden")
        font.setPointSize(36)
        font.setBold(True)
        font.setWeight(75)
        self.inquire_Pbutton.setFont(font)
        self.inquire_Pbutton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.inquire_Pbutton.setAutoFillBackground(False)
        self.inquire_Pbutton.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0.392045 rgba(255, 90, 0, 255), stop:1 rgba(160, 0, 0, 255));")
        self.inquire_Pbutton.setObjectName("inquire_Pbutton")
        self.AddRemove_Pbutton = QtWidgets.QPushButton(self.centralwidget)
        self.AddRemove_Pbutton.setGeometry(QtCore.QRect(310, 0, 331, 271))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold SemiConden")
        font.setPointSize(36)
        font.setBold(True)
        font.setWeight(75)
        self.AddRemove_Pbutton.setFont(font)
        self.AddRemove_Pbutton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.AddRemove_Pbutton.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0.0511364 rgba(61, 61, 91, 255), stop:0.528409 rgba(0, 133, 218, 255));")
        self.AddRemove_Pbutton.setObjectName("AddRemove_Pbutton")
        MainWindow.setCentralWidget(self.centralwidget)

        self.AddRemove_Pbutton.clicked.connect(self.conn_AddRemove)
        self.inquire_Pbutton.clicked.connect(self.conn_Iquire)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", 'MainWindow --Developed by "Ahmed Hawater" (hawatercoding@gmail.com)'))
        self.inquire_Pbutton.setText(_translate("MainWindow", "Inquire"))
        self.AddRemove_Pbutton.setText(_translate("MainWindow", "Add/Remove"))

    def conn_AddRemove(self):
        self.form = QtWidgets.QWidget()
        self.ui =Ui_Form()
        self.ui.setupUi(self.form)
        self.form.show()
    
    def conn_Iquire(self):
        self.form = QtWidgets.QWidget()
        self.ui = Inquire_Buttons()
        self.ui.setupUi(self.form)
        self.form.show()



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    MainWindow.setFixedSize(640,266)
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
