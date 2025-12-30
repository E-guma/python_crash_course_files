import matplotlib.pyplot as plt

# List of points pos
x_values = list(range(1001))
y_values= [x**2 for x in x_values]

plt.scatter(x_values, y_values, s=10, c=y_values, cmap=plt.cm.viridis, edgecolors='none')

# Set chart title and label axes.
plt.title("Square Numbers", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square of Value", fontsize=14)
# Set size of tick labels.
plt.tick_params(axis='both', which='major', labelsize=14)

# Set the range for each axis.
plt.axis([0, 1100, 0, 1100000])

plt.savefig('squares_plot.png', bbox_inches='tight')
plt.show()