import numpy as np
#from scipy.misc import comb
import math
#from fahrzeug_model import Fahrzeug_Model
#import fahrzeug_model

class kurve():
    def Bernstein_Poly(self,i, n, t):        #The Bernstein polynomial of n, i as a function of t
        return comb(n, i) * (t ** (n - i)) * (1 - t) ** i
    def Bezier_Kurve(self, points, nTimes=1000):
        """
           Given a set of control points, return the
           bezier curve defined by the control points.

           * points should be a list of lists, or list of tuples
            such as [ [1,1],
                     [2,3],
                     [4,5], ..[Xn, Yn] ]
            * nTimes is the number of time steps, defaults to 1000
        """
        nPoints = len(points)
        xPoints = np.array([p[0] for p in points])
        yPoints = np.array([p[1] for p in points])

        t = np.linspace(0.0, 1.0, nTimes)

        polynomial_array = np.array([self.Bernstein_Poly(i=i, n=(nPoints - 1), t=t) for i in range(nPoints)])

        xvals = np.dot(xPoints, polynomial_array)
        yvals = np.dot(yPoints, polynomial_array)

        return xvals, yvals
    def Length(self,x, y):   #return the length of curve
        """
            length = np.zeros(len(x-1))
            for i in (range(len(x) - 1)):
                length[i] = (((x[i] - x[i + 1]) ** 2 + (y[i] - y[i + 1]) ** 2) ** 0.5 )
                print(length[i])
        """
        return sum(((x[i] - x[i + 1]) ** 2 + (y[i] - y[i + 1]) ** 2) ** 0.5 for i in (range(len(x) - 1)))

class strasse():
    def line_function(self,points):
        x1 = points[0][0]; x2 = points[1][0]; y1 = points[0][1]; y2 = points[1][1]
        if x1 == x2:
            a = 1;b = 0;c = -x1
        elif  y1 == y2:
            a = 0;b = 1;c = -y1
        else:
            a = (y2 - y1) / (x1 - x2)
            b = 1
            c = -y1 + (y2 - y1) / (x2 - x1) *x1
        return [a,b,c]
    def Richtung(self,points):
        p_1_x = points[0][0]; p_2_x = points[1][0]; p_1_y = points[0][1]; p_2_y = points[1][1]
        if p_2_x == p_1_x:
            if p_2_y >= p_1_y:
                strasse_richtung = 0
            else :
                strasse_richtung = 180
        elif p_2_x > p_1_x:
            strasse_richtung = 90 - np.degrees(np.arctan((p_2_y-p_1_y)/(p_2_x-p_1_x)))
        else:
            strasse_richtung = - 90 - np.degrees(np.arctan((p_2_y-p_1_y)/(p_2_x-p_1_x)))
        return strasse_richtung
    def Schnittspunkte(self,linie_1,linie_2):
        a1 = linie_1[0]; b1 = linie_1[1]; c1 = linie_1[2]
        a2 = linie_2[0]; b2 = linie_2[1]; c2 = linie_2[2]
        if (b1!=0 and b2!=0 and (a1 / b1) == (a2 / b2)) or (a1!=0 and a2!=0 and(b1 / a1) == (b2 / a2)):
            x = None
            y = None
        elif(b1 == 0) and (b2 == 0):
            y = (c2 / a2 - c1 / a1) / (b1 / a1 - b2 / a2)
            x = -b1 / a1 * y - c1 / a1
        elif(b1 == 0) and (a2 == 0):
            x = -((b1 * c2 / a1 * b2) - c1 / a1) / (1 - (b1 * a2) / (a1 * b2))
            y = a2 / b2 * x + c2 / b2
        elif(a1 == 0) and (b2 == 0):
            x = ((b2 * c1) / (a2 * b1) - c2 / a2) / (1 - (a1 * b2) / (a2 * b1))
            y = a1 / b1 * x + c1 / b1
        elif(b2 == 0):
            x = ((b2 * c1) / (a2 * b1) - c2 / a2) / (1 - (a1 * b2) / (a2 * b1))
            y = -a1 / b1 * x - c1 / b1
        elif(b1 == 0):
            x = ((b1 * c2 / a1 * b2) - c1 / a1) / (1 - (b1 * a2) / (a1 * b2))
            y = -a2 / b2 * x - c2 / b2
        else:
            x = (c2 / b2 - c1 / b1) / (a1 / b1 - a2 / b2)
            y = -a1 / b1 * x - c1 / b1
        return [x, y]
    def Grenz_Punkte(self,points,breite):
        grenz_punkte=np.zeros(shape=((len(points)-1),4,2))
        for i in range(len(points)-1):
            richtung = self.Richtung(self=self,points=[points[i],points[i+1]])
            grenz_punkte[i][0][0] = points[i][0]-(breite/2)*math.cos(np.radians(richtung))  # Ober Links_x
            grenz_punkte[i][0][1] = points[i][1]+(breite/2)*math.sin(np.radians(richtung))  # Ober Links_y
            grenz_punkte[i][1][0] = points[i][0]+(breite/2)*math.cos(np.radians(richtung))  # Unten Links_x
            grenz_punkte[i][1][1] = points[i][1]-(breite/2)*math.sin(np.radians(richtung))  # Unten Links_y
            grenz_punkte[i][2][0] = points[i+1][0]-(breite/2)*math.cos(np.radians(richtung))# Ober Rechts_x
            grenz_punkte[i][2][1] = points[i+1][1]+(breite/2)*math.sin(np.radians(richtung))# Ober Rechts_y
            grenz_punkte[i][3][0] = points[i+1][0]+(breite/2)*math.cos(np.radians(richtung))# Unten Rechts_x
            grenz_punkte[i][3][1] = points[i+1][1]-(breite/2)*math.sin(np.radians(richtung))# Unten Rechts_y
        return grenz_punkte
    def Grenz_Punkte_Strasse(self,points):
        schnittspunkte=np.zeros(shape=(len(points)-1,2,2))
        for i in range(len(points)-1):
            line_11 = self.line_function(self=self,points=[points[i][0],points[i][2]])
            line_21 = self.line_function(self=self,points=[points[i+1][0],points[i+1][2]])
            schnittspunkte[i][0] = self.Schnittspunkte(self=self,linie_1=line_11,linie_2=line_21)
            line_12 = self.line_function(self=self,points=[points[i][1],points[i][3]])
            line_22 = self.line_function(self=self,points=[points[i+1][1],points[i+1][3]])
            schnittspunkte[i][1] = self.Schnittspunkte(self=self,linie_1=line_12,linie_2=line_22)

        grenz_punkte = np.zeros(shape=(2*len(points)+2,2))
        k = 0
        grenz_punkte[k] = points[0][0]
        for i in range(len(schnittspunkte)):
            k=k+1
            grenz_punkte[k] = schnittspunkte[i][0]
        grenz_punkte[k+1] = points[-1][2]
        grenz_punkte[k+2] = points[-1][3]
        k=k+2
        for i in range(len(schnittspunkte)):
            k=k+1
            grenz_punkte[k] = schnittspunkte[-1-i][1]
        grenz_punkte[k+1] = points[0][1]
        return  grenz_punkte
    def Polygon_Zeichnen(self,points,bereite):
        grenz_punkte = self.Grenz_Punkte(self=self,points=points,breite=bereite)
        return self.Grenz_Punkte_Strasse(self=self,points=grenz_punkte)
    def Polygon_Punkte(self, points, bereite):
        grenz_punkte = self.Grenz_Punkte(self=self, points=points, breite=bereite)
        return self.Grenz_Punkte_Strasse(self=self, points=grenz_punkte)


