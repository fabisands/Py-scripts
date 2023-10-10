# Graph a phosphate group

import matplotlib.pyplot as plt
from matplotlib.patches import Circle

# Create a figure and axes
fig, ax = plt.subplots()

# Define circles radius
H_radius = (1 * 1) / 25 # Periodic table: group 1, period 1
O_radius = H_radius * ((6 * 2) / 5) # Periodic table: group 6, period 2
P_radius = H_radius * ((5 * 3) / 5) # Periodic table: group 5, period 3

# Draw and add black circumferences
center_circumference = Circle((0.500, 0.500), P_radius, fill=False, color='black', lw=2) # Phosphate
ax.add_patch(center_circumference)
above_circumference = Circle((0.500, 0.725), O_radius, fill=False, color='black', lw=2) # Oxygen
ax.add_patch(above_circumference)
below_circumference = Circle((0.500, 0.275), O_radius, fill=False, color='black', lw=2) # Oxygen
ax.add_patch(below_circumference)
below_below_circumference = Circle((0.500, 0.130), H_radius, fill=False, color='black', lw=2) # Hydrogen
ax.add_patch(below_below_circumference)
left_circumference = Circle((0.275, 0.500), O_radius, fill=False, color='black', lw=2) # Oxygen
ax.add_patch(left_circumference)
left_left_circumference = Circle((0.130, 0.500), H_radius, fill=False, color='black', lw=2) # Hydrogen
ax.add_patch(left_left_circumference)
right_circumference = Circle((0.725, 0.500), O_radius, fill=False, color='black', lw=2) # Oxygen
ax.add_patch(right_circumference)

# Draw and add circles in the center, above, below, left, and right
center_circle = plt.Circle((0.500, 0.500), P_radius, fill=True, color='Yellow', lw=2) # Phosphate
ax.add_patch(center_circle)
above_circle = plt.Circle((0.500, 0.725), O_radius, fill=True, color='cyan', lw=2) # Oxygen
ax.add_patch(above_circle)
below_circle = plt.Circle((0.500, 0.275), O_radius, fill=True, color='cyan', lw=2) # Oxygen
ax.add_patch(below_circle)
below_below_circle = plt.Circle((0.500, 0.130), H_radius, fill=True, color='gray', lw=2) # Hydrogen
ax.add_patch(below_below_circle)
left_circle = plt.Circle((0.275, 0.500), O_radius, fill=True, color='cyan', lw=2) # Oxygen
ax.add_patch(left_circle)
left_left_circle = plt.Circle((0.1305, 0.500), H_radius, fill=True, color='gray', lw=2) # Hydrogen
ax.add_patch(left_left_circle)
right_circle = plt.Circle((0.725, 0.500), O_radius, fill=True, color='cyan', lw=2) # Oxygen
ax.add_patch(right_circle)

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
