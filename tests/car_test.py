import unittest
from trafficsim.route import *
from trafficsim.car import *

import unittest








class KollisionTest(unittest.TestCase):


    def test_size_0(self):
        Route1 = Route([Point(0.0,10.0),Point(100.0,200.0),Point(200.0,400.0),Point(300.0,800.0)], 20.0)
        Route2 = Route([Point(10.0,0.0), Point(300,800)],20)
        Route3 = Route([Point(100.0, 0.0), Point(300, 800)], 20)


        Car1 = Car("test_1", Route1, 60.0, -40.0, 300.0, 0.0, 0.0, 0.0, CarSize(10, 12))
        Car2 = Car("test_2", Route2, 40.0, -40.0, 150.0, 0.0, 0.0, 0.0, CarSize(5, 10))
        Car3 = Car("test_2", Route3, 40.0, -40.0, 150.0, 0.0, 0.0, 0.0, CarSize(30, 20))
        myCars=[Car1,Car2,Car3]
        Collision_check = check_collision(myCars)
        self.assertEqual(Collision_check,False)

        Car1 = Car("test_1", Route1, 60.0, -40.0, 300.0, 0.0, 0.0, 0.0, CarSize(10, 12))
        Car2 = Car("test_2", Route2, 40.0, -40.0, 150.0, 0.0, 0.0, 0.0, CarSize(5, 22))
        Car3 = Car("test_2", Route3, 40.0, -40.0, 150.0, 0.0, 0.0, 0.0, CarSize(30, 20))
        myCars = [Car1, Car2, Car3]
        Collision_check = check_collision(myCars)
        self.assertEqual(Collision_check,True)


    def test_Cars(self):
        Route1 = Route([Point(0.0, 10.0), Point(100.0, 200.0), Point(200.0, 400.0), Point(300.0, 800.0)], 20.0)
        Car_1 = Car("test", Route1, 60.0, -40.0, 300.0, 0.0, 0.0, 1.0, CarSize(10, 12))
        self.assertEqual(Car_1.a_max,60)
        self.assertEqual(Car_1.a_min, -40)
        self.assertEqual(Car_1.v_max, 300)
        self.assertEqual(Car_1.v_min,0)
        self.assertEqual(Car_1.v,0)
        self.assertEqual(Car_1.a,1)


        Car_2 = Car("test2", Route1, -10, 40.0, 300.0, -10, 0.0, 1.0, CarSize(-10, -12))
        len=Car_2.size.get_length()
        self.assertEqual(Car_2.size.get_length(),12)
        self.assertEqual(Car_2.size.get_width(),10)





















if __name__ == "__main__":
    unittest.main()

