import numpy as np
import matplotlib.pyplot as plt

def geometrical_properties_linear_algebra(a, b, theta):
    """
    Uses linear algebra to compute:
      - P, a point on the ellipse: P = (a cosθ, b sinθ)
      - Tangent line at P in vector form (via the gradient)
          * u = (x0/a^2, y0/b^2), so the tangent is uᵀ·[x,y] = 1.
      - T, the intersection of the tangent with the x-axis:
          set y = 0 and solve for x.
      - t, the intersection of the tangent with the y-axis:
          set x = 0 and solve for y.
      - N: The projection of P onto the x-axis (using v_x = (1,0)).
      - M: The projection of P onto the y-axis (using v_y = (0,1)).
      
    Returns a dictionary with:
        P, T, t, N, M, CN, CT, CM, Ct.
    """
    # Point on the ellipse: P = (a*cosθ, b*sinθ)
    x0 = a * np.cos(theta)
    y0 = b * np.sin(theta)
    P = np.array([x0, y0])
    
    # Construct the "normal" vector used in the tangent's linear form:
    # u = (x0/a^2, y0/b^2) so that u • P = 1.
    u = np.array([x0/(a**2), y0/(b**2)])
    
    # The tangent is given by uᵀ·[x, y] = 1.
    # Intersection with x-axis (y=0): u_x * x = 1  ⇒  x = 1/u_x.
    if np.abs(u[0]) > 1e-9:
        T = np.array([1/u[0], 0])
    else:
        T = np.array([np.nan, np.nan])  # Degenerate
    # Intersection with y-axis (x=0): u_y * y = 1  ⇒  y = 1/u_y.
    if np.abs(u[1]) > 1e-9:
        t_pt = np.array([0, 1/u[1]])
    else:
        t_pt = np.array([np.nan, np.nan])
    
    # Use vector projection to determine the feet of perpendiculars:
    # Projection of P onto the x–axis:
    v_x = np.array([1, 0])
    N = (np.dot(P, v_x)/np.dot(v_x, v_x)) * v_x  # results in (x0, 0)
    # Projection of P onto the y–axis:
    v_y = np.array([0, 1])
    M = (np.dot(P, v_y)/np.dot(v_y, v_y)) * v_y  # results in (0, y0)
    
    # Distances from the center C = (0,0)
    CN = np.linalg.norm(N)       # = |x0|
    CT = np.linalg.norm(T)       # = |a^2/x0|
    CM = np.linalg.norm(M)       # = |y0|
    Ct = np.linalg.norm(t_pt)    # = |b^2/y0|
    
    return {
        'P': P,
        'T': T,
        't': t_pt,
        'N': N,
        'M': M,
        'CN': CN,
        'CT': CT,
        'Prod_major': CN * CT,  # should equal a^2
        'CM': CM,
        'Ct': Ct,
        'Prod_minor': CM * Ct   # should equal b^2
    }

# ----------------------------
# Demonstration for Section 0.6(1)
# ----------------------------
a_val = 5.0  # semi–major axis
b_val = 3.0  # semi–minor axis
theta_val = np.pi/4  # 45 degrees

# Compute properties using linear algebra
results = geometrical_properties_linear_algebra(a_val, b_val, theta_val)
for k, v in results.items():
    print(f"{k}: {v}")

# Plot the ellipse, point P, tangent, and intersections using vector techniques.
theta_arr = np.linspace(0, 2*np.pi, 400)
x_ell = a_val * np.cos(theta_arr)
y_ell = b_val * np.sin(theta_arr)

plt.figure(figsize=(8,8))
plt.plot(x_ell, y_ell, 'b-', linewidth=2, label="Ellipse: $x^2/a^2+y^2/b^2=1$")

# Plot the center C at (0,0)
plt.plot(0, 0, 'ko', label="Center C")

# Plot point P
P = results['P']
plt.plot(P[0], P[1], 'ro', markersize=8, label="Point P")
plt.text(P[0]*1.05, P[1]*1.05, "P", color="red", fontsize=12)

# Plot tangent line at P:
# The tangent is given by: uᵀ·[x, y] = 1, with u computed above.
# A direction vector for the tangent is any vector orthogonal to u; we choose d = (-u[1], u[0])
u = np.array([P[0]/(a_val**2), P[1]/(b_val**2)])
d = np.array([-u[1], u[0]])  # direction vector for the tangent
t_param = np.linspace(-10, 10, 300)
tangent_points = results['T'].reshape(2,1) + np.outer(d, t_param)
plt.plot(tangent_points[0, :], tangent_points[1, :], 'r--', linewidth=2, label="Tangent at P")

# Plot intersections of tangent with the axes, T and t.
plt.plot(results['T'][0], results['T'][1], 'go', markersize=10, label="Intersection T (x-axis)")
plt.text(results['T'][0] + 0.1, results['T'][1] - 0.2, "T", color="green", fontsize=12)
plt.plot(results['t'][0], results['t'][1], 'mo', markersize=10, label="Intersection t (y-axis)")
plt.text(results['t'][0] + 0.1, results['t'][1] - 0.2, "t", color="magenta", fontsize=12)

# Plot projections (using vector projection concept)
plt.plot(results['N'][0], results['N'][1], 'co', markersize=8, label="Projection N (to x-axis)")
plt.plot(results['M'][0], results['M'][1], 'yo', markersize=8, label="Projection M (to y-axis)")

# Draw perpendicular lines from P to axes
plt.plot([P[0], results['N'][0]], [P[1], results['N'][1]], 'k--', label="Perpendicular to x-axis")
plt.plot([P[0], results['M'][0]], [P[1], results['M'][1]], 'k-.', label="Perpendicular to y-axis")

# Annotations and labels
plt.title("Geometrical Properties of an Ellipse using Linear Algebra (Section 0.6(1))")
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.grid(True)
plt.axis("equal")
plt.show()