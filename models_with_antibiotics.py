# -*- coding: utf-8 -*-
"""
Created on Mon Jun 26 13:32:17 2023

@author: gilor
"""
import random
import math
import common_functions as cf


def simulate_colonies(R_0, I, r, N, model, antibiotic_step=10, l=None, showPlots=False):
    # Default value of length if not specified
    if l is None:
        l = 4 * math.e * I

    colonies = []
    concentrations = []
    densities = []

    # On the first step we generate 1-3 colonies with the following probabilities
    probabilities = [0.6, 0.3, 0.1]
    initial_num_colonies = random.choices(range(1, 4), probabilities)[0]

    # generate initial colonies
    for _ in range(initial_num_colonies):
        colony = cf.generate_colony(l, R_0, I)
        colonies.append(colony)

    # calculate initial concentration / density
    if showPlots:
        density = cf.calculate_percentage_covered(colonies, l)
        densities.append(density)
        concentration = cf.calculate_bacterial_concentration(colonies)
        concentrations.append(concentration)

    for k in range(antibiotic_step):
        print(k)
        # old colonies have grown
        for colony in colonies:
            colony['age'] = colony['age'] + 1
            colony['radius'] = cf.calculate_new_radius(R_0, I, r, colony['age'])

        # Basic model: In every step the probability of generating one colony is p
        p = 0.1
        # Second and third model: In every step, we take into account the availability of nutrients to 
        # calculate the probability of generating a new colony
        if model == 'model_2' or model == 'model_3':
            p = p * cf.calculate_nutrient_availability(colonies, l)

        if random.random() <= p:
            new_colony = cf.generate_colony(l, R_0, I, colonies, checkSpaceAvailable=(model == 'model_3'))
            if new_colony is not None:
                colonies.append(new_colony)

        # calculate new density taking into account the growth and the new colonies

        if showPlots:
            concentration = cf.calculate_bacterial_concentration(colonies)
            concentrations.append(concentration)
            density = cf.calculate_percentage_covered(colonies, l)
            densities.append(density)
            print(f"Step without A {k + 1}: Density = {density:.4f},  Concentration = {concentration:.4f}")
            cf.plot_colonies(colonies, l)

    for k in range(antibiotic_step, N):
        # old colonies have grown
        for colony in colonies:
            colony['age'] = colony['age'] + 1
            colony['radius'] = cf.calculate_new_radius_with_antibiotics(N-k,colony)

        # Basic model: In every step the probability of generating one colony is p
        p = 0.1
        # Second and third model: In every step, we take into account the availability of nutrients to
        # calculate the probability of generating a new colony

        ## TODO: in the antibiotics steps no new colonies are generated!
        if model == 'model_2' or model == 'model_3':
            p = p * cf.calculate_nutrient_availability(colonies, l)

        if random.random() <= p:
            new_colony = cf.generate_colony(l, R_0, I, colonies, checkSpaceAvailable=(model == 'model_3'))
            if new_colony is not None:
                colonies.append(new_colony)

        # calculate new density taking into account the growth and the new colonies

        if showPlots:
            concentration = cf.calculate_bacterial_concentration(colonies)
            concentrations.append(concentration)
            density = cf.calculate_percentage_covered(colonies, l)
            densities.append(density)
            print(f"Step with A {k + 1}: Density = {density:.4f},  Concentration = {concentration:.4f}")
            cf.plot_colonies(colonies, l)

    if showPlots:
        cf.plot_array(concentrations, 'Concentration')
        cf.plot_array(densities, 'Density')
        cf.plot_growth_colony(N, R_0, I, r)
    return colonies, cf.calculate_bacterial_concentration(colonies), cf.calculate_percentage_covered(colonies, l)

from datetime import datetime
time_1 = datetime.now()
area = simulate_colonies(1, 20, 0.4, 20, 'model_1',10, 4 * 20 * 2, showPlots=True)
time_2 = datetime.now()
print(time_2-time_1)
