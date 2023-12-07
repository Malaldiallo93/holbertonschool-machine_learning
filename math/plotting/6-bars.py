import numpy as np
import matplotlib.pyplot as plt

# Set random seed for reproducibility
np.random.seed(5)

# Define the fruit matrix
fruit = np.random.randint(0, 20, (4, 3))

# Define colors for each fruit
colors = ['red', 'yellow', '#ff8000', '#ffe5b4']

# Define labels for each person
persons = ['Farrah', 'Fred', 'Felicia']

# Plot the stacked bar graph
bottom = np.zeros(3)

for i in range(4):
    plt.bar(
        persons,
        fruit[i],
        bottom=bottom,
        color=colors[i],
        label=['Apples', 'Bananas', 'Oranges', 'Peaches'][i],
        width=0.5
    )
    bottom += fruit[i]

# Customize the plot
plt.xlabel('Person')
plt.ylabel('Quantity of Fruit')
plt.title('Number of Fruit per Person')
plt.legend()
plt.ylim(0, 80)
plt.yticks(np.arange(0, 81, 10))

# Display the plot
plt.show()
