from PyQt5 import uic
from PyQt5 import QtWidgets
from PyQt5.QtGui import QMovie

from time import sleep

# from two_story_house_level import TwoStoryHouse


class GamerRoom():
    def __init__(self, ui, won=False):
        self.ui = ui
        self.ui.show()  # Starting program

        self.ui.robot_truck_frame.close()
        self.ui.open_portal_frame.close()
        self.ui.glitch_frame.close()

        self.won = won
        self.test_if_won()
        self.Ui_Elements()
        self.computer_screen = None

    def Ui_Elements(self):
        self.ui.open_pc_btn.clicked.connect(self.open_window)
        self.ui.finish_level_btn.clicked.connect(self.show_portal)
        self.ui.open_portal_btn.clicked.connect(self.open_portal)

    def open_window(self):
        gr_ui = self.ui
        ui = self.computer_screen = uic.loadUi("windows_ui\\computer_screen_window.ui")
        self.computer_screen = ComputerScreen(gr_ui, ui)
        self.ui.close()

    def test_if_won(self):
        if self.won:
            self.ui.robot_truck_frame.show()

    def show_portal(self):
        self.ui.robot_truck_frame.close()
        self.ui.open_portal_frame.show()
        self.movie = QMovie("images/gifs/gamer_room_portal_gif.gif")
        self.ui.bg_img_lb.setMovie(self.movie)
        self.movie.start()

    def show_glitch(self):
        self.ui.open_portal_frame.close()
        self.ui.glitch_frame.show()
        self.movie = QMovie("images/gifs/glitch_gif.gif")
        self.ui.bg_img_lb.setMovie(self.movie)
        self.movie.start()

    def open_two_story_house(self):
        ...
        # self.next_level = TwoStoryHouse()
        # self.close()
        # self.next_level.show()

    def open_portal(self):
        self.show_glitch()
        sleep(5)
        self.open_two_story_house()
        print("GLITCH SCREEN")
        print("OPENING NEW WINDOW")


class ComputerScreen():
    def __init__(self, gr_ui, ui):
        self.ui = ui
        self.gr_ui = gr_ui
        self.ui.show()

        self.ui.password_frame.close()
        self.ui.file_opened_frame.close()

        self.Ui_Elements()
        self.gamer_room = None
        

    def Ui_Elements(self):
        self.ui.back_to_room_btn.clicked.connect(self.back_to_room)
        self.ui.open_file_btn.clicked.connect(self.open_file_click)
        self.ui.enter_pass_btn.clicked.connect(self.check_input)
        self.ui.get_truck_btn.clicked.connect(self.finish_level)

    def back_to_room(self, won=False):
        GamerRoom(self.gr_ui, won)
        self.ui.close()

    def open_file_click(self):
        self.ui.password_frame.show()

    def check_input(self):
        if self.ui.pass_input.text() == "pass":
            self.ui.file_opened_frame.show()
        else:
            print("WRONG PASS")
        self.ui.password_frame.close()

    def finish_level(self):
        self.back_to_room(won=True)
