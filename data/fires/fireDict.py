def parseFireHistory():
    fireDict = {}

    with open("data/fires/Fires_100 - 2017.csv", "r") as data2017:
        fireData = []
        lines = data2017.readlines()
        for line in lines:
            line = line[:-2]
            fire = line.split(",")
            fireData.append(fire) 
        fireDict["2017"] = fireData

    with open("data/fires/Fires_100 - 2016.csv", "r") as data2017:
        fireData = []
        lines = data2017.readlines()
        for line in lines:
            fire = line.split(",")
            fireData.append(fire)
        fireDict["2016"] = fireData

    with open("data/fires/Fires_100 - 2015.csv", "r") as data2017:
        fireData = []
        lines = data2017.readlines()
        for line in lines:
            line = line[:-2]
            fire = line.split(",")
            fire = [x for x in fire if x != " "]
            fireData.append(fire) 
        fireDict["2015"] = fireData

    return fireDict
