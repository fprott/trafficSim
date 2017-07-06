import linecache
import parameter

def file_load_Strassen():
    File = "Sim_Daten_Strassen.csv"
    file = open(File,"r")
    list = []

    for i in range(1, len(file.readlines()) + 1):
        line = linecache.getline("Sim_Daten_Strassen.csv", i).split(',')
        print(line)
        list.append(line)

    print(list)

    parameter.Strassen_Nets = []
    for num_Strassen in range(int((len(list)) / 2)):
        parameter.Strassen_Nets.append([int(list[2 * num_Strassen][0])])
        for num_Punkte in range(len(list[2 * num_Strassen]) - 2):
            parameter.Strassen_Nets[num_Strassen].append(
                [int(list[2 * num_Strassen][num_Punkte + 1]), int(list[2 * num_Strassen + 1][num_Punkte + 1])])
    print(parameter.Strassen_Nets)

    file.close();

def file_load_Fahrzeug():
    File = "Sim_Daten_Fahrzeug.csv"
    file = open(File,"r")
    list = []
    splitLine = [-1]

    for i in range(1, len(file.readlines()) + 1):
        line = linecache.getline("Sim_Daten_Fahrzeug.csv", i).split(',')
        print(line)
        list.append(line)

    for i in range(len(list)):
        if list[i][0] == '\n':
            splitLine.append(i)

    print(splitLine)
    print(list)

    parameter.Fahrzeuge_Nets = []
    for num_Fahrzeuge in range(int((splitLine[1] - splitLine[0] - 1) / 2)):
        parameter.Fahrzeuge_Nets.append([int(list[2 * num_Fahrzeuge + splitLine[0] + 1][0])])
        for num_Punkte in range(len(list[2 * num_Fahrzeuge + splitLine[0] + 1]) - 2):
            parameter.Fahrzeuge_Nets[num_Fahrzeuge].append(
                [int(list[2 * num_Fahrzeuge + splitLine[0] + 1][num_Punkte + 1]),
                 int(list[2 * num_Fahrzeuge + splitLine[0] + 2][num_Punkte + 1])])
    print(parameter.Fahrzeuge_Nets)

    parameter.Fahrbahn_Nets = []
    for num_Fahrbahn in range(int((splitLine[2] - splitLine[1] - 1) / 2)):
        parameter.Fahrbahn_Nets.append([])
        for num_Punkte in range(len(list[2 * num_Fahrbahn + splitLine[1] + 1]) - 1):
            # print(num_Fahrbahn,num_Punkte)
            parameter.Fahrbahn_Nets[num_Fahrbahn].append([float(list[2 * num_Fahrbahn + splitLine[1] + 1][num_Punkte]),
                                                          float(list[2 * num_Fahrbahn + splitLine[1] + 2][num_Punkte])])
    print(len(parameter.Fahrbahn_Nets))

    file.close();

def file_speichern_Strassen():
    file = open("Sim_Daten_Strassen.csv", "w")

    # Speichern die Daten von Strassen_Nets
    for num_Strassen in range(len(parameter.Strassen_Nets)):

        bereit_Strasse = parameter.Strassen_Nets[num_Strassen][0]
        inhalt_x = str()
        inhalt_y = str()
        inhalt_x = inhalt_x + str(bereit_Strasse).rstrip("\n") + ","
        inhalt_y = inhalt_y + str(bereit_Strasse).rstrip("\n") + ","

        for num_Punkte in range(1, (len(parameter.Strassen_Nets[num_Strassen]))):
            inhalt_x = inhalt_x + str(parameter.Strassen_Nets[num_Strassen][num_Punkte][0]).rstrip("\n") + ","
            inhalt_y = inhalt_y + str(parameter.Strassen_Nets[num_Strassen][num_Punkte][1]).rstrip("\n") + ","

        file.writelines(inhalt_x + "\n")
        file.writelines(inhalt_y + "\n")
        # print(inhalt_x)
        # print(inhalt_y)

    file.writelines("\n")

    file.close()


def file_speichern_Fahrzeug():
    file = open("Sim_Daten_Fahrzeug.csv", "w")

    # Speichern die Daten von Fahrzeuge_Nets
    for num_Fahrzeuge in range(len(parameter.Fahrzeuge_Nets)):

        type_Fahrzeug = parameter.Fahrzeuge_Nets[num_Fahrzeuge][0]
        inhalt_x = str()
        inhalt_y = str()
        inhalt_x = inhalt_x + str(type_Fahrzeug).rstrip("\n") + ","
        inhalt_y = inhalt_y + str(type_Fahrzeug).rstrip("\n") + ","

        for num_Punkte in range(1, (len(parameter.Fahrzeuge_Nets[num_Fahrzeuge]))):
            inhalt_x = inhalt_x + str(parameter.Fahrzeuge_Nets[num_Fahrzeuge][num_Punkte][0]).rstrip("\n") + ","
            inhalt_y = inhalt_y + str(parameter.Fahrzeuge_Nets[num_Fahrzeuge][num_Punkte][1]).rstrip("\n") + ","

        file.writelines(inhalt_x + "\n")
        file.writelines(inhalt_y + "\n")
        # print(inhalt_x)
        # print(inhalt_y)

    file.writelines("\n")

    # Speichern die Daten von Fahrbahn_Nets
    for num_Fahrbahn in range(len(parameter.Fahrbahn_Nets)):

        inhalt_x = str()
        inhalt_y = str()

        for num_Punkte in range(0, (len(parameter.Fahrbahn_Nets[num_Fahrzeuge]))):
            inhalt_x = inhalt_x + str(parameter.Fahrbahn_Nets[num_Fahrzeuge][num_Punkte][0]).rstrip("\n") + ","
            inhalt_y = inhalt_y + str(parameter.Fahrbahn_Nets[num_Fahrzeuge][num_Punkte][1]).rstrip("\n") + ","

        file.writelines(inhalt_x + "\n")
        file.writelines(inhalt_y + "\n")
        print(inhalt_x)
        print(inhalt_y)

    file.writelines("\n")

    file.close()

# if __name__ == '__main__':
#     file_speichern()
