import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style

# produce 3d Line chart

ax = plt.axes(projection='3d')

x = np.arange(0, 50, 0.1)
y = np.arange(0, 50, 0.1)
z = np.cos(x + y)

ax.plot(x, y, z)
ax.set_xlabel('X Value')
ax.set_ylabel('Y Value')
ax.set_zlabel('Cosine of X + Y')
ax.set_title('3D Line Plot')
plt.show()

# POlots in 3d and can rotate the plot by dragging

plt.savefig('../Figures/figure13_2_HQ.png', dpi=300)
