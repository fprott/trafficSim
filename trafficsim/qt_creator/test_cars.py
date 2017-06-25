import unittest

import  sys
sys.path.append("..")
import trafficsim.car
import trafficsim.route




class KollisionTest(unittest.TestCase):


    def test_size_0(self):
        myRoute = Route([Point(0.0,10.0),Point(100.0,200.0),Point(200.0,400.0),Point(300.0,800.0)], 20.0)
        myRout2 = Route([Point(10.0,0.0), Point(300,800)],20)
        myRout3 = Route([Point(100.0, 0.0), Point(300, 800)], 20)


        Car1 = Car("test_1", Route1, 60.0, -40.0, 300.0, 0.0, 0.0, 0.0, CarSize(10, 12))
        Car2 = Car("test_2", Route2, 40.0, -40.0, 150.0, 0.0, 0.0, 0.0, CarSize(5, 10))
        Car3 = Car("test_2", Route3, 40.0, -40.0, 150.0, 0.0, 0.0, 0.0, CarSize(30, 20))
        myCars=[Car1,Car2]
        Collsion_check = check_collision(myCars)
        self.assertEqual(Collision_check,False)
