
import pygame, sys, time
import numpy as np
from pygame.locals import *
from zeichnen import *

white = (255, 255, 255)
black = (20, 20, 40)
red = (255, 0, 0)
blue = (0, 255, 0)
green = (127,255, 212)
cyan = (0, 255, 255)
gray = (128, 128, 128)

# constants
pygame.init()
fpsClock = pygame.time.Clock()

# initialize and prepare screen
#draw = pygame_Draw(500, 500)
screen = pygame.display.set_mode((500,500),0,32)
pygame.display.set_caption('Traffic Simulation')

class Street():
    def __init__(self,XDIM = 500,YDIM = 500):
        self.XDIM = XDIM
        self.YDIM = XDIM
        self.WINSIZE = [XDIM, YDIM]
        self.EPSILON = 7.0
        self.NUMNODES = 5000
        self.GOAL_RADIUS = 10
        self.MIN_DISTANCE_TO_ADD = 1.0
        self.GAME_LEVEL = 1
    def draw(self):
        pygame.init()

        #draw = pygame_Draw(self.XDIM,self.YDIM)
        #draw.screen = pygame.display.set_mode(self.WINSIZE)
        pygame.display.set_caption('Traffic Simulation')

class Car:
    def __init__(self, color, pos_y):
        self.image_filename = 'car_' + color + '.png'
        self.image = pygame.image.load(self.image_filename).convert()
        self.image = pygame.transform.scale(self.image, (10, 10))
        self.rect_def = self.image.get_rect()
        self.rect_def.y = pos_y
        self.rect_def.x = 50
        self.color = color + ' car'
        screen.blit(self.image, self.rect_def)

    def move(self):
        self.dx = 10#randint(10, 25)
        self.rect_def.x = self.dx + self.rect_def.x
        screen.blit(self.image, self.rect_def)

def test_1():
    draw = Street(500, 500)

    Strasse = math_Strasse
    nPoints = 10
    Strasse_Punkte = [[0, 4.5], [11, 5]]#, [10.5, -2],[1, -6], [-5, -5], [-10, 3], [-4, 6],[0, 4.5]]
    #Strasse_Punkte = np.array([[0, 4.5], [11, 5], [10.5, -2], [1, -6], [-5, -5], [-10, 3], [-4, 6],[0, 4.5]]) * 10+[XDIM/2,YDIM/2] # [[0,0],[2,2],[5,0],[5,-1],[2,-3]]
    #Strasse_Punkte = ((100,100),(100,150),(150,200),(200,400))  # [[0,0],[2,2],[5,0],[5,-1],[2,-3]]
    # Strasse_Punkte = np.random.rand(nPoints,2)*20
    Polygon_Punkte = np.array(Strasse.Polygon_Punkte(Strasse, points=Strasse_Punkte, bereite=3))*10+[draw.XDIM/2,draw.YDIM/2]
    print(Polygon_Punkte)

    k=0;temp=True
    while temp==True:
        screen.fill(green)
        print(tuple(Strasse_Punkte[i] for i in range(len(Strasse_Punkte))))
        pygame.draw.polygon(screen,gray, tuple(Polygon_Punkte[i] for i in range(len(Polygon_Punkte))))
        # Strasse.DrawPolygon(Strasse,vertices=Strasse_Punkte,color=(128,128,128))
        pygame.display.update()
        fpsClock.tick(10000)
        k=k+1
        if k>100:
            temp=False

if __name__ == "__main__":
    test_1()
