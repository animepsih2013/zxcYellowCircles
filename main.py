import sys
import random
from UI import Ui_circles
from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6.QtGui import QPainter, QColor


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_circles()
        self.ui.setupUi(self)

        self.circles = []

        self.ui.pushButton.clicked.connect(self.add_circle)

    def add_circle(self):
        diameter = random.randint(20, 100)
        x = random.randint(0, self.width() - diameter)
        y = random.randint(0, self.height() - diameter)
        self.circles.append((x, y, diameter))

        self.update()

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)


        for (x, y, diameter) in self.circles:
            r = random.randint(0, 256)
            g = random.randint(0, 256)
            b = random.randint(0, 256)
            painter.setBrush(QColor(r, g, b))
            painter.drawEllipse(x, y, diameter, diameter)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
