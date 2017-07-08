import sys
import math
sys.path.append("..")
#from route import *
import unittest
from parameter import *
from path_planning import *
from matplotlib import pyplot as plt


class RoutenTest(unittest.TestCase):

    def testInit(self):
        #***************TEST ROUTE******************
        """
        Route1 = Route([(0, 1), (1000, 1)], width=1)

        a1 = 10
        a2 = -10
        v0 = 0
        t1 = 3
        #t2 = 3
        #t2 = 6
        t2 = 8
        v1 = v0 + a1*t1
        l1 = v0*t1 + 0.5*a1*t1*t1
        l2 = v1*t2 + 0.5*a2*t2*t2
        print(l1)
        print(l2)
        print(Route1.get_new_pos(l1))
        print(Route1.get_new_pos(l2))
        #print(Route1.get_next_dis())
        #print(Route1.point_iterator)
        #print(Route1.traveled_distance_on_route())
        #print(Route1.percent_of_route_still_to_travel())
        print(Strassen_Nets[1][1])
        #print(Route1.get_angle_from_start(1000))
        #print(Route1.get_new_pos(l2))
        #print(Route1.get_new_pos(-50))
        ##########BEISPIEL HIER##################
        
        Hier kann man eine Lange wie vorher eingeben, auch negative Lange möglich
        Weiss nicht was deine Problem ist, aber nach meiner Meinung
        mit Gleichung L = v_0*t+1/2*a*t^2 kann immer eine Lange berechnet werden
        
        Im Beispiel, a1 = 10, a2 = -10
        t1 = 3, l1 = 45
        wenn t2 = 3, l2 = 45 richtig
             t2 = 6, l2 = 0 richtig
             t2 = 8, l2 = -80 richtig
        

        #print(Route1.get_new_pos_from_start(50))
        #print(Route1.get_current_pos())
        #print(Route1.traveled_distance_on_route())
        #print(Route1.percent_of_route_still_to_travel())
        #print(Route1.get_percentage_from_start(100))
        #print(Route1.get_percentage_from_start(600))
"""

        # ***************TEST MATHE****************

        #list_a = [1,2,3,4]
        #list_b = [3,4,6,8]
        #print(list_and_list(list_a,list_b))



        #***************TEST NODE****************
        point = [250,400]
        street = Strassen_Nets
        direction = 1
        start = [0,250]
        end = [250,470]
        Node1 = Node([349.4,366.3],street,direction)
        #print(Node1.get_lower_node())


        #print(stack[len(stack)-1])

        #***************TEST PATH****************
        #Path1 = Path([0,250],[500,625],street=[[20, [0, 250, 1], [250, 250, 1], [375, 250], [500, 250]], [20, [250, 0], [250, 125], [250, 250], [250, 400]], [20, [125, 0], [250, 125], [375, 250], [500, 625]]])
        Path1 = Path(start, end, street)


        #Path1.set_visited([375,250])
        #print(Path1.check_visited([250,250]))
        #print(Path1.street)
        #Path1.set_unvisited([0,250])
        #print(Path1.check_visited([0,250]))
        #print(Path1.street)


        #print(Path1.get_unvisited_child([250, 250], [[250,123.25],[250,400],[301.8,250]],[[0,250]]))
        #print(Path1.get_unvisited_child([0,250],[0,250]))



        #print(Path1.depthFirstSearch_test())

        path = Path1.depthFirstSearch()
        print(path)

        #print(path[1][0])
        #print(calculate_length(path[0]))
        #print(calculate_length(path[1]))

        path = Path1.get_path()
        #path = [[0,100],[100,150],[300,400]]
        print(path)


        #Route1 = Route(path,width=20)
        #print(Route1.routepoints)

        #x = [p[0] for p in Route1.routepoints]
        #y = [p[1] for p in Route1.routepoints]
        #plt.plot(x,y,"g")
        #plt.show()


        #a = [1,2,3,4]
        #b = []
        #print(list_remove_list(a,b))






#****************Beispiel*************************

if __name__ == "__main__":
    unittest.main()


