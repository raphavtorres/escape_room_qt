from PyQt5 import QtCore, QtGui, QtWidgets
from gamer_room_window import Ui_GamerRoom
from computer_screen_window import Ui_ComputerScreen


class GamerRoom(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        self.ui = Ui_GamerRoom()
        self.ui.setupUi(self)

        self.ui.open_pc_btn.clicked.connect(self.open_window)

        self.computer_screen = None

    def open_window(self):
        self.computer_screen = ComputerScreen()
        self.close()
        self.computer_screen.show()


class ComputerScreen(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        self.ui = Ui_ComputerScreen()
        self.ui.setupUi(self)
        self.ui.password_frame.close()
        self.ui.back_to_room_btn.clicked.connect(self.back_to_room)
        self.ui.open_file_btn.clicked.connect(self.open_file_click)
        self.ui.enter_pass_btn.clicked.connect(self.check_input)

        self.gamer_room = None

    def back_to_room(self):
        self.gamer_room = GamerRoom()
        self.close()
        self.gamer_room.show()

    def open_file_click(self):
        self.ui.password_frame.show()

    def check_input(self):
        if self.ui.pass_input.text() == "pass":
            print("RIGHT PASS")
        else:
            print("WRONG PASS")
        self.ui.password_frame.close()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    gamer_room = GamerRoom()
    gamer_room.show()
    sys.exit(app.exec_())
