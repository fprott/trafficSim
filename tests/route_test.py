# Weil jeder UnitTest kennt benutzen wir das
from trafficsim.route import*
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

    # Hier müssen mehr Tests gemacht werden.

    # ANFORDERUNGEN ROUTE / WANG:
    #     Jede Punkt auf der Route darf maximal 10 cm abstand vom nächsten haben
    #     percent_of_route_still_to_travel MUSS am Ende 0 zurücklieferen
    #     auf der Route zu lange zu fahren d.h. zu weit zu fahren darf KEINEN Fehler schmeisen d.h. das ist geplant
    #     Alle Ausgaben müssen die Punkt klasse verwenden (eingaben am besten auch)
    #     Es darf nicht sein das die Route die Straße verällst d.h. ein überschießen der Straße ist nicht vorgesehen

if __name__ == "__main__":
    unittest.main()




