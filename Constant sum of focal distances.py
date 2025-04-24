import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Ellipse parameters
a = 5.0
b = 3.0
e = np.sqrt(1 - b**2 / a**2)
F1 = np.array([a*e, 0])
F2 = np.array([-a*e, 0])

fig, ax = plt.subplots(figsize=(8,8))
theta_vals = np.linspace(0, 2*np.pi, 400)
x_ellipse = a * np.cos(theta_vals)
y_ellipse = b * np.sin(theta_vals)
ax.plot(x_ellipse, y_ellipse, 'b-', label="Ellipse")
ax.plot(F1[0], F1[1], 'ro', label="Focus F1")
ax.plot(F2[0], F2[1], 'ro', label="Focus F2")
ax.set_xlim(-a-1, a+1)
ax.set_ylim(-b-1, b+1)
ax.set_aspect('equal')
ax.grid(True)
 
# Create artist objects for the animated elements.
# Note: set_data expects sequences (lists/tuples) even for a single point.
point_P, = ax.plot([], [], 'ko', markersize=6, label="P")
line_F1, = ax.plot([], [], 'g--', lw=2, label="P-F1")
line_F2, = ax.plot([], [], 'm--', lw=2, label="P-F2")
text_sum = ax.text(-a, a, "", fontsize=12, color="purple")

def update_focal(theta):
    # theta is a scalar.
    P = np.array([a * np.cos(theta), b * np.sin(theta)])
    d1 = np.linalg.norm(P - F1)
    d2 = np.linalg.norm(P - F2)
    sum_d = d1 + d2
    
    # Wrap scalar values in lists:
    point_P.set_data([P[0]], [P[1]])
    line_F1.set_data([P[0], F1[0]], [P[1], F1[1]])
    line_F2.set_data([P[0], F2[0]], [P[1], F2[1]])
    text_sum.set_text(f"Sum = {sum_d:.2f} (2a = {2*a:.2f})")
    
    return point_P, line_F1, line_F2, text_sum

# Create the animation by passing the update function and the frames as a sequence.
anim2 = FuncAnimation(fig,
                      update_focal,
                      frames=np.linspace(0, 2*np.pi, 200),
                      interval=50,
                      blit=True)

plt.title("Animation 2: Constant Sum of Focal Distances")
ax.legend(loc='upper right')
plt.show()