import matplotlib.image as img
import difflib


# finds the difference between two lists
def dist_lists(observed, expected):
    chi = 0
    for i in range(len(observed)):
        chi += abs(expected[i] - observed[i])
    return chi


# determines the biome from a given rgb value
def color_to_biome(rgb):
    red = rgb[0]
    green = rgb[1]
    blue = rgb[2]
    
    biome_conifer = [80, 120, 68]
    biome_desert = [255, 235, 190]
    biome_grassland = [254, 167, 2]
    biome_chaparral = [231, 230, 0]
    biome_oak = [156, 171, 214]
    biome_agriculture = [168, 111, 8]
    biome_wetlands = [115, 179, 253]
    biome_juniper = [1, 2, 7]
    biome_urban = [226, 226, 226]
    biome_other = [129, 127, 132]
    biome_null = [255, 255, 255]

    biomes = [biome_conifer,
                biome_desert,
                biome_grassland,
                biome_chaparral,
                biome_oak,
                biome_agriculture,
                biome_wetlands,
                biome_juniper,
                biome_urban,
                biome_other,
                biome_null
    ]

    biome_names = [
        9, #"conifer",
        .1, #"desert",
        10, #"grassland",
        7, #"chaparral",
        8, #"oak",
        2, #"agriculture",
        3, #"wetlands",
        7, #"juniper",
        .1, #"urban",
        .1, #"other",
        .1 #"null"
    ]

    biome_chi = []

    for biome in biomes:
        biome_chi.append(dist_lists(rgb, biome))

    biome = biome_names[biome_chi.index(min(biome_chi))]
    return biome
    

# CALL THIS FUNCTION!!
# Will collect the biome data and return it:
# Output: [x, y, biome]
def collect_biomes():
    image = img.imread("data/biomes/ca_biome_map_cropped.png")
    image = image.tolist()

    biomes = []
    h = -1
    for row in image:
        h += 1
        w = -1
        for col in row:
            w += 1
            red = int(col[0] * 255)
            green = int(col[1] * 255)
            blue = int(col[2] * 255)
            
            biomes.append([w, h, color_to_biome([red, green, blue])])
    return biomes
