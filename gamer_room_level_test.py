from PyQt5 import uic
from PyQt5 import QtWidgets
from PyQt5.QtGui import QMovie

from time import sleep

# from two_story_house_level import TwoStoryHouse


def gamer_room(self):
    ...
    # self.ui.robot_truck_frame.close()
    # self.ui.open_portal_frame.close()
    # self.ui.glitch_frame.close()

    # self.test_if_won()

def Ui_Elements(self):
    ...
    # self.ui.finish_level_btn.clicked.connect(self.show_portal)
    # self.ui.open_portal_btn.clicked.connect(self.open_portal)

def open_window(self):
    self.ui.close()
    computer_screen = ComputerScreen(self.ui, self.computer_screen)

    # def test_if_won(self):
    #     if self.won:
    #         self.ui.robot_truck_frame.show()

    # def show_portal(self):
    #     self.ui.robot_truck_frame.close()
    #     self.ui.open_portal_frame.show()
    #     self.movie = QMovie("images/gifs/gamer_room_portal_gif.gif")
    #     self.ui.bg_img_lb.setMovie(self.movie)
    #     self.movie.start()

    # def show_glitch(self):
    #     self.ui.open_portal_frame.close()
    #     self.ui.glitch_frame.show()
    #     self.movie = QMovie("images/gifs/glitch_gif.gif")
    #     self.ui.bg_img_lb.setMovie(self.movie)
    #     self.movie.start()

    # def open_two_story_house(self):
    #     ...
    #     # self.next_level = TwoStoryHouse()
    #     # self.close()
    #     # self.next_level.show()

    # def open_portal(self):
    #     self.show_glitch()
    #     sleep(5)
    #     self.open_two_story_house()
    #     print("GLITCH SCREEN")
    #     print("OPENING NEW WINDOW")
