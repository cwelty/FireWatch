import data.data_collection
import curves.curve
import math

# This file outlines a simple case of calculating fire risk coefficients!!!! 
def determine_coefficients():
    input_mat, output_mat = data.data_collection.generate_matrices()
    coefficients = curves.curve.polynomial_regression(input_mat, output_mat)
    return coefficients

# predicts how likely an area is to catch fire. X/Y are GEOGRAPHIC COORDINATES
def predict(coords):  # coords is a LIST of [x, y]: [[x1,y1], [x2,y2], [x3,y3]]
    coefficients = determine_coefficients()
    biome_coefficient = coefficients[0]
    precipitation_coefficient = coefficients[1]

    collected_data, fire_data = data.data_collection.collect_data()

    burn_scores = []
    for coordinate in coords:
        #top: 42 long
        #bottom: 32 long
        #left: 125 lat
        #right 114 lat

        #image: 434 x by 491 y

        #x: -(x - 114) * 43.4
        #y: (y - 32) * 49.1

        y = (float(coordinate[1]) - 32) * 49.1 - 1  # scale to biome map dimensions
        x = (1 - (float(coordinate[0]) - 114)/11) * 433 + 1

        coord = str(int(x)) + "," + str(int(y))
        components = collected_data[coord]
        #print(collected_data.keys())

        biome = components[0]
        precipitation = components[1]
    
        burn_score = biome_coefficient * biome - precipitation_coefficient ** 2/3 * precipitation
        burn_scores.append(burn_score)

    return burn_scores # it returns a list of floats, cooresponding to the coordinates inputted

#print(predict([[124, 42]]))
