import numpy as np
import matplotlib.pyplot as plt

# Histogram
# Use numpy to produce a normal distribution of number

# Argument 1 mean value, arg 2 standard deviation, arg 3 items
ages = np.random.normal(20, 2.5, 1000)

# Plot and show histogram
# plt.hist(ages, bins=20, color='green', )

# Another way to change bins:
# plt.hist(ages, bins=[2, 4, 6, 8, 10, 12, 14, 16,
#          18, 20, 22, 24, 26, 28, 30], color='green')

# plot cumulative distribution

plt.hist(ages, bins=20, cumulative=True)
plt.savefig('../Figures/figure4_4.png')
plt.show()

# save the figure
