from mathe import Point, Line, calculate_pos
import itertools
import functools
import math
from car import *
from route import *
from heapq import *
from enum import Enum

class QualityFunction(Enum):
    STANDART = 1
    LEVI = 2

class NoPathAvailableError(Exception):
    def __init__(self, message):
        self.message = message

def bulletime(cars, default_dt=1): #muss immer unterschätzen aber nie meher als min_abstand zwischen zwei punkten
    """
    Errechnet die dt und da
   cars = liste mit allen autos, default_dt= dt wenn autos voneinander weit entfernt sind
    """
    return 0.25

class Graph():
    """
    Der Graph enhällt als Knoten alle Senarien. Auf dem Graph wird ein A* Algo ausgeführt. Der Graph wird nur wenn notwendig angepasst.
    """
    def __init__(self, root_senario):
        self.open_list = [] #erkannte aber noch nicht geprüfte / benutzte knoten
        self.closed_list = [] # erkannte und behandelte knoten
        self.root = root_senario
        heappush(self.open_list, root_senario) # der root ist der erste zu prüfende

    def calluclate_best_senarios(self):
        best_way=[]
        node = self._do_A_star() #liefert den Zielknoten
        while(node != self.root):
            best_way.append(node)
            node = node.parent
        best_way.reverse()
        return best_way


    def _do_a_stern(self):
        while len(self.open_list)>0:
            current_node = heappop(self.open_list)
            if current_node.target_reached() == True: # wir erwarten das wir eine Lösung finden. Wenn wir eine finden dann ist es automatisch die beste Lösung
                return current_node
            self.closed_list.append(current_node)
            next_nodes = current_node.get_next_senarios()
            for node in next_nodes:
                if node.cost < float('inf'):
                    heappush(self.open_list,node)
        raise NoPathAvailableError("A Stern findet keinen möglichen Pfad. Bitte Eingabe überprüfen!")


