from mathe import Point, Line, calculate_pos
from car import *
from route import *
import copy

#Kochrezept
# SCHRÖDINGERS_CRASH:
# 1.) Setze Beschleunigung aller autos auf maximum
# 2.) Fahre bis zu einem Unfall
# 3.) Suche die zwei (!) Autos die im Umfall verwickelt sind
# Lösche das jetzige Senario und mache zwei neue Senarien nach folgenden Muster
# Für Auto1 und Auto2 mache jeweils:
# 	4.) Erechne die Strecke die den Unfall verhindert
# 	5.) Bremse mit a_min möglichst Nahe vor dem Unfall d.h. in den letzen X Zeitschriten vor dem Unfall bremse mit maximaler Geschwindigkeit (wenn man vorher bremmst macht man ggf. andere Unfälle rein, wenn man hier neue rein macht ist das mathematisch weniger schlim)
# 6.) Gehe immer alle Senarien durch bis alle Senarien entweder das Ziel erreichen oder
# 7.) Lösche Senarien aus der To-Do liste immer dann wenn:
# a.) ein Auto dauerhaft steht (v == 0, a == 0)
# b.) man zum Anfangszeitpunkt schon bremst
# c.) ein Auto rückwärst fährt
# 8.) Nehme das beste Senario was das Ziel erreicht (beste heißt hier das wir eine Gütefunktion brauchen. z.B. maximirung von Beschleunigungen oder minimrung der gesamtzeit etc.

class SchroedingersCrash():
    def __init__(self, start_zeitpunkt):
        self.scenarios = []
        self.possible_solutions = []

        # Setze Beschleunigung aller autos auf maximum
        myScenario = Scenario()
        myScenario.build_self_with_max_a(start_zeitpunkt)
        self.scenarios.append(myScenario)

    def do_the_schroedinger(self):
        #sollange es noch möglichkeiten gibt
        while len(self.scenarios)>0:
            scenario = self.scenarios.pop()
            if scenario.is_scenario_invalid() == False: #wenn das Scenario sinnvoll ist d.h. man nicht steht oder rückwertsfährt oder sowas
                # Fahre bis zu einem Unfall
                crash = scenario.get_first_crash()
                if crash == None:
                    self.possible_solutions.append(scenario)
                else:
                    #Suche die zwei (!) Autos die im Umfall verwickelt sind
                    car1, car2 = crash.car1, crash.car2
                    crash_zeitpunkt = crash.zeitpunkt
                    # Lösche das jetzige Senario und mache zwei neue Senarien
                    clone1 = scenario.clone_self()
                    clone2 = scenario.clone_self()
                    scenario.delete_self()
                    #Passe das Scenario so an das der Unfall verhindert wird
                    self.prevent_crash(clone1, crash_zeitpunkt, car1, car2)
                    self.prevent_crash(clone1, crash_zeitpunkt, car2, car1)
                    self.scenarios.append(clone1)
                    self.scenarios.append(clone2)

    def prevent_crash(self, scenario, crash_zeitpunkt, car_to_break, car_not_to_break):
        # Zeit die wir bremsen müssen
        break_time = Crash.get_brake_start(crash_zeitpunkt, car_to_break, car_not_to_break)
        #finde den Zeitpunkt an den wir zu bremsen beginnen müssen
    #    t_before_crash = crash_zeitpunkt.time - break_time
        zeitpunkt = crash_zeitpunkt.parent
        while zeitpunkt.time>break_time:
            zeitpunkt = zeitpunkt.parent
        #bau das ding neu auf
        scenario.rebuild_self_with_break(zeitpunkt, crash_zeitpunkt, car_to_break)

