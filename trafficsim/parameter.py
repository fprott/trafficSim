Strassen_Nets = [
    [40,[0,250],[490,250]],
    [40,[250,0],[250,490]]
]

Schnitt_Punkte = [
    [[0,1],[1,1],[250,250]]
]

Startpunkt = [250,0]
Endpunkt = [0,250]
"""
Strassen_Nets = [
    [20,[0,250],[400,250],[300,480]],
    [20,[250,0],[250,400],[50,460]],
    [40,[200,1],[400,490]]
]

Schnitt_Punkte = [
         [[0,1],[0,2],[400,250]],
         [[0,1],[1,1],[250,250]],
         [[0,1],[2,1],[301.8,250]],
         [[0,2],[2,1],[349.4,366.3]],
         [[1,1],[1,2],[250,400]],
         [[1,1],[2,1],[250,123.25]]
]

Startpunkt = [250,0]
Endpunkt = [0,250]
"""

#import copy
#streets = copy.deepcopy(Strassen_Nets)
#points = copy.deepcopy(Schnitt_Punkte)
#print(streets)
#print(points)


from path_planning import *
Path1 = Path(Startpunkt, Endpunkt, Strassen_Nets=Strassen_Nets, Schnitt_Punkte=Schnitt_Punkte)
# All parameters to define a CLASS PATH are given from GUI, example as above*********************
Strassen_Nets_mit_Schnitt_Punkte = Path1.street

print(Strassen_Nets_mit_Schnitt_Punkte)
print(Path1.get_path())

print(Strassen_Nets)
print(Schnitt_Punkte)
#print(streets)
#print(points)


Fahrzeuge_Nets = [
    [3,[0,250],[500,250]],
    [5,[250,0],[250,500]]
]

Fahrbahn_Nets = [
    [[0,250]],
    [[250,0]]
]


for i in range(250):
    Fahrbahn_Nets[0].append([0+(i+1)*500/250,250])
Fahrbahn_Nets[1].append([250,0+(i+1)*500/250])
