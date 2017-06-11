from mathe import Point, Line, calculate_pos
import itertools
import functools
import math
from car import Car, CarSize
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
            current_node = heappop(self.open_list)
            if (current_node.target_reached() == True): # wir erwarten das wir eine Lösung finden. Wenn wir eine finden dann ist es automatisch die beste Lösung
                return current_node

            self.closed_list.add(current_node)
            self._expand_graph(current_node)
        raise NoPathAvailableError("A Stern findet keinen möglichen Pfad. Bitte Eingabe überprüfen!")

    def _expand_graph(self, node):
        """
        Erweiteret den Graphen um alle möglichen Kinder des Nodes
        :param node:
        :return:
        """

        time_step =  bulletime(node.cars)
        new_nodes = node.callculate_next_senarios(time_step)
        for node in new_nodes:
            heappush(self.open_list, node) # Achtung, noch gibt es keine Zusammenführung d.h. keine möglichkeit das ein node zwei Eltern hat

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
            cost = float('inf')
            return cost
        for car in self.cars:
            cost+=1/car.a # sehr simpler Algo der angepasst werden sollte
        return cost

    def get_heuristic_cost(self): # TODO mehr variität !
        cost=0
        for car in self.cars:
            cost +=car.route.percent_of_route_still_to_travel() # sehr simpler Algo der angepasst werden sollte

        return cost

    def __lt__(self, other): # Iterator !
        return (self.get_node_cost+self.get_heuristic_cost)<(other.get_node_cost+other.get_heuristic_cost)
        #  return self.cost < other.cost

    def target_reached(self):
        for car in self.cars:
            if car.route.percent_of_route_still_to_travel !=0:
                return False
        return True

    def callculate_next_senarios(self, time_step):
        new_time = self.start_time + time_step

        all_possible_car_tuples = []
        for a_car in self.cars:
            possible_new_cars = ()
            for a in a_car.get_possible_a_range(5): #TODO N wählen
                possible_new_cars = possible_new_cars + (a_car.get_next_car_marker(time_step,a),) # ein tupel enhällt alle möglichen nächsten Autos
                all_possible_car_tuples.append(possible_new_cars) # List von tupeln

    #    print(tuple(all_possible_car_ghosts_tuples))
        all_car_possiblites = list(itertools.product(*all_possible_car_tuples)) # hexerei, bitte schaut euch die doku an wenn das net geht

        all_possible_steps = []
        for possiblity in all_car_possiblites:
            all_possible_steps.append(Senario(self, new_time, possiblity))
        return all_possible_steps

class CarMarker(Car):
    """
    Die Klasse CarMarker besteht aus einem Auto zu einer bestimmten Position. Es findet keine Bewegung dies Autos statt
    """
    def get_next_car_marker(self, dt, da):
        new_v = self.v+self.a*dt # wir erechnen die neue geschwindigkeit
    #    new_pos = calculate_pos(self.pos, dt, self.v) # wir erechnen die neue Position
        new_a = self.get_a_by_da(da)
        new_route = self.route
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
            dist = math.hypot(cars[i].x - cars[j].x, cars[i].y - cars[j].y);    #autos werden vereinfacht als kreise modelliert'
            if dist <= 1.4*(cars[i].length+cars[j].length):
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

