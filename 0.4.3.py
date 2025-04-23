import numpy as np
import matplotlib.pyplot as plt

# ================================
# Parameters for the ellipse:
#   Ellipse: x^2/a^2 + y^2/b^2 = 1
# Choose a > b so the major axis is horizontal.
a = 5    # semi-major axis
b = 3    # semi-minor axis

# ================================
# 0.4.3: Condition for Tangency
#
# For a line y = m*x + c to be tangent to the ellipse,
# the necessary and sufficient condition is:
#
#         c^2 = a^2 * m^2 + b^2.
#
# We choose a slope m and then compute c accordingly.
m = 0.8  # chosen slope for the line

# Compute c from the tangency condition.
c = np.sqrt(a**2 * m**2 + b**2)
print("---- Tangency Condition (0.4.3) ----")
print(f"Chosen slope, m = {m:.4f}")
print(f"Computed tangent intercept, c = {c:.4f} (using c^2 = a^2*m^2 + b^2)")

# Now, let's verify the tangency by substituting the line
# y = m*x + c into the ellipse x^2/a^2 + y^2/b^2 = 1.
#
# Substitution yields:
#    x^2/a^2 + (m*x + c)^2/b^2 = 1.
#
# Write this as a quadratic in x:
#    A * x^2 + B * x + C = 0,
# with
A_coef = 1/(a**2) + (m**2)/(b**2)
B_coef = 2 * m * c / (b**2)
C_coef = (c**2)/(b**2) - 1

# Compute the discriminant.
discriminant = B_coef**2 - 4 * A_coef * C_coef

print(f"Quadratic coefficients: A = {A_coef:.6f}, B = {B_coef:.6f}, C = {C_coef:.6f}")
print(f"Discriminant = {discriminant:.6e}")
if np.isclose(discriminant, 0, atol=1e-7):
    print("Tangency condition verified: discriminant is (nearly) zero.\n")
else:
    print("Warning: Discriminant is nonzero; tangency condition not satisfied.\n")

# ================================
# Plotting the ellipse and the tangent line.

# Parametric representation of ellipse:
t = np.linspace(0, 2*np.pi, 400)
ellipse_x = a * np.cos(t)
ellipse_y = b * np.sin(t)

# Equation of the tangent line: y = m*x + c.
x_line = np.linspace(-a-2, a+2, 400)
y_line = m * x_line + c

plt.figure(figsize=(8,6))
plt.plot(ellipse_x, ellipse_y, 'b-', lw=2, label=r'Ellipse: $\frac{x^2}{a^2}+\frac{y^2}{b^2}=1$')
plt.plot(x_line, y_line, 'r--', lw=2, label=f'Tangent: y = {m:.2f}x + {c:.2f}')

# Annotate the point of tangency.
# To obtain the tangency point, solve (x, m*x+c) satisfying
# the tangent equation. Since the discriminant is zero,
# a unique point exists.
x_tangent = -B_coef / (2 * A_coef)
y_tangent = m * x_tangent + c
plt.plot(x_tangent, y_tangent, 'ko', markersize=8, label="Tangency Point")

plt.xlabel("x")
plt.ylabel("y")
plt.title("Condition for Tangency to the Ellipse\n(0.4.3: c² = a²·m² + b²)")
plt.legend()
plt.grid(True)
plt.axis("equal")
plt.show()