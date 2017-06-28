from car import *
from route import *

# Stecke = zur Vermeidung der Kollision
#a = Transition die zur kollision geführt hat
#dt = Zeit zwischen szenarien
def break_car (Strecke,car,a,dt):
    distance=0
    i = 0
    while(distance < Strecke):
        i=i+1
        distance = (a-car.a_min)*(i*dt)*(i*dt)*0.5
              #  if distance > Strecke:
            #     while distance >= Strecke:
             #           distance = (a-car.a_min + car.)*(i*dt)*(i*dt)*0.5


    return [i, car.a_min]     # du musst dann i mal zurückgehn und jeweils mit a_min als beschleunigung verwenden



#myRoute = Route(Route.castPointsToWangNotation([Point(0.0,1000.0),Point(1000.0,0.0)]), 2)
#myCar = Car("test_1", 0.0, 55.0, -60.0, 300.0, 10.0, 0.0, 0.0, CarSize(30,10), myRoute.get_current_pos(), myRoute)


#val = break_car(40,myCar,45,0.1)
#print(val)






