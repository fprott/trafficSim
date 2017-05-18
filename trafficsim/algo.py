from mathe import Point, Line, calculate_pos
import itertools as it

class SheduleStep():
    def __init__(self, start_time, car_ghosts):
        self.time = start_time
        self.car_ghosts = car_ghosts
        self.quality_value = None

    def assign_quality_value(self, value):
        self.quality_value = value

    def callculate_next_steps(self, t, dt, da, cars):
        dt, da = bulletime()
        new_time = self.start_time + dt
        for ghost in self.car_ghosts:
            ghost.get_possible_a_range(t,da)
            list(it.product(('1', '11'), ('2', '22'), ('3', '33')))

            a_range = car.get_possible_a_range(dt,da)
            for a_step in a_range: # bessere variablennamen !
                new_car = car.change_a_by_da(a_step)

class Step():
    def __init__(self, parent_step, t, car_actions):
        self.parent = parent_step
        self.t=t # jeder shedul Schrit hat eine startzeit
        self.car_actions=car_actions

    def is_root(self):
        if(self.parent == None):
            return True
        return False

    def make_next_steps(self, dt, da):


        possible_actions = []
        for car_action in self.car_actions:
            a_range = car_action.get_possible_a_range(self.t,da)
            possible_actions.append(tuple(a_range))
        print(tuple(possible_actions))

        print(list(it.product(tuple(possible_actions))))
        list(it.product(('1', '11'), ('2', '22'), ('3', '33')))

        new_step = Step(self, self.t+dt, )



# class CarAction():
#     def __init__(self, car_id, a):
#         self.car_id = car_id
#         self.a = a
#
#     def get_possible_a_range(self, t,da):
#         # FIXME : Levi, ka was die Phisik macht. Bitte denk dir was schlaues aus :D
#         a_range = range(-50, 50, 10)
#         a_range = [x / 10 for x in a_range]
#         return a_range
#
# car_actions=[CarAction("1",0),CarAction("2",0),CarAction("3",0)]
# my_step = Step(None,0, car_actions)
# my_step.make_next_steps(1,1)

def bulletime(self): # FIXME : implementieren !
    """
    Diese Funktion gibt eine diskrete Zeit "dt" und eine diskrete BEschleunigung "da" zurück. Diese Differenz ist klein wenn ein Unfall warscheinlich ist und groß wenn unwarscheinlich
    """
    dt = 1
    da = 1
    return dt,da #dt, da


class CarGhost():
    """
    Ein CarGhost ist ein Auto zu einem diskreten zeitpunkt. Der CarGhost hat N nachfolger, einen pro schrit
    """
    def __init__(self, max_v, max_a, v=0, a=0, pos=(0,0)):
        self.max_v=max_v #max_v : maximale geschwindigkeit
        self.max_a=max_a #max_a : maximale beschleunigung
        self.v=v
        self.a=a
        self.pos=pos

        def _set_v(self, new_v):
            if(new_v<=self.max_v):
                self.v=new_v
            else:
                self.v=self.max_v

        def _set_a(self, new_a):
            if(new_a<=self.max_a):
                self.a=new_a
            else:
                self.a=self.max_a
            pass

        def _change_a_by_da(self, da):
            if (self.a+da <= self.max_a): # wenn die neue beschleunigung kleiner als max beschleunigung
                if(self.a+da >= -self.max_a): # und wenn die (möglicherweise negative) beschleunigung größer als min beschleunigung
                    self.a=self.a+da;
                else:
                    self.a = -self.max_a
            else:
                self.a = self.max_a


        def get_change_a_by_da(self, da):
            if (self.a+da <= self.max_a): # wenn die neue beschleunigung kleiner als max beschleunigung
                if(self.a+da >= -self.max_a): # und wenn die (möglicherweise negative) beschleunigung größer als min beschleunigung
                    return self.a+da;
                else:
                    return -self.max_a
            else:
                return self.max_a

        def get_possible_a_range(self, t, da):
            """
            Diese Funktion gibt eine Liste aller möglichen relativenen Beschleunigungen zurück. t bestimmt wie viele a möglichkeiten es gibt
            0.0 sollte immer vorhanden sein. Wenn die Zeit "t" ausreicht dann halt auch +/-da, +/-2*da usw.
            :param self:
            :param t: zeit
            :param da: diskrete beschleunigung
            :return: Liste aller Beschleunigungen
            """
            # FIXME : Levi, ka was die Phisik macht. Bitte denk dir was schlaues aus :D
            a_range = range(-50,50,1)
            a_range /= 10
            return a_range

        def get_next_ghost(self, t, a):
            new_v = self.v+self.a*t # wir erechnen die neue geschwindigkeit
            new_pos = calculate_pos(self.pos, self.v) # wir erechnen die neue Position
            new_a = get_change_a_by_da(a)
            return CarGhost(self.max_v,self.max_a, new_v, new_a, new_pos) #make the next ghost
