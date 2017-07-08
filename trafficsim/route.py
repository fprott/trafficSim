#import sys
import math
#sys.path.append("..")

#for "test" running
from mathe import *
#for "route" running
#from mathe import *

from parameter import *
# Wangs Klasse wurde hierher verschoben !
# getested, geht halbwegs XD

#UPDATE 25/06/2017
#get_next_pos input a negative Length
#get_next_dis: find out the distance to the next point
#get_new_pos_without_position_change: only find out the next pos without any pointer change


class Route():
    def __init__(self,points,width):
        self.points = points  # The points to define the street
        self.width = width
        self.routepoints = self.get_route(self.points, self.width)
        self.point_iterator = 0
        self.routelength= self.route_length()

    def gui_to_route(self):
        return 0

    def get_one_turning_point(self,startpoint,endpoint,width):

        xs=startpoint[0]
        ys=startpoint[1]
        xe=endpoint[0]
        ye=endpoint[1]
        l=math.hypot((xs-xe),(ys-ye))

        x=xe + ((width / 2) * (xs - xe)) / l
        y=ye + ((width / 2) * (ys - ye)) / l
        #print([x,y])
        return [x,y]

    def get_two_turning_points(self,startpoint,endpoint,width):

        xs = startpoint[0]
        ys = startpoint[1]
        xe = endpoint[0]
        ye = endpoint[1]
        l = math.hypot((xs - xe), (ys - ye))

        x2 = xe + ((width / 2) * (xs - xe)) / l
        y2 = ye + ((width / 2) * (ys - ye)) / l
        x1 = xs + ((width / 2) * (xe - xs)) / l
        y1 = ys + ((width / 2) * (ye - ys)) / l
        p=[[x1,y1],[x2,y2]]
        #print(p[0])
        return (p)

    def get_key_points(self,points,width):

        n=len(points)

        new_p = [self.get_one_turning_point(points[0],points[1],width)]
        for i in range(n-1):
            if i+2<n:
                new_p = new_p+self.get_two_turning_points(points[i+1],points[i+2],width)
            else:
                pass

        #new_p.pop()
        #delete the last item

        #print(new_p)
        return new_p

    def get_route(self,points,width):
        #from matplotlib import pyplot as plt

        #points = self.points
        #width = self.width
        xpoints = [p[0] for p in points]
        ypoints = [p[1] for p in points]
        n = len(points)
        new_p = self.get_key_points(points,width)
        m = len(new_p)

        s = math_Kurve()
        x,y = s.Bezier_Kurve(points=[new_p[0],points[0]])
        x = list(x)
        y = list(y)
        y.pop()
        x.pop()

        for i in range(1,n-1):
            kpoints=[new_p[(2*i - 1)], points[i], new_p[(2*i-2)]]
            x_new, y_new = s.Bezier_Kurve(points=kpoints) # Ablenkung
            x_new = list(x_new)
            y_new = list(y_new)
            x_new.pop()
            y_new.pop()
            x = list(x)+x_new
            y = list(y)+y_new
            lpoints=[new_p[2*i],new_p[(2*i-1)]]
            x_new, y_new = s.Bezier_Kurve(points=lpoints) #Gerade Linien
            x_new = list(x_new)
            y_new = list(y_new)
            x_new.pop()
            y_new.pop()
            x = list(x) + x_new
            y = list(y) + y_new

        x_final,y_final=s.Bezier_Kurve(points=[points[n-1],new_p[2*(n-2)]])
        x_final = list(x_final)
        y_final = list(y_final)
        #x_final.pop()
        #y_final.pop()
        x = x + x_final
        y = y + y_final

        k = len(x)
        r = []

        for i in range(0, k):
            r = r + [[x[i],y[i]]]

        #print(new_p)
        #print(x)
        #print(len(x))
        #print (r)
        #print (len(r))
        #print(r[0])
        #plt.plot(x, y,"go")
        #plt.show()
        return r

    def route_length(self):
        x = [p[0] for p in self.routepoints]
        y = [p[1] for p in self.routepoints]
        d = sum(((x[i] - x[i + 1]) ** 2 + (y[i] - y[i + 1]) ** 2) ** 0.5 for i in (range(len(x)-1)))
        #print(d)

        return d


    def basic_route(points, width): #points can only be given by 3 points like [[1,4],[2,1],[5,1]]
