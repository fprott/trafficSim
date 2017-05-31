from mathe import *

class Car:
    """Car Klasse. Diese Klasse bietet die Grundlage aller Auto Objekte und soll nach möglichkeit geerbt werden"""
    def __init__(self, id, a_max, a_min, v_max, v_min, v, a, start_pos, car_size):
        self.id=id
        self.a_min = a_min
        self.a_max = a_max
        self.v_max = v_max
        self.v_min = v_min

        self.a = a
        self.v = v #
        self.pos = start_pos
        self.route = Route(start_pos) # TODO Implement me :D
        self.size = car_size

    def _set_v(self, new_v):
        if (new_v <= self.max_v):
            self.v = new_v
        else:
            self.v = self.max_v

    def _set_a(self, new_a):
        if (new_a <= self.max_a):
            self.a = new_a
        else:
            self.a = self.max_a
        pass

    def get_pos(self):
        """
        Gibt momentane Possition zurück
        :return: Einen Punkt in Form von Klasse Point
        """
        return self.pos

    def get_possible_a_range(self, N):
        """
        Gibt N äquidistante mögliche beschleunigungswerte zurück
        :return:
        """
        da = (self.a_max-self.a_min)/(N-1)
        a_values= list();
        for i in range(0, N):
            a_values.append(self.a_min+ da*i)
        return a_values

    def get_a_by_da(self, da):
        """
        Gibt eine legale Beschleunigung abhängig von einer Beschleunigunsänderung da an. Beachtet die minimal und maximal Beschleunigung.
        :return:
        """
        if (self.a+da <= self.max_a): # wenn die neue beschleunigung kleiner als max beschleunigung
            if(self.a+da >= self.min_a): # und wenn die (möglicherweise negative) beschleunigung größer als min beschleunigung
                return self.a+da;
            else:
                return self.min_a
        else:
            return self.max_a

    #def get_next_car(self, dt, new_a):
    #    """new_a ist ein Wert aus der Liste a_values"""
    #    new_v = self.v + new_a * dt  # wir erechnen die neue geschwindigkeit
    #    new_pos = self.s + self.v * dt +0.5*new_a*dt*dt;  # wir erechnen die neue Position
    #    #new_x="";
    #    #nex_y="";   to DO
    #    return Cars(self.id, self.a_min, self.a_max,new_pos, new_v, new_a, new_x, new,y, self.length, self.nr_intervals)  # make the next ghost

    def __str__(self):  # TODO mehr Werte
        return (str(self.id) + " " + str(self.a))

class CarSize():
    def __init__(self):
        pass  # TODO implement me

    def get_size(self):
        pass  # TODO implement me

class Route():
    def __init__(self):
        pass # TODO Implement me, wang

    def basic_route(points, width): #points can only be given by 3 points like [[1,4],[2,1],[5,1]]
        from matplotlib import pyplot as plt

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

        s13 = ((x3 - x1) ** 2 + (y3 - y1) ** 2) ** 0.5
        s35 = ((x3 - x5) ** 2 + (y3 - y5) ** 2) ** 0.5

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
        return xvals,yvals
        #plt.plot(xpoints, ypoints, "ro")
        #plt.show()

    def get_new_pos(self, route, pos, l):
        """Verändert die Position um den Abstand l. l ist t*v"""

    def traveled_distance_on_route(self):
        """"Zurückgelegter Weg auf der Route d.h. wie weit wir schon gefahren sind"""
        return s

    def percent_of_route_still_to_travel(self):
        """Wie viel Prozent der Route noch zurückgelegt werden müssen wobei 0 Prozent heißt das wir angekommen sind und 100 Prozent das wir am Start sind"""
        return p

    def get_angle_of_pos(self, pos):
        """Gibt den Winkel zurück so als ob das Auto von Start zu Ende geht"""
        return angle
