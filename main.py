from PyQt5 import uic
from PyQt5 import QtWidgets

from gamer_room_level_test import gamer_room, open_window


class PortalGUI():
    def __init__(self):
        app = QtWidgets.QApplication([])
        self.windows()
        self.ui_elements()
        self.gamer_room_window.show()
        app.exec()

    def windows(self):
        self.gamer_room_window = uic.loadUi("windows_ui\\gamer_room_window.ui")
        self.computer_screen = uic.loadUi("windows_ui\\computer_screen_window.ui")

    def ui_elements(self):
        # gamer room
        self.gamer_room_window.open_pc_btn.clicked.connect(self.open_window)
        # computer screen
        self.computer_screen.back_to_room_btn.clicked.connect(self.back_to_room)
        self.computer_screen.open_file_btn.clicked.connect(self.open_file_click)
        self.computer_screen.enter_pass_btn.clicked.connect(self.check_input)
        self.computer_screen.get_truck_btn.clicked.connect(self.finish_level)

    def open_window(self):
        self.gamer_room_window.close()

        self.computer_screen.show()
        self.computer_screen.password_frame.close()
        self.computer_screen.file_opened_frame.close()

    # Computer screen FUNCTIONS
    def back_to_room(self, won=False):
        self.computer_screen.close()
        self.gamer_room_window.show()
        
    def open_file_click(self):
        self.computer_screen.password_frame.show()

    def check_input(self):
        if self.computer_screen.pass_input.text() == "pass":
            self.computer_screen.file_opened_frame.show()
        else:
            print("WRONG PASS")
        self.computer_screen.password_frame.close()

    def finish_level(self):
        self.back_to_room(won=True)

if __name__ == "__main__":
    window = PortalGUI()
    