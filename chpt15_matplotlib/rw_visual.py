import matplotlib.pyplot as plt

from random_walk import RandomWalk

while True:
    # Create and plot random walk
    rw = RandomWalk(50000)
    # Set the size of the plotting window.
    plt.figure(dpi=120, figsize=(8, 5))
    
    npoints = list(range(rw.npoints))
    plt.scatter(rw.x_pos, rw.y_pos, s=2, c=npoints, cmap=plt.cm.Blues, edgecolors='none')
    # Emphasize the first and last points.
    plt.scatter(0, 0, c='green', s=100, edgecolors='none')
    plt.scatter(rw.x_pos[-1], rw.y_pos[-1], c='red', s=100, edgecolors='none')
    # Remove the axes.
    plt.axis('off')

    plt.show()
    
    break
    keep_running = input("Would you liken to generate another walk? (y/n): ")
    if keep_running.lower() == 'n':
        break

