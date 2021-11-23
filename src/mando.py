from person import Person
from board import Board
from colorama import Fore
from landscape import Landscape
from obstacle import Coin, Magnet
from beam import Beam
from bullet import Bullet, EnemyBullet
from time import time
import os


class Mando(Person):
    def __init__(self, x, y, height, width, figure, lives, color):
        super().__init__(x, y, height, width, figure, lives, color)
        self.__Coins = 0
        self.__Score = 0
        self.__CoinsTaken = []
        self.__shift = 2
        self.__CoinValue = 100
        self.__allBullets = []
        self.__shieldActive = False
        self.__shieldCoolDown = 60
        self.__shieldTime = 10
        self.__shieldLatestUse = (-1) * self.__shieldCoolDown
        self.__shieldLastActive = self.__shieldLatestUse
        self.__powerUpCoolDown = 60
        self.__powerUpTime = 10
        self.__powerUpActive = False
        self.__powerUpLatestUse = (-1) * self.__powerUpCoolDown
        self.__powerUpLastActive = self.__powerUpLatestUse
        self.__latestup = time()
        self.__BulletVelocity = 2

    def getAllBullets(self):
        return self.__allBullets

    def getCoins(self):
        return self.__Coins

    def getScore(self):
        return self.__Score

    def getShieldStatus(self):
        return self.__shieldActive

    def getShieldLatestUse(self):
        return self.__shieldLatestUse

    def getShieldLastActive(self):
        return self.__shieldLastActive

    def changeRightShift(self, shift):
        self.__shift = shift

    def getPowerUptime(self):
        return self.__powerUpTime

    def getShieldTime(self):
        return self.__shieldTime

    def getShieldCoolDown(self):
        return self.__shieldCoolDown

    def changeShieldStatus(self):
        self.__shieldActive = not self.__shieldActive

    def setShieldStatus(self, status):
        self.__shieldActive = status

    def getPowerUpStatus(self):
        return self.__powerUpActive

    def getPowerUpLastActive(self):
        return self.__powerUpLastActive

    def getPowerUpCoolDown(self):
        return self.__powerUpCoolDown

    def getPowerUpLatestUse(self):
        return self.__powerUpLatestUse

    def changePowerUpStatus(self):
        self.__powerUpActive = not self.__powerUpActive

    def placeMando(self, board: Board):
        for i in range(self._Height):
            for j in range(self._Width):
                board.placeObject(self._y_coordinate+i,
                                  self._x_coordinate+j, self.getColor() + self._Matrix[i][j])

    def checkCoinCollision(self, x, y, landscape: Landscape):
        for coin in landscape.getCoinPositions():
            if coin.getXcoordinate() == x and coin.getYcoordinate() == y and coin.collectionStatus() == False:
                coin.setCollectionStatus(True)
                self.__Coins = self.__Coins + 1
                self.__Score = self.__Score + self.__CoinValue

    def checkBeamCollision(self, x, y, landscape: Landscape, board: Board):
        for beam in landscape.getAllBeams():
            for i in range(beam.getSize()):
                if x == beam.getXcoordinates()[i] and y == beam.getYcoordinates()[i] and beam.getVisibleStatus() == True:
                    beam.disappearBeam(board)
                    beam.setVisibleStatus(False)
                    if self.__shieldActive == False:
                        os.system('clear')
                        print("You lost a life.")
                        if self.getLives() > 1:
                            self.setLives(self.getLives() - 1)
                            print("Remaining Lives : ", self.getLives())
                            print("Press ENTER to continue.")
                            input()
                        else:
                            print("No lives left.")
                            print("You lost.")
                            print("Final Score : ", self.__Score,
                                  "Coins : ", self.__Coins)
                            exit()
                    break

    def checkBulletCollision(self, x, y, landscape: Landscape, board: Board, bullet):
        for beam in landscape.getAllBeams():
            for i in range(beam.getSize()):
                if x == beam.getXcoordinates()[i] and y == beam.getYcoordinates()[i] and beam.getVisibleStatus() == True:
                    beam.disappearBeam(board)
                    beam.setVisibleStatus(False)
                    bullet.changeOnBoardStatus(False)
                    bullet.disappearBullet(board)
                    self.__Score += 50

    def bulletWithBoss(self, boss, bullet: Bullet, board: Board):
        for y in range(boss.getHeight()):
            for x in range(boss.getWidth()):
                if bullet.getXcoordinate() == boss.getXcoordinate() + x and bullet.getYcoordinate() == boss.getYcoordinate()+y:
                    bullet.disappearBullet(board)
                    bullet.changeOnBoardStatus(False)
                    self.__Score += 500
                    boss.lostlife(board)
                    break

    def moveAllBullets(self, board: Board, landscape: Landscape, boss):
        for bullet in self.__allBullets:
            if bullet.getXcoordinate() >= board.getFrameStart() + board.getFrameSize() - 2 or bullet.getXcoordinate() >= board.getNoOfColumns():
                bullet.changeOnBoardStatus(False)
                bullet.disappearBullet(board)
            if bullet.getOnBoardStatus() == True:
                for i in range(bullet.getXcoordinate(), bullet.getXcoordinate()+bullet.getVelocity()):
                    self.checkBulletCollision(
                        i, bullet.getYcoordinate(), landscape, board, bullet)
                    self.bulletWithBoss(boss, bullet, board)
            if bullet.getOnBoardStatus() == True:
                bullet.move(board, landscape)
                bullet.placeBullet(board)

            if bullet.getOnBoardStatus() == False:
                self.__allBullets.remove(bullet)

    def mandoAttract(self, landscape: Landscape):
        for magnet in landscape.getAllMagnets():
            if abs(self._x_coordinate - magnet.getXcoordinate() - 1) <= magnet.getRange() and abs(self._y_coordinate - magnet.getYcoordinate() - 1) <= magnet.getRange():
                if self._x_coordinate - magnet.getXcoordinate() - 1 > 0 and self._x_coordinate - magnet.getXcoordinate() - 1 <= magnet.getRange():
                    self._x_coordinate -= 1
                elif self._x_coordinate - magnet.getXcoordinate() - 1 < 0 and magnet.getXcoordinate() + 1 - self._x_coordinate <= magnet.getRange():
                    self._x_coordinate += 1
                if self._y_coordinate - magnet.getYcoordinate() - 1 > 0 and self._y_coordinate - magnet.getYcoordinate() - 1 <= magnet.getRange():
                    self._y_coordinate -= 2
                elif self._y_coordinate - magnet.getYcoordinate() - 1 < 0 and magnet.getYcoordinate() + 1 - self._y_coordinate <= magnet.getRange():
                    self._y_coordinate += 2

    def lostlife(self):
        os.system('clear')
        print("You lost a life.")
        if self.getLives() > 1:
            self.setLives(self.getLives() - 1)
            print("Remaining Lives : ", self.getLives())
            print("Press ENTER to continue.")
            input()
        else:
            print("No lives left.")
            print("You lost.")
            print("Final Score : ", self.__Score,
                  "Coins : ", self.__Coins)
            exit()

    def move(self, input, board: Board, landscape: Landscape):
        for i in range(self._Height):
            for j in range(self._Width):
                board.placeObject(self._y_coordinate+i,
                                  self._x_coordinate+j, " ")
                self.checkCoinCollision(
                    self._x_coordinate+j, self._y_coordinate+i, landscape)
                self.checkBeamCollision(
                    self._x_coordinate+j, self._y_coordinate+i, landscape, board)
        # self.mandoAttract(landscape)
        if input is not None:
            if input is 'w':
                self.__latestup = time()
                if self.Collision_With_Ground(board, self._y_coordinate-self._jump) != True and self.Collision_With_Sky(board, self._y_coordinate - self._jump) != True:
                    self._y_coordinate = self._y_coordinate - self._jump

                if self.Collision_With_Sky(board, self._y_coordinate-self._jump) == True:
                    self._y_coordinate = 1

            if input is 'a':
                if self.Collison_With_left(board, self._x_coordinate-self.__shift) != True:
                    self._x_coordinate = self._x_coordinate - self.__shift

            if input is 'd':
                if self.Collision_With_right(board, self._x_coordinate + self.__shift) != True:
                    self._x_coordinate = self._x_coordinate + self.__shift
                else:
                    self._x_coordinate = board.getFrameStart() + board.getFrameSize() - \
                        1 - self._Width

            if input is 'b':
                new_bullet = Bullet(self._x_coordinate +
                                    self._Width, self._y_coordinate, ">", self.__BulletVelocity)
                self.__allBullets.append(new_bullet)

            if input is 'f':
                if time() - self.__powerUpLastActive > self.__powerUpCoolDown and self.__powerUpActive == False:
                    self.changePowerUpStatus()
                    board.updateFrameVelocity(0.05)
                    self.changeRightShift(3)
                    self.__BulletVelocity = 3
                    self.__powerUpLatestUse = time()
            if input is ' ':
                if time() - self.__shieldLastActive > self.__shieldCoolDown and self.__shieldActive == False:
                    self.changeShieldStatus()
                    self.setColor(Fore.BLUE)
                    self.changeRightShift(2)
                    self.__shieldLatestUse = time()

        if self.__shieldActive == True:
            if time() - self.__shieldLatestUse > self.__shieldTime:
                self.changeShieldStatus()
                self.setColor(Fore.RED)
                self.__shieldLastActive = time()

        if self.__powerUpActive == True:
            if time() - self.__powerUpLatestUse > self.__powerUpTime:
                self.changePowerUpStatus()
                self.__powerUpLastActive = time()
                self.changeRightShift(2)
                self.__BulletVelocity = 2
                board.updateFrameVelocity(0.3)
        if self.Collison_With_left(board, self._x_coordinate) == True:
            self._x_coordinate = board.getFrameStart()

        if input is not 'w':
            down = 1 + 2 * int(time() - self.__latestup)
            if down > self._Height:
                down = self._Height - 1
            if self.Collision_With_Ground(board, self._y_coordinate+down) != True and self.Collision_With_Sky(board, self._y_coordinate+down) != True:
                self._y_coordinate = self._y_coordinate + down

            if self.Collision_With_Ground(board, self._y_coordinate + down) == True:
                self._y_coordinate = board.getNoOfRows()-5
