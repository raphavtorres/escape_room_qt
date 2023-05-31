from PyQt5 import QtCore, QtGui, QtWidgets
from escape_room import Ui_MainWindow

class MyWindow(Ui_MainWindow):
    def __init__(self, MainWindow):
        self.setupUi(MainWindow)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    # ui = Ui_MainWindow()
    # ui.setupUi(MainWindow)
    window = MyWindow(MainWindow)

    MainWindow.show()
    sys.exit(app.exec_())
