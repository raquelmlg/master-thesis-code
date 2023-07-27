# -*- coding: utf-8 -*-
"""
Created on Mon Jul 17 13:50:54 2023

@author: gilor
"""
import random
import math
import matplotlib.pyplot as plt
import numpy as np

from datetime import datetime

"""FUNCTIONS TO CALCULATE THE MODELS"""


# Calculate Distance from a point (x,y) to the center of a colony.
def calculate_distance_to_colony(x, y, colony):
    return math.sqrt((colony['center_x'] - x) ** 2 + (colony['center_y'] - y) ** 2)


# Calculate Distance between the centers of two colonies.
def calculate_distance_between_colonies(colony1, colony2):
    return calculate_distance_to_colony(colony1['center_x'], colony1['center_y'], colony2)


# Calculate the area of a colony
def calculate_area(colony):
    return math.pi * colony['radius'] ** 2


# Generate a new colony. If colonies already exist, take into account that new colonies are not generated inside them.
# Colonies can also not be generated in the edge of the domain
# (therefore we generate them between I*math.e and l-I*math.e)
# last, if checkSpaceAvailable = True, we check if the colony has enough space to be generated
def generate_colony(l, R_0, I, old_colonies=[], checkSpaceAvailable=False):
    threshold = 0
    if checkSpaceAvailable:
        threshold = I * math.e / 2  # if checkSpaceAvailable, distance to the closest colony must be bigger than this
    if len(old_colonies) > 0:
        while True:
            center_x = random.uniform(I * math.e, l - I * math.e)
            center_y = random.uniform(I * math.e, l - I * math.e)
            new_colony = {'center_x': center_x, 'center_y': center_y, 'radius': R_0, 'age': 0}
            valid = True
            for colony in old_colonies:
                distance = calculate_distance_between_colonies(new_colony, colony)
                if distance <= colony['radius'] + threshold:
                    valid = False
                    break
            if valid:
                return {'center_x': center_x, 'center_y': center_y, 'radius': R_0, 'age': 0}
            else:
                return None
    else:
        center_x = random.uniform(I * math.e, l - I * math.e)
        center_y = random.uniform(I * math.e, l - I * math.e)
        return {'center_x': center_x, 'center_y': center_y, 'radius': R_0, 'age': 0}


# Calculate the bacterial concentration in our domain (sum of all colonies)
# In this case, we assume that the bacteria can be overlapping, i.e. we count twice whenever two colonies overlap
def calculate_bacterial_concentration(colonies):
    return sum(calculate_area(colony) for colony in colonies)


# Calculate how much of our domain lxl is covered with bacteria numerically.
def calculate_total_covered_area(colonies, l, grid_step=0.1):
    area = 0
    for i in np.arange(0, l, grid_step):
        for j in np.arange(0, l, grid_step):
            for colony in colonies:
                if calculate_distance_to_colony(i, j, colony) <= colony['radius']:
                    area += grid_step ** 2
                    break
    return area

# def calculate_total_covered_area(colonies, l, num_samples=100000):
#     covered_points = 0
#     for _ in range(num_samples):
#         x = np.random.uniform(0, l)
#         y = np.random.uniform(0, l)
#         for colony in colonies:
#             if calculate_distance_to_colony(x, y, colony) <= colony['radius']:
#                 covered_points += 1
#                 break
#     return (covered_points / num_samples) * l ** 2


# Calculate the percentage of the grid that it´s covered by the bacteria
# This can also be a measure for the density of the colonies
# In this case, we assume that bacterial colonies don´t overlap
def calculate_percentage_covered(colonies, l, num_samples=0.1):
    return calculate_total_covered_area(colonies, l, num_samples) / l ** 2


# colony = {'center_x': 10, 'center_y':10, 'radius':10}
# print(10**2*math.pi)
# time1 = datetime.now()
# print(calculate_total_covered_area2([colony], 20))
# time2 = datetime.now()
#
# print(time2-time1)
#
# time1 = datetime.now()
# print(calculate_total_covered_area([colony], l=20))
# time2 = datetime.now()
# print(time2-time1)

# We consider that the nutrients are distributed homogeneously in the medium at the beginning
# so a measure of nutrient availability could be the percentage of the domain which is not covered by colonies
def calculate_nutrient_availability(colonies, l, num_steps=0.1):
    return 1 - calculate_percentage_covered(colonies, l, num_steps)


# Radius increases according to the Logistic Growth with Carrying Capacity I and Growth Rate r
def calculate_new_radius(R_0, I, r, t):
    return I * R_0 * np.exp(r * t) / (I + R_0 * np.exp(r * t - 1))


"""FUNCTIONS TO PLOT THE MODELS"""


def plot_colonies(colonies, l):
    fig, ax = plt.subplots()
    for colony in colonies:
        circle = plt.Circle((colony['center_x'], colony['center_y']), colony['radius'], fill=False, edgecolor='b')
        ax.add_patch(circle)
    ax.set_xlim(0, l)
    ax.set_ylim(0, l)
    ax.set_aspect('equal', adjustable='box')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title('Bacteria Colonies')
    plt.show()


def plot_array(array, title):
    plt.plot(array)
    plt.xlabel('Time in Hours')
    plt.ylabel(title)
    plt.title('Bacterial ' + title + ' Over Time')
    plt.show()


def plot_growth_colony(N, R_0, I, r):
    t = np.linspace(0, N, N, dtype=int)
    y = calculate_new_radius(R_0, I, r, t)
    plt.plot(y)
    plt.xlabel('Time in Hours')
    plt.ylabel('Size')
    plt.title('Colony Radius Over Time')
    plt.show()


""" NOT USEFUL ANYMORE """


# These functions make no real sense cause the intersection could be of three or more colonies.


## TODO: write mathematically  
def calculate_intersection_area(colony1, colony2):
    distance = calculate_distance_between_colonies(colony1, colony2)
    if distance >= colony1['radius'] + colony2['radius']:
        return 0
    elif distance <= abs(colony1['radius'] - colony2['radius']):
        return math.pi * min(colony1['radius'], colony2['radius']) ** 2
    else:
        radius1_sq = colony1['radius'] ** 2
        radius2_sq = colony2['radius'] ** 2
        d = distance
        a = (radius1_sq - radius2_sq + d ** 2) / (2 * d)
        h = math.sqrt(radius1_sq - a ** 2)
        theta1 = math.acos(a / colony1['radius'])
        theta2 = math.acos((d - a) / colony2['radius'])
        intersection_area = (theta1 * radius1_sq - h * a) + (theta2 * radius2_sq - h * (d - a))
        return intersection_area


# makes no real sense cause the intersection could be of three or more colonies.
def calculate_bacterial_density(colonies, l):
    total_concentration = calculate_bacterial_concentration(colonies)
    intersection_area = 0
    for i in range(len(colonies)):
        for j in range(i + 1, len(colonies)):
            intersection_area += calculate_intersection_area(colonies[i], colonies[j])

    density = total_concentration / (l ** 2 + intersection_area)
    return density


def is_colony_inside_square(colony, l):
    # Check if the circle's center is within the boundaries of the square
    radius = colony['radius']
    if (colony['center_x'] - radius >= 0 and colony['center_x'] + radius <= l and
            colony['center_y'] - radius >= 0 and colony['center_y'] + radius <= l):
        return True
    return False
