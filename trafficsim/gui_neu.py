"""
GUI mit PyQT5 und PyGame

PyQT5 wird für die Events und das Menü genutzt. PyGame wird als einfache, leichtnutzbare Zeichenfläche genutzt

TODO:
    * Punkte ineinander überführen wenn nahe genug (was ist nahe genug ???)
    * Immer Punkte im Paar setzen (Levi sollte dafür erstmal die Punkte beschreiben :D)
    * Zeichenfläche an Fenster anpassen (ist das sinnvoll???)
    * Ganz viel zeugs
"""
import sys
import inspect
import numpy as np
import pygame
from qt_design_neu import *#Ui_qt_design
from PyQt5 import QtWidgets, QtGui, QtCore
import PyQt5
from mathe import *
#from pygame_draw import *
#  from fahrzeug_model import *
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QHBoxLayout, QGroupBox, QDialog, QVBoxLayout, QGridLayout
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot

Punkte_Nets = []

white = (255, 255, 255)
black = (20, 20, 40)
red = (255, 0, 0)
blue = (0, 255, 0)
green = (127,255, 212)
cyan = (0, 255, 255)
gray = (128, 128, 128)
BackGroundColor = (25,235,25)

class QTDesignWidget(QtWidgets.QMainWindow, Ui_MainWindow): # Erbebt von qt_design aus dem qtDesigner
    """
    QT Haupt Fenster, nutzt auto generietes qt Design
    Hier werden die Events gesteuert
    Hier werden die Buttons und Menüs verwaltet
    Das Fenster hält die Zeichenfläche.
    Wichtiges Ding
    """
    def __init__(self,pyGameDrawingBoard ,parent=None):
        super(QTDesignWidget, self).__init__(parent)
        self.setupUi(self)
        self.drawingBoard = pyGameDrawingBoard
        self.drawingBoardWidget = ImageWidget(self.drawingBoard.surface)

        self.lable_1 = QtWidgets.QLabel(self.frame_Strasse)
        self.lable_1.setGeometry((QtCore.QRect(0, 0, 500, 500)))
        self.lable_1 = QVBoxLayout()
        self.lable_1.addWidget(self.drawingBoardWidget)
        self.frame_Strasse.setLayout(self.lable_1)

        #self.pushButton1 = QtWidgets.QPushButton("PyQt5 button")'

        #self.setCentralWidget(self.drawingBoardWidget)
        #self.tabWidget.setCornerWidget(self.drawingBoardWidget)
        #register Buttons
        self.pushButton_Add_Strasse.clicked.connect(self.on_pushButton_Add_Strasse_triggered)
        self.pushButton_Add_Strasse.clicked.connect(self.on_pushButton_Add_Strasse_triggered)

    def on_pushButton_Add_Strasse_triggered(self):
        if(self.pushButton_Losen_Strasse.isChecked()):
            self.pushButton_Add_Strasse.setChecked(False)

    def on_pushButton_Losen_Strasse_triggered(self):
        if(self.pushButton_Add_Strasse.isChecked()):
            self.pushButton_Losen_Strasse.setChecked(False)

    def isOnDrawingBoard(self, x, y):
        boardX = self.drawingBoardWidget.pos().x()
        boardY = self.drawingBoardWidget.pos().y()
        boardHeight = self.drawingBoard.surface.get_size()[1]#self.drawingBoardWidget.size().height()
        boardWidth = self.drawingBoard.surface.get_size()[0]#self.drawingBoardWidget.size().width()
        # wenn wir zuweit oben oder links sind
        if x<boardX:
            return False
        if y<boardY:
            return False
        #wenn wir über dem board hinaus sind
        if x>boardX+boardWidth:
            return False
        if y>boardY+boardHeight:
            return False
        return True

    def mousePressEvent(self, event):
        if self.pushButton_Add_Strasse.isChecked(): # wenn wir zeichnen wollen
            if (self.isOnDrawingBoard(event.pos().x(),event.pos().y())==True):
                drawX = event.pos().x()-self.drawingBoardWidget.pos().x()
                drawY = event.pos().y()-self.drawingBoardWidget.pos().y()
                self.drawingBoard.streetPoints.append((drawX, drawY))
                self.drawingBoard.drawPoint(drawX, drawY)
                Punkte_Nets.append([drawX, drawY])
                print(Punkte_Nets)
                if (len(Punkte_Nets)>1):
                    print(len(Punkte_Nets))
                    Polygon_Punkte = math_Strasse.Polygon_Punkte(self=math_Strasse,points=Punkte_Nets,bereite=20)
                    self.drawingBoard.drawStrasse(Polygon_Punkte)

        if self.pushButton_Losen_Strasse.isChecked(): # wir achten darauf das nicht beide Knöpfe gleichzeitig an sind !
            if (self.isOnDrawingBoard(event.pos().x(),event.pos().y())):
                #wenn ein Punkt in der nähe ist
                drawX = event.pos().x() - self.drawingBoardWidget.pos().x()
                drawY = event.pos().y() - self.drawingBoardWidget.pos().y()
                pointPos = self.drawingBoard.getNearestPointWithinXY(drawX,drawY,25)
                if(pointPos is not None): # wenn es einen Punkt gibt
                    self.drawingBoard.streetPoints.remove(pointPos)
                    self.drawingBoard.unDrawPoint(pointPos[0],pointPos[1])

            # QtWidgets.QApplication.processEvents() # irgenwie geht das Update nicht XD
            # self.drawingBoardWidget.repaint()
            # self.drawingBoardWidget.update()
            # self.drawingBoardWidget.show()
            # QtWidgets.QApplication.processEvents()

        # Aktuallisiert die Anzeige !!!
        #self.drawingBoardWidget = ImageWidget(self.drawingBoard.surface) #TODO Besser machen ! Super inefektiv :D
        #self.setCentralWidget(self.drawingBoardWidget)
        self.drawingBoardWidget = ImageWidget(self.drawingBoard.surface)
        self.lable_1 = QtWidgets.QLabel(self.frame_Strasse)
        self.lable_1.setGeometry((QtCore.QRect(0, 0, 500, 500)))
        self.lable_1 = QVBoxLayout()
        self.lable_1.addWidget(self.drawingBoardWidget)
        self.frame_Strasse.setLayout(self.lable_1)

