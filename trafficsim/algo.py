import copy

from mathe import Point, Line, calculate_pos
import itertools
import functools
import math
from car import *
from route import *

from heapq import *

class Graph():
    """
    Der Graph enhällt als Knoten alle Senarien. Auf dem Graph wird ein A* Algo ausgeführt. Der Graph wird nur wenn notwendig angepasst.
    """
    def __init__(self, root_senario):
        self.nodes = [] # Eine Liste von Senarios
        self.root = root_senario # wir merken uns den root da dieser unveränderlich ist

        self.open_list=[] # erkannte und geprüfte nodes
        heappush(self.open_list, root_senario) # wir sotieren in O(1) mittels heap :D

        self.closed_list=set() # erkannte aber noch nicht geprüfte nodes

    def calluclate_best_senarios(self):
        best_way=[]
        node = self._do_A_star()
        while(node != self.root):
            best_way.append(node)
            node = node.parent
        best_way.reverse()
        return best_way

    def _do_A_star(self):
        while(len(self.open_list)>0):
            current_node = self.get_current_node()
            if(current_node==None):
                break
            if (current_node.target_reached() == True): # wir erwarten das wir eine Lösung finden. Wenn wir eine finden dann ist es automatisch die beste Lösung
                return current_node

            self.closed_list.add(current_node)
            self._expand_graph(current_node)
        raise NoPathAvailableError("A Stern findet keinen möglichen Pfad. Bitte Eingabe überprüfen!")

    def get_current_node(self):
        if(len(self.open_list)>0):
            current_node = heappop(self.open_list)
            for old_nodes in self.closed_list:
                if current_node.compare_with_other(old_nodes):
                    self.get_current_node()
            if current_node.get_cost()==float('inf'):
                return None
            return current_node
        else:
            return None

    def _expand_graph(self, node): #should expand by the factor of N
        """
        Erweiteret den Graphen um alle möglichen Kinder des Nodes und nur um diese
        :param node:
        :return:
        """
        time_step =  1# bulletime(node.cars)
    #    print(time_step)
        new_nodes = node.callculate_next_senarios(time_step) # break second loop !
        # for node in new_nodes:
        #     print(node.start_time)
        # print("---")
        for n in new_nodes:
        #    if n.get_cost()!=float('inf'):
            heappush(self.open_list, n) # Achtung, noch gibt es keine Zusammenführung d.h. keine möglichkeit das ein node zwei Eltern hat

class NoPathAvailableError(Exception):
     def __init__(self, message):
         self.message = message

class Senario():
    def __init__(self, parent, start_time, cars):
        """
        :param cars: Eine Liste von CarMarker
        """
        self.cars = cars
        self.parent = parent
        self.start_time = start_time
    #    self.cost = self.get_node_cost()+self.get_heuristic_cost() # Dieser Aufrruf dient zur Beschleunigung des Programms

    def get_node_cost(self): # TODO mehr variität !
        cost=0
        if(check_collision(self.cars)==True):
        #    print("Kollision")
            cost = float('inf')
            return cost
        for car in self.cars:
            cost+=1/(car.a+0.00001) # sehr simpler Algo der angepasst werden sollte
        return cost

    def get_node_cost_2(self):
        cost=0
        if (check_collision(self.cars) == True):
            cost = float('inf')
            return cost
        return len(self.cars)*self.start_time      #ist start_time die aktuelle Zeit? hiermit würde man die summe der vergangenen Zeiten der Autos berechnen also die Entfernung vom Startpunk kostenmäßig

    def get_heuristic_cost_2(self):
        cost=0;
        for car in self.cars:
            cost +=(car.route.percent_of_route_still_to_travel())/(car.v_max+car.v)  # mal route.länge_der_Strecke
        return cost

    def get_heuristic_cost(self): # TODO mehr variität !
        cost=0
        for car in self.cars:
            cost +=car.route.percent_of_route_still_to_travel() # sehr simpler Algo der angepasst werden sollte
        return cost

    def get_cost(self):
        return self.get_node_cost()+self.get_heuristic_cost()

    def __lt__(self, other): # Iterator !
        return (self.get_cost())<(other.get_cost())
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
        return True

    def callculate_next_senarios(self, time_step):
        new_time = self.start_time + time_step

        all_possible_car_tuples = []
        #Bilde ein tuple pro auto mit verschieden Werten
        for a_car in self.cars:
        #    print(a_car)
            possible_new_cars = ()
            #print(a_car.get_possible_a_range(5))
            for a in a_car.get_possible_a_range(5): #TODO N wählen
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
        #    for car in possiblity:
        #        print(car) #soll immer 2 autos mixen
        #    print("----")
            all_possible_steps.append(Senario(self, new_time, possiblity))
        return all_possible_steps

    def printDebugSenarios(senarios):
        for senario in senarios:
            print("Timestep "+str(senario.start_time))
            p=0
            print("Current Cars:")
            for c in senario.cars:
                print(c)
                p+=c.route.percent_of_route_still_to_travel()
            p=p/len(senario.cars)
            print("Percent still to travel "+str(p))
            print("-----")

