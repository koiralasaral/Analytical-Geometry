import numpy as np
import matplotlib.pyplot as plt

# -------------------------------
# Ellipse Parameters and Key Quantities
# -------------------------------
a = 5  # semi-major axis
b = 3  # semi-minor axis
c = np.sqrt(a**2 - b**2)  # focal distance
e = c / a  # eccentricity

# -------------------------------
# Define Eccentric Angles
# -------------------------------
phi = np.radians(30)      # first eccentric angle (in degrees)
phi_dash = np.radians(70) # second eccentric angle

# Compute Points on the Auxiliary Circle (Where Eccentric Angles Are Formed)
P_aux = np.array([a * np.cos(phi), a * np.sin(phi)])  # Corresponding auxiliary point for φ
Q_aux = np.array([a * np.cos(phi_dash), a * np.sin(phi_dash)]) # Corresponding auxiliary point for φ'

# Compute Points on the Ellipse
P = np.array([a * np.cos(phi), b * np.sin(phi)])  # Ellipse point for φ
Q = np.array([a * np.cos(phi_dash), b * np.sin(phi_dash)]) # Ellipse point for φ'

# -------------------------------
# Drop Perpendiculars from Auxiliary Circle to the Major Axis
# -------------------------------
# These perpendiculars are vertical lines passing through P_aux and Q_aux to the base (y=0)
P_drop = np.array([P_aux[0], 0])  # Foot of perpendicular for φ
Q_drop = np.array([Q_aux[0], 0])  # Foot of perpendicular for φ'

# -------------------------------
# Define the Chord Joining P and Q
# -------------------------------
A = b * (np.sin(phi_dash) - np.sin(phi))
B = a * (np.cos(phi_dash) - np.cos(phi))
C = a * b * np.sin(phi - phi_dash)

# -------------------------------
# Prepare Data for Plotting the Ellipse and Auxiliary Circle
# -------------------------------
theta = np.linspace(0, 2 * np.pi, 400)
ellipse_x = a * np.cos(theta)
ellipse_y = b * np.sin(theta)

circle_x = a * np.cos(theta)
circle_y = a * np.sin(theta)

# -------------------------------
# Plot Everything
# -------------------------------
plt.figure(figsize=(10, 10))

# Plot the ellipse
plt.plot(ellipse_x, ellipse_y, 'b-', label="Ellipse")

# Plot the auxiliary circle
plt.plot(circle_x, circle_y, 'g--', label="Auxiliary Circle")

# Plot the major and minor axes
plt.axhline(0, color='r', linestyle='--', label="Major Axis (Base)")
plt.axvline(0, color='purple', linestyle='--', label="Minor Axis")

# Plot the foci
plt.plot([c, -c], [0, 0], 'r*', markersize=12, label="Foci")

# Plot the chord
plt.plot([P[0], Q[0]], [P[1], Q[1]], 'r-', label="Chord")

# Plot the eccentric rays (lines forming angles φ and φ')
plt.plot([0, P_aux[0]], [0, P_aux[1]], 'c-', label=r"Eccentric ray for $\phi$")
plt.plot([0, Q_aux[0]], [0, Q_aux[1]], 'c-', label=r"Eccentric ray for $\phi'$")

# Plot the auxiliary points and ellipse points
plt.plot(P_aux[0], P_aux[1], 'ko', label="Auxiliary Circle Point (φ)")
plt.plot(Q_aux[0], Q_aux[1], 'ko', label="Auxiliary Circle Point (φ')")
plt.plot(P[0], P[1], 'bo', label="Ellipse Point (φ)")
plt.plot(Q[0], Q[1], 'bo', label="Ellipse Point (φ')")

# Drop perpendiculars from auxiliary points to the major axis
plt.plot([P_aux[0], P_drop[0]], [P_aux[1], P_drop[1]], 'k:', label="Perpendicular for φ")
plt.plot([Q_aux[0], Q_drop[0]], [Q_aux[1], Q_drop[1]], 'k:', label="Perpendicular for φ'")

# ---------------------------------------------------------------
# Plot directrix and latus rectum
plt.axvline(a/e, color='orange', linestyle='-', label=f"Directrix (x = {a/e:.3f})")
plt.plot([c, c], [b**2/a, -b**2/a], 'y-', linewidth=3, label="Latus Rectum")

plt.xlabel("x")
plt.ylabel("y")
plt.title("Ellipse Construction: Chord, Auxiliary Circle, Perpendiculars, and Axes")
plt.legend(loc="best")
plt.grid(True)
plt.gca().set_aspect('equal', adjustable='box')
plt.show()

# -------------------------------
# Print Key Equations
# -------------------------------
print("Ellipse equation: (x²)/({}²) + (y²)/({}²) = 1".format(a, b))
print("Major axis: y = 0")
print("Minor axis: x = 0")
print("Foci: ({:.3f}, 0) and ({:.3f}, 0)".format(c, -c))
print("Latus rectum endpoints at x = {:.3f}, with y = ±{:.3f}".format(c, b**2/a))
print("Directrix: x = {:.3f}".format(a/e))

print("\nChord equation: ({:.3f}) x + ({:.3f}) y + ({:.3f}) = 0".format(A, B, C))
print("Eccentric ray equations: y = tan(φ)*x and y = tan(φ')*x")
print("Perpendicular drop for φ: Vertical line at x = {:.3f}".format(P_aux[0]))
print("Perpendicular drop for φ': Vertical line at x = {:.3f}".format(Q_aux[0]))
