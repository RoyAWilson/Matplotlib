import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style
import random

# Animate random coin flip

heads_tails = [0, 0]

for _ in range(100000):
    heads_tails[random.randint(0, 1)] += 1
    # plot the results as a bar plot
    plt.bar(['heads', 'tails'], heads_tails, color=['Red', 'Blue'])
    plt.pause(0.001)
plt.show()

# Do not run, can't break out even with control C
