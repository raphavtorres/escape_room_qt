from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(600, 600)
        MainWindow.setMinimumSize(QtCore.QSize(600, 600))
        MainWindow.setMaximumSize(QtCore.QSize(600, 600))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.background_lb = QtWidgets.QLabel(self.centralwidget)
        self.background_lb.setGeometry(QtCore.QRect(0, 0, 600, 600))
        self.background_lb.setMinimumSize(QtCore.QSize(600, 600))
        self.background_lb.setMaximumSize(QtCore.QSize(600, 600))
        self.background_lb.setText("")
        self.background_lb.setPixmap(QtGui.QPixmap(":/background/futuristic_plants_room_img.webp"))
        self.background_lb.setScaledContents(True)
        self.background_lb.setObjectName("background_lb")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
