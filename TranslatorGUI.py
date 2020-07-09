from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import PigLatinProgram

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(250, 400)
        MainWindow.setAutoFillBackground(True)
        # MainWindow.setStyleSheet("background-color: white;")
        MainWindow.setWindowIcon(QtGui.QIcon('logo.png'))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.pushButton1 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton1.setStyleSheet("background-color: red; ")
        self.pushButton1.setFont(font)
        self.pushButton1.setGeometry(QtCore.QRect(0, 120, 250, 125))
        self.pushButton1.setObjectName("pushButton1")
        self.pushButton1.clicked.connect(self.printTextFromBox)

        self.topLabel1 = QtWidgets.QLabel(self.centralwidget)
        self.topLabel1.setFont(font)
        self.topLabel1.setGeometry(QtCore.QRect(0, 0, 250, 125))
        self.topLabel1.setAlignment(QtCore.Qt.AlignCenter)
        self.topLabel1.setObjectName("topLabel")

        self.bottomLabel1 = QtWidgets.QLabel(self.centralwidget)
        self.bottomLabel1.setFont(font)
        self.bottomLabel1.setGeometry(QtCore.QRect(0, 250, 250, 125))
        self.bottomLabel1.setAlignment(QtCore.Qt.AlignCenter)
        self.bottomLabel1.setObjectName("bottomLabel1")

        self.plainTextEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.plainTextEdit.setGeometry(QtCore.QRect(85, 20, 81, 31))
        self.plainTextEdit.setObjectName("plainTextEdit")

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 250, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        MainWindow.setMenuBar(self.menubar)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Pig Latin"))
        self.pushButton1.setText(_translate("MainWindow", "PUSH THIS TO TRANSLATE"))
        self.topLabel1.setText(_translate("MainWindow", "Type in English"))
        self.bottomLabel1.setText(_translate("MainWindow", "Translated To Pig Latin"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))

    def printTextFromBox(self):
        textFromBox = self.plainTextEdit.text()
        self.bottomLabel1.setText(PigLatinProgram.pigLatin(textFromBox))


def main():
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

main()
