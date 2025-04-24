import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Ellipse parameters
a = 5.0
b = 3.0

def tangent_properties(theta):
    """
    Compute the following for a given angle theta (a scalar):
      - P is the point on the ellipse: P = (a*cos(theta), b*sin(theta))
      - u is defined such that u^T * P = 1:
            u = (x0/a^2, y0/b^2)  where x0=a*cos(theta), y0=b*sin(theta)
      - T is the intersection of the tangent line with the x-axis (found by setting y = 0):
            u[0]*x = 1  -->  x = 1/u[0]
      - t_pt is the intersection with the y-axis (by setting x = 0):
            u[1]*y = 1  -->  y = 1/u[1]
    """
    x0 = a * np.cos(theta)
    y0 = b * np.sin(theta)
    P = np.array([x0, y0])
    u = np.array([x0/(a**2), y0/(b**2)])
    # Using if...else to protect against division by zero; u[0] and u[1] are scalars here.
    T = np.array([1/u[0], 0]) if np.abs(u[0]) > 1e-9 else np.array([np.nan, np.nan])
    t_pt = np.array([0, 1/u[1]]) if np.abs(u[1]) > 1e-9 else np.array([np.nan, np.nan])
    return P, T, t_pt

# Set up the figure and initial plot
fig, ax = plt.subplots(figsize=(8,8))
theta_vals = np.linspace(0, 2*np.pi, 400)
x_ellipse = a * np.cos(theta_vals)
y_ellipse = b * np.sin(theta_vals)
ax.plot(x_ellipse, y_ellipse, 'b-', label="Ellipse")
ax.set_xlim(-a-1, a+1)
ax.set_ylim(-b-1, b+1)
ax.set_aspect('equal')
ax.grid(True)
plt.title("Animation 1: Tangent Geometry on an Ellipse")

# Create artist objects for animated elements
tangent_line, = ax.plot([], [], 'r--', lw=2, label="Tangent at P")
point_P, = ax.plot([], [], 'ko', markersize=6, label="P")
point_T, = ax.plot([], [], 'go', markersize=8, label="T on x-axis")
point_t, = ax.plot([], [], 'mo', markersize=8, label="t on y-axis")
ax.legend(loc='upper right')

def update_tangent(theta):
    # Given a scalar theta, compute properties.
    P, T, t_pt = tangent_properties(theta)
    # Because set_data expects sequences, we wrap scalars in lists:
    point_P.set_data([P[0]], [P[1]])
    point_T.set_data([T[0]], [T[1]])
    point_t.set_data([t_pt[0]], [t_pt[1]])
    
    # Compute the tangent's direction.
    # Use u = (x0/a^2, y0/b^2) computed at P.
    x0, y0 = P
    u = np.array([x0/(a**2), y0/(b**2)])
    # d is a vector orthogonal to u.
    d = np.array([-u[1], u[0]])
    # Use T as the base point.
    base = T
    t_line = np.linspace(-10, 10, 100)
    # Ensure base is reshaped to column vector.
    line_points = base.reshape(2,1) + np.outer(d, t_line)
    tangent_line.set_data(line_points[0, :], line_points[1, :])
    
    return point_P, point_T, point_t, tangent_line

# Here, we pass the function update_tangent directly and supply frames as a sequence of scalar theta values.
anim1 = FuncAnimation(fig,
                      update_tangent,
                      frames=np.linspace(0, 2*np.pi, 200),
                      interval=50, blit=True)

plt.show()