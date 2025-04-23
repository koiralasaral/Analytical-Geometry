import numpy as np
import matplotlib.pyplot as plt

# Parameters for the ellipse (choose a > b so major axis is horizontal)
a = 5          # semi-major axis
b = 3          # semi-minor axis
e = np.sqrt(1 - (b/a)**2)  # eccentricity, since e < 1 for an ellipse
c = a * e      # focal distance

# Coordinates for the ellipse via parametric form: (a*cos(t), b*sin(t))
t = np.linspace(0, 2*np.pi, 400)
x = a * np.cos(t)
y = b * np.sin(t)

# Compute directrices (for ellipse with horizontal major axis, they are vertical lines:)
directrix_right = a / e
directrix_left = -a / e

# Latus rectum length L = 2b^2 / a.
L = 2 * b**2 / a

# For the right focus, the latus rectum is a vertical line at x = c.
# Its endpoints (L/2 above and below the focus)
latus_y = np.linspace(-L/2, L/2, 50)
latus_x = np.full_like(latus_y, c)

# Prepare the figure.
plt.figure(figsize=(8,8))
plt.plot(x, y, 'b-', lw=2, label=r'Ellipse: $\frac{x^2}{a^2}+\frac{y^2}{b^2}=1$')

# Plot major and minor axes
plt.plot([-a, a], [0, 0], 'k--', lw=1, label='Major axis')
plt.plot([0, 0], [-b, b], 'k--', lw=1, label='Minor axis')

# Plot foci
plt.plot(c, 0, 'ro', markersize=8, label='Focus')
plt.plot(-c, 0, 'ro', markersize=8)

# Plot directrices
plt.axvline(directrix_right, color='purple', linestyle=':', lw=2, label='Directrix')
plt.axvline(directrix_left, color='purple', linestyle=':', lw=2)

# Plot the latus rectum (through right focus)
plt.plot(latus_x, latus_y, 'g-', lw=3, label='Latus Rectum')

# Annotate key points
plt.annotate('Center (0,0)', xy=(0,0), xytext=(-0.8, 0.5))
plt.annotate('Focus', xy=(c,0), xytext=(c+0.2, 0.2))
plt.annotate('Directrix', xy=(directrix_right, 0), xytext=(directrix_right+0.3, -0.5))

plt.xlabel("x")
plt.ylabel("y")
plt.title("Annotated Ellipse with Axes, Foci, Directrices & Latus Rectum")
plt.legend(loc='upper right')
plt.grid(True)
plt.axis('equal')
plt.show()