#Diese Klassen sollen von euch nach euren Vorschlägen verfollständig werden.
#Wenn feststeht wie der Polygonenzug aussieht kann ich das auch noch schnell fertig machen, aber erstmal gibt mir feedback !
class StreetSystem:
    """
    Anzahl aller Straßenetze. Verwaltet die Netze
    """
    def __init__(self):
        self.nets=[] # Alle möglichen netze

    # Es ist notwendig eine Line für jeden ereichbaren Punkt und für jeden daraufolgenden Punkt anzulegen

    def addPoint(self, new_point, connected_point=None):
        if (connected_point==None): # wir müssen ein neues Netz eröfnnen
            newStreetNet = StreetNet(new_point)
            self.nets.append(newStreetNet)
            #TODO : FERTIG CODEN!

class StreetNet:
    """
    Anzahl von Punkten die miteinander verbunden sind und ein mögliches Straßennetz beschreiben. Dient der abstrakten Darstellung
    """

    def __init__(self):
        self.street_end_points = []  # Alle möglichen netze

    def add_point(self, new_point, connected_point=None):
        if (connected_point == None):  # wir müssen ein neues Netz eröfnnen
            self.nets.append()
            # TODO : FERTIG CODEN!



def calculate_pos(old_pos, dt, v):
    """
    Errechnet eine neue Position anhand von der alten Position und diversen Parameteren. Achtung, statische Funktion
    :param old_pos: Alte Position
    :param dt: Zeiteinheit
    :param v: Geschwindigkeit
    :return:
    """
    return old_pos+((v*dt),(v*dt)) # FIXME das braucht noch ne richtungsvektor !!!

#Die funktionierien und sind frei nutzbar!!!
class Line(list):
    """
    Linie zwischen zwei Punkten. Dient der grafischen Darstellung
    """
    def __init__(self, start_point=None):
        self=[]
        if not start_point==None:
            self.append(start_point)

    def append(self, point):
        if not isinstance(point, Point):
            raise TypeError("Line can only hold Object of type Poin")
        super(Line, self).append(point)

    def getFirstPoint(self):
        return self[0]

    def getLastPoint(self):
        return self[-1]

class Point(tuple):
    """
    Ein einzelnder Punkt mit x,y kordinate
    """
    def __new__(self, x, y):
        return tuple.__new__(Point, (x, y))

    def __init__(self, x, y):
        self=(x,y)

    def _get_x(self):
        return self[0]

    def _set_x(self,new_x):
        self=(new_x,self[1])

    x = property(_get_x,_set_x)

    def _get_y(self):
        return self[1]

    def _set_y(self,new_y):
        self = (self[0], new_y)

    y = property(_get_y, _set_y)