class Scenario():
    def __init__(self):
        self.zeitpunkte = []
        self.dt = 0.1

    def clone_self(self):
        #clone = copy.deepcopy(self) # geht net (!) weil Bug in aktueller Python Version (?)
        clone = Scenario()
        cloned_zeitpunkte = []
        for zeitpunkt in self.zeitpunkte:
            clone_zeitpunkt = zeitpunkt.clone_self()
            cloned_zeitpunkte.append(clone_zeitpunkt)
        clone.zeitpunkte = cloned_zeitpunkte
        return clone

    def delete_self(self):
        for zeitpunkt in self.zeitpunkte:
            zeitpunkt.delete_self()
        del self

    def build_self_with_max_a(self, start_zeitpunkt):
        start_zeitpunkt.set_all_cars_to_max_a()
        self.zeitpunkte.append(start_zeitpunkt)
        zeitpunkt = start_zeitpunkt
        while zeitpunkt.target_reached()==False:
            zeitpunkt=zeitpunkt.make_next_zeitpunkt()
            zeitpunkt.set_all_cars_to_max_a()
            self.zeitpunkte.append(zeitpunkt)

    def rebuild_self_with_break(self, start_break_zeitpunkt, end_break_zeitpunkt, car_to_break):
        start_breaking_time = start_break_zeitpunkt.time
        end_breaking_time = end_break_zeitpunkt.time
        start_breaking = False
        for zeitpunkt in self.zeitpunkte:
            if zeitpunkt.time == start_breaking_time:
                breaking = True
            if start_breaking == True:
                zeitpunkt.delete_self # wir löschen die weiteren Zeitpunkte
                self.zeitpunkte.remove(zeitpunkt)

        zeitpunkt = start_break_zeitpunkt
        while zeitpunkt.target_reached()==False:
            zeitpunkt.set_all_cars_to_max_a()
            if zeitpunkt.time < end_breaking_time: #wenn wir noch bremsen
                for car in zeitpunkt.cars:
                    if car == car_to_break: #kann man das vergleichen BUG???
                        car.a=car.a_min
            self.zeitpunkte.append(zeitpunkt)
            zeitpunkt = zeitpunkt.make_next_zeitpunkt()

    # Lösche Senarien aus der To-Do liste immer dann wenn:
    # a.) man zum Anfangszeitpunkt schon bremst
    # b.) ein Auto dauerhaft steht (v == 0, a == 0)
    # c.) ein Auto rückwärst fährt
    def is_scenario_invalid(self):
        if self.zeitpunkte[0].is_one_car_breaking():
            return True
        for zeitpunkt in self.zeitpunkte:
            if zeitpunkt.is_one_car_permanently_standing():
                return True
            if zeitpunkt.is_car_rolling_back():
                return True
        return False

    def get_first_crash(self):
        for zeitpunkt in self.zeitpunkte:
            if check_collision(zeitpunkt.cars) == True:
                car1, car2 = get_first_two_cars_that_collide(zeitpunkt.cars)
                return Crash(zeitpunkt, car1, car2)
        return None

# nicht wirklich python like aber hilft mir denken
class Crash():
    def __init__(self, zeitpunkt, car1, car2):
        self.zeitpunkt = zeitpunkt
        self.car1 = car1
        self.car2 = car2

    def get_crash_avoidance_distance(car_to_brake, car_not_to_brake):
        return car_not_to_brake.size.width+car_not_to_brake.size.length # TODO besserer Abstand

    def get_brake_start(crash_zeitpunkt, car_to_brake, car_not_to_brake):
        safe_distance = Crash.get_crash_avoidance_distance(car_to_brake, car_not_to_brake)
        t_brake = math.sqrt(-2 * safe_distance / car_to_brake.a_min)
        return crash_zeitpunkt.time - t_brake

class Zeitpunkt():
    def __init__(self, t, cars, parent, dt):
        self.cars = cars
        self.time = t
        self.parent = parent
        self.dt = dt

    def set_all_cars_to_max_a(self):
        for car in self.cars:
            car.a=car.a_max

    def make_next_zeitpunkt(self): # make sure that the a are set
        new_cars = []
        for car in self.cars:
            new_cars.append(car.get_next_car(self.dt, car.a))
        new_node = Zeitpunkt(self.time+self.dt, new_cars, self, self.dt)
        return new_node

    # Eigentlich könnte man die folgenden Funktionen zusammenfassen aber das sind Optimirungen die nicht so dringend sind wie andere weil es gilt O(X)+O(X) = 2*O(X) = O(X)

    def target_reached(self):
        for car in self.cars:
            if car.route.get_percentage_from_start(car.strecke) !=0:
                return False
        return True

    # a.) ein Auto dauerhaft steht (v == 0, a == 0)
    def is_one_car_permanently_standing(self):
        for car in self.cars:
            if car.v == car.a == 0:
                return True
        return False

    # b.) man zum Anfangszeitpunkt schon bremst
    def is_one_car_breaking(self):
        for car in self.cars:
            if car.a<0:
                return True
        return False

    # c.) ein Auto rückwärst fährt
    def is_car_rolling_back(self):
        for car in self.cars:
            if car.v <0:
                return True
        return False

    def clone_self(self):
        cloned_cars = []
        for car in self.cars:
            cloned_pos = Point(car.pos.x, car.pos.y)
            cloned_car = Car(car.id, car.strecke, car.a_max, car.a_min, car.v_max, car.v_min, car.v, car.a, car.size, cloned_pos, car.route)
            cloned_cars.append(cloned_car)
        return Zeitpunkt(self.time, cloned_cars, self.parent, self.dt)

    def delete_self(self):
        for car in self.cars:
            del car
        del self

    def __repr__(self):
        return "Zeitpunkt[%2.2f]" % self.time

class NoPathAvailableError(Exception):
    def __init__(self, message):
        self.message = message


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

sc = SchroedingersCrash(Zeitpunkt(0, myCars, None, 0.1))
sc.do_the_schroedinger()
#myAlgo.do_algo()
