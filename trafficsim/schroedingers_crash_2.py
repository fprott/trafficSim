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

class NoPathAvailableError(Exception):
    def __init__(self, message):
        self.message = message

class Algo():
    def __init__(self,root_scenario):
        self.root_scenario = root_scenario
        root_scenario.build_self() #wir bauen also den Graph selber auf
        self.scenarios = [root_scenario]
        self.possible_solutions = []

    def do_algo(self):
        while len(self.scenarios)>0:
            scenario = self.scenarios.pop()
            printDebugFirstCollision(scenario)
            collision, scenario1, scenario2 = scenario.do_the_schroedinger()
            if collision==True:
            #    printDebugScenario(scenario)
                if scenario1 != None:
                    self.scenarios.append(scenario1)
                if scenario2 != None:
                    self.scenarios.append(scenario2)
                # print("XXXXXXXXXXXXXXXXXXXXXXXXXX")
                # printDebugScenario(scenario1)
                # print("XXXXXXXXXXXXXXXXXXXXXXXXXX")
                # printDebugScenario(scenario2)

            else: #keine Kollision
                self.possible_solutions.append(scenario)
                print("NICE")
        raise NoPathAvailableError("Algo findet keinen möglichen Pfad. Bitte Eingabe überprüfen!")

def printDebugScenario(scenario):
    for node in scenario.nodes:
        print("Timestep "+str(node.start_time))
        p=0
        print("Current Cars:")
        for c in node.cars:
            print(c)
            #print(c.size.get_width())
            #p+=c.route.percent_of_route_still_to_travel()
            print("Percent to  travel :" +str(c.route.get_percentage_from_start(c.strecke)) )
        #p=p/len(scenario.cars)
        #print("Percent still to travel "+str(p))
        print("Crash?: "+str(check_collision(node.cars)))
        print("-----")

def printDebugFirstCollision(scenario):
    i=0
    for node in scenario.nodes:
        if check_collision(node.cars) ==True :
            print("First collision : " + str(i))
        i+=1

class Graph():
    def __init__(self, start_node):
        self.root = start_node
        self.nodes = [start_node]

    #einmal (!) beim start aufrufen !
    def build_self(self):
        last_node = self.nodes[-1]
        if last_node.target_reached():
            return
        new_cars = []
        dt = self.get_dt()
        for car in last_node.cars:
            new_cars.append(car.get_next_car(dt, car.a_max))  # wir fahren so schnell wie möglich im ersten versuch

        new_node = Node(last_node.start_time + dt, new_cars, last_node)
        self.nodes.append(new_node)
        self.build_self()

    #weil route blöd ist müssen wir alle autos neu bauen XD
    def rebuild_self(self): #suppppper inefizent XD
        curren_node = self.root
        new_nodes = [self.root]

        for old_node in self.nodes:
            dt = self.get_dt()
            new_cars = []
            for car in old_node.cars:
                new_cars.append(car.get_next_car(dt, car.a))
            #    print(car.a)
            new_node = Node(curren_node.start_time + dt, new_cars, curren_node)
            new_nodes.append(new_node)
            curren_node = new_node
        self.nodes = new_nodes

    def get_dt(self):
        return 0.1

    def get_first_collision(self):
        for node in self.nodes:
            if check_collision(node.cars) == True:
                car1,car2 = get_first_two_cars_that_collide(node.cars) #ineffizient aber erstmal gehts nur ums prinzip
            #    print(node.start_time)
                return node, car1,car2
        return None, None, None

    #macht eine deepcopy des Graphen
    def clone_self(self):
        #clone = copy.deepcopy(self()) #geht nicht !
        clone = Graph(self.root)
        new_nodes = []
        for node in self.nodes:
            new_cars = []
            for car in node.cars:
                new_pos = Point(car.pos.x, car.pos.y)
                new_car = Car(car.id, car.strecke, car.a_max, car.a_min, car.v_max, car.v_min, car.v, car.a, car.size, new_pos, car.route)
                new_cars.append(new_car)
            new_node = Node(node.start_time, new_cars, node.parent)
            new_nodes.append(new_node)
        clone.nodes = new_nodes
        return clone

    def do_the_schroedinger(self):
        #Geht den Graphen bis zur ersten Kollision durch und splittet diesen dann in zwei, gibt ein True für "Kollision" zurück
        #Wenn es keine Kollision gibt geben wir None als graphen zurück und ein False
        crash_node, car1, car2 = self.get_first_collision()
     #   print(crash_node)
        if crash_node==False: #wenn wir keinen Crash haben !
            return False, None, None
        g1 = self._make_alternative_reality(crash_node, car1, car2) # möglichkeit 1: das erste auto bremst
        # print("Vorher")
        # for n in self.nodes:
        #     print(n)
        #     # for c in n.cars:
        #     #     print(c.a)

        # print("nachher")
        # for n in g1.nodes:
        #     print(n)
        #     # for c in n.cars:
        #     #     print(c.a)
        g2 = self._make_alternative_reality(crash_node, car2, car1) # möglichkeit 2: das zweite auto bremst

    #    g2 = None
        return True, g1,g2

    def _make_alternative_reality(self, crash_node, car_to_break, car_not_to_break):
        dt = self.get_dt()
    #    print(crash_node)
        crash_node_index = self.nodes.index(crash_node)  # wir arbeiten mit dem index weil der sich nicht ändern kann, die objekte schon
        car_index = crash_node.cars.index(car_to_break)
        s_break = self.get_crash_avoidance_distance(car_to_break, car_not_to_break)
    #    v_break = s_break/self.get_dt() # um diese geschwindkeit müssen wir langsamer werden

        new_graph = self.clone_self()  # wir haben eine exakte kopie des Graphen
        # jetzt bügeln wir den crash aus


