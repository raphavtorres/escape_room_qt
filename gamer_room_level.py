from PyQt5 import QtCore, QtGui, QtWidgets
from gamer_room_window import Ui_GamerRoom
from computer_screen_window import Ui_ComputerScreen


class GamerRoom(Ui_GamerRoom):
    def __init__(self, MainWindow):
        self.MainWindow = MainWindow
        self.setupUi(MainWindow)
        self.UiComponents()

    def UiComponents(self):
        self.open_pc_btn.clicked.connect(self.open_window)

    def open_window(self):
        ComputerScreen(MainWindow)
        self.MainWindow.close()
        MainWindow.show()


class ComputerScreen(Ui_ComputerScreen):
    def __init__(self, MainWindow):
        self.MainWindow = MainWindow
        self.setupUi(MainWindow)
        self.UiComponents()

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
