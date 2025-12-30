import matplotlib.pyplot as plt

# Ordinates lists
x_values = list(range(5001))
y_values = [x**3 for x in x_values]

# Set plot title and label axis
plt.title("Cube of Numbers", fontsize=24)
plt.xlabel("Values", fontsize=14)
plt.ylabel("Cubes", fontsize=14)
plt.tick_params(axis='both', labelsize=14)
# Create plot
plt.scatter(x_values, y_values, c=y_values, cmap=plt.cm.viridis)


# Set axis range
# plt.axis([0,6,0,130])

plt.show()

