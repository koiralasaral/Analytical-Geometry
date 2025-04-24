import sympy as sp
import numpy as np
import matplotlib.pyplot as plt

# ***********************
# THEORETICAL METHODS 
# ***********************

class EllipseTheory:
    @staticmethod
    def compute_eccentricity_from_latus(b):
        """
        Example 10:
        For an ellipse: x²/a² + y²/b² = 1 with Latus rectum L = 2b²/a.
        The condition "latus rectum is half the minor axis" means:
            L = (1/2)*(2b) = b.
        Hence, 2b²/a = b  ==>  a = 2b.
        Then eccentricity: e = sqrt(1 - (b²/a²)).
        """
        a = 2 * b
        e = np.sqrt(1 - (b**2) / (a**2))
        return a, e

    @staticmethod
    def plot_ellipse(a, b, title="Ellipse", color="blue", show=True):
        """Utility function to plot an ellipse x²/a² + y²/b² = 1."""
        theta = np.linspace(0, 2*np.pi, 400)
        x = a * np.cos(theta)
        y = b * np.sin(theta)
        plt.plot(x, y, color=color, label=title)
        plt.axis('equal')
        if show:
            plt.show()

    @staticmethod
    def fit_ellipse_through_points(p1, p2):
        """
        Example 11:
        Finds ellipse parameters (a, b) such that
           x²/a² + y²/b² = 1
        holds for two given points p1 = (x1, y1) and p2 = (x2, y2).
        By noting that if we set X = 1/a² and Y = 1/b² then:
            x1²*X + y1²*Y = 1   and   x2²*X + y2²*Y = 1.
        Returns a and b.
        """
        x1, y1 = p1
        x2, y2 = p2
        X, Y = sp.symbols('X Y', positive=True)
        eq1 = sp.Eq(x1**2 * X + y1**2 * Y, 1)
        eq2 = sp.Eq(x2**2 * X + y2**2 * Y, 1)
        sol = sp.solve([eq1, eq2], (X, Y), dict=True)[0]
        a_sq = 1 / sol[X]
        b_sq = 1 / sol[Y]
        return sp.sqrt(a_sq), sp.sqrt(b_sq)
    
    @staticmethod
    def ellipse_from_minor_and_focal(b, focal_distance):
        """
        Example 12:
        For an ellipse with minor axis length 2b and foci at (±ae, 0) such that
           focal separation = 2ae,
        we have e = (focal_distance)/(2a) and the relation:
           b² = a² (1 - e²).
        In Example 12, with b = 2 and focal_distance = 2, we recover a² = 5.
        Returns a, b, and e.
        """
        # Use: b^2 = a^2 - (focal_distance^2)/4  ==>  a^2 = b^2 + (focal_distance^2)/4.
        a = np.sqrt(b**2 + (focal_distance**2) / 4)
        e = focal_distance / (2 * a)
        return a, b, e

    @staticmethod
    def ellipse_from_latus_and_ecc(L, e):
        """
        Example 13:
        For an ellipse, the latus rectum L = 2b²/a and b² = a²(1-e²).
        Thus, L = 2a(1-e²). Then a = L/(2(1-e²)) and b = a*sqrt(1-e²).
        Returns a, b, and e.
        """
        a = L / (2 * (1 - e**2))
        b = a * np.sqrt(1 - e**2)
        return a, b, e

    @staticmethod
    def ellipse_from_focal_perp(a):
        """
        Example 14:
        If the line segments from the focus S=(ae,0) to the minor-axis endpoint (0,b)
        are perpendicular then b² = a²e². Also, b² = a²(1-e²). Equate to get:
            e² = 1 - e²   ->   e = 1/√2.
        Then b = a*sqrt(1 - e²).
        Here a is provided (from major-axis 2a).
        Returns a, b, and e.
        """
        e = 1 / np.sqrt(2)
        b = a * np.sqrt(1 - e**2)
        return a, b, e

    @staticmethod
    def rational_parametrization(a, b, t):
        """
        Example 15:
        Returns the point (x,y) by the rational parametrization:
            x = a(1-t²)/(1+t²),   y = (2b*t)/(1+t²).
        """
        x = a * (1 - t**2) / (1 + t**2)
        y = 2 * b * t / (1 + t**2)
        return x, y

    @staticmethod
    def verify_rational_parametrization(a, b):
        """
        Example 15:
        Symbolically verify that x²/a² + y²/b² = 1 when
            x = a(1-t²)/(1+t²),   y = 2b*t/(1+t²).
        Returns the symbolic expression (should simplify to 1).
        """
        t = sp.symbols('t', real=True)
        x_expr = a * (1 - t**2) / (1 + t**2)
        y_expr = 2 * b * t / (1 + t**2)
        expr = sp.simplify(x_expr**2 / a**2 + y_expr**2 / b**2)
        return expr