class CarMarker(Car):
    """
    Die Klasse CarMarker besteht aus einem Auto zu einer bestimmten Position. Es findet keine Bewegung dies Autos statt
    """
    def get_next_car_marker(self, dt, da):
        new_v = self.v+self.a*dt # wir erechnen die neue geschwindigkeit

        if new_v > self.v_max:
            new_v = self.v_max
        if new_v < -self.v_min:
            new_v = self.v_min
    #    new_pos = calculate_pos(self.pos, dt, self.v) # wir erechnen die neue Position
        new_a = self.get_a_by_da(da)
        new_route = copy.deepcopy(self.route) # Deep copy, achtung Flaschenhals TODO verbeser speicher ausnutzung
        new_route.get_new_pos(self.v*dt)
        return CarMarker(self.id, new_route, self.a_max, self.a_min, self.v_max,self.v_min, new_v, new_a, self.size) #make the next ghost


def bulletime(cars, default_dt=1): #
    """
    Errechnet die dt und da
   cars = liste mit allen autos, default_dt= dt wenn autos voneinander weit entfernt sind
    """
    safe_zone=1;
    for i in range(len(cars)):
        for j in range(i + 1, len(cars)):
            dist = math.hypot(cars[i].pos.x - cars[j].pos.x, cars[i].pos.y - cars[j].pos.y);    #autos werden vereinfacht als kreise modelliert'
            if dist <= 1.4*(cars[i].size.get_length()+cars[j].size.get_length()):
                safe_zone=0;
                break
        if safe_zone == 0:
            break
    #'sobald ein Paar Autos welches nicht in der safe_zone ist gefunden wurde, werden die for schleifen abgebrochen...bei safe_Zone' \
    #'bleibt die Abtastzeit gleich dt_default in der danger_zone verkleinern wir die abtastzeit um das 10-fache...wert ist wilkürlich gewählt worden'
    if  safe_zone == 1:
        dt=default_dt;
    else:
        dt = default_dt / 10;          #da = bleibt gleich...wir können aber wegen dem neuen dt den kurs der Autos öfters korrigieren

    return dt


#Wang test
# myRoute_1 = Route([Point(0.0,0.0),Point(100.0,200.0),Point(200.0,400.0),Point(300.0,800.0)], 2.0)
# myRoute_2 = Route([Point(300.0,800.0),Point(200.0,400.0),Point(100.0,200.0),Point(0.0,0.0)], 2.0)
#
# print(myRoute_1.get_current_pos())
# print(myRoute_1.traveled_distance_on_route())
# print(myRoute_1.percent_of_route_still_to_travel())
# print(myRoute_1.get_new_pos(100.0))
# print(myRoute_1.get_current_pos())
# print(myRoute_1.traveled_distance_on_route())
# print(myRoute_1.percent_of_route_still_to_travel())


myRoute = Route(Route.castPointsToWangNotation([Point(0.0,0.0),Point(100.0,0.0),Point(200.0,0.0),Point(300.0,0.0)]), 2)
myRoute2 = Route(Route.castPointsToWangNotation([Point(300.0,0.0),Point(200.0,0.0),Point(100.0,0.0),Point(0.0,0.0)]), 2)

# myRoute = Route(Route.castPointsToWangNotation([Point(0.0,0.0),Point(100.0,100.0)]), 2)
# myRoute2 = Route(Route.castPointsToWangNotation([Point(0.0,100.0),Point(100.0,0.0)]), 2)
#myRoute2 = Route([[0.0,800.0],[100.0,400.0],[200.0,200.0],[300.0,0.0]] , 2)

# print(myRoute2.get_current_pos())
# #print(myRoute2.percent_of_route_still_to_travel())
# #print(myRoute2.get_new_pos(100))
# #print(myRoute2.percent_of_route_still_to_travel())
#
# print(myRoute2.get_new_pos(1000))
# print(myRoute2.percent_of_route_still_to_travel())
#
# print(myRoute2.get_new_pos(1000))
# print(myRoute2.percent_of_route_still_to_travel())
#
# print(myRoute2.get_new_pos(10000))
# print(myRoute2.percent_of_route_still_to_travel())

myCar = CarMarker("test_1", myRoute, 20.0, 20.0, 300.0, 20.0, 0.0, 0.0, CarSize(50,20))
myCar2 = CarMarker("test_2", myRoute2, 40.0, 20.0, 120.0, 20.0, 0.0, 0.0, CarSize(50,20))
myCars=[]
myCars.append(myCar)
myCars.append(myCar2)
mySenario = Senario(None,0,myCars)
myGraph = Graph(mySenario)
bestSenarios = myGraph.calluclate_best_senarios()
Senario.printDebugSenarios(bestSenarios)