myStrecke = Strecke([Point(0.0,0.0),Point(1.0,2.0),Point(2.0,4.0),Point(3.0,8.0)])
myRoute = Route(myStrecke,0.1)
myCar = CarMarker("test_1", myRoute, 55, 20, 120, 20, 0, 0, (50,20))
myCars=[]
myCars.append(myCar)
mySenario = Senario(None,0,myCars)
myGraph = Graph(mySenario)
myGraph.calluclate_best_senarios()
#
# class Shedule():
#     # Achtung noch kein echter A*, nur ein test
#     def __init__(self, cars):
#         self.shedule_steps = []
#         first_step = SheduleStep(None, 0, cars) # TODO aus cars car_ghost machen !
#         self.shedule_steps.append(first_step)
#
#     def make_shedule_step(self):
#         current_step = self.shedule_steps[-1]
#         dt = 1
#         da = 1
#         all_possible_next_steps=current_step.callculate_next_steps(dt,da)
#      #   for step in all_possible_next_steps:
#      #       print("STEP")
#      #       for car in step.car_ghosts:
#      #           print(car)
#
#         best_next_step=all_possible_next_steps[0]
#         for step in all_possible_next_steps:
#             if(step.quality_value>best_next_step.quality_value):
#                 best_next_step=step
#
#     #    print("we choosed")
#     #    for car in best_next_step.car_ghosts:
#      #       print(car)
#     #    print(best_next_step.quality_value)
#         if(best_next_step.start_time>10):
#         #    print(self.shedule_steps)
#             return self.shedule_steps
#         if(best_next_step==None): # wenn kein weiter schrit mehr möglich/notwendig ist
#             return self.shedule_steps
# #        if(best_next_step.quality_value()==None): #wenn Unfall oder unmöglich
# #            current_step.quality_value=None
# #            return # TODO richtiger a* machen
#         self.shedule_steps.append(best_next_step)
#         self.make_shedule_step()
#
# class SheduleStep():
#     def __init__(self, parent, start_time, car_ghosts):
#         self.parent = parent
#         self.start_time = start_time
#         self.car_ghosts = car_ghosts
#         self.quality_value = self.callculate_quality_value()
#
#     def callculate_quality_value(self): #TODO: anders maß einbringen und AUSLAGERN !
#         quality = 0
#         for car in self.car_ghosts:
#             quality += car.a
#         return quality
#
#     def callculate_next_steps(self, dt, da):
#         new_time = self.start_time + dt
#
#         all_possible_car_ghosts_tuples = []
#         for ghost in self.car_ghosts:
#             possible_new_ghosts = ()
#             for a in ghost.get_possible_a_range(dt,da):
#                 possible_new_ghosts = possible_new_ghosts + (ghost.get_next_ghost(dt,a),) # ein tupel enhällt alle möglichen nächsten ghosts
#             all_possible_car_ghosts_tuples.append(possible_new_ghosts) # List von tupeln
#
#     #    print(tuple(all_possible_car_ghosts_tuples))
#         all_car_ghost_possiblites = list(itertools.product(*all_possible_car_ghosts_tuples)) # hexerei, bitte schaut euch die doku an wenn das net geht
#
#         all_possible_steps = []
#         for possiblity in all_car_ghost_possiblites:
#             all_possible_steps.append(SheduleStep(self, new_time, possiblity))
#         return all_possible_steps
#
# def bulletime(cars,default_dt): #
#     """
#     Errechnet die dt und da
#    cars = liste mit allen autos, default_dt= dt wenn autos voneinander weit entfernt sind
#     """
#     safe_zone=1;
#     for i in range(len(cars)):
#         for j in range(i + 1, len(cars)):
#             dist = math.hypot(cars[i].x - cars[j].x, cars[i].y - cars[j].y);    'autos werden vereinfacht als kreise modelliert'
#             if dist <= 1.4*(cars[i].length+cars[j].length):
#                 safe_zone=0;
#                 break
#         if safe_zone == 0:
#             break
#     #'sobald ein Paar Autos welches nicht in der safe_zone ist gefunden wurde, werden die for schleifen abgebrochen...bei safe_Zone' \
#     #'bleibt die Abtastzeit gleich dt_default in der danger_zone verkleinern wir die abtastzeit um das 10-fache...wert ist wilkürlich gewählt worden'
#     if  safe_zone == 1:
#         dt=default_dt;
#     else:
#         dt = default_dt / 10;          #da = bleibt gleich...wir können aber wegen dem neuen dt den kurs der Autos öfters korrigieren
#
#
#
#
#
#     return dt
#
#
# class CarGhost():
#     """
#     Ein CarGhost ist ein Auto zu einem diskreten Zeitpunkt.
#     """
#     def __init__(self, id, v_max, max_a, v=0, a=0, pos=(0,0)):
#         self.id = id # das dient dazu das wir die auseinanderhalten können und zum debugen
#         self.v_max=v_max #v_max : maximale geschwindigkeit
#         self.max_a=max_a #max_a : maximale beschleunigung
#         self.v=v
#         self.a=a
#         self.pos=pos
#
#     def _set_v(self, new_v):
#         if(new_v<=self.v_max):
#             self.v=new_v
#         else:
#             self.v=self.v_max
#
#     def _set_a(self, new_a):
#         if(new_a<=self.max_a):
#             self.a=new_a
#         else:
#             self.a=self.max_a
#         pass
#
#     def _change_a_by_da(self, da):
#         if (self.a+da <= self.max_a): # wenn die neue beschleunigung kleiner als max beschleunigung
#             if(self.a+da >= -self.max_a): # und wenn die (möglicherweise negative) beschleunigung größer als min beschleunigung
#                 self.a=self.a+da;
#             else:
#                 self.a = -self.max_a
#         else:
#             self.a = self.max_a
#
#
#     def get_change_a_by_da(self, da):
#         if (self.a+da <= self.max_a): # wenn die neue beschleunigung kleiner als max beschleunigung
#             if(self.a+da >= -self.max_a): # und wenn die (möglicherweise negative) beschleunigung größer als min beschleunigung
#                 return self.a+da;
#             else:
#                 return -self.max_a
#         else:
#             return self.max_a
#
#     def get_possible_a_range(self, dt, da):
#         """
#         Diese Funktion gibt eine Liste aller möglichen relativenen Beschleunigungen zurück. t bestimmt wie viele a möglichkeiten es gibt
#         0.0 sollte immer vorhanden sein. Wenn die Zeit "t" ausreicht dann halt auch +/-da, +/-2*da usw.
#         :param self:
#         :param dt: delta zeit
#         :param da: delta beschleunigung
#         :return: Liste aller Beschleunigungen
#         """
#         # FIXME : Levi, ka was die Phisik macht. Bitte denk dir was schlaues aus :D
#         a_range = [x / 10.0 for x in range(-50, 50, 10)]
#         return a_range
#
#     def get_next_ghost(self, dt, da):
#         new_v = self.v+self.a*dt # wir erechnen die neue geschwindigkeit
#         new_pos = calculate_pos(self.pos, dt, self.v) # wir erechnen die neue Position
#         new_a = self.get_change_a_by_da(da)
#     #    return (str(self.id) +" "+ str(new_a))
#         return CarGhost(self.id, self.v_max,self.max_a, new_v, new_a, new_pos) #make the next ghost
#
#     def __str__(self): # TODO mehr Werte
#         return (str(self.id) +" "+ str(self.a))
#
#
# "dick"
#
#
# "s ist die position entlang des Pfades, length dimension des Autos, nr_intervals dia Anzahl der Möglichen Beschleunigungen/Eingangsentscheidungen"
#
# class Cars:
#     def __init__(self, id, a_min, a_max,s,v,a,x,y,length,nr_intervals):
#         self.id=id;
#         self.a_min = a_min;
#         self.a_max = a_max;
#         self.x=x;
#         self.y=y;
#         self.s=s;
#         self.v=v;
#         self.a=a
#         self.length=length;
#         self.nr_intervals=nr_intervals;
#
#
#     def _set_v(self, new_v):
#         if (new_v <= self.v_max):
#             self.v = new_v
#         else:
#             self.v = self.v_max
#
#     def _set_a(self, new_a):
#         if (new_a <= self.max_a):
#             self.a = new_a
#         else:
#             self.a = self.max_a
#         pass
#
#     "generiert nr_intervals äquidistante beschleunigungswerte und speichert sie in die liste a_values"
#
#     def get_possible_a_range(self):
#         da = (self.a_max-self.a_min)/(self.nr_intervals-1)
#         a_values= list();
#         for i in range(0, self.nr_intervals):
#             a_values.append(self.a_min+ da*i)
#         return a_values
#
#     "new_a ist ein Wert aus der Liste a_values"
#
#     def get_next_car(self, dt, new_a):
#         new_v = self.v + new_a * dt  # wir erechnen die neue geschwindigkeit
#         new_pos = self.s + self.v * dt +0.5*new_a*dt*dt;  # wir erechnen die neue Position
#         #new_x="";
#         #nex_y="";   to DO
#         return Cars(self.id, self.a_min, self.a_max,new_pos, new_v, new_a, new_x, new,y, self.length, self.nr_intervals)  # make the next ghost
#
#     def __str__(self):  # TODO mehr Werte
#         return (str(self.id) + " " + str(self.a))
#
#
#
# #Car1 = CarGhost("1",120,20,0,0,(0,0))
# #Car2 = CarGhost("2",120,30,0,0,(0,0))
# #Car3 = CarGhost("3",150,10,0,0,(0,0))
# #Car4 = CarGhost("4",150,55,0,0,(0,0))
# #shedule = Shedule([Car1,Car2,Car3,Car4])
# #shedule.make_shedule_step()
#
# #for step in shedule.shedule_steps:
# #    print("Step time : "+str(step.start_time))
# #    for car in step.car_ghosts:
# #       print(car)
#
#
#
#
