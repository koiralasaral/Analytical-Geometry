import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Improved Program 2: Robotics & Path Planning using Quiver
# Ellipse parameters (describing a planned trajectory)
a = 5.0   # semi-major axis
b = 3.0   # semi-minor axis

def robot_properties(theta):
    """
    For a given theta, compute:
      - P: position on the ellipse, P = (a*cos(theta), b*sin(theta))
      - d: unit tangent (heading) direction at P
         We use the fact that the tangent direction is orthogonal to 
         u = [cos(theta)/a, sin(theta)/b], so we can choose d = (-u[1], u[0])
    """
    x0 = a * np.cos(theta)
    y0 = b * np.sin(theta)
    P = np.array([x0, y0])
    # u is used to define the tangent line in linear form:
    u = np.array([np.cos(theta)/a, np.sin(theta)/b])
    d = np.array([-u[1], u[0]])  # Not normalized yet.
    norm_d = np.linalg.norm(d)
    if norm_d > 1e-9:
        d = d / norm_d
    return P, d

# Set up the figure and axis.
fig2, ax2 = plt.subplots(figsize=(8,8))
theta_vals = np.linspace(0, 2*np.pi, 400)
x_ellipse = a * np.cos(theta_vals)
y_ellipse = b * np.sin(theta_vals)
ax2.plot(x_ellipse, y_ellipse, 'b-', lw=2, label="Trajectory (Ellipse)")
ax2.set_xlim(-a-1, a+1)
ax2.set_ylim(-b-1, b+1)
ax2.set_aspect('equal')
ax2.grid(True)
ax2.set_title("Improved Program 2: Robotics & Path Planning")

# Create a marker for the robot position.
robot_point, = ax2.plot([], [], 'ro', markersize=8, label="Robot Position")

# Instead of repeatedly creating an arrow, use a Quiver to represent the heading:
# Initially, create a quiver at (0,0) with zero vector.
arrow_length = 1.5  # arrow scaling factor (robot's heading in visualization)
heading_quiver = ax2.quiver(0, 0, 0, 0, angles='xy', scale_units='xy',
                            scale=1, color='r', label="Heading Direction")

ax2.legend(loc='upper right')

def update_robot(theta):
    P, d = robot_properties(theta)
    # Update robot position
    robot_point.set_data([P[0]], [P[1]])
    # Update heading arrow using quiver: set_offsets and set_UVC to update the vector.
    heading_quiver.set_offsets(P.reshape(1,2))
    heading_quiver.set_UVC(arrow_length * d[0], arrow_length * d[1])
    return robot_point, heading_quiver

# Use FuncAnimation with the update function and a range of theta values.
anim2 = FuncAnimation(fig2, update_robot,
                      frames=np.linspace(0, 2*np.pi, 200),
                      interval=50, blit=True)

plt.show()