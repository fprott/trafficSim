# ANFORDERUNGEN Algo / :

#1) Ein Szenario das keine Lösung (2 Autos dieselbe Straße in entgegengesetze Richtungen) hat muss im Vorfeld erkannt werden
# (vlt vom Benutzer) sonst läuft der algo alle Fälle ab -> ewig

#2) dt muss passend gewhält werden damit alle Kollisionen entdeckt werden dt< min(länge_Autos)/max(v_max) bzw Bullettime integrieren aber erst nachdem der standard funktioniert

#3)Muss auch für initial condition ungleich 0 funktionieren/getestet werden bzw startpunkt nicht am Anfang der Route

#4) Autos die ihr ziel erreicht haben aus dem Algo rausnehmen oder konstant mit a=0 weiterfahren lassen um Rechenzeit zu redurieren

#5) Die Menge mit möglichen Beschleunigungen muss 0 beinhalten

#6) Geschwindigkeiten dürfen nicht negativ werden und die Beschleunigungen nach Erreichen des Zielen idealerweise 0 oder nicht negativ

#7)ADVANCED : Gruppen von Autos bilden zwichen denen Kollision vorkommen können und mehrere instanzen des algo parallel ablaufen lassen


import unittest




class AlgoTest(unittest.TestCase):


    def test_same_direction(self):

        # 2 Autos fahren in dieselbe Richtung das schnellere Auto (Car2) ist zu Anfang etwas weiter hinten -> Car2 muss häufig bremsen
        Route1 = Route(Route.castPointsToWangNotation([Point(0.0, 0.0), Point(1000.0, 0.0)]), 2)
        Route2 = Route(Route.castPointsToWangNotation([Point(100.0, 0.0), Point(1500.0, 0.0)]), 2)
        Car1 = CarMarker("test_1", Route1, 60.0, -40.0, 300.0, 0.0, 0.0, 0.0, CarSize(60, 0))
        Car2 = CarMarker("test_2", Route2, 40.0, -40.0, 150.0, 0.0, 0.0, 0.0, CarSize(50, 0))
        myCars = []
        myCars.append(Car1)
        myCars.append(Car2)
        mySenario = Senario(None, 0, myCars)
        myGraph = Graph(mySenario)
        bestSenarios = myGraph.calluclate_best_senarios()
        Senario.printDebugSenarios(bestSenarios)


 #   def test_collision(self):
  #      # 2 Autos fahren in dieselbe Richtung aufeinander zu
   #     Route1 = Route(Route.castPointsToWangNotation([Point(0.0, 0.0), Point(300, 0.0)]), 2)
    #    Route2 = Route(Route.castPointsToWangNotation([Point(300, 0.0), Point(0.0, 0.0)]), 2)
     #   Car1 = CarMarker("test_1", Route1, 60.0, -40.0, 300.0, 0.0, 0.0, 0.0, CarSize(60, 0))
      #  Car2 = CarMarker("test_2", Route2, 40.0, -40.0, 150.0, 0.0, 0.0, 0.0, CarSize(50, 0))
       # myCars = []
        #myCars.append(Car1)
    #    myCars.append(Car2)
     #   mySenario = Senario(None, 0, myCars)
      #  myGraph = Graph(mySenario)
       # bestSenarios = myGraph.calluclate_best_senarios()
     #   Senario.printDebugSenarios(bestSenarios)



if __name__ == "__main__":
    unittest.main()

