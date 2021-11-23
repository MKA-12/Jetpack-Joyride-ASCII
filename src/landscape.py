from colorama import Back, Fore
from board import Board
from random import randint, choice
from obstacle import Coin, Magnet
from beam import Beam


class Landscape():
    def __init__(self, board: Board):
        self.__ground = Back.YELLOW + " "
        self.__Coin = Fore.GREEN + "$"
        self.__magnet = Fore.BLUE + Back.WHITE + "M"
        self.__coinPositions = []
        self.__NoOfCoins = int(board.getNoOfColumns()/10)
        self.__NoOfBeams = int(board.getNoOfColumns()/10)
        self.__NoOfMagnets = randint(2, 4)
        self.__AllBeams = []
        self.__AllMagnets = []
        self.__Beam = ["=", "@", "%", "\\"]
        self.__BeamSize = 4

    def initialise_ground(self, board: Board):
        for i in range(board.getNoOfColumns()):
            board.placeObject(board.getNoOfRows()-1, i, self.__ground)
            board.placeObject(board.getNoOfRows()-2, i, self.__ground)

    def initialise_beams(self, board: Board):
        for i in range(self.__NoOfBeams):
            selection = randint(0, 3)
            beam = None
            if selection == 0:
                x, y = randint(10, board.getNoOfColumns() -
                               1 - self.__BeamSize - board.getFrameSize()), randint(1, board.getNoOfRows()-3)
                beam = Beam(x, y, "H", self.__BeamSize, self.__Beam[selection])
            elif selection == 1:
                x, y = randint(10, board.getNoOfColumns(
                ) - 1 - board.getFrameSize()), randint(1, board.getNoOfRows() - 3 - self.__BeamSize)
                beam = Beam(x, y, "V", self.__BeamSize, self.__Beam[selection])
            elif selection == 2:
                x, y = randint(10, board.getNoOfColumns(
                ) - 1 - self.__BeamSize - board.getFrameSize()), randint(1 + self.__BeamSize, board.getNoOfRows() - 3)
                beam = Beam(x, y, "DA", self.__BeamSize,
                            self.__Beam[selection])
            elif selection == 3:
                x, y = randint(10, board.getNoOfColumns(
                ) - 1 - self.__BeamSize - board.getFrameSize()), randint(1, board.getNoOfRows() - self.__BeamSize - 3)
                beam = Beam(x, y, "DB", self.__BeamSize,
                            self.__Beam[selection])
            beam.placeBeam(board)
            self.__AllBeams.append(beam)

    def initialise_coins(self, board: Board):
        for i in range(self.__NoOfCoins):
            coin = Coin(randint(1, board.getNoOfColumns()-42),
                        randint(1, board.getNoOfRows()-3), self.__Coin)
            self.__coinPositions.append(coin)
            board.placeObject(
                coin.getYcoordinate(), coin.getXcoordinate(), coin.getDisplay())

    def initialise_magnets(self, board: Board):
        for i in range(self.__NoOfMagnets):
            x, y = randint(40, board.getNoOfColumns() -
                           board.getFrameSize()), randint(10, board.getNoOfRows()-10)
            magnet = Magnet(x, y, self.__magnet, 2, 2)
            magnet.placeMagnet(board)
            self.__AllMagnets.append(magnet)

    def printMagnets(self, board: Board):
        for magnet in self.__AllMagnets:
            magnet.placeMagnet(board)

    def getAllMagnets(self):
        return self.__AllMagnets

    def getCoinPositions(self):
        return self.__coinPositions

    def getAllBeams(self):
        return self.__AllBeams
