from PyQt5 import uic, QtWidgets
from PyQt5.QtGui import QPixmap, QDrag
from PyQt5.QtCore import QMimeData, Qt
import sys

class MainWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.button_show()

    def button_show(self):
        self.setAcceptDrops(True)
        self.button = DragDropWidget("DRAG DROP", self)
        self.button.resize(200, 60)

    # overriding?
    def dragEnterEvent(self, event):
        event.accept()

    def dropEvent(self, event):
        pos = event.pos()
        self.button.move(pos)
        event.setDropAction(Qt.MoveAction)
        event.accept()


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
    widget = MainWidget()
    widget.resize(500, 500)
    widget.setWindowTitle("UAU")
    widget.show()
    sys.exit(application.exec_())
     