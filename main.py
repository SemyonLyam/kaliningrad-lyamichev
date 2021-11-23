import sys

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QApplication, QLabel
from PyQt5.QtGui import QPainter, QColor
from random import randint


class Example(QWidget):
    def __init__(self):
        super(Example, self).__init__()
        self.initUI()


    def drawf(self):
        self.flag = True
        self.update()

    def paintEvent(self, event):
        if self.flag:
            self.qp = QPainter()
            self.qp.begin(self)
            self.draw()
            self.qp.end()

    def initUI(self):
        self.setGeometry(300, 300, 500, 500)
        self.setWindowTitle('Рисование')

        self.coords_ = [0, 0]
        self.setMouseTracking(True)
        self.qp = QPainter()
        self.flag = False
        self.status = None

        self.show()

    def mouseMoveEvent(self, event):
        self.coords_ = [event.x(), event.y()]

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.status = 1
        elif event.button() == Qt.RightButton:
            self.status = 2
        self.drawf()

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Space:
            self.status = 3
            self.drawf()

    def draw(self):
        r = randint(1, 100)
        if self.status == 1:
            self.qp.setBrush(QColor(randint(0, 255), randint(0, 255), randint(0, 255)))
            self.qp.drawEllipse(self.coords_[0], self.coords_[1], r, r)
        elif self.status == 2:
            self.qp.setBrush(QColor(randint(0, 255), randint(0, 255), randint(0, 255)))
            self.qp.drawRect(self.coords_[0], self.coords_[1], r, r)
        elif self.status == 3:
            self.qp.setPen(QColor(randint(0, 255), randint(0, 255), randint(0, 255)))
            coord = [(self.coords_[0] - r, self.coords_[1] - r),
                     (self.coords_[0] + r, self.coords_[1] - r),
                     (self.coords_[0], self.coords_[1] + r)]
            self.qp.drawLine(*coord[0], *coord[1])
            self.qp.drawLine(*coord[1], *coord[2])
            self.qp.drawLine(*coord[2], *coord[0])


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec())