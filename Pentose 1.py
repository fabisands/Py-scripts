import matplotlib.pyplot as plt
import numpy as np

# Define the coordinates of the vertices of the pentagon
x = [0.5 + 0.4 * np.cos(2 * np.pi * i / 5) for i in range(5)]
y = [0.5 + 0.4 * np.sin(2 * np.pi * i / 5) for i in range(5)]

# Create a figure and axes
fig, ax = plt.subplots()

# Plot the pentagon and fill it with the same color as the lines
plt.fill(x + [x[0]], y + [y[0]], color='blue', edgecolor='blue', lw=2)

# Set axis limits and equal aspect ratio
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.set_aspect('equal', adjustable='box')

# Remove axis labels
ax.axis('off')

# Show the plot
plt.show()

# Save the plot as an image to your PC
# plt.savefig('Pentose.png', dpi=300, bbox_inches='tight')

# Close the plot window
plt.close()
