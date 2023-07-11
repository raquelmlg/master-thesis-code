import random
import math
import matplotlib.pyplot as plt
import numpy as np

# -*- coding: utf-8 -*-
"""
Created on Mon Jun 26 13:32:17 2023

@author: gilor

## Taking into account the availability of nutrients for the generation of new colonies.
## We weight the probability of generating a new colony by the space/nutrients available, 
taking into account the position of the new colony (its distance to the closest colonies)
"""

def calculate_distance_between_colonies(colony1, colony2):
    return math.sqrt((colony1['center_x'] - colony2['center_x'])**2 + (colony1['center_y'] - colony2['center_y'])**2)

def calculate_distance_to_colony(x,y,colony):
    return math.sqrt((colony['center_x'] - x)**2 + (colony['center_y'] - y)**2)
    
def generate_colony(l, R_0, I, isColonyInsideColonyAllowed = True, old_colonies=[]):
    threshold = I*math.e/2 # distance to closest colony must be  bigger than this
    if (not isColonyInsideColonyAllowed and len(old_colonies)>0):
        while True:
            center_x = random.uniform(I*math.e, l-I*math.e)
            center_y = random.uniform(I*math.e, l-I*math.e)
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
        center_x = random.uniform(I*math.e, l-I*math.e)
        center_y = random.uniform(I*math.e, l-I*math.e)
        return {'center_x': center_x, 'center_y': center_y, 'radius': R_0, 'age': 0}

def calculate_area(colony):
    return math.pi * colony['radius']**2

def calculate_total_covered_area(colonies, l, grid_length=0.1):
    area=0
    for i in np.arange(0,l,grid_length):
        for j in np.arange(0,l,grid_length):
            for colony in colonies:
               if (calculate_distance_to_colony(i, j, colony)<=colony['radius']):
                   area += grid_length**2
                   break
    return area

def calculate_percentage_covered(colonies,l, grid_length=10):
    return calculate_total_covered_area(colonies, l, grid_length)/l**2
            
## TODO: write mathematically
def calculate_intersection_area(colony1, colony2):
    distance = calculate_distance_between_colonies(colony1, colony2)
    if distance >= colony1['radius'] + colony2['radius']:
        return 0
    elif distance <= abs(colony1['radius'] - colony2['radius']):
        return math.pi * min(colony1['radius'], colony2['radius'])**2
    else:
        radius1_sq = colony1['radius']**2
        radius2_sq = colony2['radius']**2
        d = distance
        a = (radius1_sq - radius2_sq + d**2) / (2 * d)
        h = math.sqrt(radius1_sq - a**2)
        theta1 = math.acos(a / colony1['radius'])
        theta2 = math.acos((d - a) / colony2['radius'])
        intersection_area = (theta1 * radius1_sq - h * a) + (theta2 * radius2_sq - h * (d - a))
        return intersection_area
    
def calculate_bacterial_concentration(colonies):
    return sum(calculate_area(colony) for colony in colonies)

def calculate_bacterial_density(colonies):
    total_concentration = calculate_bacterial_concentration(colonies)
    intersection_area=0
    for i in range(len(colonies)):
        for j in range(i + 1, len(colonies)):
            intersection_area += calculate_intersection_area(colonies[i], colonies[j])

    density = total_concentration / (l**2 + intersection_area)
    return density

def calculate_new_radius(R_0, I, r, t): # Logistic Growth with Carrying Capacity I and Growth Rate r
    return I*R_0*np.exp(r*t)/(I+R_0*np.exp(r*t - 1))


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
    plt.title('Bacterial '+ title + ' Over Time')
    plt.show()

def plot_growth_colony(N, R_0, I, r):
    t = np.linspace(0, N, N, dtype=int)
    y = calculate_new_radius(R_0, I, r, t)
    plt.plot(y)
    plt.xlabel('Time in Hours')
    plt.ylabel('Size')
    plt.title('Colony Radius Over Time')
    plt.show()

def simulate_colonies(R_0,I,r,N,isColonyInsideColonyAllowed=False,l=None):
    
    # Default value of length
    if l is None: 
        l=4*math.e*I
        
    colonies = []
    concentrations = []
    densities = []
    probabilities = [0.6, 0.3, 0.1]
    num_colonies = random.choices(range(1, 4), probabilities)[0]

    # generate initial colonies
    for _ in range(num_colonies):
        colony = generate_colony(l, R_0, I,isColonyInsideColonyAllowed)
        colonies.append(colony) 
    
    # calculate initial concentration / density
    density = calculate_bacterial_density(colonies)
    densities.append(density)
    concentration = calculate_bacterial_concentration(colonies)
    concentrations.append(concentration)

    for k in range(N):
        # old colonies have grown
        for colony in colonies:
            colony['age'] = colony['age'] + 1
            colony['radius'] = calculate_new_radius(R_0, I, r, colony['age'])
          
        
        # generate new colony with probability 0.1*weighted available space
        if random.random() <= 0.1*(1-calculate_percentage_covered(colonies, l)):
            new_colony = generate_colony(l, R_0,I,isColonyInsideColonyAllowed, colonies)
            colonies.append(new_colony)
   
        # calculate new density taking into account the growth and the new colonies
        density = calculate_bacterial_density(colonies)
        densities.append(density)
        concentration = calculate_bacterial_concentration(colonies)
        concentrations.append(concentration)

        print(f"Step {k + 1}: Density = {density:.4f}, Concentration = {concentration:.4f}")
        plot_colonies(colonies, l)
    
    plot_array(concentrations, 'Concentration')
    plot_array(densities, 'Density')
    plot_growth_colony(N, R_0, I, r)

R_0 = 1  # Initial radius of colonies
I = 20 # Carrying capacity parameter
r = 0.4  # Growth rate parameter
N = 20 # number of iterations
l = 4*I*math.e  # Length of the domain

simulate_colonies(R_0, I, r, N, False, l)

# l=20
# colony = {'center_x': 10, 'center_y': 10, 'radius': 10, 'age': 0}
# colony2 = {'center_x': 2.5, 'center_y': 2.5, 'radius': 2, 'age': 0}

# print(calculate_area(colony))
# print(calculate_percentage_covered([colony,colony2], l))
# print(calculate_bacterial_concentration([colony,colony2])- calculate_intersection_area(colony, colony2))