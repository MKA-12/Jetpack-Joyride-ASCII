from person import Person
from board import Board
from bullet import EnemyBullet
from landscape import Landscape
from mando import Mando
from random import randint


class Boss(Person):
    def __init__(self, x, y, height, width, figure, lives, color):
        super().__init__(x, y, height, width, figure, lives, color)
        self.__BulletPositions = []
        self.__Start_X = x
        self.__Start_Y = y
        self.__isAlive = True
        self._Lives = 10
        with open("./Dragon.txt") as dragon:
            for line in dragon:
                self._Matrix.append(line.strip('\n'))

    def lostlife(self, board: Board):
        self._Lives -= 1
        for i in range(self._Height):
            for j in range(self._Width):
                board.placeObject(self._y_coordinate+i,
                                  self._x_coordinate+j, " ")
        if self.getLives() == 0:
            self.__isAlive = False
        else:
            self.setXcoordinate(self.__Start_X)
            self.setYcoordinate(self.__Start_Y)

    def getBulletPositions(self):
        return self.__BulletPositions

    def placeBoss(self, board: Board):
        for i in range(self._Height):
            for j in range(self._Width):
                board.placeObject(self._y_coordinate+i,
                                  self._x_coordinate+j, self.getColor() + self._Matrix[i][j])

    def generateBullet(self, board: Board, landscape: Landscape):
        bullet = EnemyBullet(self._x_coordinate, randint(
            self._y_coordinate, self._y_coordinate+self._Height - 1), "O", 3)
        self.__BulletPositions.append(bullet)

    def checkIceBallCollision(self, iceball, board: Board, mando: Mando):
        for j in range(mando.getHeight()):
            for i in range(mando.getWidth()):
                if mando.getXcoordinate() + i == iceball.getXcoordinate() and mando.getYcoordinate() + j == iceball.getYcoordinate():
                    if mando.getShieldStatus() != True:
                        mando.lostlife()
                    iceball.changeOnBoardStatus(False)
                    iceball.disappearBullet(board)
                    break

    def moveAllBullets(self, board: Board, landscape: Landscape, mando: Mando):
        for bullet in self.__BulletPositions:
            if bullet.getXcoordinate() <= board.getFrameStart() or bullet.getXcoordinate() >= board.getNoOfColumns() - 2:
                bullet.changeOnBoardStatus(False)
                bullet.disappearBullet(board)
            if bullet.getOnBoardStatus() == True:
                self.checkIceBallCollision(bullet, board, mando)
            if bullet.getOnBoardStatus() == True:
                bullet.move(board, landscape)
                bullet.placeBullet(board)

            if bullet.getOnBoardStatus() == False:
                self.__BulletPositions.remove(bullet)

    def isBossAlive(self):
        return self.__isAlive
