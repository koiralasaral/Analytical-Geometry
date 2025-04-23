import numpy as np
import matplotlib.pyplot as plt

def translate_coordinates(points, new_origin):
    """
    Translate the origin of coordinates to a new origin.

    :param points: Array of points (Nx2 or Nx3) as a NumPy array.
    :param new_origin: The new origin as a NumPy array.
    :return: Translated points as a NumPy array.
    """
    return points - new_origin

# Example usage
points = np.array([[1, 2], [3, 4], [5, 6]])  # Original points
new_origin = np.array([1, 1])  # New origin
translated_points = translate_coordinates(points, new_origin)

print("Original Points:\n", points)
print("Translated Points:\n", translated_points)

# Plot the original and translated points
plt.figure(figsize=(8, 6))
plt.scatter(points[:, 0], points[:, 1], color='blue', label='Original Points')
plt.scatter(translated_points[:, 0], translated_points[:, 1], color='red', label='Translated Points')

# Annotate the points
for i, point in enumerate(points):
    plt.text(point[0], point[1], f'P{i+1}', color='blue', fontsize=10)
for i, point in enumerate(translated_points):
    plt.text(point[0], point[1], f'P{i+1}\'', color='red', fontsize=10)

# Plot the translation lines
for original, translated in zip(points, translated_points):
    plt.plot([original[0], translated[0]], [original[1], translated[1]], 
             color='green', linestyle='--', linewidth=0.8)

plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.grid(color='gray', linestyle='--', linewidth=0.5)
plt.legend()
plt.title("Original and Translated Points")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.show()

# Transform the equation x^2 - y^2 + 2*x + 4*y = 0 to parallel axes through the point (-1, 2)
# Original equation coefficients
A, B, C, D, E, F = 1, 0, -1, 2, 4, 0

# New origin
new_origin = np.array([-1, 2])
h, k = new_origin

# Calculate new coefficients
D_new = D + 2 * A * h + B * k
E_new = E + 2 * C * k + B * h
F_new = F + A * h**2 + C * k**2 + B * h * k + D * h + E * k

# Transformed equation: X^2 - Y^2 + D_new*X + E_new*Y + F_new = 0
print(f"Transformed equation: X^2 - Y^2 + ({D_new})*X + ({E_new})*Y + ({F_new}) = 0")

# Plot the original and transformed equations
x = np.linspace(-5, 5, 400)
y = np.linspace(-5, 5, 400)
X, Y = np.meshgrid(x, y)

# Original equation: x^2 - y^2 + 2*x + 4*y = 0
original_eq = X**2 - Y**2 + 2*X + 4*Y

# Transformed equation: X^2 - Y^2 + D_new*X + E_new*Y + F_new = 0
transformed_eq = X**2 - Y**2 + D_new*X + E_new*Y + F_new

plt.figure(figsize=(10, 8))
plt.contour(X, Y, original_eq, levels=[0], colors='blue', label='Original Equation')
plt.contour(X, Y, transformed_eq, levels=[0], colors='red', label='Transformed Equation')

plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.scatter(new_origin[0], new_origin[1], color='green', label='New Origin (-1, 2)')
plt.grid(color='gray', linestyle='--', linewidth=0.5)
plt.legend(['Original Equation', 'Transformed Equation', 'New Origin'])
plt.title("Original and Transformed Equations")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.show()
