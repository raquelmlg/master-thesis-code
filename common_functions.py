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

# Calculate (Squared) Distance from a point (x,y) to the center of a colony.
def calculate_squared_distance_to_colony(x, y, colony):
    return (colony['center_x'] - x) ** 2 + (colony['center_y'] - y) ** 2

# Calculate (Squared) Distance between the centers of two colonies.
def calculate_squared_distance_between_colonies(colony1, colony2):
    return calculate_squared_distance_to_colony(colony1['center_x'], colony1['center_y'], colony2)

# Calculate the area of a colony
def calculate_area(colony):
    return math.pi * colony['radius'] ** 2

def create_new_colony(I,l,R_0):
    h=I * math.e
    center_x = random.uniform(h, l - h)
    center_y = random.uniform(h, l - h)
    return {'center_x': center_x, 'center_y': center_y, 'radius': R_0, 'age': 0}

# Generate a new colony. If colonies already exist, take into account that new colonies are not generated inside them.
# Colonies can also not be generated in the edge of the domain
# (therefore we generate them between I*math.e and l-I*math.e)
# last, if checkSpaceAvailable = True, we check if the colony has enough space to be generated
def generate_colony(l, R_0, I, old_colonies=[], checkSpaceAvailable=False):
    threshold = 0
    new_colony = None
    if checkSpaceAvailable:
        threshold = I * math.e / 2
        # if checkSpaceAvailable, distance to the closest colony must be bigger than this #
        # (otherwise, threshold == 0 but to ensure they are still) not inside each other, we check the distance is <= colony + R_0
    if len(old_colonies) > 0:
        max_iterations = 0
        valid = False
        while not valid and max_iterations < 10:
            new_colony = create_new_colony(I,l,R_0)
            valid = True
            for colony in old_colonies:
                distance = calculate_squared_distance_between_colonies(new_colony, colony)
                # function all() could also be used to check that all conditions in a loop are True (but apparantly is not faster)
                if distance <= (colony['radius'] + R_0 + threshold)**2:
                    valid = False
                    break
            max_iterations += 1
        return new_colony
    else:
        return create_new_colony(I,l,R_0)


# Calculate the bacterial concentration in our domain (sum of all colonies)
# In this case, we assume that the bacteria can be overlapping, i.e. we count twice whenever two colonies overlap
def calculate_bacterial_concentration(colonies):
    return sum(calculate_area(colony) for colony in colonies)

# Calculate how much of our domain lxl is covered with bacteria numerically.
def calculate_total_covered_area(colonies, l, grid_step=0.2):
    area = 0
    step_addition = grid_step**2
    for i in np.arange(0, l, grid_step):
        for j in np.arange(0, l, grid_step):
            for colony in colonies:
                if calculate_squared_distance_to_colony(i, j, colony) <= colony['radius']**2:
                    area += step_addition
                    break # the grid point is already covered by at least one colony, so we can move on to the next grid point.
    return area

# Calculate the percentage of the grid that it´s covered by the bacteria
# This can also be a measure for the density of the colonies
# In this case, we assume that bacterial colonies don´t overlap
def calculate_percentage_covered(colonies, l,grid_size=0.2):
    area = calculate_total_covered_area(colonies, l, grid_size)
    return area / (l ** 2)

# We consider that the nutrients are distributed homogeneously in the medium at the beginning
# so a measure of nutrient availability could be the percentage of the domain which is not covered by colonies
def calculate_nutrient_availability(colonies, l, grid_size=0.2):
    return 1 - calculate_percentage_covered(colonies, l,grid_size)


# Radius increases according to the Logistic Growth with Carrying Capacity I and Growth Rate r
def calculate_new_radius(R_0, I, r, t):
    return I * R_0 * np.exp(r * t) / (I + R_0 * np.exp(r * t - 1))

# Radius increases slower due to Antibiotics
# TODO: define the parameters meanings for A_0, A_1, theta and m (next function)
def rayleigh_distribution(t, A_0=1.65, A_1=32):
    return A_0*t*np.exp(-t**2/A_1)

#theta is the empirical constant provided the certain density of alive population
# m is the maximum value of antibiotic concentration i.e. the maximum of the rayleigh distribution
# for the default A_0 and A_1 the maximum is approximately 4
def calculate_new_radius_with_antibiotics(t,colony,theta=0.2, m=4):
    return colony['radius']*(1-theta*rayleigh_distribution(t)**2/(rayleigh_distribution(t)**2 + m))


## This function could have been use in another version of the model where we skip the already covered points
# but for some rwason is not faster
def calculate_free_points(colonies, grid_size, free_points):
    covered_points = set()
    squared_radius = [(colony['radius'])**2 for colony in colonies]  # Precompute squared radius
    for i,j in free_points:
            for index, colony in enumerate(colonies):
                squared_distance = calculate_squared_distance_to_colony(i/grid_size, j/grid_size, colony)
                if squared_distance <= squared_radius[index]:
                    covered_points.add((i,j))
                    break

    return free_points-covered_points


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

## This was a plot to check if my v2 of the models (slower) was working, but it´s not necessary
def plot_covered_points(covered_points, l, grid_size=10):
    grid_x = list(range(0, l * grid_size + 1))
    grid_y = list(range(0, l * grid_size + 1))

    # Create a meshgrid of all grid points
    X, Y = np.meshgrid(grid_x, grid_y)

    # Flatten the meshgrid and remove covered points
    X_flat = X.flatten()
    Y_flat = Y.flatten()
    not_covered = [(x, y) for x, y in zip(X_flat, Y_flat) if (x, y) not in covered_points]

    # Separate covered and not covered points
    covered_x, covered_y = zip(*covered_points)
    not_covered_x, not_covered_y = zip(*not_covered)

    # Plot the covered points and not covered points
    plt.scatter(covered_x, covered_y, color='red', label='Covered')
    plt.scatter(not_covered_x, not_covered_y, color='blue', label='Not Covered')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title('Covered Points')
    plt.legend()
    plt.grid(True)
    plt.show()

def plot_rayleigh_distribution():
    t_values = np.linspace(0, 100, 500)
    y_values = rayleigh_distribution(t_values)
    plt.plot(t_values, y_values, label='Rayleigh Distribution')
    plt.xlabel('t')
    plt.ylabel('Probability Density')
    plt.title('Rayleigh Distribution')
    plt.legend()
    plt.grid(True)
    plt.show()