import numpy
import mathe

class Strecke:
    """
    Eine Strecke ist eine Ansammlung von minimal notwendigen Punkte zum beschreiben einer Route. Der erste Punkt ist der Startpunkt, der letzte Punkt ist der Endpunkt alle anderen Punkte sind Verbindungspunkte die NICHT exakt auf der Route liegen müssen sonderen ggf. daneben
    """
    def __init__(self):
        self.points=[]

    def __init__(self, points):
        self.points=points

    def getStartPoint(self):
        return self.points[0]

    def getEndPoint(self):
        return self.points[-1]

    def getSmallestX(self):
        x_min=self.points[0].x
        for p in self.points:
            if p.x<x_min:
                x_min=p.x
        return x_min

    def getBiggestX(self):
        x_max=self.points[0].x
        for p in self.points:
            if p.x>x_max:
                x_max=p.x
        return x_max

class Route:
    def __init__(self, strecke, dStep, start_pos=None):
        self.strecke = strecke # Die Route bassiert auf einer Strecke. Wenn man die Route ändert so ändert man auch die Strecke und umgekehert !
        self.points = self._get_path_as_many_points(dStep)
        if start_pos==None:
            self.positon = strecke.getStartPoint()
        else:
            self.positon= start_pos
        self._dStep=dStep
        self.point_iterator = 0 # Position an der wir uns im point "array" befinden

    def _get_path_as_many_points(self, dStep): #WARNING EXPENSIVE !
        """
        Gibt die Route als Punktliste zurück. dStep gibt die Punktgenauigkeit an.
        :param dStep: Punkt genauigkeit
        :return:
        """
        roh_daten = self.strecke.points
        x_roh=[]
        y_roh=[]
        for p in roh_daten:
            x_roh.append(p.x)
            y_roh.append(p.y)
        x_range = numpy.arange(self.strecke.getSmallestX(), self.strecke.getBiggestX(), dStep);

        y_points = numpy.interp(x_range, x_roh, y_roh)
        points=[]
        for i in range(0,len(y_points)):
            points.append(mathe.Point(y_points[i],x_range[i]))
        return points

    def get_new_pos(self, l): # ich gehe davon aus das sich die Einheit nicht ändert !
        """Verändert die Position um den Abstand l. l ist t*v"""
        k=1/self._dStep
        self.point_iterator+=int(k)
        if self.point_iterator >= len(self.points):
            self.point_iterator= len(self.points)-1
        return self.points[self.point_iterator]

    def get_current_pos(self):
        return self.points[self.point_iterator]

    def traveled_distance_on_route(self):
        """"Zurückgelegter Weg auf der Route d.h. wie weit wir schon gefahren sind"""
        k = 1 / self._dStep
        return self.point_iterator*k

    def percent_of_route_still_to_travel(self):
        """Wie viel Prozent der Route noch zurückgelegt werden müssen wobei 0 Prozent heißt das wir angekommen sind und 100 Prozent das wir am Start sind"""
        return 100-(100*self.point_iterator/(len(self.points)-1))

    def get_angle_of_pos(self, pos):
        """Gibt den Winkel zurück so als ob das Auto von Start zu Ende geht"""
    #    return angle

# myStrecke = Strecke([mathe.Point(0.0,0.0),mathe.Point(1.0,2.0),mathe.Point(2.0,4.0),mathe.Point(3.0,8.0)])
# myRoute = Route(myStrecke,0.1)
# print(myRoute.get_current_pos())
# print(myRoute.percent_of_route_still_to_travel())
# print(myRoute.get_new_pos(1))
# print(myRoute.percent_of_route_still_to_travel())
# print(myRoute.get_new_pos(1))
# print(myRoute.percent_of_route_still_to_travel())
# print(myRoute.get_new_pos(1))
# print(myRoute.percent_of_route_still_to_travel())
