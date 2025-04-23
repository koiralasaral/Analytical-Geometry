import numpy as np
import matplotlib.pyplot as plt

# Ellipse parameters
a = 5   # semi-major axis
b = 3   # semi-minor axis

# Ellipse: x²/a² + y²/b² = 1

# Line parameters (change m and c as desired)
m = 0.5  # slope of the line
c = 0.5  # y-intercept of the line

# Substitute y = m*x + c into the ellipse:
#   x²/a² + (m*x + c)²/b² = 1.
# This can be rearranged to a quadratic in x: A*x² + B*x + C = 0.
A_coef = 1/(a**2) + (m**2)/(b**2)
B_coef = 2 * m * c / (b**2)
C_coef = (c**2)/(b**2) - 1

discriminant = B_coef**2 - 4*A_coef*C_coef

print("=== 0.4.1: Intersection of a Line and an Ellipse ===")
print("Quadratic coefficients: A =", A_coef, "B =", B_coef, "C =", C_coef)
print("Discriminant =", discriminant)

if discriminant > 0:
    x_int1 = (-B_coef + np.sqrt(discriminant)) / (2*A_coef)
    x_int2 = (-B_coef - np.sqrt(discriminant)) / (2*A_coef)
    y_int1 = m * x_int1 + c
    y_int2 = m * x_int2 + c
    intersections = [(x_int1, y_int1), (x_int2, y_int2)]
    intersection_type = "Secant: Two distinct intersection points"
elif np.isclose(discriminant, 0, atol=1e-7):
    x_int = -B_coef / (2*A_coef)
    y_int = m * x_int + c
    intersections = [(x_int, y_int)]
    intersection_type = "Tangent: One (double) intersection point"
else:
    intersections = []
    intersection_type = "No real intersection"

print(intersection_type)
for pt in intersections:
    print("Intersection point:", pt)

# Plot ellipse and line.
t = np.linspace(0, 2*np.pi, 400)
ellipse_x = a * np.cos(t)
ellipse_y = b * np.sin(t)

x_line = np.linspace(-a-1, a+1, 400)
y_line = m * x_line + c

plt.figure(figsize=(8,6))
plt.plot(ellipse_x, ellipse_y, 'b-', lw=2, label='Ellipse')
plt.plot(x_line, y_line, 'r--', lw=2, label=f'Line: y = {m:.2f}x + {c:.2f}')
if intersections:
    for i, pt in enumerate(intersections):
        plt.plot(pt[0], pt[1], 'ko', markersize=8, label="Intersection" if i==0 else "")
plt.xlabel("x")
plt.ylabel("y")
plt.title("0.4.1: Intersection of a Line & an Ellipse\n" + intersection_type)
plt.legend()
plt.grid(True)
plt.axis('equal')
plt.show()