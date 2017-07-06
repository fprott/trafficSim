# Weil jeder UnitTest kennt benutzen wir das
from algo2 import *
import unittest

class ASternTest(unittest.TestCase):

    def test_no_crash_no_problem(self):
        myRoute = Route(Route.castPointsToWangNotation([Point(0.0, 0.0), Point(100.0, 100.0)]), 2)
        myCar = Car("test_1", 0.0, 80.0, -60.0, 120.0, 0.0, 0.0, 0.0, CarSize(4, 2), myRoute.get_current_pos(), myRoute)

        myCars = []
        myCars.append(myCar)
        mySenario = Senario(None, 0, myCars)
        myGraph = Graph(mySenario)
        solution = myGraph.calluclate_best_senarios()

        self.assertIsNotNone(solution)
        for node in solution:
            for car in node.cars:
                self.assertEqual(car.a, car.a_max)

    def test_one_crash_easy(self):
        myRoute = Route(Route.castPointsToWangNotation([Point(0.0, 0.0), Point(1000.0, 1000.0)]), 2)
        myRoute2 = Route(Route.castPointsToWangNotation([Point(0.0, 1000.0), Point(1000.0, 0.0)]), 2)
        myCar = Car("test_1", 0.0, 80.0, -60.0, 120.0, 0.0, 0.0, 0.0, CarSize(4, 2), myRoute.get_current_pos(), myRoute)
        myCar2 = Car("test_2", 0.0, 80.0, -60.0, 120.0, 0.0, 0.0, 0.0, CarSize(4, 2), myRoute2.get_current_pos(), myRoute2)
        myCars = []
        myCars.append(myCar)
        myCars.append(myCar2)
        mySenario = Senario(None, 0, myCars)
        myGraph = Graph(mySenario)
        solution = myGraph.calluclate_best_senarios()
        self.assertIsNotNone(solution)

        myCars=[myCar]
        mySenario = Senario(None, 0, myCars)
        myGraph = Graph(mySenario)
        best_solution = myGraph.calluclate_best_senarios()
        # wenn man nur so fährt braucht man minimale zeit, ich denke wir sind nicht viel langsamer
        solution_cost = 0
        for node in solution:
            solution_cost += node._get_node_cost()
        best_solution_cost = 0
        for node in best_solution:
            best_solution_cost += node._get_node_cost()
     #   self.assertAlmostEqual(solution_cost, best_solution_cost, delta=0.2) # der abstand zwischen den beiden ist maximal 0.2 sec pro crash
    #
    # #    self.assertEqual()
    #
    # ACHTUNG: es ist nicht empfehlenswert diesen Test mit weniger als 16 GB Ram auszuführen !
    # JEDER einzelne Knoten muss durchgegangen werden. Das sind Millionen
    # Kleine Anmerkung, der Test ist super um kappute Speicherbereiche zu finden ;D
    def test_crash_unavoidable(self): #this will and must take forever :D
        myRoute = Route(Route.castPointsToWangNotation([Point(0.0, 0.0), Point(100.0, 0.0)]), 2)
        myRoute2 = Route(Route.castPointsToWangNotation([Point(100.0, 0.0), Point(0.0, 0.0)]), 2)
        myCar = Car("test_1", 0.0, 50.0, -60.0, 120.0, 0.0, 0.0, 0.0, CarSize(4, 4), myRoute.get_current_pos(), myRoute)
        myCar2 = Car("test_2", 0.0, 50.0, -60.0, 120.0, 0.0, 0.0, 0.0, CarSize(4, 4), myRoute2.get_current_pos(), myRoute2)
        #myCar = Car("test_1", 0.0, 50.0, -20.0, 50.0, 10.0, 0.0, 0.0, CarSize(10, 0), myRoute.get_current_pos(), myRoute)
        #myCar2 = Car("test_2", 0.0, 50.0, -20.0, 50.0, 10.0, 0.0, 0.0, CarSize(10, 0), myRoute2.get_current_pos(), myRoute2)
        myCars = []
        myCars.append(myCar)
        myCars.append(myCar2)
        mySenario = Senario(None, 0, myCars)
        myGraph = Graph(mySenario)
        exeption = False
        try:
            solution = myGraph.calluclate_best_senarios()
        except:
            exeption = True
        self.assertTrue(exeption)
    #
    # def test_long_cut_crash(self):
    #     # die route sollte einen sehr lange schnitfäche haben, außerdem sind die autos 4 x 4
    #     myRoute = Route(Route.castPointsToWangNotation([Point(0.0, 25.0), Point(1000.0, 0.0)]), 2)
    #     myRoute2 = Route(Route.castPointsToWangNotation([Point(0.0, 0.0), Point(1000.0, 50.0)]), 2)
    #     myCar = Car("test_1", 0.0, 50.0, -50.0, 120.0, 0.0, 0.0, 0.0, CarSize(4, 4), myRoute.get_current_pos(), myRoute)
    #     myCar2 = Car("test_2", 0.0, 50.0, -50.0, 120.0, 0.0, 0.0, 0.0, CarSize(4, 4), myRoute2.get_current_pos(), myRoute2)
    #     myCars = []
    #     myCars.append(myCar)
    #     myCars.append(myCar2)
    #     sc = SchroedingersCrash(Zeitpunkt(0, myCars, None, 0.05))
    #     sc.do_the_schroedinger()
    #     solution = sc.get_best_solution()
    #     self.assertEqual(len(sc.possible_solutions),2)
    #     self.assertIsNotNone(solution)
    #
    # def test_nearly_two_crashs(self):
    #     myRoute = Route(Route.castPointsToWangNotation([Point(0.0, 0.0), Point(500.0, 500.0), Point(1000.0, 0.0)]), 2)
    #     myRoute2 = Route(Route.castPointsToWangNotation([Point(0.0, 500.0), Point(500.0, 0.0), Point(1000.0, 500.0)]), 2)
    #     myCar = Car("test_1", 0.0, 50.0, -50.0, 120.0, 0.0, 0.0, 0.0, CarSize(4, 4), myRoute.get_current_pos(), myRoute)
    #     myCar2 = Car("test_2", 0.0, 50.0, -50.0, 120.0, 0.0, 0.0, 0.0, CarSize(4, 4), myRoute2.get_current_pos(), myRoute2)
    #     myCars = []
    #     myCars.append(myCar)
    #     myCars.append(myCar2)
    #     sc = SchroedingersCrash(Zeitpunkt(0, myCars, None, 0.05))
    #     sc.do_the_schroedinger()
    #     solution = sc.get_best_solution()
    #
    #     # wir erwarten exakt einen crash, NICHT zwei -> wir erwarten 2 Lösungen nicht 4
    #     self.assertEqual(len(sc.possible_solutions), 2)
    #     self.assertNotEqual(len(sc.possible_solutions), 4)
    #     self.assertIsNotNone(solution)
    #
    #     myCars=[myCar]
    #     sc = SchroedingersCrash(Zeitpunkt(0, myCars, None, 0.05))
    #     sc.do_the_schroedinger()
    #     best_solutions = sc.get_best_solution()
    #     # wenn man nur so fährt braucht man minimale zeit, ich denke wir sind nicht viel langsamer
    #     self.assertAlmostEqual(solution.get_costs(),best_solutions.get_costs(), delta=0.2) # der abstand zwischen den beiden ist maximal 0.2 sec pro crash
    #
    # def test_two_crashs(self):
    #     # 1 crash
    #     myRoute = Route(Route.castPointsToWangNotation([Point(0.0, 0.0), Point(500.0, 500.0), Point(1000.0, 0.0)]), 2)
    #     myRoute2 = Route(Route.castPointsToWangNotation([Point(0.0, 500.0), Point(500.0, 0.0), Point(1000.0, 1000.0)]), 2)
    #     myCar = Car("test_1", 0.0, 50.0, -50.0, 120.0, 0.0, 0.0, 0.0, CarSize(4, 4), myRoute.get_current_pos(), myRoute)
    #     myCar2 = Car("test_2", 0.0, 50.0, -50.0, 120.0, 0.0, 0.0, 0.0, CarSize(4, 4), myRoute2.get_current_pos(), myRoute2)
    #     # 2 crash
    #     myRoute3 = Route(Route.castPointsToWangNotation([Point(2000.0, 0.0), Point(1800.0, 500.0)]), 2)
    #     myRoute4 = Route(Route.castPointsToWangNotation([Point(2000.0, 500.0), Point(1800.0, 0.0)]), 2)
    #     myCar3 = Car("test_3", 0.0, 50.0, -50.0, 120.0, 0.0, 0.0, 0.0, CarSize(4, 4), myRoute3.get_current_pos(), myRoute3)
    #     myCar4 = Car("test_4", 0.0, 50.0, -50.0, 120.0, 0.0, 0.0, 0.0, CarSize(4, 4), myRoute4.get_current_pos(), myRoute4)
    #     myCars = []
    #     myCars.append(myCar)
    #     myCars.append(myCar2)
    #     myCars.append(myCar3)
    #     myCars.append(myCar4)
    #     sc = SchroedingersCrash(Zeitpunkt(0, myCars, None, 0.05))
    #     sc.do_the_schroedinger()
    #     solutions = sc.get_best_solution()
    #
    #     # wir erwarten zwei crashs -> 4 Lösungen
    #     self.assertEqual(len(sc.possible_solutions), 4)
    #     self.assertIsNotNone(solutions)
    #
    # def test_two_crashs_same_time(self):
    #     myRoute = Route(Route.castPointsToWangNotation([Point(0.0, 0.0), Point(1000.0, 1000.0)]), 2)
    #     myRoute2 = Route(Route.castPointsToWangNotation([Point(0.0, 1000.0), Point(1000.0, 0.0)]), 2)
    #     myRoute3 = Route(Route.castPointsToWangNotation([Point(0.0, 500.0), Point(1000.0, 500.0)]), 2)
    #     myCar = Car("test_1", 0.0, 50.0, -50.0, 120.0, 0.0, 0.0, 0.0, CarSize(4, 4), myRoute.get_current_pos(), myRoute)
    #     myCar2 = Car("test_2", 0.0, 50.0, -50.0, 120.0, 0.0, 0.0, 0.0, CarSize(4, 4), myRoute2.get_current_pos(), myRoute2)
    #     myCar3 = Car("test_3", 0.0, 50.0, -50.0, 120.0, 0.0, 0.0, 0.0, CarSize(4, 4), myRoute3.get_current_pos(), myRoute3)
    #     myCars = []
    #     myCars.append(myCar)
    #     myCars.append(myCar2)
    #     myCars.append(myCar3)
    #     sc = SchroedingersCrash(Zeitpunkt(0, myCars, None, 0.05))
    #     sc.do_the_schroedinger()
    #     solution = sc.get_best_solution()
    #     # wir erwarten 4 lösungen da wir 2 unfälle haben ABER zwei dieser Lösungen MÜSSEN gelöscht werden da diese exakt gleich sind !
    #     self.assertEqual(len(sc.possible_solutions), 2)
    #     self.assertNotEqual(len(sc.possible_solutions), 4)
    #     self.assertIsNotNone(solution)
    #
    #     myCars=[myCar]
    #     sc = SchroedingersCrash(Zeitpunkt(0, myCars, None, 0.05))
    #     sc.do_the_schroedinger()
    #     best_solutions = sc.get_best_solution()
    #     # wenn man nur so fährt braucht man minimale zeit, ich denke wir sind nicht viel langsamer
    #     self.assertAlmostEqual(solution.get_costs(),best_solutions.get_costs(), delta=0.4) # der abstand zwischen den beiden ist maximal 0.1 sec pro crash

    # def lotsa_cars(self):

if __name__ == "__main__":
    unittest.main()




