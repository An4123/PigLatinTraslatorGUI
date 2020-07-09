
from PyQt5 import QtCore, QtGui, QtWidgets
import sys


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(250,250)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.pushButton1 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton1.setGeometry(QtCore.QRect(0, 110, 331, 151))
        self.pushButton1.setObjectName("pushButton1")
        self.pushButton1.clicked.connect(self.clickButton)
        self.topLabel = QtWidgets.QLabel(self.centralwidget)
        self.topLabel.setGeometry(QtCore.QRect(90, 30, 131, 41))
        self.topLabel.setObjectName("topLabel")

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 331, 21))
        self.menubar.setObjectName("menubar")

        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton1.setText(_translate("MainWindow", "PUSH THIS"))
        self.topLabel.setText(_translate("MainWindow", "    CLICK THE BUTTON"))

    def clickButton(self):
        self.topLabel.setText("FUCK YOU DUDE")

def window():
    app = QtWidgets.QApplication(sys.argv)
    win = QtWidgets.QMainWindow()
    win.setGeometry(200,200,200,300)
    win.setWindowTitle("TEST GUI")

    ui = Ui_MainWindow()
    ui.setupUi(win)

    win.show()
    sys.exit(app.exec_())


window()
