# -*- coding: utf-8 -*-
"""
Created on Fri Apr 12 15:35:03 2024

@author: mmanc
"""
# =============================================================================
# Black hole diagrams
# =============================================================================

import numpy as np
import matplotlib.pyplot as plt

# static black hole

radius = 2  # Radius of the circle
center = (0, 0)  # Center of the circle
num_points = 100  # Number of points to sample for plotting

# Create theta values for sampling points
theta = np.linspace(0, 2 * np.pi, num_points)

# Calculate x and y coordinates of the circle
x = center[0] + radius * np.cos(theta)
y = center[1] + radius * np.sin(theta)

liney = [0, 2*np.sin(np.pi/3)]
linex = [0, 2*np.cos(np.pi/3)]
# Plot the circle
plt.figure(figsize=(8, 8))
plt.fill(x, y, color='black', alpha = 0.5, label = 'Schwarzschild Black hole')  # Fill the circle with a light blue color
plt.plot(x, y, color='red', label = 'Event horizon' )  # Plot the circle outline
plt.plot(linex, liney, color = 'black', label = 'Schwarzschild radius')
plt.scatter(0, 0, label = 'Singularity', color = 'black')
plt.text(0.5,0.5, 'Schwarzchild radius')
plt.text(-0.2,-0.2, 'Singularity')
plt.text(2.1, 0, 'Event horizon', color = 'red')
plt.axis('off')
plt.title('Static (uncharged) balck hole')
plt.axis('equal')  # Ensure aspect ratio is equal
#plt.legend(loc='upper right', bbox_to_anchor=(1.1, 1)) 
plt.show()
#%%

# spinning black hole
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.patches import PathPatch, Polygon
from matplotlib.path import Path

# Parameters
center = (0, 0)  # Center of the ellipse
width = 4  # Width of the ellipse
height = 2  # Height of the ellipse
angle = 0  # Rotation angle of the ellipse (in degrees)


# Create plot
inner_horizon = patches.Ellipse(center, width, height, angle=angle, color='lightgray', alpha = 0.6)
outer_horizon = patches.Ellipse(center, width + 0.2, height + 1.1, angle=angle, color='blue', alpha = 0.1)
ring_singularity = patches.Ellipse(center, width - 1, height - 1.8, angle = angle, color = 'black', alpha = 0.7)

ergosphere_left = patches.Arc((-0.7,0), 4, 4, angle = angle, theta1 = 69, theta2 = 291, 
                              color = 'gray')
ergosphere_right = patches.Arc((0.7, 0), 4, 4, angle = angle, theta1 = -111, theta2 = 111, 
                              color = 'gray')
# Generate x values
x = np.linspace(-np.pi/2, np.pi/2, 100)
# Calculate y values for the cosine function
y1 = np.cos(x)
y2 = -np.cos(x)

vertices1 = list(zip(x, y1)) + [(x[-1], 0), (x[0], 0)]
path1 = Path(vertices1, closed=True)

vertices2 = list(zip(x, y2)) + [(x[-1], 0), (x[0], 0)]
path2 = Path(vertices2, closed=True)

filled_area1 = PathPatch(path1, color='gray', alpha=0.7)
filled_area2 = PathPatch(path2, color='gray', alpha=0.7)

# arrows


arrow_erg_outer = patches.Arrow(x = -2.5, y = -2.7, dx = 0.5, dy = 1.2, width = 0.1, color = 'black')
arrow_outer_hor = patches.Arrow(x = 3, y = -2.7, dx = -1.5, dy = 1.6, width = 0.1, color = 'black')
arrow_inner_hor = patches.Arrow(x = 4, y = -1, dx = -2.5, dy = 0.3, width = 0.1, color = 'black')
arrow_erg_inner = patches.Arrow(x = 3.8, y = 1, dx = -3, dy = -0.3, width = 0.1, color = 'black')
arrow_ring = patches.Arrow(x = 0, y = -4, dx = 0, dy = 3.9, width = 0.1, color = 'black')
# Plot
fig, ax = plt.subplots()
ax.set_aspect('equal', 'box')

ax.add_patch(inner_horizon)
ax.add_patch(outer_horizon)
ax.add_patch(ring_singularity)
ax.add_patch(ergosphere_left)
ax.add_patch(ergosphere_right)

ax.add_patch(filled_area1)
ax.add_patch(filled_area2)

ax.add_patch(arrow_erg_outer)
ax.text(-3.8, -2.9, 'Outer ergosphere')

ax.add_patch(arrow_outer_hor)
ax.text(3, -2.9, 'Outer horizon')

ax.add_patch(arrow_inner_hor)
ax.text(4.1, -1.1, 'Inner horizon')

ax.add_patch(arrow_erg_inner)
ax.text(3.9, 1, 'Inner ergosphere')

ax.add_patch(arrow_ring)
ax.text(-1, -4.3, 'Ring Singularity')

ax.set_aspect('equal', 'box')  # Set aspect ratio to be equal
ax.set_xlim(-5, 5)  # Adjust x-axis limits for better visualization
ax.set_ylim(-5, 5)  # Adjust y-axis limits for better visualization
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_title('Rotating black hole (uncharged)')
ax.set_axis_off()
#plt.grid(True)
plt.show()






