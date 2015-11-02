import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import random
import functools

class MainWindow(QWidget):

    def __init__(self, N, minesCount, mainWindow):
        super().__init__()
        self.MW = mainWindow
        self.N = N
        self.btnSize = 40
        self.minesCount = minesCount
        self.initUI()
        self.NewGame()
        self.field = []

       
    def initUI(self):
        self.move(300, 300)
        self.setWindowTitle('Miner')
        self.setWindowIcon(QIcon('icon.png'))
        self.setFixedSize(self.btnSize*self.N+20, self.btnSize*self.N+20  + self.btnSize + 10)

        self.bigBtnSize = (self.frameGeometry().width() - 10)/3 - 10

        self.buttons = [[None]*self.N for x in range(self.N)]
        for i in range(self.N):
            for j in range(self.N):
                self.buttons[i][j] = QPushButton('', self)
                self.buttons[i][j].clicked.connect(functools.partial(self.Step, i, j))
                #self.buttons[i][j].customContextMenuRequested.connect(functools.partial(self.Step, i, j))
                self.buttons[i][j].setGeometry(10 + i*self.btnSize, 10 + j*self.btnSize, self.btnSize, self.btnSize)
                self.buttons[i][j].clearFocus()

        self.NewGameBtn = QPushButton("New Game", self)
        self.NewGameBtn.clicked.connect(self.NewGame)
        self.NewGameBtn.setGeometry(10, 20 + self.N*self.btnSize, self.bigBtnSize, self.btnSize)

        self.Label = QLabel("", self)
        self.Label.setGeometry(10 + self.bigBtnSize + 10, 20 + self.N*self.btnSize, self.bigBtnSize, self.btnSize)
        self.Label.setAlignment(Qt.AlignCenter)
 
        DiffBtn = QPushButton("Difficulty", self)
        DiffBtn.clicked.connect(self.Difficulty)
        DiffBtn.setGeometry(10 + self.bigBtnSize + 10 + self.bigBtnSize + 10, 20 + self.N*self.btnSize, self.bigBtnSize, self.btnSize)

        self.show()

    def Step(self, i, j):
        self.buttons[i][j].clearFocus()
        if self.gameOver == False and self.win == False:
            self.Label.setText("Mines: " + str(self.minesCount))
            if self.firstStep == True:
                self.PlaceMines(i, j)
                self.firstStep = False
            
            if self.field[i][j] == 99:
                self.field[i][j] = 0
                for _i in range(-1, 2):
                    for _j in range(-1, 2):
                        if (0 <= i + _i < self.N) and (0 <= j + _j < self.N) and not(_i == 0 and _j == 0):
                            if self.field[i+_i][j + _j] == -1:
                                self.field[i][j] += 1
                if self.field[i][j] == 0:
                    for _i in range(-1, 2):
                        for _j in range(-1, 2):
                            if (0 <= i + _i < self.N) and (0 <= j + _j < self.N) and not(_i == 0 and _j == 0):
                                if self.field[i +_i][j + _j] == 99:
                                    self.Step(i+_i, j + _j)
                                if self.field[i+_i][j + _j] == -1:
                                    self.field[i][j] += 1
            self.DrawButton(i, j)
            self.CheckLose(i, j)
            self.WinCheck()
            
        

    def Difficulty(self):
        
        self.MW.show()
        self.hide()


    def PlaceMines(self, _i, _j):
        self.mines = 0
        self.field = [[99 for y in range(self.N)] for x in range(self.N)]
        while self.mines < self.minesCount:
            for i in range(self.N):
                for j in range(self.N):
                    if not(i == _i and j == _j):
                        if self.mines < self.minesCount and random.randint(0, self.N*self.N) < self.N:
                            if self.field[i][j] == 99:
                                self.field[i][j] = -1
                                self.mines += 1


    def NewGame(self):
        self.firstStep = True
        self.gameOver = False
        self.win = False
        for i in range(self.N):
            for j in self.buttons[i]:
                j.setText('')
                j.setStyleSheet("background-color: #E0E0E0;border: 1px solid black;")
        self.Label.setText("Mines: " + str(self.minesCount))

    def DrawButton(self, i, j):
        if self.field[i][j] == -1:
            self.buttons[i][j].setText("X")
            self.buttons[i][j].setStyleSheet("background-color: #EE0000;border: 1px solid black;")
        elif self.field[i][j] == 0:
            self.buttons[i][j].setText("")
            self.buttons[i][j].setStyleSheet("background-color: #00CCFF;border: 1px solid black;")
        elif self.field[i][j] == 99:
            self.buttons[i][j].setText("")
            self.buttons[i][j].setStyleSheet("background-color: #A0A0A0;border: 1px solid black;")
        else:
            self.buttons[i][j].setText(str(self.field[i][j]))
            self.buttons[i][j].setStyleSheet("background-color: #FFFFFF;border: 1px solid black;")


    def CheckLose(self, i, j):
        if self.field[i][j] == -1:
            self.gameOver = True
            for i in range(self.N):
                for j in range(self.N):
                    if self.field[i][j] == -1:
                        self.buttons[i][j].setText("X")
                        self.buttons[i][j].setStyleSheet("background-color: #EE0000;border: 1px solid black;")
            self.Label.setText("You Lose!")

    def WinCheck(self):
        sum = 0
        for i in range(self.N):
            for j in range(self.N):
                if self.field[i][j] == 99:
                    sum += 1
        if sum == 0:
            self.win = True
            for i in range(self.N):
                for j in range(self.N):
                    if self.field[i][j] == -1:
                        self.buttons[i][j].setText("X")
                        self.buttons[i][j].setStyleSheet("background-color: #00EE00;border: 1px solid black;")
            self.Label.setText("You Win!")



if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = MainWindow(16)
    sys.exit(app.exec_())