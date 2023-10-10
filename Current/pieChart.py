import numpy as np
import matplotlib.pyplot as plt

# Pie Chart
# Produce some data as lists for example

langs = ['Python', 'C++', 'C#', 'Java', 'Go']
votes = [50, 24, 14, 6, 17]

# Plot it
explodes = [0, 0.1, 0, 0.2, 0]
plt.pie(votes, labels=langs, explode=explodes,
        autopct='%.2f%%', pctdistance=0.75, startangle=90)
plt.show()

# Save it
plt.savefig('../Figures/figure5_2.png')
