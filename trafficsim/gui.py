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
import numpy
import pygame
from qt_design import Ui_qt_design
from PyQt5 import QtWidgets, QtGui, QtCore
from mathe import *


class QTDesignWidget(QtWidgets.QMainWindow, Ui_qt_design): # Erbebt von qt_design aus dem qtDesigner
    """
    QT Haupt Fenster, nutzt auto generietes qt Design
    Hier werden die Events gesteuert
    Hier werden die Buttons und Menüs verwaltet
    Das Fenster hält die Zeichenfläche.
    Wichtiges Ding
    """
    def __init__(self, pyGameDrawingBoard, parent=None):
        super(QTDesignWidget, self).__init__(parent)
        self.setupUi(self)
        self.drawingBoard = pyGameDrawingBoard
        self.drawingBoardWidget = ImageWidget(self.drawingBoard.surface)
        self.setCentralWidget(self.drawingBoardWidget)
        #register Buttons
        self.actionDrawStreet.triggered.connect(self.on_actionDrawStreet_triggered)
        self.actionDeleteRoad.triggered.connect(self.on_actionDeleteRoad_triggered)

    def on_actionDrawStreet_triggered(self):
        if(self.actionDeleteRoad.isChecked()):
            self.actionDrawStreet.setChecked(False)

    def on_actionDeleteRoad_triggered(self):
        if(self.actionDrawStreet.isChecked()):
            self.actionDeleteRoad.setChecked(False)

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
        if self.actionDrawStreet.isChecked(): # wenn wir zeichnen wollen
            if (self.isOnDrawingBoard(event.pos().x(),event.pos().y())==True):
                drawX = event.pos().x()-self.drawingBoardWidget.pos().x()
                drawY = event.pos().y()-self.drawingBoardWidget.pos().y()
                self.drawingBoard.streetPoints.append((drawX, drawY))
                self.drawingBoard.drawPoint(drawX, drawY)


        if self.actionDeleteRoad.isChecked(): # wir achten darauf das nicht beide Knöpfe gleichzeitig an sind !
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
        self.drawingBoardWidget = ImageWidget(self.drawingBoard.surface) #TODO Besser machen ! Super inefektiv :D
        self.setCentralWidget(self.drawingBoardWidget)

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
        self.surface = pygame.Surface((640, 480))
        self.surface.fill((25,235,25)) #grüne Hintergrundsfarbe, default
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


def main():
    Strasse = StreetSystem
    drawingBoard = PyGameDrawingBoard()     #pygame Draw Board
    app = QtWidgets.QApplication(sys.argv)
    form = QTDesignWidget(drawingBoard)     #QT Windows
    form.show()
    app.exec_()


if __name__ == '__main__': #this will call the main if this file is called as main
    main()
