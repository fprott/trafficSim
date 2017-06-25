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
import pygame
from qt_design_neu import *#Ui_qt_design
from PyQt5 import QtWidgets, QtGui, QtCore
from mathe import *
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QHBoxLayout, QGroupBox, QDialog, QVBoxLayout, QGridLayout
from parameter import *

Punkte_Nets = []
FahrzeugePunkte_Nets = []
Klick_Time = 0

white = (255, 255, 255)
black = (20, 20, 40)
red = (255, 0, 0)
blue = (0, 0,255)
green = (0,255, 0)
gray = (128, 128, 128)
purpur = (104, 34, 139)
yellow = (255, 255, 0)
BackGroundColor = (25,235,25)

class QTDesignWidget(QtWidgets.QMainWindow, Ui_MainWindow,math_Kurve,math_Strasse): # Erbebt von qt_design aus dem qtDesigner
    """
    QT Haupt Fenster, nutzt auto generietes qt Design
    Hier werden die Events gesteuert
    Hier werden die Buttons und Menüs verwaltet
    Das Fenster hält die Zeichenfläche.
    Wichtiges Ding
    """
    Klick_Time = 0;
    Klick_Time_Strasse = 0;
    Klick_Time_Fahrzeug = 0;
    Fahrbahn_Points = [];
    type_Farbe_List = [blue,black,green,purpur,red,white,yellow,white]
    def __init__(self,pyGameDrawingBoard ,parent=None):
        super(QTDesignWidget, self).__init__(parent)
        self.setupUi(self)
        self.drawingBoard_Strasse = pyGameDrawingBoard
        self.drawingBoardWidget_Strasse = ImageWidget(self.drawingBoard_Strasse.surface)
        self.drawingBoard_Fahrzeug = pyGameDrawingBoard
        self.drawingBoardWidget_Fahrzeug = ImageWidget(self.drawingBoard_Fahrzeug.surface)
        self.drawingBoard_Simulation = pyGameDrawingBoard
        self.drawingBoardWidget_Simulation = ImageWidget(self.drawingBoard_Simulation.surface)

        #self.tab_Strasse.mouseDoubleClickEvent(self.erneuen_Frame_Strasse())
        #self.tab_Fahrzeug.mouseDoubleClickEvent(self.erneuen_Frame_Fahrzeug())
        #TODO Die unterschiedliche Lable kann nicht isoliert werden.
        # pygame on frame_Strasse
        self.lable_1 = QtWidgets.QLabel(self.frame_Strasse)
        self.lable_1.setGeometry((QtCore.QRect(0, 0, 500, 500)))
        self.lable_1 = QVBoxLayout()
        self.lable_1.addWidget(self.drawingBoardWidget_Strasse)
        self.frame_Strasse.setLayout(self.lable_1)
        # pyQt5 Button - Event Connection
        self.pushButton_Losen_Strasse.clicked.connect(self.event_Button_Losen_Strasse)
        self.treeView_Strasse.clicked.connect(self.event_treeWidget_Strasse)

        #pygame on frame_Fahrzeug
        self.lable_2= QtWidgets.QLabel(self.frame_Fahrzeug)
        self.lable_2.setGeometry((QtCore.QRect(0, 0, 500, 500)))
        self.lable_2= QVBoxLayout()
        self.lable_2.addWidget(self.drawingBoardWidget_Fahrzeug)
        self.frame_Fahrzeug.setLayout(self.lable_2)
        # pyQt5 Button - Event Connection
        self.pushButton_Losen_Fahrzeug.clicked.connect(self.event_Button_Losen_Fahrzeug)
        self.treeView_Fahrzeug.clicked.connect(self.event_treeWidget_Fahrzeug)

        #pygame on frame_Simulation
        self.lable_3= QtWidgets.QLabel(self.frame_Simulation)
        self.lable_3.setGeometry((QtCore.QRect(0, 0, 500, 500)))
        self.lable_3= QVBoxLayout()
        self.lable_3.addWidget(self.drawingBoardWidget_Simulation)
        self.frame_Simulation.setLayout(self.lable_3)
        #pyQt5 QSlider - Event Connection
        self.horizontalSlider_Simulation.valueChanged.connect(self.event_Erneuen_Fahrzeugen)

        #self.pushButton1 = QtWidgets.QPushButton("PyQt5 button")'

        #register Buttons
        self.pushButton_Add_Strasse.clicked.connect(self.on_pushButton_Add_Strasse_triggered)
        self.pushButton_Losen_Strasse.clicked.connect(self.on_pushButton_Losen_Strasse_triggered)
        self.pushButton_Add_Fahrzeug.clicked.connect(self.on_pushButton_Add_Fahrzeug_triggered)
        self.pushButton_Losen_Fahrzeug.clicked.connect(self.on_pushButton_Losen_Fahrzeug_triggered)

    # Button Triggered
    def on_pushButton_Add_Strasse_triggered(self):
        if(self.pushButton_Losen_Strasse.isChecked()):
            self.pushButton_Add_Strasse.setChecked(False)
        if(self.pushButton_Add_Strasse.isChecked()==True):
            self.Klick_Time_Strasse = 0;
        elif(self.pushButton_Add_Strasse.isChecked()==False):
            if (len(Punkte_Nets)!=0):
                Punkte_Nets.insert(0,int(self.lineEdit_Str_Bereite.text()))
                print('1:'+str(Punkte_Nets))
                Strassen_Nets.append(Punkte_Nets);
                print('2:'+str(Strassen_Nets))
                del(Punkte_Nets[:]);
                print('3:'+str(Punkte_Nets))

        # erneue die pygame Inhalt in frame_Strasse
        self.erneuen_Frame_Strasse()

    def on_pushButton_Losen_Strasse_triggered(self):
        if(self.pushButton_Add_Strasse.isChecked()):
            self.pushButton_Losen_Strasse.setChecked(False)

    def on_pushButton_Add_Fahrzeug_triggered(self):
        if(self.pushButton_Losen_Strasse.isChecked()):
            self.pushButton_Losen_Fahrzeug.setChecked(False)
        if(self.pushButton_Add_Fahrzeug.isChecked()==True):
            self.Klick_Time_Fahrzeug = 0;
        elif(self.pushButton_Add_Fahrzeug.isChecked()==False):
            if (len(FahrzeugePunkte_Nets)!=0):
                type = self.comboBox_Fahrzeug.currentIndex()
                Points = [[FahrzeugePunkte_Nets[0][0], FahrzeugePunkte_Nets[0][1]], [FahrzeugePunkte_Nets[1][0],FahrzeugePunkte_Nets[1][1]]]
                Richtung = self.Richtung(Points) + 180
                self.drawingBoard_Fahrzeug.drawFahrzeug(type, FahrzeugePunkte_Nets[0][0], FahrzeugePunkte_Nets[0][1], Richtung, 20)

                #TODO: Die Kurve Funktion brauchen weite bearbeitet werden.
                print(FahrzeugePunkte_Nets)
                xvals, yvals = self.Bezier_Kurve(points=FahrzeugePunkte_Nets)
                colour = self.type_Farbe_List[self.comboBox_Fahrzeug.currentIndex()]
                self.drawingBoard_Fahrzeug.drawKurve(xvals, yvals, colour)

                FahrzeugePunkte_Nets.insert(0,int(self.comboBox_Fahrzeug.currentIndex()))
                print('1:'+str(Punkte_Nets))
                Fahrzeuge_Nets.append(FahrzeugePunkte_Nets);
                print('2:'+str(Fahrzeuge_Nets))
                del(FahrzeugePunkte_Nets[:]);
                print('3:'+str((FahrzeugePunkte_Nets)))

        # erneue die pygame Inhalt in frame_Strasse
        self.erneuen_Frame_Fahrzeug()

    def on_pushButton_Losen_Fahrzeug_triggered(self):
        if(self.pushButton_Add_Fahrzeug.isChecked()):
            self.pushButton_Losen_Fahrzeug.setChecked(False)

    def isOnDrawingBoard(self,drawingBoard,drawingBoardWidget, x, y):
        boardX = drawingBoardWidget.pos().x()
        boardY = drawingBoardWidget.pos().y()
        boardHeight = drawingBoard.surface.get_size()[1]#self.drawingBoardWidget.size().height()
        boardWidth = drawingBoard.surface.get_size()[0]#self.drawingBoardWidget.size().width()
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
        self.Klick_Time = self.Klick_Time +1;
        print("Klick Time is %d"%(self.Klick_Time))
        #prufen die current tabWidget
        ########################################################
        #wenn the currentWidget is tab_Strasse
        ########################################################
        if self.tabWidget.currentWidget()==self.tab_Strasse:
            print('tab_Strasse')

            # wenn wir zeichnen wollen
            if self.pushButton_Add_Strasse.isChecked():
                if (self.isOnDrawingBoard(self.drawingBoard_Strasse,self.drawingBoardWidget_Strasse,event.pos().x(), event.pos().y()) == True):

                    self.Klick_Time_Strasse = self.Klick_Time_Strasse + 1;
                    print("Klick Time Strasse is %d"%(self.Klick_Time_Strasse))

                    drawX = event.pos().x() - self.drawingBoardWidget_Strasse.pos().x() - 20
                    drawY = event.pos().y() - self.drawingBoardWidget_Strasse.pos().y() - 20 - 21 - 21
                    self.drawingBoard_Strasse.streetPoints.append((drawX, drawY))
                    self.drawingBoard_Strasse.drawPoint(drawX, drawY,blue)

                    # Add die Strasse Punkt zum Punkte_Nets
                    Punkte_Nets.append([drawX, drawY])
                    print(Punkte_Nets)

                    if (len(Punkte_Nets) > 1):
                        # Zeichnen die Strasse
                        print(len(Punkte_Nets))
                        strasse_Bereite = int(self.lineEdit_Str_Bereite.text())
                        Polygon_Punkte = math_Strasse.Polygon_Punkte(self,points=Punkte_Nets, bereite=strasse_Bereite)
                        self.drawingBoard_Strasse.drawStrasse(Polygon_Punkte)
                        self.statusBar.showMessage('Draw Strasse.')

                    #Erneuen die TreeWidget
                    #TODO: Die TreeWidget brauchen noch bearbeitet wird.
                    if (self.Klick_Time_Strasse == 1):
                        root = QtWidgets.QTreeWidgetItem(self.treeView_Strasse)
                        root.setText(0, 'Strasse')
                        root.setText(1, str([drawX,drawY]))
                        root.setSelected(True)
                    else:
                        child1 = QtWidgets.QTreeWidgetItem(self.treeView_Strasse)
                        child1.setText(0, 'Point %d'%self.Klick_Time_Strasse)
                        child1.setText(1, str([drawX,drawY]))

            # erneue die pygame Inhalt in frame_Strasse
            self.erneuen_Frame_Strasse()

        ########################################################
        #wenn the currentWidget is tab_Fahrzeug
        ########################################################
        elif self.tabWidget.currentWidget()==self.tab_Fahrzeug:
            print('tab_Fahrzeug')

            # wenn wir Fahrzeug plazieren wollen
            if self.pushButton_Add_Fahrzeug.isChecked():
                if (self.isOnDrawingBoard(self.drawingBoard_Fahrzeug,self.drawingBoardWidget_Fahrzeug,event.pos().x(), event.pos().y()) == True):

                    self.Klick_Time_Fahrzeug = self.Klick_Time_Fahrzeug + 1;
                    print("Klick Time Fahrzeug is %d" % (self.Klick_Time_Fahrzeug))

                    drawX = event.pos().x() - self.drawingBoardWidget_Fahrzeug.pos().x() - 20
                    drawY = event.pos().y() - self.drawingBoardWidget_Fahrzeug.pos().y() - 20 - 21 - 21
                    FahrzeugePunkte_Nets.append([drawX, drawY])

                    # Erneuen die TreeWidget
                    #TODO: Die TreeWidget brauchen noch bearbeitet wird.
                    colour = self.type_Farbe_List[self.comboBox_Fahrzeug.currentIndex()]
                    if(self.Klick_Time_Fahrzeug==1):
                        self.drawingBoard_Fahrzeug.drawPoint(drawX, drawY, colour)
                        self.statusBar.showMessage('Draw Fahrzeug.')

                        root = QtWidgets.QTreeWidgetItem(self.treeView_Fahrzeug)
                        root.setText(0, 'Fahrzeug')
                        root.setText(1, str([drawX,drawY]))
                        root.setSelected(True)
                    #self.treeView_Fahrzeug.setCurrentItem(root)
                    else:
                        self.drawingBoard_Fahrzeug.drawPoint(drawX, drawY, colour)

                        child1 = QtWidgets.QTreeWidgetItem(self.treeView_Fahrzeug)
                        child1.setText(0, 'Point %d'%(self.Klick_Time_Fahrzeug-1))
                        child1.setText(1, str([drawX,drawY]))

            # erneue die pygame Inhalt in frame_Strasse
            self.erneuen_Frame_Fahrzeug();


        ########################################################
        #wenn the currentWidget is tab_Simulation
        ########################################################
        elif self.tabWidget.currentWidget()==self.tab_Simulation:
            self.drawingBoard_Simulation.surface.fill(BackGroundColor)
            self.event_Erneuen_Strassen()
            print('tab_Simulation')


            # QtWidgets.QApplication.processEvents() # irgenwie geht das Update nicht XD
            # self.drawingBoardWidget.repaint()
            # self.drawingBoardWidget.update()
            # self.drawingBoardWidget.show()
            # QtWidgets.QApplication.processEvents()

    def event_Erneuen_Strassen(self):
        # Zeichnen die Strassen , wahrend simulation
        self.drawingBoard_Simulation.surface.fill(BackGroundColor)
        print(Strassen_Nets)
        for i in range(len(Strassen_Nets)):
            # #TODO Die neue Strassen kann nicht in Strassen_Nets gespeichert werden
            Points = list(Strassen_Nets[i][1:len(Strassen_Nets[i])])
            print(Points)
            print(len(Strassen_Nets))
            print(Strassen_Nets[i])
            Bereite = int(Strassen_Nets[i][0])
            Polygon_Punkte = self.Polygon_Punkte(points=Points, bereite=Bereite)
            self.drawingBoard_Simulation.drawStrasse(Polygon_Punkte)

    def event_Erneuen_Fahrzeugen(self,time):
        self.event_Erneuen_Strassen()
        # Zeichnen die Fahrzeugen , wahrend simulation
        for i in range(len(Fahrbahn_Nets)):
            # Die Fahrbahn_Nets speichern alle Positions-Punkte alles Fahrzeugen durch die ganze Simulation
            drawX = Fahrbahn_Nets[i][time][0]
            drawY = Fahrbahn_Nets[i][time][1]
            if time<(len(Fahrbahn_Nets[i])-1):
                Points = [[drawX,drawY],[Fahrbahn_Nets[i][time+1][0],Fahrbahn_Nets[i][time+1][1]]]
            else:
                Points = [[Fahrbahn_Nets[i][time-1][0],Fahrbahn_Nets[i][time-1][1]],[drawX,drawY]]
            Richtung = self.Richtung(Points)+180
            self.drawingBoard_Simulation.drawFahrzeug(Fahrzeuge_Nets[i][0],drawX, drawY, Richtung, 20)
        self.statusBar.showMessage('Simulation.')

        print(Strassen_Nets)
        # zeichnen die Schnittpunkte der Strasse
        Schnittpunkte = self.suchen_Kreuzung(Strassen_Nets)
        # for i in range(len(Schnittpunkte)):
        #     self.drawingBoard_Fahrzeug.drawPoint(int(Schnittpunkte[i][2][0]), int(Schnittpunkte[i][2][1]), red)
        print("***********************************")
        self.suchen_Punkte_Kreuzung(Strassen_Nets,Schnittpunkte)
        print("***********************************")
        # erneue die pygame Inhalt in frame_Simulation
        self.erneuen_Frame_Simulation();

    def event_Button_Losen_Strasse(self):
        #TODO: Wie kann ein Item in TreeWidget lösen?
        print(self.treeView_Strasse.currentItem())
        #self.treeView_Strasse.removeItemWidget(self.treeView_Strasse.currentItem(),1)

    def event_Button_Losen_Fahrzeug(self):
        print("abc")

    def event_treeWidget_Strasse(self):
        #TODO: Die Punkte Daten brauchen mit ENTER erneuen
        item = self.treeView_Strasse.currentItem()
        print(item.text(0),item.text(1))
        self.lineEdit_Str_Punkte.setText(item.text(1))
        #TODO: Die TreeWidget brauchen noch bearbeitet wird.
        #root = QtWidgets.QTreeWidgetItem(self.treeView_Strasse)
        #root.setText(1, '[123,123]')
        #self.treeView_Strasse.currentItemChanged(root)

    def event_treeWidget_Fahrzeug(self):
        #TODO: Die Punkte Daten brauchen mit ENTER erneuen
        item = self.treeView_Fahrzeug.currentItem()
        print(item.text(0),item.text(1))
        self.lineEdit_Fahrzeug_Punkte.setText(item.text(1))
        #TODO: Die TreeWidget brauchen noch bearbeitet wird.
        #root = QtWidgets.QTreeWidgetItem(self.treeView_Fahrzeug)
        #root.setText(1, '[123,123]')
        #self.treeView_Strasse.currentItemChanged(root)

    def erneuen_Frame_Strasse(self):
        # erneue die pygame Inhalt in frame_Strasse
        self.lable_1.removeItem(self.lable_1)
        self.drawingBoardWidget_Strasse = ImageWidget(self.drawingBoard_Strasse.surface)
        self.lable_1 = QVBoxLayout()
        self.lable_1.addWidget(self.drawingBoardWidget_Strasse)
        self.frame_Strasse.setLayout(self.lable_1)

    def erneuen_Frame_Fahrzeug(self):
        # erneue die pygame Inhalt in frame_Strasse
        self.lable_2.removeItem(self.lable_2)
        self.drawingBoardWidget_Fahrzeug = ImageWidget(self.drawingBoard_Fahrzeug.surface)
        self.lable_2 = QVBoxLayout()
        self.lable_2.addWidget(self.drawingBoardWidget_Fahrzeug)
        self.frame_Fahrzeug.setLayout(self.lable_2)

    def erneuen_Frame_Simulation(self):
        # erneue die pygame Inhalt in frame_Simulation
        self.lable_3.removeItem(self.lable_3)
        self.drawingBoardWidget_Simulation = ImageWidget(self.drawingBoard_Simulation.surface)
        self.lable_3 = QVBoxLayout()
        self.lable_3.addWidget(self.drawingBoardWidget_Simulation)
        self.frame_Simulation.setLayout(self.lable_3)

    def suchen_Kreuzung(self,Strass_Nets):
        # suchen alle Kreuzung von die Strassen
        Schnitt_Punkte = [];
        temp = False
        for i in range(len(Strass_Nets)):
            for j in range(len(Strass_Nets[i])-2):
                punkte0 = [[Strass_Nets[i][j+1][0],Strass_Nets[i][j+1][1]],
                           [Strass_Nets[i][j+2][0],Strass_Nets[i][j+2][1]]]
                line1 = self.line_function(points=punkte0);
                for k in range(len(Strass_Nets)-i):
                    if k==0:
                    # Die 2 Linie ist an der gleiche Strasse
                        for l in range(len(Strass_Nets[i+k])-2-j):
                            punkte1 = [[Strass_Nets[i+k][j+l + 1][0],Strass_Nets[i+k][j+l + 1][1]],
                                       [Strass_Nets[i+k][j+l + 2][0],Strass_Nets[i+k][j+l + 2][1]]]
                            line2 = self.line_function(points=punkte1)
                            schnittpunkt = self.Schnittspunkte(line1,line2)
                            # Prüfen ob die Schnittpunkt an der Strasse ist
                            if schnittpunkt[0] != None:
                                # Schnitt_Punkte.append([[i, j + 1], [i + k, j + l + 1], schnittpunkt])
                                if punkte0[0][0] <= punkte0[1][0] :
                                    if int(schnittpunkt[0])>=punkte0[0][0] and int(schnittpunkt[0]) <= punkte0[1][0]:
                                        temp = True
                                elif punkte0[0][0] >= punkte0[1][0]:
                                    if int(schnittpunkt[0]) >= punkte0[1][0] and int(schnittpunkt[0]) <= punkte0[0][0]:
                                        temp = True
                                if temp == True:
                                    if punkte1[0][0] <= punkte1[1][0] :
                                        if int(schnittpunkt[0])>=punkte1[0][0] and int(schnittpunkt[0]) <= punkte1[1][0]:
                                            Schnitt_Punkte.append([[i,j+1],[i+k,j+l+1],schnittpunkt])
                                    elif punkte1[0][0] >= punkte1[1][0]:
                                        if int(schnittpunkt[0]) >= punkte1[1][0] and int(schnittpunkt[0]) <= punkte1[0][0]:
                                            Schnitt_Punkte.append([[i,j+1],[i+k,j+l+1],schnittpunkt])
                    elif k>0:
                    # Die 2 Linie ist an der unterschiedliche Strasse
                        for l in range(len(Strass_Nets[i+k])-2):
                            punkte1 = [[Strass_Nets[i+k][l + 1][0],Strass_Nets[i+k][l + 1][1]],
                                       [Strass_Nets[i+k][l + 2][0],Strass_Nets[i+k][l + 2][1]]]
                            line2 = self.line_function(points=punkte1)
                            schnittpunkt = self.Schnittspunkte(line1,line2)
                            # Prüfen ob die Schnittpunkt an der Strasse ist
                            if schnittpunkt[0] != None:
                                # Schnitt_Punkte.append([[i, j + 1], [i + k, l + 1], schnittpunkt])
                                if punkte0[0][0] <= punkte0[1][0] :
                                    if int(schnittpunkt[0])>=punkte0[0][0] and int(schnittpunkt[0]) <= punkte0[1][0]:
                                        temp = True
                                    else:
                                        temp = False
                                elif punkte0[0][0] >= punkte0[1][0]:
                                    if int(schnittpunkt[0]) >= punkte0[1][0] and int(schnittpunkt[0]) <= punkte0[0][0]:
                                        temp = True
                                    else:
                                        temp = False
                                else:
                                    temp = False
                                if temp == True:
                                    if punkte1[0][0] <= punkte1[1][0] :
                                        if schnittpunkt[0]>=punkte1[0][0] and schnittpunkt[0] <= punkte1[1][0]:
                                            Schnitt_Punkte.append([[i,j+1],[i+k,l+1],schnittpunkt])
                                    elif punkte1[0][0] >= punkte1[1][0]:
                                        if schnittpunkt[0] >= punkte1[1][0] and schnittpunkt[0] <= punkte1[0][0]:
                                            Schnitt_Punkte.append([[i,j+1],[i+k,l+1],schnittpunkt])

        print(Schnitt_Punkte)
        return Schnitt_Punkte;

    def suchen_Punkte_Kreuzung(self,Strass_Nets,Schnitt_Punkte):
        # suchen die Punkte an alle Kreuzungen
        num_Punkte_1 = 0;
        num_Punkte_2 = 0;
        print("***********************")
        print(Strass_Nets)
        print(Schnitt_Punkte)
        print("************************")
        # Definiren die List. Diese List speichert alles Standard_Punkte alles Strasse
        Strassen_Standard_Punkte = [0 for Anzahl_Strassen in range(len(Strass_Nets))]
        for i in range(len(Strass_Nets)):
            print("=================================")
            Bahn = [0 for Anzahl_Bahn in range(int(Strass_Nets[i][0]/20))]

            # Add die Anfangspunkt in die List
            Strassen_Standard_Punkte[i]=Bahn
            points = [Strass_Nets[i][1],Strass_Nets[i][2]]
            points = self.Grenz_Punkte(points,Strass_Nets[i][0])
            print(Strassen_Standard_Punkte)
            for j in range(len(Bahn)):
                x = points[0][0][0] - (j+1)*(points[0][0][0] - points[0][1][0])/(len(Bahn)+1)
                y = points[0][0][1] - (j+1)*(points[0][0][1] - points[0][1][1])/(len(Bahn)+1)
                # self.drawingBoard_Strasse.drawPoint(int(x), int(y), yellow)
                Strassen_Standard_Punkte[i][j]=[0]
                Strassen_Standard_Punkte[i][j][0] = [x,y]
            # Add die Endpunkt in die List
            points = [Strass_Nets[i][-2],Strass_Nets[i][-1]]
            points = self.Grenz_Punkte(points,Strass_Nets[i][0])
            print(Strassen_Standard_Punkte)
            for j in range(len(Bahn)):
                x = points[0][2][0] - (j+1)*(points[0][2][0] - points[0][3][0])/(len(Bahn)+1)
                y = points[0][2][1] - (j+1)*(points[0][2][1] - points[0][3][1])/(len(Bahn)+1)
                # self.drawingBoard_Strasse.drawPoint(int(x), int(y), yellow)
                Strassen_Standard_Punkte[i][j].append([x, y])
            print(Strassen_Standard_Punkte)
        print("=================================")
        # Standard Punkte finden
        for i in range(len(Schnitt_Punkte)):
            # Suchen die Anzahl der Standard Punkte beides Strassen an eine Kreuzung
            num_Punkte_1 = int(Strass_Nets[Schnitt_Punkte[i][0][0]][0]/20)
            num_Punkte_2 = int(Strass_Nets[Schnitt_Punkte[i][1][0]][0]/20)
            print(num_Punkte_1,num_Punkte_2)
            # Suchen die Punkte die zwei Strassen
            points = [Strass_Nets[Schnitt_Punkte[i][0][0]][Schnitt_Punkte[i][0][1]] , Strass_Nets[Schnitt_Punkte[i][0][0]][Schnitt_Punkte[i][0][1]+1]]
            points1 = [Strass_Nets[Schnitt_Punkte[i][1][0]][Schnitt_Punkte[i][1][1]] , Strass_Nets[Schnitt_Punkte[i][1][0]][Schnitt_Punkte[i][1][1]+1]]
            print(points)
            print(points1)
            grenz_Punkte = self.Grenz_Punkte(points,20*num_Punkte_1)
            grenz_Punkte1 = self.Grenz_Punkte(points1,20*num_Punkte_2)
            # print(grenz_Punkte)
            # print(grenz_Punkte1)
            points_line11 = [grenz_Punkte[0][0],grenz_Punkte[0][2]]
            points_line12 = [grenz_Punkte[0][1],grenz_Punkte[0][3]]
            points_line21 = [grenz_Punkte1[0][0],grenz_Punkte1[0][2]]
            points_line22 = [grenz_Punkte1[0][1],grenz_Punkte1[0][3]]
            line11 = self.line_function(points_line11)
            line12 = self.line_function(points_line12)
            line21 = self.line_function(points_line21)
            line22 = self.line_function(points_line22)
            # Suchen die Grenzpunkte an einer Kreuzung
            schnittpunkt11 = self.Schnittspunkte(line11,line21)
            schnittpunkt12 = self.Schnittspunkte(line11,line22)
            schnittpunkt21 = self.Schnittspunkte(line12,line21)
            schnittpunkt22 = self.Schnittspunkte(line12,line22)
            # self.drawingBoard_Strasse.drawPoint(int(schnittpunkt11[0]), int(schnittpunkt11[1]), green)
            # self.drawingBoard_Strasse.drawPoint(int(schnittpunkt12[0]), int(schnittpunkt12[1]), green)
            # self.drawingBoard_Strasse.drawPoint(int(schnittpunkt21[0]), int(schnittpunkt21[1]), green)
            # self.drawingBoard_Strasse.drawPoint(int(schnittpunkt22[0]), int(schnittpunkt22[1]), green)
            print([schnittpunkt11,schnittpunkt12,schnittpunkt21,schnittpunkt22])
            print('--------------------------------')

            # Zeichnen die GrenzPunkte der Strasse
            # for k in range(len(grenz_Punkte[0])):
            #     self.drawingBoard_Strasse.drawPoint(int(grenz_Punkte[0][k][0]),int(grenz_Punkte[0][k][1]),black)
            # for k in range(len(grenz_Punkte1[0])):
            #     self.drawingBoard_Strasse.drawPoint(int(grenz_Punkte1[0][k][0]), int(grenz_Punkte1[0][k][1]), yellow)

            standard_Punkte = [[[[0 for i in range(2)]for j in range(2)] for k in range(max(num_Punkte_1,num_Punkte_2))] for l in range(2)]
            # TODO: BUG! Mehr Standard Punkte in Wendepunkt
            for j in range(num_Punkte_1):
            # Die StandardPunkte an der 1. Strasse
                # Die 1. Punkt an der 1. Strasse
                x = schnittpunkt11[0] - (j+1)*(schnittpunkt11[0] - schnittpunkt21[0])/(num_Punkte_1+1)
                y = schnittpunkt11[1] - (j+1)*(schnittpunkt11[1] - schnittpunkt21[1])/(num_Punkte_1+1)
                # self.drawingBoard_Strasse.drawPoint(int(x), int(y), purpur)
                standard_Punkte[0][j][0] = [x,y]
                Strassen_Standard_Punkte[Schnitt_Punkte[i][0][0]][j].insert(-2,[x,y])
                Strassen_Standard_Punkte[Schnitt_Punkte[i][0][0]][j].insert(-2,Schnitt_Punkte[i][2])
                # Die 2. Punkt an der 1. Strasse
                x = schnittpunkt12[0] - (j+1)*(schnittpunkt12[0] - schnittpunkt22[0])/(num_Punkte_1+1)
                y = schnittpunkt12[1] - (j+1)*(schnittpunkt12[1] - schnittpunkt22[1])/(num_Punkte_1+1)
                # self.drawingBoard_Strasse.drawPoint(int(x), int(y), purpur)
                standard_Punkte[0][j][1] = [x,y]
                Strassen_Standard_Punkte[Schnitt_Punkte[i][0][0]][j].insert(-2,[x,y])

            for j in range(num_Punkte_2):
            # Die StandardPunkte an der 2. Strasse
                # Die 1. Punkt an der 2. Strasse
                x = schnittpunkt11[0] - (j+1)*(schnittpunkt11[0] - schnittpunkt12[0])/(num_Punkte_2+1)
                y = schnittpunkt11[1] - (j+1)*(schnittpunkt11[1] - schnittpunkt12[1])/(num_Punkte_2+1)
                # self.drawingBoard_Strasse.drawPoint(int(x), int(y), purpur)
                Strassen_Standard_Punkte[Schnitt_Punkte[i][1][0]][j].insert(-2,[x,y])
                Strassen_Standard_Punkte[Schnitt_Punkte[i][1][0]][j].insert(-2,Schnitt_Punkte[i][2])
                standard_Punkte[1][j][0] = [x,y]
                # Die 1. Punkt an der 2. Strasse
                x = schnittpunkt21[0] - (j+1)*(schnittpunkt21[0] - schnittpunkt22[0])/(num_Punkte_2+1)
                y = schnittpunkt21[1] - (j+1)*(schnittpunkt21[1] - schnittpunkt22[1])/(num_Punkte_2+1)
                # self.drawingBoard_Strasse.drawPoint(int(x), int(y), purpur)
                Strassen_Standard_Punkte[Schnitt_Punkte[i][1][0]][j].insert(-2,[x,y])
                standard_Punkte[1][j][1] = [x,y]
            print(standard_Punkte)
            print(Strassen_Standard_Punkte)
            print('--------------------------------')
        print("==================================")
        # Zeichnen die StandardPunkte bestimmter Bahn in bestimmten Strasse
        print(Strassen_Standard_Punkte)
        for i in range(len(Strassen_Standard_Punkte)):
            for j in range(len(Strassen_Standard_Punkte[i])):
                for k in range(len(Strassen_Standard_Punkte[i][j])):
                    x = Strassen_Standard_Punkte[i][j][k][0]
                    y = Strassen_Standard_Punkte[i][j][k][1]
                    self.drawingBoard_Strasse.drawPoint(int(x), int(y), purpur)


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

    def drawPoint(self, x, y,colour):
        """
        Zeichnet einen Punkt als kleiner, blauer Punkt (3 Pixel radius) dargestellt auf die Karte
        Args:
            :param1 (int) : X Kordinate auf der Map (Pixel)
            :param2 (int) : Y Kordinate auf der Map (Pixel)
        """
        pygame.draw.circle(self.surface , colour, (x, y), 3)

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

    def drawKurve(self, x, y,colour):
        #Zeichnet einen Kurve
        if len(x)==len(y):
            for i in range(len(x)):
                pygame.draw.circle(self.surface , colour, (int(x[i]), int(y[i])), 0)

    def drawStrasse(self,Polygon_Punkte):
        #self.surface.fill(BackGroundColor)
        pygame.draw.polygon(self.surface, gray, tuple(Polygon_Punkte[i] for i in range(len(Polygon_Punkte))))

    def drawFahrzeug(self,type,x,y,winkel,breite_strasse):
        #Load die Image
        type_Farbe_List = ['blue','black','green','purpur','red','white','yellow','white']
        type_Farbe = type_Farbe_List[type]

        if type>=0 and type<=5:
            type_Fahrzeug = 'car_'
        elif type==6 or type==7:
            type_Fahrzeug = 'bus_'

        self.image_filename = 'qt_creator\icons\icon_'+ type_Fahrzeug + type_Farbe + '.png'
        print(self.image_filename)
        self.image = pygame.image.load(self.image_filename)

        #Die Grosse der Image einstellen
        rect = list(self.image.get_rect())
        breite = breite_strasse/2
        lange = breite*rect[3]/rect[2]
        self.image = pygame.transform.scale(self.image, (int(breite),int(lange)))
        self.image = pygame.transform.rotate(self.image,winkel-180)

        self.rect_def = self.image.get_rect()
        # TODO Es gibt Verschiebung wegen rotation
        self.rect_def.x = x - breite/2
        self.rect_def.y = y - lange/2
        self.surface.blit(self.image,self.rect_def)

def main():
    drawingBoard = PyGameDrawingBoard()     #pygame Draw Board
    app = QtWidgets.QApplication(sys.argv)
    form = QTDesignWidget(drawingBoard)     #QT Windows
    form.show()
    app.exec_()


if __name__ == '__main__': #this will call the main if this file is called as main
    main()
