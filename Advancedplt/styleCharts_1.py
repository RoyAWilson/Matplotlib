'''`

Stylesheet gallery link: https://matplotlib.org/stable/gallery/style_sheets/style_sheets_reference.html
Styleshhet customisation link: https://matplotlib.org/stable/users/explain/customizing.html

'''

import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style

# More advanced pie chart with style

# Generate some data:

votes = [10, 2, 5, 16, 22]
people = ['A', 'B', 'C', 'D', 'E']

# set the style
# style.use('ggplot')
style.use('dark_background')

explodes = [0, 0.15, 0, 0.15, 0]
plt.pie(votes, labels=None, explode=explodes,
        autopct='%.2f%%', pctdistance=0.9)
plt.legend(people, loc='upper left')
plt.title('Votes', fontsize=15, fontname='Times New Roman')
plt.savefig('../Figures/figure9_2.png')
plt.show()
