import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from mpl_toolkits.mplot3d import Axes3D  # for 3D plotting

# ========================================================
# Global Ellipse Parameters and Static Geometry Definitions
# ========================================================
a = 5                 # Semi-major axis
b = 3                 # Semi-minor axis
c = np.sqrt(a**2 - b**2)  # Focal distance
e = c / a             # Eccentricity

# Create static curves: ellipse and auxiliary circle
theta = np.linspace(0, 2*np.pi, 400)
ellipse_x = a * np.cos(theta)
ellipse_y = b * np.sin(theta)

aux_circle_x = a * np.cos(theta)
aux_circle_y = a * np.sin(theta)

# Directrix (right-side) is at x = a/e
x_directrix = a / e

# Latus rectum for the right focus: endpoints at (c, ±b²/a)
latus_y_top = b**2 / a
latus_y_bot = -b**2 / a

# ========================================================
# 2D Animation: Dynamic Geometry for Varying Eccentric Angles
# ========================================================
fig2d, ax2d = plt.subplots(figsize=(8, 8))

# Plot static geometry
ax2d.plot(ellipse_x, ellipse_y, 'b-', lw=2, label="Ellipse")
ax2d.plot(aux_circle_x, aux_circle_y, 'g--', lw=1.5, label="Auxiliary Circle")
ax2d.axhline(0, color='r', linestyle='--', label="Major Axis (Base)")
ax2d.axvline(0, color='purple', linestyle='--', label="Minor Axis")
ax2d.plot([c, -c], [0, 0], 'r*', markersize=12, label="Foci")
ax2d.plot([c, c], [latus_y_top, latus_y_bot], 'y-', lw=3, label="Latus Rectum")
ax2d.axvline(x_directrix, color='orange', linestyle='-', 
             label=f"Directrix (x = {x_directrix:.3f})")
ax2d.set_xlim(-a-1, a+1)
ax2d.set_ylim(-a-1, a+1)
ax2d.set_aspect('equal', adjustable='box')
ax2d.grid(True)
ax2d.legend(loc="upper right", fontsize=8)

# Create animated (dynamic) artists with initial empty data
chord_line, = ax2d.plot([], [], 'r-', lw=2, label="Chord")
ray1_line, = ax2d.plot([], [], 'c-', lw=2, label=r"Eccentric ray for $\phi$")
ray2_line, = ax2d.plot([], [], 'c-', lw=2, label=r"Eccentric ray for $\phi'$")
perp1_line, = ax2d.plot([], [], 'k:', lw=2, label=r"Perp drop for $\phi$")
perp2_line, = ax2d.plot([], [], 'k:', lw=2, label=r"Perp drop for $\phi'$")
point_P_aux, = ax2d.plot([], [], 'ko', markersize=6, label=r"Aux. Pt $\phi$")
point_Q_aux, = ax2d.plot([], [], 'ko', markersize=6, label=r"Aux. Pt $\phi'$")
point_P, = ax2d.plot([], [], 'bo', markersize=6, label=r"Ellipse Pt $\phi$")
point_Q, = ax2d.plot([], [], 'bo', markersize=6, label=r"Ellipse Pt $\phi'$")

def update_2d(frame):
    """
    Animate the 2D geometry by updating positions of the dynamic objects.
    The eccentric angles vary with time.
    """
    # Base angles (in radians) with small oscillatory variations:
    base_phi = np.radians(30)
    base_phi_dash = np.radians(70)
    phi = base_phi + np.radians(10) * np.sin(0.05 * frame)
    phi_dash = base_phi_dash + np.radians(10) * np.cos(0.05 * frame)
    
    # Points on the auxiliary circle (where the angles are formed)
    P_aux = np.array([a * np.cos(phi), a * np.sin(phi)])
    Q_aux = np.array([a * np.cos(phi_dash), a * np.sin(phi_dash)])
    
    # Corresponding points on the ellipse
    P = np.array([a * np.cos(phi), b * np.sin(phi)])
    Q = np.array([a * np.cos(phi_dash), b * np.sin(phi_dash)])
    
    # Update chord joining the ellipse points
    chord_line.set_data([P[0], Q[0]], [P[1], Q[1]])
    
    # Update eccentric rays (from origin to auxiliary circle points)
    ray1_line.set_data([0, P_aux[0]], [0, P_aux[1]])
    ray2_line.set_data([0, Q_aux[0]], [0, Q_aux[1]])
    
    # Update vertical drops (perpendiculars) from auxiliary circle points to the base (y=0)
    perp1_line.set_data([P_aux[0], P_aux[0]], [P_aux[1], 0])
    perp2_line.set_data([Q_aux[0], Q_aux[0]], [Q_aux[1], 0])
    
    # Update point markers (each as a sequence with one element)
    point_P_aux.set_data([P_aux[0]], [P_aux[1]])
    point_Q_aux.set_data([Q_aux[0]], [Q_aux[1]])
    point_P.set_data([P[0]], [P[1]])
    point_Q.set_data([Q[0]], [Q[1]])
    
    return (chord_line, ray1_line, ray2_line, perp1_line, perp2_line,
            point_P_aux, point_Q_aux, point_P, point_Q)

