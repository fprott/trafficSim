from mathe import Point, Line, calculate_pos
import itertools
import functools
import math
from car import *
from route import *
from heapq import *
from enum import Enum
import copy
import time

collision_counter = 0

class QualityFunction(Enum):
    STANDART = 1
    LEVI = 2

class NoPathAvailableError(Exception):
    def __init__(self, message):
        self.message = message

def bulletime(cars, default_t = 100): #muss immer unterschätzen aber nie meher als min_abstand zwischen zwei punkten
    """
    Errechnet die dt und da
    cars = liste mit allen autos, default_dt= dt wenn autos voneinander weit entfernt sind
    """
    i = 0
    t_min = default_t
    # für alle autoparre
    while i<len(cars):
        c1=cars[i]
        j=i+1
        while j<len(cars):
            c2=cars[j]
            #eigentlicher t_min berechnung
            t = _calc_t_min(c1,c2)
            if t_min > t:
                t_min = t
            j+=1
        i+=1
    print("t_min "+str(t_min))
    return t_min

def _calc_t_min(car1,car2):
    #wir nehmen worst-case an, beide autos kommen mit v_max direkt aufeinander zu
    l = math.sqrt((car1.pos.x-car2.pos.x)**2+(car1.pos.y-car2.pos.y)**2)
    v_g = car1.v_max+car2.v_max
    t_min = l/v_g
    return t_min

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
        node = self._do_A_stern() #liefert den Zielknoten
        while(node != self.root):
            best_way.append(node)
            node = node.parent
        best_way.reverse()
        return best_way

    def _do_A_stern(self):
        while len(self.open_list)>0:
            current_node = heappop(self.open_list)
            print("Current Level: " + str(current_node.start_time) + " List lenght: " + str(len(self.open_list)))
            if current_node.target_reached() == True: # wir erwarten das wir eine Lösung finden. Wenn wir eine finden dann ist es automatisch die beste Lösung
                return current_node
            self.closed_list.append(current_node)
            next_nodes = current_node.get_next_senarios(current_node.cars)
            for node in next_nodes:
                if node.cost < float('inf'):
                    heappush(self.open_list,node)
                else:
                    self._remove_subtree_by_time(node,0.25) # wenn das nächste kind einen Unfall baut
        raise NoPathAvailableError("A Stern findet keinen möglichen Pfad. Bitte Eingabe überprüfen!")

    #entfernt bei einem Unfall den Teil des Baums wo der Unfall unvermeidlich ist !
    def _remove_subtree_by_time(self, crash_node, t):
        parrent_node = crash_node.parent
        dt = crash_node.start_time - parrent_node.start_time
        if dt <= t:
            t=t-dt
            #löschen aller kinder des knotens
            for n in parrent_node._children:
                if n in self.open_list:
                    self.open_list.remove(n)
            #self.open_list.remove(parrent_node)
            self._remove_subtree_by_time(parrent_node, t)
        else:
            if crash_node in self.open_list:
                self.open_list.remove(crash_node)

class Senario():
    def __init__(self, parent, start_time, cars):
        """
        :param cars: Eine Liste von CarMarker
        """
        self.cars = cars
        self.parent = parent
        self._children = None # am anfang leer
        self.start_time = start_time
        self.quality_function = QualityFunction.STANDART  # Ändert Gütekriterium TODO richtig übergeben als global !
        self.cost = self._get_cost() # Dieser Aufrruf dient zur Beschleunigung des Programms

    def _get_node_cost(self): # TODO mehr variität !
        global collision_counter
        cost=0
        if(self.quality_function==QualityFunction.STANDART):
            if check_collision(self.cars)==True:
            #    print("Kollision")
                collision_counter+=1
                cost = float('inf')
                return cost
            for car in self.cars:
                cost+=1/(car.a+0.00001) # sehr simpler Algo der angepasst werden sollte
            return cost

        if(self.quality_function==QualityFunction.LEVI):
            if check_collision(self.cars) == True:
                cost = float('inf')
            #    print("Kollision")
                collision_counter+=1
                return cost
            else :
                cost = len(self.cars)*self.start_time
                return cost      #ist start_time die aktuelle Zeit? hiermit würde man die summe der vergangenen Zeiten der Autos berechnen also die Entfernung vom Startpunk kostenmäßig


    def _get_heuristic_cost(self): # TODO mehr variität !
        cost=0
        if(self.quality_function==QualityFunction.STANDART):
            for car in self.cars:
                cost +=car.route.get_percentage_from_start(car.strecke) # sehr simpler Algo der angepasst werden sollte
            return cost
        if(self.quality_function==QualityFunction.LEVI):
            for car in self.cars:
                cost += ((car.route.get_percentage_from_start(car.strecke))*car.route.route_length()) / (1*(car.v_max))  # mal route.länge_der_Strecke
            return cost


    def _get_cost(self):
        return self._get_node_cost()+self._get_heuristic_cost()

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
            if car.route.get_percentage_from_start(car.strecke) !=0:
                print(car.route.get_percentage_from_start(car.strecke))
                return False
        print("Target reach")
        return True

    def get_next_senarios(self, cars):
        if self._children is None:
            dt = bulletime(cars)
            self._children = self._callculate_next_senarios(dt)
            return self._children
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
            for a in a_car.get_possible_a_range(2): #TODO N wählen  ergibt N+1 Beschleunigungen da 0 zwingend dabei ist
                possible_new_cars = possible_new_cars + (a_car.get_next_car(time_step,a),) # ein tupel enhällt alle möglichen nächsten Autos
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
                print("Percent to  travel :" +str(c.route.get_percentage_from_start(c.strecke)) )
            #p=p/len(senario.cars)
            #print("Percent still to travel "+str(p))
            print("-----")
        print("Number of Collisions "+str(collision_counter))


start_time = time.time()
myRoute = Route(Route.castPointsToWangNotation([Point(0.0,0.0),Point(100.0,100.0)]), 2)
myRoute2 = Route(Route.castPointsToWangNotation([Point(0.0,100.0),Point(100.0,0.0)]), 2)
myRoute3 = Route(Route.castPointsToWangNotation([Point(0.0,50.0),Point(100.0,50.0)]), 2)

myCar = Car("test_1", 0.0, 50.0, -60.0, 300.0, 10.0, 0.0, 0.0, CarSize(20,0), myRoute.get_current_pos(), myRoute)
myCar2 = Car("test_2", 0.0, 50.0, -60.0, 300.0, 10.0, 0.0, 0.0, CarSize(30,0), myRoute2.get_current_pos(), myRoute2)
myCar3 = Car("test_2", 0.0, 50.0, -60.0, 300.0, 10.0, 0.0, 0.0, CarSize(30,0), myRoute3.get_current_pos(), myRoute3)


myCars=[]
myCars.append(myCar)
myCars.append(myCar2)
myCars.append(myCar3)
mySenario = Senario(None,0,myCars)
myGraph = Graph(mySenario)
bestSenarios = myGraph.calluclate_best_senarios()

end_time = time.time()


Senario.printDebugSenarios(bestSenarios)
print("run time (s) "+str(end_time-start_time))
