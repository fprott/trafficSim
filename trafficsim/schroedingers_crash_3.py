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
        self.prevent_crashs=[]

        # Setze Beschleunigung aller autos auf maximum
        myScenario = Scenario()
        myScenario.build_self_with_max_a(start_zeitpunkt)
        self.scenarios.append(myScenario)

    def do_the_schroedinger(self):
        # n_c =0
        #sollange es noch möglichkeiten gibt
        while len(self.scenarios)>0:
            scenario = self.scenarios.pop()
            if scenario.is_scenario_invalid() == False: #wenn das Scenario sinnvoll ist d.h. man nicht steht oder rückwertsfährt oder sowas
                # Fahre bis zu einem Unfall
                crash = scenario.get_first_crash()
                if crash == None:
                    print("no crash")
                #    SchroedingersCrash._printDebugScenario(scenario)
                    self.possible_solutions.append(scenario)
                else:
                    print("crash")

                    # if n_c > 0:
                    #     SchroedingersCrash._printDebugScenario(scenario)
                    #     sbsdb
                    # n_c += 1
                #    SchroedingersCrash._printDebugScenario(scenario)
                    #Suche die zwei (!) Autos die im Umfall verwickelt sind
                    car1, car2 = crash.car1, crash.car2
                    crash_zeitpunkt = crash.zeitpunkt

                    # wir prüfen ob das scenario schonmal da war (verhindert das wir in endlosschleifen geraten wenn das problem unlösbar ist !)
                    if self.scenario_already_handeled(scenario):
                        continue
                    self.prevent_crashs.append(scenario) #sonst kümmeren wir uns um den crash

                    # Lösche das jetzige Senario und mache zwei neue Senarien
                    clone1 = scenario.clone_self()
                    clone2 = scenario.clone_self()
                    scenario.delete_self()
                    #Passe das Scenario so an das der Unfall verhindert wird
                    if self.prevent_crash(clone1, crash_zeitpunkt, car1, car2) == True:
                        self.scenarios.append(clone1)
                    if self.prevent_crash(clone2, crash_zeitpunkt, car2, car1) == True:
                        self.scenarios.append(clone2)
            else:
                print("invalid")

    def scenario_already_handeled(self, scenario):
        for old_scenario in self.prevent_crashs:
            if scenario.is_equal(old_scenario):
                return True
        return False

    def _printDebugScenario(scenario): #
        for node in scenario.zeitpunkte:
            print("Timestep " + str(node.time))
            p = 0
            print("Current Cars:")
            for c in node.cars:
                print(c)
                # print(c.size.get_width())
                # p+=c.route.percent_of_route_still_to_travel()
                print("Percent to  travel :" + str(c.route.get_percentage_from_start(c.strecke)))
            # p=p/len(scenario.cars)
            # print("Percent still to travel "+str(p))
            print("Crash?: " + str(check_collision(node.cars)))
            print("-----")

    def prevent_crash(self, scenario, crash_zeitpunkt, car_to_brake, car_not_to_brake):
        # Zeit die wir bremsen müssen
        brake_time = Crash.get_brake_start(crash_zeitpunkt, car_to_brake, car_not_to_brake)
        #finde den Zeitpunkt an den wir zu bremsen beginnen müssen
    #    t_before_crash = crash_zeitpunkt.time - brake_time
        zeitpunkt = crash_zeitpunkt.parent
        while zeitpunkt.time>brake_time:
            zeitpunkt = zeitpunkt.parent
        #bau das ding neu auf
        return scenario.rebuild_self_with_brake(zeitpunkt, crash_zeitpunkt, car_to_brake)