#        from matplotlib import pyplot as plt

        Line1 = math_Kurve()
        Line2 = math_Kurve()
        Kurve = math_Kurve()

        xpoints = [p[0] for p in points]
        ypoints = [p[1] for p in points]

        x1 = xpoints[0]
        x3 = xpoints[1]
        x5 = xpoints[2]
        y1 = ypoints[0]
        y3 = ypoints[1]
        y5 = ypoints[2]

        s13 = math.hypot((x3-x1),(y3-y1)) #((x3 - x1) ** 2 + (y3 - y1) ** 2) ** 0.5
        s35 = math.hypot((x3-x5),(y3-y5)) #((x3 - x5) ** 2 + (y3 - y5) ** 2) ** 0.5

        x2 = x3 + ((width / 2) * (x1 - x3)) / s13
        y2 = y3 + ((width / 2) * (y1 - y3)) / s13
        x4 = x3 + ((width / 2) * (x5 - x3)) / s35
        y4 = y3 + ((width / 2) * (y5 - y3)) / s35

        lpoints1 = [[x1, y1], [x2, y2]]
        lpoints2 = [[x4, y4], [x5, y5]]
        kpoints = [[x2, y2], [x3, y3], [x4, y4]]

        xpoints = [x1, x2, x3, x4, x5]
        ypoints = [y1, y2, y3, y4, y5]

        xline1, yline1 = Kurve.Bezier_Kurve(points=lpoints1)
        xline2, yline2 = Kurve.Bezier_Kurve(points=lpoints2)
        xkurve, ykurve = Kurve.Bezier_Kurve(points=kpoints)
        #print(xkurve, ykurve)

        xvals = list(xline1) + list(xkurve) + list(xline2)
        yvals = list(yline1) + list(ykurve) + list(yline2)
        #connection of all 3

        Route_Points = [xpoints, ypoints] #all key points to define the route

        #plt.plot(xkurve, ykurve)
        #plt.plot(xline1, yline1)
        #plt.plot(xline2, yline2)

        #plt.plot(xvals,yvals)
        #plt.plot(xpoints, ypoints, "ro")
        #plt.show()

        return xvals,yvals


    def get_current_pos(self):
        return Point(self.routepoints[self.point_iterator][0],self.routepoints[self.point_iterator][1])

    def get_step(self,l):
        #Done
        n = len(self.routepoints)
        k = 0 #k=要走的步数
        x = [p[0] for p in self.routepoints]
        y = [p[1] for p in self.routepoints]
        i = self.point_iterator
        s = 0 #走的路程
        if l == 0:
            k = 0
        else:
            while i < n - 1:
                s = s + ((x[i] - x[i + 1]) ** 2 + (y[i] - y[i + 1]) ** 2) ** 0.5
                if s > l:
                    # print(s)
                    break
                i += 1
                k += 1

        #print(k)
        #print(self.point_iterator)
        return k

    def get_new_pos(self, l):
        """Verändert die Position um den Abstand l. l ist t*v"""
        # Done
        d = self.traveled_distance_on_route()

        if l >= 0:
            if l > (self.routelength - d):
                # print('Error: "l" is out of range')
                # ********Warning: folowing parts can be deleted*************
                # The car always stay at the endposition
                self.point_iterator = len(self.routepoints) - 1
                t = Point(self.routepoints[len(self.routepoints) - 1][0],
                          self.routepoints[len(self.routepoints) - 1][1])
            else:
                k = self.get_step(l)
                self.point_iterator += int(k)
                # print(self.routepoints[self.point_iterator])
                # print(self.point_iterator)
                # The return value should be a tuple!!!!!!!!!
                t = Point(self.routepoints[self.point_iterator][0], self.routepoints[self.point_iterator][1])
        else:
            if abs(l) > d:
                t = Point(self.routepoints[0][0],self.routepoints[0][1])
            else:
                k = self.get_step(abs(l))
                self.point_iterator -= int(k)
                t = Point(self.routepoints[self.point_iterator][0], self.routepoints[self.point_iterator][1])


     #   print(t)
        return t

    def get_next_dis(self):

        i = self.point_iterator
        x = [p[0] for p in self.routepoints]
        y = [p[1] for p in self.routepoints]

        s = ((x[i] - x[i + 1]) ** 2 + (y[i] - y[i + 1]) ** 2) ** 0.5

        return s

    def get_new_pos_without_position_change(self,l):

        d = self.traveled_distance_on_route()
        i = self.point_iterator

        if l >= 0:
            if l > (self.routelength - d):
                # print('Error: "l" is out of range')
                # ********Warning: folowing parts can be deleted*************
                # The car always stay at the endposition
                i = len(self.routepoints) - 1
                t = Point(self.routepoints[len(self.routepoints) - 1][0],
                          self.routepoints[len(self.routepoints) - 1][1])
            else:
                k = self.get_step(l)
                i += int(k)
                # print(self.routepoints[self.point_iterator])
                # print(self.point_iterator)
                # The return value should be a tuple!!!!!!!!!
                t = Point(self.routepoints[i][0], self.routepoints[i][1])
        else:
            if abs(l) > d:
                t = Point(self.routepoints[0][0], self.routepoints[0][1])
            else:
                k = self.get_step(abs(l))
                i -= int(k)
                t = Point(self.routepoints[i][0], self.routepoints[i][1])

        #print(i)
        #print(self.point_iterator)
        return t

    def traveled_distance_on_route(self):
        """"Zurückgelegter Weg auf der Route d.h. wie weit wir schon gefahren sind"""
        #关键在于步长不相等
        x = [p[0] for p in self.routepoints]
        y = [p[1] for p in self.routepoints]
        d = sum(((x[i] - x[i + 1]) ** 2 + (y[i] - y[i + 1]) ** 2) ** 0.5 for i in (range(self.point_iterator)))
        #print(d)
        return d

    def percent_of_route_still_to_travel(self):
        """Wie viel Prozent der Route noch zurückgelegt werden müssen wobei 0 Prozent heißt das wir angekommen sind und 100 Prozent das wir am Start sind"""
        # Done
        # 步长不一定

        #Bugfix weil er mir keine 0 zurückliefert XD
        if self.point_iterator >= len(self.routepoints)-1:
            return 0.0

        d = self.traveled_distance_on_route()
        dd = self.routelength
        #print(100-(100*d/dd))
        return 100-(100*d/dd)

    def get_new_pos_from_start(self,l):

        d = self.traveled_distance_on_route()
        i = 0

        if l > self.routelength:
            # print('Error: "l" is out of range')
            # ********Warning: folowing parts can be deleted*************
            # The car always stay at the endposition
            #self.i = len(self.routepoints) - 1
            t = Point(self.routepoints[len(self.routepoints) - 1][0],self.routepoints[len(self.routepoints) - 1][1])
        else:
            k = self.get_step(l)
            i += int(k)
            # print(self.routepoints[self.point_iterator])
            # print(self.point_iterator)
            # The return value should be a tuple!!!!!!!!!
            t = Point(self.routepoints[i][0], self.routepoints[i][1])

            return t


    def get_percentage_from_start(self,l):

            if l>=self.routelength:
                return 0.0
            else:
                return 100-(100*l/self.routelength)





    def get_angle_of_pos(self):
        """Gibt den Winkel zurück so als ob das Auto von Start zu Ende geht"""
        x = [p[0] for p in self.routepoints]
        y = [p[1] for p in self.routepoints]
        vx = x[self.point_iterator+1] - x[self.point_iterator]
        vy = y[self.point_iterator+1] - y[self.point_iterator]
        return (vx,vy)

    def get_angle_from_start(self,l):

        i = 0
        if l > self.routelength:
            i = len(self.routepoints) - 2
        else:
            k = self.get_step(l)
            i += int(k)

        x = [p[0] for p in self.routepoints]
        y = [p[1] for p in self.routepoints]
        vx = x[i + 1] - x[i]
        vy = y[i + 1] - y[i]

        return (vx,vy)



    def castPointsToWangNotation(points):
        """
        Nimmt eine Liste von Punkten und macht die in eine Liste von Listen d.h. die Notation die Wang verwendet
        """
        wang=[]
        for p in points:
            wang.append([p.x,p.y])
        return wang



