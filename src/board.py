import numpy as np
from colorama import Style, Back
import os
from time import time


class Board():
    def __init__(self, rows, columns, frame_size, frame_start):
        self.__Rows = rows
        self.__Columns = columns
        self.__frameSize = frame_size
        self.__frameStart = frame_start
        self.__frameVelocity = 0.3
        self.__GameTime = 120
        self.__InitialTime = time()

    def getNoOfRows(self):
        return self.__Rows

    def getNoOfColumns(self):
        return self.__Columns

    def getFrameSize(self):
        return self.__frameSize

    def getFrameStart(self):
        return self.__frameStart

    def initialize_board(self):
        matrix = []
        for i in range(self.__Rows):
            single_row = []
            for j in range(self.__Columns):
                single_row.append(" ")
            matrix.append(single_row)
        self.__board = np.array(matrix, dtype=object)

    def placeObject(self, row_id, column_id, char):
        self.__board[row_id][column_id] = char

    def getFrameVelocity(self):
        return self.__frameVelocity

    def updateFrameVelocity(self, new_velocity):
        self.__frameVelocity = new_velocity

    def updateFrameStart(self):
        self.__frameStart = self.__frameStart + 1

    def print_board(self, myMando, Enemy):
        os.system('clear')
        print("Time Remaining : ", self.__GameTime -
              int(time() - self.__InitialTime))
        print("Coins : ", myMando.getCoins(), "Score : ",
              myMando.getScore(), "Lives : ", myMando.getLives())
        if myMando.getShieldStatus() == True:
            print("Shield ON ", "Time Left : ", int(myMando.getShieldTime() -
                                                    (time() - myMando.getShieldLatestUse())))
        else:
            if myMando.getShieldCoolDown() - int(time() - myMando.getShieldLastActive()) <= 0:
                print("Shield Ready To Use")
            else:
                print("Time Until shield can be used : ", myMando.getShieldCoolDown(
                ) - int(time() - myMando.getShieldLastActive()))

        if myMando.getPowerUpStatus() == True:
            print("Speed Boost Activated ", "Time Left : ",
                  int(myMando.getPowerUptime() - (time()-myMando.getPowerUpLatestUse())))
        else:
            if myMando.getPowerUpCoolDown() - int(time() - myMando.getPowerUpLastActive()) <= 0:
                print("Speed Boost Ready To Use")
            else:
                print("Time Remaining until speed boost can be used : ", myMando.getPowerUpCoolDown(
                ) - int(time() - myMando.getPowerUpLastActive()))
        if self.getFrameStart() >= self.getNoOfColumns() - self.getFrameSize() - 2 and Enemy.isBossAlive() == True:
            print("Dragon Lives :", Enemy.getLives())
        for i in range(self.getFrameSize()):
            print(Back.LIGHTBLUE_EX + " " + Style.RESET_ALL, end="")
        for i in range(self.__Rows):
            for j in range(self.__frameStart, self.__frameStart + self.__frameSize):
                if j < self.getNoOfColumns():
                    print(self.__board[i][j], end="")
                print(Style.RESET_ALL, end="")
            print()
        if time() - self.__InitialTime > self.__GameTime:
            os.system('clear')
            print("Time's Up")
            print("Game Over")
            print("Final Coins : ", myMando.getCoins(), "Final Score : ",
                  myMando.getScore())
            exit()
