# -*- coding: utf-8 -*-
"""
Created on Mon Jul 17 10:17:43 2023

@author: gilor
"""

from create_dataframes import data_frame1, data_frame2, data_frame3
from scipy.stats import ttest_ind
import numpy as np
import matplotlib.pyplot as plt

# Calculate mean and standard deviation for each model
mean_colonies = [data_frame1['number_colonies'].mean(), data_frame2['number_colonies'].mean(), data_frame3['number_colonies'].mean()]
std_colonies = [data_frame1['number_colonies'].std(), data_frame2['number_colonies'].std(), data_frame3['number_colonies'].std()]

mean_concentration = [data_frame1['concentrations'].mean(), data_frame2['concentrations'].mean(), data_frame3['concentrations'].mean()]
std_concentration = [data_frame1['concentrations'].std(), data_frame2['concentrations'].std(), data_frame3['concentrations'].std()]

mean_density = [data_frame1['density'].mean(), data_frame2['density'].mean(), data_frame3['density'].mean()]
std_density = [data_frame1['density'].std(), data_frame2['density'].std(), data_frame3['density'].std()]

# Bar plot for comparing the number of colonies
models = ['Model 1', 'Model 2', 'Model 3']
x_pos = np.arange(len(models))
plt.bar(x_pos, mean_colonies, yerr=std_colonies, align='center', alpha=0.5)
plt.xticks(x_pos, models)
plt.ylabel('Number of Colonies')
plt.title('Comparison of Final Number of Colonies')
plt.show()

# Bar plot for comparing concentration
plt.bar(x_pos, mean_concentration, yerr=std_concentration, align='center', alpha=0.5)
plt.xticks(x_pos, models)
plt.ylabel('Concentration')
plt.title('Comparison of Final Concentration')
plt.show()

# Bar plot for comparing density
plt.bar(x_pos, mean_density, yerr=std_density, align='center', alpha=0.5)
plt.xticks(x_pos, models)
plt.ylabel('Density')
plt.title('Comparison of Final Density')
plt.show()



## Perform t-test to see whether the diference in number of colonies is significant

# If the p-value is below a chosen significance level (e.g., 0.05), 
# we can reject the null hypothesis and conclude
# that the difference in means is statistically significant.


## Perform t-test to see whether the diference in density is significant

print("T-Test Number of Colonies")
# Perform t-test between Model 1 and Model 2
t_statistic, p_value = ttest_ind(data_frame1['number_colonies'], data_frame2['number_colonies'], equal_var=False)
print("Model 1 vs Model 2 - t-statistic:", t_statistic)
print("Model 1 vs Model 2 - p-value:", p_value)

# Perform t-test between Model 1 and Model 3
t_statistic, p_value = ttest_ind(data_frame1['number_colonies'], data_frame3['number_colonies'], equal_var=False)
print("Model 1 vs Model 3 - t-statistic:", t_statistic)
print("Model 1 vs Model 3 - p-value:", p_value)

# Perform t-test between Model 2 and Model 3
t_statistic, p_value = ttest_ind(data_frame2['number_colonies'], data_frame3['number_colonies'], equal_var=False)
print("Model 2 vs Model 3 - t-statistic:", t_statistic)
print("Model 2 vs Model 3 - p-value:", p_value)

print("T-Test Density")

# Perform t-test between Model 1 and Model 2
t_statistic, p_value = ttest_ind(data_frame1['density'], data_frame2['density'], equal_var=False)
print("Model 1 vs Model 2 - t-statistic:", t_statistic)
print("Model 1 vs Model 2 - p-value:", p_value)

# Perform t-test between Model 1 and Model 3
t_statistic, p_value = ttest_ind(data_frame1['density'], data_frame3['density'], equal_var=False)
print("Model 1 vs Model 3 - t-statistic:", t_statistic)
print("Model 1 vs Model 3 - p-value:", p_value)

# Perform t-test between Model 2 and Model 3
t_statistic, p_value = ttest_ind(data_frame2['density'], data_frame3['density'], equal_var=False)
print("Model 2 vs Model 3 - t-statistic:", t_statistic)
print("Model 2 vs Model 3 - p-value:", p_value)


## Perform t-test to see whether the diference in concentration is significant
print("T-Test Concentration")

# Perform t-test between Model 1 and Model 2
t_statistic, p_value = ttest_ind(data_frame1['concentrations'], data_frame2['concentrations'], equal_var=False)
print("Model 1 vs Model 2 - t-statistic:", t_statistic)
print("Model 1 vs Model 2 - p-value:", p_value)

# Perform t-test between Model 1 and Model 3
t_statistic, p_value = ttest_ind(data_frame1['concentrations'], data_frame3['concentrations'], equal_var=False)
print("Model 1 vs Model 3 - t-statistic:", t_statistic)
print("Model 1 vs Model 3 - p-value:", p_value)

# Perform t-test between Model 2 and Model 3
t_statistic, p_value = ttest_ind(data_frame2['concentrations'], data_frame3['concentrations'], equal_var=False)
print("Model 2 vs Model 3 - t-statistic:", t_statistic)
print("Model 2 vs Model 3 - p-value:", p_value)