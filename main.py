from PyQt5 import QtCore, QtGui, QtWidgets
from python.escape_room import Ui_MainWindow

class MyWindow(Ui_MainWindow):
    def __init__(self, MainWindow):
        self.setupUi(MainWindow)


stylesheet = """
    MainWindow {
        background-image: url("C:\\Users\\ct67ca\\Desktop\\escape_room_qt\\teste.jpg");
        background-repeat: no-repeat; 
        background-position: center;
    }
"""


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    app.setStyleSheet(stylesheet)
    MainWindow = QtWidgets.QMainWindow()
    # ui = Ui_MainWindow()
    # ui.setupUi(MainWindow)
    window = MyWindow(MainWindow)

    MainWindow.show()
    sys.exit(app.exec_())
