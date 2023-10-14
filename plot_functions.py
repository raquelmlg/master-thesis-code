"""FUNCTIONS TO PLOT THE MODELS"""
import matplotlib.pyplot as plt
import common_functions as cf
import numpy as np
import math



"""FUNCTIONS TO PLOT THE MODELS"""

def plot_colonies(colonies, l, t):
    fig, ax = plt.subplots()
    for colony in colonies:
        circle = plt.Circle((colony['center_x'], colony['center_y']), colony['radius'],
                            fill=True,edgecolor='#1f77b4', linewidth=2,facecolor=(31./255, 119./255, 180./255,0.3))
        ax.add_patch(circle)
    ax.set_xlim(0, l)
    ax.set_ylim(0, l)
    ax.set_aspect('equal', adjustable='box')
    plt.xlabel('X', fontsize=14)
    plt.ylabel('Y', fontsize=14)
    plt.title('Bacteria Colonies at t =' + str(t), fontsize=16)
    plt.show()

def plot_array(array, title):
    plt.plot(array)
    plt.xlabel('Time in Hours', fontsize = 14)
    plt.ylabel(title, fontsize = 14)
    plt.title('Bacterial ' + title + ' Over Time', fontsize = 16)
    plt.show()

def plot_radius_growth(N, R_0, I, r):
    t = np.linspace(0, N, N, dtype=int)
    y = cf.calculate_new_radius(R_0, I, r, t)
    plt.plot(y)
    plt.xlabel('Time in Hours')
    plt.ylabel('Size')
    plt.title('Colony Radius Over Time')
    plt.show()

def plot_rayleigh_distribution(A_0=1.65,A_1=32):
    t_values = np.linspace(0, 24, 100)
    y1_values = cf.rayleigh_distribution(t_values, A_0, A_1)
    plt.plot(t_values, y1_values, label='$A_0=$'+ str(A_0) +', $A_1=$' + str(A_1))
    plt.xlabel('t', fontsize = 14)
    plt.ylabel('Probability Density', fontsize = 14)
    plt.title('Rayleigh Distribution', fontsize = 16)
    plt.legend(fontsize=12)
    plt.grid(False)
    plt.show()

def radius_adjustment_function(t, theta=0.2, A_0=1.65, A_1=32):
    m = cf.rayleigh_distribution(math.sqrt(A_1/2))
    return (1 - theta * cf.rayleigh_distribution(t,A_0,A_1) ** 2 / (cf.rayleigh_distribution(t,A_0,A_1) ** 2 + m))

def plot_adjustment_function(A_0=1.65, A_1=32):
    t_values = np.linspace(0, 24, 100)
    y1_values = radius_adjustment_function(t_values, A_0, A_1)
    plt.plot(t_values, y1_values, label='$A_0=$'+ str(A_0) +', $A_1=$' + str(A_1))
    plt.ylim(0.6,1.4)
    plt.xlabel('t', fontsize = 14)
    plt.ylabel('Adjustment Rate', fontsize = 14)
    plt.title('Radius Adjustment Rate Function', fontsize = 16)
    plt.legend(fontsize=12)
    plt.grid(False)
    plt.show()

##############################################################################################
# This was a plot to check if my v2 of the models (slower) was working, but it´s not necessary
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