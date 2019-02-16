import matplotlib.image as img
import difflib


# finds the difference between two lists
def dist_lists(observed, expected):
    chi = 0
    for i in range(len(observed)):
        chi += abs(expected[i] - observed[i])
    return chi


# determines the precip level from a given rgb value
def color_to_precip_level(rgb):
    red = rgb[0]
    green = rgb[1]
    blue = rgb[2]
    
    precip_0_5 = [253, 1, 0]
    precip_5_10 = [254, 112, 2]
    precip_10_15 = [250, 171, 16]
    precip_15_20 = [253, 214, 0]
    precip_20_25 = [234, 245, 0]
    precip_25_30 = [214, 254, 10]
    precip_30_35 = [170, 255, 0]
    precip_35_40 = [100, 255, 0]
    precip_40_50 = [9, 242, 0]
    precip_50_60 = [3, 206, 98]
    precip_60_70 = [173, 253, 254]
    precip_70_80 = [0, 255, 217]
    precip_80_100 = [1, 245, 245]
    precip_100_120 = [25, 164, 219]
    precip_120_140 = [4, 4, 252]
    precip_140_180 = [153, 12, 238]
    precip_180_200 = [244, 9, 252]
    precip_null = [255,255,255]

    precips = [  precip_0_5,
                precip_5_10,
                precip_10_15,
                precip_15_20,
                precip_20_25,
                precip_25_30,
                precip_30_35,
                precip_35_40,
                precip_40_50,
                precip_50_60,
                precip_60_70,
                precip_70_80,
                precip_80_100,
                precip_100_120,
                precip_120_140,
                precip_140_180,
                precip_180_200,
                precip_null
    ]

    precip_inches = [
        "0-5",
        "5-10",
        "10-15",
        "15-20",
        "20-25",
        "25-30",
        "30-35",
        "35-40",
        "40-50",
        "50-60",
        "60-70",
        "70-80",
        "80-100",
        "100-120",
        "120-140",
        "140-180",
        "180-200",
        "null"
    ]

    precip_diff = []

    for precip in precips:
        precip_diff.append(dist_lists(rgb, precip))

    precip = precip_inches[precip_diff.index(min(precip_diff))]
    return precip
    

# CALL THIS FUNCTION!!
# Will collect the precipitation data and return it:
# Output: [x, y, precipitation]
def collect_precip():
    image = img.imread("ca_precip_cleared.png")
    image = image.tolist()

    precips = []
    h = -1
    for row in image:
        h += 1
        w = -1
        for col in row:
            w += 1
            red = int(col[0] * 255)
            green = int(col[1] * 255)
            blue = int(col[2] * 255)
            
            precips.append([w, h, color_to_precip_level([red, green, blue])])
    return precips