class Senario():
    def __init__(self, parent, start_time, cars):
        """
        :param cars: Eine Liste von CarMarker
        """
        self.cars = cars
        self.parent = parent
        self._children = None # am anfang leer
        self.start_time = start_time
        self.quality_function = QualityFunction.LEVI  # Ändert Gütekriterium TODO richtig übergeben als global !
        self.cost = self._get_cost() # Dieser Aufrruf dient zur Beschleunigung des Programms

    def _get_node_cost(self): # TODO mehr variität !
        cost=0
        if(self.quality_function==QualityFunction.STANDART):
            if check_collision(self.cars)==True:
            #    print("Kollision")
                cost = float('inf')
                return cost
            for car in self.cars:
                cost+=1/(car.a+0.00001) # sehr simpler Algo der angepasst werden sollte
            return cost

        if(self.quality_function==QualityFunction.LEVI):
            if check_collision(self.cars) == True:
                cost = float('inf')
            #    print("Kollision")
                return cost
            else :
                cost = len(self.cars)*self.start_time
                return cost      #ist start_time die aktuelle Zeit? hiermit würde man die summe der vergangenen Zeiten der Autos berechnen also die Entfernung vom Startpunk kostenmäßig


    def _get_heuristic_cost(self): # TODO mehr variität !
        cost=0
        if(self.quality_function==QualityFunction.STANDART):
            for car in self.cars:
                cost +=car.route.percent_of_route_still_to_travel() # sehr simpler Algo der angepasst werden sollte
            return cost
        if(self.quality_function==QualityFunction.LEVI):
            for car in self.cars:
                cost += ((car.route.percent_of_route_still_to_travel())*car.route.route_length()) / (1*(car.v_max))  # mal route.länge_der_Strecke
            return cost


    def _get_cost(self):
        return self.get_node_cost()+self.get_heuristic_cost()

    def __lt__(self, other): # Iterator !
        return (self.cost)<(other.cost)
        #  return self.cost < other.cost

    def compare_with_other(self, other):
        if self.start_time == other.start_time and self.parent == other.parent:
            i=0
            while i<len(self.cars):
                if self.cars[i].pos == other.cars[i].pos and self.cars[i].v == other.cars[i].v:
                    return True
        return False

    def target_reached(self):
    #    print("----")
        for car in self.cars:
    #        print(car.route.percent_of_route_still_to_travel())
            if car.route.percent_of_route_still_to_travel() !=0:
                return False
        print("Target reach")
        return True

    def get_next_senarios(self, cars):
        if self._children is None:
            dt = bulletime(cars)
            self._children = self._callculate_next_senarios(dt) #ERROR!!!!!!
        else:
            return self._children

    def _callculate_next_senarios(self, time_step):
        new_time = self.start_time + time_step
    #    print(self.start_time)
        all_possible_car_tuples = []
        #Bilde ein tuple pro auto mit verschieden Werten
        for a_car in self.cars:
        #    print(a_car)
            possible_new_cars = ()
            #print(a_car.get_possible_a_range(5))
            for a in a_car.get_possible_a_range(5): #TODO N wählen  ergibt N+1 Beschleunigungen da 0 zwingend dabei ist
                possible_new_cars = possible_new_cars + (a_car.get_next_car_marker(time_step,a),) # ein tupel enhällt alle möglichen nächsten Autos
            all_possible_car_tuples.append(possible_new_cars) # List von tupeln, darf NICHT in der for schleife sein !

        #print(tuple(all_possible_car_tuples))
        # for ct in all_possible_car_tuples:
        #     print("--")
        #     for c in ct:
        #         print(c)
        #         pass

        all_car_possiblites = list(itertools.product(*all_possible_car_tuples)) # hexerei, bitte schaut euch die doku an wenn das net geht #BUUUG
        #EXAMPLE
        # l = [("A1","A2"),("B1","B2"),("C1","C2")]
        # ap = list(itertools.product(*l))
        # ap ist dann
        # [('A1', 'B1', 'C1'),
        #  ('A1', 'B1', 'C2'),
        #  ('A1', 'B2', 'C1'),
        #  ('A1', 'B2', 'C2'),
        #  ('A2', 'B1', 'C1'),
        #  ('A2', 'B1', 'C2'),
        #  ('A2', 'B2', 'C1'),
        #  ('A2', 'B2', 'C2')]

        all_possible_steps = []
        for possiblity in all_car_possiblites:
            # for car in possiblity:
            #     print(car) #soll immer 2 autos mixen
            # print("----")
            all_possible_steps.append(Senario(self, new_time, possiblity))
        self.children=all_possible_steps
        return all_possible_steps


    def printDebugSenarios(senarios):
        for senario in senarios:
            print("Timestep "+str(senario.start_time))
            p=0
            print("Current Cars:")
            for c in senario.cars:
                print(c)
                print(c.size.get_width())
                #p+=c.route.percent_of_route_still_to_travel()
                print("Percent to  travel :" +str(c.route.percent_of_route_still_to_travel()) )
            #p=p/len(senario.cars)
            #print("Percent still to travel "+str(p))
            print("-----")

class CarMarker(Car):
    """
    Die Klasse CarMarker besteht aus einem Auto zu einer bestimmten Position. Es findet keine Bewegung dies Autos statt
    """
    def __init__(self, id, route, a_max, a_min, v_max, v_min, v, a, car_size, new_pos):
        super.__init__(id, route, a_max, a_min, v_max, v_min, v, a, car_size)
        self.pos = new_pos

    def get_next_car_marker(self, dt, da):
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

        new_pos = self.route.get_next_pos_from_pos(self.pos, self.v*dt+new_a*dt*dt*0.5) #errechnet nur neue position

        return CarMarker(self.id, self.route, self.a_max, self.a_min, self.v_max,self.v_min, new_v, new_a, self.size, new_pos) #make the next ghost
