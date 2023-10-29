# -*- coding: utf-8 -*-
"""
Created on Mon Jul 17 13:50:54 2023

@author: gilor
"""
import random
import math
import numpy as np

"""FUNCTIONS TO CALCULATE THE MODELS"""

# Calculate (Squared) Distance from a point (x,y) to the center of a colony.
def calculate_squared_distance_to_colony(x, y, colony):
    return (colony['center_x'] - x) ** 2 + (colony['center_y'] - y) ** 2

# Calculate (Squared) Distance between the centers of two colonies.
def calculate_squared_distance_between_colonies(colony1, colony2):
    return calculate_squared_distance_to_colony(colony1['center_x'], colony1['center_y'], colony2)

# Calculate the area of a colony
def calculate_area(colony):
    return math.pi * colony['radius'] ** 2

# We choose I, i.e. the maximum radius size of a colony, as the minimum distance to the border, so that colonies do not
# grow outside the boundaries.
def create_new_colony(I, l, R_0):
    center_x = random.uniform(I, l - I)
    center_y = random.uniform(I, l - I)
    return {'center_x': center_x, 'center_y': center_y, 'radius': R_0, 'age': 0}

# Generate a new colony. If colonies already exist, take into account that new colonies are not generated inside them.
# Colonies can also not be generated in the edge of the domain
# (therefore we generate them between I and l-I)
# last, if checkSpaceAvailable = True, we check if the colony has enough space to be generated
def generate_colony(l, R_0, I, old_colonies=[], checkSpaceAvailable=False):
    threshold = 0
    new_colony = None
    if checkSpaceAvailable:
        threshold = I / 2
        # if checkSpaceAvailable, distance to the closest colony must be bigger than this
        # otherwise, threshold = 0 but to ensure they are still not inside each other,
        # we check the distance is <= colony + R_0
    if len(old_colonies) > 0:
        max_iterations = 0
        valid = False
        while not valid and max_iterations < 1:
            new_colony = create_new_colony(I, l, R_0)
            valid = True
            for colony in old_colonies:
                distance = calculate_squared_distance_between_colonies(new_colony, colony)
                # function all() could also be used to check that all conditions in a loop are True (
                # but apparently is not faster)
                isInsideColony=distance <= (colony['radius'] + R_0 + threshold) ** 2
                if isInsideColony:
                    valid = False
                    break
            max_iterations += 1
        return new_colony if valid else None
    else:
        return create_new_colony(I, l, R_0)

# Calculate the bacterial concentration in our domain (sum of all colonies' areas)
# In this case, we assume that the bacteria can be overlapping, i.e. we count twice whenever two colonies overlap
def calculate_bacterial_concentration(colonies):
    return sum(calculate_area(colony) for colony in colonies)

# Calculate how much of our domain lxl is covered with bacteria numerically.
def calculate_total_covered_area(colonies, l, grid_step=0.2):
    area = 0
    step_addition = grid_step ** 2
    for i in np.arange(0, l, grid_step):
        for j in np.arange(0, l, grid_step):
            for colony in colonies:
                if calculate_squared_distance_to_colony(i, j, colony) <= colony['radius'] ** 2:
                    area += step_addition
                    # the grid point is already covered by at least one colony, so we can move on to the next grid point
                    break

    return area

# Calculate the percentage of the grid that it´s covered by the bacteria
# We use this measure for the density of the colonies
def calculate_percentage_covered(colonies, l, grid_size=0.2):
    area = calculate_total_covered_area(colonies, l, grid_size)
    return area / (l ** 2)

# We consider that the nutrients are distributed homogeneously in the medium at the beginning
# so a measure of nutrient availability could be the percentage of the domain which is not covered by colonies
def calculate_nutrient_availability(colonies, l, grid_size=0.2):
    return 1 - calculate_percentage_covered(colonies, l, grid_size)

# Radius increases according to the Logistic Growth with Carrying Capacity I and Growth Rate r
def calculate_new_radius(R_0, I, r, t):
    return I * R_0 * np.exp(r * t) / (I + R_0 *(np.exp(r * t) - 1))

# A_0 = controls the value of the maximum antibiotic effectiveness
# A_1 = controls how quickly the antibiotic loses its effectiveness over time
def rayleigh_distribution(t, A_0=1.65, A_1=32):
    return A_0 * t * np.exp(-t ** 2 / A_1)

# theta is the empirical constant provided the certain density of alive population
# m is the maximum value of antibiotic concentration i.e. the maximum of the rayleigh distribution
# for the default A_0 and A_1 the maximum is approximately 4
def calculate_new_radius_with_antibiotics(t, colony, theta=0.2, A_0=1.65, A_1=32):
    m=rayleigh_distribution(math.sqrt(A_1/2), A_0,A_1)
    return colony['radius'] * (1 - theta * rayleigh_distribution(t,A_0, A_1) ** 2 / (rayleigh_distribution(t,A_0,A_1) ** 2 + m))

# Calculation of the total linear size R(t)
def sum_of_radiuses(colonies):
    return sum(colony['radius'] for colony in colonies)

# Calculation of the Generalized Antibiotics vector, GA
def sum_of_antibiotic_effects(A_0=1.65, A_1=32, antibiotic_steps=[10,30], hour_count=60):
    # check that antibiotic_steps is not empty and all antibiotic applications are before than the maximum time
    if (not len(antibiotic_steps)>0 or not all(antibiotic_step <=hour_count for antibiotic_step in antibiotic_steps)):
        return

    sum_of_rayleighs= [0]*(hour_count)
    for i in range (len(antibiotic_steps)):
        rayleigh_values = [0]*antibiotic_steps[i]
        rayleigh_values.extend([rayleigh_distribution(t,A_0,A_1) for t in range(0, hour_count-antibiotic_steps[i])])
        sum_of_rayleighs = np.add(sum_of_rayleighs, rayleigh_values)

    return sum_of_rayleighs

# Calculating new radius with multiple application of antibiotics
def calculate_new_radius_with_antibiotics_generalized(colony, rayleigh_value, A_0, A_1, theta=0.2):
    m = rayleigh_distribution(math.sqrt(A_1 / 2), A_0, A_1)
    return colony['radius'] * (1 - theta * rayleigh_value ** 2 / (rayleigh_value ** 2 + m))

# This function could have been used in another version of the model where we skip the already covered points
# but for some reason is not faster
def calculate_free_points(colonies, grid_size, free_points):
    covered_points = set()
    squared_radius = [(colony['radius']) ** 2 for colony in colonies]  # Precompute squared radius
    for i, j in free_points:
        for index, colony in enumerate(colonies):
            squared_distance = calculate_squared_distance_to_colony(i / grid_size, j / grid_size, colony)
            if squared_distance <= squared_radius[index]:
                covered_points.add((i, j))
                break

    return free_points - covered_points
