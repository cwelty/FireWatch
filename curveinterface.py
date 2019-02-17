import data.data_collection
import curves.curve
import math

# This file outlines a simple case of calculating fire risk coefficients!!!! 
def determine_coefficients():
    input_mat, output_mat = data.data_collection.generate_matrices()
    coefficients = curves.curve.polynomial_regression(input_mat, output_mat)
    return coefficients

# predicts how likely an area is to catch fire. X/Y are PIXEL COORDINATES!!!
def predict_pixel(x, y):
    coefficients = determine_coefficients()
    biome_coefficient = coefficients[0]
    precipitation_coefficient = coefficients[1]

    coordinate = str(x) + "," + str(y)
    collected_data, fire_data = data.data_collection.collect_data()
    components = collected_data[coordinate]
    biome = components[0]
    precipitation = components[1]
    
    burn_score = biome_coefficient * biome - precipitation_coefficient ** 2/3 * precipitation
    return burn_score


# USE THIS!!!! x and y should be your geocoordinates
def predict_geo(x, y):
    y = (float(y) - 32.6) * 52.3  # scale to biome map dimensions
    x = (-1 * (float(x)) - 114) * 34
    return predict_pixel(x, y)
    


#print(predict_pixel(123, 123))
