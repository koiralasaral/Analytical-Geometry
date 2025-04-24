import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Program 2: Robotics & Path Planning
# Ellipse parameters represent a planned trajectory
a = 5.0
b = 3.0

def robot_properties(theta):
    """
    Given theta, compute:
      - P: Robot position on the ellipse.
      - d: Unit tangent vector (robot's intended heading).
    """
    P = np.array([a * np.cos(theta), b * np.sin(theta)])
    # Compute tangent direction vector: u = (cos(theta)/a, sin(theta)/b)
    u = np.array([np.cos(theta)/a, np.sin(theta)/b])
    d = np.array([-u[1], u[0]])   # d is perpendicular to u.
    d = d / np.linalg.norm(d) if np.linalg.norm(d) != 0 else d
    return P, d

fig2, ax2 = plt.subplots(figsize=(8,8))
theta_vals = np.linspace(0, 2*np.pi, 400)
x_ellipse = a * np.cos(theta_vals)
y_ellipse = b * np.sin(theta_vals)
ax2.plot(x_ellipse, y_ellipse, 'b-', lw=2, label="Planned Trajectory (Ellipse)")
ax2.set_xlim(-a-1, a+1)
ax2.set_ylim(-b-1, b+1)
ax2.set_aspect('equal')
ax2.grid(True)
ax2.set_title("Program 2 (Robotics): Elliptical Trajectory & Heading Direction")

# Robot as point P and heading arrow.
robot_point, = ax2.plot([], [], 'ro', markersize=8, label="Robot Position")
heading_arrow = None  # We will update this object dynamically.

def update_robot(theta):
    global heading_arrow
    P, d = robot_properties(theta)
    robot_point.set_data([P[0]], [P[1]])
    # Remove the previous arrow if it exists:
    if heading_arrow is not None:
        heading_arrow.remove()
    # Draw new arrow from P in direction d (scaled for visualization)
    arrow_length = 2.0
    heading_arrow = ax2.arrow(P[0], P[1], arrow_length*d[0], arrow_length*d[1],
                              head_width=0.3, head_length=0.5, fc='r', ec='r')
    return robot_point, heading_arrow

anim2 = FuncAnimation(fig2, update_robot, frames=np.linspace(0, 2*np.pi, 200),
                      interval=50, blit=False)  # blit False since arrow is redrawn

plt.legend(loc='upper right')
plt.show()