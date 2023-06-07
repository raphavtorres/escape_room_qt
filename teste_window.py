from PyQt5 import uic, QtWidgets
from PyQt5.QtGui import QPixmap, QDrag
from PyQt5.QtCore import QMimeData, Qt


class Test(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        
        app = QtWidgets.QApplication([])
        self.windows()
        self.button_show()
        app.exec()

    def windows(self):
        self.teste_window = uic.loadUi("windows_ui\\teste_window.ui")
        self.teste_window.show()


    def button_show(self):
        self.teste_window.setAcceptDrops(True)
        self.btn = DragDropWidget("DRAG DROP", self.teste_window)

    # overriding?
    def dragEnterEvent(self, event):
        event.accept()

    def dropEvent(self, event):
        pos = event.pos()
        self.teste_window.btn.move(pos)
        event.setDropAction(Qt.MoveAction)
        event.accept()
        
    

class DragDropWidget(QtWidgets.QPushButton):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def mouseMoveEvent(self, event):
        mime_data = QMimeData()  # holding the instance of the exact location of btn
        drag = QDrag(self)
        drag.setMimeData(mime_data)
        drag.setHotSpot(event.pos())  # cursor moving with btn
        drag.exec_(Qt.MoveAction)


if __name__ == "__main__":
    portal_gui = Test()
     