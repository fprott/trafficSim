from mathe import Point, Line, calculate_pos
import itertools
import functools

# TODO @Levi :
# 1.) Phisk von CarGhosts anschauen und fixen
# 2.) Bullettime algo basteln, er soll uns einen Zeitschrit und Beschleunigunsschrit (diskret) zurückgeben
# 3.) Position der Autos berücksichtigen d.h. einen Fahrtvektor einfügen. Hier wurde noch nix gemacht d.h. freie enfaltung
# TODO @Flo:
# 1.) Algo auf A* Nievou bringen
# 2.) Traceback überprüfen
# 3.) Terminirung einführen d.h. die autos die schon durch sind irgenwie aus dem system enferen und schauen das es immer terminiert auch wenn unöglich (d.h. immer unfall)
# 4.) Testen. Am besten grafisch auf der animation

class Shedule():
    # Achtung noch kein echter A*, nur ein test
    def __init__(self, cars):
        self.shedule_steps = []
        first_step = SheduleStep(None, 0, cars) # TODO aus cars car_ghost machen !
        self.shedule_steps.append(first_step)

    def make_shedule_step(self):
        current_step = self.shedule_steps[-1]
        dt = 1
        da = 1
        all_possible_next_steps=current_step.callculate_next_steps(dt,da)
        for step in all_possible_next_steps:
            print("STEP")
            for car in step.car_ghosts:
                print(car)

        best_next_step=all_possible_next_steps[0]
        for step in all_possible_next_steps:
            if(step.quality_value>best_next_step.quality_value):
                best_next_step=step

        print("we choosed")
        for car in best_next_step.car_ghosts:
            print(car)
    #    print(best_next_step.quality_value)
        if(best_next_step.start_time>10):
        #    print(self.shedule_steps)
            return self.shedule_steps
        if(best_next_step==None): # wenn kein weiter schrit mehr möglich/notwendig ist
            return self.shedule_steps
#        if(best_next_step.quality_value()==None): #wenn Unfall oder unmöglich
#            current_step.quality_value=None
#            return # TODO richtiger a* machen
        self.shedule_steps.append(best_next_step)
        self.make_shedule_step()

class SheduleStep():
    def __init__(self, parent, start_time, car_ghosts):
        self.parent = parent
        self.start_time = start_time
        self.car_ghosts = car_ghosts
        self.quality_value = self.callculate_quality_value()

    def callculate_quality_value(self): #TODO: anders maß einbringen und AUSLAGERN !
        quality = 0
        for car in self.car_ghosts:
            quality += car.a
        return quality

    def callculate_next_steps(self, dt, da):
        new_time = self.start_time + dt

        all_possible_car_ghosts_tuples = []
        for ghost in self.car_ghosts:
            possible_new_ghosts = ()
            for a in ghost.get_possible_a_range(dt,da):
                possible_new_ghosts = possible_new_ghosts + (ghost.get_next_ghost(dt,a),) # ein tupel enhällt alle möglichen nächsten ghosts
            all_possible_car_ghosts_tuples.append(possible_new_ghosts) # List von tupeln

    #    print(tuple(all_possible_car_ghosts_tuples))
        all_car_ghost_possiblites = list(itertools.product(*all_possible_car_ghosts_tuples)) # hexerei, bitte schaut euch die doku an wenn das net geht
        all_possible_steps = []
        for possiblity in all_car_ghost_possiblites:
            all_possible_steps.append(SheduleStep(self, new_time, possiblity))
        return all_possible_steps
    #     print("----")
    # #    print(all_car_ghost_possiblites)
    #     print("----")
    #     for possiblity in all_car_ghost_possiblites:
    #     #    print(possiblity)
    #         for ghost in possiblity:
    #             print(ghost)
    #         #    print(ghost.id, ghost.a)
    #         print("----")
    #         #list(it.product(('1', '11'), ('2', '22'), ('3', '33')))

def bulletime(): # FIXME : implementieren !
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
    def __init__(self, id, max_v, max_a, v=0, a=0, pos=(0,0)):
        self.id = id # das dient dazu das wir die auseinanderhalten können und zum debugen
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

    def get_possible_a_range(self, dt, da):
        """
        Diese Funktion gibt eine Liste aller möglichen relativenen Beschleunigungen zurück. t bestimmt wie viele a möglichkeiten es gibt
        0.0 sollte immer vorhanden sein. Wenn die Zeit "t" ausreicht dann halt auch +/-da, +/-2*da usw.
        :param self:
        :param dt: delta zeit
        :param da: delta beschleunigung
        :return: Liste aller Beschleunigungen
        """
        # FIXME : Levi, ka was die Phisik macht. Bitte denk dir was schlaues aus :D
        a_range = [x / 10.0 for x in range(-50, 50, 10)]
        return a_range

    def get_next_ghost(self, dt, da):
        new_v = self.v+self.a*dt # wir erechnen die neue geschwindigkeit
        new_pos = calculate_pos(self.pos, dt, self.v) # wir erechnen die neue Position
        new_a = self.get_change_a_by_da(da)
    #    return (str(self.id) +" "+ str(new_a))
        return CarGhost(self.id, self.max_v,self.max_a, new_v, new_a, new_pos) #make the next ghost

    def __str__(self): # TODO mehr Werte
        return (str(self.id) +" "+ str(self.a))


Car1 = CarGhost("1",120,20,0,0,(0,0))
Car2 = CarGhost("2",120,30,0,0,(0,0))
Car3 = CarGhost("3",150,10,0,0,(0,0))
Car4 = CarGhost("4",150,55,0,0,(0,0))
shedule = Shedule([Car1,Car2,Car3,Car4])
shedule.make_shedule_step()
for step in shedule.shedule_steps:
    print("Step time : "+str(step.start_time))
    for car in step.car_ghosts:
        print(car)
