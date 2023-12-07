#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt

x = np.arange(0, 28651, 5730)

# Define decay parameters
r = np.log(0.5)  # Decay rate
t = 5730         # Half-life of the decaying substance

# Calculate y values using the decay formula
y = np.exp((r / t) * x)

plt.semilogy(x, y, color='blue')

# Labeling the axes and title of the plot
plt.xlabel('Time (years)')
plt.ylabel('Fraction Remaining')
plt.title('Exponential Decay of C-14')

# Setting x-axis range
plt.xlim(0, 28650)

# Display the plot
plt.show()
