import sympy as sp
import numpy as np
import matplotlib.pyplot as plt

# We work with the standard ellipse: x^2/a^2 + y^2/b^2 = 1. 
# Recall: Latus rectum L = 2b^2/a, minor axis = 2b.
# We require: 2b^2/a = b  --> a = 2b.
# Also, b^2 = a^2 (1-e^2). With a = 2b, this gives:
#   b^2 = (2b)^2 (1-e^2)  -->  b^2 = 4b^2 (1-e^2)
# Dividing by b^2:
#   1 = 4 (1-e^2)  --> e^2 = 3/4  -->  e = sqrt(3)/2.

# Choose b = 1 so that a = 2.
b_val = 1
a_val = 2
e_val = np.sqrt(3)/2

# Define the ellipse: x^2/4 + y^2 = 1.
x, y = sp.symbols('x y', real=True)
ellipse_eq = sp.Eq(x**2/a_val**2 + y**2/b_val**2, 1)

# --- Plot the ellipse and label foci, minor axis, and latus rectum.
X = np.linspace(-2.5, 2.5, 400)
Y = np.linspace(-1.5, 1.5, 300)
Xv, Yv = np.meshgrid(X, Y)
F = Xv**2/(a_val**2) + Yv**2/(b_val**2) - 1  # zero-contour represents the ellipse

plt.figure(figsize=(6,4))
CS = plt.contour(Xv, Yv, F, levels=[0], colors=['blue'])
plt.clabel(CS, inline=1, fontsize=10)
plt.title("Example 10: Ellipse x²/4 + y² = 1")
plt.xlabel("x"), plt.ylabel("y")

# Mark the foci (located at ±(ae,0)):
focus1 = (a_val*e_val, 0)
focus2 = (-a_val*e_val, 0)
plt.plot(focus1[0], focus1[1], 'ro', label="Foci")
plt.plot(focus2[0], focus2[1], 'ro')

# Draw the minor axis as a green dashed vertical line.
plt.plot([0, 0], [-b_val, b_val], 'g--', label="Minor axis")

# Draw the latus rectum through focus1.
# Its length L = 2b^2/a = 2*1/2 = 1, so endpoints are (a*e, ±L/2)
lr_y = np.array([-0.5, 0.5])
lr_x = np.full_like(lr_y, focus1[0])
plt.plot(lr_x, lr_y, 'm-', linewidth=2, label="Latus rectum")

plt.legend(), plt.grid(True)
plt.axis('equal')
plt.show()