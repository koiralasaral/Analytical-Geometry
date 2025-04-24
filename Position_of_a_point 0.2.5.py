import sympy as sp
import numpy as np
import matplotlib.pyplot as plt

# =============================================================================
# Theoretical Methods for Ellipse Topics
# =============================================================================

class EllipseTheory:
    @staticmethod
    def position_of_point(a, b, point):
        """
        Determine the position of a point (x1, y1) relative to the ellipse:
            x²/a² + y²/b² = 1.
        Returns a tuple (position, value), where position is "Inside", "On", or "Outside"
        and value = x1²/a² + y1²/b² - 1.
        """
        x1, y1 = point
        value = x1**2 / a**2 + y1**2 / b**2 - 1
        if sp.N(value) > 0:
            pos = "Outside"
        elif sp.N(value) == 0:
            pos = "On the ellipse"
        else:
            pos = "Inside"
        return pos, sp.N(value)

    @staticmethod
    def sum_of_focal_distances(a, b, theta_value):
        """
        For a point P on the ellipse given in polar form:
            P = (a cosθ, b sinθ).
        The foci are at (±ae, 0) where e = sqrt(1 - b²/a²).
        Returns (sum, d1, d2) where sum is the sum of distances from P to the two foci.
        (For a point on the ellipse, the sum equals 2a.)
        """
        e = np.sqrt(1 - b**2 / a**2)
        P = np.array([a * np.cos(theta_value), b * np.sin(theta_value)])
        F1 = np.array([a * e, 0])
        F2 = np.array([-a * e, 0])
        d1 = np.linalg.norm(P - F1)
        d2 = np.linalg.norm(P - F2)
        return d1 + d2, d1, d2

    @staticmethod
    def polar_equation(a, b, num_points=200):
        """
        Derive the polar equation for the ellipse x²/a² + y²/b² = 1.
        Using the substitution x = r cosθ, y = r sinθ, we obtain:
            r = 1/sqrt((cos²θ)/a² + (sin²θ)/b²).
        Returns: θ array, r values, and (x,y) coordinates for plotting.
        """
        theta_vals = np.linspace(0, 2*np.pi, num_points)
        r_vals = 1/np.sqrt((np.cos(theta_vals)**2)/a**2 + (np.sin(theta_vals)**2)/b**2)
        x = r_vals * np.cos(theta_vals)
        y = r_vals * np.sin(theta_vals)
        return theta_vals, r_vals, x, y

    @staticmethod
    def plot_auxiliary_circle(a, ax=None):
        """
        Plot the auxiliary circle for an ellipse with semi‐major axis a.
        (The auxiliary circle is: x² + y² = a².)
        Returns (x_vals, y_vals) for the circle.
        """
        theta_vals = np.linspace(0, 2*np.pi, 300)
        x = a * np.cos(theta_vals)
        y = a * np.sin(theta_vals)
        if ax is None:
            ax = plt.gca()
        ax.plot(x, y, 'm--', linewidth=2, label="Auxiliary Circle")
        return x, y

    @staticmethod
    def plot_eccentric_angle_line(a, b, theta_value, ax=None):
        """
        For a point on the ellipse given by (a cosθ, b sinθ),
        plot the line through the origin (the eccentric angle direction) for the corresponding
        parameter θ on the auxiliary circle, i.e. (a cosθ, a sinθ).
        Returns the point on the ellipse and the corresponding point on the auxiliary circle.
        """
        if ax is None:
            ax = plt.gca()
        P = (a * np.cos(theta_value), b * np.sin(theta_value))
        aux_pt = (a * np.cos(theta_value), a * np.sin(theta_value))
        ax.plot([0, aux_pt[0]], [0, aux_pt[1]], 'c--', linewidth=2, label="Eccentric Angle Direction")
        ax.plot(P[0], P[1], 'ko', markersize=8, label="Point on Ellipse")
        return P, aux_pt

# =============================================================================
# Demonstration for the Requested Topics
# =============================================================================

