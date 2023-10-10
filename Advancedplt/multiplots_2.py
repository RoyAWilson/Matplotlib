import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style

# Plot multiple charts on page.
# Produce some data

x = np.arange(100)

# grid of four subplots in one figure
fig, axs = plt.subplots(2, 2)

# Describe plot functions and give titles axs arg 1 row then column
axs[0, 0].plot(x, np.sin(x))
axs[0, 0].set_title('Sine Wave')

axs[0, 1].plot(x, np.cos(x))
axs[0, 1].set_title('Cosine Wave')

axs[1, 0].plot(x, np.random.random(100))
axs[1, 0].set_title('Random Function')

axs[1, 1].plot(x, np.log(x))
axs[1, 1].set_title('Log Fumction')
axs[1, 1].set_xlabel('Test')

fig.suptitle('Four Plots')

# plot the data
plt.show()

# and save it
plt.savefig('../Figures/figure11_1_HQ.png', dpi=300)
