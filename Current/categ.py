import numpy as np
import matplotlib.pyplot as plt

# categorical data in bar chart

x = ['C++', 'C#', 'Python', 'Java', 'Go']
y = [20, 50, 140, 1, 45]
plt.bar(x, y, color='Orange', align='edge', width=0.95, edgecolor='Blue', lw=3)
# Not so sure that I like the thicker line - obliterates the lowest value's bar
plt.savefig('../Figures/figure3_2.png')
plt.show()
