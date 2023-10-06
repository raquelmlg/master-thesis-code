# -*- coding: utf-8 -*-
"""
Created on Mon Jul 17 10:17:43 2023

@author: gilor
"""

from scipy.stats import ttest_ind
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


def selectVersion(version):
    model_1 = pd.read_csv("dataframes/" + str(version) + "/model1.csv")
    model_2 = pd.read_csv("dataframes/"+ str(version)+ "/model2.csv")
    model_3 = pd.read_csv("dataframes/"+ str(version)+ "/model3.csv")
    model_4= pd.read_csv("dataframes/"+ str(version)+ "/model4.csv")
    return model_1, model_2, model_3, model_4

model_1, model_2, model_3, model_4 = selectVersion("1")


# Calculate mean and standard deviation for each model
mean_colonies = [model_1['number_colonies'].mean(), model_2['number_colonies'].mean(), model_3['number_colonies'].mean(), model_4['number_colonies'].mean()]
std_colonies = [model_1['number_colonies'].std(), model_2['number_colonies'].std(), model_3['number_colonies'].std(), model_4['number_colonies'].std()]

mean_concentration = [model_1['concentrations'].mean(), model_2['concentrations'].mean(), model_3['concentrations'].mean(), model_4['concentrations'].mean()]
std_concentration = [model_1['concentrations'].std(), model_2['concentrations'].std(), model_3['concentrations'].std(), model_4['concentrations'].std()]

mean_density = [model_1['density'].mean(), model_2['density'].mean(), model_3['density'].mean(), model_4['density'].mean()]
std_density = [model_1['density'].std(), model_2['density'].std(), model_3['density'].std(), model_4['density'].std()]

mean_time = [model_1['running_time'].mean(), model_2['running_time'].mean(), model_3['running_time'].mean(), model_4['running_time'].mean()]
std_time = [model_1['running_time'].std(), model_2['running_time'].std(), model_3['running_time'].std(), model_4['running_time'].std()]


# Bar plot for comparing the number of colonies
models = ['Model 1', 'Model 2', 'Model 3', 'Model 4']
x_pos = np.arange(len(models))
plt.bar(x_pos, mean_colonies, yerr=std_colonies, align='center', alpha=0.7, capsize=3, width=0.7)
plt.xticks(x_pos, models)
plt.ylabel('Number of Colonies')
plt.title('Comparison of Final Number of Colonies')
plt.show()

# Bar plot for comparing concentration
plt.bar(x_pos, mean_concentration, yerr=std_concentration, align='center', alpha=0.7, capsize=3, width=0.7)
plt.xticks(x_pos, models)
plt.ylabel('Concentration')
plt.title('Comparison of Final Concentration')
plt.show()

# Bar plot for comparing density
plt.bar(x_pos, mean_density, yerr=std_density, align='center', alpha=0.7, capsize=3, width=0.7)
plt.xticks(x_pos, models)
plt.ylabel('Density')
plt.title('Comparison of Final Density')
plt.show()

# Bar plot for comparing running_time
plt.bar(x_pos, mean_time, yerr=std_time, align='center', alpha=0.7, capsize=3, width=0.7)
plt.xticks(x_pos, models)
plt.ylabel('Runnning Time (Seconds)')
plt.title('Comparison of Running Time in Seconds')
plt.show()


mean_time = [model_1['running_time'].mean(), model_3['running_time'].mean()]
std_time = [model_1['running_time'].std(), model_3['running_time'].std()]

# Bar plot for comparing running_time
plt.bar(np.arange(2), mean_time, yerr=std_time, align='center', alpha=0.7, capsize=3, width=0.7)
plt.xticks(np.arange(2), ['Model 1', 'Model_3'])
plt.ylabel('Runnning Time (Seconds)')
plt.title('Comparison of Running Time in Seconds')
plt.show()


## Perform t-test to see whether the diference in number of colonies is significant

# If the p-value is below a chosen significance level (e.g., 0.05), 
# we can reject the null hypothesis and conclude
# that the difference in means is statistically significant.


def perform_t_tests(models, column_names):
    for column_name in column_names:
        print(f"T-Test for {column_name}")
        for i in range(len(models)):
            for j in range(i + 1, len(models)):
                model1 = models[i]
                model2 = models[j]
                t_statistic, p_value = ttest_ind(model1[column_name], model2[column_name], equal_var=False)
              #  print(f"Model {i + 1} vs Model {j + 1} - t-statistic:", t_statistic)
                print(f"Model {i + 1} vs Model {j + 1} - p-value:", p_value)
                
perform_t_tests([model_1,model_2,model_3,model_4], ['density','concentrations','running_time','number_colonies'])


# # Create subplots for each model
# fig, ax = plt.subplots(figsize=(10, 6))
#
# # Define the number of bins for the histograms
# num_bins = 10  # You can adjust this as needed
#
# # Create histograms for each model and plot them as grouped bars
# for i, data in enumerate([model_1['number_colonies'],model_2['number_colonies'],
#                           model_3['number_colonies'],model_4['number_colonies']]):
#     ax.hist(data, bins=num_bins, alpha=0.5, label=models[i])
#
# # Customize the plot
# plt.xlabel('Variable Values')
# plt.ylabel('Frequency')
# plt.title('Distribution of Variable in Three Models')
# plt.legend()
# plt.grid(True)
#
# # Show the plot
# plt.show()
