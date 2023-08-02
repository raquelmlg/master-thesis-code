import pandas as pd
import multiprocessing
import models

if __name__ == "__main__":
    multiprocessing.set_start_method("spawn")
def single_run(model, R_0, I, r, N, grid_size, l):
    return models.simulate_colonies(R_0, I, r, N, model,grid_size, l)

num_runs=100
model = "model_1"
R_0 = 1
I = 20
r= 0.4
N=20
grid_size= 5
l=4*20*3
args_list = [(model, R_0, I, r, N, grid_size, l)]*num_runs

pool = multiprocessing.Pool(processes=multiprocessing.cpu_count())

results = pool.map(single_run,args_list)
pool.close()
pool.join()

df = pd.DataFrame(results, columns=['Number Colonies', 'Concentration', 'Density'])
df.to_csv('dataframe')
