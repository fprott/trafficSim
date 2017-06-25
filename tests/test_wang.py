import sys
import math
sys.path.append("..")
from route import *
import unittest
from parameter import *



class RoutenTest(unittest.TestCase):

    # Beispiel für einen Test
    def testInit(self):
        Route1 = Route([(500, 1), (1000, 1)], width=1)
        print(Route1.get_new_pos(10))
        #print(Route1.get_next_dis())
        #print(Route1.point_iterator)
        print(Route1.traveled_distance_on_route())
        print(Route1.percent_of_route_still_to_travel())
        print(Strassen_Nets[1][1])
        print(Route1.get_angle_from_start(1000))
        #print(Route1.get_new_pos(-500))
        #print(Route1.get_new_pos_from_start(50))
        #print(Route1.get_current_pos())
        #print(Route1.traveled_distance_on_route())
        #print(Route1.percent_of_route_still_to_travel())
        #print(Route1.get_percentage_from_start(100))
        #print(Route1.get_percentage_from_start(600))




#****************Beispiel*************************

if __name__ == "__main__":
    unittest.main()


