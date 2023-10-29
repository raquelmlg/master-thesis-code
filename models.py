import random
import common_functions as cf
import plot_functions as pf


# Simulate the growth of bacterial colonies in a square domain.
#
# Parameters:
# R_0: Initial radius of bacterial colonies.
# I: Carrying capacity, representing the limit for the colonies'radius.
# r: Growth rate, determining how fast colonies grow.
# hour_count: Total number of hours for the simulation.
# model (string): selecting model_1, model_2, model_3, model_4
# l: Length of the square domain (default is 5*I, to at least have enough space for the generation).
# showPlots: Set to True to display plots, False when creating dataframes.

# seed = 1411 was used for the comparison of the models with and without antibiotics in the
# Chapter: Modeling Antibiotic effects
def simulate_colonies(R_0, I, r, hour_count, model, l=None, showPlots=False):
    # random.seed(1411)

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
        pf.plot_colonies(colonies,l,0)
        sum_of_radiuses.append(cf.sum_of_radiuses(colonies))

    for k in range(hour_count):
        # old colonies have grown
        for colony in colonies:
            colony['age'] = colony['age'] + 1
            colony['radius'] = cf.calculate_new_radius(R_0, I, r, colony['age'])

        # Basic model: In every step the probability of generating one colony is p
        p = 0.1
        # Second and fourth model: In every step, we take into account the availability of nutrients to
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
            pf.plot_colonies(colonies, l,k+1)
            concentration = cf.calculate_bacterial_concentration(colonies)
            concentrations.append(concentration)
            density = cf.calculate_bacterial_density(colonies, l)
            densities.append(density)
            sum_of_radiuses.append(cf.sum_of_radiuses(colonies))
            print(f"Step {k + 1}: Density = {density:.4f},  Concentration = {concentration:.4f}")

    if showPlots:
         pf.plot_array(concentrations, 'Concentration')
         pf.plot_array(densities, 'Density')
         pf.plot_array(sum_of_radiuses, "Total Linear Size")

    return colonies, cf.calculate_bacterial_concentration(colonies), cf.calculate_bacterial_density(colonies, l)

# Uncomment and adapt the parameters to generate the simulations
#result = simulate_colonies(R_0=1, I=20, r=0.4, hour_count=40, model='model_3', l=100, showPlots=True)

