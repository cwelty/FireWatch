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
                if "</coordinates>" in coord:
                    continue

            else: 
                name = x[0][6:]
                coord = x[6].split(",")[:2]
                if "</coordinates>" in coord:
                    continue
            
            coord[0] = float(coord[0]) * .9061976549 # scaled down coordinates
            coord[1] = float(coord[1]) * .9061976549
            coord[0] = float(coord[0]) + 125
            results[name.upper()] = coord

    fireData = []
    with open("Fires_100 - 2017.csv", "r") as data2017:
        lines = data2017.readlines()
        for line in lines:
            line = line[:-1]
            fire = line.split(",")
            fireData.append(fire)

        mismatches = [[x[0] + " FIRE", x[1]] for x in fireData if x[0] not in results.keys()] 

    fireData = [x for x in fireData if x[0] in results.keys()] + mismatches
    fireData = [x for x in fireData if x[0] in results.keys()]
    # results has the coordinates, fireData has the date

    res = {}
    for fire in fireData:
        if fire[0] in results.keys():
            res[fire[0]] = results[fire[0]] + [fire[1]]

#    matlab_format = "["
#    for i in res.keys():
#        matlab_format += str(float(res[i][0])) + "," + str(float(res[i][1])) + ";"
#    matlab_format += "]"
#    print(matlab_format)
    return res

parseFireCoord2017()






