import matplotlib.pyplot as plt
import numpy as np

# Generate x values representing time in years
x = np.arange(0, 21001, 1000)

# Define decay parameters for C-14 and Ra-226
r = np.log(0.5)   # Decay rate
t1 = 5730         # Half-life of C-14
t2 = 1600         # Half-life of Ra-226

# Calculate y values using the decay formula for C-14 and Ra-226
y1 = np.exp((r / t1) * x)
y2 = np.exp((r / t2) * x)

# Plotting the exponential decay curves with dashed red and solid green lines
plt.plot(x, y1, '--r', label='C-14')
plt.plot(x, y2, '-g', label='Ra-226')

# Labeling the axes and title of the plot
plt.xlabel('Time (years)')
plt.ylabel('Fraction Remaining')
plt.title('Exponential Decay of Radioactive Elements')

# Setting x-axis and y-axis ranges
plt.xlim(0, 20000)
plt.ylim(0, 1)

# Adding legend in the upper right hand corner
plt.legend(loc='upper right')

# Display the plot
plt.show()
