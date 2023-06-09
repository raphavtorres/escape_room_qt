from PyQt5 import uic
from PyQt5 import QtWidgets


from gamer_room_functions import open_computer, open_street_window, back_to_room, open_file_click, check_input, finish_level, show_clock, close_paper_clock,get_paper, glitch_screen


import files_rc


class PortalGUI():
    def __init__(self):
        app = QtWidgets.QApplication([])
        self.windows()
        self.ui_elements()
        self.start_game()
        app.exec()

    def start_game(self):
        self.gamer_room_window.show()
        self.gamer_room_window.clock_lb.close()
        self.gamer_room_window.close_paper_clock_btn.close()
        self.gamer_room_window.opened_paper_lb.close()


    def windows(self):
        self.gamer_room_window = uic.loadUi("windows_ui\\gamer_room_window.ui")
        self.computer_screen = uic.loadUi("windows_ui\\computer_screen_window.ui")
        self.street_window = uic.loadUi("windows_ui\\street_window.ui")
        self.gamer_room_portal = uic.loadUi("windows_ui\\gamer_room_portal.ui")

        self.two_story_house_window = uic.loadUi("windows_ui\\two_story_house_window.ui")

    def ui_elements(self):
        # gamer room
        self.gamer_room_window.open_pc_btn.clicked.connect(lambda: open_computer(self))
        self.gamer_room_window.street_window_btn.clicked.connect(lambda: open_street_window(self))
        self.gamer_room_window.clock_btn.clicked.connect(lambda: show_clock(self))
        self.gamer_room_window.clock_btn.clicked.connect(lambda: show_clock(self))
        self.gamer_room_window.close_paper_clock_btn.clicked.connect(lambda: close_paper_clock(self))
        self.gamer_room_window.get_paper_btn.clicked.connect(lambda: get_paper(self))
        # computer screen
        self.computer_screen.back_to_room_btn.clicked.connect(lambda: back_to_room(self))
        self.computer_screen.open_file_btn.clicked.connect(lambda: open_file_click(self))
        self.computer_screen.enter_pass_btn.clicked.connect(lambda: check_input(self))
        self.computer_screen.get_truck_btn.clicked.connect(lambda: finish_level(self))
        # street window
        self.street_window.back_to_room_btn.clicked.connect(lambda: back_to_room(self))
        #gamer room portal
        self.gamer_room_portal.open_next_btn.clicked.connect(lambda: glitch_screen(self))



if __name__ == "__main__":
    portal_gui = PortalGUI()
    