import numpy as np
import matplotlib.pyplot as plt

# Histogram
# Use numpy to produce a normal distribution of number

# Argument 1 mean value, arg 2 standard deviation, arg 3 items
ages = np.random.normal(20, 1.5, 1000)

# Plot and show histogram
plt.hist(ages)
plt.show()

# save the figure
plt.savefig('../Figures/figure4_1.png')
