import pygame
import numpy as np
import math
from pygame.locals import *
from sys import exit
from zeichnen import *


def polygon(points):
    pygame.init()
     #fpsClock = pygame.time.Clock()
    screen = pygame.display.set_mode((640, 480), 0, 32)


    Strasse = math_Strasse
    # points=main_strasse.Polygon_Punkte
    # points=(array([  99.95459234,  105.99896854]), array([ 211.07754863,  111.05001201]), array([ 205.88605073,   38.36904131]), array([  47.49404802,  125.75773246]), array([ 100.35112344,  105.93632918]), array([  99.64887656,  104.06367082]), array([  72.50595198,  114.24226754]), array([ 204.11394927,   41.63095869]), array([ 208.92245137,  108.94998799]), array([ 100.04540766,  104.00103146]))
    Polygon_Punkte = np.array(Strasse.Polygon_Punkte(Strasse, points=points, bereite=10))  # +[640/2,480/2]
    # print(list(Polygon_Punkte)[0][1])
    Polygon_Punkte = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    print((Polygon_Punkte))
    print(list(Polygon_Punkte)[0:2][0])

    while True:

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()
            if event.type == MOUSEBUTTONDOWN:
                screen.fill((255, 255, 255))
                pygame.draw.polygon(screen, (255, 0, 0), tuple(Polygon_Punkte[i] for i in range(len(Polygon_Punkte))))
        pygame.display.update()


if __name__ == "__main__":
    polygon(points = [[200, 100], [200, 300], [616, 417], [600,100]])
