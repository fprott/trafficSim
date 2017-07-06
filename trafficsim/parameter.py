from route import *
from path_planning import *

Flag_STOP = False

Strassen_Nets = [
    [40,[0,250],[250,250],[470,250]],
    [40,[250,0],[250,250],[250,470]]
]

# Strassen_Nets = [
#     [20,[0,250],[400,250],[300,480]],
#     [20,[250,0],[250,400],[50,460]],
#     [40,[200,1],[400,490]]
# ]

# Fahrzeuge_Nets = []

Fahrzeuge_Nets = [
    [3,[0,250],[500,250]],
    [5,[250,0],[250,500]]
]

Fahrbahn_Nets = [
    [[0,250]],
    [[250,0]]
]

for i in range(750):
    Fahrbahn_Nets[0].append([0+(i+1)*500/250,250])
    Fahrbahn_Nets[1].append([250,0+(i+1)*500/250])


start = [0,250]
end = [250,470]
Path1 = Path(start, end, Strassen_Nets)
#path = [[260,0],[250,250],[500,240]]
path = Path1.get_path()
Route1 = Route(path, width=40,accur=4)
print(Route1.routepoints)
Fahrbahn_Nets[1] = Route1.routepoints


Potenzielle_Fahrbahn_Nets = [[0 for i in range(int((Strassen_Nets[j][0])/20))] for j in range(len(Strassen_Nets))]
    # [[0,250]],
    # [[250,0]]
#]

# for i in range(250):
#     Potenzielle_Fahrbahn_Nets[0].append([0+(i+1)*500/250,250])
#     Potenzielle_Fahrbahn_Nets[1].append([250,0+(i+1)*500/250])
#
# Potenzielle_Fahrbahn_Nets[1] = Route1.routepoints

class strassen_info:
    def __init__(self, bereite = 20, nets = []):
        self.Bereite = bereite
        self.Nets = nets

    def add(self,strasse):
        strasse.append(self)

    def erneuen_bereite(self,bereite):
        self.Bereite = bereite

    def erneuen_nets(self,nets):
        self.Nets = nets

class fahrzeug_info:
    def __init__(self, type = 0, nets = []):
        self.Type = type
        self.Nets = nets

    def erneuen_type(self,type):
        self.Type = type

    def erneuen_nets(self,nets):
        self.Nets = nets

Strassen = []
for i in range(len(Strassen_Nets)):
    Strassen.append(strassen_info)
    Strassen[i].Bereite = Strassen_Nets[i][0]
    Strassen[i].Nets = Strassen_Nets[i][1:]
    print(Strassen[i].Bereite)
    print(Strassen[i].Nets)
    Strassen[i].erneuen_bereite(self = Strassen[i],bereite=50)
    print(Strassen[i].Bereite)

Fahrzeuge = []
for i in range(len(Fahrzeuge_Nets)):
    Fahrzeuge.append(fahrzeug_info)
    Fahrzeuge[i].Type = Fahrzeuge_Nets[i][0]
    Fahrzeuge[i].Nets = Fahrzeuge_Nets[i][1:]
    print(Fahrzeuge[i].Type)
    print(Fahrzeuge[i].Nets)
