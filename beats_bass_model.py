import numpy as np
import matplotlib.pyplot as plt

p = 0.0381
q = 0.6433
M = 250

def simulate_beats_adoption(p, q, M, time_periods):
    N = [0]
    for t in range(time_periods):
        new_adopters = p * (M - N[t]) + q * (N[t] / M) * (M - N[t])
        N.append(N[t] + new_adopters)
    return N

time_periods = 10
adoption = simulate_beats_adoption(p, q, M, time_periods)

plt.figure(figsize=(10, 6))
plt.plot(range(time_periods + 1), adoption, marker='o', color='orangered', label='Cumulative Adopters')
plt.title('Projected Adoption of Beats Studio Buds+')
plt.xlabel('Years')
plt.ylabel('Cumulative Adopters (in millions)')
plt.xticks(range(time_periods + 1))
plt.grid()
plt.legend()
plt.show()