anim2d = FuncAnimation(fig2d, update_2d, frames=200, interval=50, blit=False)


# ========================================================
# 3D Animation: Rotating the 2D Geometry in 3D
# ========================================================
fig3d = plt.figure(figsize=(10, 10))
ax3d = fig3d.add_subplot(111, projection='3d')

# Plot the same static outlines (drawn in the z=0 plane)
ax3d.plot(ellipse_x, ellipse_y, zs=0, zdir='z', color='b', lw=2, label="Ellipse")
ax3d.plot(aux_circle_x, aux_circle_y, zs=0, zdir='z', color='g', linestyle='--', lw=1.5, label="Auxiliary Circle")
ax3d.plot([-a-1, a+1], [0, 0], zs=0, zdir='z', color='r', linestyle='--', label="Major Axis")
ax3d.plot([0, 0], [-a-1, a+1], zs=0, zdir='z', color='purple', linestyle='--', label="Minor Axis")
ax3d.plot([c], [0], [0], 'r*', markersize=12, label="Focus")
ax3d.plot([-c], [0], [0], 'r*', markersize=12)
ax3d.plot([c, c], [latus_y_top, latus_y_bot], [0, 0], 'y-', lw=3, label="Latus Rectum")
ax3d.plot([x_directrix, x_directrix], [-a-1, a+1], [0, 0], color='orange', lw=2, 
          label=f"Directrix (x = {x_directrix:.3f})")

# Set 3D axes limits and aspect
ax3d.set_xlim([-a-1, a+1])
ax3d.set_ylim([-a-1, a+1])
ax3d.set_zlim([-a/2, a/2])
ax3d.set_box_aspect([1, 1, 0.5])
ax3d.legend(loc="upper right", fontsize=8)

def update_3d(frame):
    """
    Update function for the 3D animation; simply rotates the view.
    """
    ax3d.view_init(elev=30, azim=frame)
    return ax3d

anim3d = FuncAnimation(fig3d, update_3d, frames=np.arange(0, 360, 2), interval=50, blit=False)

# ========================================================
# Display the Animations
# ========================================================
plt.show()

# ========================================================
# Print Key Equations and Geometric Details
# ========================================================
print("Ellipse equation: (x²)/({}²) + (y²)/({}²) = 1".format(a, b))
print("Major axis: y = 0")
print("Minor axis: x = 0")
print("Foci: ({:.3f}, 0) and ({:.3f}, 0)".format(c, -c))
print("Latus rectum endpoints (for right focus): x = {:.3f}, y = ±{:.3f}".format(c, b**2/a))
print("Directrix: x = {:.3f}".format(x_directrix))
print("\nChord equation (joining ellipse points corresponding to φ and φ'):")
# The chord equation logic (derived from points) would be:
# A = b*(sin(phi_dash)-sin(phi)), B = a*(cos(phi_dash)-cos(phi)), C = a*b*sin(phi-phi_dash)
# Here we display the form for reference.
print("Chord: A*x + B*y + C = 0   (A, B, C depend on φ and φ')")
print("Eccentric ray equations: y = tan(φ)*x and y = tan(φ')*x")
print("Perpendicular drop from auxiliary circle points: vertical lines at x = P_aux[0] and Q_aux[0]")
