from math import ceil

def no_of_cans(wall_height, wall_width, coverage):

    area = wall_width*wall_height
    #print(area / coverage)
    cans = ceil(area / coverage)

    return cans


wall_height = int(input("Enter wall height :"))
wall_width = int(input("Enter wall width :"))
coverage = 7

cans = no_of_cans(wall_height, wall_width, coverage)

print(f"To paint this wall, you will required {cans} cans")