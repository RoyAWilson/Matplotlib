import numpy as np
import matplotlib.pyplot as plt

# Pie Chart
# Produce some data as lists for example

langs = ['Python', 'C++', 'C#', 'Java', 'Go']
votes = [50, 24, 14, 6, 17]

# Plot it
plt.pie(votes, labels=langs)
plt.show()

# Save it
plt.savefig('../Figures/figure5_1.png')
