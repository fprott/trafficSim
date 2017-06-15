from mathe import *
from route import *

class Car:
    """Car Klasse. Diese Klasse bietet die Grundlage aller Auto Objekte und soll nach möglichkeit geerbt werden"""
    def __init__(self, id, route, a_max, a_min, v_max, v_min, v, a, car_size):
        self.id=id
        self.a_min = a_min
        self.a_max = a_max
        self.v_max = v_max
        self.v_min = v_min

        self.a = a
        self.v = v #
        self.pos = route.get_current_pos()
        self.route = route
        self.size = car_size

    def _set_v(self, new_v):
        if (new_v <= self.max_v):
            self.v = new_v
        else:
            self.v = self.max_v

    def _set_a(self, new_a):
        if (new_a <= self.a_max):
            self.a = new_a
        else:
            self.a = self.a_max
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
        if (self.a+da <= self.a_max): # wenn die neue beschleunigung kleiner als max beschleunigung
            if(self.a+da >= self.a_min): # und wenn die (möglicherweise negative) beschleunigung größer als min beschleunigung
                return self.a+da
            else:
                return self.a_min
        else:
            return self.a_max

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
                dist = math.hypot(car_1.pos.x - car_2.pos.x, car_1.pos.y - car_2.pos.y)
                diag_1 = math.sqrt((car_1.size.get_width() ** 2) + (car_1.size.get_length() ** 2))
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
