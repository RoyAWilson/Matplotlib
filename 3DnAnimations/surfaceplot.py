import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style

# produce 3d Line chart

ax = plt.axes(projection='3d')

# Produce values
x = np.arange(-5, 5, 0.1)
y = np.arange(-5, 5, 0.1)

# set up the mesh grid
X, Y = np.meshgrid(x, y)
Z = np.sin(X) * np.cos(Y)


ax.plot_surface(X, Y, Z, cmap='Spectral')
ax.set_xlabel('X Value')
ax.set_ylabel('Y Value')
ax.set_zlabel('Sin of X * Cos of Y')
ax.set_title('3D Surface Plot')
# To change default view of the chart - can still rotate it
ax.view_init(azim=0, elev=25)
plt.show()

# POlots in 3d and can rotate the plot by dragging

plt.savefig('../Figures/figure14_1_HQ.png', dpi=300)
