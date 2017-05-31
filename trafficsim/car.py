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
        diag_1 = math.sqrt( (self.size.get_width() ** 2) + (self.size.get_length() ** 2 ) )
        diag_2 = math.sqrt( (car_2.size.get_width() ** 2) + (car_2.size.get_length() ** 2) )
        if dist <= 0.5*(diag_1+diag_2):
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

class CarSize():
    """die größere Zahl ist immer length"""
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

    def __init__(self, start_pos):
        pass # TODO Implement me, wang

    def get_new_pos(self, pos, l):
        """Verändert die Position um den Abstand l. l ist t*v"""

    def traveled_distance_on_route(self):
        """"Zurückgelegter Weg auf der Route d.h. wie weit wir schon gefahren sind"""
        return s

    def percent_of_route_still_to_travel(self):
        """"Wie viel Prozent der Route noch zurückgelegt werden müssen wobei 0 Prozent heißt das wir angekommen sind und 100 Prozent das wir am Start sind"""
        return p

    def get_angle_of_pos(self, pos):
        """Gibt den Winkel zurück so als ob das Auto von Start zu Ende geht"""
        return angle


#Test
#pos1 = Point(0,0)
#pos2 = Point(500,4)
#size1 = CarSize(10,20)
#car1 = Car(1,1,1,1,1,1,1,pos1,size1)
#car2 = Car(1,1,1,1,1,1,1,pos2,size1)
#b = car1.simple_car_collision(car2)
#print(b)
