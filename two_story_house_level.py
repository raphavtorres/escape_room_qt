from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QMovie

from two_story_house_window import Ui_TwoStoryHouse


class TwoStoryHouse(QtWidgets.QMainWindow):
    def __init__(self, won=False):
        super().__init__()

        self.ui = Ui_TwoStoryHouse()
        self.ui.setupUi(self)
        # self.won = won
        # self.test_if_won()
        # self.Ui_Elements()
        self.computer_screen = None

    # def Ui_Elements(self):
    #     self.ui.open_pc_btn.clicked.connect(self.open_window)
    #     self.ui.finish_level_btn.clicked.connect(self.show_portal)
    #     self.ui.open_portal_btn.clicked.connect(self.open_portal)

    # def open_window(self):
    #     self.computer_screen = ComputerScreen()
    #     self.close()
    #     self.computer_screen.show()

    # def test_if_won(self):
        # if self.won:
        #     self.ui.robot_truck_frame.show()

    # def show_portal(self):
    #     self.ui.robot_truck_frame.close()
    #     self.ui.open_portal_frame.show()
    #     self.movie = QMovie("images/gifs/gamer_room_portal_gif.gif")
    #     self.ui.bg_img_lb.setMovie(self.movie)
    #     self.movie.start()

    def open_portal(self):
        print("GLITCH SCREEN")
        print("OPENING NEW WINDOW")


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    gamer_room = TwoStoryHouse()
    gamer_room.show()
    sys.exit(app.exec_())
