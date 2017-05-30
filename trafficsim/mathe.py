#Diese Klassen sollen von euch nach euren Vorschlägen verfollständig werden.
#Wenn feststeht wie der Polygonenzug aussieht kann ich das auch noch schnell fertig machen, aber erstmal gibt mir feedback !
import numpy as np
#from scipy.misc import comb # bitte nicht benutzen, kann nicht überall einfach installiert werden. Bitte nur PIP verwenden
import math
import pygame
from gui import *

class StreetSystem:
    """
    Anzahl aller Straßenetze. Verwaltet die Netze
    """
    def __init__(self):
        self.nets=[] # Alle möglichen netze

    # Es ist notwendig eine Line für jeden ereichbaren Punkt und für jeden daraufolgenden Punkt anzulegen

    def addPoint(self, new_point, connected_point=None):
        if (connected_point==None): # wir müssen ein neues Netz eröfnnen
            newStreetNet = StreetNet(new_point)
            self.nets.append(newStreetNet)
            #TODO : FERTIG CODEN!

class StreetNet:
    """
    Anzahl von Punkten die miteinander verbunden sind und ein mögliches Straßennetz beschreiben. Dient der abstrakten Darstellung
    """

    def __init__(self):
        self.street_end_points = []  # Alle möglichen netze

    def add_point(self, new_point, connected_point=None):
        if (connected_point == None):  # wir müssen ein neues Netz eröfnnen
            self.nets.append()
            # TODO : FERTIG CODEN!



def calculate_pos(old_pos, dt, v):
    """
    Errechnet eine neue Position anhand von der alten Position und diversen Parameteren. Achtung, statische Funktion
    :param old_pos: Alte Position
    :param dt: Zeiteinheit
    :param v: Geschwindigkeit
    :return:
    """
    return old_pos+((v*dt),(v*dt)) # FIXME das braucht noch ne richtungsvektor !!!

#Die funktionierien und sind frei nutzbar!!!
class Line(list):
    """
    Linie zwischen zwei Punkten. Dient der grafischen Darstellung
    """
    def __init__(self, start_point=None):
        self=[]
        if not start_point==None:
            self.append(start_point)

    def append(self, point):
        if not isinstance(point, Point):
            raise TypeError("Line can only hold Object of type Poin")
        super(Line, self).append(point)

    def getFirstPoint(self):
        return self[0]

    def getLastPoint(self):
        return self[-1]

class Point(tuple):
    """
    Ein einzelnder Punkt mit x,y kordinate
    """
    def __new__(self, x, y):
        return tuple.__new__(Point, (x, y))

    def __init__(self, x, y):
        self=(x,y)

    def _get_x(self):
        return self[0]

    def _set_x(self,new_x):
        self=(new_x,self[1])

    x = property(_get_x,_set_x)

    def _get_y(self):
        return self[1]

    def _set_y(self,new_y):
        self = (self[0], new_y)

    y = property(_get_y, _set_y)


# Bitte auslageren, die Mathe Klasse wird von allen genutzt. Eure Main Funktion macht mir Zeug kapput

