def parseFireCoord2017():

    with open("2017 Statewide Fire Map.kml", "r") as data2017:
        lines = data2017.read() #reads the entire file

        lines = lines.split("<Placemark>")

        #list comprehension
        lines = [x for x in lines if "<Point>" in x]
        fires = [x.split("\n") for x in lines]

        fires = [[y.lstrip(" ") for y in x] for x in fires]

        results = {}
        for x in fires:
            x = [y for y in x if y != ""]
            if len(x) == 9:
                name = x[0][6:-7]
                coord = x[5].split(",")[:2]
            else: 
                name = x[0][6:]
                coord = x[6].split(",")[:2]
            results[name.upper()] = coord 

    with open("Fires_100 - 2017.csv", "r") as data2017:
        fireData = []
        lines = data2017.readlines()
        for line in lines:
            line = line[:-2]
            fire = line.split(",")
            fireData.append(fire) 

    mismatches = [[x[0] + " FIRE", x[1]] for x in fireData if x[0] not in results.keys()] 

    fireData = [x for x in fireData if x[0] in results.keys()] + mismatches
    fireData = [x for x in fireData if x[0] in results.keys()]
    # results has the coordinates, fireData has the date

    print(fireData)

    res = {}
    for fire in fireData:
        if fire[0] in results.keys():
            res[fire[0]] = results[fire[0]] + [fire[1]]

    return res

def parseFireCoord2016():

    #results = name + coordinates 
    with open("2016 Statewide Fire Map.kml", "r") as data2017:
        lines = data2017.read() #reads the entire file

        lines = lines.split("<Placemark>")

        #list comprehension
        lines = [x for x in lines if "<Point>" in x]
        fires = [x.split("\n") for x in lines]

        fires = [[y.lstrip(" ") for y in x] for x in fires]

        results = {}
        for x in fires:
            x = [y for y in x if y != ""]
            if len(x) == 9:
                name = x[0][6:-7]
                coord = x[5].split(",")[:2]
            else: 
                name = x[0][6:]
                coord = x[6].split(",")[:2]
            results[name.upper()] = coord 

    #fireData = name + date
    with open("Fires_100 - 2016.csv", "r") as data2015:
        fireData = []
        lines = data2015.readlines()
        for line in lines:
            line = line[:-2]
            fire = line.split(",")
            fireData.append(fire) 

    #find mismatches in the data 
    mismatches = [[x[0] + " FIRE", x[1]] for x in fireData if x[0] not in results.keys()] 

    #add updated mismatches(appended with FIRE so now they match) to fireData
    fireData = [x for x in fireData if x[0] in results.keys()] + mismatches
    #updated complete fireData, missing dates 
    fireData = [x for x in fireData if x[0] in results.keys()]
    
    # results has the coordinates, fireData has the date


    res = {}
    for fire in fireData:
        if fire[0] in results.keys():
            res[fire[0]] = results[fire[0]] + [fire[1]]

    return res    

def parseFireCoord2015():

    #results = name + coordinates 
    with open("2015 Statewide Fire Map.kml", "r") as data2017:
        lines = data2017.read() #reads the entire file

        lines = lines.split("<Placemark>")

        #list comprehension
        lines = [x for x in lines if "<Point>" in x]
        fires = [x.split("\n") for x in lines]

        fires = [[y.lstrip(" ") for y in x] for x in fires]

        results = {}
        for x in fires:
            x = [y for y in x if y != ""]
            if len(x) == 9:
                name = x[0][6:-7]
                coord = x[5].split(",")[:2]
            else: 
                name = x[0][6:]
                coord = x[6].split(",")[:2]
            results[name.upper()] = coord 

    #fireData = name + date
    with open("Fires_100 - 2015.csv", "r") as data2015:
        fireData = []
        lines = data2015.readlines()
        for line in lines:
            line = line[:-2]
            fire = line.split(",")
            fireData.append(fire) 

    #find mismatches in the data 
    mismatches = [[x[0] + " FIRE", x[1]] for x in fireData if x[0] not in results.keys()] 

    #add updated mismatches(appended with FIRE so now they match) to fireData
    fireData = [x for x in fireData if x[0] in results.keys()] + mismatches
    #updated complete fireData, missing dates 
    fireData = [x for x in fireData if x[0] in results.keys()]

    # results has the coordinates, fireData has the date

    res = {}
    for fire in fireData:
        if fire[0] in results.keys():
            res[fire[0]] = results[fire[0]] + [fire[1]]

    return res    

parseFireCoord2017()
parseFireCoord2016()
parseFireCoord2015()






