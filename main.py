import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton
from PyQt5.QtGui import QPainter, QBrush, QPen
from PyQt5.QtCore import Qt


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        self.k = 0
        uic.loadUi('Ui.ui', self)

        self.pb.clicked.connect(self.click)

    def click(self):
        self.k = 1

    def paintEvent(self, e):
        qp = QPainter()
        qp.begin(self)
        self.drawRectangles(qp)
        qp.end()

    def drawRectangles(self, qp):
        if self.k == 1:
            qp.setPen(QPen(Qt.green, 8, Qt.SolidLine))
            qp.setBrush(QBrush(Qt.red))
            qp.drawEllipse(20, 20, 100, 100)
            self.update()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())