from PyQt5 import QtCore, QtGui, QtWidgets
from gamer_room_window import Ui_GamerRoom
from computer_screen_window import Ui_ComputerScreen


class GamerRoom(Ui_GamerRoom):
    def __init__(self, MainWindow):
        super().__init__()
        self.MainWindow = MainWindow
        self.setupUi(MainWindow)
        self.MainWindow.show()
        self.UiComponents()

    def UiComponents(self):
        self.open_pc_btn.clicked.connect(self.open_window)

    def open_window(self):
        ComputerScreen(self.MainWindow)


class ComputerScreen(Ui_ComputerScreen):
    def __init__(self, MainWindow):
        super().__init__()
        self.MainWindow = MainWindow
        self.ui = Ui_ComputerScreen()
        self.ui.setupUi(MainWindow)
        self.MainWindow.show()
        self.UiComponents()

    def UiComponents(self):
        self.back_to_room_btn.clicked.connect(self.open_window)
        self.open_file.clicked.connect(self.open_file_click)

    def open_window(self):
        GamerRoom(MainWindow)

    def open_file_click(self):
        self.label.setText("FILE OPENED")


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    window = ComputerScreen(MainWindow)
    sys.exit(app.exec_())
