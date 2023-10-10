import numpy as np
import matplotlib.pyplot as plt

# Use numpy to produce some example data

x_data = np.random.random(50) * 100
y_data = np.random.random(50) * 100

# Scatter Plots:

plt.scatter(x=x_data, y=y_data)
plt.show()
