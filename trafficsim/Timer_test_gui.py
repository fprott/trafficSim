import pygame, math

import pygame.gfxdraw
import numpy as np
import matplotlib.pyplot as plt





status = pygame.init()
print(status)
disp=pygame.display.set_mode((800,600))
pygame.display.set_caption('help')

class Street:
    def __init__(self,x1,y1,x2,y2,width ):
        self.x1 = x1
        self.x2 = x2
        self.y1 = y1
        self.y2 = y2
        self.width = width
        #self.length = math.sqrt(math.pow(abs(x2-x1),2)+math.pow(abs(y2-y1),2))

    def drawstreet(self,screen):
        grey = (128, 128, 128)
        pygame.draw.line(screen, grey,(self.x1,self.y1),(self.x2,self.y2), self.width)
        pygame.draw.circle(screen, (0,0,0), (self.x1, self.y1), 2, 0)
        pygame.draw.circle(screen, (0, 0, 0), (self.x2, self.y2), 2, 0)

    def streetmerge(self,street2):
        if self.x1 == street2.x1 and self.y1 == street2.y1:
            if self.x1 == self.x2:
                if self.y2>self.y1:
                  h=1
        elif self.x1 == street2.x2 and self.y1 == street2.y2:
            f
        elif self.x2 == street2.x2 and self.y2 == street2.y2:
            f
        else:
            print('can t merge')





white=(255,255,255)
black=(0,0,0)
x = np.linspace(0, 500, 500)
y = 50*np.sin(0.01*x)+200
xvals = np.linspace(0, 500, 5000)
yvals = np.interp(xvals, x, y)




while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    disp.fill(white)
   #pygame.draw.rect
    #street(1,2,3,4,disp,3)
    #pygame.draw.polygon(disp, black, [(300, 110), (400, 110), (400, 450),(300,450)], 0)
    #street(100,100,400,100,disp,100)


    #street(300,100,300,400,disp,80)
    #street(300, 400, 600, 400, disp, 80)
    #street(500, 320, 600, 220, disp, 80)
    a=Street(300,100,300,400,40)
    a.drawstreet(disp)
    b=Street(300, 400, 600, 400,40)
    b.drawstreet(disp)
    c=Street(300,100,150,100,40)
    c.drawstreet(disp)
    a.streetmerge(c)

    #x = np.array([300,300,600])
    #y = np.array([100,400,400])


    i = 0
    while i < x.size-1:
        pygame.draw.line(disp, black, (x[i], y[i]), (x[i+1], y[i+1]), 40)
        i += 1




    pygame.display.update()



#pygame.quit()
