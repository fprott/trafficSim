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

        def simple_car_collision(self, car_2):
            """Kollisionscheck das schnell ist aber nicht exakt"""
            dist = math.hypot(self.pos.x - car_2.pos.x, self.pos.y - car_2.pos.y)
            diag_1 = math.sqrt((self.size.get_width() ** 2) + (self.size.get_length() ** 2))
            diag_2 = math.sqrt((car_2.size.get_width() ** 2) + (car_2.size.get_length() ** 2))
            if dist <= 0.5 * (diag_1 + diag_2):
                return True
            else:
                return False

            def exact_car_collision(self, car_2):
                """Kollision über Separating Axis Theorem ist exact aber langsam und funktioniert noch nicht richtig :D"""
                return 0

    #def get_next_car(self, dt, new_a):
    #    """new_a ist ein Wert aus der Liste a_values"""
    #    new_v = self.v + new_a * dt  # wir erechnen die neue geschwindigkeit
    #    new_pos = self.s + self.v * dt +0.5*new_a*dt*dt;  # wir erechnen die neue Position
    #    #new_x="";
    #    #nex_y="";   to DO
    #    return Cars(self.id, self.a_min, self.a_max,new_pos, new_v, new_a, new_x, new,y, self.length, self.nr_intervals)  # make the next ghost

    def __str__(self):  # TODO mehr Werte
        return (str(self.id) + " " + str(self.a))

def check_collision(cars):
    """
    Prüft ob 2 Autos kollidieren. Bricht ab sobald das war ist. Sagt nicht welche Autos.
    :param cars:
    :return:
    """
    for car_1 in cars:
        for car_2 in cars:
            if(car_1 != car_2):
                # der folgende Algo ist abgeschrieben, ka ob das funktioniert
                dist = math.hypot(self.pos.x - car_2.pos.x, self.pos.y - car_2.pos.y)
                diag_1 = math.sqrt((self.size.get_width() ** 2) + (self.size.get_length() ** 2))
                diag_2 = math.sqrt((car_2.size.get_width() ** 2) + (car_2.size.get_length() ** 2))
                if dist <= 0.5 * (diag_1 + diag_2):
                    return True
    return False


class CarSize():
    """die größere Zahl ist immer length""" # frage, wie baut man damit einen smart nach :D ?
    def __init__(self, width, length):
        if length >= width :
            self.width = width
            self.length = length
        else:
            self.width=length
            self.length=width

    def get_width(self):
        return self.width

    def get_length(self):
        return self.length

class Route():
    def __init__(self):
        pass # TODO Implement me, wang

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
        from matplotlib import pyplot as plt

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

        #print(new_p)
        #print(x)
        #print(len(x))
        #plt.plot(x, y,"go")
        #plt.show()
        return x,y

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








