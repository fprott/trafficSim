from mathe import *
from route import *

class Car:
    """Car Klasse. Diese Klasse bietet die Grundlage aller Auto Objekte und soll nach möglichkeit geerbt werden"""
    def __init__(self, id, strecke, a_max, a_min, v_max, v_min, v, a, car_size, pos, route):
        self.id=id
        self.a_min = a_min
        self.a_max = a_max
        self.v_max = v_max
        self.v_min = v_min

        self.strecke = strecke # strecke die das ding schon gefahren ist
        self.a = a
        self.v = v #
#       self.pos = route.get_current_pos()
#        self.route = route
        self.pos = pos
        self.size = car_size

        self.route = route # nur ein POINTER auf Route, da Listen nicht deep-copy werden

    def _set_v(self, new_v):
        if (new_v <= self.v_max):
            self.v = new_v
        else:
            self.v = self.v_max

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
        da = (self.a_max-self.a_min)/(N)
        a_values= list()
        for i in range(0, N):
            a_values.append(self.a_min+ da*i)
        if 0  in a_values:        # 0 muss vorhanden sein
            a_values.remove(0)
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

    def get_next_car(self, dt, da):
       # if self.v == self.v_max or self.v == self.v_min:
        #    return Car("Delete", 0, 0, 0, 0, 0, 0, 0, self.size, self.pos, self.route)
        new_v = self.v+self.a*dt # wir erechnen die neue geschwindigkeit

        if new_v > self.v_max:
            new_v = self.v_max
        if new_v < -self.v_min:
            new_v = self.v_min
    #    new_pos = calculate_pos(self.pos, dt, self.v) # wir erechnen die neue Position
        #new_a = self.get_a_by_da(da)
        new_a = self.get_a_by_da(da)
        if self.v >= self.v_max and new_a > 0:
            new_a=0
        if self.v <= self.v_min and new_a < 0:
            new_a=0

        new_strecke = self.strecke+self.v*dt+new_a*dt*dt*0.5
        new_pos = self.route.get_new_pos_without_position_change(new_strecke) #errechnet nur neue position
        return Car(self.id, new_strecke,self.a_max, self.a_min, self.v_max,self.v_min, new_v, new_a, self.size, new_pos, self.route) #make the next car


    #def get_next_car(self, dt, new_a):
    #    """new_a ist ein Wert aus der Liste a_values"""
    #    new_v = self.v + new_a * dt  # wir erechnen die neue geschwindigkeit
    #    new_pos = self.s + self.v * dt +0.5*new_a*dt*dt;  # wir erechnen die neue Position
    #    #new_x="";
    #    #nex_y="";   to DO
    #    return Cars(self.id, self.a_min, self.a_max,new_pos, new_v, new_a, new_x, new,y, self.length, self.nr_intervals)  # make the next ghost

    def __str__(self):  # TODO mehr Werte
        return ("ID: "+str(self.id) + " current pos: "+str(self.pos)+" a: " + str(self.a)+" v: "+ str(self.v))

def check_collision(cars):
    """
    Prüft ob 2 Autos kollidieren. Bricht ab sobald das war ist. Sagt nicht welche Autos.
    :param cars:
    :return:
    """
    for car_1 in cars:
        for car_2 in cars:
            if(car_1 != car_2):
                # car_1_oben = car_1.pos.x



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


#car1 =

