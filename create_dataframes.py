# -*- coding: utf-8 -*-
"""
Created on Tue Jul 11 12:50:20 2023

@author: gilor
"""
import pandas as pd
import models as models
from datetime import datetime


def create_simulations_dataframe(model, M, R_0, I, r, N, l):
    time1 = datetime.now()
    print(time1)

    data = {'number_colonies': [],
            'concentrations': [],
            'density': [],
            'running_time': []
            }
    for i in range(0, M):
        print(model,i)
        start_time = datetime.now()
        colonies, final_concentration, final_density = models.simulate_colonies(R_0, I, r, N, model, l)
        end_time = datetime.now()
        data['number_colonies'].append(len(colonies))
        data['concentrations'].append(final_concentration)
        data['density'].append(final_density)
        data['running_time'].append((end_time-start_time).total_seconds())
    
    time2 = datetime.now()
    print(model, time2 - time1)
    
    return pd.DataFrame(data)


M = 200
R_0 = 1  # Initial radius of colonies
I = 20  # Carrying capacity parameter
r = 0.4  # Growth rate parameter
N = 50  # number of iterations
l = 5 * I  # Length of the domain

time1 = datetime.now()
print(time1)
data_frame1 = create_simulations_dataframe('model_1', M, R_0, I, r, N, l)
data_frame2 = create_simulations_dataframe('model_2', M, R_0, I, r, N, l)
data_frame3 = create_simulations_dataframe('model_3', M, R_0, I, r, N, l)
data_frame4 = create_simulations_dataframe('model_4', M, R_0, I, r, N, l)
time2 = datetime.now()
print(time2 - time1)

data_frame1.to_csv("dataframes/4/model1.csv")   
data_frame2.to_csv("dataframes/4/model2.csv")   
data_frame3.to_csv("dataframes/4/model3.csv")   
data_frame4.to_csv("dataframes/4/model4.csv")   
