from colorama import Fore
from board import Board


class Bullet:
    def __init__(self, x, y, figure, velocity):
        self._xCoordinate = x
        self._yCoordinate = y
        self._Display = figure
        self._Velocity = velocity
        self._onBoard = True
        self._Color = Fore.LIGHTMAGENTA_EX

    def getVelocity(self):
        return self._Velocity

    def setVelocity(self, new_velocity):
        self._Velocity = new_velocity

    def getXcoordinate(self):
        return self._xCoordinate

    def getYcoordinate(self):
        return self._yCoordinate

    def getColor(self):
        return self._Color

    def setColor(self, color):
        self._Color = color

    def setXcoordinate(self, new_x):
        self._xCoordinate = new_x

    def setYcoordinate(self, new_y):
        self._yCoordinate = new_y

    def move(self, board: Board, landscape):
        board.placeObject(self._yCoordinate,
                          self._xCoordinate, " ")
        for coin in landscape.getCoinPositions():
            for i in range(self._xCoordinate, self._xCoordinate + self._Velocity):
                if i == coin.getXcoordinate() and self._yCoordinate == coin.getYcoordinate() and coin.collectionStatus() == False:
                    board.placeObject(coin.getYcoordinate(),
                                      coin.getXcoordinate(), coin.getDisplay())

        if self._onBoard == True:
            self._xCoordinate += self._Velocity

    def placeBullet(self, board: Board):
        if self._onBoard == True:
            board.placeObject(self._yCoordinate,
                              self._xCoordinate, self._Color + self._Display)

    def disappearBullet(self, board: Board):
        if self._onBoard == False:
            board.placeObject(self._yCoordinate, self._xCoordinate, " ")

    def changeOnBoardStatus(self, new_status):
        self._onBoard = new_status

    def getOnBoardStatus(self):
        return self._onBoard


class EnemyBullet(Bullet):
    def __init__(self, x, y, figure, velocity):
        super().__init__(x, y, figure, velocity)

    def move(self, board: Board, landscape):
        board.placeObject(self._yCoordinate,
                          self._xCoordinate, " ")
        for coin in landscape.getCoinPositions():
            for i in range(self._xCoordinate, self._xCoordinate + self._Velocity):
                if i == coin.getXcoordinate() and self._yCoordinate == coin.getYcoordinate() and coin.collectionStatus() == False:
                    board.placeObject(coin.getYcoordinate(),
                                      coin.getXcoordinate(), coin.getDisplay())

        if self._onBoard == True:
            self._xCoordinate -= self._Velocity
