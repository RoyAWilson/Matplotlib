import numpy as np
import matplotlib.pyplot as plt

# Box Plot

# Generate some data for plotting
# arg 1 = mean. arg 2 = standard distribution, arg 3 = number of points
heights = np.random.normal(172, 8, 300)

# Plot it
plt.boxplot(heights)
plt.savefig('../Figures/figure6_2.png')
plt.show()
