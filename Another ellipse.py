import numpy as np
import matplotlib.pyplot as plt

# Ellipse parameters
a = 5  # Semi-major axis
b = 3  # Semi-minor axis
t = np.linspace(0, 2 * np.pi, 500)

# Parametric equations of the ellipse
x = a * np.cos(t)
y = b * np.sin(t)

# Plot the ellipse
plt.plot(x, y, label="Ellipse")
plt.title("Tracing the Ellipse")
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.legend()
plt.axis('equal')
plt.grid(True)
plt.show()
# Specific point on the ellipse (angle)
theta = np.pi / 4  # Example angle in radians

# Point coordinates
x_point = a * np.cos(theta)
y_point = b * np.sin(theta)

# Plot the ellipse and the point
plt.plot(x, y, label="Ellipse")
plt.scatter([x_point], [y_point], color='red', label="Point on Ellipse")
plt.title("Position of a Point on the Ellipse")
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.legend()
plt.axis('equal')
plt.grid(True)
plt.show()
# Distance from the foci
c = np.sqrt(a**2 - b**2)  # Foci distance
focus1 = (-c, 0)
focus2 = (c, 0)

# Calculating focal distances
distance1 = np.sqrt((x_point - focus1[0])**2 + (y_point - focus1[1])**2)
distance2 = np.sqrt((x_point - focus2[0])**2 + (y_point - focus2[1])**2)

print(f"Sum of focal distances: {distance1 + distance2}")
# Polar equation parameters
e = c / a  # Eccentricity
l = b**2 / a  # Semi-latus rectum
theta = np.linspace(0, 2 * np.pi, 500)

# Polar radius
r = l / (1 + e * np.cos(theta))

# Convert polar to Cartesian coordinates
x_polar = r * np.cos(theta)
y_polar = r * np.sin(theta)

# Plot
plt.plot(x_polar, y_polar, label="Ellipse in Polar Form")
plt.title("Polar Equation of the Ellipse")
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.legend()
plt.axis('equal')
plt.grid(True)
plt.show()
# Auxiliary Circle
t_aux = np.linspace(0, 2 * np.pi, 500)
x_aux = a * np.cos(t_aux)
y_aux = a * np.sin(t_aux)

# Plot auxiliary circle
plt.plot(x_aux, y_aux, label="Auxiliary Circle")
plt.title("Auxiliary Circle of Ellipse")
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.legend()
plt.axis('equal')
plt.grid(True)
plt.show()