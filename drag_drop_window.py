from PyQt5 import QtWidgets, QtGui
from PyQt5.QtGui import QPixmap, QDrag
from PyQt5.QtCore import QMimeData, Qt

import sys
from windows_ui.shelf_window import Ui_shelf_window
import files_rc

class ShelfWindow(QtWidgets.QMainWindow, QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_shelf_window()
        self.ui.setupUi(self)
        self.books_show()

    def books_show(self):
        self.setAcceptDrops(True)

        self.green_book_lb = DragDropWidget("green_book_lb", self)
        self.green_book_lb.setPixmap(
            QPixmap("images\\two_story_house_fase\\green_book.png"))
        self.green_book_lb.setScaledContents(True)
        self.green_book_lb.setGeometry(400, 170, 51, 81)
        self.green_book_lb.setObjectName("green_book_lb")
        
        self.red_book_lb = DragDropWidget("red_book_lb", self)
        self.red_book_lb.setPixmap(
            QPixmap("images\\two_story_house_fase\\red_book.png"))
        self.red_book_lb.setScaledContents(True)
        self.red_book_lb.setGeometry(260, 170, 51, 91)
        self.red_book_lb.setObjectName("red_book_lb")

        self.blue_book_lb = DragDropWidget("blue_book_lb", self)
        self.blue_book_lb.setPixmap(
            QPixmap("images\\two_story_house_fase\\blue_book.png"))
        self.blue_book_lb.setScaledContents(True)
        self.blue_book_lb.setGeometry(150, 180, 51, 71)
        self.blue_book_lb.setObjectName("blue_book_lb")

    def dragEnterEvent(self, event):
        event.accept()

    def dropEvent(self, event):
        pos = event.pos()
        # print(event.source().objectName())
        print(pos)

        if event.source().objectName() == "green_book_lb":
            self.green_book_lb.move(pos)
        elif event.source().objectName() == "red_book_lb":
            self.red_book_lb.move(pos)
        elif event.source().objectName() == "blue_book_lb":
            self.blue_book_lb.move(pos)

        # TEST POSITIONS
        self.test_positions()

        event.setDropAction(Qt.MoveAction)
        event.accept()

    def test_positions(self):
        # Getting positions
        b_x_pos = self.blue_book_lb.x()
        b_y_pos = self.blue_book_lb.y()

        r_x_pos = self.red_book_lb.x()
        r_y_pos = self.red_book_lb.y()

        g_x_pos = self.green_book_lb.x()
        g_y_pos = self.green_book_lb.y()

        # Testing
        if (130 < b_y_pos < 220) and (130 < r_y_pos < 220) and (130 < g_y_pos < 220):
            # R G B
            if (r_x_pos < g_x_pos) and (r_x_pos < b_x_pos):
                if (g_x_pos < b_x_pos):
                    print("ok")



class DragDropWidget(QtWidgets.QLabel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def mouseMoveEvent(self, event):
        mime_data = QMimeData()  # holding the instance of the exact location of btn
        drag = QDrag(self)
        drag.setMimeData(mime_data)
        drag.setHotSpot(event.pos())  # cursor moving with btn
        drag.exec_(Qt.MoveAction)


if __name__ == "__main__":
    application = QtWidgets.QApplication(sys.argv)
    widget = ShelfWindow()
    widget.show()
    sys.exit(application.exec_())
   