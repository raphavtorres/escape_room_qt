from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QMovie
from time import sleep

from gamer_room_window import Ui_GamerRoom
from computer_screen_window import Ui_ComputerScreen
from two_story_house_level import TwoStoryHouse


class GamerRoom(QtWidgets.QMainWindow):
    def __init__(self, won=False):
        super().__init__()

        self.ui = Ui_GamerRoom()
        self.ui.setupUi(self)
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
        self.computer_screen = ComputerScreen()
        self.close()
        self.computer_screen.show()

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
        self.next_level = TwoStoryHouse()
        self.close()
        self.next_level.show()

    def open_portal(self):
        self.show_glitch()
        sleep(5)
        self.open_two_story_house()
        print("GLITCH SCREEN")
        print("OPENING NEW WINDOW")


class ComputerScreen(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        self.ui = Ui_ComputerScreen()
        self.ui.setupUi(self)
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
        self.gamer_room = GamerRoom(won)
        self.close()
        self.gamer_room.show()

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


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    gamer_room = GamerRoom()
    gamer_room.show()
    sys.exit(app.exec_())
