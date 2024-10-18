import pandas as pd
import numpy as np
from scipy.optimize import minimize

data = pd.read_csv('data/airpods_sales_data.csv')

years = data['Year'].values
annual_sales = data['Units'].values
cumulative_sales = np.cumsum(annual_sales)

M = 350

def bass_discrete_model(params):
    p, q = params
    N = [0]
    for t in range(len(annual_sales)):
        new_adopters = p * (M - N[t]) + q * (N[t] / M) * (M - N[t])
        N.append(N[t] + new_adopters)
    return N[1:]

def objective_function(params):
    N_pred = bass_discrete_model(params)
    return np.sum((N_pred - cumulative_sales)**2)


initial_guess = [0.02, 0.1]
result = minimize(objective_function, initial_guess, bounds=((0, 1), (0, 1)))
p, q = result.x

print(f"Estimated parameters: p = {p:.4f}, q = {q:.4f}, M = {M}")