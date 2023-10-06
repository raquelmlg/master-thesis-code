# -*- coding: utf-8 -*-
"""
Created on Mon Jun 26 13:32:17 2023

@author: gilor
"""
import random
import common_functions as cf


def simulate_colonies(R_0, I, r, hour_count, model, l=None, showPlots=False):
    # Default value of length if not specified
    if l is None:
        l = 5*I

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
        cf.plot_colonies(colonies,l,0)

    for k in range(hour_count):
        # old colonies have grown
        for colony in colonies:
            colony['age'] = colony['age'] + 1
            colony['radius'] = cf.calculate_new_radius(R_0, I, r, colony['age'])

        # Basic model: In every step the probability of generating one colony is p
        p = 0.1
        # Second and third model: In every step, we take into account the availability of nutrients to 
        # calculate the probability of generating a new colony
        if model == 'model_2' or model == 'model_4':
            p = p * cf.calculate_nutrient_availability(colonies, l)

        if random.random() <= p:
            new_colony = cf.generate_colony(l, R_0, I, colonies,
                                            checkSpaceAvailable=(model == 'model_3' or model == 'model_4'))
            if new_colony is not None:
                colonies.append(new_colony)

        # calculate new density taking into account the growth and the new colonies

        if showPlots:
            cf.plot_colonies(colonies, l,k+1)
            concentration = cf.calculate_bacterial_concentration(colonies)
            concentrations.append(concentration)
            density = cf.calculate_percentage_covered(colonies, l)
            densities.append(density)
            print(f"Step {k + 1}: Density = {density:.4f},  Concentration = {concentration:.4f}")

    if showPlots:
         cf.plot_array(concentrations, 'Concentration')
         cf.plot_array(densities, 'Density')
         cf.plot_growth_colony(hour_count, R_0, I, r)
    return colonies, cf.calculate_bacterial_concentration(colonies), cf.calculate_percentage_covered(colonies, l)


# from datetime import datetime
# time_1 = datetime.now()
# area = simulate_colonies(R_0=1, I=20, r=0.4, hour_count=50, model='model_4', l=5 * 20, showPlots=True)
# time_2 = datetime.now()
# print(time_2-time_1)