class Scenario():
    def __init__(self):
        self.zeitpunkte = []
        self.dt = 0.05
        # self.cost = float('Inf')

    def get_costs(self):
        return self.zeitpunkte[-1].time # wenig Zeit gebraucht ist kleine Kosten :D

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

    def is_equal(self, otherScenario):
        if len(self.zeitpunkte) != len(otherScenario.zeitpunkte):
            return False

        while i< len(self.zeitpunkte):
            zp_self = self.zeitpunkte[i]
            zp_other = otherScenario.zeitpunkte[i]
            if zp_self.time != zp_other.time:
                return False
            if zp_self.parrent != zp_other.parrent:
                return False
            if zp_self.dt != zp_other.dt:
                return False

            if len(zp_self.cars) != len(zp_other.cars):
                return False
            j=0
            while j<len(zp_self.cars):
                car_self = zp_self.cars[j]
                car_other = zp_other.cars[j]
                if not car_self.is_equal(car_other):
                    return False

        return True

    def build_self_with_max_a(self, start_zeitpunkt):
        self.dt = start_zeitpunkt.dt
        self.cost = 0
        start_zeitpunkt.set_all_cars_to_max_a()
        self.zeitpunkte.append(start_zeitpunkt)
        zeitpunkt = start_zeitpunkt
        while zeitpunkt.target_reached()==False:
            zeitpunkt=zeitpunkt.make_next_zeitpunkt()
            zeitpunkt.set_all_cars_to_max_a()
            self.zeitpunkte.append(zeitpunkt)

    def rebuild_self_with_brake(self, start_brake_zeitpunkt, end_brake_zeitpunkt, car_to_brake):
        start_braking_time = start_brake_zeitpunkt.time
        end_braking_time = end_brake_zeitpunkt.time

      #  print(start_braking_time)
        # gehe alle Zeitpunkte rückwerts durch
        # wenn wir den Zeitpunkt finden wo wir anfangen müssen zu bremsen dann
        # schau ob der Zeitpunkt schon bremmst, wenn ja dann muss man früher anfangen zu bremsen
    #    print(start_braking_time)
        for zeitpunkt in reversed(self.zeitpunkte):
            if zeitpunkt.time < end_braking_time and zeitpunkt.time > start_braking_time: # wir müssten bremsen
                for car in zeitpunkt.cars:
                    if car.id == car_to_brake.id:  # ID muss eindeutig sein !
                        if car.a == car.a_min:
                            start_braking_time -= self.dt
     #   print(start_braking_time)
        times_to_break = math.ceil((end_braking_time - start_braking_time) / self.dt)

        # jetzt ist die start_braking_time und die times_to_break richtig
        if start_braking_time <0 :
            return False

        # löschen der liste für alle zeitpunkte nach dem start
        start_braking = False
        neue_zeitpunkte = []
        for zeitpunkt in self.zeitpunkte:
            if zeitpunkt.time == start_braking_time:
                start_braking = True
                start_brake_zeitpunkt = zeitpunkt
            if start_braking == True:
                zeitpunkt.delete_self() # wir löschen die weiteren Zeitpunkte, das ist eingeltich nicht notwendig aber dann muss das der garbage collector nicht machen d.h. es passiert sicher kein müll
            else:
                neue_zeitpunkte.append(zeitpunkt)

        self.zeitpunkte = neue_zeitpunkte

        # erweitert die Liste wieder zur vollständigkeit
        zeitpunkt = start_brake_zeitpunkt
        while zeitpunkt.target_reached()==False:
            zeitpunkt.set_all_cars_to_max_a()
            if times_to_break!=0: #wenn wir noch bremsen
                for car in zeitpunkt.cars:
                    if car.id == car_to_brake.id: #ID muss eindeutig sein !
                        car.a=car.a_min
                        times_to_break -= 1
            self.zeitpunkte.append(zeitpunkt)
            zeitpunkt = zeitpunkt.make_next_zeitpunkt()
        return True

    # Lösche Senarien aus der To-Do liste immer dann wenn:
    # a.) man zum Anfangszeitpunkt schon bremst
    # b.) ein Auto dauerhaft steht (v == 0, a == 0)
    # c.) ein Auto rückwärst fährt
    def is_scenario_invalid(self):
        if self.zeitpunkte[0].is_one_car_braking():
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
        # self.cost = 0

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
    def is_one_car_braking(self):
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


myRoute = Route(Route.castPointsToWangNotation([Point(0.0,0.0),Point(100.0,100.0)]), 2)
#myRoute2 = Route(Route.castPointsToWangNotation([Point(100.0,100.0),Point(0.0,0.0)]), 2)
myRoute2 = Route(Route.castPointsToWangNotation([Point(0.0,100.0),Point(100.0,0.0)]), 2)
myRoute3 = Route(Route.castPointsToWangNotation([Point(0.0,50.0),Point(100.0,50.0)]), 2)

myCar = Car("test_1", 0.0, 50.0, -60.0, 120.0, 0.0, 0.0, 0.0, CarSize(4,2), myRoute.get_current_pos(), myRoute)
myCar2 = Car("test_2", 0.0, 50.0, -60.0, 120.0, 0.0, 0.0, 0.0, CarSize(4,2), myRoute2.get_current_pos(), myRoute2)
myCar3 = Car("test_3", 0.0, 50.0, -60.0, 120.0, 0.0, 0.0, 0.0, CarSize(30,0), myRoute3.get_current_pos(), myRoute3)


myCars=[]
myCars.append(myCar)
myCars.append(myCar2)
#myCars.append(myCar3)

sc = SchroedingersCrash(Zeitpunkt(0, myCars, None, 0.05))
sc.do_the_schroedinger()
print(sc.possible_solutions)
#myAlgo.do_algo()
