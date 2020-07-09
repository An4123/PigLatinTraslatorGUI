# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'testModified.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(250, 400)
        MainWindow.setAutoFillBackground(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton1 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton1.setGeometry(QtCore.QRect(0, 120, 250, 125))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.pushButton1.setFont(font)
        self.pushButton1.setObjectName("pushButton1")
        self.topLabel = QtWidgets.QLabel(self.centralwidget)
        self.topLabel.setGeometry(QtCore.QRect(0, 0, 250, 125))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.topLabel.setFont(font)
        self.topLabel.setAutoFillBackground(False)
        self.topLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.topLabel.setObjectName("topLabel")
        self.topLabel_2 = QtWidgets.QLabel(self.centralwidget)
        self.topLabel_2.setGeometry(QtCore.QRect(0, 250, 250, 125))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.topLabel_2.setFont(font)
        self.topLabel_2.setAlignment(QtCore.Qt.AlignCenter)
        self.topLabel_2.setObjectName("topLabel_2")
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit.setGeometry(QtCore.QRect(85, 20, 81, 31))
        self.plainTextEdit.setObjectName("plainTextEdit")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 250, 21))
        self.menubar.setObjectName("menubar")
        self.menuFUCK_OFF = QtWidgets.QMenu(self.menubar)
        self.menuFUCK_OFF.setObjectName("menuFUCK_OFF")
        MainWindow.setMenuBar(self.menubar)
        self.menubar.addAction(self.menuFUCK_OFF.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton1.setText(_translate("MainWindow", "PUSH THIS TO TRANSLATE"))
        self.topLabel.setText(_translate("MainWindow", "Type in English"))
        self.topLabel_2.setText(_translate("MainWindow", "Translated To Pig Latin"))
        self.menuFUCK_OFF.setTitle(_translate("MainWindow", "FUCK OFF"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
