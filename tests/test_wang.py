import sys
import math
sys.path.append("..")
from trafficsim.route import *
import unittest



class RoutenTest(unittest.TestCase):

    # Beispiel für einen Test
    def testInit(self):
        Route1 = Route([(500, 1), (1000, 1)], width=1)
        print(Route1.get_new_pos(100))
        print(Route1.get_current_pos())
        print(Route1.traveled_distance_on_route())
        print(Route1.percent_of_route_still_to_travel())




#****************Beispiel*************************

if __name__ == "__main__":
    unittest.main()


