Strassen_Nets = [
    [40,[0,250],[490,250]],
    [40,[250,0],[250,490]]
]

# Strassen_Nets = [
#     [20,[0,250],[400,250],[300,480]],
#     [20,[250,0],[250,400],[50,460]],
#     [40,[200,1],[400,490]]
# ]

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

