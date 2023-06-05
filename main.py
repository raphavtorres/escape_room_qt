import os, sys

from PyQt5 import uic
from PyQt5 import QtWidgets

from gamer_room_level_test import GamerRoom


class PortalGUI():
    def __init__(self):
        # WINDOWS
        self.gamer_room_window = uic.loadUi("windows_ui\\gamer_room_window.ui")
        

        GamerRoom(self.gamer_room_window)  # Starting program


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = PortalGUI()
    sys.exit(app.exec_())