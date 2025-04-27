import numpy as np
import matplotlib.pyplot as plt

# -------------------------------
# Ellipse Parameters and Angles
# -------------------------------
a = 5  # semi-major axis
b = 3  # semi-minor axis

# Eccentric angles in radians (you can change these values)
phi = np.radians(30)      # first eccentric angle, phi
phi_dash = np.radians(70) # second eccentric angle, phi'

# ------------------------------------------
# Compute Points on the Ellipse (Using t = eccentric angle)
# ------------------------------------------
# For an ellipse: x = a*cos(t), y = b*sin(t)
P = np.array([a * np.cos(phi), b * np.sin(phi)])         # Point corresponding to phi
Q = np.array([a * np.cos(phi_dash), b * np.sin(phi_dash)])   # Point corresponding to phi'

# ---------------------------------------------------
# Determine the Equation of the Chord Joining P and Q
# ---------------------------------------------------
# Using the two-point form we can write the line in determinant form:
#   (x - x1)*(y2 - y1) - (y - y1)*(x2 - x1) = 0
# Which expands to: A*x + B*y + C = 0, where:
A = b * (np.sin(phi_dash) - np.sin(phi))
B = a * (np.cos(phi_dash) - np.cos(phi))
C = a * b * np.sin(phi - phi_dash)
# (Note that using trigonometric identities, one can show that C = a*b*sin(phi - phi');)
print("Chord equation (standard form):")
print(f"{A:.3f} * x + {B:.3f} * y + {C:.3f} = 0\n")

# ----------------------------------------------------------
# Compute the Foot of the Perpendicular from the Origin to the Chord
# ----------------------------------------------------------
# We find the foot D (from origin 0,0 to the line through P and Q) using vector projection:
# Let v = Q - P, then the projection parameter t is given by:
#   t = - (P · v) / |v|^2   so that D = P + t*v
v = Q - P
t = - (np.dot(P, v)) / (np.dot(v, v))
D = P + t * v  # This point is the foot of the perpendicular

# ---------------------------------------------------------------
# Prepare Data for Plotting the Ellipse and the Auxiliary Circle
# ---------------------------------------------------------------
theta = np.linspace(0, 2 * np.pi, 400)
ellipse_x = a * np.cos(theta)
ellipse_y = b * np.sin(theta)

# The auxiliary circle (based on the major axis 'a') is given by x^2 + y^2 = a^2.
circle_x = a * np.cos(theta)
circle_y = a * np.sin(theta)

# ---------------------------------------------------------------
# Plotting
# ---------------------------------------------------------------
plt.figure(figsize=(8, 8))

# Plot the Ellipse
plt.plot(ellipse_x, ellipse_y, label="Ellipse", lw=2)

# Plot the Auxiliary Circle (dashed green line)
plt.plot(circle_x, circle_y, 'g--', label="Auxiliary Circle")

# Plot the Chord joining the two ellipse points (red solid line)
plt.plot([P[0], Q[0]], [P[1], Q[1]], 'r-', linewidth=2, label="Chord")

# Mark the two points on the ellipse
plt.plot(P[0], P[1], 'bo', label="Point P")
plt.plot(Q[0], Q[1], 'bo', label="Point Q")
plt.text(P[0], P[1], "  P", fontsize=12, color="blue")
plt.text(Q[0], Q[1], "  Q", fontsize=12, color="blue")

# Plot the perpendicular from the center to the chord (magenta dashed line)
plt.plot([0, D[0]], [0, D[1]], 'm--', linewidth=2, label="Perpendicular from Center")
plt.plot(D[0], D[1], 'mo', label="Foot of Perpendicular")

# ---------------------------------------------------------------------------
# Plot the Rays on the Auxiliary Circle Showing the Eccentric Angles
# ---------------------------------------------------------------------------
# These rays extend from the origin to the points on the auxiliary circle corresponding
# to the eccentric angles phi and phi_dash.
A1 = np.array([a * np.cos(phi), a * np.sin(phi)])       # For angle phi
A2 = np.array([a * np.cos(phi_dash), a * np.sin(phi_dash)]) # For angle phi'
plt.plot([0, A1[0]], [0, A1[1]], 'k:', linewidth=1.5, label="Eccentric Angle Rays")
plt.plot([0, A2[0]], [0, A2[1]], 'k:', linewidth=1.5)

# Annotate the angles on the auxiliary circle
plt.text(A1[0] * 1.05, A1[1] * 1.05, r"$\phi$", fontsize=12)
plt.text(A2[0] * 1.05, A2[1] * 1.05, r"$\phi'$", fontsize=12)

# ---------------------------------------------------------------
# Figure Enhancements
# ---------------------------------------------------------------
plt.xlabel("x")
plt.ylabel("y")
plt.title("Ellipse with Auxiliary Circle, Chord, and Dropped Perpendicular")
plt.legend(loc="best")
plt.gca().set_aspect('equal', adjustable='box')
plt.grid(True)
plt.show()
