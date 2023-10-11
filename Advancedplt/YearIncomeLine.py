import numpy as np
import matplotlib.pyplot as plt

# Line plot with ticks.

years = [2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021]

income = [55, 56, 62, 61, 72, 72, 73, 75]
# tick ranges from 50 to 81 a little below and above the data range.
income_ticks = list(range(50, 81, 2))

plt.plot(years, income)
plt.title('Income of John in Pounds Sterling',
          fontsize=25, fontname='Times New Roman')
plt.xlabel('Year', fontname='Times New Roman')
plt.ylabel('Income in Pounds Sterling', fontname='Times New Roman')
# list comprehension loop through all ticks and produce f'string for ticks on y axi
plt.yticks(income_ticks, [
           f'£{x}K  UK' for x in income_ticks], fontname='Times New Roman')
plt.savefig('../Figures/figure7_3.png')
plt.show()
