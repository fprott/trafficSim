



from trafficsim.route import *
from trafficsim.car import *

import unittest




def bulletime(cars, default_dt=1): #
    """
    Errechnet die dt und da
   cars = liste mit allen autos, default_dt= dt wenn autos voneinander weit entfernt sind
    """
    safe_zone=1;
    for i in range(len(cars)):
        for j in range(i + 1, len(cars)):
            dist = math.hypot(cars[i].pos.x - cars[j].pos.x, cars[i].pos.y - cars[j].pos.y);    #autos werden vereinfacht als kreise modelliert'
            if dist <= (cars[i].v+cars[j].v)*default_dt:
                safe_zone=0;
                break
        if safe_zone == 0:
            break
    #'sobald ein Paar Autos welches nicht in der safe_zone ist gefunden wurde, werden die for schleifen abgebrochen...bei safe_Zone' \
    #'bleibt die Abtastzeit gleich dt_default in der danger_zone verkleinern wir die abtastzeit um das 10-fache...wert ist wilkürlich gewählt worden'
    if  safe_zone == 1:
        dt = default_dt;
    else:
        dt = 0.2

                  #da = bleibt gleich...wir können aber wegen dem neuen dt den kurs der Autos öfters korrigieren

    return dt

class KollisionTest(unittest.TestCase):


    def test_size_0(self):

