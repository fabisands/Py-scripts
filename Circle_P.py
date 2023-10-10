import matplotlib.pyplot as plt
from matplotlib.patches import Circle

# Create a figure and axes
fig, ax = plt.subplots()

# Draw a black circumference
circle_outer = Circle((0.5, 0.5), 0.45, fill=False, color='black', lw=2)
ax.add_patch(circle_outer)

# Draw a white circle with a smaller radius to eliminate white space
circle_inner = Circle((0.5, 0.5), 0.44, fill=True, color='yellow', edgecolor='black', lw=2)
ax.add_patch(circle_inner)

# Add the letter "P"
ax.text(0.5, 0.5, "P", color='black', fontsize=100, ha='center', va='center')

# Set axis limits and equal aspect ratio
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.set_aspect('equal', adjustable='box')

# Remove axis labels
ax.axis('off')

# Show the plot
plt.show()

# Close the plot window
plt.close()
