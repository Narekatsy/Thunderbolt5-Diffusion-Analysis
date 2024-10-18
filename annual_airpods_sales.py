import numpy as np
import pandas as pd
from scipy.interpolate import make_interp_spline
import matplotlib.pyplot as plt

data = pd.read_csv('data/airpods_sales_data.csv')

years = data['Year'].values
annual_sales = data['Units'].values

years_smooth = np.linspace(years.min(), years.max(), 500)
spline = make_interp_spline(years, annual_sales, k=3)
annual_sales_smooth = spline(years_smooth)

plt.figure(figsize=(10, 6))
plt.plot(years_smooth, annual_sales_smooth, color='lightseagreen', label='Annual Sales (Smoothed)', linewidth=2)
plt.scatter(years, annual_sales, color='teal', marker='o', label='Annual Sales Data', zorder=5)
plt.title('Annual Sales of AirPods (2017-2022)')
plt.xlabel('Year')
plt.ylabel('Annual Sales (millions)')
plt.xticks(years)
plt.legend()
plt.grid()
plt.show()

