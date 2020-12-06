import sys

from random import randint

from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton
from PyQt5.QtGui import QPainter, QColor


class Ellipse(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setFixedSize(350, 500)
        self.setWindowTitle('Ellipse')

        self.drawbtn = QPushButton(self)
        self.drawbtn.move(110, 30)
        self.drawbtn.resize(120, 40)
        self.drawbtn.setText('Рисовать')

        self.do_paint = False
        self.drawbtn.clicked.connect(self.paint)

    def paintEvent(self, event):
        if self.do_paint:
            qp = QPainter()
            qp.begin(self)
            self.draw_flag(qp)
            qp.end()

    def paint(self):
        self.do_paint = True
        self.repaint()

    def draw_flag(self, qp):
        a = randint(50, 300)
        qp.setBrush(QColor(randint(0, 255), randint(0, 255), randint(0, 255)))
        qp.drawEllipse(50, 200, a, a)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    e = Ellipse()
    e.show()
    sys.exit(app.exec())