import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# ------------------------------------------------
# Program 1: Collision Detection with an Elliptical Obstacle
# ------------------------------------------------

# Define the elliptical obstacle parameters (centered at (0,0))
a_obs = 3    # semi-axis along x
b_obs = 2    # semi-axis along y

def is_inside_ellipse(x, y, a, b):
    """
    Returns True if point (x,y) lies inside (or on) the ellipse:
        (x/a)^2 + (y/b)^2 <= 1.
    """
    return (x**2)/(a**2) + (y**2)/(b**2) <= 1

# Define the robot's planned straight-line path.
start = np.array([-6, -4])
goal  = np.array([6, 4])
num_steps = 200
# Create a linear path from start to goal
path = np.linspace(start, goal, num_steps)

# Set up the plot.
fig, ax = plt.subplots(figsize=(8,6))
ax.set_xlim(-8, 8)
ax.set_ylim(-8, 8)
ax.set_aspect('equal')
ax.grid(True)
ax.set_title("Collision Detection with an Elliptical Obstacle")

# Plot the obstacle: draw the ellipse.
t = np.linspace(0, 2*np.pi, 400)
ellipse_x = a_obs * np.cos(t)
ellipse_y = b_obs * np.sin(t)
ax.plot(ellipse_x, ellipse_y, 'k-', lw=2, label="Obstacle (Ellipse)")

# Plot the path (the planned trajectory).
ax.plot(path[:,0], path[:,1], 'b--', lw=1, label="Planned Path")

# Mark start and goal.
ax.plot(start[0], start[1], 'go', markersize=8, label="Start")
ax.plot(goal[0], goal[1], 'ro', markersize=8, label="Goal")

# Create the robot as a circle (using a small radius).
r_robot = 0.3   # robot's "size"
robot_patch = plt.Circle((start[0], start[1]), r_robot, color='green')
ax.add_patch(robot_patch)

# Text for collision status.
collision_text = ax.text(-7, 7, "", fontsize=14, color='red')

def update_collision(frame):
    # Get the current robot position along the path.
    pos = path[frame]
    # Update the circle's center.
    robot_patch.center = (pos[0], pos[1])
    # Check collision: if the center is inside the ellipse, we declare collision.
    if is_inside_ellipse(pos[0], pos[1], a_obs, b_obs):
        robot_patch.set_color('red')             # change color on collision
        collision_text.set_text("Collision Detected!")
    else:
        robot_patch.set_color('green')
        collision_text.set_text("")
    return robot_patch, collision_text

collision_anim = animation.FuncAnimation(fig, update_collision,
                                           frames=num_steps, interval=50, blit=True)
ax.legend()
plt.show()