import numpy as np
import matplotlib.pyplot as plt
# More advanced pie chart

# Generate some data:

votes = [10, 2, 5, 16, 22]
people = ['A', 'B', 'C', 'D', 'E']

# Plot it

explodes = [0, 0.15, 0, 0.15, 0]
plt.pie(votes, labels=None, explode=explodes,
        autopct='%.2f%%', pctdistance=0.9)
plt.legend(people, loc='upper left')
plt.title('Votes', fontsize=15, fontname='Times New Roman')
plt.savefig('../Figures/figure8_1.png')
plt.show()
