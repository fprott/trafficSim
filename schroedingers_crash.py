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

class algo():
    def __init__(self, root_senario):
        self.root_senario = root_senario
        self.senarios = [root_senario]
        self.possible_solutions = []

    def do_algo(self):
        while len(self.senarios)>0:
            senario = self.senarios.pop()
            finished, senario_new_1, senario_new_2 = senario.drive_until_crash()
            if not finished:
                if senario_new_1 != None:
                    self.senarios.append(senario_new_1)
                if senario_new_2 != None:
                    self.senarios.append(senario_new_2)
            if finished:
                self.possible_solutions.append(senario)

        if len(self.possible_solutions)==0:
            raise NoPathAvailableError("Algo findet keinen möglichen Pfad. Bitte Eingabe überprüfen!")
        else:
            for good_senario in self.possible_solutions:
                return good_senario

class Senario():
    def __init__(self, cars, root_senario, t, dt_steps_done):
        if root_senario == None:
            self.root = self
        else:
            self.root = copy.deepcopy(root_senario)
        self.cars = cars
        self.dt = t
        self.dt_steps_done = dt_steps_done

    def drive_until_crash(self):
        while not self.target_reached():
            if check_collision(self.cars) == True:
                # print("Kollision")
                #make new senarios, die beiden autos die den Unfall gebaut haben werden zurückgeschoben d.h. beschleunigen weniger als vorher notwendig
                car1, car2 = get_first_two_cars_that_collide(self.cars)
                #für das erste auto
                crash_lenght = car2.size.get_length() + car2.size.get_width() #TODO schlauer machen, super blöd
                # s = 1/2*a*t^2+t*v0+s0
                ap=crash_lenght*2*self.dt*self.dt #TODO formel prüfen ! ich bin zu übermüdet um klar zu denken

                senario1 = copy.deepcopy(self.root)
                car1_befor = None
                for car_old in senario1.cars:
                    if car_old == car1:
                        car1_befor=car_old
                car1_befor.ap_to_miss+=ap
                car1_befor.steps_until_crash = self.dt_steps_done

                senario2 = copy.deepcopy(self.root)
                car2_befor = None
                for car_old in senario2.cars:
                    if car_old == car2:
                        car2_befor=car_old
                car2_befor.ap_to_miss+=ap
                car2_befor.steps_until_crash = self.dt_steps_done

                return False, senario1, senario2
            self.drive_dt()

        return True, None, None

    def drive_dt(self):
        i = 0
        while len(self.cars)>i:
            car = self.cars[i]
            a_penalty = 0
            if car.steps_until_crash != None:
                a_penalty = car.ap_to_miss/car.steps_until_crash
                new_a = car.a_max - a_penalty
            else:
                new_a = car.a_max
            car = car.get_next_car_schroedinger(self.dt, new_a)
            car.ap_to_miss = car.ap_to_miss - a_penalty
            car.ap_accumulated_since_last_checkpoint+=new_a
            self.cars[i] = car
            i+=1

    def target_reached(self):
    #    print("----")
        for car in self.cars:
    #        print(car.route.percent_of_route_still_to_travel())
            if car.route.get_percentage_from_start(car.strecke) !=0:
            #    print(car.route.get_percentage_from_start(car.strecke))
                return False
        #print("Target reach")
        return True

class CarSchroedinger(Car):
    def __init__(self, id, strecke, a_max, a_min, v_max, v_min, v, a, car_size, pos, route):
        super(CarSchroedinger, self).__init__(id, strecke, a_max, a_min, v_max, v_min, v, a, car_size, pos, route)
        self.ap_accumulated_since_last_checkpoint = 0 # Ein ap ist ein Beschleunigungspunkt d.h. eine Beschleunigung die bereits gemacht wurde
        self.ap_to_miss = 0 # Wie viel beschleunigungen man verpassen muss damit das ganze funktioniert. Wann man die verpasst ist sehr kritisch und noch ein ungelöstes problem
        self.steps_until_crash = None
        self.cost = 0

    def get_next_car_schroedinger(self, dt, da):
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
        return CarSchroedinger(self.id, new_strecke,self.a_max, self.a_min, self.v_max,self.v_min, new_v, new_a, self.size, new_pos, self.route) #make the next car

start_time = time.time()
myRoute = Route(Route.castPointsToWangNotation([Point(0.0, 0.0), Point(100.0, 100.0)]), 2)
myRoute2 = Route(Route.castPointsToWangNotation([Point(0.0, 100.0), Point(100.0, 0.0)]), 2)
myRoute3 = Route(Route.castPointsToWangNotation([Point(0.0, 50.0), Point(100.0, 50.0)]), 2)

myCar = CarSchroedinger("test_1", 0.0, 50.0, -60.0, 300.0, 10.0, 0.0, 0.0, CarSize(20, 0), myRoute.get_current_pos(),
            myRoute)
myCar2 = CarSchroedinger("test_2", 0.0, 50.0, -60.0, 300.0, 10.0, 0.0, 0.0, CarSize(30, 0), myRoute2.get_current_pos(),
             myRoute2)
myCar3 = CarSchroedinger("test_3", 0.0, 50.0, -60.0, 300.0, 10.0, 0.0, 0.0, CarSize(30, 0), myRoute3.get_current_pos(),
             myRoute3)

myCars = []
myCars.append(myCar)
myCars.append(myCar2)
#myCars.append(myCar3)
mySenario = Senario(myCars, None, 0.1, 0)
myAlgo = algo(mySenario)
myAlgo.do_algo()

end_time = time.time()

#Senario.printDebugSenarios(bestSenarios)
print("run time (s) " + str(end_time - start_time))
