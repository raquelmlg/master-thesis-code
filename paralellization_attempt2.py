# -*- coding: utf-8 -*-
"""
Created on Tue Jul 11 12:50:20 2023

@author: gilor
"""
import pandas as pd
import math
import models as models
from datetime import datetime
from concurrent.futures import ThreadPoolExecutor

def create_simulations_dataframe(model, M, R_0, I, r, N, l):
    data = {'number_colonies': [],
            'concentrations': [],
            'density': []
            }
    for i in range(0, M):
        print(str(i) + model)
        colonies, final_concentration, final_density = models.simulate_colonies(R_0, I, r, N, model, l)
        data['number_colonies'].append(len(colonies))
        data['concentrations'].append(final_concentration)
        data['density'].append(final_density)
    return pd.DataFrame(data)

M = 100
R_0 = 1  # Initial radius of colonies
I = 20  # Carrying capacity parameter
r = 0.4  # Growth rate parameter
N = 20  # number of iterations
l = 4 * I * math.e  # Length of the domain

time1 = datetime.now()

# Create a ThreadPoolExecutor
with ThreadPoolExecutor() as executor:
    # Use submit to start each function call asynchronously and get the result later
    future1 = executor.submit(create_simulations_dataframe, 'model_1', M, R_0, I, r, N, l)
    future2 = executor.submit(create_simulations_dataframe, 'model_2', M, R_0, I, r, N, l)
    future3 = executor.submit(create_simulations_dataframe, 'model_3', M, R_0, I, r, N, l)

# Get the results from the futures
data_frame1 = future1.result()
data_frame2 = future2.result()
data_frame3 = future3.result()

time2 = datetime.now()
print(time2 - time1)

data_frame1.to_csv("dataframes/2/model1.csv")
data_frame3.to_csv("dataframes/2/model2.csv")
data_frame3.to_csv("dataframes/2/model3.csv")
