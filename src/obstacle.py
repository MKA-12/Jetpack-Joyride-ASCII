from board import Board


class Obstacle:
    def __init__(self, x, y, figure):
        self._x_coordinate = x
        self._y_coordinate = y
        self._Display = figure

    def getXcoordinate(self):
        return self._x_coordinate

    def getYcoordinate(self):
        return self._y_coordinate

    def getDisplay(self):
        return self._Display


class Coin(Obstacle):
    def __init__(self, x, y, figure):
        super().__init__(x, y, figure)
        self.__isCollected = False

    def collectionStatus(self):
        return self.__isCollected

    def setCollectionStatus(self, status):
        self.__isCollected = status


class Magnet(Obstacle):
    def __init__(self, x, y, figure, height, width):
        super().__init__(x, y, figure)
        self.__Height = height
        self.__Width = width
        self.__Range = 10

    def placeMagnet(self, board: Board):
        for i in range(self.__Height):
            for j in range(self.__Width):
                board.placeObject(self._y_coordinate+i,
                                  self._x_coordinate+j, self._Display)

    def getRange(self):
        return self.__Range
