import os
from board import Board
from landscape import Landscape
from input import Get, input_to
from mando import Mando
from colorama import Fore
from time import time
from enemy import Boss
os.system('clear')
print('Hello there!, Welcome to The Mandalorian.')
print('Press any key to continue.')
yo = Get().__call__()
print('Here we go')


screen = Board(30, 500, 100, 0)
screen.initialize_board()
landscape = Landscape(screen)
landscape.initialise_ground(screen)
landscape.initialise_coins(screen)
landscape.initialise_beams(screen)
landscape.initialise_magnets(screen)
boss = Boss(screen.getNoOfColumns() - 45, screen.getNoOfRows() -
            26, 13, 41, [], 5, Fore.YELLOW)
mando_figure = [["`", "[", "]"], ["[", "|", "|"], ["\"", "/", "\\"]]
myMando = Mando(0, 24, 3, 3, mando_figure, 5, Fore.RED)
myMando.placeMando(screen)
curr_time = time()
initial_time = time()
while True:
    screen.print_board(myMando, boss)
    char = input_to(Get())
    myMando.move(char, screen, landscape)
    if screen.getFrameStart() >= screen.getNoOfColumns() - screen.getFrameSize():
        if boss.isBossAlive() == True:
            boss.move(char, screen, landscape)
            boss.placeBoss(screen)
            if int(time()) % 2 == 0:
                boss.generateBullet(screen, landscape)
            boss.moveAllBullets(screen, landscape, myMando)
        else:
            for bullet in boss.getBulletPositions():
                screen.placeObject(bullet.getYcoordinate(),
                                   bullet.getXcoordinate(), ' ')
                boss.getBulletPositions().remove(bullet)
    myMando.mandoAttract(landscape)
    myMando.placeMando(screen)
    myMando.moveAllBullets(screen, landscape, boss)
    landscape.printMagnets(screen)
    if screen.getFrameStart() < screen.getNoOfColumns() - screen.getFrameSize() and time() - curr_time >= screen.getFrameVelocity():
        screen.updateFrameStart()
        screen.updateFrameStart()
        curr_time = time()
    if char == 'q':
        os.system('clear')
        print('You Pressed q')
        print('Game exited')
        exit()
    if boss.isBossAlive() == False:
        os.system('clear')
        print("You Won!")
        print("Your Score : ", myMando.getScore())
        print("Coins Collected : ", myMando.getCoins())
        exit()
