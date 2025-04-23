import numpy as np
import matplotlib.pyplot as plt

def rotate_coordinates(points, theta):
    """
    Rotate the coordinate axes by an angle theta (in radians).

    This function applies a 2D rotation transformation to each point in the
    given array. The rotation matrix used here corresponds to a counter-clockwise
    rotation. For a point [x, y] in the original system, the new coordinates [X, Y]
    will be:
        X = x*cos(theta) - y*sin(theta)
        Y = x*sin(theta) + y*cos(theta)

    :param points: NumPy array of points (shape Nx2)
    :param theta: Rotation angle in radians
    :return: Rotated points (same shape as input)
    """
    c, s = np.cos(theta), np.sin(theta)
    R = np.array([[c, -s],
                  [s,  c]])
    return points @ R.T   # Using matrix multiplication with the transpose of R

# -------------------------------------------------------------------
# Example 1: Rotating Points
# -------------------------------------------------------------------

# Original points
points = np.array([[1, 2], [3, 4], [5, 6]])
theta = np.pi / 6  # 30° rotation in radians
rotated_points = rotate_coordinates(points, theta)

print("Original Points:\n", points)
print("Rotated Points:\n", rotated_points)

# Plot the original and rotated points
plt.figure(figsize=(8, 6))
plt.scatter(points[:, 0], points[:, 1], color='blue', label='Original Points')
plt.scatter(rotated_points[:, 0], rotated_points[:, 1], color='red', label='Rotated Points')

# Annotate points
for i, point in enumerate(points):
    plt.text(point[0], point[1], f'P{i+1}', color='blue', fontsize=10)
for i, point in enumerate(rotated_points):
    plt.text(point[0], point[1], f'P{i+1}\'', color='red', fontsize=10)

# Draw connecting lines for clarity
for original, rotated in zip(points, rotated_points):
    plt.plot([original[0], rotated[0]], [original[1], rotated[1]],
             color='green', linestyle='--', linewidth=0.8)

plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.grid(color='gray', linestyle='--', linewidth=0.5)
plt.legend()
plt.title("Original and Rotated Points")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.show()

# -------------------------------------------------------------------
# Example 2: Transforming a Quadratic Equation via Rotation
# -------------------------------------------------------------------

# Original quadratic equation: x^2 - y^2 + 2*x + 4*y = 0
# Coefficients:
#   x^2 coefficient: 1, y^2 coefficient: -1, xy coefficient: 0,
#   x coefficient: 2, y coefficient: 4, constant: 0
#
# Under a rotation by theta, we substitute:
#   x = X*cos(theta) - Y*sin(theta)
#   y = X*sin(theta) + Y*cos(theta)
#
# Derivation summary:
#   x^2    -> X^2 (cos^2θ - sin^2θ) - 2XY( sinθ*cosθ )
#   y^2    -> X^2 (sin^2θ) + 2XY(sinθ*cosθ) + Y^2(cos^2θ)
# Hence, 
#   x^2 - y^2 = X^2 (cos^2θ - sin^2θ) - 2XY( sinθ*cosθ )
#              - [X^2 sin^2θ + 2XY sinθ*cosθ + Y^2 cos^2θ]
#            = cos(2θ)*X^2 - 2 sin(2θ)*XY - cos(2θ)*Y^2
#
# Also, the linear terms transform as:
#   2x + 4y = 2*(X*cosθ - Y*sinθ) + 4*(X*sinθ + Y*cosθ)
#           = (2 cosθ + 4 sinθ)*X + (-2 sinθ + 4 cosθ)*Y
#
# Thus the transformed equation in the rotated axes (X,Y) is:
#   [cos(2θ)]*X^2 - [2 sin(2θ)]*X*Y - [cos(2θ)]*Y^2 +
#   [2 cosθ + 4 sinθ]*X + [ -2 sinθ + 4 cosθ ]*Y = 0

theta = np.pi / 6  # rotation angle in radians

# Compute new coefficients using trigonometric identities
c2 = np.cos(2*theta)
s2 = np.sin(2*theta)
A_new = c2                     # coefficient for X^2
B_new = -2 * s2                # coefficient for X*Y term
C_new = -c2                  # coefficient for Y^2
D_new = 2*np.cos(theta) + 4*np.sin(theta)   # coefficient for X
E_new = -2*np.sin(theta) + 4*np.cos(theta)   # coefficient for Y
F_new = 0  # constant term remains zero

print(f"Transformed Equation Coefficients:")
print(f"X^2: {A_new}")
print(f"X*Y: {B_new}")
print(f"Y^2: {C_new}")
print(f"X: {D_new}")
print(f"Y: {E_new}")
print(f"Constant: {F_new}")

# Generate a grid to plot contours
x = np.linspace(-5, 5, 400)
y = np.linspace(-5, 5, 400)
X_grid, Y_grid = np.meshgrid(x, y)

# Original equation expressed in (x,y)
original_eq = X_grid**2 - Y_grid**2 + 2*X_grid + 4*y[:, None]
# Note: using broadcasting for the linear term in y to ensure proper shapes.

# Transformed equation expressed in the rotated coordinates (X, Y)
transformed_eq = (A_new*X_grid**2 + B_new*X_grid*Y_grid +
                  C_new*Y_grid**2 + D_new*X_grid + E_new*Y_grid + F_new)

plt.figure(figsize=(10, 8))


# For a simple legend, get the first contour line from each set.

plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.grid(color='gray', linestyle='--', linewidth=0.5)
plt.title("Original and Rotated Equation Contours")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.show()
