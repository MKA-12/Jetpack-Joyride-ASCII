from colorama import Fore
from board import Board


class Beam:
    def __init__(self, start_x, start_y, kind, size, figure):
        self.__startX = start_x
        self.__startY = start_y
        self.__Type = kind
        self.__Figure = figure
        self.__Size = size
        self.__xCoordinates = []
        self.__yCoordinates = []
        self.__Color = Fore.CYAN
        self.__isVisible = True
        for i in range(self.__Size):
            if self.__Type == "H":
                self.__xCoordinates.append(self.__startX + i)
                self.__yCoordinates.append(self.__startY)
            elif self.__Type == "V":
                self.__xCoordinates.append(self.__startX)
                self.__yCoordinates.append(self.__startY + i)
            elif self.__Type == "DA":
                self.__xCoordinates.append(self.__startX + i)
                self.__yCoordinates.append(self.__startY - i)
            elif self.__Type == "DB":
                self.__xCoordinates.append(self.__startX + i)
                self.__yCoordinates.append(self.__startY + i)

    def placeBeam(self, board: Board):
        for i in range(self.__Size):
            board.placeObject(
                self.__yCoordinates[i], self.__xCoordinates[i], self.__Color + self.__Figure)

    def disappearBeam(self, board: Board):
        for i in range(self.__Size):
            board.placeObject(
                self.__yCoordinates[i], self.__xCoordinates[i], " ")

    def getXcoordinates(self):
        return self.__xCoordinates
    
    def getYcoordinates(self):
        return self.__yCoordinates

    def getSize(self):
        return self.__Size

    def getVisibleStatus(self):
        return self.__isVisible

    def setVisibleStatus(self,status):
        self.__isVisible = status