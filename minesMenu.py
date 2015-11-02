from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys
import functools
import random
import mines

class Menu(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.move(300, 300)
        self.setWindowTitle('Miner')
        self.setFixedSize(600, 200)

        self.btnWidth = (self.frameGeometry().width()-10)/3 - 10
        self.btnHeight = 180
        

        self.btn8x8 = QPushButton("8x8", self)
        self.btn8x8.clicked.connect(functools.partial(self.Click, (8, 10)))
        self.btn8x8.setGeometry(10, 10, self.btnWidth, self.btnHeight)
        self.btn8x8.setStyleSheet('font-size: 32pt;')

        self.btn12x12 = QPushButton("12x12", self)
        self.btn12x12.clicked.connect(functools.partial(self.Click, (12, 21)))
        self.btn12x12.setGeometry(10 + self.btnWidth + 10, 10, self.btnWidth, self.btnHeight)
        self.btn12x12.setStyleSheet('font-size: 32pt;')

        self.btn16x16 = QPushButton("16x16", self)
        self.btn16x16.clicked.connect(functools.partial(self.Click, (16, 36)))
        self.btn16x16.setGeometry(10 + self.btnWidth + 10 + self.btnWidth + 10, 10, self.btnWidth, self.btnHeight)
        self.btn16x16.setStyleSheet('font-size: 32pt;')

        self.show()

    def Click(self, n):
        ex = mines.MainWindow(n[0], n[1], self)
        self.hide()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Menu()
    sys.exit(app.exec_())