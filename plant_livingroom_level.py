from PyQt5 import QtCore, QtGui, QtWidgets
from plant_livingroom_window import Ui_PlantRoom


class PlantRoom(Ui_PlantRoom):
    def __init__(self, MainWindow):
        self.setupUi(MainWindow)        


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow() 
    window = PlantRoom(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