#%%%
        # i=0
        # while s_break > 0:
        # #    print(s_break)
        # #    print("index "+str(crash_node_index + i))
        #     a_momentan = new_graph.nodes[crash_node_index - i].cars[car_index].a
        #     a_min = new_graph.nodes[crash_node_index - i].cars[car_index].a_min
        #     v_momentan = new_graph.nodes[crash_node_index - i].cars[car_index].v
        #     # s_momentan = new_graph.nodes[crash_node_index - i].cars[car_index].strecke
        #     a_diff = a_momentan - a_min
        #     s_break-=a_diff*1/2*dt*dt#+dt*v_momentan
        #     new_graph.nodes[crash_node_index - i].cars[car_index].a = a_min
        #     if crash_node_index - i <= 0 : #wenn wir zu weit gehen
        #         return None # kein scenario möglich !
        #     i += 1
#%%%
        # jetzt müssen wir leider noch die knoten aktuallisieren
    #    i+=1 # wir starten beim knoten BEFOR der letzen änderung

        # current_node = new_graph.nodes[crash_node_index - i]
        # while i != 0:
        #     dt = self.get_dt()
        #     new_cars = []
        #     for car in current_node.cars:
        #         new_cars.append(car.get_next_car(dt, car.a))  # wir fahren wie geplant diesemal
        #     i -= 1
        #     current_node = new_graph.nodes[crash_node_index - i]
        #     current_node.cars = new_cars



        # new_strecke = self.strecke + self.v * dt + new_a * dt * dt * 0.5
        # i=0
        # while v_break > 0:
        #     v_momentan = new_graph.nodes[crash_node_index - i].cars[car_index].v
        #     v_minimal = new_graph.nodes[crash_node_index - i].cars[car_index].v_min
        #     dv = v_minimal -v_momentan
        #     v_break -= dv
        #
        # d = v_break_anteil_soviel_wie_möglich *dt + new_a * dt *dt *0.5

     #   print("geht")
     #   num_of_breaks, break_a = self.get_breaking_a_and_i(s_break, car_to_break, self.get_dt()) #kapput XD
     #   print("^ putt")

        new_graph = self.clone_self()  # wir haben eine exakte kopie des Graphen
        a_min = new_graph.nodes[crash_node_index].cars[car_index].a_min
        s_tb = a_min * 1/2* dt*dt
        a_p=s_break/s_tb
        a_p=-a_p
        a_p = 100
        print(a_p)
    #    a_p = -(num_of_breaks*break_a+break_a) #TODO fixen
     #   print(a_p)
        # jetzt bügeln wir den crash aus
        i = 0
        while a_p > 0:
            a_momentan = new_graph.nodes[crash_node_index - i].cars[car_index].a
            a_min = new_graph.nodes[crash_node_index - i].cars[car_index].a_min
            a_diff = a_momentan - a_min
            new_graph.nodes[crash_node_index - i].cars[car_index].a = a_min
            a_p -= a_diff
            if crash_node_index - i < 0 : #wenn wir zu weit gehen
                print("KKKAPPPUT")
                return None # kein scenario möglich !
            i += 1

        new_graph.rebuild_self()
        # printDebugScenario(self)
        # print("XXXXXXXXXXXXXXXXXXXXXX")
        # printDebugScenario(new_graph)

        return new_graph



    #abstand den man einhalten muss damit der unfall vermident werden kann
    #car_to_break, car_not_to_break
    def get_crash_avoidance_distance(self,car_to_break , car_not_to_break):
        return car_not_to_break.size.get_length() + car_not_to_break.size.get_width()  # TODO schlauer machen, super blöd aber geht schnomal

    # Stecke = zur Vermeidung der Kollision
    # a = Beschleunigung die zur kollision geführt hat
    # dt = Zeit zwischen Knoten
    def get_breaking_a_and_i(self, Strecke, car_to_break, dt):
        distance = 0
        i = 0
        while (distance < Strecke):
            i = i + 1
            distance = (car_to_break.a - car_to_break.a_min) * (i * dt) * (i * dt) * 0.5
            #  if distance > Strecke:
            #     while distance >= Strecke:
            #           distance = (a-car.a_min + car.)*(i*dt)*(i*dt)*0.5
        return i, car_to_break.a_min  # du musst dann i mal


    # def does_graph_crash(self):
    #     true/False
    #
    # def



