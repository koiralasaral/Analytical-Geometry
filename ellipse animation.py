import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Ellipse Parameters
a = 5  # Semi-major axis
b = 3  # Semi-minor axis
phi_offset = np.radians(40)  # Angular offset between φ and φ'

# Pre-calculate ellipse and auxiliary circle points for fixed plots
theta = np.linspace(0, 2 * np.pi, 400)
ellipse_x = a * np.cos(theta)
ellipse_y = b * np.sin(theta)
aux_circle_x = a * np.cos(theta)
aux_circle_y = a * np.sin(theta)

# Set up the figure and axis
fig, ax = plt.subplots(figsize=(8, 8))
ax.set_xlim(-a - 1, a + 1)
ax.set_ylim(-b - 1, b + 1)
ax.set_aspect('equal', adjustable='box')
ax.grid(True)
ax.set_title('2D Animation: Ellipse with Auxiliary Circle')

# Plot the fixed elements: ellipse, auxiliary circle, and axes
ax.plot(ellipse_x, ellipse_y, 'b-', label='Ellipse')
ax.plot(aux_circle_x, aux_circle_y, 'g--', label='Auxiliary Circle')
ax.axhline(0, color='r', linestyle='--', label='Major Axis')
ax.axvline(0, color='purple', linestyle='--', label='Minor Axis')

# Create animated elements (initially empty)
point_ellipse1, = ax.plot([], [], 'ro', label='Point 1 (Ellipse)')
point_ellipse2, = ax.plot([], [], 'ro', label='Point 2 (Ellipse)')
chord_line, = ax.plot([], [], 'm-', linewidth=2, label='Chord')
point_aux1, = ax.plot([], [], 'ko', label='Point 1 (Auxiliary Circle)')
point_aux2, = ax.plot([], [], 'ko', label='Point 2 (Auxiliary Circle)')

def init():
    point_ellipse1.set_data([], [])
    point_ellipse2.set_data([], [])
    chord_line.set_data([], [])
    point_aux1.set_data([], [])
    point_aux2.set_data([], [])
    return point_ellipse1, point_ellipse2, chord_line, point_aux1, point_aux2

def update(frame):
    # Define the eccentric angles that vary with the frame number
    phi1 = frame * 0.05
    phi2 = (phi1 + phi_offset) % (2 * np.pi)

    # Compute coordinates on the ellipse for the given eccentric angles
    x1, y1 = a * np.cos(phi1), b * np.sin(phi1)
    x2, y2 = a * np.cos(phi2), b * np.sin(phi2)

    # Compute points on the auxiliary circle (with radius = a)
    aux_x1, aux_y1 = a * np.cos(phi1), a * np.sin(phi1)
    aux_x2, aux_y2 = a * np.cos(phi2), a * np.sin(phi2)

    # Set the updated point coordinates as sequences (lists)
    point_ellipse1.set_data([x1], [y1])
    point_ellipse2.set_data([x2], [y2])
    chord_line.set_data([x1, x2], [y1, y2])
    point_aux1.set_data([aux_x1], [aux_y1])
    point_aux2.set_data([aux_x2], [aux_y2])

    return point_ellipse1, point_ellipse2, chord_line, point_aux1, point_aux2

# Create and run the animation
anim = FuncAnimation(fig, update, frames=200, init_func=init, blit=True, interval=50)
plt.legend()
plt.show()