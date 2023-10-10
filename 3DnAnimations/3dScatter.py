import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style

# produce 3d scatter chart

ax = plt.axes(projection='3d')

x = np.random.random(100)
y = np.random.random(100)
z = np.random.random(100)

ax.scatter(x, y, z)

ax.set_title('3D Scatter Plot')
plt.show()

# POlots in 3d and can rotate the plot by dragging

plt.savefig('../Figures/figure12_1_HQ.png', dpi=300)
