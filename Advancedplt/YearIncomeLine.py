import numpy as np
import matplotlib.pyplot as plt

# Line plot with ticks.

years = [2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021]

income = [55, 56, 62, 61, 72, 72, 73, 75]

income_ticks = list(range(50, 81, 2))

plt.plot(years, income)
plt.show()
plt.savefig('../Figures/figure7_1.png')
