import numpy as np
import matplotlib.pyplot as plt

# Produce some data to work with

stock_a = [100, 102, 99, 101, 101, 100, 102]
stock_b = [90, 95, 102, 104, 105, 103, 109]
stock_c = [110, 115, 100, 105, 100, 98, 95]
yLabels = ['Monday', 'Tuesday', 'Wednesday',
           'Thursday', 'Friday', 'Saturday', 'Sunday']

plt.plot(yLabels, stock_a, label='Company 1')
plt.plot(stock_b, label='Company 2')
plt.plot(stock_c, label='Company 3')
plt.title('My Stocks', fontname='Times New Roman', fontsize=20)
plt.legend(loc='lower right')
plt.ylabel('Price in Pounds', fontname='Times New Roman')
plt.xlabel('Closing Price', fontname='Times New Roman')
plt.savefig('../Figures/figure7i_1.png')
plt.show()
