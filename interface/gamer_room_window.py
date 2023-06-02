# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gamer_room_window.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(600, 600)
        MainWindow.setMinimumSize(QtCore.QSize(600, 600))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 600, 600))
        self.label.setMinimumSize(QtCore.QSize(600, 600))
        self.label.setMaximumSize(QtCore.QSize(600, 600))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("../images/gamer_room_img.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.open_pc_btn = QtWidgets.QPushButton(self.centralwidget)
        self.open_pc_btn.setGeometry(QtCore.QRect(200, 250, 91, 81))
        self.open_pc_btn.setStyleSheet("background-color: rgba(0,0,0,0);")
        self.open_pc_btn.setText("")
        self.open_pc_btn.setObjectName("open_pc_btn")
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