#****************Beispiel*************************

#if __name__ == "__main__":

# Route1=Route([(500,1),(1000,1)],width=1)
# print(Route1.get_new_pos(100))
# print(Route1.traveled_distance_on_route())
# print(Route1.percent_of_route_still_to_travel())




# Meine alte Klasse

# import numpy
# import mathe
#
# class Strecke:
#     """
#     Eine Strecke ist eine Ansammlung von minimal notwendigen Punkte zum beschreiben einer Route. Der erste Punkt ist der Startpunkt, der letzte Punkt ist der Endpunkt alle anderen Punkte sind Verbindungspunkte die NICHT exakt auf der Route liegen müssen sonderen ggf. daneben
#     """
#     def __init__(self):
#         self.points=[]
#
#     def __init__(self, points):
#         self.points=points
#
#     def getStartPoint(self):
#         return self.points[0]
#
#     def getEndPoint(self):
#         return self.points[-1]
#
#     def getSmallestX(self):
#         x_min=self.points[0].x
#         for p in self.points:
#             if p.x<x_min:
#                 x_min=p.x
#         return x_min
#
#     def getBiggestX(self):
#         x_max=self.points[0].x
#         for p in self.points:
#             if p.x>x_max:
#                 x_max=p.x
#         return x_max
#
# class Route:
#     def __init__(self, strecke, dStep, start_pos=None):
#         self.strecke = strecke # Die Route bassiert auf einer Strecke. Wenn man die Route ändert so ändert man auch die Strecke und umgekehert !
#         self.points = self._get_path_as_many_points(dStep)
#         if start_pos==None:
#             self.positon = strecke.getStartPoint()
#         else:
#             self.positon= start_pos
#         self._dStep=dStep
#         self.point_iterator = 0 # Position an der wir uns im point "array" befinden
#
#     def _get_path_as_many_points(self, dStep): #WARNING EXPENSIVE !
#         """
#         Gibt die Route als Punktliste zurück. dStep gibt die Punktgenauigkeit an.
#         :param dStep: Punkt genauigkeit
#         :return:
#         """
#         roh_daten = self.strecke.points
#         x_roh=[]
#         y_roh=[]
#         for p in roh_daten:
#             x_roh.append(p.x)
#             y_roh.append(p.y)
#         x_range = numpy.arange(self.strecke.getSmallestX(), self.strecke.getBiggestX(), dStep);
#         y_points = numpy.interp(x_range, x_roh, y_roh)
#         points=[]
#         for i in range(0,len(y_points)):
#         #    points.append(mathe.Point(y_points[i],x_range[i]))
#             points.append(mathe.Point(x_range[i], y_points[i]))
#
#         return points
#
#     def get_new_pos(self, l): # ich gehe davon aus das sich die Einheit nicht ändert !
#         """Verändert die Position um den Abstand l. l ist t*v"""
#         k=l/self._dStep
#         self.point_iterator+=int(k)
#         if self.point_iterator >= len(self.points):
#             self.point_iterator= len(self.points)-1
#         return self.points[self.point_iterator]
#
#     def get_current_pos(self):
#         return self.points[self.point_iterator]
#
#     def traveled_distance_on_route(self):
#         """"Zurückgelegter Weg auf der Route d.h. wie weit wir schon gefahren sind"""
#         k = 1 / self._dStep
#         return self.point_iterator*k
#
#     def percent_of_route_still_to_travel(self):
#         """Wie viel Prozent der Route noch zurückgelegt werden müssen wobei 0 Prozent heißt das wir angekommen sind und 100 Prozent das wir am Start sind"""
#         return 100-(100*self.point_iterator/(len(self.points)-1))
#
#     def get_angle_of_pos(self, pos):
#         """Gibt den Winkel zurück so als ob das Auto von Start zu Ende geht"""
#     #    return angle
#
# # myStrecke = Strecke([mathe.Point(0.0,0.0),mathe.Point(1.0,2.0),mathe.Point(2.0,4.0),mathe.Point(3.0,8.0)])
# # myRoute = Route(myStrecke,0.1)
# # print(myRoute.get_current_pos())
# # print(myRoute.percent_of_route_still_to_travel())
# # print(myRoute.get_new_pos(1))
# # print(myRoute.percent_of_route_still_to_travel())
# # print(myRoute.get_new_pos(1))
# # print(myRoute.percent_of_route_still_to_travel())
# # print(myRoute.get_new_pos(1))
# # print(myRoute.percent_of_route_still_to_travel())