class Node():
    def __init__(self, t, cars, parent):
        self.cars = cars
        self.start_time = t
        self.parent = parent

    def target_reached(self):
    #    print("----")
        for car in self.cars:
    #        print(car.route.percent_of_route_still_to_travel())
            if car.route.get_percentage_from_start(car.strecke) !=0:
            #    print(car.route.get_percentage_from_start(car.strecke))
                return False
        #print("Target reach")
        return True


# start_time = time.time()
myRoute = Route(Route.castPointsToWangNotation([Point(0.0,0.0),Point(1000.0,1000.0)]), 2)
myRoute2 = Route(Route.castPointsToWangNotation([Point(0.0,1000.0),Point(1000.0,0.0)]), 2)
myRoute3 = Route(Route.castPointsToWangNotation([Point(0.0,50.0),Point(100.0,50.0)]), 2)

myCar = Car("test_1", 0.0, 50.0, -60.0, 120.0, 0.0, 0.0, 0.0, CarSize(20,0), myRoute.get_current_pos(), myRoute)
myCar2 = Car("test_2", 0.0, 50.0, -60.0, 120.0, 0.0, 0.0, 0.0, CarSize(30,0), myRoute2.get_current_pos(), myRoute2)
myCar3 = Car("test_3", 0.0, 50.0, -60.0, 120.0, 0.0, 0.0, 0.0, CarSize(30,0), myRoute3.get_current_pos(), myRoute3)


myCars=[]
myCars.append(myCar)
myCars.append(myCar2)
#myCars.append(myCar3)
myNode = Node(0, myCars,None)
myGraph = Graph(myNode)
myAlgo = Algo(myGraph)
myAlgo.do_algo()
# myscenario = scenario(None,0,myCars)
# myGraph = Graph(myscenario)
# bestscenarios = myGraph.calluclate_best_scenarios()
#
# end_time = time.time()
#
#
# scenario.printDebugscenarios(bestscenarios)
# print("run time (s) "+str(end_time-start_time))
