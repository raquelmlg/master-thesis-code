# -*- coding: utf-8 -*-
"""
Created on Tue Jul 11 12:50:20 2023

@author: gilor
"""
import pandas as pd
import math
import models as models
from datetime import datetime


def create_simulations_dataframe(model, M, R_0, I, r, N, l):
    data = {'number_colonies': [],
            'concentrations': [],
            'density': []
            }
    for i in range(0, M):
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

#time1 = datetime.now()
#print(time1)
#data_frame1 = create_simulations_dataframe('model_1', M, R_0, I, r, N, l)
#data_frame2 = create_simulations_dataframe('model_2', M, R_0, I, r, N, l)
#data_frame3 = create_simulations_dataframe('model_3', M, R_0, I, r, N, l)
#time2 = datetime.now()

#print(time2 - time1)
#data_frame3.to_csv("model3-2.csv")
