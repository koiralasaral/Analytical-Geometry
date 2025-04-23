import numpy as np
import matplotlib.pyplot as plt

# =============================================================================
# Helper function: Rotate points (works on an (N,2) array).
# =============================================================================
def rotate_points(points, theta, pivot=None):
    """
    Rotate an array of 2D points by an angle theta (in radians).
    If pivot is provided, rotate about that point; otherwise, rotate about the origin.

    :param points: NumPy array of shape (N, 2).
    :param theta: Rotation angle in radians.
    :param pivot: Optional point (array-like of shape (2,)).
    :return: Rotated points as a NumPy array.
    """
    R = np.array([[np.cos(theta), -np.sin(theta)],
                  [np.sin(theta),  np.cos(theta)]])
    if pivot is not None:
        return (points - pivot) @ R.T + pivot
    else:
        return points @ R.T

# =============================================================================
# Helper function: Rotate coordinate grids (for mesh grids).
# =============================================================================
def rotate_axes(X, Y, theta):
    """
    Rotate coordinate grid arrays X and Y by angle theta.

    :param X: X coordinates (NumPy array).
    :param Y: Y coordinates (NumPy array).
    :param theta: Rotation angle in radians.
    :return: Tuple (x_rot, y_rot)
    """
    x_rot = X * np.cos(theta) - Y * np.sin(theta)
    y_rot = X * np.sin(theta) + Y * np.cos(theta)
    return x_rot, y_rot

# =============================================================================
# Example 1: Rotating Points about a Pivot and Displaying Rotated Axes
# =============================================================================

# Data: points and pivot (change as desired)
points = np.array([[1, 2], [3, 4], [5, 6]])
pivot = np.array([-2, -3])  # Pivot point for rotation
theta_points = np.pi / 6    # 30° rotation

# Rotate points about the pivot.
rotated_points = rotate_points(points, theta_points, pivot=pivot)

# Set up the plot.
fig1, ax1 = plt.subplots(figsize=(8, 6))
ax1.scatter(points[:, 0], points[:, 1], color="blue", label="Original Points")
ax1.scatter(rotated_points[:, 0], rotated_points[:, 1],
            color="red", label="Rotated Points (Pivot)")

# Annotate each point.
for i, pt in enumerate(points):
    ax1.text(pt[0] + 0.2, pt[1] + 0.2, f"P{i+1}", color="blue", fontsize=10)
for i, pt in enumerate(rotated_points):
    ax1.text(pt[0] + 0.2, pt[1] + 0.2, f"P{i+1}'", color="red", fontsize=10)
    
# Mark the pivot.
ax1.scatter(pivot[0], pivot[1], color="green", s=100, marker="x", label="Pivot")

# --- Add rotated axes arrows from the pivot ---
# Compute rotated unit vectors for the new x' and y' axes.
rot_x = np.array([np.cos(theta_points), np.sin(theta_points)])    # Rotated x-axis unit vector.
rot_y = np.array([-np.sin(theta_points), np.cos(theta_points)])   # Rotated y-axis unit vector.

arrow_scale = 4  # Adjust the length as needed.
ax1.annotate("", xy=pivot + arrow_scale * rot_x, xytext=pivot,
             arrowprops=dict(facecolor="orange", width=2, headwidth=8))
ax1.text(*(pivot + arrow_scale * rot_x + np.array([0.3, 0.2])), "x'", color="orange", fontsize=12)

ax1.annotate("", xy=pivot + arrow_scale * rot_y, xytext=pivot,
             arrowprops=dict(facecolor="purple", width=2, headwidth=8))
ax1.text(*(pivot + arrow_scale * rot_y + np.array([0.3, 0.2])), "y'", color="purple", fontsize=12)

# Draw global (original) axes.
ax1.axhline(0, color="gray", linestyle="--", linewidth=1)
ax1.axvline(0, color="gray", linestyle="--", linewidth=1)

# Set axis limits so arrows are visible.
ax1.set_xlim(-8, 8)
ax1.set_ylim(-8, 10)

ax1.set_title("Points Rotation about a Pivot with Rotated Axes")
ax1.set_xlabel("X-axis")
ax1.set_ylabel("Y-axis")
ax1.legend(loc="upper left")
ax1.grid(True, linestyle="--", linewidth=0.5)
plt.show()

# =============================================================================
# Example 2: Transforming a Quadratic Equation via Rotation & Displaying Rotated Axes
# =============================================================================

# Rotation for the equation.
theta_eq = np.pi / 4  # 45° rotation

# Create a grid.
X, Y = np.meshgrid(np.linspace(-100, 100, 400),
                   np.linspace(-100, 100, 400))
# Define a quadratic equation; here, we use:
#   2x² + 4xy − 5y² + 20x − 22y − 14 = 0.
Z = 2*X**2 + 4*X*Y - 5*Y**2 + 20*X - 22*Y - 14

# Rotate the grid (rotation about the origin).
x_rot_grid, y_rot_grid = rotate_axes(X, Y, theta_eq)
Z_rot = 2*x_rot_grid**2 + 4*x_rot_grid*y_rot_grid - 5*y_rot_grid**2 + 20*x_rot_grid - 22*y_rot_grid - 14

# Set up subplots.
fig2, (ax2, ax3) = plt.subplots(1, 2, figsize=(14, 6))

# Plot the original equation.
ax2.contour(X, Y, Z, levels=[0], colors="blue")
ax2.set_title("Original Equation")
ax2.set_xlabel("X")
ax2.set_ylabel("Y")
ax2.axhline(0, color="gray", linestyle="--", linewidth=1)
ax2.axvline(0, color="gray", linestyle="--", linewidth=1)
ax2.grid(True, linestyle="--", linewidth=0.5)

# Plot the transformed (rotated) equation.
ax3.contour(X, Y, Z_rot, levels=[0], colors="red")
ax3.set_title("Transformed Equation After 45° Rotation")
ax3.set_xlabel("X")
ax3.set_ylabel("Y")
ax3.axhline(0, color="gray", linestyle="--", linewidth=1)
ax3.axvline(0, color="gray", linestyle="--", linewidth=1)
ax3.grid(True, linestyle="--", linewidth=0.5)

# --- Add rotated axes arrows on the transformed plot (about the origin) ---
axes_scale = 40  # Adjust for grid range.
rot_x_eq = np.array([np.cos(theta_eq), np.sin(theta_eq)]) * axes_scale
rot_y_eq = np.array([-np.sin(theta_eq), np.cos(theta_eq)]) * axes_scale

ax3.annotate("", xy=rot_x_eq, xytext=(0, 0),
             arrowprops=dict(facecolor="orange", width=3, headwidth=12))
ax3.text(rot_x_eq[0] + 2, rot_x_eq[1] + 2, "x'", color="orange", fontsize=12)

ax3.annotate("", xy=rot_y_eq, xytext=(0, 0),
             arrowprops=dict(facecolor="purple", width=3, headwidth=12))
ax3.text(rot_y_eq[0] + 2, rot_y_eq[1] + 2, "y'", color="purple", fontsize=12)

ax3.set_xlim(-60, 60)
ax3.set_ylim(-60, 60)

plt.tight_layout()
plt.show()
