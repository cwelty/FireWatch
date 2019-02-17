import fires.parseCoord
import biomes.biome_collect
import precipitation.precip_collect


# returns the coordinate information and fire data
def collect_data():
    biome_data = biomes.biome_collect.collect_biomes()  # biome data per pixel
    precipitation_data = precipitation.precip_collect.collect_precip()  # precipitation data per pixel
    fire_data = fires.parseCoord.parseFireCoord2017()
    
    coordinate_information = {}
    for entry_id in range(len(biome_data)):
        coordinate_information[str(biome_data[entry_id][0]) + "," + str(biome_data[entry_id][1])] = [biome_data[entry_id][2], precipitation_data[entry_id][2]]
    # [biome data, precip data]
    
    input_matrix = []
    output_matrix = []
    for fire in fire_data.keys():
        coordinates = str(int(fire_data[fire][0])) + "," + str(int(fire_data[fire][1]))
        input_matrix.append([coordinate_information[coordinates][0], coordinate_information[coordinates][1]])
        output_matrix.append(1)
    return input_matrix, output_matrix
