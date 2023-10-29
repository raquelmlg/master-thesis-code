import random
import numpy as np

import common_functions as cf
import plot_functions as pf


# Simulate the growth of bacterial colonies in a square domain with an application of antibiotics and no bacterial regrowth.
#
# Parameters:
# R_0: Initial radius of bacterial colonies.
# I: Carrying capacity, representing the limit for the colonies'radius.
# r: Growth rate, determining how fast colonies grow.
# A_0: Affects the maximum antibiotic effectiveness
# A_1: Affects the duration of the antibiotic effectiveness
# hour_count: Total number of hours for the simulation.
# antibiotic_steps: time steps at which the antibiotics are added
# l: Length of the square domain (default is 5*I, to at least have enough space for the generation).
# showPlots: Set to True to display plots, False when creating dataframes.

# Model 3 is used

# seed = 1411 was used for the comparison of the models with and without antibiotics in the
# Chapter: Modeling Antibiotic effects

def simulate_colonies(R_0, I, r, A_0,A_1, hour_count=50, antibiotic_steps=[10,30,35],  l=None, showPlots=False):
    random.seed(1411)
    #prove that antibiotic_steps is not empty and all antibiotic steps are less than the maximum time
    if (not len(antibiotic_steps)>0 or not all(antibiotic_step <=hour_count for antibiotic_step in antibiotic_steps)):
        return

    # Default value of length if not specified
    if l is None:
        l = 5*I

    colonies = []
    concentrations = []
    densities = []
    sum_of_radiuses = []

    # On the first step we generate 1-3 colonies with the following probabilities
    probabilities = [0.6, 0.3, 0.1]
    initial_num_colonies = random.choices(range(1, 4), probabilities)[0]

    # generate initial colonies
    for _ in range(initial_num_colonies):
        colony = cf.generate_colony(l, R_0, I)
        colonies.append(colony)

    # calculate initial concentration / density
    if showPlots:
        density = cf.calculate_bacterial_density(colonies, l)
        densities.append(density)
        concentration = cf.calculate_bacterial_concentration(colonies)
        concentrations.append(concentration)
        sum_of_radiuses.append(cf.sum_of_radiuses(colonies))
        pf.plot_colonies(colonies,l,0)

    sum_of_rayleighs = cf.sum_of_antibiotic_effects(A_0,A_1,antibiotic_steps,hour_count)

    for k in range(hour_count):
        if(sum_of_rayleighs[k] <= 0.05):
            steps_without_antibiotics(colonies,concentrations, densities,sum_of_radiuses, R_0, I, r,l,k, showPlots)
        else:
            steps_with_antibiotics(colonies,concentrations, densities,sum_of_radiuses, l,k, A_0,A_1, sum_of_rayleighs[k], showPlots)
            possible_ages = np.linspace(0, 50, 50, dtype=int)
            possible_radius_values = cf.calculate_new_radius(R_0, I, r, possible_ages)
            for colony in colonies:
                colony['age']=np.abs(possible_radius_values - colony['radius']).argmin()

    if showPlots:
         pf.plot_array(concentrations, 'Concentration')
         pf.plot_array(densities, 'Density')
         pf.plot_array(sum_of_radiuses, "Total Linear Size")
    return colonies, cf.calculate_bacterial_concentration(colonies), cf.calculate_bacterial_density(colonies, l), sum_of_radiuses


def steps_without_antibiotics(colonies,concentrations, densities,sum_of_radiuses, R_0, I, r,l,k, showPlots):
    # old colonies have grown
    for i, colony in enumerate(colonies):
        colony['age'] = colony['age'] + 1
        colony['radius'] = cf.calculate_new_radius(R_0, I, r, colony['age'])
        # Third model: In every step the probability of generating one colony is p
    p = 0.1
    if random.random() <= p:
        new_colony = cf.generate_colony(l, R_0, I, colonies, checkSpaceAvailable=True)
        if new_colony is not None:
             colonies.append(new_colony)

    # calculate new density taking into account the growth and the new colonies
    if showPlots:
        pf.plot_colonies(colonies, l, k + 1)
        concentration = cf.calculate_bacterial_concentration(colonies)
        concentrations.append(concentration)
        density = cf.calculate_bacterial_density(colonies, l)
        densities.append(density)
        sum_of_radiuses.append(cf.sum_of_radiuses(colonies))
        print(f"Step without antibiotics{k + 1}: Density = {density:.4f},  Concentration = {concentration:.4f}")

def steps_with_antibiotics(colonies,concentrations, densities,sum_of_radiuses, l,k, A_0,A_1, rayleigh_value, showPlots):
    # old colonies have schrunk
    for colony in colonies:
        colony['age'] = colony['age'] + 1
        colony['radius'] = cf.calculate_new_radius_with_antibiotics_generalized(colony, rayleigh_value, A_0, A_1, 0.2)
        if (colony['radius'] < 1):
            colonies.remove(colony)

    # calculate new density taking into account the growth and the new colonies
    if showPlots:
        pf.plot_colonies(colonies, l, k)
        concentration = cf.calculate_bacterial_concentration(colonies)
        concentrations.append(concentration)
        density = cf.calculate_bacterial_density(colonies, l)
        densities.append(density)
        sum_of_radiuses.append(cf.sum_of_radiuses(colonies))
        print(f"Step with antibiotics {k + 1}: Density = {density:.4f},  Concentration = {concentration:.4f}")

results = simulate_colonies(R_0=1, I=20, r=0.4, hour_count=50, antibiotic_steps=[10, 20], l=5 * 20, showPlots=True, A_0=1.65,A_1=32)

