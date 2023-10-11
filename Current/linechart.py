import numpy as np
import matplotlib.pyplot as plt

# produce list of years and weights

years = [2006 + x for x in range(16)]
# print(years)
weight = [80, 83, 84, 85, 86, 82, 81, 79,
          83, 80, 82, 82, 83, 81, 80, 79]

# Default plt function plots line chart so no need to call line

plt.plot(years, weight, c='Blue', lw=3,
         linestyle='--')
plt.savefig('../Figures/figure2_2.png')
plt.show()
