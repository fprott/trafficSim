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
        da = (self.a_max-self.a_min)/(N-1)
        a_values= list();
        for i in range(0, N):
            new_a = self.a_min+ da*i
#            a_values.append(new_a)
            if new_a >0: # macht das nicht schneller :D
                if self.v < self.v_max:
                    a_values.append(new_a)
            else:
                a_values.append(new_a)

        if 0 not in a_values:        # 0 darf nicht vorhanden sein sonst ist dass das gleiche
            a_values.append(0);
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
    def get_cornerpoints(self,angle):
        Ox=self.size.get_length()*0.5
        Oy=self.size.get_width()*0.5
        Rx = self.pos.x + (Ox * math.cos(angle)) - (Oy * math.sin(angle))
        Ry = self.pos.y + (Ox * math.sin(angle)) + (Oy * math.cos(angle))
        forward_left = Point(Rx,Ry)

        Ox = self.size.get_length() * 0.5
        Oy = -self.size.get_width() * 0.5
        Rx = self.pos.x + (Ox * math.cos(angle)) - (Oy * math.sin(angle))
        Ry = self.pos.y + (Ox * math.sin(angle)) + (Oy * math.cos(angle))
        forward_right = Point(Rx,Ry)

        Ox = -self.size.get_length() * 0.5
        Oy = self.size.get_width() * 0.5
        Rx = self.pos.x + (Ox * math.cos(angle)) - (Oy * math.sin(angle))
        Ry = self.pos.y + (Ox * math.sin(angle)) + (Oy * math.cos(angle))
        back_left = Point(Rx, Ry)

        Ox = -self.size.get_length() * 0.5
        Oy = -self.size.get_width() * 0.5
        Rx = self.pos.x + (Ox * math.cos(angle)) - (Oy * math.sin(angle))
        Ry = self.pos.y + (Ox * math.sin(angle)) + (Oy * math.cos(angle))
        back_right = Point(Rx,Ry)
        return [forward_left,forward_right, back_left, back_right]

    def get_crash_zone(car1, car2, dt,time):
        safe_distance = 0.5*(car_1.size.get_length()+car_2.size.get_length())
        actuall_distance = math.hypot(car1.pos.x - car2.pos.x, car1.pos.y - car2.pos.y)
        error = safe_distance - actuall_distance
        t = math.sqrt((2*error)/car1.a_min)
        if t < dt:
            t=dt
        return t












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
                #if dist <= 0.5 * (diag_1 + diag_2):
                if dist <= 0.5*(car_1.size.get_length()+car_2.size.get_length()):
                    return True
    return False

# car1 und car2 haben zum jetzigen Zeitpunkt eine Kollision
# gibt die länge an die car1 nichts machen kann um die Kollision zu vermeiden
# car2 wird in der Zwischenzeit in ruhe gelassen
# wir nehmen das car was kleiners t hat dann später !

#def get_crash_zone2(time, car1,car2):
#    v1 = car1.getVec
#    v2 = car2.getVec
    # finde p_crash; p_crash = oberster punkt (vektoriel gesehen) an dem die Autos sich berühren
#    P = Point(math.abs(car1.pos.x-car2.pos.x)*0.5,math.abs(car1.pos.y-car2.pos.y)*0.5)
#    if car1.pos.x <= car2.pos.x:
#        x = car1.pos.x + P.x
#    else:
#        x= car2.pos.x +P.x
#    if car1.pos.y <= car2.pos.y:
#        y= car1.pos.y + P.y
#    else:
#        y= car2.pos.y + P.y
#    p_crash = Point(x,y)









    # finde p_end; p_end = wir verlassen das car2 an der stelle
#    p_end = car2.pos.x*cos(winkel)-sin(winkel)+car2.pos.y*sin(winkel)+cos(winkel)
    # s finden; s = länge von berühungspunkt bis ende des autos
#    car2.size.get_length()#levi
    # t_min erechen; t_min = zeit die vergeht bis car2 wegefahren ist









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



myRoute = Route(Route.castPointsToWangNotation([Point(0.0,0.0),Point(100.0,100.0)]), 2)



myCar = Car("test_1", 0.0, 55.0, -60.0, 300.0, 10.0, 0.0, 0.0, CarSize(30,10), myRoute.get_current_pos(), myRoute)
print(myCar.get_cornerpoints(3.14/2))
