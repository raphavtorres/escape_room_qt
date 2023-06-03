from PyQt5 import QtCore, QtGui, QtWidgets
from computer_screen_window import Ui_ComputerScreen
from gamer_room_level import GamerRoom


class ComputerScreen(Ui_ComputerScreen):
    def __init__(self, MainWindow):
        self.setupUi(MainWindow)

    def UiComponents(self):
        self.back_to_room_btn.clicked.connect(self.open_window)

    def open_window(self):
        GamerRoom(MainWindow)
        self.MainWindow.close()
        MainWindow.show()    


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow() 
    window = GamerRoom(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
