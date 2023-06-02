from PyQt5 import QtCore, QtGui, QtWidgets
import interface.gamer_room_window as g_room
import interface.plant_livingroom_window as p_liv_room

class MyWindow(g_room.Ui_MainWindow):
    def __init__(self, MainWindow):
        self.setupUi(MainWindow)
        self.UiComponents()

    def UiComponents(self):
        self.open_pc_btn.clicked.connect(self.open_window)

    def open_window(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = SecondWindow(window)
        self.window.show()
        self.MainWindow.close()


class SecondWindow(p_liv_room.Ui_MainWindow):
    def __init__(self, MainWindow):
        self.setupUi(MainWindow)



# stylesheet = """
#     MainWindow {
#         background-image: url("C:\\Users\\ct67ca\\Desktop\\escape_room_qt\\teste.jpg");
#         background-repeat: no-repeat; 
#         background-position: center;
#     }
# """


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    # app.setStyleSheet(stylesheet)
    MainWindow = QtWidgets.QMainWindow()
    window = MyWindow(MainWindow)

    MainWindow.show()
    sys.exit(app.exec_())
