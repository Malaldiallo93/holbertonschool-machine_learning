import matplotlib.pyplot as plt
import numpy as np

np.random.seed(5)

# Generate data for the plots
y0 = np.arange(0, 11) ** 3

mean = [69, 0]
cov = [[15, 8], [8, 15]]
x1, y1 = np.random.multivariate_normal(mean, cov, 2000).T
y1 += 180

x2 = np.arange(0, 28651, 5730)
r2 = np.log(0.5)
t2 = 5730
y2 = np.exp((r2 / t2) * x2)

x3 = np.arange(0, 21000, 1000)
r3 = np.log(0.5)
t31 = 5730
t32 = 1600
y31 = np.exp((r3 / t31) * x3)
y32 = np.exp((r3 / t32) * x3)

student_grades = np.random.normal(68, 15, 50)

np.random.seed(5)

# Plot 1
plt.subplot(3, 2, 1)
y = np.arange(0, 11) ** 3
plt.plot(y, color='red')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Line Graph of y = x^3')

# Plot 2
plt.subplot(3, 2, 2)
mean = [69, 0]
cov = [[15, 8], [8, 15]]
x, y = np.random.multivariate_normal(mean, cov, 2000).T
y += 180
plt.scatter(x, y, color='magenta')
plt.xlabel('Height (in)')
plt.ylabel('Weight (lbs)')
plt.title("Men's Height vs Weight")

# Plot 3
plt.subplot(3, 2, 4)
x = np.arange(0, 28651, 5730)
r = np.log(0.5)
t = 5730
y = np.exp((r / t) * x)
plt.semilogy(x, y, color='blue')
plt.xlabel('Time (years)')
plt.ylabel('Fraction Remaining')
plt.title('Exponential Decay of C-14')
plt.xlim(0, 28650)

# Plot 4
plt.subplot(3, 2, 5)
x = np.arange(0, 21001, 1000)
r = np.log(0.5)
t1 = 5730
t2 = 1600
y1 = np.exp((r / t1) * x)
y2 = np.exp((r / t2) * x)
plt.plot(x, y1, '--r', label='C-14')
plt.plot(x, y2, '-g', label='Ra-226')
plt.xlabel('Time (years)')
plt.ylabel('Fraction Remaining')
plt.title('Exponential Decay of Radioactive Elements')
plt.xlim(0, 20000)
plt.ylim(0, 1)
plt.legend(loc='upper right')

# Plot 5
plt.subplot(3, 2, 6)
student_grades = np.random.normal(68, 15, 50)
plt.hist(student_grades, bins=np.arange(0, 101, 10), edgecolor='black')
plt.xlabel('Grades')
plt.ylabel('Number of Students')
plt.title('Project A')

# Adjust layout for better visualization
plt.tight_layout()

# Title of the entire figure
plt.suptitle('All in One', fontsize='x-small')

# Display the plots
plt.show()
