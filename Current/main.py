import numpy as np
import matplotlib.pyplot as plt

# Use numpy to produce some example data

x_data = np.random.random(1000) * 100
y_data = np.random.random(1000) * 100

# Scatter Plots:

z_plot = plt.scatter(x=x_data, y=y_data, c='Green',
                     marker='*', s=150, alpha=0.3)
plt.savefig('../Figures/figure1_2Try.png')
plt.show()
