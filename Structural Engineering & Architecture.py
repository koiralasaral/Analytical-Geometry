import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Program 3: Structural Engineering & Architecture
# Example: Elliptical arch with a = 8 m and b = 6 m.
a = 8.0
b = 6.0

def arch_properties(theta):
    """
    Compute for a given angle theta:
      - P: point on the ellipse (arch)
      - Tangent intersections T (x-axis) and t (y-axis)
      - Projections: N = (a*cos(theta), 0) and M = (0, b*sin(theta))
      Returns:
         P, T, t, CN, CT, CM, Ct.
    """
    x0 = a * np.cos(theta)
    y0 = b * np.sin(theta)
    P = np.array([x0, y0])
    u = np.array([np.cos(theta)/a, np.sin(theta)/b])
    T = np.array([1/u[0], 0]) if np.abs(u[0]) > 1e-9 else np.array([np.nan, np.nan])
    t_pt = np.array([0, 1/u[1]]) if np.abs(u[1]) > 1e-9 else np.array([np.nan, np.nan])
    
    # Projection vectors onto axes
    N = np.array([x0, 0])
    M = np.array([0, y0])
    
    CN = np.abs(x0)
    CT = np.abs(T[0])
    CM = np.abs(y0)
    Ct = np.abs(t_pt[1])
    
    return P, T, t_pt, CN, CT, CM, Ct

fig3, ax3 = plt.subplots(figsize=(8,8))
theta_vals = np.linspace(0, 2*np.pi, 400)
x_arch = a * np.cos(theta_vals)
y_arch = b * np.sin(theta_vals)
ax3.plot(x_arch, y_arch, 'b-', lw=2, label="Elliptical Arch")
ax3.set_xlim(-a-1, a+1)
ax3.set_ylim(-b-1, b+1)
ax3.set_aspect("equal")
ax3.grid(True)
ax3.set_title("Program 3 (Structural Eng.): Elliptical Arch Invariants")

# Artists for animated objects:
point_P, = ax3.plot([], [], 'ro', markersize=8, label="Point P on Arch")
tangent_line, = ax3.plot([], [], 'r--', lw=2, label="Tangent at P")
int_T, = ax3.plot([], [], 'go', markersize=8, label="Intersection T on x-axis")
int_t, = ax3.plot([], [], 'mo', markersize=8, label="Intersection t on y-axis")
line_perp_x, = ax3.plot([], [], 'k--', lw=1, label="Projection: Perp to x-axis")
line_perp_y, = ax3.plot([], [], 'k-.', lw=1, label="Projection: Perp to y-axis")
prod_text = ax3.text(-a, a-1, "", fontsize=12, color="purple")

def update_arch(theta):
    P, T, t_pt, CN, CT, CM, Ct = arch_properties(theta)
    point_P.set_data([P[0]], [P[1]])
    int_T.set_data([T[0]], [T[1]])
    int_t.set_data([t_pt[0]], [t_pt[1]])
    
    u = np.array([np.cos(theta)/a, np.sin(theta)/b])
    # Tangent direction vector, perpendicular to u:
    d = np.array([-u[1], u[0]])
    t_range = np.linspace(-10, 10, 100)
    tangent_pts = T.reshape(2,1) + np.outer(d, t_range)
    tangent_line.set_data(tangent_pts[0,:], tangent_pts[1,:])
    
    # Draw perpendicular lines from P onto the x and y axes:
    line_perp_x.set_data([P[0], P[0]], [P[1], 0])
    line_perp_y.set_data([P[0], 0], [P[1], P[1]])
    
    prod_major = CN * CT   # should equal a^2
    prod_minor = CM * Ct   # should equal b^2
    prod_text.set_text(f"CN·CT = {prod_major:.1f} (a² = {a**2:.1f})\nCM·Ct = {prod_minor:.1f} (b² = {b**2:.1f})")
    
    return point_P, tangent_line, int_T, int_t, line_perp_x, line_perp_y, prod_text

anim3 = FuncAnimation(fig3, update_arch,
                      frames=np.linspace(0, 2*np.pi, 200),
                      interval=50, blit=True)
ax3.legend(loc='upper right')
plt.show()