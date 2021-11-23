from board import Board
from landscape import Landscape


class Person:
    def __init__(self, x, y, height, width, figure, lives, color):
        self._x_coordinate = x
        self._y_coordinate = y
        self._Matrix = figure
        self._Height = height
        self._Width = width
        self._Lives = lives
        self._Color = color
        self._jump = 3

    def getLives(self):
        return self._Lives

    def setLives(self, new_lives):
        self._Lives = new_lives

    def getMatrix(self):
        return self._Matrix

    def getColor(self):
        return self._Color

    def setColor(self, new_color):
        self._Color = new_color

    def getPerson(self):
        return self._Matrix

    def getXcoordinate(self):
        return self._x_coordinate

    def getYcoordinate(self):
        return self._y_coordinate

    def setXcoordinate(self, new_x):
        self._x_coordinate = new_x

    def setYcoordinate(self, new_y):
        self._y_coordinate = new_y

    def getHeight(self):
        return self._Height

    def getWidth(self):
        return self._Width

    def Collision_With_Ground(self, board: Board, y):
        if y + self._Height > board.getNoOfRows()-2:
            return True
        return False

    def Collision_With_Sky(self, board: Board, y):
        if y < 0:
            return True
        return False

    def Collison_With_left(self, board: Board, x):
        if x < board.getFrameStart():
            return True
        return False

    def Collision_With_right(self, board: Board, x):
        if x + self._Width - 1 > board.getFrameStart() + board.getFrameSize() - 1:
            return True
        return False

    def move(self, input, board: Board, landscape: Landscape):
        for i in range(self._Height):
            for j in range(self._Width):
                board.placeObject(self._y_coordinate+i,
                                  self._x_coordinate+j, " ")
        if input is 'w':
            if self.Collision_With_Ground(board, self._y_coordinate - self._jump) != True and self.Collision_With_Sky(board, self._y_coordinate - self._jump) != True:
                self._y_coordinate = self._y_coordinate - self._jump

            if self.Collision_With_Sky(board, self._y_coordinate-self._jump) == True:
                self._y_coordinate = 1

        else:
            if self.Collision_With_Ground(board, self._y_coordinate+1) != True and self.Collision_With_Sky(board, self._y_coordinate+1) != True:
                self._y_coordinate = self._y_coordinate + 1
