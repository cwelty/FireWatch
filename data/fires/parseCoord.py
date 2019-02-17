def parseFireCoord2017():
    with open("data/fires/2017 Statewide Fire Map.kml", "r") as data2017:
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
            
            coord[1] = (float(coord[1]) - 32.6) * 52.3  # scale to biome map dimensions
            coord[0] = (-1 * (float(coord[0])) - 114) * 34
            results[name.upper()] = coord

    fireData = []
    with open("data/fires/Fires_100 - 2017.csv", "r") as data2017:
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

    #print(res)
    maxx = 0
    for i in res.keys():
        if res[i][1] > maxx:
            maxx = res[i][1]
    #print(maxx)
    return res






