import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Program 1: Computer Graphics & CAD
# Ellipse parameters (e.g., a design curve)
a = 5.0
b = 3.0

def tangent_geometry(theta):
    """
    Compute:
     - P: A point on the ellipse: P = (a*cos(theta), b*sin(theta))
     - u: Derived vector for tangent: u = (cos(theta)/a, sin(theta)/b)
         (so that u^T * P = 1)
     - Tangent intersections:
         T: Intersection with the x-axis (set y = 0)  =>  T = (1/u[0], 0)
         t: Intersection with the y-axis (set x = 0)  =>  t = (0, 1/u[1])
    """
    P = np.array([a * np.cos(theta), b * np.sin(theta)])
    u = np.array([np.cos(theta)/a, np.sin(theta)/b])
    T = np.array([1/u[0], 0]) if np.abs(u[0]) > 1e-9 else np.array([np.nan, np.nan])
    t_pt = np.array([0, 1/u[1]]) if np.abs(u[1]) > 1e-9 else np.array([np.nan, np.nan])
    return P, T, t_pt

# Set up figure and axis
fig, ax = plt.subplots(figsize=(8,8))
theta_vals = np.linspace(0, 2*np.pi, 400)
x_ellipse = a * np.cos(theta_vals)
y_ellipse = b * np.sin(theta_vals)
ax.plot(x_ellipse, y_ellipse, 'b-', lw=2, label="Design Curve (Ellipse)")
ax.set_xlim(-a-1, a+1)
ax.set_ylim(-b-1, b+1)
ax.set_aspect('equal')
ax.grid(True)
ax.set_title("Program 1 (CAD): Tangent Geometry on an Elliptical Curve")

# Drawing artists for animation
point_P, = ax.plot([], [], 'ro', markersize=8, label="Point P")
tangent_line, = ax.plot([], [], 'r--', lw=2, label="Tangent at P")
intersection_T, = ax.plot([], [], 'go', markersize=8, label="Intersection on x-axis")
intersection_t, = ax.plot([], [], 'mo', markersize=8, label="Intersection on y-axis")
ax.legend(loc='upper right')

def update1(theta):
    P, T, t_pt = tangent_geometry(theta)
    point_P.set_data([P[0]], [P[1]])
    intersection_T.set_data([T[0]], [T[1]])
    intersection_t.set_data([t_pt[0]], [t_pt[1]])
    # Compute the tangent's direction.
    u = np.array([np.cos(theta)/a, np.sin(theta)/b])
    d = np.array([-u[1], u[0]])   # d is perpendicular to u.
    t_range = np.linspace(-10, 10, 100)
    line_pts = T.reshape(2,1) + np.outer(d, t_range)
    tangent_line.set_data(line_pts[0, :], line_pts[1, :])
    return point_P, tangent_line, intersection_T, intersection_t

anim1 = FuncAnimation(fig, update1, frames=np.linspace(0, 2*np.pi, 200),
                      interval=50, blit=True)
plt.show()