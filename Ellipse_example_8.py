import numpy as np
import matplotlib.pyplot as plt

# Given ellipse: x^2 + 4y^2 - 4x + 24y + 24 = 0
# Step 1. Complete the square.
# For x:
#    x^2 - 4x = (x - 2)^2 - 4.
# For y:
#    4y^2 + 24y = 4*(y^2 + 6y)
#               = 4*((y+3)^2 - 9)
#               = 4(y+3)^2 - 36.
#
# Thus, the equation becomes:
#    (x - 2)^2 - 4 + 4(y+3)^2 - 36 + 24 = 0
# => (x - 2)^2 + 4(y+3)^2 - 16 = 0
# => (x - 2)^2 + 4(y+3)^2 = 16.
#
# Dividing both sides by 16 gives:
#    ((x - 2)^2)/16 + ((y+3)^2)/4 = 1.
#
# Therefore, the ellipse is in standard form:
#    (x - h)^2 / a^2 + (y - k)^2 / b^2 = 1,
#
# where:
#    Center: (h, k) = (2, -3)
#    a^2 = 16   => a = 4   (semi-major axis)
#    b^2 = 4    => b = 2   (semi-minor axis)
#
# Since a > b the major axis is horizontal.
#
# Step 2. Compute the eccentricity (e):
#    e = √(1 - (b^2)/(a^2)) = √(1 - 4/16) = √(0.75) = (√3)/2.
#
# Step 3. Determine the foci.
#    For a horizontal ellipse, the foci are at:
#       (h ± a·e, k)
#    Here: (2 ± 4*(√3/2), -3) = (2 ± 2√3, -3).
#
# Step 4. Length of latus rectum:
#    L = (2 * b^2) / a = (2*4)/4 = 2.
#
# Also, major axis length = 2a = 8, minor axis length = 2b = 4.

# Define parameters:
a = 4
b = 2
center = (2, -3)
a_squared = a**2   # 16
b_squared = b**2   # 4

# Compute eccentricity:
e = np.sqrt(1 - b_squared / a_squared)  # e = sqrt(1 - 4/16) = sqrt(0.75)
print("Eccentricity e =", e)

# Compute foci (for horizontal ellipse):
f1 = (center[0] + a * e, center[1])
f2 = (center[0] - a * e, center[1])

# Compute latus rectum length:
L = 2 * b_squared / a  # 2*4/4 = 2

# Print computed parameters:
print("Center =", center)
print("Semi-major axis a =", a)
print("Semi-minor axis b =", b)
print("Major axis length = ", 2*a)
print("Minor axis length = ", 2*b)
print("Foci =", f1, "and", f2)
print("Length of latus rectum =", L)

# Plot the ellipse and its geometric features.
# Parametric representation of the ellipse:
t = np.linspace(0, 2*np.pi, 400)
x = center[0] + a * np.cos(t)
y = center[1] + b * np.sin(t)

plt.figure(figsize=(8,8))
plt.plot(x, y, 'b-', lw=2, label=r'Ellipse: $\frac{(x-2)^2}{16}+\frac{(y+3)^2}{4}=1$')

# Plot the center.
plt.plot(center[0], center[1], 'ko', markersize=8, label="Center (2, -3)")

# Plot the major axis:
plt.plot([center[0] - a, center[0] + a], [center[1], center[1]], 'k--', lw=1, label="Major Axis")
# Plot the minor axis:
plt.plot([center[0], center[0]], [center[1] - b, center[1] + b], 'k--', lw=1, label="Minor Axis")

# Plot the foci:
plt.plot(f1[0], f1[1], 'ro', markersize=8, label="Foci")
plt.plot(f2[0], f2[1], 'ro', markersize=8)

# Plot the latus rectum (through the right focus f1):
latus_y = np.linspace(f1[1] - L/2, f1[1] + L/2, 50)
latus_x = np.full_like(latus_y, f1[0])
plt.plot(latus_x, latus_y, 'g-', lw=2, label="Latus Rectum")

# Annotate important points:
plt.text(center[0]-0.8, center[1]+0.5, "Center (2, -3)", fontsize=10)
plt.text(f1[0]+0.2, f1[1]+0.2, "Focus", fontsize=10)
plt.text(directrix := center[0] + a/e, center[1]-1, "Directrix: x = {:.2f}".format(directrix), color='purple', fontsize=10)

plt.xlabel("x")
plt.ylabel("y")
plt.title("Example 8: Ellipse\nx² + 4y² - 4x + 24y + 24 = 0")
plt.legend(loc="upper right")
plt.grid(True)
plt.axis('equal')
plt.show()