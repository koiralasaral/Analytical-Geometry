import numpy as np
import matplotlib.pyplot as plt

def geometrical_properties(a, b, theta):
    """
    Given ellipse parameters a and b and an eccentric angle theta,
    compute:
      - P = (a*cosθ, b*sinθ) on the ellipse;
      - Tangent line at P;
      - T = Intersection of tangent with the x-axis;
      - t = Intersection of tangent with the y-axis;
      - Verify CN*CT = a² and CM*Ct = b².
      
    Returns a dictionary with the computed points and products.
    """
    # Point on the ellipse
    x0 = a * np.cos(theta)
    y0 = b * np.sin(theta)
    P = np.array([x0, y0])
    
    # Equation of tangent: (x0*x)/a^2 + (y0*y)/b^2 = 1
    
    # Intersection with the x-axis: set y = 0.
    # Then: (x0*x)/a^2 = 1   -->  x = a^2/x0.
    T = np.array([a**2 / x0, 0])
    
    # Intersection with the y-axis: set x = 0.
    # Then: (y0*y)/b^2 = 1  -->  y = b^2/y0.
    t_point = np.array([0, b**2 / y0])
    
    # CN is the distance from center (0,0) to N, the foot of the perpendicular from P onto the x-axis.
    # N is simply (x0, 0). Thus, CN = |x0|
    CN = np.abs(x0)
    # CT is the distance from center to T.
    CT = np.abs(T[0])
    
    # Similarly, the perpendicular from P to the y-axis has foot M=(0,y0),
    # so CM = |y0|, and Ct is the distance from center to t_point.
    CM = np.abs(y0)
    Ct = np.abs(t_point[1])
    
    prod_major = CN * CT
    prod_minor = CM * Ct
    
    return {
        'P': P,
        'T': T,
        't': t_point,
        'CN': CN,
        'CT': CT,
        'Prod_major (should be a^2)': prod_major,
        'CM': CM,
        'Ct': Ct,
        'Prod_minor (should be b^2)': prod_minor
    }

# Parameters: choose an ellipse with a and b
a_val = 5.0   # semi-major axis
b_val = 3.0   # semi-minor axis

# Choose an eccentric angle theta for the point on the ellipse.
theta_val = np.pi/4  # 45° in radians

# Compute the geometrical properties.
results = geometrical_properties(a_val, b_val, theta_val)
for key, value in results.items():
    print(f"{key}: {value}")

# Now plot the ellipse, the point P, the tangent line at P, and the intersections with axes.

# Create a plot for the ellipse:
theta_vals = np.linspace(0, 2*np.pi, 400)
x_ellipse = a_val * np.cos(theta_vals)
y_ellipse = b_val * np.sin(theta_vals)

plt.figure(figsize=(8,8))
plt.plot(x_ellipse, y_ellipse, 'b-', label="Ellipse: x²/a² + y²/b² = 1")

# Plot center, C=(0,0)
plt.plot(0, 0, 'ko', label="Center C")

# Plot P
P = results['P']
plt.plot(P[0], P[1], 'ko', markersize=8, label="Point P")
plt.text(P[0]*1.05, P[1]*1.05, "P", color="black", fontsize=12)

# Plot tangent line at P:
# The tangent equation: (x0*x)/a^2 + (y0*y)/b^2 = 1
# Solve for y: y = (b^2/(y0))*(1 - (x0*x)/a^2) 
# (This formula works provided y0 != 0; if y0=0 then the tangent is horizontal.)
x_line = np.linspace(-a_val-1, a_val+1, 300)
if np.abs(P[1]) > 1e-6:
    y_line = (b_val**2/(P[1])) * (1 - (P[0]*x_line)/(a_val**2))
else:
    y_line = np.zeros_like(x_line)  # horizontal line
plt.plot(x_line, y_line, 'r-', linewidth=2, label="Tangent at P")

# Compute intersections:
T = results['T']  # Intersection with x-axis
t_point = results['t']  # Intersection with y-axis

plt.plot(T[0], T[1], 'go', markersize=8, label="Intersection T on x-axis")
plt.text(T[0]+0.1, T[1]-0.2, "T", color="green", fontsize=12)
plt.plot(t_point[0], t_point[1], 'mo', markersize=8, label="Intersection t on y-axis")
plt.text(t_point[0]+0.1, t_point[1]-0.2, "t", color="magenta", fontsize=12)

# Draw perpendicular from P to x-axis (major axis) with dashed line.
plt.plot([P[0], P[0]], [P[1], 0], 'k--', label="Perpendicular from P to x-axis")
# Draw perpendicular from P to y-axis (minor axis) with dashed line.
plt.plot([P[0], 0], [P[1], P[1]], 'k-.', label="Perpendicular from P to y-axis")

plt.title("Geometrical Properties of an Ellipse (Section 0.6 (1))")
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.grid(True)
plt.axis("equal")
plt.show()