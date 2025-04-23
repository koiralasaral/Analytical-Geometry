import matplotlib
matplotlib.use("TkAgg")  # You can try this if needed

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# ------------------------------------------------
# Program 2: Robotics Path Planning Using Potential Fields
# (Animation Duration: 15 seconds)
# ------------------------------------------------

# Obstacle: Elliptical obstacle (centered at (0,0)).
a_obs = 3   # semi-axis along x of obstacle
b_obs = 2   # semi-axis along y of obstacle

def f_obs(x, y, a, b):
    """Compute the ellipse implicit function value.
       f = (x^2)/(a^2) + (y^2)/(b^2) (f = 1 on the obstacle boundary)."""
    return (x**2)/(a**2) + (y**2)/(b**2)

def grad_f_obs(x, y, a, b):
    """Compute the gradient of f_obs at (x, y)."""
    dfdx = 2 * x / (a**2)
    dfdy = 2 * y / (b**2)
    return np.array([dfdx, dfdy])

# Start and goal positions.
start = np.array([-7.0, -7.0])
goal  = np.array([7.0, 7.0])

# Potential field parameters.
k_attr = 1.0       # Attractive gain: pulls the robot toward the goal.
k_rep  = 10.0      # Repulsive gain: pushes the robot away from the obstacle.
d0     = 1.5       # Threshold: repulsion is activated when f_obs(x,y) < d0.
# (f_obs(x,y) = 1 along the elliptical obstacle boundary.)

def attractive_force(pos):
    """Return the attractive force vector toward the goal."""
    return k_attr * (goal - pos)

def repulsive_force(pos):
    """Compute the repulsive force vector if the robot is close to the obstacle."""
    x, y = pos
    f_val = f_obs(x, y, a_obs, b_obs)
    if f_val < d0:
        # Compute repulsive force magnitude factor.
        factor = k_rep * (1.0/f_val - 1.0/d0) * (1.0 / (f_val**2))
        # Repulsion is directed along the gradient of f_obs.
        return factor * grad_f_obs(x, y, a_obs, b_obs)
    else:
        return np.array([0.0, 0.0])

# Simulation parameters.
dt = 0.05       # Time step (seconds)
num_steps = 300 # Fixed simulation steps for 15-second animation

# Initialize the robot's position.
pos = start.copy()
trajectory = [pos.copy()]

# Euler integration for potential field path planning.
for _ in range(num_steps):
    F_attr = attractive_force(pos)
    F_rep  = repulsive_force(pos)
    F_total = F_attr + F_rep
    pos = pos + dt * F_total
    trajectory.append(pos.copy())

trajectory = np.array(trajectory)

# ------------------------------------------------
# Set up the animation plot.
fig2, ax2 = plt.subplots(figsize=(8,8))
ax2.set_xlim(-8, 8)
ax2.set_ylim(-8, 8)
ax2.set_aspect('equal')
ax2.grid(True)
ax2.set_title("Potential Field Path Planning around an Elliptical Obstacle\n(15-second Animation)")

# Plot the obstacle (ellipse).
t = np.linspace(0, 2*np.pi, 400)
obs_x = a_obs * np.cos(t)
obs_y = b_obs * np.sin(t)
ax2.plot(obs_x, obs_y, 'k-', lw=2, label="Obstacle (Ellipse)")

# Plot the start and goal markers.
ax2.plot(start[0], start[1], 'go', markersize=8, label="Start")
ax2.plot(goal[0], goal[1], 'ro', markersize=8, label="Goal")

# Prepare the plot objects for the robot and its trajectory.
robot_point, = ax2.plot([], [], 'bo', markersize=6, label="Robot")
path_line, = ax2.plot([], [], 'b-', lw=1, label="Path")

def init_pf():
    """Initialization function for animation."""
    robot_point.set_data([], [])
    path_line.set_data([], [])
    return robot_point, path_line

def animate_pf(i):
    """Animation update: displays the robot’s position and path at frame i."""
    current = trajectory[i]
    # Wrap scalars in a list so that set_data receives sequences.
    robot_point.set_data([current[0]], [current[1]])
    path_line.set_data(trajectory[:i+1, 0], trajectory[:i+1, 1])
    return robot_point, path_line

# Set up FuncAnimation: 300 frames, each with an interval of 50ms (i.e., 15 seconds total).
ani_pf = animation.FuncAnimation(fig2, animate_pf, frames=len(trajectory),
                                 init_func=init_pf, interval=50, blit=False)

if __name__ == '__main__':
    ax2.legend()
    plt.show()