# class math_Kurve():
#     def Bernstein_Poly(self,i, n, t):        #The Bernstein polynomial of n, i as a function of t
#         return comb(n, i) * (t ** (n - i)) * (1 - t) ** i
#
#     def Bezier_Kurve(self, points: object, nTimes: object = 1000) -> object:
#         """
#            Given a set of control points, return the
#            bezier curve defined by the control points.
#
#            * points should be a list of lists, or list of tuples
#             such as [ [1,1],
#                      [2,3],
#                      [4,5], ..[Xn, Yn] ]
#             * nTimes is the number of time steps, defaults to 1000
#         """
#         nPoints = len(points)
#         xPoints = np.array([p[0] for p in points])
#         yPoints = np.array([p[1] for p in points])
#
#         t = np.linspace(0.0, 1.0, nTimes)
#
#         polynomial_array = np.array([self.Bernstein_Poly(i=i, n=(nPoints - 1), t=t) for i in range(nPoints)])
#
#         xvals = np.dot(xPoints, polynomial_array)
#         yvals = np.dot(yPoints, polynomial_array)
#
#         return xvals, yvals
#     def Length(self,x, y):   #return the length of curve
#         """
#             length = np.zeros(len(x-1))
#             for i in (range(len(x) - 1)):
#                 length[i] = (((x[i] - x[i + 1]) ** 2 + (y[i] - y[i + 1]) ** 2) ** 0.5 )
#                 print(length[i])
#         """
#         return sum(((x[i] - x[i + 1]) ** 2 + (y[i] - y[i + 1]) ** 2) ** 0.5 for i in (range(len(x) - 1)))
#
#
# class math_Strasse():
#     def __init__(self):
#         a=1
#     def line_function(self,points):
#         #rechnen die Funktion Parameter einer Linie , die zwischen 2 Punkte
#         x1 = points[0][0]; x2 = points[1][0]; y1 = points[0][1]; y2 = points[1][1]
#         if x1 == x2:
#             a = 1;b = 0;c = -x1
#         elif  y1 == y2:
#             a = 0;b = 1;c = -y1
#         else:
#             a = (y2 - y1) / (x1 - x2)
#             b = 1
#             c = -y1 + (y2 - y1) / (x2 - x1) *x1
#         return [a,b,c]
#
#     def Richtung(self,points):
#         #rechnen die Richtung einer Linie
#         p_1_x = points[0][0]; p_2_x = points[1][0]; p_1_y = points[0][1]; p_2_y = points[1][1]
#         if p_2_x == p_1_x:
#             if p_2_y >= p_1_y:
#                 strasse_richtung = 0
#             else :
#                 strasse_richtung = 180
#         elif p_2_x > p_1_x:
#             strasse_richtung = 90 - np.degrees(np.arctan((p_2_y-p_1_y)/(p_2_x-p_1_x)))
#         else:
#             strasse_richtung = - 90 - np.degrees(np.arctan((p_2_y-p_1_y)/(p_2_x-p_1_x)))
#         return strasse_richtung
#
#     def Schnittspunkte(self,linie_1,linie_2):
#         #rechnen die Schnittpunkt zwischen 2 Linien
#         a1 = linie_1[0]; b1 = linie_1[1]; c1 = linie_1[2]
#         a2 = linie_2[0]; b2 = linie_2[1]; c2 = linie_2[2]
#         if (b1!=0 and b2!=0 and (a1 / b1) == (a2 / b2)) or (a1!=0 and a2!=0 and(b1 / a1) == (b2 / a2)):
#             x = None
#             y = None
#         elif(b1 == 0) and (b2 == 0):
#             y = (c2 / a2 - c1 / a1) / (b1 / a1 - b2 / a2)
#             x = -b1 / a1 * y - c1 / a1
#         elif(b1 == 0) and (a2 == 0):
#             x = -((b1 * c2 / a1 * b2) - c1 / a1) / (1 - (b1 * a2) / (a1 * b2))
#             y = a2 / b2 * x + c2 / b2
#         elif(a1 == 0) and (b2 == 0):
#             x = ((b2 * c1) / (a2 * b1) - c2 / a2) / (1 - (a1 * b2) / (a2 * b1))
#             y = a1 / b1 * x + c1 / b1
#         elif(b2 == 0):
#             x = ((b2 * c1) / (a2 * b1) - c2 / a2) / (1 - (a1 * b2) / (a2 * b1))
#             y = -a1 / b1 * x - c1 / b1
#         elif(b1 == 0):
#             x = ((b1 * c2 / a1 * b2) - c1 / a1) / (1 - (b1 * a2) / (a1 * b2))
#             y = -a2 / b2 * x - c2 / b2
#         else:
#             x = (c2 / b2 - c1 / b1) / (a1 / b1 - a2 / b2)
#             y = -a1 / b1 * x - c1 / b1
#         return [x, y]
#
#     def Grenz_Punkte(self,points,breite):
#         #rechnen die Rand Punkte jeder gerade Strasse
#         grenz_punkte=np.zeros(shape=((len(points)-1),4,2))
#         for i in range(len(points)-1):
#             richtung = self.Richtung(self=self,points=[points[i],points[i+1]])
#             grenz_punkte[i][0][0] = points[i][0]-(breite/2)*math.cos(np.radians(richtung))  # Ober Links_x
#             grenz_punkte[i][0][1] = points[i][1]+(breite/2)*math.sin(np.radians(richtung))  # Ober Links_y
#             grenz_punkte[i][1][0] = points[i][0]+(breite/2)*math.cos(np.radians(richtung))  # Unten Links_x
#             grenz_punkte[i][1][1] = points[i][1]-(breite/2)*math.sin(np.radians(richtung))  # Unten Links_y
#             grenz_punkte[i][2][0] = points[i+1][0]-(breite/2)*math.cos(np.radians(richtung))# Ober Rechts_x
#             grenz_punkte[i][2][1] = points[i+1][1]+(breite/2)*math.sin(np.radians(richtung))# Ober Rechts_y
#             grenz_punkte[i][3][0] = points[i+1][0]+(breite/2)*math.cos(np.radians(richtung))# Unten Rechts_x
#             grenz_punkte[i][3][1] = points[i+1][1]-(breite/2)*math.sin(np.radians(richtung))# Unten Rechts_y
#         return grenz_punkte
#
#     def Grenz_Punkte_Strasse(self,points):
#         #verbinden jeder Strasse
#         schnittspunkte=np.zeros(shape=(len(points)-1,2,2))
#         for i in range(len(points)-1):
#             line_11 = self.line_function(self=self,points=[points[i][0],points[i][2]])
#             line_21 = self.line_function(self=self,points=[points[i+1][0],points[i+1][2]])
#             schnittspunkte[i][0] = self.Schnittspunkte(self=self,linie_1=line_11,linie_2=line_21)
#             line_12 = self.line_function(self=self,points=[points[i][1],points[i][3]])
#             line_22 = self.line_function(self=self,points=[points[i+1][1],points[i+1][3]])
#             schnittspunkte[i][1] = self.Schnittspunkte(self=self,linie_1=line_12,linie_2=line_22)
#
#         grenz_punkte = np.zeros(shape=(2*len(points)+2,2))
#         k = 0
#         grenz_punkte[k] = points[0][0]
#         for i in range(len(schnittspunkte)):
#             k=k+1
#             grenz_punkte[k] = schnittspunkte[i][0]
#         grenz_punkte[k+1] = points[-1][2]
#         grenz_punkte[k+2] = points[-1][3]
#         k=k+2
#         for i in range(len(schnittspunkte)):
#             k=k+1
#             grenz_punkte[k] = schnittspunkte[-1-i][1]
#         grenz_punkte[k+1] = points[0][1]
#         return  grenz_punkte
#
#     def Polygon_Punkte(self,points,bereite):
#         #als die Eingabe der Polygon Zeichnung
#         grenz_punkte = self.Grenz_Punkte(self=self,points=points,breite=bereite)
#         return self.Grenz_Punkte_Strasse(self=self,points=grenz_punkte)
#
#
# def main_strasse():
#     from matplotlib import pyplot as plt
#     from matplotlib.lines import Line2D
#     Strasse_1 = math_Strasse
#     nPoints = 10
#     Strasse_Punkte = [[0,4.5],[11,5]]#,[10.5,-2],[1,-6],[-5,-5],[-10,3],[-4,6],[0,4.5]]#[[0,0],[2,2],[5,0],[5,-1],[2,-3]]
#     #Strasse_Punkte = np.random.rand(nPoints,2)*20
#     Polygon_Punkte = Strasse_1.Polygon_Punkte(Strasse_1,points=Strasse_Punkte,bereite=2)
#     print(Polygon_Punkte)
#
#     figure, ax = plt.subplots()
#     # 设置x，y值域
#     ax.set_xlim(left=-20, right=20)
#     ax.set_ylim(bottom=-20, top=20)
#     # 两条line的数据
#     for i in range(len(Polygon_Punkte)-1):
#         (line1_xs, line1_ys) = zip(*[Polygon_Punkte[i],Polygon_Punkte[i+1]])
#     # 创建两条线，并添加
#         ax.add_line(Line2D(line1_xs, line1_ys, linewidth=1, color='blue'))
#     plt.plot()
#     #plt.show()
# #"""
#     xpoints = [p[0] for p in Strasse_Punkte]#points[i]]
#     ypoints = [p[1] for p in Strasse_Punkte]#points[i]]
#     plt.plot(xpoints,ypoints,'bo')
#     xpoints = [p[0] for p in Polygon_Punkte]#points[i]]
#     ypoints = [p[1] for p in Polygon_Punkte]#points[i]]
#     plt.plot(xpoints,ypoints,'ro')
#     plt.show()
# #"""
#
# def main_kurve(points):
#     from matplotlib import pyplot as plt
#
#     Kurve = math_Kurve()
#     #nPoints = 6
#     #points = np.random.rand(nPoints,2)*200
#     #points = [[0,0],[0,4],[1,5],[2,3],[5 ,5]]#np.random.rand(nPoints,2)*200
#
#     #points to define the kurve
#     xpoints = [p[0] for p in points]
#     ypoints = [p[1] for p in points]
#     Route_Points=[xpoints,ypoints]
#     print(Route_Points)
#
#     #points of the kurve
#     xvals, yvals = Kurve.Bezier_Kurve(points=points)
#
#     Kurve_Points=[xvals,yvals]
#     print(Kurve_Points)
#
#     plt.plot(xvals, yvals)
#     plt.plot(xpoints, ypoints, "ro")
#     plt.show()
#
#     for nr in range(len(points)):
#         plt.text(points[nr][0], points[nr][1], nr)
#
#     print(Kurve.Length(x=xvals,y=yvals))
#
#
#
# def bahn(points,width):
#     from matplotlib import pyplot as plt
#
#     Line1=math_Kurve()
#     Line2=math_Kurve()
#     Kurve=math_Kurve()
#
#     xpoints = [p[0] for p in points]
#     ypoints = [p[1] for p in points]
#
#     x1=xpoints[0]
#     x3=xpoints[1]
#     x5=xpoints[2]
#     y1=ypoints[0]
#     y3=ypoints[1]
#     y5=ypoints[2]
#
#     s13=((x3 - x1) ** 2 + (y3 - y1) ** 2) ** 0.5
#     s35 = ((x3 - x5) ** 2 + (y3 - y5) ** 2) ** 0.5
#
#     x2=x3+((width/2)*(x1-x3))/s13
#     y2=y3+((width/2)*(y1-y3))/s13
#     x4=x3+((width/2)*(x5-x3))/s35
#     y4=y3+((width/2)*(y5-y3))/s35
#
#     lpoints1=[[x1,y1],[x2,y2]]
#     lpoints2 = [[x4, y4], [x5, y5]]
#     kpoints=[[x2,y2],[x3,y3],[x4,y4]]
#
#     xpoints=[x1,x2,x3,x4,x5]
#     ypoints=[y1,y2,y3,y4,y5]
#
#     xline1, yline1 = Kurve.Bezier_Kurve(points=lpoints1)
#     xline2, yline2 = Kurve.Bezier_Kurve(points=lpoints2)
#     xkurve, ykurve = Kurve.Bezier_Kurve(points=kpoints)
#     print(xkurve,ykurve)
#
#     #xvals=list(xline1).extend(list(xkurve))
#     #yvals = list(yline1).extend((ykurve))
#     #Bahn_Points = [xvals, yvals]
#     #print(Bahn_Points)
#
#     Route_Points = [xpoints, ypoints]
#
#     plt.plot(xkurve, ykurve)
#     plt.plot(xline1, yline1)
#     plt.plot(xline2, yline2)
#     #plt.plot(Bahn_Points)
#     plt.plot(xpoints, ypoints, "ro")
#     plt.show()
#
#
#
# if __name__ == "__main__":
#     bahn(points=[[1,4],[2,1],[5,1]],width=2);
#     #main_strasse()
