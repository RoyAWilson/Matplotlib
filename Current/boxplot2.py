import numpy as np
import matplotlib.pyplot as plt

# Box plot second example.
# Create some data to work with.  Give some extreme values.

first = np.linspace(0, 10, 25)
second = np.linspace(10, 200, 25)
third = np.linspace(200, 210, 25)
fourth = np.linspace(210, 230, 25)
fifth = np.linspace(300, 250, 25)

data = np.concatenate((first, second, third, fourth, fifth))
plt.boxplot(data)
plt.show()
# give weird results if add a second dataset
plt.savefig('../Figures/figure6_3.png')