if __name__ == "__main__":
    # Common parameters for demonstration:
    a_val = 5    # semi–major axis for demonstration
    b_val = 3    # semi–minor axis

    # -------------------------------------------------------------------------
    # 1. POSITION OF A POINT WITH RESPECT TO THE ELLIPSE
    # -------------------------------------------------------------------------
    point = (2, 1)  # test point
    pos, F_val = EllipseTheory.position_of_point(a_val, b_val, point)
    print(f"Position of point {point}: {pos} (F = {F_val})")
    
    # Plot the ellipse and the point
    theta = np.linspace(0,2*np.pi,400)
    x_ellipse = a_val * np.cos(theta)
    y_ellipse = b_val * np.sin(theta)
    plt.figure(figsize=(6,6))
    plt.plot(x_ellipse, y_ellipse, 'b-', label="Ellipse: x²/a² + y²/b² = 1")
    plt.plot(point[0], point[1], 'ro', markersize=8, label=f"Point {point} ({pos})")
    plt.title("Position of a Point Relative to an Ellipse")
    plt.xlabel("x"), plt.ylabel("y")
    plt.legend(), plt.grid(True)
    plt.axis("equal")
    plt.show()
    
    # -------------------------------------------------------------------------
    # 2. SUM OF THE FOCAL DISTANCES OF A POINT ON THE ELLIPSE
    # -------------------------------------------------------------------------
    theta_val = np.pi/3  # choose a parameter
    sum_d, d1, d2 = EllipseTheory.sum_of_focal_distances(a_val, b_val, theta_val)
    print(f"For a point P at θ={theta_val:.2f} rad, d1 = {d1:.3f}, d2 = {d2:.3f}, and d1+d2 = {sum_d:.3f} (should equal 2a = {2*a_val})")
    
    # Plot the ellipse, its foci, and the segments from P to the foci.
    e_val = np.sqrt(1 - b_val**2/a_val**2)
    F1 = (a_val*e_val, 0)
    F2 = (-a_val*e_val, 0)
    P_point = (a_val*np.cos(theta_val), b_val*np.sin(theta_val))
    plt.figure(figsize=(6,6))
    plt.plot(x_ellipse, y_ellipse, 'b-', label="Ellipse")
    plt.plot(F1[0], F1[1], 'ro', markersize=8, label="Focus 1")
    plt.plot(F2[0], F2[1], 'ro', markersize=8, label="Focus 2")
    plt.plot(P_point[0], P_point[1], 'ko', markersize=8, label="Point P")
    plt.plot([P_point[0], F1[0]], [P_point[1], F1[1]], 'g--', linewidth=2, label="P-Focus1")
    plt.plot([P_point[0], F2[0]], [P_point[1], F2[1]], 'g--', linewidth=2, label="P-Focus2")
    plt.title("Sum of Focal Distances for a Point on the Ellipse")
    plt.xlabel("x"), plt.ylabel("y")
    plt.legend(), plt.grid(True)
    plt.axis("equal")
    plt.show()
    
    # -------------------------------------------------------------------------
    # 3. POLAR EQUATION OF THE ELLIPSE
    # -------------------------------------------------------------------------
    theta_vals, r_vals, x_pol, y_pol = EllipseTheory.polar_equation(a_val, b_val)
    plt.figure(figsize=(6,6))
    plt.plot(x_pol, y_pol, 'm-', linewidth=2, label="Polar form of Ellipse")
    plt.title("Polar Equation of the Ellipse")
    plt.xlabel("x"), plt.ylabel("y")
    plt.legend(), plt.grid(True)
    plt.axis("equal")
    plt.show()
    
    # -------------------------------------------------------------------------
    # 4. AUXILIARY CIRCLE OF THE ELLIPSE
    # -------------------------------------------------------------------------
    plt.figure(figsize=(6,6))
    plt.plot(x_ellipse, y_ellipse, 'b-', linewidth=2, label="Ellipse")
    EllipseTheory.plot_auxiliary_circle(a_val)
    plt.title("Auxiliary Circle of the Ellipse (x²+y² = a²)")
    plt.xlabel("x"), plt.ylabel("y")
    plt.legend(), plt.grid(True)
    plt.axis("equal")
    plt.show()
    
    # -------------------------------------------------------------------------
    # 5. ECCENTRIC ANGLE
    # -------------------------------------------------------------------------
    # A point on the ellipse in parametric form is given by (a cos θ, b sin θ).
    # Its "eccentric angle" is the parameter θ. Its corresponding point on the
    # auxiliary circle is (a cos θ, a sin θ).
    plt.figure(figsize=(6,6))
    plt.plot(x_ellipse, y_ellipse, 'b-', linewidth=2, label="Ellipse")
    EllipseTheory.plot_auxiliary_circle(a_val, plt.gca())
    theta_demo = np.pi/4
    P_ecc, aux_point = EllipseTheory.plot_eccentric_angle_line(a_val, b_val, theta_demo, plt.gca())
    plt.text(aux_point[0]*0.7, aux_point[1]*0.7, f"θ = {theta_demo:.2f}", color="purple", fontsize=12)
    plt.title("Eccentric Angle & Auxiliary Circle")
    plt.xlabel("x"), plt.ylabel("y")
    plt.legend(), plt.grid(True)
    plt.axis("equal")
    plt.show()