# *******************************
# DEMONSTRATION FOR EXAMPLES 10-15
# *******************************

if __name__ == "__main__":
    # ------- Example 10 -------
    print("=== Example 10 ===")
    # Compute the eccentricity when Latus rectum L = b (i.e. latus rectum is half the minor axis)
    b_ex10 = 1.0
    a_ex10, e_ex10 = EllipseTheory.compute_eccentricity_from_latus(b_ex10)
    print(f"For b = {b_ex10}, we get a = {a_ex10} and eccentricity e = {e_ex10:.3f}")
    
    plt.figure(figsize=(6,6))
    EllipseTheory.plot_ellipse(a_ex10, b_ex10, title="Example 10 Ellipse", color="blue", show=False)
    # Mark foci
    focus1 = (a_ex10 * e_ex10, 0)
    focus2 = (-a_ex10 * e_ex10, 0)
    plt.plot(focus1[0], focus1[1], 'ro', label="Focus 1")
    plt.plot(focus2[0], focus2[1], 'ro', label="Focus 2")
    # Draw the minor axis (vertical line)
    plt.plot([0, 0], [-b_ex10, b_ex10], 'g--', label="Minor axis")
    # Latus rectum through Focus 1: length = b_ex10, so endpoints at (a_ex10*e_ex10, ±b_ex10/2)
    lr_y = np.array([-b_ex10/2, b_ex10/2])
    lr_x = np.full_like(lr_y, focus1[0])
    plt.plot(lr_x, lr_y, 'm-', linewidth=2, label="Latus rectum")
    plt.title("Example 10: Ellipse with Latus rectum = b")
    plt.xlabel("x"); plt.ylabel("y")
    plt.legend()
    plt.grid(True)
    plt.axis("equal")
    plt.show()
    
    # ------- Example 11 -------
    print("\n=== Example 11 ===")
    # Fit an ellipse through points (2,2) and (1,4)
    p1 = (2, 2)
    p2 = (1, 4)
    a_fit, b_fit = EllipseTheory.fit_ellipse_through_points(p1, p2)
    a_fit, b_fit = float(a_fit), float(b_fit)
    print(f"Fitted ellipse: a = {a_fit:.3f}, b = {b_fit:.3f}")
    
    plt.figure(figsize=(6,6))
    theta = np.linspace(0, 2*np.pi, 400)
    x_fit = a_fit * np.cos(theta)
    y_fit = b_fit * np.sin(theta)
    plt.plot(x_fit, y_fit, 'b-', label="Fitted ellipse")
    plt.plot(p1[0], p1[1], 'ro', markersize=8, label="Point (2,2)")
    plt.plot(p2[0], p2[1], 'mo', markersize=8, label="Point (1,4)")
    plt.title("Example 11: Ellipse Through (2,2) and (1,4)")
    plt.xlabel("x"); plt.ylabel("y")
    plt.legend()
    plt.grid(True)
    plt.axis("equal")
    plt.show()
    
    # ------- Example 12 -------
    print("\n=== Example 12 ===")
    # Given minor axis length = 4 (so b = 2) and focal separation = 2.
    b_ex12 = 2
    focal_distance_ex12 = 2
    a_ex12, b_ex12, e_ex12 = EllipseTheory.ellipse_from_minor_and_focal(b_ex12, focal_distance_ex12)
    print(f"Ellipse: a = {a_ex12:.3f}, b = {b_ex12:.3f}, eccentricity e = {e_ex12:.3f}")
    
    plt.figure(figsize=(6,6))
    theta = np.linspace(0, 2*np.pi, 400)
    x_ex12 = a_ex12 * np.cos(theta)
    y_ex12 = b_ex12 * np.sin(theta)
    plt.plot(x_ex12, y_ex12, 'b-', label="Example 12 Ellipse")
    # Mark the foci (at ±(a*e, 0))
    plt.plot(a_ex12 * e_ex12, 0, 'ro', label="Focus")
    plt.plot(-a_ex12 * e_ex12, 0, 'ro')
    plt.title("Example 12: Ellipse from minor axis & focal separation")
    plt.xlabel("x"); plt.ylabel("y")
    plt.legend()
    plt.grid(True)
    plt.axis("equal")
    plt.show()
    
    # ------- Example 13 -------
    print("\n=== Example 13 ===")
    # Given latus rectum L = 3 and eccentricity e = 1/√2.
    L_ex13 = 3
    e_ex13 = 1 / np.sqrt(2)
    a_ex13, b_ex13, _ = EllipseTheory.ellipse_from_latus_and_ecc(L_ex13, e_ex13)
    print(f"Ellipse: a = {a_ex13:.3f}, b = {b_ex13:.3f}, e = {e_ex13:.3f}")
    
    plt.figure(figsize=(6,6))
    theta = np.linspace(0, 2*np.pi, 400)
    x_ex13 = a_ex13 * np.cos(theta)
    y_ex13 = b_ex13 * np.sin(theta)
    plt.plot(x_ex13, y_ex13, 'b-', label="Example 13 Ellipse")
    plt.title("Example 13: Ellipse from Latus rectum and e")
    plt.xlabel("x"); plt.ylabel("y")
    plt.legend()
    plt.grid(True)
    plt.axis("equal")
    plt.show()
    
    # ------- Example 14 -------
    print("\n=== Example 14 ===")
    # If the vectors from the focus to the minor-axis endpoint are perpendicular then e = 1/√2.
    # Given major axis: 2a = 2√2, so a = √2.
    a_ex14 = np.sqrt(2)
    a_ex14, b_ex14, e_ex14 = EllipseTheory.ellipse_from_focal_perp(a_ex14)
    print(f"Ellipse: a = {a_ex14:.3f}, b = {b_ex14:.3f}, e = {e_ex14:.3f}")
    
    plt.figure(figsize=(6,6))
    theta = np.linspace(0, 2*np.pi, 400)
    x_ex14 = a_ex14 * np.cos(theta)
    y_ex14 = b_ex14 * np.sin(theta)
    plt.plot(x_ex14, y_ex14, 'b-', label="Example 14 Ellipse")
    # Mark the focus and minor-axis endpoint.
    focus_ex14 = (a_ex14 * e_ex14, 0)
    plt.plot(focus_ex14[0], focus_ex14[1], 'ro', label="Focus")
    plt.plot(0, b_ex14, 'go', label="Minor-axis endpoint")
    plt.title("Example 14: Ellipse from foci-perpendicular condition")
    plt.xlabel("x"); plt.ylabel("y")
    plt.legend()
    plt.grid(True)
    plt.axis("equal")
    plt.show()
    
    # ------- Example 15 -------
    print("\n=== Example 15 ===")
    # Verify the rational parametrization: x = a(1-t²)/(1+t²), y = 2b*t/(1+t²)
    a_ex15, b_ex15 = 3, 2
    expr_check = EllipseTheory.verify_rational_parametrization(a_ex15, b_ex15)
    print("Verification (should equal 1):", expr_check)
    
    t_vals = np.linspace(-10, 10, 400)
    x_rat = a_ex15 * (1 - t_vals**2) / (1 + t_vals**2)
    y_rat = 2 * b_ex15 * t_vals / (1 + t_vals**2)
    # Standard parametric form for the ellipse:
    theta_std = np.linspace(0, 2*np.pi, 400)
    x_std = a_ex15 * np.cos(theta_std)
    y_std = b_ex15 * np.sin(theta_std)
    
    plt.figure(figsize=(6,6))
    plt.plot(x_std, y_std, 'b--', label="Standard Parametrization")
    plt.plot(x_rat, y_rat, 'r-', label="Rational Parametrization")
    plt.title("Example 15: Comparison of parametrizations")
    plt.xlabel("x"); plt.ylabel("y")
    plt.legend()
    plt.grid(True)
    plt.axis("equal")
    plt.show()