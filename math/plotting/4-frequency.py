import matplotlib.pyplot as plt
import numpy as np

np.random.seed(5)

# Generate random student grades using a normal distribution
student_grades = np.random.normal(68, 15, 50)

# Plotting a histogram of student scores
plt.hist(student_grades, bins=np.arange(0, 101, 10), edgecolor='black')

# Labeling the axes and title of the plot
plt.xlabel('Grades')
plt.ylabel('Number of Students')
plt.title('Project A')

# Display the plot
plt.show()
