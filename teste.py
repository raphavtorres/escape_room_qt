import os, sys

from PyQt5 import uic
from PyQt5 import QtWidgets


class Teste():
    def __init__(self):

        # WINDOWS
        self.gamer_room_window = uic.loadUi("windows_ui\\untitled.ui")
        self.teste = uic.loadUi("windows_ui\\computer_screen_window.ui")

        self.gamer_room_window.pushButton.clicked.connect(self.open_window)
        self.gamer_room_window.show()  # Starting program

    def open_window(self):
        self.gamer_room_window.close()
        Teste2(self.teste)


class Teste2():
    def __init__(self, teste):
        # WINDOWS
        self.teste = teste
        self.teste.show()  # Starting program

        


if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    window = Teste()
    app.exec()