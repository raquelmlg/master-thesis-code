# -*- coding: utf-8 -*-
"""
Created on Mon Jul 17 10:17:43 2023

@author: gilor
"""

from scipy.stats import ttest_ind
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

model_1 = pd.read_csv("Dataframes/first_try/mmodel1-1-5m.csv")
model_2 = pd.read_csv("Dataframes/first_try/mmodel2-1_1h-19-29.767445.csv")
model_3 = pd.read_csv("Dataframes/first_try/mmodel3-1-1h-18m.csv")


# Calculate mean and standard deviation for each model
mean_colonies = [model_1['number_colonies'].mean(), model_2['number_colonies'].mean(), model_3['number_colonies'].mean()]
std_colonies = [model_1['number_colonies'].std(), model_2['number_colonies'].std(), model_3['number_colonies'].std()]

mean_concentration = [model_1['concentrations'].mean(), model_2['concentrations'].mean(), model_3['concentrations'].mean()]
std_concentration = [model_1['concentrations'].std(), model_2['concentrations'].std(), model_3['concentrations'].std()]

mean_density = [model_1['density'].mean(), model_2['density'].mean(), model_3['density'].mean()]
std_density = [model_1['density'].std(), model_2['density'].std(), model_3['density'].std()]

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
t_statistic, p_value = ttest_ind(model_1['number_colonies'], model_2['number_colonies'], equal_var=False)
print("Model 1 vs Model 2 - t-statistic:", t_statistic)
print("Model 1 vs Model 2 - p-value:", p_value)

# Perform t-test between Model 1 and Model 3
t_statistic, p_value = ttest_ind(model_1['number_colonies'], model_3['number_colonies'], equal_var=False)
print("Model 1 vs Model 3 - t-statistic:", t_statistic)
print("Model 1 vs Model 3 - p-value:", p_value)

# Perform t-test between Model 2 and Model 3
t_statistic, p_value = ttest_ind(model_2['number_colonies'], model_3['number_colonies'], equal_var=False)
print("Model 2 vs Model 3 - t-statistic:", t_statistic)
print("Model 2 vs Model 3 - p-value:", p_value)

print("T-Test Density")

# Perform t-test between Model 1 and Model 2
t_statistic, p_value = ttest_ind(model_1['density'], model_2['density'], equal_var=False)
print("Model 1 vs Model 2 - t-statistic:", t_statistic)
print("Model 1 vs Model 2 - p-value:", p_value)

# Perform t-test between Model 1 and Model 3
t_statistic, p_value = ttest_ind(model_1['density'], model_3['density'], equal_var=False)
print("Model 1 vs Model 3 - t-statistic:", t_statistic)
print("Model 1 vs Model 3 - p-value:", p_value)

# Perform t-test between Model 2 and Model 3
t_statistic, p_value = ttest_ind(model_2['density'], model_3['density'], equal_var=False)
print("Model 2 vs Model 3 - t-statistic:", t_statistic)
print("Model 2 vs Model 3 - p-value:", p_value)


## Perform t-test to see whether the diference in concentration is significant
print("T-Test Concentration")

# Perform t-test between Model 1 and Model 2
t_statistic, p_value = ttest_ind(model_1['concentrations'], model_2['concentrations'], equal_var=False)
print("Model 1 vs Model 2 - t-statistic:", t_statistic)
print("Model 1 vs Model 2 - p-value:", p_value)

# Perform t-test between Model 1 and Model 3
t_statistic, p_value = ttest_ind(model_1['concentrations'], model_3['concentrations'], equal_var=False)
print("Model 1 vs Model 3 - t-statistic:", t_statistic)
print("Model 1 vs Model 3 - p-value:", p_value)

# Perform t-test between Model 2 and Model 3
t_statistic, p_value = ttest_ind(model_2['concentrations'], model_3['concentrations'], equal_var=False)
print("Model 2 vs Model 3 - t-statistic:", t_statistic)
print("Model 2 vs Model 3 - p-value:", p_value)