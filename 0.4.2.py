import numpy as np
import matplotlib.pyplot as plt

# Ellipse parameters
a = 5
b = 3

# Choose an eccentric angle t0 to pick a point P on the ellipse.
t0 = np.pi / 4  # you may change this angle
x1 = a * np.cos(t0)
y1 = b * np.sin(t0)
print("\n=== 0.4.2: Tangent and Normal at a Point on the Ellipse ===")
print("Point on ellipse P: ({:.2f}, {:.2f})".format(x1, y1))

# Tangent line of an ellipse (using the standard tangent formula):
# For a point P=(x1, y1) on the ellipse, the tangent is:
# (x*x1)/a^2 + (y*y1)/b^2 = 1.
# Solve for y (assuming y1 is not zero):
if abs(y1) > 1e-6:
    def tangent_y(x):
        return (b ** 2 / y1) * (1 - (x * x1) / (a ** 2))
else:
    # If y1 == 0, the tangent is horizontal; but for our chosen t0 this case does not occur.
    tangent_y = None

# Alternatively, the slope of the tangent may be computed via implicit differentiation:
# For x^2/a^2 + y^2/b^2 = 1, we get:
# dy/dx = - (b^2 * x)/(a^2 * y)  at P.
if abs(y1) > 1e-6:
    slope_tangent = - (b ** 2 * x1) / (a ** 2 * y1)
else:
    slope_tangent = None
print("Tangent slope (from derivative):", slope_tangent)

# The normal line is perpendicular to the tangent. Its slope is:
if slope_tangent is not None and abs(slope_tangent) > 1e-6:
    slope_normal = -1 / slope_tangent
else:
    # if the tangent is vertical, the normal is horizontal
    slope_normal = 0
print("Normal slope:", slope_normal)

# For plotting, define a set of x-values around the point P.
x_vals = np.linspace(x1 - 6, x1 + 6, 400)
if tangent_y is not None:
    y_tangent_vals = tangent_y(x_vals)
else:
    # In the (unlikely) case tangent_y is not defined, handle vertical line.
    x_tangent_vals = np.full_like(x_vals, x1)

# Equation of normal through P: y - y1 = slope_normal*(x - x1)
y_normal_vals = slope_normal * (x_vals - x1) + y1

# Plot the ellipse, tangent, and normal.
t = np.linspace(0, 2 * np.pi, 400)
ellipse_x = a * np.cos(t)
ellipse_y = b * np.sin(t)

plt.figure(figsize=(8, 6))
plt.plot(ellipse_x, ellipse_y, 'b-', lw=2, label='Ellipse')
if tangent_y is not None:
    plt.plot(x_vals, y_tangent_vals, 'r-', lw=2, label='Tangent at P')
else:
    plt.plot(x_tangent_vals, np.linspace(y1 - 6, y1 + 6, 400), 'r-', lw=2, label='Tangent at P (vertical)')
plt.plot(x_vals, y_normal_vals, 'g--', lw=2, label="Normal at P")
plt.plot(x1, y1, 'ko', markersize=8, label="P on Ellipse")
plt.xlabel("x")
plt.ylabel("y")
plt.title("0.4.2: Tangent and Normal at a Point on the Ellipse")
plt.legend()
plt.grid(True)
plt.axis('equal')
plt.show()