def main_strasse():
    from matplotlib import pyplot as plt
    from matplotlib.lines import Line2D
    Strasse_1 = strasse
    nPoints = 10
    Strasse_Punkte = [[100,105],[210,110],[205,40],[60,120],[100,105]]#[[0,0],[2,2],[5,0],[5,-1],[2,-3]]
    #Strasse_Punkte = np.random.rand(nPoints,2)*20
    Polygon_Punkte = tuple(Strasse_1.Polygon_Zeichnen(Strasse_1,points=Strasse_Punkte,bereite=2))
    print(Polygon_Punkte)

    """figure, ax = plt.subplots()
     #设置x，y值域
    ax.set_xlim(left=-20, right=20)
    ax.set_ylim(bottom=-20, top=20)
     #两条line的数据
    for i in range(len(Polygon_Punkte)-1):
        (line1_xs, line1_ys) = zip(*[Polygon_Punkte[i],Polygon_Punkte[i+1]])
     #创建两条线，并添加
        ax.add_line(Line2D(line1_xs, line1_ys, linewidth=1, color='blue'))
    plt.plot()
    #plt.show()


    xpoints = [p[0] for p in Strasse_Punkte]#points[i]]
    ypoints = [p[1] for p in Strasse_Punkte]#points[i]]
    plt.plot(xpoints,ypoints,'bo')
    xpoints = [p[0] for p in Polygon_Punkte]#points[i]]
    ypoints = [p[1] for p in Polygon_Punkte]#points[i]]
    plt.plot(xpoints,ypoints,'ro')
    plt.show()
#"""

def main_kurve():
    from matplotlib import pyplot as plt

    Kurve = kurve
    nPoints = 3
    ##points = [[0, 0],[0,4],[1,5],[5 ,5]]#np.random.rand(nPoints,2)*200
    points = np.random.rand(nPoints,2)*200
    xpoints = [p[0] for p in points]
    ypoints = [p[1] for p in points]

    xvals, yvals = Kurve.Bezier_Kurve(self = Kurve,points=points)
    plt.plot(xvals, yvals)
    plt.plot(xpoints, ypoints, "ro")
    for nr in range(len(points)):
        plt.text(points[nr][0], points[nr][1], nr)

    plt.show()
    print(Kurve.Length(self = Kurve,x=xvals,y=yvals))

if __name__ == "__main__":
    #main_kurve();
    main_strasse()