class ImageWidget(QtWidgets.QWidget):
    """
    Qt Haupt Image, enhällt pygame in das wir zeichnen bzw. das wir als Zeichenfläche nutzen
    Nicht sonderlich wichtig.
    """
    def __init__(self,surface,parent=None):
        super(ImageWidget,self).__init__(parent)
        w=surface.get_width()
        h=surface.get_height()
        self.data=surface.get_buffer().raw
        self.image=QtGui.QImage(self.data,w,h,QtGui.QImage.Format_RGB32)

    def paintEvent(self,event): # FIXME, das ding zeichnet nicht wirklich neu, es sei denn man erneuert das Widget
        qp=QtGui.QPainter()
        qp.begin(self)
        qp.drawImage(0,0,self.image)
        qp.end()

class PyGameDrawingBoard():
    """
    Eine Instanz von PyGame die wir zum Zeichnen der Straße und Animation nutzen
    In dieser Instanz werden ALLE Zeichnungen gemacht
    """
    def __init__(self):
        pygame.init()
        pygame.event.pump() # sollte die pygame events handeln, wir nutzen die qt events weil die besser sind (keinen loop brauchen)
        self.surface = pygame.Surface((500, 500))
        self.surface.fill(BackGroundColor) #grüne Hintergrundsfarbe, default
        self.streetPoints = [] #liste von Punkten, bis ich besseres weiß halte ich die Punkte erstmal als tuple

    def scaleToWindowSize(self, width, height): # FIXME noch nicht getestet
        """
        Diese Funktion soll die Zeichenfläche an das Fenster anpassen
        :param width: die Höhe des Fensters
        :param height: die Breite des Fensters
        :return: None
        """
        pygame.transform.scale(self.surface, (width, height))

    def getNearestPointWithinXY(self,x,y,abstandMax):
        """
        Gibt den nächsten Punkt auf der Karte zurück sollange dieser im Abstand von radiusMax liegt
        :param x: X Kordinaten
        :param y: Y Kordinaten
        :param abstandMax: Maximaler abstand zum Punkt. ACHTUNG: kein Radius, X bzw. Y werden einzelnd betrachtet !
        :return: den nächsten Punkt
        """
        #was ein abfuck, diese Funktion ist super blöd aber ich habe keine Zeit mehr
        #TODO : Diese Funktion schön machen
        possiblePoints=[]
        for k in range(0,abstandMax):
            for streetPoint in self.streetPoints:
                if streetPoint[0]+k == x:
                    possiblePoints.append(streetPoint) #möglich Lösung gefunden
                if streetPoint[0] - k == x:
                    possiblePoints.append(streetPoint) #möglich Lösung gefunden

        for k in range(0, abstandMax):
            for streetPoint in possiblePoints:
                if streetPoint[1] + k == y:
                    return streetPoint
                if streetPoint[1] - k == y:
                    return streetPoint # lösung

        return None # wenn wir nix finden haben wir keine Lösung

    def drawPoint(self, x, y):
        """
        Zeichnet einen Punkt als kleiner, blauer Punkt (3 Pixel radius) dargestellt auf die Karte
        Args:
            :param1 (int) : X Kordinate auf der Map (Pixel)
            :param2 (int) : Y Kordinate auf der Map (Pixel)
        """
        pygame.draw.circle(self.surface , (0,0,255), (x, y), 3)

    #def drawPolygon(self, TODO):
        #pygame.draw.polygon(self.surface, gray, tuple(Polygon_Punkte[i] for i in range(len(Polygon_Punkte))))

    def unDrawPoint(self, x, y):
        """
        Entfernt einen Punkt(3 Pixel radius) von der Karte
        Args:
            :param1 (int) : X Kordinate auf der Map (Pixel)
            :param2 (int) : Y Kordinate auf der Map (Pixel)
        """
        #Soweit ich das sehe gibt es keine Möglichkeit den Punkt zu löschen, daher übermalen wir Ihn
        #TODO Prüfen ob man Zeichnungen enfernen kann oder übermalen muss
        pygame.draw.circle(self.surface , (25,235,25), (x, y), 3) #crapy fix but who cares

    def drawStrasse(self,Polygon_Punkte):
        self.surface.fill(BackGroundColor)
        pygame.draw.polygon(self.surface, gray, tuple(Polygon_Punkte[i] for i in range(len(Polygon_Punkte))))

    def drawFahrzeug(self,x,y,winkel):
        self.image_filename = 'qt_creator\icons\car_' + 'red' + '.png'
        self.image = pygame.image.load(self.image_filename)#.convert()
        self.image = pygame.transform.scale(self.image, (25,50))
        self.image = pygame.transform.rotate(self.image,winkel-180)
        self.rect_def = self.image.get_rect()
        self.rect_def.y = y
        self.rect_def.x = x
        self.surface.blit(self.image,self.rect_def)

def main():
    drawingBoard = PyGameDrawingBoard()     #pygame Draw Board
    drawingBoard.drawFahrzeug(100,100,0)
    app = QtWidgets.QApplication(sys.argv)
    form = QTDesignWidget(drawingBoard)     #QT Windows
    form.show()
    app.exec_()


if __name__ == '__main__': #this will call the main if this file is called as main
    main()
