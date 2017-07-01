# Weil jeder UnitTest kennt benutzen wir das
from route import *
import unittest

class RoutenTest(unittest.TestCase):

    # Beispiel für einen Test
    def testInit(self):
        myRoute = Route([Point(0.0,0.0),Point(100.0,200.0),Point(200.0,400.0),Point(300.0,800.0)], 2.0)
        self.assertIsNotNone(myRoute.points)
        self.assertIsNotNone(myRoute.width)
        self.assertIsNotNone(myRoute.routepoints)
        self.assertEqual(myRoute.point_iterator, 0)
        self.assertNotEqual(myRoute.routelength,0)

    def testIDoNotBeliveWang(self):
        y_max = 0
        myRoute = Route(Route.castPointsToWangNotation([Point(0.0, 0.0), Point(1000.0, 1000.0)]), 2)
        px_1 = myRoute.points[0][0]
        py_1 = myRoute.points[0][1]
        for p in myRoute.routepoints:
            px_2 = p[0]
            py_2 =p[1]
            self.assertLess(abs(px_2 - px_1),0.1,"Wangs Route macht zu kleine Schritte in X")
            self.assertLess(abs(py_2 - py_1), 0.1, "Wangs Route macht zu kleine Schritte in Y")
            px_1 = px_2
            py_1 = py_2

        myRoute2 = Route(Route.castPointsToWangNotation([Point(0.0, 1000.0), Point(1000.0, 0.0)]), 2)
        px_1 = myRoute2.points[0][0]
        py_1 = myRoute2.points[0][1]
        for p in myRoute2.routepoints:
            px_2 = p[0]
            py_2 = p[1]
            self.assertLess(abs(px_2 - px_1), 0.1, "Wangs Route macht zu kleine Schritte in X")
            self.assertLess(abs(py_2 - py_1), 0.1, "Wangs Route macht zu kleine Schritte in Y")
            px_1 = px_2
            py_1 = py_2
    #    myRoute2 = Route(Route.castPointsToWangNotation([Point(0.0, 100.0), Point(100.0, 0.0)]), 2)

    # Hier müssen mehr Tests gemacht werden.

    # ANFORDERUNGEN ROUTE / WANG:
    #     Jede Punkt auf der Route darf maximal 10 cm abstand vom nächsten haben <- 5 verschiedene Tests die das beweisen [100, 200, 300]
    #     percent_of_route_still_to_travel MUSS am Ende 0 zurücklieferen
    #     auf der Route zu lange zu fahren d.h. zu weit zu fahren darf KEINEN Fehler schmeisen d.h. das ist geplant
    #     Alle Ausgaben müssen die Punkt klasse verwenden (eingaben am besten auch)
    #     Es darf nicht sein das die Route die Straße verällst d.h. ein überschießen der Straße ist nicht vorgesehen

if __name__ == "__main__":
    unittest.main()




