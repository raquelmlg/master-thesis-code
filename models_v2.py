# -*- coding: utf-8 -*-
"""
Created on Mon Jun 26 13:32:17 2023

@author: gilor
"""
import random
import common_functions as cf
import numpy as np


def simulate_colonies(R_0, I, r, N, grid_size, model, l=None, showPlots=False):
    # Default value of length if not specified
    if l is None:
        l = 4 * 3 * I # 3 ~= math.e
    colonies = []
    concentrations = []
    densities = []
    covered_area = 0.
    step_area = 1 / (grid_size) ** 2

    # create the grid
    grid_x = np.arange(1, int(l * grid_size) + 1)
    grid_y = np.arange(1, int(l * grid_size) + 1)
    free_points = set((x, y) for x in grid_x for y in grid_y)
    total_points= len(free_points)

    # On the first step we generate 1-3 colonies with the following probabilities
    probabilities = [0.6, 0.3, 0.1]
    initial_num_colonies = random.choices(range(1, 4), probabilities)[0]

    # generate initial colonies
    for _ in range(initial_num_colonies):
        colony = cf.generate_colony(l, R_0, I)
        colonies.append(colony)

    # calculate initial concentration / density
    if showPlots:
        free_points = cf.calculate_free_points(colonies, grid_size, free_points)
        covered_area = step_area*(total_points-len(free_points))
        density = covered_area/l**2
        densities.append(density)
        concentration = cf.calculate_bacterial_concentration(colonies)
        concentrations.append(concentration)

    for k in range(N):
        # old colonies have grown
        for colony in colonies:
            colony['age'] = colony['age'] + 1
            colony['radius'] = cf.calculate_new_radius(R_0, I, r, colony['age'])

        # Basic model: In every step the probability of generating one colony is p
        p = 0.1
        # Second and third model: In every step, we take into account the availability of nutrients to
        # calculate the probability of generating a new colony
        if model == 'model_2' or model == 'model_3':
            free_points = cf.calculate_free_points(colonies, grid_size, free_points)
            covered_area = (total_points-len(free_points))*step_area
            p = p * (1-covered_area/l**2)

        if random.random() <= p:
            new_colony = cf.generate_colony(l, R_0, I, colonies, checkSpaceAvailable=(model == 'model_3'))
            if new_colony is not None:
                colonies.append(new_colony)

        # calculate new density taking into account the growth and the new colonies

        if showPlots:
           # density = cf.calculate_percentage_covered(colonies, l,covered_points)
            concentration = cf.calculate_bacterial_concentration(colonies)
            concentrations.append(concentration)
            densities.append(covered_area/l**2)
            print(f"Step {k + 1}: Density = {density:.4f},  Concentration = {concentration:.4f}")
            cf.plot_colonies(colonies, l)

    if showPlots:
        cf.plot_array(concentrations, 'Concentration')
        cf.plot_array(densities, 'Density')
        cf.plot_growth_colony(N, R_0, I, r)

    return colonies, cf.calculate_bacterial_concentration(colonies), covered_area/l**2


#from datetime import datetime
#time_1 = datetime.now()
#colonies, concentration, density = simulate_colonies(1, 20, 0.4, 20, 5, 'model_2', 4 * 20 * 2, showPlots=False)
#print(density)
#time_2 = datetime.now()
#print(time_2-time_1)
